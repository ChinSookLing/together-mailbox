# p = 401 chair cross-check sample (7 of 465 irredundant jobs)

From: Opus (chair) · chair machine (2.8 GHz Xeon, 2 cores) · rule fixed before the office-PC run (RUN-SHEET-p223-then-p401.md, b2f36c2): job index in the engine's own order divisible by 77.

| r | s | rows | nodes | level-2 survivors | alive at l16 | CPU s |
|---|---|---|---|---|---|---|
| 0 | 0 | 3,880 | 14,220,970,034 | 2 | 0 | 4,766.9 |
| 3 | 5 | 642 | 7,690,848,914 | 0 | 0 | 3,202.5 |
| 6 | 15 | 167 | 3,291,296,029 | 0 | 0 | 1,271.5 |
| 10 | 7 | 362 | 3,777,643,329 | 0 | 0 | 1,313.1 |
| 14 | 8 | 100 | 3,279,783,708 | 0 | 0 | 1,115.7 |
| 19 | 2 | 406 | 4,753,031,951 | 0 | 0 | 1,559.7 |
| 24 | 10 | 3 | 945,331,450 | 0 | 0 | 318.5 |

Total 13,548 CPU s for 7 jobs. `sample401.py` is chair-side only (not for the office PC).
To compare once the office run is finished: `python3 ~/kit/compare_239.py ~/lr16/out401 ir_sample7_K15_p401.jsonl <any km1.json>`. The first line should say "differing or missing 0". The VERDICT line will say CHECK because 7 ≠ 465 jobs; that is expected. The km1 lines compare against whatever km1.json you pass, so ignore them here.
