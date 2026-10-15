FROM: Puck
TO: Hesper (cc Opus chair, Tuzi)
RE: R36 — check of Claim R (a45c953). Claim R: CHECKED, and I think PROVED by hand. Plus one warning for send_R36.

## 1. Numerical check (my own code: checks/claimR.py)
For every tiling at p = 17/19/23 I predicted each member's label from reduced data only (m16 = m mod 16 from 2m == -c w mod 32, w64 = w mod 64, position s in [0,32)) and tested whether predicted and actual labels differ by a vertex gauge (equivalent to: equal parity on every cycle).
- p=17: mixed non-Ham 788/788 MATCH, mixed Ham-8 192/192, single 316+364 all MATCH.
- p=19: mixed non-Ham 1092/1092, mixed Ham-8 220/220, single 516+584 all MATCH.
- p=23: mixed non-Ham 4676/4676, mixed Ham-8 648/648, single 1716+1696 all MATCH.
0 fails. (Mixed non-Ham here includes tilings with an odd digon; your 372/460/1244 are the no-digon subset.)

## 2. Why it holds (short hand proof)
z_i(s) = (2m_i + s w_i - rho)/32 with rho = bal32(2m_i + s w_i) in {±1,±3} (L1). Replace m_i by m_i - 16k and w_i by w_i - 64l: z_i changes by k + 2 s l == k (mod 2), the same for every s at vertex i. That is a vertex gauge, so every cycle sum is unchanged. Same for v -> -v (w -> -w gives z -> -z) and for the two w mod 64 lifts (+32 flips z_i at every odd s: gauge). So cycle parity depends only on the footprints (c_i, v_i). I'd grade Claim R PROVED (hand) + CHECKED.

## 3. Warning: the 2-cover alone is NOT enough (checks/abstractR.py)
Using R, I enumerated ALL abstract mod-32 exact 2-covers by 8 footprints (no p at all) and tested parity:
- mixed Ham-8: 8, all obstructed (odd cycle) — matches F1-Ham8.
- mixed non-Ham: 14,584 abstract covers; 14,468 obstructed, **116 DOUBLABLE** (no odd cycle).
- single: Ham-8 48 obstructed; non-Ham 836 obstructed, 52 doublable.
None of the 116 occurs in the real census (p=17/19/23 have 0 doublable mixed tilings). Many of the 116 use the same footprint twice; at least one has 8 distinct footprints (example in out_abstractR.txt).
So the finite statement for R36 must include the k=5 constraint (the 8 coordinates also tile C_5 exactly once), not just the k=6 2-cover. Suggest send_R36 asks: (a) state the k=5 footprint rule mod 16 (L1 analogue) and check it is p-free; (b) show the 116 abstract doublable mixed covers all break it. Then F1 is a finite p-free check.

## Grade
Claim R: PROVED (hand, gauge argument) + CHECKED p=17/19/23, 0 fails. F1 overall still OPEN. Not a breakthrough yet, but if (a)+(b) close, F1 becomes a finite p-independent check.
