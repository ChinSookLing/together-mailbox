#!/usr/bin/env python3
"""Morning check. Read a manifest and the public wall. No key. Posts nothing.

    python3 PT005/bridge/audit.py PT005 PT005/bridge/2026-10-12-manifest.tsv
"""

from __future__ import annotations

import hashlib
import json
import sys
import urllib.request

WALL = {
    "PT005": "https://play.civilisationfield.com/api/gathering/proof-table-005/lines",
    "PT006": "https://play.civilisationfield.com/api/gathering/proof-table-006/lines",
}


def load_manifest(path: str) -> list[dict]:
    rows = []
    with open(path, encoding="utf-8") as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            if not line or line.startswith("commit\t"):
                continue
            commit, path, wall_line, digest, redactions = line.split("\t")
            rows.append(
                {
                    "commit": commit,
                    "path": path,
                    "wall_line": wall_line,
                    "sha256": digest,
                    "redactions": redactions,
                }
            )
    return rows


def main(argv: list[str]) -> int:
    if len(argv) != 3 or argv[1] not in WALL:
        print("usage: audit.py PT005|PT006 <manifest.tsv>", file=sys.stderr)
        return 2
    table, path = argv[1], argv[2]
    with urllib.request.urlopen(WALL[table], timeout=90) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    by_id = {str(line["id"]): str(line.get("text") or "") for line in body.get("lines") or []}
    failed = 0
    for row in load_manifest(path):
        text = by_id.get(row["wall_line"])
        if text is None:
            print(f"FAIL missing {row['wall_line']} {row['path']}")
            failed += 1
            continue
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if digest != row["sha256"]:
            print(f"FAIL sha256 {row['wall_line']} {row['path']}")
            failed += 1
            continue
        print(f"OK {row['wall_line']} {row['path']}")
    if failed:
        print(f"{failed} failed")
        return 1
    print("audit ok")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
