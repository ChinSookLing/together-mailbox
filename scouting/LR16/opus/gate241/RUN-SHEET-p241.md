# Office PC run sheet · p = 241 gate · for Puck · after 401 → 233 → 191

From: Opus (chair) · 2026-10-06 10:15 +08 (machine clock)
**No new code.** (c) uses the read p = 233 kit v3 with `P=241` and `-DPP=241`. (a)+(b) use `kcascade_run.py`, as before.
Why the office PC: at p = 241 the work is about 10× that of 223, too much for the chair's 2 cores alone.

## What the chair has already done (TEST, chair machine)

- **p = 241 has no cover on ≤ 12 classes** (`km1low 12`: 0). There are 936 canonical 13-class cores (`km1low13_p241.txt`, sha256 `312d5927…`).
- **(b), by the chair's faster route:**
  - 344,280 irredundant 14-covers (km1root, deduped; sha256 `4f313fec…`), each extended by one class: 41,313,600 rows.
  - The 13,307 rows that contain a covering 13-subset belong to (c).
  - The other 41,300,293 rows **all die by level 8**: 2,329,711 survive level 2, 591 of them die at level 8, all others at level 4; 0 reach level 16.
- **(c):** 46 of the 936 cores done so far (`chair_cores241_partial.jsonl`). All pass: 0 unhandled; every lift has 13 coordinates ≡ 0 (mod 16) and 2 odd.
- **(a):** running on the chair's machine (172 jobs; ESTIMATE 3–4 hours).

## Steps on the office PC

```bash
# (c) — ESTIMATE about 3 hours with 12 workers
mkdir -p ~/core241 && cd ~/core241        # copy run_cores.py, shift_rows.cpp (gate233/) and compare_cores.py (core223/)
sha256sum run_cores.py shift_rows.cpp compare_cores.py | tee kit.sha256
g++ -O2 -std=c++17 -DPP=241 -o shift_rows241 shift_rows.cpp
~/lr16/code/bgk15 241 km1low 13 km1low13_p241.txt | tee km1low.log     # must say canonical=936 (about 3 min)
sha256sum km1low13_p241.txt                                            # chair: 312d5927…
date '+%F %T %Z' | tee run.time
P=241 WORKERS=12 python3 run_cores.py km1low13_p241.txt | tee run.log
date '+%F %T %Z' | tee -a run.time
python3 compare_cores.py cores.jsonl chair_cores241_partial.jsonl | tee compare.txt
# expected: "differing/missing" = 0 for the chair's 46 cores; "extra" = 890 and VERDICT CHECK are expected here

# (a)+(b) — ESTIMATE several hours; the reducible part runs on ONE core (single filterext process)
cd ~/lr16/code
date '+%F %T %Z' | tee ~/kit/run241.time
python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 241 12 ~/lr16/out241 2>&1 | tee ~/kit/run241.log
date '+%F %T %Z' | tee -a ~/kit/run241.time
```

## Expected (from the chair's runs)

- **(c):** 936 cores, every one `unhandled 0`. The chair will compare all 936 once its own run or yours is complete.
- **(b) in `km1.json`:**
  - roots and covers: covers = 344,280; ext_rows = 41,313,600.
  - ext_survivors will be **larger** than 2,329,711, because your route also cascades the 13,307 core rows; those become PERSISTENT.
  - Please send: the counts of `l4=0`, `l8=0` and PERSISTENT lines, the sha256 of km1.json, and the non-`l4=0` lines.
- **(a):** `rows_alive_at_l16` must be 0. The chair will compare job by job when its run finishes.

Status claim: OPEN until the chair reads it.
