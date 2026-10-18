# Puck check · PT-008 R008 · Track B (Argon 434ace8, Qwen b680387)
WEB OFF · own code check_r8_trackB.py, exact Fractions. Hesper's own 200,000-point checks are in those commits.

## Argon (Gemini 3.1 Pro seat)
- B1: correct but narrow. V=(1,2,3,3+sqrt2): exact (b+c)t in Z and (c+d)t in Z impossible (irrational ratio). Only rules out EXACT double locking; the claim that the second pair "must be handled by pure inequalities" is a reasonable conclusion, not a proof that no other control exists. Same point as Opus B10 and Qwen B1.
- B2: region c >= 1.5b, a >= 0.1(b+c), 0.6(b+c) <= d <= 0.9(b+c), t = 2/(b+c). Hand proof correct (bt in (0.2,0.8], ct = 2 - bt, at in [0.2,0.8), dt in [1.2,1.8]). Region implicitly needs c < 9b (from a < b). Example (1.1,2,4,5), t=1/3: distances 11/30, 1/3, 1/3, 1/3, correct. Puck exact test 100,000 cases, 0 failures. CHECKED, proof candidate.
- Note: header "Copy time 2026-06-28" is the browser/Gemini clock, ignore.

## Qwen
- B1: correct (1,2,3,pi). The "two constraints vs one k, generically over-determined" line is heuristic, not proof.
- B2: c + d <= 5a, t = 1/(c+d), min = a/(c+d) >= 1/5. Proof correct (all four inside the first half-lap except d, whose distance is c/(c+d)). Example (2,3,4,5), t=1/9: 2/9, 1/3, 4/9, 4/9 correct. Puck exact test 100,000 cases, 0 failures (min equals a/(c+d) every time). CHECKED; region narrow (d < 4a).
- D3 (t = 1/(a+d) when d <= 4a and c < (a+d)/2), left UNFINISHED by Qwen.

## Puck observation (proof candidate, small, hand + exact check)
Qwen's D3 holds WITHOUT the condition c < (a+d)/2: for any 0<a<b<c<d with d <= 4a, t = 1/(a+d) gives at = a/(a+d) >= 1/5, dt = 1 - a/(a+d), and for x in {b,c}, a < x < d so ||xt|| = min(x, a+d-x)/(a+d) > a/(a+d). Hence min = a/(a+d) >= 1/5. This region strictly contains Qwen's B2 (c+d <= 5a forces d < 4a). Exact test 100,000 cases with d <= 4a, 0 failures; 74,938 of them lie outside Qwen's B2 region. Edge d = 4a: (1,2,3,4), t=1/5 gives 1/5, 2/5, 2/5, 1/5. (This is just the five-runner analogue of S1, "all speeds within a factor 4"; Puck flags it for the chair, does not claim it.)

Neither seat self-labelled PROVED. F5 remains UNFINISHED.
