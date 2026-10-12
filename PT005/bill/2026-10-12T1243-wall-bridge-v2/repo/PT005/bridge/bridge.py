#!/usr/bin/env python3
"""Release-gated wall bridge. Posts only the POST lines of a chair release slip.

No whitelist and no block-word check. The slip decides. This file refuses a path
outside that slip's table folder, adds the first line, and applies REDACT / SPLIT
when the slip says so. It does not choose what is worth posting.

Not installed while it lives under PT005/bill/. GitHub runs a workflow only from
the repository root .github/workflows/.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

ORIGIN = "https://play.civilisationfield.com"
LIMIT = 20_000
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}")
COMMIT = re.compile(r"^[0-9a-f]{40}$")
TABLES = {"PT005": "proof-table-005", "PT006": "proof-table-006"}


class BridgeError(Exception):
    pass


@dataclass
class PostItem:
    commit: str
    path: str
    redact: bool
    split: bool
    index: int


@dataclass
class Slip:
    table: str
    release_up_to: str
    released_by: str
    posts: list[PostItem] = field(default_factory=list)


@dataclass
class Posted:
    commit: str
    path: str
    part: int
    parts: int
    wall_line: str
    sha256: str
    redactions: int


def utf16_len(text: str) -> int:
    """Match the wall API, which measures JavaScript string length."""
    return sum(2 if ord(ch) > 0xFFFF else 1 for ch in text)


def normalize(text: str) -> str:
    """Same two edits the wall's keep() applies, so the stored text matches."""
    return text.replace("\x00", "").replace("\r\n", "\n")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def check_path(table: str, path: str) -> None:
    if not path or path.startswith("/") or "\\" in path or ".." in path.split("/"):
        raise BridgeError(f"path refused: {path}")
    if path != os.path.normpath(path):
        raise BridgeError(f"path refused: {path}")
    prefix = table + "/"
    if not path.startswith(prefix):
        raise BridgeError(f"path is outside {table}/: {path}")


def parse_release(text: str, expect_table: str) -> Slip:
    table = ""
    release_up_to = ""
    released_by = ""
    section = ""
    posts: list[PostItem] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("TABLE:"):
            table = line.split(":", 1)[1].strip()
            continue
        if line.startswith("RELEASE_UP_TO:"):
            release_up_to = line.split(":", 1)[1].strip()
            continue
        if line.startswith("RELEASED_BY:"):
            released_by = line.split(":", 1)[1].strip()
            continue
        if line in ("POST:", "HOLD:", "SKIP:"):
            section = line[:-1]
            continue
        if section != "POST":
            continue
        bits = line.split()
        if len(bits) < 2 or not COMMIT.fullmatch(bits[0]):
            raise BridgeError(f"bad POST line: {line}")
        flags = bits[2:]
        unknown = [flag for flag in flags if flag not in ("REDACT", "SPLIT")]
        if unknown:
            raise BridgeError(f"bad POST flag: {' '.join(unknown)}")
        posts.append(
            PostItem(
                commit=bits[0],
                path=bits[1],
                redact="REDACT" in flags,
                split="SPLIT" in flags,
                index=len(posts),
            )
        )
    if table != expect_table:
        raise BridgeError(f"{expect_table}/bridge/RELEASE says TABLE: {table or 'none'}")
    if not COMMIT.fullmatch(release_up_to):
        raise BridgeError("RELEASE_UP_TO must be a full commit hash")
    return Slip(table=table, release_up_to=release_up_to, released_by=released_by, posts=posts)


def header_value(text: str, name: str) -> str | None:
    head = "\n".join(text.splitlines()[:40])
    found = re.search(rf"(?m)^{name}:\s*(.+?)\s*$", head)
    if found:
        return found.group(1).strip()
    inline = re.search(rf"{name}:\s*([^·\n]+)", head)
    if inline:
        return inline.group(1).strip()
    return None


def corrects_of(text: str, table: str) -> str | None:
    raw = header_value(text, "CORRECTS")
    if raw is None:
        return None
    slug = TABLES[table]
    if not re.fullmatch(rf"{slug}-\d+", raw):
        raise BridgeError(f"CORRECTS must be {slug}-<n>, not {raw}")
    return raw


def redact_emails(text: str) -> tuple[str, int]:
    count = 0

    def swap(_match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return "[已遮蔽]"

    return EMAIL.sub(swap, text), count


def first_line(
    *,
    as_of: str,
    commit: str,
    when: str,
    path: str,
    revision: bool,
    redactions: int | None,
    part: tuple[int, int, int, int] | None,
) -> str:
    bits = []
    if revision:
        bits.append("修改版")
    bits.append(f"原收到時間 {as_of}")
    bits.append(f"信箱提交 {commit} {when}")
    bits.append(path)
    line = " · ".join(bits)
    if part is not None:
        k, n, start, end = part
        line += f" · part {k}/{n} · offset {start}-{end}"
    if redactions is not None:
        line += f" · 自動遮蔽 {redactions} 處"
    return line


def _fits(header: str, body: str) -> bool:
    return utf16_len(header) + utf16_len("\n") + utf16_len(body) <= LIMIT


def plan_spans(body: str, one_header: str, split_header, allow_split: bool) -> list[tuple[int, int]]:
    """Return [start, end) code-point spans. End is exclusive. Spans join back to body."""
    if _fits(one_header, body):
        return [(0, len(body))]
    if not allow_split:
        raise BridgeError(f"over {LIMIT} characters and the slip does not say SPLIT")
    spans: list[tuple[int, int]] = []
    i = 0
    n = len(body)
    while i < n:
        cands: list[int] = []
        j = i
        while True:
            nl = body.find("\n", j)
            if nl == -1:
                cands.append(n)
                break
            cands.append(nl + 1)
            j = nl + 1
        best: int | None = None
        for end in cands:
            if end <= i:
                continue
            if _fits(split_header(i, end), body[i:end]):
                best = end
            else:
                break
        if best is None:
            lo, hi = i + 1, n
            fit: int | None = None
            while lo <= hi:
                mid = (lo + hi) // 2
                if _fits(split_header(i, mid), body[i:mid]):
                    fit = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            if fit is None:
                raise BridgeError("the first line does not fit in 20000 characters")
            best = fit
        spans.append((i, best))
        i = best
    return spans


def line_type_for(table: str, path: str) -> tuple[str, str]:
    if path.startswith(f"{table}/opus/"):
        return "chair_note", "Opus"
    return "courier_note", "Hesper"


def path_in_first(first: str, path: str) -> bool:
    token = f" · {path}"
    at = first.find(token)
    if at < 0:
        return False
    after = first[at + len(token) :]
    return after == "" or after.startswith(" · ")


def wall_hit(lines: list[dict], commit: str, path: str, part: int, parts: int) -> dict | None:
    needle = f"信箱提交 {commit} "
    mark = f" · part {part}/{parts} · "
    for line in lines:
        text = str(line.get("text") or "")
        first = text.split("\n", 1)[0]
        if needle not in first or not path_in_first(first, path):
            continue
        has = " · part " in first
        if parts > 1 and mark not in first:
            continue
        if parts == 1 and has:
            continue
        return line
    return None


def git(repo: str, *args: str, env: dict | None = None) -> str:
    run = subprocess.run(
        ["git", "-C", repo, *args],
        check=False,
        capture_output=True,
        env=env,
    )
    if run.returncode != 0:
        err = run.stderr.decode("utf-8", "replace").strip()
        raise BridgeError(err or f"git {' '.join(args)} failed")
    return run.stdout.decode("utf-8")


def commit_time(repo: str, commit: str) -> str:
    env = os.environ.copy()
    env["TZ"] = "Asia/Kuala_Lumpur"
    text = git(repo, "show", "-s", "--format=%cd", "--date=format-local:%Y-%m-%d %H:%M:%S %z", commit, env=env)
    return text.strip()


def commit_unix(repo: str, commit: str) -> int:
    return int(git(repo, "show", "-s", "--format=%ct", commit).strip())


def is_ancestor(repo: str, commit: str, tip: str) -> bool:
    if commit == tip:
        return True
    run = subprocess.run(
        ["git", "-C", repo, "merge-base", "--is-ancestor", commit, tip],
        check=False,
        capture_output=True,
    )
    return run.returncode == 0


def blob(repo: str, commit: str, path: str) -> str:
    run = subprocess.run(
        ["git", "-C", repo, "show", f"{commit}:{path}"],
        check=False,
        capture_output=True,
    )
    if run.returncode != 0:
        raise BridgeError(f"no file {commit}:{path}")
    try:
        return run.stdout.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise BridgeError(f"not utf-8: {path}") from exc


def read_posted(path: str) -> list[Posted]:
    if not os.path.exists(path):
        return []
    rows: list[Posted] = []
    with open(path, encoding="utf-8") as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            if not line or line.startswith("commit\t"):
                continue
            bits = line.split("\t")
            if len(bits) != 7:
                raise BridgeError(f"bad posted.tsv row: {line}")
            rows.append(
                Posted(
                    commit=bits[0],
                    path=bits[1],
                    part=int(bits[2]),
                    parts=int(bits[3]),
                    wall_line=bits[4],
                    sha256=bits[5],
                    redactions=int(bits[6]),
                )
            )
    return rows


def append_tsv(path: str, header: str, rows: list[str]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as handle:
        if new:
            handle.write(header + "\n")
        for row in rows:
            handle.write(row + "\n")


def post_line(origin: str, table: str, key: str, payload: dict) -> str:
    slug = TABLES[table]
    url = f"{origin}/api/gathering/{slug}/lines"
    data = json.dumps(payload).encode("utf-8")

    def once() -> str:
        req = urllib.request.Request(
            url,
            data=data,
            method="POST",
            headers={"content-type": "application/json", "x-play-courier-key": key},
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:400]
            raise BridgeError(f"wall {exc.code}: {detail}") from exc
        line = body.get("line") or {}
        ident = line.get("id")
        if not ident:
            raise BridgeError("wall reply had no line id")
        return str(ident)

    try:
        return once()
    except BridgeError as exc:
        if str(exc).startswith("wall 409:"):
            return once()
        raise


def fetch_wall(origin: str, table: str) -> list[dict]:
    slug = TABLES[table]
    url = f"{origin}/api/gathering/{slug}/lines"
    with urllib.request.urlopen(url, timeout=90) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return list(body.get("lines") or [])


def build_parts(body: str, item: PostItem, as_of: str, when: str, revision: bool, redactions: int | None):
    def one_header() -> str:
        return first_line(
            as_of=as_of,
            commit=item.commit,
            when=when,
            path=item.path,
            revision=revision,
            redactions=redactions,
            part=None,
        )

    def sized(start: int, end: int) -> str:
        return first_line(
            as_of=as_of,
            commit=item.commit,
            when=when,
            path=item.path,
            revision=revision,
            redactions=redactions,
            part=(999, 999, start, end),
        )

    spans = plan_spans(body, one_header(), sized, item.split)
    parts = len(spans)
    built = []
    for index, (start, end) in enumerate(spans, start=1):
        part = None if parts == 1 else (index, parts, start, end)
        header = first_line(
            as_of=as_of,
            commit=item.commit,
            when=when,
            path=item.path,
            revision=revision,
            redactions=redactions,
            part=part,
        )
        text = header + "\n" + body[start:end]
        if utf16_len(text) > LIMIT:
            raise BridgeError(f"part {index} is over {LIMIT} after the real first line")
        built.append((index, parts, text))
    joined = "".join(body[start:end] for start, end in spans)
    if joined != body:
        raise BridgeError("split did not rejoin")
    return built


def changed_tables(repo: str) -> list[str]:
    event = os.environ.get("GITHUB_EVENT_NAME") or ""
    before = os.environ.get("EVENT_BEFORE") or os.environ.get("GITHUB_EVENT_BEFORE") or ""
    sha = os.environ.get("GITHUB_SHA") or "HEAD"
    if event == "workflow_dispatch" or not before or set(before) == {"0"}:
        return ["PT005", "PT006"]
    names = git(repo, "diff", "--name-only", before, sha).splitlines()
    found = []
    for table in ("PT005", "PT006"):
        if f"{table}/bridge/RELEASE" in names or f"{table}/bridge/PAUSE" in names:
            found.append(table)
    return found


def manifest_path(repo: str, table: str) -> str:
    env = os.environ.copy()
    env["TZ"] = "Asia/Kuala_Lumpur"
    day = subprocess.check_output(["date", "+%Y-%m-%d"], env=env).decode().strip()
    return os.path.join(repo, table, "bridge", f"{day}-manifest.tsv")


def process_table(
    repo: str,
    table: str,
    *,
    origin: str = ORIGIN,
    key: str = "",
    plan_only: bool = False,
    push: bool = False,
    poster=post_line,
    wall: list[dict] | None = None,
) -> list[str]:
    """Post one table's slip. Returns human-readable notes. Raises BridgeError on a bad slip."""
    release_path = os.path.join(repo, table, "bridge", "RELEASE")
    if not os.path.exists(release_path):
        return [f"{table}: no RELEASE"]
    if os.path.exists(os.path.join(repo, table, "bridge", "PAUSE")):
        return [f"{table}: PAUSE, nothing posted"]
    slip = parse_release(Path(release_path).read_text(encoding="utf-8"), table)
    if not slip.posts:
        return [f"{table}: POST is empty"]
    notes: list[str] = []
    state_path = os.path.join(repo, table, "bridge", "posted.tsv")
    posted = read_posted(state_path)
    have = {(row.commit, row.path, row.part) for row in posted}
    order = sorted(slip.posts, key=lambda item: (commit_unix(repo, item.commit), item.index))
    new_posted: list[str] = []
    new_manifest: list[str] = []
    if wall is None and not plan_only:
        wall = fetch_wall(origin, table)
    wall = wall or []

    for item in order:
        check_path(table, item.path)
        if not is_ancestor(repo, item.commit, slip.release_up_to):
            raise BridgeError(f"{item.commit} is not at or before RELEASE_UP_TO")
        raw = normalize(blob(repo, item.commit, item.path))
        corrects = corrects_of(raw, table)
        body = raw
        redactions: int | None = None
        if item.redact:
            body, count = redact_emails(raw)
            redactions = count
        as_of = header_value(raw, "AS_OF") or commit_time(repo, item.commit)
        if item.redact:
            as_of, _ignored = redact_emails(as_of)
        when = commit_time(repo, item.commit)
        revision = any(row.path == item.path and row.commit != item.commit for row in posted)
        built = build_parts(body, item, as_of, when, revision, redactions)
        line_type, speaker = line_type_for(table, item.path)
        for part, parts, text in built:
            if (item.commit, item.path, part) in have:
                notes.append(f"skip already posted {item.path} part {part}")
                continue
            hit = wall_hit(wall, item.commit, item.path, part, parts)
            if plan_only:
                if hit is not None:
                    notes.append(f"already on the wall {hit.get('id')} {item.path} part {part}")
                else:
                    notes.append(
                        f"would post {line_type} {speaker} {item.path} part {part}/{parts} {sha256_text(text)[:12]}"
                    )
                continue
            if hit is not None:
                wall_id = str(hit["id"])
                digest = sha256_text(str(hit.get("text") or ""))
                notes.append(f"already on the wall {wall_id} {item.path} part {part}")
            else:
                if not key:
                    raise BridgeError("PLAY_BRIDGE_KEY is not set")
                payload = {
                    "line_type": line_type,
                    "speaker": speaker,
                    "carried_by": "Hesper",
                    "relay": None,
                    "text": text,
                    "corrects": corrects,
                }
                wall_id = poster(origin, table, key, payload)
                digest = sha256_text(text)
                notes.append(f"posted {wall_id} {item.path} part {part}/{parts}")
            row = Posted(
                commit=item.commit,
                path=item.path,
                part=part,
                parts=parts,
                wall_line=wall_id,
                sha256=digest,
                redactions=0 if redactions is None else redactions,
            )
            posted.append(row)
            have.add((item.commit, item.path, part))
            new_posted.append(
                "\t".join(
                    [
                        row.commit,
                        row.path,
                        str(row.part),
                        str(row.parts),
                        row.wall_line,
                        row.sha256,
                        str(row.redactions),
                    ]
                )
            )
            new_manifest.append("\t".join([row.commit, row.path, row.wall_line, row.sha256, str(row.redactions)]))

    if new_posted and not plan_only:
        append_tsv(
            state_path,
            "commit\tpath\tpart\tparts\twall_line\tsha256\tredactions",
            new_posted,
        )
        append_tsv(
            manifest_path(repo, table),
            "commit\tpath\twall_lines\tsha256\tredactions",
            new_manifest,
        )
        if push:
            publish(repo, [state_path, manifest_path(repo, table)], f"bridge: {table} manifest")
    return notes


def publish(repo: str, files: list[str], message: str) -> None:
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = "Bridge"
    env["GIT_AUTHOR_EMAIL"] = "bridge@play.local"
    env["GIT_COMMITTER_NAME"] = "Bridge"
    env["GIT_COMMITTER_EMAIL"] = "bridge@play.local"
    git(repo, "add", "--", *files, env=env)
    git(repo, "commit", "-m", message, env=env)
    git(repo, "fetch", "origin", "main", env=env)
    git(repo, "rebase", "origin/main", env=env)
    git(repo, "push", "origin", "HEAD:main", env=env)


def main(argv: list[str]) -> int:
    plan_only = "--plan" in argv
    repo = os.environ.get("BRIDGE_REPO") or git(os.getcwd(), "rev-parse", "--show-toplevel").strip()
    if "--plan" in argv:
        os.environ["GITHUB_EVENT_NAME"] = os.environ.get("GITHUB_EVENT_NAME") or "workflow_dispatch"
    tables = changed_tables(repo)
    key = os.environ.get("PLAY_BRIDGE_KEY", "")
    failed = False
    for table in tables:
        try:
            for note in process_table(repo, table, key=key, plan_only=plan_only, push=not plan_only):
                print(note)
        except BridgeError as exc:
            print(f"{table}: {exc}", file=sys.stderr)
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
