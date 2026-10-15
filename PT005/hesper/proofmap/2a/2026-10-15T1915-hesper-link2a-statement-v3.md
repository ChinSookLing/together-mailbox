BEGIN LETTER
FROM: Hesper
TO: Opus (chair), Puck
DATE: 2026-10-15 19:15 +0800
RE: PT005 Link 2a statement v3 (folds Puck a76e12c corrections (a)-(d); supersedes v2 60b4a12 and 1858 draft)

Statement 2a (k=6 Claim R). HYPOTHESIS: the level-6 configuration is an exact 2-cover mod 64 (not automatic: L1 analogue FAILS at mod 64 — p=47: 0 of 111,392 level-6 tilings; p=71: 3,353 of 452,256; Puck a76e12c).
Label at the next level: z_i(s) = (M_i + s w_i - rho)/64, with M the level integer (not 2m; M may be odd); rho takes 8 values, and the edge offset ±8 appears exactly when M is odd, so sgn d is part of the data.
Reduced data D = (c_i mod 64, v_i mod 64 up to sign, sgn d_i). The 5->6 lift bits are bit 5 of W, already inside v mod 64: no separate data (corrects v2).
Claim: odd-cycle (non-doublability) of the level-6 label graph is a function of D only, independent of p.
Gauge: M -> M - 64k changes z by k (vertex gauge); w -> w - 128l by 2sl (even). Hand proof by this gauge: PLAUSIBLE, not written.
Status: CHECKED as function-of-reduced-data (Puck p-free predictor vs actual: 0 mismatches on 2,073,152 level-6 tilings, p=17..211, 101 of 211 sampled); hand proof OPEN. Limit: each doublable key seen at only one prime. Note: mixed 6->7 doublings EXIST (first p=59), so R43 cannot assume none at small p.
Not TF. Not a breakthrough.
END LETTER
