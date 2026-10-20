# Hesper check — Opus R030 (1/4), facts only / CHECKED
Reply file: replies/2026-10-21T0708-reply-Opus-R030.txt
Exact Fraction checks:
1. S_{1/5}(1,2,3), one period, exact breakpoints: components [1/5,4/15] and [11/15,4/5], isolated safe points 2/5, 3/5. Matches Opus (K*=[1/5,4/15], ℓ*=1/15, M=6).
2. (1,2,3,4) t=1/5: 1/5,2/5,2/5,1/5. (1,2,3,5) t=6/25: 6/25,12/25,7/25,1/5, all ≥1/5. MATCH.
3. DEC rule for (1,2,3), δ=1/5, as written ((a) PS steps from t0=1/5, (b) α=1/5 shift, (c) table): 20,000 random u (rational and integer ≤200): paths (a)/(b)/(c) = 13,653/6,149/198, 0 failures; PS step count always < 2δ/e+1; (b) outputs stay in K*. CHECKED, not a proof.
4. SF counterexample (float): f(2/5)=0.33066; min f on [1/5,4/15]=0.32301 at t=4/15 (200,001-point grid); cos(2π/5)=0.30902. MATCH Opus numbers.
Not checked by Hesper: A1/DEC/UPD for other V; Lebesgue 297/325 count; Opus's own 3,000-u runs on (1,2,3,4),(1,3,4,7),(1,2,9,30).
Opus requests DeepSeek review for circularity of DEC (not assigned this round). No status change.
