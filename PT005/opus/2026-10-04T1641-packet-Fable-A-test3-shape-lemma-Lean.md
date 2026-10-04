# PT005 · Fable-A packet · testing turn 3 · rest of the shape lemma in Lean (not urgent)

Carried by Tuzi to the same Fable-A chat that did test 2.

```
BEGIN PT005-TEST-3
TOGETHER · PROOF TABLE 005 · TESTING TURN 3 · seat: Fable-A · carried by Tuzi · AS_OF 2026-10-04T16:41+08:00
Chair: Opus. Self-contained. Lean 4.30.0, Mathlib c5ea00351c28e24afc9f0f84379aa41082b1188f. Build on your PT005.lean (sha256 d5c5d22e…be7505, PROVED-LEAN, approved by Tuzi 16:35, wall line 45). You may import or copy its definitions.
Budget: about 60 minutes. Deliver what is finished and mark the rest OPEN. No sorry, admit, native_decide or new axiom; #print axioms for every main theorem.

GOAL. Finish the shape lemma R_15 < 1/2 in Lean: for every u : Fin 15 → ℝ with all u_i ∈ (0,1] and some u_i = 1,
   H u = (Σ_i w(u_i)) · Π_i a(u_i) > 900,
   where q x = 1 + 2x − x^2, a x = q x / x^(2/15) (real power), w x = x^2 / q x.
Your partC already covers the one-variable Case 3.

STEPS, in order of value (each its own theorem):
D1 (single variable): ∀ x ∈ (0,1], a x > 8/5.
   Facts you may use (chair-checked with sympy):
   - d/dx log a = 2(14x^2 − 13x + 1) / (15x(x^2 − 2x − 1)). The denominator is < 0 on (0,1).
   - So a decreases on (0, u1], increases on [u1, u2] and decreases on [u2, 1], where u1, u2 = (13 ∓ √113)/28. Hence min over (0,1] = min(a u1, a 1) with a 1 = 2.
   - For a u1 > 8/5 use 23/280 < u1 < 237/2800 (from your B2: (107/10)^2 > 113, (1063/100)^2 < 113), q increasing on (0,1), and your B3: q(23/280)^15 > (8/5)^15 · (237/2800)^2.
   - A route that avoids the exact root u1: let l = 23/280 and h = 237/2800, so l < u1 < h < u2.
     - On [l, h]: a x ≥ q(l) / h^(2/15) > 8/5 (q is increasing; x^(2/15) ≤ h^(2/15); B3).
     - On (0, l]: 14x^2 − 13x + 1 > 0, so a is decreasing there and a x ≥ a l, which is covered by the previous case.
     - On [h, 1]: a rises up to u2, then falls to a 1 = 2, so a x ≥ min(a h, 2).
     Any other sound route is fine.
D2 (Case 2): if all u_i ∈ (0,1] and at least two indices have u_i = 1, then H u > 900.
   Use w ≥ 0, w 1 = 1/2, a 1 = 2, a > 8/5 (D1). Then H ≥ (k/2)·2^k·(8/5)^(15−k) ≥ 4·(8/5)^13 > 1801 (your B4).
D3 (Case 1, single variable): L x = q(x)(1 − 13x + 14x^2) / (15x^2(1+x)) is strictly decreasing on (0, α], where α = 3/35 > (13 − √113)/28.
   Chair-checked: dL/dx = −2(7x^5 + 14x^4 − 27x^3 − 11x^2 − 4x + 1) / (15x^3(x+1)^2). The quintic is > 0 on (0, 3/35] (drop 7x^5 and 14x^4; −27x^3 − 11x^2 − 4x + 1 is decreasing and equals 23981/42875 > 0 at 3/35, half of your B1's 47962/42875).
STRETCH (only if time remains):
D4: the reduction. At a minimiser of H on {u ∈ (0,1]^15 : max u_i = 1}, all coordinates below 1 are equal and lie in (0, α). Then assemble D2 + partC (+ the case "all u_i = 1", where H = (15/2)·2^15) into the full theorem.
   This needs existence of a minimiser (H → ∞ as a coordinate → 0) and the one-coordinate analysis (β, φ) from the author's template. It is the hardest part; partial progress is welcome.

REPORT: the .lean file and its sha256, command, exit code, run time, full output. STATUS CLAIM: OPEN (the chair reads, then Puck re-runs).
Rules: read the quoted sources, do not cite from memory; label FACT / ESTIMATE / IDEA; mark gaps INCOMPLETE; times and hashes from tool output only; do not search or read other chats; say which account records, if any, you read; no keys or passwords.
END PT005-TEST-3
```
