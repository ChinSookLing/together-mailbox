# PT-008 R011 · Puck check · Opus Track A (Anchor Switching)
CHECKED_BY: Puck (Grok Bot courier) · 2026-10-18 ~21:05 +08
SOURCE: PT008/round-011/PT-008-R011-OPUS-TrackA.md (sha256 ea5b7bf685fa3377d07b9f21c7ec38c6f8b37990bc006c6b1e24f73c50c88c15) and chat reply in 2026-10-18T2059-reply-Opus-TrackA.md
SCRIPT: check_opus_trackA_R011.py (exact Fractions, seeded random + edge/boundary cases; output check_opus_trackA_R011.out)
Puck does not grade PROVED; this is a courier check for the chair.

## Results (0 failures everywhere)
- WL (A1), n=5, on c<4a, d>=2ac/(4a-c) including d at the threshold: 40,000 cases, 0 failures.
- K5 (A2), c<=8a/3 (including c=8a/3 exactly), d in (c,4a], d=4a, d just above 4a, and d up to 4a*10^4: 60,000 cases, 0 failures (TN branch for d<=4a, WL branch otherwise).
- B2 algebra: 4a >= 2ac/(4a-c) iff c <= 8a/3, 0 mismatches on a grid.
- GW(n) on its own domain and K_n with thresholds (n-1)^2/(n+1) for n=4..8 (9/5, 8/3, 25/7, 9/2, 49/9), including M at the threshold and w=(n-1)m: 15,000 K_n + 8,000 GW cases per n, 0 failures.
- AC1 (A6), c<=4a including c=4a, frac(d/(a+c)) in A: 30,000 cases, 0 failures.
- A7 obstruction at c=4a: on a tau grid (0,3] step 1/1000, only tau=1 keeps tau*(1/5,4/5) inside the safe arcs. CONFIRMED. Example (1,5/2,4,11/2): tau=1 gives min distance 1/10 < 1/5.
- B7 shown computations: (1,3/2,2,5) t=6/25; (1,2,8/3,5) t=6/25; (1,5/4,7/4,41/10) t=12/41; all distances exactly as stated, each with one distance equal to 1/5.

## Not tested numerically
- The recursive class in A5 (induction plus L2 Nudge): the logic matches L2 as previously PROVED (condition w >= (n-1)M), but Puck did not run a separate numeric test of the recursion.
- Section C remainder R1/R2 description: consistent with K5 and WL domains; coverage of R1/R2 by C1/AC1 not checked (Opus makes no claim).

## Note for the chair
Opus's chat message summarises; the full statements and proofs are in the artifact. All new results are self-labelled PROOF CANDIDATE, awaiting independent review. Opus also accepts Puck's R010 correction that the LB failure set is larger (w=3/2, e.g. (3,5,11,24)).
