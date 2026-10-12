#!/usr/bin/env python3
"""Local checks. No network and no key."""

from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import bridge


def git(repo: str, *args: str) -> str:
    env = os.environ.copy()
    env["TZ"] = "Asia/Kuala_Lumpur"
    run = subprocess.run(["git", "-C", repo, *args], check=True, capture_output=True, env=env)
    return run.stdout.decode()


def init_repo() -> str:
    repo = tempfile.mkdtemp(prefix="bridge-")
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "t@example.com")
    git(repo, "config", "user.name", "Tester")
    return repo


def commit_file(repo: str, path: str, text: str, when: str) -> str:
    full = Path(repo) / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(text, encoding="utf-8")
    git(repo, "add", "--", path)
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = when
    env["GIT_COMMITTER_DATE"] = when
    subprocess.run(
        ["git", "-C", repo, "commit", "-q", "-m", path],
        check=True,
        env=env,
    )
    return git(repo, "rev-parse", "HEAD").strip()


class Pure(unittest.TestCase):
    def test_path_rules(self):
        bridge.check_path("PT005", "PT005/hesper/a.md")
        bridge.check_path("PT006", "PT006/hesper/2026-10-12T1200-astra-note.md")
        for path in ("PT006/hesper/a.md", "PT005/../PT006/a.md", "/PT005/a.md", "PT005/a/../../x.md"):
            with self.assertRaises(bridge.BridgeError):
                bridge.check_path("PT005", path)

    def test_slip_posts_only_post_section(self):
        text = """
TABLE: PT005
RELEASE_UP_TO: 0123456789abcdef0123456789abcdef01234567
RELEASED_BY: Opus, with Tuzi's OK at 22:10
POST:
0123456789abcdef0123456789abcdef01234567 PT005/hesper/a.md
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa PT005/opus/n.md REDACT
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb PT005/opus/PT005-LEDGER.md SPLIT
cccccccccccccccccccccccccccccccccccccccc PT005/hesper/b.md REDACT SPLIT
HOLD:
dddddddddddddddddddddddddddddddddddddddd PT005/hesper/no.md block word
SKIP:
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee PT005/bill/x.md code
"""
        slip = bridge.parse_release(text, "PT005")
        self.assertEqual([item.path for item in slip.posts], [
            "PT005/hesper/a.md",
            "PT005/opus/n.md",
            "PT005/opus/PT005-LEDGER.md",
            "PT005/hesper/b.md",
        ])
        self.assertEqual([item.redact for item in slip.posts], [False, True, False, True])
        self.assertEqual([item.split for item in slip.posts], [False, False, True, True])
        with self.assertRaises(bridge.BridgeError):
            bridge.parse_release(text.replace("TABLE: PT005", "TABLE: PT006"), "PT005")

    def test_unknown_flag_is_refused(self):
        text = (
            "TABLE: PT005\nRELEASE_UP_TO: 0123456789abcdef0123456789abcdef01234567\n"
            "POST:\n0123456789abcdef0123456789abcdef01234567 PT005/hesper/a.md HOLD\n"
        )
        with self.assertRaises(bridge.BridgeError):
            bridge.parse_release(text, "PT005")

    def test_redact_every_email_including_the_footer(self):
        raw = "write theadventuresoftuzi@gmail.com and Seat: a.b@c.de please\n"
        text, count = bridge.redact_emails(raw)
        self.assertEqual(count, 2)
        self.assertNotIn("@", text)
        self.assertEqual(text.count("[已遮蔽]"), 2)

    def test_block_word_is_not_this_program(self):
        self.assertIn("token", "a token and password stay")
        text, count = bridge.redact_emails("a token and password stay\n")
        self.assertEqual(count, 0)
        self.assertIn("token", text)

    def test_corrects_and_as_of(self):
        raw = "BEGIN\nAS_OF: 2026-10-12 12:15 +08\nCORRECTS: proof-table-005-163\nEND\n"
        self.assertEqual(bridge.corrects_of(raw, "PT005"), "proof-table-005-163")
        self.assertEqual(bridge.header_value(raw, "AS_OF"), "2026-10-12 12:15 +08")
        with self.assertRaises(bridge.BridgeError):
            bridge.corrects_of("CORRECTS: proof-table-006-1\n", "PT005")

    def test_first_line_shapes(self):
        base = bridge.first_line(
            as_of="2026-10-12 12:15 +08",
            commit="a" * 40,
            when="2026-10-12 12:16:01 +0800",
            path="PT005/hesper/a.md",
            revision=False,
            redactions=None,
            part=None,
        )
        self.assertEqual(
            base,
            f"原收到時間 2026-10-12 12:15 +08 · 信箱提交 {'a'*40} 2026-10-12 12:16:01 +0800 · PT005/hesper/a.md",
        )
        edited = bridge.first_line(
            as_of="2026-10-12 12:15 +08",
            commit="b" * 40,
            when="2026-10-12 12:20:00 +0800",
            path="PT005/opus/PT005-LEDGER.md",
            revision=True,
            redactions=3,
            part=(2, 4, 20000, 35000),
        )
        self.assertTrue(edited.startswith("修改版 · 原收到時間 "))
        self.assertIn(" · part 2/4 · offset 20000-35000 · 自動遮蔽 3 處", edited)

    def test_split_rejoins_on_line_starts(self):
        body = ("line\n" * 8000)
        self.assertGreater(len(body), bridge.LIMIT)

        def one():
            return "H" * 80

        def sized(start, end):
            return "H" * 80 + f" · part 999/999 · offset {start}-{end}"

        spans = bridge.plan_spans(body, one(), sized, True)
        self.assertGreater(len(spans), 1)
        self.assertEqual("".join(body[a:b] for a, b in spans), body)
        for start, end in spans[1:]:
            self.assertEqual(body[start - 1], "\n")
        for start, end in spans:
            header = "H" * 40
            self.assertLessEqual(bridge.utf16_len(header + "\n" + body[start:end]), bridge.LIMIT)

    def test_hard_split_states_the_offset(self):
        body = "x" * 25000
        spans = bridge.plan_spans(body, "H" * 40, lambda s, e: "H" * 60 + f"{s}-{e}", True)
        self.assertGreater(len(spans), 1)
        self.assertEqual("".join(body[a:b] for a, b in spans), body)
        self.assertNotEqual(spans[0][1], body.find("\n") + 1)

    def test_no_split_flag_refuses_a_long_file(self):
        with self.assertRaises(bridge.BridgeError):
            bridge.plan_spans("y" * 20001, "H", lambda s, e: "H", False)

    def test_speaker(self):
        self.assertEqual(bridge.line_type_for("PT005", "PT005/opus/n.md"), ("chair_note", "Opus"))
        self.assertEqual(bridge.line_type_for("PT006", "PT006/hesper/a.md"), ("courier_note", "Hesper"))
        self.assertEqual(bridge.line_type_for("PT005", "PT005/puck/a.md"), ("courier_note", "Hesper"))

    def test_parts_rejoin_under_the_real_first_line(self):
        body = "abc\n" * 7000
        item = bridge.PostItem("c" * 40, "PT005/hesper/a.md", False, True, 0)
        built = bridge.build_parts(body, item, "2026-10-12 10:00 +08", "2026-10-12 10:00:01 +0800", False, None)
        self.assertGreater(len(built), 1)
        pieces = []
        for part, parts, text in built:
            head, rest = text.split("\n", 1)
            self.assertIn(f" · part {part}/{parts} · offset ", head)
            self.assertLessEqual(bridge.utf16_len(text), bridge.LIMIT)
            pieces.append(rest)
        self.assertEqual("".join(pieces), body)


class Repo(unittest.TestCase):
    def setUp(self):
        self.repo = init_repo()

    def tearDown(self):
        shutil.rmtree(self.repo)

    def slip(self, tip: str, posts: list[str]) -> None:
        path = Path(self.repo) / "PT005/bridge/RELEASE"
        path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "TABLE: PT005",
            f"RELEASE_UP_TO: {tip}",
            "RELEASED_BY: Opus, with Tuzi's OK at 22:10",
            "POST:",
            *posts,
            "HOLD:",
            f"{'d'*40} PT005/hesper/held.md a reason",
        ]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def test_posts_in_commit_order_and_does_not_repeat(self):
        early = commit_file(
            self.repo,
            "PT005/hesper/note.md",
            "BEGIN\nAS_OF: 2026-10-12 10:00 +08\nCORRECTS: proof-table-005-163\nhello a@b.cd\n",
            "2026-10-12T02:00:00+0800",
        )
        later = commit_file(
            self.repo,
            "PT005/opus/note.md",
            "BEGIN\nAS_OF: 2026-10-12 11:00 +08\ntoken stays\n",
            "2026-10-12T03:00:00+0800",
        )
        # Slip lists the later commit first. The bridge still posts the earlier commit first.
        self.slip(
            later,
            [
                f"{later} PT005/opus/note.md",
                f"{early} PT005/hesper/note.md REDACT",
            ],
        )
        calls = []

        def poster(origin, table, key, payload):
            calls.append(payload)
            return f"proof-table-005-{100+len(calls)}"

        notes = bridge.process_table(
            self.repo, "PT005", key="not-a-real-key", plan_only=False, push=False, poster=poster, wall=[]
        )
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0]["line_type"], "courier_note")
        self.assertEqual(calls[0]["speaker"], "Hesper")
        self.assertEqual(calls[0]["carried_by"], "Hesper")
        self.assertIsNone(calls[0]["relay"])
        self.assertEqual(calls[0]["corrects"], "proof-table-005-163")
        self.assertNotIn("a@b.cd", calls[0]["text"])
        self.assertIn("自動遮蔽 1 處", calls[0]["text"].split("\n", 1)[0])
        self.assertIn("2026-10-12 10:00 +08", calls[0]["text"])
        self.assertIn(" +0800 · PT005/hesper/note.md", calls[0]["text"].split("\n", 1)[0])
        self.assertEqual(calls[1]["line_type"], "chair_note")
        self.assertEqual(calls[1]["speaker"], "Opus")
        self.assertIsNone(calls[1]["corrects"])
        self.assertIn("token stays", calls[1]["text"])
        self.assertTrue(calls[0]["text"].split("信箱提交 ", 1)[1].startswith(early))
        posted = (Path(self.repo) / "PT005/bridge/posted.tsv").read_text(encoding="utf-8")
        self.assertIn(early, posted)
        self.assertIn(later, posted)
        manifest = list((Path(self.repo) / "PT005/bridge").glob("*-manifest.tsv"))
        self.assertEqual(len(manifest), 1)
        body = manifest[0].read_text(encoding="utf-8")
        self.assertIn("wall_lines", body)
        again = bridge.process_table(
            self.repo, "PT005", key="not-a-real-key", plan_only=False, push=False, poster=poster, wall=[]
        )
        self.assertEqual(len(calls), 2)
        self.assertTrue(any("skip already posted" in note for note in again))
        self.assertTrue(notes)

    def test_revision_and_pause_and_outside_path(self):
        first = commit_file(self.repo, "PT005/opus/PT005-LEDGER.md", "L1\n", "2026-10-12T04:00:00+0800")
        second = commit_file(self.repo, "PT005/opus/PT005-LEDGER.md", "L1\nL2\n", "2026-10-12T05:00:00+0800")
        self.slip(second, [f"{first} PT005/opus/PT005-LEDGER.md", f"{second} PT005/opus/PT005-LEDGER.md"])
        calls = []

        def poster(origin, table, key, payload):
            calls.append(payload["text"].split("\n", 1)[0])
            return f"proof-table-005-{len(calls)}"

        bridge.process_table(self.repo, "PT005", key="k", push=False, poster=poster, wall=[])
        self.assertFalse(calls[0].startswith("修改版"))
        self.assertTrue(calls[1].startswith("修改版"))
        pause = Path(self.repo) / "PT005/bridge/PAUSE"
        pause.write_text("\n", encoding="utf-8")
        notes = bridge.process_table(self.repo, "PT005", key="k", push=False, poster=poster, wall=[])
        self.assertIn("PAUSE", notes[0])
        self.assertEqual(len(calls), 2)
        pause.unlink()
        outside = commit_file(self.repo, "PT006/hesper/x.md", "no\n", "2026-10-12T06:00:00+0800")
        self.slip(outside, [f"{outside} PT006/hesper/x.md"])
        with self.assertRaises(bridge.BridgeError):
            bridge.process_table(self.repo, "PT005", key="k", push=False, poster=poster, wall=[])

    def test_wall_hit_is_not_posted_twice(self):
        commit = commit_file(self.repo, "PT005/hesper/a.md", "AS_OF: 2026-10-12 01:00 +08\nbody\n", "2026-10-12T01:00:00+0800")
        self.slip(commit, [f"{commit} PT005/hesper/a.md"])
        calls = []

        def poster(origin, table, key, payload):
            calls.append(payload)
            return "proof-table-005-9"

        bridge.process_table(self.repo, "PT005", key="k", push=False, poster=poster, wall=[])
        text = calls[0]["text"]
        wall = [{"id": "proof-table-005-9", "text": text}]
        (Path(self.repo) / "PT005/bridge/posted.tsv").unlink()
        calls.clear()
        bridge.process_table(self.repo, "PT005", key="k", push=False, poster=poster, wall=wall)
        self.assertEqual(calls, [])
        posted = (Path(self.repo) / "PT005/bridge/posted.tsv").read_text(encoding="utf-8")
        self.assertIn("proof-table-005-9", posted)
        self.assertIn(hashlib.sha256(text.encode()).hexdigest(), posted)

    def test_missing_key_posts_nothing(self):
        commit = commit_file(self.repo, "PT005/hesper/a.md", "hi\n", "2026-10-12T01:00:00+0800")
        self.slip(commit, [f"{commit} PT005/hesper/a.md"])
        with self.assertRaises(bridge.BridgeError):
            bridge.process_table(self.repo, "PT005", key="", push=False, poster=lambda *a: "x", wall=[])
        self.assertFalse((Path(self.repo) / "PT005/bridge/posted.tsv").exists())


class Tree(unittest.TestCase):
    def test_workflow_names_the_secret_and_does_not_contain_one(self):
        workflow = Path(__file__).resolve().parents[2].joinpath(".github/workflows/wall-bridge.yml")
        text = workflow.read_text(encoding="utf-8")
        self.assertIn("secrets.PLAY_BRIDGE_KEY", text)
        self.assertNotIn("x-play-courier-key:", text)


if __name__ == "__main__":
    unittest.main()
