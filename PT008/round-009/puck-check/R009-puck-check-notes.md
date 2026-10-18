# PT-008 Round 009 · Puck check of Tracks B, C, D (exact Fractions)
FROM: Puck · 2026-10-18 ~17:55 +08 · script R009_puck_check.py, output R009_puck_check_output.txt
Inputs: Track D 92fa87a/1c09ea5 (DeepSeek, Gemini), Qwen Track B 9c30bcf, Argon Track C 53cb768, Hesper letter 3209af7.
Result: 4575 exact checks, 0 failures. Puck checks are supporting evidence, not PROVED; chair decides.

## Track D (n-runner lemma, b <= (n-1)a, t = 1/(a+b))
Both reviews PROOF VERIFIED, with n = total runners incl. reference, n >= 2. Puck grid check n = 2..8, equality b = (n-1)a and a = b included: 0 failures. Agrees with Puck's earlier check (34f13ba). DeepSeek wording note: "all runners" should read "reference vs each non-reference runner".

## Track B (Qwen)
- Region 1 (z <= 4, t = 1/(1+z)): correct; it is the known d <= 4a lemma restated, nothing new.
- Region 2 (1 < x < 5/2, x < y < z < 5 - x, t = 1/(x+z)): proof correct, BUT it adds no coverage: z < 5 - x < 4, so Region 2 lies entirely inside Region 1. Seat's self-label PROVED is the seat's own; the region is redundant.
- Region 3 candidate (4 < z <= 9, t = 2/(1+z), x, y outside the open interval (2(1+z)/5, 3(1+z)/5)): checked as an exact iff on a grid, 0 failures; endpoints included correctly (distance exactly 1/5). Correct as PROOF CANDIDATE; it is the k = 2 lock of runners 1 and z.
- Section 4 (IDEA) numbers are wrong: with k = ceil((1+z)/5) the forbidden band for x has width 2(1+z)/(5k), about 2 (not about 2/5), with period about 5, so roughly 2/5 of x values are bad (Puck exact count z = 24: 796/2299, about 35%), not about 8%; the "0.6% joint failure" estimate is unsupported.
- Section 5 (IDEA) layer formula off by one: k = ceil((1+z)/5) = k exactly when 5k - 6 < z <= 5k - 1, not (5k - 1, 5k + 4]. Also each layer has several forbidden bands per variable, not one.

## Track C (Argon)
- CE1 (1,2,3,5): t = k/5 kills d for every k; t = k/6 fails for every k mod 6; t = 1/4 works. All correct.
  Correction: t = 1/4 = 1/(a+c) is itself a lock (runners a and c), so "non-lock / unrelated denominator 4" is wrong. What is shown: the fixed b+c lock and the fixed a+d lock each miss this example. It does not show that every single fixed lock pair misses it (the a+c lock catches it).
- CE2 (1,2,4,5): t = 1/3 works; at t0 = 1/5 phases are 1/5, 2/5, 1/5, 0. Every shift t0 + e with 0 < e < 1/10 breaks c, every t0 - e with 0 < e < 2/5 breaks a (checked exactly on a 1/1000 grid). First working time after 1/5 on a 1/600 grid is 3/10. Correct as a local-tweak obstruction (Argon's own range e < 1/20 is safely inside). Argon does not infer F5 is impossible.

Track A (Opus) not yet included in this check.
