# PT-008 R011 · Puck check of Track C (Argon 281229e) and Track D (DeepSeek e65a779, Gemini b5878c9)

Script: puck_check_R011_C.py (exact Fractions). Output: puck_check_R011_C_output.txt. 0 failures.

## Track C — Argon, (a,b,c,d) = (1,3,4,5)
- In the corridor: 4 < 5 < 16. Confirmed.
- Every time x/14, x/12, x/10 (that is, tau/(b+c), tau/(a+d), tau/(a+c) with tau integer or half-integer) fails: Puck finds no successful x mod 14, 12 or 10. Confirmed, and Argon's per-x failing runner lines are right.
- Success set in [0,1): exactly the two windows [11/25, 9/20] and [11/20, 14/25] (Argon wrote [0.44,0.45] and [0.55,0.56]). Confirmed, e.g. t = 9/20 gives 9/20, 7/20, 1/5, 1/4.
- Puck flag (not a grade): Argon's last paragraph says any finite-phase adaptive algebraic rule is DISPROVED. The example only disproves this particular menu (three anchors, tau in Z/2). For instance t = 9/20 = (9/4)/(a+c), a quarter-integer phase on the a+c anchor, works. The chair's rule against extrapolating applies.

## Track D — HB and C1 reviews
- DeepSeek (DeepThink, search off, e65a779): HB PROOF VERIFIED, C1 PROOF VERIFIED. Notes the else branch of C1 is w in (4/5,6/5), not [4/5,6/5); no effect.
- Gemini 3.1 Pro (Thinking High, fresh chat, b5878c9): HB PROOF VERIFIED, C1 PROOF VERIFIED. Same note on (4/5,6/5).
- Both match Puck's exact check (PUCK-CHECK-R010-A.md 935f7c8, PUCK-CHECK-R010-CHAIR.md 98c6b4c). The missing notation lines in Puck's review text (erratum send_011_trackD_erratum.md) did not stop either reviewer: both used s, r, w, theta, A correctly.
- Archive note for Hesper: the record headers give copy times 20:37 (Argon) and 20:47 (Gemini review) +08, later than the 20:12 +08 commits; please check those time stamps.

## Still open
- Track A (Opus) and Track B (Qwen) not yet in.
