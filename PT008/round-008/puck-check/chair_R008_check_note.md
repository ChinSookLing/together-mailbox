# Puck check — GPT-6 R008 chair ruling (new results introduced by the chair)

Script: check_chair_R008.py (exact Fractions), output check_chair_R008.out.

1. Chair's n-runner generalisation: non-reference speed magnitudes in [a,b], b <= (n-1)a, t = 1/(a+b).
   Hand: every v*t lies in [a/(a+b), b/(a+b)] subset of [1/n, (n-1)/n], so ||v t|| >= 1/n. Equality at b=(n-1)a gives exactly 1/n (allowed, >=).
   Exact check n=3..12, 40,000 random rational cases + boundary b=(n-1)a for n=3..49: 0 failures.
   Note for Track D reviewers: needs a>0 (no speed equal to the reference speed after the reference change); signs of speeds do not matter since ||-x|| = ||x||.
2. Chair's re-proof of Argon B2 (t = 2/(b+c)): 72,038 integer cases (a<=30, b<=30, c,d<=60), 0 failures.
3. Chair's inclusion Qwen B2 (c+d <= 5a) inside d < 4a (uses c > a): 402,080 integer quadruples below 80, 0 failures.

Remark: the chair states the ruling was made from Puck's summary, not a line-by-line read of the GitHub manuscript.
T4 remains PROOF CANDIDATE per the chair; the T4 independent reviews (DeepSeek 1c510ce, Gemini b6bea7b) are being forwarded to the chair now.
