Hesper: exact-Fraction check of Qwen R016 2/4 (chk_qwen_r016.py). Courier promotes nothing.
1. TE-AL / TE-AU review: PROOF VERIFIED by Qwen (reviewer 1 of 2 for TE). Obstruction: Qwen also verified (unassigned extra; Argon is the assigned reviewer).
2. V4 at t=2/9: distances 2/9,1/3,1/3,2/9 — CHECKED; at+dt=18 pairing correct.
3. Q-NC1 (c=2b, exists k≢0 mod 3 with ||ka/3b||,||kd/3b||≥1/5 ⇒ t=k/(3b)): proof correct, but (N2) assumes exactly the a- and d-conditions at the chosen time; it is a family of candidate times, not a region formula. c=2b exact is a hyperplane, so no open real neighbourhood of V4 in R^4.
4. ERROR — neighbourhood: for k=20, d must satisfy frac(20d/90) in [1/5,4/5]; this gives 77.4 ≤ d ≤ 80.1 (ε up to +1/10, not +2.6). Qwen used 7/9−1/5 on both sides. d=81: 20·81/90=18, distance 0 (fails).
5. ERROR — "k0, k0+1, k0+2, at most two steps, deterministic": the procedure is deterministic but NOT covering. For (1,30,60,d) with d on a 1/10 grid in (60,240), it returns no k in 270 of 1,799 cases (first d=311/5); e.g. d=81 fails for k=19 and k=20.
6. V4 not covered by certified list: plausible (no single TE/P1/WL/R013 rule covers it); Opus R016 ETS also reaches V4 at t=31/150 (first success).
