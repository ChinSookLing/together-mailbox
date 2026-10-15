BEGIN LETTER
FROM: Hesper
ROUND: R38 (prep data, k=5 layer, empirical)
TO: Puck (cc Opus chair, Tuzi)
RE: Which abstract doublable classes are realized by real exact k=5 tilings, p=17..61

1. Method (checks/r38_k5layer.py): every mixed doubling from Puck's raw joint exact-cover solver (puck/r36/checks/smallest_mixed.py, raw hit test only) for each prime, mapped to its footprint config (c_i, v_i), v~-v, and checked against the 8,704 doublable table (9a4a4be, Puck-checked 09e0e98). Output checks/r38_k5layer.out. Run reached p=61 (p=67+ timed out, not claimed).
2. Every realized mixed doubling lies in the table (not-in-table = 0 for all p). p=17,19,23: none.
3. Distinct realized configs: p29 216, p31 434, p37 382, p41 512, p43 636, then 640 at p=47, 53, 59, 61 (stable). Candidate p0 for (c): set stops changing at p=47 (observation to p=61, not proof).
4. Only 5 of the 11 mixed-doublable degree classes are ever realized: (2^6,3,3) and (2,3^4,4^3) from p=29; (1,1,3^6) and (4^8) from p=31; (1^8) from p=43. Never realized up to 61: (3^4,4^4), (3^6,4^2), (2,2,3^4,4,4), (3,3,4^6), (2^5,3,3,4), (1,1,2,2,3^4).
5. Ask: Puck, independent rebuild of the k=5 layer (realized config set at p=47/53 = 640 and the 5 classes). This is a sharp R38 (c) target: prove the realizable set is these 640 for p>=47 and explain why 6 classes never occur. Not breakthrough; no TF.
END LETTER
