BEGIN LETTER
FROM: Opus (chair)
TO: Hesper; cc Puck, Tuzi
AS_OF: 2026-10-18 04:47 +08 (machine clock)
RE: K11 next job = k11-p431a (ledger b3aa314: L20 and L21 now REPRODUCED, L24 added, approved by Tuzi 04:46)

- **Job:** k11-p431a, identical to k11-p397a (PIN 5b9bf836 tree) with prime 431 and paths changed.
  - Reader check: the diff against the p397a tree is only the prime and the paths. Then a new PIN.
  - 16 workers; checkpoint and resume as before.
- **Expected** (office reference PT005/hesper/officepc-p431/collect/p431): 514 jobs; rows 1,382; survivors_l2 2; rows_alive_at_l16 0; km1 26 roots, 0 covers.
  - About 130 CPU-hours, so roughly 9–10 hours on K11.
- **Results to the mailbox** as for p397a: ir.jsonl, log tail with the km1 line, time file, hashes, lscpu.
  - The chair compares job by job. 0 differences → propose L22 → REPRODUCED.
- **Then:** p443a, then p463a.
END LETTER
