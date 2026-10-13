# Chair predictions before computation · GLM level law at level 128 (p = 131)

Written 2026-10-13 09:37 +0800 (machine clock), before the level-128 run finished. Run: chair scouting cascade, MAX_LIFT_EXP = 7, rows below.

Fit l_{2^k} = A·16^{k−1} + B·8^{k−1} + C·4^{k−1} on (l16, l32, l64), which the chair computed today at level 64.

| row (base + extra class) | l16 | l32 | l64 | A, B, C | **predicted l128** |
|---|---|---|---|---|---|
| B1 + 50 | 2,240 | 17,152 | 134,144 | 0, 4, 3 | **1,060,864** |
| B2 (1 1 7 8 17 18 26 30 35 47 50 58 60 65) + 4 | 4,032 | 32,512 | 261,120 | 0, 8, −1 | **2,093,056** |
| B2 + 9 | 4,032 | 32,512 | 261,120 | 0, 8, −1 | **2,093,056** |

If the run reproduces these, the law has passed a held-out test on rows that lock in at level 16. That is the class note 79 could not test.
