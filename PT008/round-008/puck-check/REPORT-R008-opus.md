# Puck check · PT-008 R008 · Opus T4 manuscript (8 branches)
Manuscript sha256 4720413d78955ea05f7d66bcb0136ff93c0231a954120a4b482fa8a11ae07408 · WEB OFF · own code, exact Fractions.
Status of T4 stays PROOF CANDIDATE; this is a courier spot-check, not one of the two independent reviews.

## Hand check (re-derived)
- Eight vs nine: manuscript now says T4 has EIGHT ordered branches (S1, S2, S3, B3, B2, B4, B5, S6-A); "nine" in R007 was a counting error. Matches the R007 rule list Puck checked (it had 8 rules). Document gap closed.
- L3 (three runners, F3 = ceil((a+b)/(3a))/(a+b)): c0*theta in [1/3, 2/3] proof correct.
- S2 two-sided Nudge: shift |t - t0| = (1/4 - |e|)/c <= 1/(4c) <= 1/(12b); old runners keep >= 1/4 via Lipschitz; t >= 1/(4b) > 0. Tie note correct (k unique when ||X|| < 1/4).
- S3 PLS: (ii) both Delta cases correct (Delta in (0,1/2)); (iv) strict chain at < 1/4 + 2a/(b+c) + a/(2b) correct (k0*eta < 1/4 + eta strict; j < Delta/theta + 1, Delta < 1/2); (v) a(5b+c) <= b(b+c) with margin (2/3)b(c-b) > 0 from b >= 3a. No gap.
- B(k,m) lemma and the four rectangle endpoints: recomputed exactly, all match.
- D constraints 1<r<3, 3+3/r < s < 3(1+r), 4<s<12: correct. R1 = B(2,0) inside D: correct.
- Coverage of D (four r-segments) and branch-order argument B9: correct; G = {7/5<r<5/3, s<16/3} inside S6-A via c < 10a/3 < 11a, c >= 25a/11, c <= 49a/11: correct.
- B10 (two exact integer locks need (p+q)/(p'+q') rational): correct, but it only rules out EXACT double locking, not approximate/inequality control of a second pair.

## Exact tests (check_r8_t4.py, own re-implementation from table A1-A3)
- 159,968 cases, 0 failures: 40,000 whole space (a=1), 40,000 inside D, 10,000 in G, every branch line r in {7/5,5/3,9/7,11/5,13/7}, s in {8,16/3,20/3}, c=3a, c=3b exact and +-1e-6, S3 edges, 5,000 with a != 1.
- Branch counts: S1 20,999 · S2 42,875 · S3 18,650 · B3 7,728 · B2 44,830 · B4 13,795 · B5 8,962 · S6-A 2,129. Every S6-A case lay in G (assertion never fired).
- All 10 worked examples in Section C.6 reproduce exactly (branch, t and the three distances).

## Small notes for the reviewers / chair (not errors in the proof)
- The chat reply says "9 hand-worked examples"; the table in C.6 actually has 10 rows (8 + 2 added for B4, B5).
- B5 condition omits r <= 3 and s <= 20; fine because in D r < 3 and s < 12 (stated in B9).
- Opus self-test numbers (120,000 random + 29,419 boundary points, polygon difference area 0) are the author's own; Puck did not re-run that polygon check.

Puck grade: CHECKED (no gap found). Formal PROVED needs the two independent reviews (DeepSeek, Gemini) and the chair.
