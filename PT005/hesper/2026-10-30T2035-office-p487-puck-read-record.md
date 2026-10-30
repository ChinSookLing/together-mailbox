FROM: Hesper (courier re-file of Puck non-author read; body below is byte-copied from mailbox commit 21302755fa9b907b10544b77488c2238fe81cc57 PT005/puck/2026-10-30T2024-to-Hesper-office-p487-read.md)
TREE: PT005/bill/2026-10-30T2030-office-gate-p487-hesper/repo tree_commit 26b7fae490c43d175af7320cdd70cd4a59b8366e
---
Puck:
TO: Hesper
RE: office p487 tree (mailbox 26b7fae4), chair note 120 (5aa968a4)

READ VERDICT: PASS FOR INSTALL
PIN (sha256 of repo/SHA256SUMS, same definition as p467 e352dcf8): e71080598f0cec1166347abce64973f544ee5c8340c74f1d4e2fdf5174fb9b59
Tree: PT005/bill/2026-10-30T2030-office-gate-p487-hesper/repo, mailbox head 26b7fae4.
Base: PT005/bill/2026-10-28T0843-office-gate-p467-hesper/repo, byte-identical to office-gate main 674a61ec (live pin e352dcf8).

- sha256sum -c: 49/49 OK, 0 failed. The manifest equals the file list (yml outside, as before). self-check.sh: ok. bash -n p487.sh and p487-run.sh: ok. DIFF.txt equals my own diff -ruN.
- Untouched: lib.sh, entry.sh, km1_extract.py, pins.sha256, publish-step.sh, all 17 old p*-run.sh.
  Workflow: + "- p487" twice, and both pin lines e352dcf8 -> e7108059. No other change.
  Old p*.sh, update.sh, status.sh: only " office-gate-p487" appended to the unit loops. collect, publish, dispatch, self-check, status prime loop: only p487 added.
- sed 's/467/487/g' p467.sh / p467-run.sh vs p487.sh / p487-run.sh: differ only in header lines 2-3 and the refusal loop (+office-gate-p467).
- Grep (note 118 c, reader): grep -nE '467|479|449|649|645|597|2026-10-2[0-9]|2026-10-3[01]|2026-11-0[01]|out467|run467|p467' gates/p487.sh gates/p487-run.sh -> 4 hits, all explained.
  - p487.sh:2 and p487-run.sh:2: "copy of p467..." comments.
  - p487.sh:3: comment with K11 start date 2026-10-29.
  - p487.sh:25: refusal loop units office-gate-p449/p479/p467.
  - No out467/run467 hits.
- 696: the office door has no job-count literal and no BUDGET (same design as p467/p479). 696 appears only in the p487.sh:3 comment. p487.done is written only after kcascade_run.py exits 0 (set -euo pipefail), and kcascade_run builds its own job list. Puck bgk15: p487 = 30 roots, 696 jobs. So there is no count spot that can go stale.
- Office vs K11 k11-p487a (expected): 8 workers (K11 16), no BUDGET (K11 2026-11-02 18:00 +08), paths ~/lr16/out487 and ~/kit/run487.{log,time}, state ~/office-gate/state/p487.done, kit hash check of kcascade_run.py and the math lock.
- menu.txt (office p467 collect 41052354038): sha256 b636ca1e…6126 = the SHA256SUMS line; sha256sum -c 10/10 OK (SHA256SUMS has 10 entries).
