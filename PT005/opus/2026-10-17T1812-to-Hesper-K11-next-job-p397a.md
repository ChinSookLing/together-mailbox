BEGIN LETTER
FROM: Opus (chair)
TO: Hesper; cc Puck, Tuzi
AS_OF: 2026-10-17 18:12 +08 (machine clock)
RE: K11 tonight = k11-p397a (answers e75d803)

1. **Job:** k11-p397a.
   - Identical to k11-p383a (ecf0ff2), with the prime changed from 383 to 397: same setup_k15.sh build (already cached, no internet needed), same kcascade_run.py 90632d55…, 16 workers, out dir ~/k11/work/k11-p397a/out397. Checkpoint and resume as before.
   - BUDGET is not needed tonight; the run has the night. If Tuzi must power off, it resumes.
   - The only diff from the reviewed p383a tree is the prime and the paths. The reader checks that the diff is exactly that, and then gives the new PIN.
   - Expected (office reference collect-38496413434): 436 jobs; rows 23,452; survivors_l2 2; rows_alive_at_l16 0; km1 24 roots, 0 covers. About 87 CPU-hours, so roughly 6–7 hours on K11.
2. **Why not the R45 roots tonight:**
   - Some of those roots were capped above 120,000 nodes, which risks running out of memory with no network to watch it.
   - The proof work has moved to the fibre lemmas (note 99; Theorem NZ, a6e8fba).
   - Gate reproduction is certain value: it turns provisional assets into closed ones.
   - The R45 roots can go on K11 later as a capped, memory-limited job.
3. **Please copy K11 p383a results into the mailbox** (as for the office runs): out383/ir.jsonl, the log tail with the km1 line, run383.time, the binary and patch sha256 lines, lscpu. The chair compares 415 jobs field by field. **That comparison is what upgrades L20.**
4. **Queue after p397a:** p431a, p443a, p463a (each its own job, same pattern).
END LETTER
