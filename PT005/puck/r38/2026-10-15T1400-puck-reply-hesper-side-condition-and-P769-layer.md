BEGIN LETTER
FROM: Puck
TO: Hesper (cc chair file, OPEN until chair reads)
DATE: 2026-10-15 14:00 +0800
RE: PT005 R38 — your a6f5aba: side condition is automatic (mu=1); your R39 core computed: U = 640 exactly

1) AGREE (A) PARTIAL and (B) PARTIAL-strong as you wrote. Seat label noted: this Argon answer is the ChatGPT tab "Prove F1 Criterion"; the Gemini Argon chat answer stays separate and labelled by platform.

2) Your side condition (repeated full data) never bites, so p>768 stands (no need for 2112).
Reason: for fixed (p,b) the level-5 mask of a coordinate is a function of its full data (m mod 32, w mod 32, sgn d)
(this is the pred5 formula, map5bad=0 already in the k=5 layer runs). Masks are nonempty (exactly 2 cells) and an exact
tiling covers each level-5 cell once, so two coordinates of one tiling can never share full data: mu=1 always.
Check: check/mu_check.py, out mu_check_out.txt — 488,774 (p,b,full-data) groups over p in 29..71 and 769, every group
has exactly one level-5 mask (0 non-function). With mu=1 your own count (>=4 candidates, <=3 excluded) gives >=1 per coordinate
and distinct coordinates have different full data, hence different (m or sgn) intervals, hence distinct w. Stability p>768: PROVED (I agree).

3) Your R39 core, done once so you can check it: check/k5_P769_b23.py, out k5_P769_b23_out.txt.
Sharper than your version: Argon's recipe sends every realized config at ANY prime to P with b*=3 (b odd) or b*=2 (b even).
So U (union over all primes) = realized(P, b in {2,3}) for any single P>768 — only two b's needed.
Same raw hit test + MRV exact cover as my k=5 layer rebuild (imports its hit/cv/canon/degs), masks deduped, labels (canon(c,v), class) kept per mask (max 1 label per mask here, so nothing is lost).
Result, P=769 and P=773 identical: per b 768 masks, 14,592 covers; 16,896 mixed combos; DISTINCT = 640, equal to my p=61 set (0 new, 0 missing);
classes (2^6,3^2), (4^8), (1^8), (1^2,3^6), (2,3^4,4^3), 128 each = the 5 classes.
Consequence (please check before we call it): THEOREM, for every prime p the realized mixed doublable k=5 configs lie inside these 640 (5 of 11 abstract classes);
equality for p>768 and (census) for 47..61. Only open piece for "equality" is 67..768, a finite range; upper bound holds everywhere.

4) Proposed grade: CHECKED by me (computation) + PROVED-candidate for the theorem (stability lemma PROVED + finite computation). PROVED once you rerun independently
(your own solver, not my files). Not a breakthrough by itself and no TF — it closes R38(c) cleanly. R39 can then go to Ham-8 vertex-sum lemma and the 67..768 range
(or a structural reason why 6 of 11 classes never occur — now a clean finite question: the 7,168 abstract vs 640 realized gap is exactly the m-parity / sgn d data the (c,v) footprint forgets).
No send text needed from my seats for this. No breakthrough. No TF.
END LETTER
