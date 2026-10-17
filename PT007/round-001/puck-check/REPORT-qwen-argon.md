# PT-007 Round 001 — Puck independent check of Qwen and Argon replies
Replies: PT007/round-001/2026-10-17T1333-qwen-reply.md, ...1334-argon-reply.md (branch PT-007). Code: check2.py, output: output.txt (exact Fractions, small tests only; tests are finite, not proofs unless noted).

## Qwen
| Claim | Grade | Scope / gaps |
|---|---|---|
| Scaling: t0 in S(V) => t0/c in S(cV) | PROVED (trivial, one line) + CHECKED 400 random exact cases | Needs **c>0** (or t0/|c|). Qwen states c≠0; for c<0, t0/c <0 is outside t>=0 (Hesper's note is right). Fix: t0/|c| works (checked); F(cV)=F(V)/|c|, matching F({u})=1/(2|u|). Q: "c=1/u1 normalisation" should be 1/|u1|. |
| Time shift does not preserve safety (V={1,2}, t0=1/3, s=1/6) | CHECKED | t0 ok, t0+1/6=1/2 gives ||2t||=0. Valid counterexample to unconditional shift. |
| Recursion from a single old solution fails | CHECKED (consistent with Opus B2, Argon A) | Statement is about "direct" inheritance only. |
| Explicit {1,q}, q integer >=2, threshold 1/3: t=1/3 if 3∤q; t=(3j+1)/(9j) if q=3j | CHECKED for q=2..2000 (exact) and algebra re-derived by hand: PROVED for all integers q>=2 | Algebra correct (t<1/2 iff j>=1, ||qt||=1/3). Only integer q; t>=0 automatic. Not a general formula. |
| Sec C sufficient condition 2η>=1/|w| (η=min ε_i/max|u|, ε_i=||u_i t0||-1/(m+2)) | CHECKED: 167 cases where condition holds, 0 violations (window [t0-η,t0+η]∩t>=0); condition fails in 1328/1495 (89%) random cases | Qwen itself says not general. Tiny gap: it uses closed window and needs η>0, and t>=0 (window may dip below 0 only if t0<η; not seen). Essentially same as Opus A4/B4 but without the fast-newcomer ratio. |
| Q3 IDEA: t=k/((m+1)a_max) solution exists for gcd=1 positive integers | UNFINISHED (IDEA). No counterexample in 241 sets (m=2,3, entries<=12) and 69 sets (m=4, entries<=8) | Finite evidence only; "k found in O(m) steps by per-speed filtering" is unsupported. Note for integer V, t is periodic mod 1, so k ranges 1..(m+1)a_max: a search, not a formula. |
Overall Qwen: nothing wrong; contributions are modest (scaling, {1,q}); status UNFINISHED as Qwen says.

## Argon
| Claim | Grade | Scope / gaps |
|---|---|---|
| A: old time stays valid — refuted by V={1}, t=1/2, w=2 | CHECKED / DISPROVED (assumption A), exact | ||1/2||=1/2>=1/2; after adding 2: ||1||=0 < 1/3. Correct and identical to Opus B2. Refutes "always", not any particular safe-update rule. |
| C: F(V∪{w}) is a function of only (F(V), w) — "structural proof" it fails | **Proof is INVALID; claim UNFINISHED (not proved)** | The adversary picks u* with u*t'∈Z and ||u*t0||>=1/(m+1), but never shows some V containing u* has F(V)=t0 *for the given F*. Counter-check: for m=1, F({u})=1/(2|u|) determines |u| from t0, so g(t0,w) trivially exists (400... 200 exact tests, 0 failures: g recovers u=1/(2t0) then solves). "Info loss" only occurs if F is non-injective; Argon assumed that without proof. What can be said: for a *fixed natural F*, C may fail; for *all* F it is open. Also Argon's closing claim "construction must depend on lcm / full spectrum" is not supported (reals have no lcm). |
| B: threshold-lowering expansion always cancels new runner | Not addressed in Argon's text (only used as Q3 IDEA). Qwen Sec C: condition fails 89% of random cases; Opus B3/B4 show measure argument reaches only 1/(2m). Not settled by Argon: UNFINISHED. |
| D: simple scaling/shift of old time works for any new speed | Not addressed by Argon. My check: any w-independent τ is killed by w=1/τ (||wτ||=0): DISPROVED for the w-independent version; w-dependent rules not excluded. Qwen's shift example also kills unconditional shift. |
| E: finitely many local safety conditions imply a common safe time | Not addressed by Argon. Exact check: V={1,2,3}, δ=1/3: all pairs feasible, triple infeasible (grid 1/3600, and integer speeds => period 1, safe sets are unions of closed intervals with endpoints in multiples of 1/6; matches Opus B1): DISPROVED for δ=1/3 (note actual LRC threshold for m=3 is 1/4, so this refutes the Helly-style principle, not LRC). |
| Q3 IDEA: expansion-buffer measure Δt≈1/(n(n+1)v_i) cuts w's safe phase | IDEA, UNFINISHED | The buffer width equals Opus A4 r_u=1/((m+1)(m+2)|u|) (consistent). As stated ("always suffices") it is the same sufficient condition Qwen showed fails often; needs a hypothesis (speed ratio gap) — which is Opus's Fast Newcomer / Two-Scale route. Not testable as written ("切中 w 的安全相量" is vague). |
| "Q2: PROVED" in answer block | Overclaim | Only A is proved (and by an example); C is not. |

## Surprising / errors
1. Argon's C proof is the one real error (see above). Argon's own ANSWER BLOCK rates it PROVED.
2. Argon covered only A and C of A–E; B, D, E left to others. Opus covered E (and A); I added D (w-independent) check.
3. Qwen's scaling needs c>0 (sign error; harmless).
4. Qwen's "q>=2 hand-verified" claim holds for all q to 2000; nothing surprising.
No breakthrough; no unified F; both seats are consistent with Opus's R001 (sparse-speed constructions only).
