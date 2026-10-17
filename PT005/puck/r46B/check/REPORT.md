FROM: Puck  TO: Hesper (cc Opus, Tuzi)  TIME: 2026-10-18 05:35 +08
RE: PT005 R46 Track B — independent check of the chair's printed fibre-runner model (packet 85461bf)

VERDICT: printed model WRONG at one boundary (CHECKED by Puck); fractional-phase fix CHECKED (0 mismatches).

PROOF (two lines). With T = a + p s, alpha = a u mod p, c = (a u - alpha)/p, we have exactly
  T u = alpha + p (u s + c)   (integers), so  T u mod N = alpha + p x,  x = (u s + c) mod 2^d,  N = 2^d p.
Direct coverage 16 ||T u||_N < N  <=>  x + alpha/p < 2^(d-4)  or  2^d - x - alpha/p < 2^(d-4).
For alpha > 0 this is  x in [0, 2^(d-4)-1]  or  x in [2^d - 2^(d-4), 2^d - 1]  — an arc of exactly 2^(d-3) phases (= 1/8, Theorem NZ).
The printed strict symmetric test ||x||_{2^d} < 2^(d-4) accepts only 2^(d-3) - 1 phases: it drops x = 2^d - 2^(d-4).
So the printed model even contradicts Theorem NZ's 1/8 count. Correct form: ||u s + c + alpha/p||_{2^d} < 2^(d-4)
(Astra and DeepSeek), equivalently the half-open arc above. For alpha = 0 (p | u) the printed test is right.

FACT (chk.py, seed 20261018, 20,000 random (p,k,v,u,a) with p in {3..23}, k 5..10, all s): 3,334,656 comparisons,
1,840,464 at d >= 5. Printed model: 19,266 mismatches at d >= 5 (326,702 incl. d <= 4, where the packet already says
a separate description is needed). Fixed model: 0 mismatches at every depth. Both seat examples reproduced:
Astra p=17 M=2176 T=201 w=228 (||Tw||=132 < 136, covered); DeepSeek p=17 M=1088 T=511 w=2 (66 < 68, covered).

GRADES (Puck): Astra GAP-found CORRECT; DeepSeek GAP-found CORRECT (+ Theorem NZ CORRECT, not re-read by Puck this round);
Grok "identity, 0 mismatches" WRONG. Chair's "461 checks, 0 mismatches" cannot be with the printed rule; the oracle
used there probably already had the fractional phase — chair please check.
NOT CHECKED by Puck: Astra's 2,688 / 24 split (single-fibre vs cross-fibre death) and its 16 / 8 minimal blocking sets.
These are the interesting new numbers; worth a K11 or Puck recount before anyone uses them.
GPT seat still generating at 05:30; Copilot waits for GPT.
