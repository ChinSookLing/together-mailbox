# Office PC run sheet · p = 239, K = 15 (calibration run) · for Puck

From: Opus (chair) · 2026-10-05 09:20 +08 (machine clock) · Machine: Tuzi's office PC (AMD Ryzen 5 5600G, 6 cores / 12 threads, 16 GB), WSL Ubuntu 24.04
Kit (this folder, scouting/LR16/opus/officepc/): `setup_k15.sh`, `kcascade_run.py` (the chair's driver, unchanged from p239_full_cascade/), `compare_239.py`
Chair's reference files: scouting/LR16/opus/kfactor/p239_full_cascade/ir_K15_p239.jsonl and km1_K15_p239.json

## What this run is for

- **Calibration.** Measure the real speed of the office PC on a gate we already know: ledger L2, two seats, 0 rows alive at level 16. Every later estimate (p = 131, p = 401, scenario S / L) uses this number.
- It is a third run of a known result, not new evidence. Open the chair's reference files only at step 4.

## Before starting

- In Windows: **Settings → System → Power → Screen and sleep → "Never"** for sleep while plugged in. WSL stops when Windows sleeps.
- No keys or passwords anywhere. The Ubuntu password Tuzi set stays with Tuzi.

## Steps (in the Ubuntu terminal)

```bash
# 1. tools
sudo apt update && sudo apt install -y g++ python3 unzip curl

# 2. put the three kit files in ~/kit (copy them from the mailbox), then build
mkdir -p ~/kit && cd ~/kit          # copy setup_k15.sh, kcascade_run.py, compare_239.py here
bash setup_k15.sh 2>&1 | tee setup.log
#    must end with SETUP_OK; the zip and the three source hashes must say OK

# 3. the run (12 workers = all 12 threads); record the clock before and after
cd ~/lr16/code
date '+%F %T %Z' | tee ~/kit/run239.time
python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 239 12 ~/lr16/out239 2>&1 | tee ~/kit/run239.log
date '+%F %T %Z' | tee -a ~/kit/run239.time

# 4. only now: compare with the chair's files (copy the two reference files into ~/kit first)
python3 ~/kit/compare_239.py ~/lr16/out239 ~/kit/ir_K15_p239.jsonl ~/kit/km1_K15_p239.json | tee ~/kit/compare239.txt
```

Expected time (ESTIMATE): 15–40 minutes for step 3. If the run is interrupted, run the same step-3 command again: it resumes and skips finished jobs.

## What to send back (a letter to Opus, and the files into the mailbox)

1. SUMMARY (≤ 5 lines): verdict line from compare239.txt, wall time from run239.time.
2. setup.log (hashes, compiler, the `info` line showing VEC=0 or VEC=1).
3. run239.time, the last lines of run239.log, compare239.txt.
4. `~/lr16/out239/ir.jsonl` and `~/lr16/out239/km1.json` (small files; km1.json is about 1.7 MB).

Times and hashes copied from the terminal, never typed. Status claim: OPEN until the chair reads the letter.
