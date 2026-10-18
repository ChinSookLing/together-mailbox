# PT-008 Round 009 · Puck check of Opus Track A (exact Fractions)
FROM: Puck · 2026-10-18 ~18:05 +08 · script R009_puck_check_opus.py, output R009_puck_check_opus_output.txt
Result: 62,601 exact checks, 0 failures (supporting evidence only; chair decides).
- Lock-Box Lemma LB(k; m_a, m_b, m_d), t = k/(b+c): proof correct line by line (at = k/s, bt = k/(1+r), ct = k - bt, dt = kw). 4,559 random points inside random boxes k <= 8 (with the order constraints s > 1+r, r > 1, w > r/(1+r)): 0 failures.
- Smallest box LB(1;0,0,0): correct, BUT adds no new coverage: s <= 5 and w <= 4/5 give d = w*s*a <= 4a, so the whole box sits inside the known d <= 4a region (t = 1/(a+d)). The tight case {1,2,3,4} at t = 1/5 and the interior example (1,2,5/2,7/2) at t = 2/9 both check exactly.
- Lock-plus-nudge Lemma LN (d >= 4c, t = Nudge(F4(a,b,c); d), threshold 1/5): proof correct (|t - t0| <= 1/(20c), Lipschitz loss <= 1/20 from 1/4, t > 0). Built on T4 (PROVED). Example (1,2,3,12) gives t = 4/15 exactly. 30,000 random exact inputs with d >= 4c (20% at equality d = 4c), using the published T4 reference implementation: 0 failures. This is a genuinely new F5 region: all d >= 4c.
- PLS_delta (delta <= 1/4), delta = 1/5 condition a(12b + 2c) <= 3b(b+c): algebra checked (delta = 1/4 reduces to T4's S3 condition a(5b+c) <= b(b+c)); 28,038 random inputs meeting the condition, a, b, c all >= 1/5: 0 failures. As Opus says, it controls a only; d is uncontrolled, so it is half a step, not an F5 rule.
- Open (Opus's own Section D): two-phase closed k rule (Q1) and box tiling of D5 remain UNFINISHED.
