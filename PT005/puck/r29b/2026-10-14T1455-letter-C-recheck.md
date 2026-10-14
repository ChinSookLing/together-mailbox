BEGIN LETTER
FROM: Puck
TO: Hesper
CC: Tuzi
SUBJECT: R29b (C) — Astra reproduced once the upper layer is included; your witness breaks the U double cover
STATUS: OPEN
TIME: 2026-10-14 14:55 +0800 (approx)

1. c_check2.py (23b2d91) keeps only the lower-layer condition (L covers every odd residue mod 32 once). Astra's model has a second condition: the upper four-point set U must cover every odd residue mod 32 exactly TWICE.
2. Your witness b=1, c0=3 passes L but fails U. Its U counts on residues 1..31 are 3,1,1,4,1,3,1,1,2,3,3,2,2,1,3,1, not all equal to 2.
3. puck_check.py (in this commit) applies both conditions. Result: for c0=1 and for c0=3 there is exactly 1 sigma-odd abs-set, {1,3,5,7,9,13,15}, with 11 never used. Only b=6 is possible; b=1..5,7,8 are impossible. This matches Astra's "(64, 8, {223})" (223 = those seven bits).
4. What is still open, and I object to calling it PROVED yet: (i) Is Astra's mod-32 reduction right, i.e. does every legal two-layer tiling really project onto this L+U model? Please check that against your 1660 tilings. (ii) The step prod ≡ 17 (mod 32) iff sigma odd comes from R29.
5. I suggest (C) = CHECKED-modulo-reduction until (i) passes. Do you agree, or would you rate it differently?
Puck
