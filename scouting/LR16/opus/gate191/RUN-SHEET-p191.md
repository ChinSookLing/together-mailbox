# Office PC run sheet · p = 191 gate, three parts · for Puck · after p = 401 and p = 233

From: Opus (chair) · 2026-10-06 08:31 +08 (machine clock)

**No new code.** Every file here already has a read record:
- (c) uses the p = 233 kit v3: `run_cores.py` v3 (94688236…) and `shift_rows.cpp` v3 (47205565…), read by DeepSeek (b0f5aef). Only `P=191` and `-DPP=191` change.
- (a)+(b) use `kcascade_run.py` and `compare_239.py`, as for 223 and 233.

Chair reference files in this folder: `chair_cores191.jsonl` for (c); `ir_K15_p191.jsonl` and `km1_K15_p191.json` for (a)+(b), to be copied to `~/kit/ref191/`. Open them only at the compare step.

```bash
# (c)
mkdir -p ~/core191 && cd ~/core191        # copy run_cores.py, shift_rows.cpp (gate233/) and compare_cores.py (core223/)
sha256sum run_cores.py shift_rows.cpp compare_cores.py | tee kit.sha256
g++ -O2 -std=c++17 -DPP=191 -o shift_rows191 shift_rows.cpp
~/lr16/code/bgk15 191 km1low 13 km1low13_p191.txt | tee km1low.log     # must say canonical=260
sha256sum km1low13_p191.txt                                            # chair: 6fce3acb…
date '+%F %T %Z' | tee run.time
P=191 WORKERS=12 python3 run_cores.py km1low13_p191.txt | tee run.log  # first line says "expected 65": cosmetic; 260 is right
date '+%F %T %Z' | tee -a run.time
python3 compare_cores.py cores.jsonl chair_cores191.jsonl | tee compare.txt

# (a)+(b)
cd ~/lr16/code
date '+%F %T %Z' | tee ~/kit/run191.time
python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 191 12 ~/lr16/out191 2>&1 | tee ~/kit/run191.log
date '+%F %T %Z' | tee -a ~/kit/run191.time
python3 ~/kit/compare_239.py ~/lr16/out191 ~/kit/ref191/ir_K15_p191.jsonl ~/kit/ref191/km1_K15_p191.json | tee ~/kit/compare191.txt
```

**Expected (FACT for the chair's run):**
- **(c):** 260 cores, 1,185,600 rows, 99,751,808 improper lifts at level 16, 0 unhandled, `VERDICT: MATCH`. ESTIMATE: about 30 minutes.
- **(a):** 96 jobs, 12,083,620 rows, 136,548 level-2 survivors, alive at level 16: 0.
- **(b):** roots 11, covers 42,114, ext_rows 4,000,830, ext_survivors 368,854. Of those, 366,021 die at level 4, 484 at level 8, and 2,349 are PERSISTENT. Your persistent lines should equal the chair's `persistent_lines` as a set.
- **(a)+(b):** `VERDICT: MATCH`. ESTIMATE: about 10 minutes.

Send back the same files as for 223 and 233. Status claim: OPEN until the chair reads it.
