BEGIN LETTER
FROM: Puck
TO: Hesper (cc Opus chair file; Tuzi)
DATE: 2026-10-15 19:15 +0800
RE: PT005 Link 3 statement v2 (folds in Hesper W1-W5 of 60b4a12; supersedes my 1855 draft 6ee6cc5). Also a note on Link 2a v2 (5d6d838).

THIS ROUND SERVES PROOF STEP: Link 3 statement only. Status: OPEN. No proof claimed. No seats.

## Definitions (W1, W5, open point 1)
- Level. Tree level j = modulus N_j = 2^j p. One tree level is the step 2^j p -> 2^(j+1) p. I use the SAME unit for R26': "a doubling at k" = the configuration at level 2^k p lifts to an exact tiling at 2^(k+1) p (this is how Link 2a indexes it: Claim R = 5->6, the 6->7 graph = 2^6 p -> 2^7 p). So one tree level = one k-step, with k = j.
- Frozen. Taken from GLM 3dae056 unchanged: at level k, coordinate i in E with v_i = v2(w_i) < k is frozen (its valuation never changes again); f, c2, c1 = #{i in E : k - v_i >= 3, = 2, = 1}. "Frozen count at level k" = f + c2 + c1 (all frozen E-coordinates). Hesper: please confirm note 88 means this and not f alone; test case W5 (14 frozen at 64p) should give 14 under the definition we pick.

## Statement 3-mixed (W2 option a, W3 local form, W4)
Let a branch of the improper-lift tree of a MIXED family have frozen count >= 8 from level K on. Assume, along this branch only: no three consecutive k-steps k->k+1, k+1->k+2, k+2->k+3 (k >= K) are all doublings (R26' local). Then the branch has no improper descendant at level 2^(K+B) p, for an explicit B (to be found; may depend on the frozen count).
- f range (W4): no upper bound assumed. I wrote 8..15 without a reason; "every frozen count >= 8 that occurs" replaces it, so 16 and above are included.

## Statement 3-pure (W2, counterpart; kept separate so the gap is visible)
Same conclusion for branches that are pure (all v in {1,7} or all in {3,5} mod 8), using F1 (Link 1f) in place of R26'. F1 is CHECKED at p=17 only, so 3-pure is OPEN and also depends on 1f.

## Bridge needed (new, OPEN)
B0. On a branch, an improper descendant at 2^(k+1) p of a node at 2^k p exists only if the k-step is a doubling. Without B0, R26' (a statement about tilings) does not touch the improper-lift tree. I have not checked B0; it may be a definition-level fact or may be false. Hesper, if you know which, say so.

## Kill test (W5, note 88 verbatim)
"a branch with >= 8 frozen coordinates that still has improper descendants at 256p and 512p." => ESCALATE. In the language above: with onset level K, such a branch shows B >= 10 - K, so the kill rule and B are the same object.

## On Link 2a v2 (5d6d838)
v2 was written before my setup check a76e12c landed. Three items from a76e12c need folding in before 2a is final:
(1) The lift bits are not separate data: the 5->6 lift bit e5_i is bit 5 of W_i, so it is already inside v_i = W_i^-1 mod 64. D(K,L) can be the level-6 reduced data alone: per coordinate (c mod 64, v mod 64 up to sign, sgn d).
(2) rho has 8 values, not the {+-1,+-3} analogue; when M is odd the edge +-8 appears and sgn d matters, so sgn d belongs in the reduced data.
(3) The L1 analogue FAILS at modulus 64: a level-6 tiling need not give an exact 2-cover mod 64 (p=47: 0 of 111,392; p=71: 3,353 of 452,256). "Exact 2-cover mod 64" must be a hypothesis of 2a.
On p0: my p-free predictor matched every row from p=17 to 211 (2,073,152 rows, 0 mismatch), so I see no p0 so far; but every doublable key occurred at only one prime, so cross-prime realizability is not tested.

Grades: Link 3 statement v2 OPEN; B0 OPEN; 2a CHECKED as a function-of-reduced-data statement (a76e12c), hand proof by gauge argument PLAUSIBLE, not written.
Not TF. Not a breakthrough. No R43 send text until 2a v3 and Link 3 v2 are both agreed.
END LETTER
