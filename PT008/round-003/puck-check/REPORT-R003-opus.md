# Independent check of Opus PT-008 R003 (exact Fractions; chk.py)
Grid/random evidence only; not proofs. Windows may extend below t=0 (not clipped).
1. Two-Window Lemma: 17,940 random (V size1-5 mixed int/rational/negative, old safe times from grid 1/240, random w). Hypothesis held in 12,100; conclusion failed in 0 -> CHECKED (random). Hypothesis failed and both windows failed in 985 cases; only 2 with gap > -1/50, i.e. failures are not hugging the threshold, so tightness of the constant was NOT demonstrated by random search (the "can't be smaller" claim is unconfirmed by me; only the zero-violation direction).
2. Degeneration |w|>=nM: 8,945 tests, single window failures 0 -> CHECKED.
3. V={1}, w=4/3, n=2, δ=1/3: ρ=1/6 at half-integers. Single window at t_a=3/2 fails (e.g. window [4/3,5/3]); t_b=5/2 works; ||w(ta-tb)||=1/3 >= 2δ-w(ρa+ρb)=2/9 -> lemma applies. t_a=3/2,t_b=9/2 gives ||..||=0, both fail. CHECKED.
4. V={1,2}, w=3, δ=1/4: Lipschitz windows succeeding: 0 of 6 old safe grid points in [0,3] -> Opus confirmed. Exact components (e.g. [1/4,3/8],[5/8,3/4],[5/4,11/8]) all 6 succeed (they contain safe points like 1/4, 3/4, 5/4). Global safe points for {1,2,3} at 1/4: t=1/4,3/4,5/4,7/4,... (isolated points, i.e. t≡±1/4 mod 1). CHECKED. Note exact-comp success is touching at a single point (||3t||=1/4 exactly).
5. V={1,3}, w=2: old safe set is [4/9,5/9] mod 1 (hand-checked). Exact component [5/12,7/12] has max||2t||=1/6<1/4: fails; 0 of 3 components succeed, 0 Lipschitz. Global safe for {1,2,3}: t=1/4,3/4,5/4,... (same set as claim 4). Nearest old safe time to 1/4 is 4/9, distance 7/36≈0.194. CHECKED.
Insight: both end at {1,2,3}, safe set t≡±1/4 mod 1; consistent with Opus's insertion-order remark.
Not tested: the Nudge rule, the "no order works for any V" question.
