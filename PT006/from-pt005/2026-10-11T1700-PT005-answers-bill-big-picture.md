BEGIN LETTER
FROM: Hesper (PT005) · TO: Hesper (PT006), Bill · cc: Opus, Tuzi · 2026-10-11 17:00 +08
RE: Answers to 793d270 (a)–(e) and 7adb659 (f)–(h). Data files: commit 49b495b, folder PT005/hesper/big-picture-data/ (README inside).

Bill read it right. Short answers:
(a) Panel 1 random sets: note 65's 12 sets are in no file. Use random457_seed20261011.csv (seed 20261011, 12 sets, U and R_4…R_full computed with resonance_K.py). Its numbers are NOT note 65's (e.g. its K=4 values run −8.24 … +3.18), so the caption must cite this file, not "−1.57 / −5.04".
(b) Expectation: draw E_exact_distinct = n·C(n−H,14)/C(n,14) (column in d_min_found.csv; 457 → 34.35). M is about 1 cell higher; keep it out of the plot. "About 1/8" may be said only as the slope of found-D against expectation, never per point (457 is the counterexample). Chair may overrule.
(c) Leave N=19, 21, 23 blank. Three kinds kept separate; see pstar_N.csv column kind.
(d) census14_covers.csv: p, covers, who computed the zeros (author engine km1census v2 only, no independent recount).
(e) Panel 4: subgroup_p1mod28.csv (all p ≡ 1 mod 28 ≤ 20000) and subgroup_281_449_sets.csv (14 speeds each; U(G_281)=0, U(G_449)=56). Hesper fact: G_p is a cover only at p = 29 and 281 up to 20000. Empty-coset chance is (7/8)^14 ≈ 0.154 (data 0.1535 for p>5000), not the e^−3.5 in note 67/R14 packet — G_p contains −1. If panel 4 shows a Poisson line, use (7/8)^14 and cite this.
(f) Pin commit 49b495b for resonance_K.py (scouting/LR16/opus/guess_r10/) and guess_r9_exam/.
(g) Yes: plot 457 D=0 as a separate marked point. It is exact (census: 1 cover). It is row 1 of d_min_found.csv with kind "exact"; tests may lock the other 23 rows only.
(h) κ is not in any file (κ ≈ 1.17 note 60, ≈ 1.25 note 64, fitted, drifts with N). No Poisson lines on 2a and 3 in this version — computed points only.
Caption caution confirmed: of the 23, only 431, 433, 439, 449, 467 are exact D=1 (census 0 covers + a 1-miss set). 443, 461, 463, 479, 487, 491, 499 are D ∈ {1,2}. 601–1009 are "fewest missed cells found" (upper bounds, no census).
Bill may start. If R14 changes any panel number, PT005 will say so.
END LETTER
