# Round 19 data (chair, 2026-10-12)

- rows_383_0_10.txt, rows_383_14_4.txt: all irredundant 15-class covers of two p = 383 gate jobs
  (root 0 / sub 10: 11 rows; root 14 / sub 4: 114 rows). Author's engine, mode irsubrootrawc.
  Counts and node totals identical to the office run (ir.jsonl, collect-38060748868).
  Format: one row per line, 15 classes, each 2 hex digits, folded classes 1..191 (class v and p−v are the same class).
  Rows are in the engine's normal form: every row contains class 1 (unit dilation), and the root/sub-root classes
  of the job. So small classes are partly over-represented by construction.
- rare_14class_covers.txt: the first 14-class cover found by the census at primes with 1–3 such covers
  (379, 409, 419, 421, 457).
- cluster.py: the chair's first-look statistic (see packet).
