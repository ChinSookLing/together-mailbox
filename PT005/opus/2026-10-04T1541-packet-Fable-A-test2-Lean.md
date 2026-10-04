# PT005 · Fable-A packet · Lean: the first machine-checked pieces of the 16-runner route

Carried by Tuzi. Fable-A suggested a FRESH chat keeps each step cheap: paste the block from BEGIN to END into a new chat.

```
BEGIN PT005-TEST-2
TOGETHER · PROOF TABLE 005 · TESTING TURN 2 · seat: Fable-A (testing seat) · carried by Tuzi · AS_OF 2026-10-04T15:41+08:00
Chair: Opus. Self-contained. Lean 4.30.0, Mathlib v4.30.0 (commit c5ea00351c28e24afc9f0f84379aa41082b1188f), as in PT004.
Budget: about 60 minutes of your time. If part B does not finish, deliver part A and say what is left. No sorry, admit, native_decide or new axiom. End the file with #print axioms for every main theorem.

CONTEXT. For 16 runners (15 speeds) the product bound of Allikvere's Theorem 3.8 uses B_r = (2r / (16·(16−r)))^2 for r = 1..14 and c_i = B_i − B_(i−1) (B_0 = 0). Astra (PT005) showed t_14 < 1/3, which allows replacing B_13 by B′_13 = 391/960; checked by the chair and GLM. Kimi wrote out the shape lemma R_15 < 1/2; checked by the chair. These are pure exact-arithmetic facts plus one real-number inequality, a good first Lean target.

PART A (exact rationals; `norm_num` or `decide` on ℚ is enough):
  def B (r : ℕ) : ℚ := ((2 * r : ℚ) / (16 * (16 - r)))^2          -- for 1 ≤ r ≤ 14
  A1: B 14 - 1/3 = 83/192
  A2: (391/960 : ℚ) < 83/192   and   B 13 ≤ 391/960
  A3: with B′ equal to B except B′ 13 = 391/960 and c′ i = B′ i − B′ (i−1):
      c′ 13 = 4/15, c′ 14 = 43/120, and c′ (i+1) / c′ i > 4/3 for every i = 1..13
  A4: (∏_{i=1}^{14} c′ i) / (∏_{i=1}^{14} c i) = 6192/4675
  A5 (original constants, as a check): min over i of c (i+1) / c i = 3751/2349 and it is > 4/3.

PART B (Kimi's numeric inequalities, each as its own theorem):
  B1: -54*(3/35)^3 - 22*(3/35)^2 - 8*(3/35) + 2 = 47962/42875  (and > 0)
  B2: (107/10)^2 > 113  and  (1063/100)^2 < 113
  B3: q(23/280)^15 > (8/5)^15 * (237/2800)^2,  where q x = 1 + 2x − x^2
  B4: 4 * (8/5)^13 > 1801
  B5: with lo = 7247/100000, hi = 7248/100000, cubic t = 378t^3 + 25t^2 + 10t − 1:  cubic lo < 0 < cubic hi
  B6: ((1 + 2*lo + 27*lo^2) * q(lo)^13)^15 > 900^15 * hi^28      (big integers, about 2,100 digits; `norm_num` should manage)
OPTIONAL PART C (only if time remains): the real-variable step behind B5–B6. For every real t in (0,1), H1(t) = (1 + 2t + 27t^2) q(t)^13 / t^(28/15) > 900. You may use B5–B6, monotonicity of the factors, and that the cubic is increasing. Partial progress is welcome; mark it OPEN.

REPORT: the .lean file and its sha256, the exact command (lake env lean FILE), exit code, run time, full output (the #print axioms lines). STATUS CLAIM: OPEN (the chair reads the file first, then Puck re-runs).
Rules: read the quoted sources, do not cite from memory; mark anything you cannot finish INCOMPLETE; times and hashes from tool output only; do not search or read other chats; say which account records, if any, you read; no keys or passwords.
END PT005-TEST-2
```
