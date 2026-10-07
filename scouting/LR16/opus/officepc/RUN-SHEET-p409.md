# Office PC run sheet · p = 409 gate · for Hesper · after p = 241 (c)

From: Opus (chair) · 2026-10-07 21:17 +08 (machine clock) · Asked for by Tuzi (21:16: "night time, PC can run 100%")

**No new code.** The same `kcascade_run.py` (90632d55…), `bgk15` and `cascade_k15p` as for p = 239 and p = 401. All three have read records. Only the prime changes.

```bash
cd ~/lr16/code
date '+%F %T %Z' | tee ~/kit/run409.time
nohup python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 409 12 ~/lr16/out409 > ~/kit/run409.log 2>&1 &
# progress any time:  wc -l ~/lr16/out409/ir.jsonl
# if the PC restarts: run the same command again; finished jobs are skipped
```

- **ESTIMATE:** about 26 hours wall time. That is p = 401's 23 h 25 min, scaled by (409/401)^6.
- Keep the PC awake. The same power settings as for 401.
- **Expected:** `"rows_alive_at_l16": 0` in the last line of the log, and no PERSISTENT lines in km1.json. If a row stays alive, that is a finding, not a failure: send it to the chair.
- **Cross-check:** as for 401, the chair picks the sample before the run, by a fixed rule: jobs whose index in the engine's own order is divisible by 77. The chair recomputes those jobs on its own machine, and compares field by field when your ir.jsonl arrives.
- **Ledger:** like 401, this gate stays out of the ledger until Tuzi decides how single-machine gates are recorded (decision of 2026-10-06 16:24).

**Send back:** run409.time, the last 3 lines of run409.log, ir.jsonl, the km1.json summary (sha256 plus the lines that are not `l4=0`). Copy times and hashes from the terminal. Status claim: OPEN until the chair reads it.
