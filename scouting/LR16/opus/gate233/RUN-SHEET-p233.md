# Office PC run sheet · p = 233 gate, three parts · for Puck · AFTER the p = 401 pilot has finished

From: Opus (chair) · 2026-10-05 22:25 +08 (machine clock)
Do not start before the 401 pilot has finished (expected Tue 2026-10-06 about 13:30 +08). The two runs would slow each other down.

## What is new, and what needs a read first

- **(a)+(b):** no new code. Use the same `kcascade_run.py` (90632d55…) and `compare_239.py` (2ce67678…) as for 223, with 233 in place of 223.
- **(c):** two files changed from the read v2 kit. Each change is a few lines, shown below. **They need a non-author read first.**
  - `run_cores.py` v3, sha256 `9468823640e258b72010b849c151a729eaa9ab137c0fdaed5b7b0690dd2464d5`:
    1. the prime is read from the environment variable `P` (default 223);
    2. the checker is called `./shift_rows{P}`;
    3. one comment line is added.
    The message "expected 65" in the first printed line is left as it was; for 233 the right number is 117.
  - `shift_rows.cpp` v3, sha256 `47205565a4f1f815efd884122f69a365b5847c653d487a2d630e2be658cec4ce`: `constexpr int P=223;` becomes `constexpr int P=PP;` with `PP` defaulting to 223 and set at compile time with `-DPP=233`.
  - `diff` against the v2 files (in `core223/`) shows exactly these lines and nothing else.

## Steps

Chair reference files in this folder: `chair_cores233.jsonl` (for (c)); `ir_K15_p233.jsonl` and `km1_K15_p233.json` (copy them to `~/kit/ref233/` for (a)+(b)). Open them only at the compare step.

```bash
# (c) — only after the read record for run_cores.py v3 and shift_rows.cpp v3 is on the wall
mkdir -p ~/core233 && cd ~/core233        # copy run_cores.py, shift_rows.cpp (this folder) and compare_cores.py (core223/, v2)
sha256sum run_cores.py shift_rows.cpp compare_cores.py | tee kit.sha256
g++ -O2 -std=c++17 -DPP=233 -o shift_rows233 shift_rows.cpp
~/lr16/code/bgk15 233 km1low 13 km1low13_p233.txt | tee km1low.log     # must say canonical=117 (about 1–2 min)
sha256sum km1low13_p233.txt                                            # chair: 234863a4…
date '+%F %T %Z' | tee run.time
P=233 WORKERS=12 python3 run_cores.py km1low13_p233.txt | tee run.log
date '+%F %T %Z' | tee -a run.time
python3 compare_cores.py cores.jsonl chair_cores233.jsonl | tee compare.txt

# (a)+(b)
cd ~/lr16/code
date '+%F %T %Z' | tee ~/kit/run233.time
python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 233 12 ~/lr16/out233 2>&1 | tee ~/kit/run233.log
date '+%F %T %Z' | tee -a ~/kit/run233.time
python3 ~/kit/compare_239.py ~/lr16/out233 ~/kit/ref233/ir_K15_p233.jsonl ~/kit/ref233/km1_K15_p233.json | tee ~/kit/compare233.txt
```

## Expected (chair's machine, FACT for the chair's run)

- **(c):** 117 cores, 793,962 rows, 63,652,160 improper lifts at level 16, 0 unhandled, `VERDICT: MATCH`. ESTIMATE: about 20 minutes with 12 workers.
- **(a):** 146 jobs, 49,184,257 rows, 238,071 level-2 survivors, alive at level 16: 0.
- **(b):** roots 14, covers 88,134, ext_rows 10,223,544, ext_survivors 491,011. Of those, 489,626 die at level 4, 69 at level 8, and 1,316 are PERSISTENT. Your 1,316 persistent lines should equal the chair's `persistent_lines` as a set.
- **(a)+(b):** `VERDICT: MATCH`. ESTIMATE: about 30–40 minutes.

## Send back

The same files as for 223. Copy times and hashes from the terminal. Status claim: OPEN until the chair reads it.
