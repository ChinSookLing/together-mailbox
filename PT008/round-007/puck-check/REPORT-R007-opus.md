# PT-008 R007 · Puck independent check of Opus Track A (theorem T4)
Checked: 2026-10-18 ~15:15 +08. Opus reply file PT008/round-007/2026-10-18T1507-reply-Opus-R007.md (sha256 85d1462e2f5c7a3d50aa9822fc038fac477243c6314ac86059e87a26e6e0b344). WEB OFF. Own code (check_opus_T4.py), exact Fractions, small sizes only.

## Grade (Puck): CHECKED. Hand proof read line by line, no gap found. Recommend chair review for PROVED.

## Hand re-reading (each step re-derived by Puck)
- B0 case split: c<=3a, c>=3b, b>=3a, else D={b<3a, 3a<c<3b}. Exhaustive. OK.
- S1 t=1/(4a): at=1/4, bt,ct in (1/4,3/4]. OK.
- S2 Nudge: shift |t-t0| = (1/4-|e|)/c <= 1/(4c) <= 1/(12b); 1/3 - 1/12 = 1/4 for b, a better. Sign rule sigma=sign(e) moves to nearer safe edge. Uses 3-runner F3 (>=1/3). OK.
- S3 PLS(b,c;a): pairing exact; frac(k*theta) in [1/4,1/4+theta), theta<1/2; k*eta < 1/4+2eta+eta/(2theta); condition a(5b+c)<=b(b+c) re-derived; b>=3a gives margin 2b(c-b)/3>0. OK.
- B(k,m) rectangle: at=k/s in [1/4,3/4] iff 4k/3<=s<=4k; bt=k/(1+r) in [m+1/4,m+3/4] iff 4k/(4m+3)-1<=r<=4k/(4m+1)-1. Four block endpoints recomputed: B(2,0) r[5/3,7], B(3,1) r[5/7,7/5], B(4,1) r[9/7,11/5], B(5,1) r[13/7,3]. All match.
- B6: in D, 3+3/r < s < 3(1+r), r in (1,3), so 4<s<12. OK.
- B7: all four r-segments re-checked; fallback is exactly G={7/5<r<5/3, s<16/3}; G inside S6-A via c<10a/3, 11c>=25a, 11c<=49a. OK.
- Rule order B3,B2,B4,B5,S6-A: fallback forced into G (verified as an assertion in code; never fired).
- Chair R1 = B(2,0) restricted to D: c>=5b/3 iff r>=5/3, c<=8a-b iff s<=8. Agrees.
- Opus S5 (b<=3a, 5(a+b)/4<=c<=7(a+b)/4, t=1/(a+b)) also correct (5,000 cases, 0 failures).

## Exact tests (CHECKED level only, not a proof)
130,036 cases, 0 failures: 20,000 whole space (x up to 40, y-x up to 400), 20,000 inside D, boundary lines r in {7/5,5/3,9/7,11/5,13/7,3}, s in {16/3,8,20/3,4,12}, x=3, y=3, y=3x (each exact and +-1e-6), and the three G vertices (+-1e-5). Rule use: S1 16,029; S2 33,005; S3 5,320; B2 26,748; B3 5,254; B4 7,096; B5 5,372; S6-A 883. Plus 3,000 cases with a != 1 (scale check), 0 failures. All five Opus C2 examples reproduce exactly.

## Notes
- Opus itself says the 4-runner existence is already known in the literature (not checked, WEB OFF); the claim is only the explicit 9-piece formula and its elementary proof.
- Least-sure items Opus names (S2 tie e=-1/2, PLS x0 exactly 1/4 or 3/4, G vertices) were in Puck's boundary set; no failure.
