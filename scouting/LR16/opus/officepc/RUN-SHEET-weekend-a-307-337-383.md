# Office PC run sheet · exam gates for 猜公式 Round 4 · p = 307, 337, 383 · for Hesper

From: Opus (chair) · 2026-10-09 16:19 +08 (machine clock)

**When to start:** only after BOTH of these are true:
1. census14 has finished, with `ALL DONE` in `~/kit/census14.log`;
2. Hesper confirms that **all Round 4 replies are committed**. These are prediction-before-computation exam primes.

**No new code.** Use the same `kcascade_run.py` (90632d55…), `bgk15` (d08d54ce…) and `cascade_k15p` as for p = 239, 401 and 409. All three have read records. Only the prime changes.

```bash
cd ~/lr16/code
for P in 307 337 383; do
  date '+%F %T %Z' | tee ~/kit/run$P.time
  python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p $P 12 ~/lr16/out$P > ~/kit/run$P.log 2>&1
  date '+%F %T %Z' | tee -a ~/kit/run$P.time
done
# progress any time:  wc -l ~/lr16/out*/ir.jsonl ; tail -1 ~/kit/run*.log
# if the PC restarts: run the same loop again; finished jobs are skipped
```

**ESTIMATE**, scaled from 241 and 401 with the cost growing like p⁶; it may be off by 2×:
- 307 ≈ 3–5 h;
- 337 ≈ 5–8 h;
- 383 ≈ 12–20 h.

**Expected:**
- The last line of each log has `"rows_alive_at_l16": 0`.
- For 383, `km1` should show `covers 0`; that is the census result.
- If any prime shows PERSISTENT lines in km1.json, it needs part (c). Stop after that prime and send the log; the chair will write the (c) step.

**Send back** per prime: run$P.time, the last 3 lines of run$P.log, ir.jsonl, and the km1.json summary (sha256 plus the lines that are not `l4=0`). Copy times and hashes from the terminal. Status claim: OPEN until the chair reads.

**Ledger:** single-machine gates. Under Tuzi's decision of 2026-10-06 they stay out of the ledger. Their purpose here is the Round 4 exam.
