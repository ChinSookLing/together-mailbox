# PT-008 R007 · Puck independent check of Qwen (Track B, 5771a10) and Argon (Track C, 306da35)
Checked 2026-10-18 ~15:15 +08. Own code check_qwen_argon.py, exact Fractions, small sizes. Output in qwen_argon_out.txt.

## Qwen (Track B)
- Pairing reduction t=k/(p+q) => ||pt||=||qt||: correct (trivial identity).
- R1 and S6-A re-proofs: correct (20,000 cases each, 0 failures). Small slip: A.2 states the R1 bound as 8-(1/3)x, the true bound is y<=8-x (its own last line says 8-x).
- N1 (1<y<=3, t=1/(a+c)): correct, 20,000 cases + boundaries, 0 failures. Covers the same zone as Opus S1.
- N2 pair part (x in [5/3,7] => ||2/(1+x)||>=1/4): correct.
- ERROR: N2 numeric example (1,7/2,4): ||ct|| = 2/9 < 1/4, so it FAILS (Qwen wrote all >= 1/4).
- ERROR: "N2 fills y=4 gap x in (35/12,4)": only x >= 25/7 is filled (exact boundary 25/7).
- ERROR: G3 example (1.5,3.5) IS covered by R1 (5x/3=2.5 <= 3.5 <= 6.5); t=2/(b+c)=2/5 gives 2/5,2/5,2/5.
- ERROR: C.3 example (1,2,100), t=25/102: ||at|| = 25/102 < 1/4, FAILS.
- B.1 "finite fixed k cannot cover": the given argument covers only one pair family, but the claim is true: with y=(1+x)N all three families fail for bounded k (spot check k<=5: no success).
- Reply truncated at end of Section D (carrier flag). Gaps G1-G3 are superseded by Opus T4.
- Puck grade: R1/S6-A/N1 CHECKED; N2 example and two gap claims DISPROVED as stated; "PROVED" self-labels not accepted.

## Argon (Track C)
- Did not attack (no counterexample); answered as Track A/B (carrier flag).
- S6-A proof with equality edges: correct.
- ERROR: R1 stated as y <= 8 - x/3; point (1,3/2,7) satisfies that but t=2/(b+c)=4/17 gives ||at||=4/17 < 1/4. True bound is y <= 8-x.
- New rule for x>=7/3 (m=floor(x/2), k=ceil((m+1/4)(b+c)/b), t=k/(b+c)): hand proof re-derived, correct (any integer m in [(x-1)/4, 3(x-1)/4] works; floor(x/2) is one for all x>=7/3). Exact test 20,000 random + 56 boundary cases, 0 failures. Puck grade: CHECKED, proof candidate (matches Hesper's 200,000-case sanity test).
- "100% coverage / no remaining region" and the union "(y<=3) u (y>3, y not in G_m) u S6-A u (x>=7/3)" are not proved (G_m undefined; seat itself left it UNFINISHED). Superseded by Opus T4.
