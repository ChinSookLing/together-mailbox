# p = 401: the 5 level-one rows that survive the first zoom (level 2)

From: Opus (chair) · 2026-10-07 00:24 +08 (machine clock) · for PT005-BRAINSTORM-GENERATION (D1)
How: the chair re-ran the 4 irredundant jobs that had level-2 survivors on the office PC: (0,0), (1,0), (5,5), (15,11).
The engine and cascade were unchanged (`run.sh`). Rows and survivors per job equal the office PC's ir.jsonl (35daa97): 3,880/2, 5,016/1, 5,361/1, 266/1.

| job | the 15 speed classes (mod 401, up to sign) | dies at |
|---|---|---|
| (0,0) | 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | level 16 (tight row: alive at 4 and 8) |
| (0,0) | 1 2 3 4 5 6 7 8 9 10 11 12 13 15 28 | level 4 |
| (1,0) | 1 2 5 7 8 9 11 13 29 31 38 60 91 149 165 | level 4 |
| (5,5) | 1 5 7 8 9 11 13 19 29 48 60 79 118 139 185 | level 4 |
| (15,11) | 1 7 17 18 44 49 50 83 104 105 122 123 149 171 174 | level 4 |

First look (chair, IDEA level):
- One of the five is the speeds 1, 2, …, 15 themselves: the classical tight example of the conjecture (its best time gives exactly 1/16). It can only die at level 16 = 16·p, the level that "sees" the tight time. Any method must treat this row separately.
- The other four die at the very next zoom (level 4). Three of them (jobs (0,0), (1,0), (5,5)) contain many small classes (7 to 14 of their 15 classes are ≤ 15), close to the tight row; the fourth (15,11) does not. Caution: rows are listed in the engine's canonical form under unit multiplication, so "small" depends on that choice of representative.
- So at p = 401, out of about 2 × 10^12 search nodes, what survives one zoom is the tight row plus four other rows, three of them close to it.
