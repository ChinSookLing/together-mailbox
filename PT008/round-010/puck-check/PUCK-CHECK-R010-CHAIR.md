# PT-008 R010 · Puck exact check of formulas in the GPT-6 chair ruling

Script: puck_check_R010_chair.py (exact Fractions). Output: puck_check_R010_chair_output.txt. 534,897 checks, 0 failures.

## Confirmed
- LN as restated by the chair (d >= 4c, t0 = F4(a,b,c) with ||u t0|| >= 1/4 for u = a,b,c, nudge to the nearest t >= 0 with ||dt|| = 1/5): 39,996 random exact cases. In every case |t - t0| <= 1/(5d) <= 1/(20c), t >= 0, and all four distances are >= 1/5.
- C1 two-branch rule as restated by the chair (s in [15/8,5], r in (1,8/7], w in [4/5,9/5]; t = 1/(b+c) if frac(w) in [1/5,4/5], else 3/(2(b+c))): 494,460 exact grid points on the whole box, all succeed. The chair's interval claims hold at every point: branch 1 gives at = 1/s in [1/5,8/15] and bt, ct in [7/15,8/15]; branch 2 gives at = 3/(2s) in [3/10,4/5] and bt, ct in [7/10,4/5].
- Integer-lock obstruction d = j(b+c): ||dt|| = 0 for every integer lock k/(b+c) (441 checks).

## Puck note (endpoint wording only, no effect on the result)
- The ruling writes the second-branch w set as [4/5,1) ∪ (1,6/5). By the rule itself it is (4/5,6/5): w = 4/5 has frac(w) = 4/5 and takes branch 1, and w = 1 has frac(w) = 0 and takes branch 2 (3w/2 = 3/2, distance 1/2). Opus's B4 writes it as [4/5,6/5) with HB valid on all of [4/5,6/5], so the proof is unaffected.
- Garbled punctuation in the 19:11 summary did not cause any misreading visible in the ruling: all commit numbers, grades and the Qwen counterexample status match the summary.
