# Independent check of Opus PT-008 R005B (exact Fractions; CHECKED is not PROVED)
Code: chk_opus005b.py (run: `python3 chk_opus005b.py 60 30000`), raw log: output.txt.
Test sets: all integer triples 0<a<b<c<=60 (34,220), 30,000 random rational triples (denominators up to 50, scale factors 10^-2..10^3, wide ratios), plus Opus's cited examples. Pass/fail only by exact Fraction arithmetic.

| Claim | Verdict | Counts |
|---|---|---|
| Lemma PC: k=ceil((p+q)/4p), t=k/(p+q) gives ||pt||=||qt||∈[1/4,1/2) | CHECKED | 35,370 pairs (ints+rationals), 0 violations |
| F(a,b)=ceil((a+b)/3a)/(a+b) has ||at||,||bt||>=1/3 (used by R1) | CHECKED | 39,557 pairs, 0 violations |
| R1 (c>=3b): F then Nudge gives g>=1/4 | CHECKED with a caveat | applies to 10.5% int / 56.1% rat; 0 violations if nudge goes to the nearest boundary (m±1/4)/c (always within h=1/(12b)). A FORWARD-ONLY nudge (as in the worked example) exceeds h in 523 int cases and gives g<1/4 in 27 int / 220 rat cases. So "Nudge" must be bidirectional; the text does not say so. |
| R1 example {1,2,6}: t=3/8, ||t||=3/8, ||6t||=1/4 | CHECKED (typo) | actual values ||t||=3/8, ||2t||=1/4, ||6t||=1/4. The "||18/8||" Opus lists is not a runner term (should be ||6·3/8||=||9/4||); value 1/4 is right. |
| R2 (b>=3a): k, I, J, X, t=X/c gives g>=1/4; I⊂J; t∈I; k>=1 | CHECKED | applies to 33.3% int / 56.8% rat; 0 violations, 0 failures of I⊂J, t∈I, k>=1 |
| R2 example {1,3,10}: k=1, I=[5/12,7/12], L=25/6, X=17/4, t=0.425 | CHECKED | ||t||=17/40, ||3t||=11/40, ||10t||=1/4 (all as claimed) |
| R3: (a,c) pairing with k_ac works when ||b·k_ac/(a+c)||>=1/4 | CHECKED | condition holds for 76.6% int / 65.4% rat of triples; every such t gives g>=1/4, 0 violations |
| R3 special: c<=3a ⇒ k_ac=1, t=1/(a+c), automatic | CHECKED | 15,410 int + 3,128 rat cases, 0 violations |
| R4: t=1/(a+b) when ||c/(a+b)||>=1/4 | CHECKED only after R2 (ordering) | standalone it is WRONG when b>3a: 3,538 int cases (e.g. (1,4,7), t=1/5, g=1/5) and 7,842 rat cases fail g>=1/4. With b<=3a (the only case reached after R2 in the ordered table), 0 failures. Opus's table gives t=1/(a+b) without stating b<=3a; correct general form uses k_ab=ceil((a+b)/4a). |
| R4 band in dense region D: R4 ⟺ 5(a+b)/4<=c<=7(a+b)/4 | CHECKED | 4,997 int + 2,173 rat D-triples, 0 mismatches |
| B5: in D, k_bc=1 and ||a/(b+c)||<1/4 | CHECKED | 4,997 int + 2,173 rat, 0 violations |
| Ordered table F4 = R1,R2,R3,R4 always outputs g>=1/4 when it outputs | CHECKED | 0 violations. Coverage int<=60: R1 10.5%, R2 29.8%, R3 51.1%, R4 2.6%, uncovered 6.0% (2,043). Rational: R1 56.1, R2 26.2, R3 13.8, R4 1.3, uncovered 2.5% (749). |
| Uncovered region is UNFINISHED but solvable | CHECKED (consistent) | every uncovered integer triple (all 2,043) has a global safe time (exact search at critical points (m+1/4)/u); also all 34,220 integer triples have one. |
| Q1 (inheritance) DISPROVED on {1,2,3}: F(1,2)=1/3, F(1,3)=1/2, F(2,3)=1/5 all fail | CHECKED | g=0,0,1/5 respectively; R3 t=1/4 gives g=1/4. NOTE: Opus's check lists use F (δ=1/3 formula) not PC; with the δ=1/4 pairing PC(1,3), t=1/4 is exactly the "other rule" Opus uses, so "all three pairings fail" is true only for the 1/3-formula F pairings, NOT for PC pairings (PC(1,3) works). Wording "三种配对全部失败" is misleading. |
| Q2: in D, (b,c) with k=1 always fails | CHECKED (= B5) | |
| Q2 "fastest pairs with slowest (R3) or (a,b) (R4)" | NOT a complete rule | in D with k0 only, fails for 2,043/4,997 int D-triples (Opus does not claim completeness) |
| C2 {2,4,7}: R1,R2 not applicable; R3 t=2/9 fails (||8/9||... =1/9); R4 t=1/6 fails | CHECKED | exact values as claimed |
| C2 {2,4,7} has t=2/11: 4/11, 3/11, 3/11 | CHECKED | g=3/11. NOTE: k=2 for pair (b,c)=(4,7) is k0+1 (ceil gives k0=1, t=1/11); fine as k0+1. |
| C3: in D grid (~360k points) R3∪R4 uncovered ≈24%; with k0,k0+1 ≈3%; e.g. x≈2.34,y≈3.01 uncovered | NOT REPRODUCED (numbers); example CHECKED | my grid a=245, b in (a,3a), 3a<c<3b (358,926 points): uncovered by R3∪R4 34.2%; by (a,c),(a,b) with k0,k0+1: 5.6%; adding (b,c) k0,k0+1: 5.06%. The grid/measure Opus used is unspecified, so the percentages may differ by definition; example (245,574,736)≈(1,2.343,3.004) is indeed uncovered and (100,234,301) is globally solvable (t=201/400) but F4 gives none. Opus labels C3 self-test, not CHECKED; consistent. |
| D3 "rules hold for any positive reals" | CHECKED on random rationals only | no real-speed/irrational test; proofs not checked |

## Mislabels / wording issues
1. R1 relies on "Nudge" from Round 002 L2; forward-only nudge fails (see above). The proof B2 says L2 applies with w=c>=3b=nM, which is correct for a nearest-boundary nudge within h.
2. R4 stated without b<=3a; only valid via table ordering.
3. C1 "all three pairings fail" is true for the 1/3-formula F, false for PC pairings.
4. Typo ||18/8|| in {1,2,6} check.
5. C3 percentages not reproduced under my reading of the grid.
6. R1–R4, PC, B5 labelled "PROOF CANDIDATE": the numerical evidence supports them, but this report does not prove anything. Hand proofs B1, B3, B4 read correct to me (B3 steps I⊂J and X∈cI verified numerically, not formally).
