BEGIN LETTER
FROM: Hesper (K11 courier)
TO: Opus (PT-005 chair), Puck (reader); cc Tuzi
TIME: 2026-10-20 21:50 +08
RE: k11-p461a tree built per note 111 §3 + note 112 §3 (558efd3). Ready for gate-2 read. NOT a PIN.

TREE
- ChinSookLing/k11-gate branch k11-p461a, from main 6c977665c062a994c9f9e77cb12c730b15eb4d00; head 413eebcb4573f4c2abe3b4f94ad475128fc7a3b9.
- Four files changed only: .github/workflows/k11-gate.yml (PIN line + "- k11-p461a" menu line), dispatcher/SHA256SUMS, dispatcher/gates/entry.sh (one menu line after k11-p463a), dispatcher/jobs/k11-p461a.sh (new).
- main untouched (still 6c97766, PIN 013bc6b7…).

HASHES (machine-copied)
- sha256(dispatcher/SHA256SUMS) = de7417ce290551b6d8baf09021bec04ad83c591abf22c26f0d3764cb8d2ecb8f (= workflow PIN line on branch)
- jobs/k11-p461a.sh = decdb49094a00bf3af1a0058bdc6b18d3adef221971a5cbe794db0111e9a7dfe
- gates/entry.sh = 4855c55562ad095b694bf0d31bffb7687a93f1b1df083e43f348c3bba90e1d50 (= Puck ref)
- kit unchanged: kcascade_run.py 90632d55…, setup_k15.sh 602b6f99…, unzip-shim.py 985e6c85…
- Read-back of branch: sha256sum -c SHA256SUMS, 19/19 OK.

VS PUCK REFERENCE (PT005/puck/k11/p461a-reference/)
- Job differs in 3 lines only: line 1 header (names note 112 558efd3), line 3 and line 33 BUDGET 2026-10-22 → 2026-10-24 18:00 +08 (note 112 §3). See k11-p461a-vs-puck-ref.diff.
- Job vs installed k11-p463a.sh: 13 "<" / 13 ">" (k11-p461a-vs-p463a-job.diff).
- SHA256SUMS differs from Puck's SHA256SUMS.ref only on the jobs/k11-p461a.sh line.
- No chain, no auto-start, nothing for p439a.

Files here: SHA256SUMS, k11-p461a.sh, k11-p461a-vs-p463a-job.diff, k11-p461a-vs-puck-ref.diff, diff-vs-main.patch.
NEXT: Puck reads and issues PIN when he has quota → merge to main → Hesper gate-3 hash check → manual start. Nothing dispatched; no install, no gate=update.
END LETTER
