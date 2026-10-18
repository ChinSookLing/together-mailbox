# REPORT R005 — Puck independent check: Argon 005C, Qwen 005B, Gemini 005A
Setting: circle length 1, ‖x‖ nearest-integer distance, g(t)=min_{u∈A}‖ut‖, n=|A|+1, success iff g≥1/n. Exact Fractions. Script: chk_r005_argon_qwen.py, output: output.txt. All three replies were on branch PT-008 (PT008/round-005/ files 1258 Argon, 1259 Gemini, 1300 Qwen); read in full.

## (a) Argon 005C — claim B "global optimum always has the fastest speed active" — DISPROVED, counterexample correct
V={2,4,15}, n=4 (threshold 1/4). Exhaustive exact check (candidate times m/(s+s') plus a fine grid of 38760 points, same answer):
- max g = 1/3, attained ONLY at t=1/6 and 5/6 (mod 1). There ‖2t‖=‖4t‖=1/3 and ‖15t‖=1/2 > 1/3, so speed 15 is inactive at every global maximiser. (t=1/3, 2/3 maximise {2,4} but give ‖15t‖=0.)
- So claim B as worded ("at every global max point the fastest speed is in the active set") is false. Argon's arithmetic is all correct. Only the global-optimum version is refuted; Argon's claim A (some local max involves fastest speed) and C (a success time exists using fastest speed) are not refuted.
- Claim C check: times with g≥1/4 among candidates: 16, of which 4 have 15 active (6/19, 6/17, 11/17, 13/19; g=5/19, 5/17, 5/17, 5/19, all ≥1/4). Max g over times where 15 is active = 5/17 < 1/3.
- Small wording fix: at t=3/19 (Argon's example, g=6/19) the active speed is 2 (‖2t‖=6/19; ‖4t‖=‖15t‖=7/19), not 15. t=3/19 lies on the 15t+4t=3 branch crossing but 15 is not the minimiser there. The claim "the 15-containing candidates can reach the threshold" is still true (see above), but 3/19 is not the best witness for "15 active". Use 6/17 (g=5/17).
- Remark: the counterexample is only about optimisation; it does not touch existence/construction of a success time.

## (b) Qwen 005B — n=4 triples a<b<c
- Family 1: c≤2a ⇒ t=1/(2c) succeeds. Family 2: b,c≤3a ⇒ t=1/(4a) succeeds. Proofs in the reply are correct (re-derived; fine).
- Exhaustive integer triples 1≤a<b<c≤60 (34220 triples): family 1 covers 8555, family 2 covers 15410, both 8555, either 15410 → coverage 45.03%. Violations: 0.
- Family 1 ⊂ family 2 (c≤2a implies b,c≤3a). So family 1 is redundant: t=1/(4a) works there too (though t=1/(2c) is a different time). Wording fix: don't present them as two separate families covering different ranges.
- 300 random rational triples (denominators ≤12): 0 violations. 300 more forced inside the families (real ratios): 0 violations. Boundary cases (c=2a, b=c=3a limits) pass.
- F(1,2,3) failure confirmed: F(1,2)=⌈3/3⌉/3=1/3, g(1/3)=0 (‖3·1/3‖=0); right time t=1/4, g=1/4 exactly (‖1/4‖,‖1/2‖,‖3/4‖=1/4,1/2,1/4). Qwen's three pair table checks: (a,b) t=1/3 g=0; (a,c) t=1/2 g=0; (b,c) t=1/5 g=1/5<1/4. All correct. Qwen's "no single 3-runner pair generates the 4-runner time for {1,2,3}" is true for this example only (the three pair times each fail), not a general theorem — keep the claim to the example.
- Qwen's UNFINISHED example (1,4,7), t=3/8: g=3/8 (success) but Qwen wrote ‖21/8‖=5/8; correct value is 3/8 (distance cannot exceed 1/2). Conclusion (≥1/4) unaffected; fix the typo.
- Side check: integer triples ≤40, every one has a success time among candidates m/(s+s') (0 failures), consistent with n=4 being true; (1,4,7) lies outside both families.
- Qwen's Section D "branch table grows with ⌈c/a⌉" is a prediction, unproved; leave as UNFINISHED. Families cover 45% of triples ≤60, so the c>3a region is the main remaining case.

## (c) Gemini 005A — review of F and T1′
- F: "PROOF VERIFIED" — agree (bounds, b≤2a/b>2a branches, bt=k−x identity; real speeds OK). Minor: the b>2a case argument "x ∈[1/3,2/3) so ‖x‖≥1/3" is right.
- T1′: Gemini says PROOF VERIFIED. Its proof of necessity (each local max has an active rising and falling branch, so t=(p+q)/(a+b)) is correct as a necessary condition, and it correctly says this is not a construction. Points to flag, none outright false: (i) it needs g(t0)>0 and the branch values p,q must be those of active branches with the common value on the lower envelope, which the statement as "formula = local maxima" omits; DeepSeek rated it PROOF INCOMPLETE for the bare formula (needs same-speed branches a=b, merged equal |speed|, common value 0<v≤1/2 on the lower envelope). Gemini's own text does say "necessary only", so it does not claim the converse, but the grade PROOF VERIFIED should be tied to the corrected statement "every local max has this form" (not "formula characterises"). (ii) In answer to the 'plateau' question it argues no flat maxima since 0∉A: correct. (iii) The phrase "公式精确覆盖了全部局部极大点" is fine for necessity but "精确" could be read as iff; reword. (iv) "g(t)>0, t>0" is assumed without stating how it is used. No incorrect mathematical statement found.
- Not an error but note: the "tightness is realisable" claim in the earlier Gemini review is separate and unchecked here.

## Summary
Violations found: none in Qwen's two constructions or Argon's counterexample. Wording fixes: Argon (3/19 witness), Qwen (family 1 ⊂ family 2; 5/8 typo; "no single pair" limited to {1,2,3}), Gemini (T1′ grade should attach to the corrected necessity statement).
