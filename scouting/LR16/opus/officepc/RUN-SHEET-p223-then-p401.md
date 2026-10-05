# Office PC run sheet · p = 223 gate (a)+(b), then the p = 401 pilot · for Puck

From: Opus (chair) · 2026-10-05 16:10 +08 (machine clock)
Asked for by Tuzi: 12:59 ("ask Puck to run on my pc"); 15:57 ("p = 401 的试跑 … yes, please")
Machine: Tuzi's office PC, WSL Ubuntu, the same `~/lr16/code` build and `~/kit` as the p = 239 calibration (chair note 27)

## No new code in this sheet

Both jobs use only files that already have read records and ran on this PC for p = 239:
- `kcascade_run.py` (the chair's driver, unchanged; same sha as in `SHA256SUMS` in this folder)
- `compare_239.py` (nothing in it is specific to 239; it compares any OUTDIR with a chair reference)
- the author's `bgk15` and the `cascade_k15p` build from `setup_k15.sh`

Only the prime changes. Please check the two sha256 sums against `SHA256SUMS` before running.

## Order on the office PC

1. **p = 223 (c)**: `core223/RUN-SHEET-core223.md` (kit v2, read by DeepSeek, wall record 2026-10-05 15:50). About 15 minutes.
2. **p = 223 (a)+(b)**: below. ESTIMATE about 15–30 minutes wall time. The reducible part runs on one core, so a few minutes of it are single-threaded.
3. **p = 401 pilot**: below. ESTIMATE about 21 hours (cost model; chair note 27). This is a new gate, not a reproduction.

## Step 2 · p = 223 (a)+(b)

```bash
cd ~/lr16/code
sha256sum ~/kit/kcascade_run.py ~/kit/compare_239.py      # must match SHA256SUMS in this folder
date '+%F %T %Z' | tee ~/kit/run223.time
python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 223 12 ~/lr16/out223 2>&1 | tee ~/kit/run223.log
date '+%F %T %Z' | tee -a ~/kit/run223.time
# only now: compare with the chair (copy ref223/ from this folder to ~/kit/ref223/)
python3 ~/kit/compare_239.py ~/lr16/out223 ~/kit/ref223/ir_K15_p223.jsonl ~/kit/ref223/km1_K15_p223.json | tee ~/kit/compare223.txt
```

**Expected (from the chair's machine; FACT for the chair's run):**
- irredundant: 132 jobs, 15,177,679 rows, 75,130 level-2 survivors, **alive at level 16: 0**
- reducible: roots 13, covers 33,694, ext_rows 3,740,034, ext_survivors 223,025
- `VERDICT: MATCH`

**How to read the reducible survivors** (this is the one difference from 239):
- 222,478 rows die at level 4, and 34 rows die at level 8.
- 513 rows are PERSISTENT. Each of them contains a 13-class cover. Those rows belong to part (c), which step 1 checks.
- So the 223 gate is closed when **all three** hold: step 1 says MATCH, step 2 says MATCH, and `persistent_lines` in your `km1.json` are exactly the chair's 513 lines.
- Puck may check that last point with `diff`, or the chair can do it from the files you send back.

## Step 3 · p = 401 pilot

```bash
cd ~/lr16/code
date '+%F %T %Z' | tee ~/kit/run401.time
nohup python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 401 12 ~/lr16/out401 > ~/kit/run401.log 2>&1 &
# progress any time:  wc -l ~/lr16/out401/ir.jsonl     (465 irredundant jobs in total)
# if the PC restarts: run the same command again; finished jobs are skipped (the reducible part restarts if it had not finished)
```

- Please keep Windows from sleeping while it runs (power settings: never sleep when plugged in), and keep the WSL window open.
- If Tuzi needs the PC for heavy work, use 8 workers instead of 12 (the last number before the output folder). The results are the same.
- **Cross-check (401 has no reference):**
  - The chair is running 7 of the 465 irredundant jobs on its own machine, chosen before your run by a fixed rule (job index divisible by 77 in the engine's own order): (0,0), (3,5), (6,15), (10,7), (14,8), (19,2), (24,10).
  - Expect the compare to show "differing or missing 0" for those 7. Its VERDICT line will say CHECK only because the job counts differ (7 against 465). That is expected, not a failure.
- **The gate is closed** when the final summary line says `"rows_alive_at_l16": 0`, and the km1 line has no PERSISTENT survivors. If any row stays alive, that is not a failure of the run; it is a finding. Send it to the chair.

## What to send back

SUMMARY (≤ 5 lines per prime). Then:
- `run*.time`
- the last 3 lines of `run*.log`
- `compare223.txt`
- `ir.jsonl` and `km1.json` from `out223` and `out401`. km1.json may be large; if so, send its sha256 plus the lines that are not `l4=0`.

Copy times and hashes from the terminal. Status claim: OPEN until the chair reads it.
