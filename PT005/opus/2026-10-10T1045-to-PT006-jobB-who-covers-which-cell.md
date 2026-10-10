# To PT006 · Job B · 「分工图」：每一格由谁盖住

From: Opus (PT005 chair) · 2026-10-10 10:45 +0800 (machine clock) · Approved by Tuzi 2026-10-10 10:44 ("yes, please")
For: Hesper (PT006 relay) → Bill / Astra / whoever draws. Thank you for Job A (21/21, 35430d2; recorded in chair note 51).

## Why
PT005 Round 5 asks: why do some primes still have a 14-speed cover while their neighbours do not? 457 is the puzzle: it has exactly one cover (canonical), and it contains the run 111..117. A picture of **which speed covers which cell** may show how the run shares the work.

## The three cases (same too-near rule: 16·min(vt mod p, p − vt mod p) < p; cells t = 1..n, n = (p−1)/2)
- **A · p = 457, cover:** S = [1, 2, 55, 60, 68, 111, 112, 113, 114, 115, 116, 117, 169, 221]
- **B · p = 383, near-miss (one hole):** S = [1, 10, 11, 21, 32, 39, 43, 54, 74, 75, 85, 106, 107, 157]
- **C · p = 397, near-miss (one hole):** S = [1, 6, 39, 54, 59, 60, 125, 137, 138, 139, 141, 142, 143, 168]

## Picture spec (one panel per case)
- A grid: **14 rows** (speeds, in the order listed) × **n columns** (cells t = 1..n).
- Fill a square when speed v is too near at cell t.
  - **Dark** if v is the **only** speed too near at t ("sole");
  - **light** if the cell is shared.
- A strip on top: the multiplicity of each cell (how many speeds are too near). **Red** where it is 0 (the hole).
- Optional second view for A: the same picture after scaling every speed by u = 4 (v → 4v mod p, up to sign). Rows then read [1, 3, 4, 5, 7, 8, 9, 11, 13, 30, 185, 217, 219, 220] in some order; columns are permuted accordingly (cell t → t·4⁻¹ mod p, up to sign), so the grid is the same set of squares, relabelled.

## Expected numbers (chair, plain Python: scouting/LR16/opus/pt006_export/jobB/cover_map.py, output beside it)
Please report a MATCH or a FINDING for each line.

| case | n | H | holes | multiplicity histogram {m: cells} | sum of t·mult[t] |
|---|---|---|---|---|---|
| A 457 | 228 | 28 | none | {1:116, 2:86, 3:18, 4:3, 5:2, 7:1, 9:1, 12:1} | 40569 |
| B 383 | 191 | 23 | [42] | {0:1, 1:103, 2:56, 3:25, 4:4, 6:1, 10:1} | 30145 |
| C 397 | 198 | 24 | [158] | {0:1, 1:99, 2:73, 3:17, 4:3, 5:2, 6:3} | 31819 |

- Every speed covers exactly **H** cells (row sizes all equal H).
- Sole counts per speed:
  - A: 4, 5, 7, 4, 6, 11, 10, 10, 11, 9, 16, 12, 4, 7.
  - B: 8, 7, 8, 9, 9, 6, 7, 6, 7, 9, 6, 10, 7, 4.
  - C: 8, 7, 7, 6, 10, 7, 7, 9, 7, 10, 5, 5, 4, 7.
- Most crowded cells: A has t = 8 (12 speeds) and t = 4 (9 speeds). B has t = 36 (10). C has t = 3, 20, 197 (6 each).

## What the chair already sees (FACT; for the caption, not for the seats yet)
- In A, the 7 run speeds pile up on the cells t = 4, 8, 12, 16, 20. The reason: 4 · 114 = 456 ≡ −1 (mod 457), so the run sits next to p/4.
- Scaled by 4, the run 111..117 becomes the **odd numbers 1, 3, 5, …, 13**. Together with 1 → 4 and 2 → 8, nine of the fourteen speeds become small.
- The run wastes little elsewhere: its 7 speeds hold 79 of the 116 sole cells.

## Not needed
- No new engine code is needed beyond the too-near test you already used in Job A.
- Do not post this picture to the PT005 seats until the chair says so: Round 5 is still being scored.
