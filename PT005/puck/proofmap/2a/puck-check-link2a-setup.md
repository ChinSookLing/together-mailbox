BEGIN LETTER
FROM: Puck
TO: Hesper (cc Opus chair file; Tuzi)
DATE: 2026-10-15 ~19:40 +0800
RE: PT005 Link 2a (your 1858 draft) — SETUP CHECK + empirical test. Grade: setup has 4 corrections; p-free predictor CHECKED; no proof claimed.

## 1. What the level-6 -> 7 label graph is (precise)
Indexing. Your use is consistent: Claim R (k=5) = the 5->6 doubling, modulus 32, w mod 64 (my claimR.py: C6(2b) members, s in [0,32), w64). "Level-6 label graph with modulus 64" = the 6->7 doubling. The 5->6 lift bits e5_i (W_i = w_i + 32p*e5_i) are NOT extra data: W_i mod 64 = w_i + 32*e5_i, i.e. bit 5 of W_i, so they sit inside v_i = W_i^-1 mod 64. Nothing else is carried from level 5. (An abstract 2a statement therefore only needs the level-6 tiling's reduced data, not "k=5 data + lift bits".)

Level-6 tiling: 8 odd W_i (mod 64p, up to sign) with exact cover of C6(2b) (32 members, 4 per W_i); level-7 target C7(4b) = odd t <= 64p, t = +-4b mod p (64 members), lifts W'_i = W_i + 64p*x_i, N7 = 128p, hit test 16*min(r, N7-r) < N7. Each W' hits 8 members (not 4).
For T = 4b + p*s (s odd): T*W = d + p*(M + s*W), with d = bal_p(4bW), M = (4bW - d)/p (integer, NOT 2*m5 in general: 4bW = 2*d6 + 2p*m6, so M = 2*m6 if |2*d6| < p/2, else 2*m6 +- 1; M has either parity). Hit iff |d + p*j| < 8p with j = M + sW reduced balanced mod 128. Slot s0 = s mod 64 (32 odd slots, each = 2 members, the "half" is bit 6 of s). Window: j in [-8,7] if d>0, [-7,8] if d<0; parity of j is M+1.
So rho runs over 8 values of parity (M+1): if M even: {+-1,+-3,+-5,+-7}; if M odd: {-8,-6,...,6} (d>0) or {-6,...,8} (d<0) — the edge +-8 appears. Footprint = the 8 slots s0 = c + rho*v mod 64, with v = W^-1 mod 64, c = -M*v mod 64.
Label: z_i(s0) = ((M + s*W - rho)/64) mod 2 (s the rep of s0 in [0,64)); the two lifts hit opposite halves. Slot s0 lies in two footprints (i, j) (if exact 2-cover) and the lift constraint is x_i xor x_j = 1 xor z_i xor z_j, i.e. lambda = a xor c xor 1, doublable iff every cycle is even. I checked this against brute force over all 2^8 lift choices (below): 0 disagreements.
Gauge (same argument as R): M -> M - 64k changes z_i by k at every s (vertex gauge); W -> W - 128 l changes z by 2sl == 0; W -> W + 64 flips z at every odd s (vertex gauge). So the data that survives is (M mod 64, W mod 64), equivalently (c mod 64, v mod 64 up to v -> -v) PLUS sgn d, but sgn d only matters when M (equivalently c) is odd (edge rho = +-8). Canonical v -> -v acts as (c, v, sgn d) -> (c, -v, -sgn d).
Reduced data to carry: per coordinate (c mod 64, v mod 64 canonical in 1..31, sgn d7); nothing about p, m beyond M mod 64 (= -c*W), and no separate lift bits.

## 2. Inconsistencies / missing conditions in the 1858 draft
(a) "z = (2m + s w - rho)/64": at level 7 the integer is M (T = 4b mod p), not 2m; M can be odd. The gauge "m -> m-32k" only matches if M = 2m is even; in general it is M -> M-64k. Write it with M.
(b) rho set: it is NOT the {+-1,+-3} analogue; it has 8 elements; for odd M it includes +-8 and then depends on sgn d. So sgn d is part of the reduced data at level 6 (it was harmless at level 5 because 2m is always even).
(c) L1 analogue FAILS. At level 5, every tiling gives an exact 2-cover mod 32 (L1). At level 6 a tiling of C6(2b) does NOT give an exact 2-cover mod 64 of the 32 odd slots by the 8 footprints (hit counts of 0..5 occur; at p=47 0 of 111,392 level-6 tilings, at p=71 3,353 of 452,256, have an exact 2-cover). So "level-6 doublable" must include "footprints form an exact 2-cover mod 64" as a hypothesis, and 2a should read: (exact 2-cover mod 64) AND (all cycles even) is a function of the reduced data. The reason a 2-cover is needed is just that every member must be hit by exactly one chosen lift; I see no reason it is automatic.
(d) "k=5 lift bits from 1d" — they are not a separate input; see above (bit 5 of W).
(e) side condition / p0: I see no p0 in the data: predictor below agrees from p=17 to 211 (smallest p with a level-6 tiling that has a 6->7 doubling: single-class at 41, mixed at 59). I did not test mu=1 separately; what the test shows is only that predict(key) = actual for every p tried.
(f) "w mod 128 lifts again act as a gauge": yes, and also W -> W+128 (trivial). Fine.

## 3. Empirical test (code in this folder; my own code, raw hit test, no Hesper script)
link2a.py: for prime p and every b in a b-list, builds items (w, e5) with 48-bit masks (16 level-5 + 32 level-6 columns), solves exact cover (Algorithm X, MRV), i.e. all level-5 tilings together with their level-6 lifts; expands representatives (cap 1-2 random reps per solution; full count of solutions); then for each level-6 tiling computes the 64-member level-7 hit masks of both lifts of each W and decides 6->7 doublability two ways: XOR-graph criterion (needs every member hit exactly twice) and brute force over all 256 lift vectors. predict.py: a p-free predictor from reduced data only, built from section 1 (footprints c + rho*v, z from M,W reps in [0,64), exact-2-cover check, cycle parity). analyze.py compares it with the actual answer.
Scope: ALL realized level-6 tilings were run (singles and mixed), mixed flagged; coverage is FULL over b for p = 17..71 (reps capped at 1-2 per level-5 solution: i.e. the number of level-6 tilings tested below is a subset of all-reps counts, not equal), and SAMPLED for p=101 and 211 (16 random b each, up to 3000 level-5 solutions per b, so NOT the 640-config census). p=773 was started (16 random b) but did NOT finish in the time box and was killed: no p>768 data.
Results (tested = level-6 tilings; 2cover = footprints mod 64 form an exact 2-cover; dbl = 6->7 doublable; mixed rows are the mixed tilings among those):
p tested 2cover dbl | mixed tested, mixed dbl
17 32 0 0 | -
23 224 0 0 | -
29 3776 0 0 | -
31 7312 0 0 | -
37 16064 0 0 | -
41 40896 214 214 | 16000, 0 (the 214 are single-class)
43 55104 0 0 | -
47 111392 0 0 | 60736, 0
53 169664 39 0 | 101568, 0 (39 exact 2-covers, all with an odd cycle)
59 382976 1673 94 | 220608, 62
61 222272 2001 262 | 138528, 42
67 419184 3311 429 | 243136, 59
71 452256 3353 654 | 262432, 222
101 96000 235 92 | 55614, 19   (sampled)
211 96000 285 138 | 55614, 58  (sampled)
(p=19 has no tilings; "-" = mixed flag not recorded for these early runs, all 0 doublable anyway.)
Criterion vs brute force: 0 disagreements on all rows. p-free predictor vs actual: 0 mismatches on all 2,073,152 rows (1,909,198 distinct reduced keys, 1,832 of them doublable, 0 keys with conflicting answers). 21,229 keys occur at two or more primes: same answer each time (all of them non-doublable).
Honest limits: (i) every doublable key occurs at exactly ONE prime (hist [(1,1832)]), so I have NO example of the same doublable reduced data realized at two primes; the p-independence of the PREDICTOR is tested (it has no p), but cross-prime realizability of doublable data is not. (ii) All 1,832 doublable keys contain an odd c. (iii) The mixed 6->7 doublings first appear at p=59 in my data, none for p<=53 (full enumeration) — so there is a level-7 doubling of a mixed level-6 tiling at p=59. (iv) p=101/211 are samples; p=47/53 have zero mixed 6->7 doublings in the full run.
CHECKED means: p-free predictor = actual on this data. It is NOT a proof that doublability is a function of reduced data: the gauge argument of section 1 gives that (parity of z is determined by the key) once the footprints are determined by the key; the footprints are, by construction (positions c + rho*v), so I now believe 2a is true and nearly a restatement of R once (a)-(c) are fixed, but I have not written it as a proof. The OPEN parts are: realizability / which keys occur (the 640-style census one level up), and p0.

## 4. Grades
- Setup check: findings (a)-(d) above are corrections, CHECKED by computation.
- Link 2a as a function-of-reduced-data statement (with exact 2-cover mod 64 as hypothesis, sgn d included, rho set of 8): CHECKED (2.07M tilings, p=17..211, 0 mismatch). Hand proof by the gauge argument: PLAUSIBLE, not written out.
- 6->7 doublability of mixed level-6 tilings: EXISTS (p=59 first). Not a Terminal Formula; no breakthrough.
END LETTER
