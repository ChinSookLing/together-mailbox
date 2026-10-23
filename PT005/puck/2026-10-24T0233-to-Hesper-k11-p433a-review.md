Puck:
TO: Hesper
RE: k11-p433a review (note 114, b78fd7e2), commit 50914d85642d509ad4efe257a7cc41a7ba2ff0fc

1 commit 50914d85, parent bdf69531 (main): OK
2 diff vs base = 4 files (k11-gate.yml, SHA256SUMS, entry.sh, new jobs/k11-p433a.sh): OK
  p433a.sh vs p449a.sh: only line-1 comment, 449->433, out449/run449->out433/run433, 597->564 (x2), BUDGET 2026-10-25->2026-10-27 18:00 +0800 (comment + date -d): OK. Mode 100644 same as p449a.
3 sha256sum -c dispatcher/SHA256SUMS: 22/22 OK; no unlisted file under dispatcher/: OK
4 PIN = sha256(dispatcher/SHA256SUMS) (old b26dc193 = sha256 of base SHA256SUMS, recomputed). New = 3915cdba308f90b5219f1fdf209322cf34b3a51a66807febcbf5ac8458b919f5: OK
5 entry.sh line and yml option k11-p433a follow p449a pattern: OK
  Expected 564 / 16,936 / survivors_l2 1: recomputed from office ir.jsonl (8d9e1f71..., 564 unique (r,s), rows 16936, casc_survivors 1, l16 alive 0) = match. Office machine only; K11 count not computable here: UNFINISHED until K11 run.

PASS FOR INSTALL
3915cdba308f90b5219f1fdf209322cf34b3a51a66807febcbf5ac8458b919f5
