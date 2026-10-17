# PT-008 R002 Puck independent check of Opus audit claims (2026-10-17 16:45 +08)
Exact fractions, small programs only (r2chk.py, output r2chk_out.txt).
- B2 family V={1..n-1}, t0=j+1/n, w=nq/(jn+1): n=2..7, j in {1,2,3,10,50} (30 cases): every w < nM, window [t0-h,t0+h] has no safe time for w (grid + analytic |w|h<delta). CHECKED over that range.
- Local failure vs global: V={1}, w=4/3, window [4/3,5/3] fails; t=1/2 is safe (||1/2||=1/2, ||2/3||=1/3). CHECKED.
- L2* (actual margin rho): 13,816 random cases meeting condition (ii), 0 failures; rho >= h held in all (11,463 with rho>h strictly). CHECKED over random range only, not a proof.
- Earlier: L2 itself, 19,849 random cases, 0 failures (l2_check.py).
Not checked: Opus's proof lines (that is Opus's audit), the Two-Window Lemma (IDEA, no statement fixed), "L2 equivalent to Round 001 lemma".
Grades by Puck: CHECKED only. PROVED for L2 is the chair's/Tuzi's decision after reading Opus's audit file (PT-008-R002-OPUS-AUDIT.md, pasted by Tuzi; Tuzi to supply the original file for archiving).
