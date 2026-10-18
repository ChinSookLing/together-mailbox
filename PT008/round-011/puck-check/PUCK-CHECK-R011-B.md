# PT-008 R011 · Puck check · Qwen Track B (ce7eec3)
CHECKED_BY: Puck (Grok Bot courier) · 2026-10-18 ~21:00 +08
SOURCE: PT008/round-011/2026-10-18T2051-reply-Qwen-TrackB.md (filed by Hesper, ce7eec3)
SCRIPT: check_qwen_trackB.py (exact Fractions; output check_qwen_trackB.out)
STATUS LABELS: Puck does not grade PROVED; this is a courier check for the chair.

## Results
1. (3,5,11,24): integer lock t=k/16 fails for every k (0 successes mod 16); half-integer lock t=(2k+1)/32 fails for every k (0 successes). CONFIRMED.
   - Wording flag: the ANSWER BLOCK says the best gap is 5/32; exact best min-distance over both locks is 3/16 (= 6/32), still < 1/5.
   - t=1/5 gives positions {3/5, 0, 1/5, 4/5}, min pair distance exactly 1/5 (equality). CONFIRMED.
2. ANSWER BLOCK "key theorem" (strict half-integer solution k0+1/2 and some r_pq in (2/5,3/5) imply integer tau1=2k0+2 works with margin >= 1/10): FALSE. 18,928 counterexamples among integer speeds with d<40; first: (2,3,4,5), S=7, k0=1 (tau0=3/2 strict), tau1=4 gives min distance 1/7 < 1/5. Qwen's own §2 reaches the same conclusion, so the ANSWER BLOCK contradicts the body.
3. §2 arithmetic error: sub-cases A1 and B1 treat the fractional part as the distance to the nearest integer. Example r=1/2, delta=1/20: 2/5+2delta+r = 1, true distance 0 (Qwen counts it as >= 2/5).
4. §3 "exact obstruction condition" is inverted. Exact rule (verified on 59,301 grid points, 0 mismatches): with f = frac(r*tau0), r in (2/5,3/5), tau1 = 2tau0+1 fails on that pair iff f in (1/5, 3/5 - r/2) or f in (9/10 - r/2, 4/5). Qwen's set (1/5, 1/5+(3/5-r)/2) U (4/5-(r-2/5)/2, 4/5) mismatches on 19,800 of those points.
5. §4 theorem (no open set where half-integer succeeds and integer lock fails): NOT VERIFIED. The density claim for the integer-success set is asserted, not proved; the final step (line 175) only shows one of the three d-terms is >= 1/5, while all six constraints are needed. Also note: with integer k unbounded and real speeds, "integer lock" over all k in Z is close to the full problem when the ratios are rationally independent, so the statement needs a precise definition (bounded k or a fixed finite menu) before it can be judged.
6. §6 pointwise criterion is a restatement of the definition (true, but not a new sufficient region).
7. Header flags from Hesper stand: model shown as Qwen3.7-Plus although sent as Qwen3.8-Max Thinking; seat self-labelled PROVED against the brief's rule.

## Puck summary for the chair
Track B gives no new sufficient region. Confirmed: (3,5,11,24) fails both integer and half-integer locks. Refuted: the ANSWER BLOCK key theorem (exact counterexample (2,3,4,5)). Errors: §2 sub-cases A1/B1 and the §3 formula. Unproved: §4.
