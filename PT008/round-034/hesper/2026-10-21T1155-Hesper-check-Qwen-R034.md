# Hesper check · R034 3/4 Qwen (parts 1626811e / 29531505 / 8e9fb79e; combined d3b478aa)
Facts only. CHECKED, not proof. Courier promotes nothing.

1. Qwen §2 (same-component windows disjoint) and §3 (endpoint proposition): author proofs, Qwen labels PROOF CANDIDATE. Algebra of §2 ((q+1−δ)L ≤ (q′−δ)R < (q+δ)L ⇒ δ>1/2) checked by hand: correct. §3 counting N(e⁻)=N₀+s, N(e)=N₀+r+s, N(e⁺)=N₀+r: correct (Qwen uses surviving counts consistently). Consistent with relay.py (0 violations).
2. §4.3 component counts (δ=1/5): (1,2,5) 2 components, (1,3,5) 3, (1,2,7) 4 — MATCH. (1,3,4) = two positive + two isolated — MATCH.
3. ERROR: Qwen says all three of (1,2,5),(1,3,5),(1,2,7) have U=2δ/ℓ ≤ b (empty target range). Exact: (1,2,5) U=10/3 ≤5 ✓; (1,2,7) U=7 = b ✓ (range empty); (1,3,5) U=15 > b=5 ✗ — longest component [11/25,14/25], ℓ=3/25, so (5,15) is a nonempty target range. Qwen's search therefore skipped a testable case. (Hesper R033 2CC count: every k=3 δ=1/5 integer input ≤15 needs ≤2 components, so (1,3,5) is not a 2CC counterexample.)
4. No counterexample to R1/R2/R3 or 2CC_k reported; Qwen states search was hand-only on 4 inputs (search failure, not non-existence). R2/R3 rules were stated but not tested.
