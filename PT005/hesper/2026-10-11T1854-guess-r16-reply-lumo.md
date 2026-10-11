BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 18:54 +08
RE: 猜公式 Round 16 (packet d712a00), send text r16_send_full.txt or r16_send_short.txt
SEAT: lumo
MODEL: Lumo 2.0 Lite Fast
CHAT: https://lumo.proton.me/u/11/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
[Captured from rendered page text (Copy button did not reach the agent clipboard); KaTeX math as rendered. Model Lumo 2.0 Lite, Fast mode.]

Line A · the constant

Adding one large speed.
Hand Computation:
Let K have c(K) intervals. Speed v removes ≈ v·L length from an interval of length L, specifically removing windows of width 1/(8v) centered at j/v. Then number of removed windows in [a,b] is at most ⌊v(b-a)⌋ + 2. Total loss ≤ ∑ (count_i · 1/(8v)) ≤ (v·m(K) + 2c(K)) / (8v) = m(K)/8 + c(K)/(4v). Thus m(K ∪ v) ≥ m(K) − (m(K)/8 + c(K)/(4v)) = (7/8)m(K) − c(K)/(4v). (PROOF)

Verification for K*:
K* = {1..15} \ {6}. m(K*) = 97/6864 ≈ 0.01413. c(K*) = 4 (given).
Check if (7/8)m(K*) − 4/(4v) ≥ 97/6864 for v > 30.
LHS ≈ 0.875·(0.01413) − 1/v = 0.01236 − 1/v.
RHS = 0.01413.
0.01236 − 1/v ≥ 0.01413 ⟹ −1/v ≥ 0.00177, impossible.

Result: The bound fails. Adding a large speed reduces the measure below m(K*) if we start from K*. The "floor" 97/6864 is not maintained by simply appending a large speed to the minimal 13-set. The minimal 14-set must be a different configuration, not K* ∪ {v}.

Conclusion: The strategy of extending K* fails. The global minimum might be a set where all speeds are small (e.g., K* plus a small replacement) or a different structure entirely. UNFINISHED regarding the proof of m(K) ≥ 97/6864 for all K.

Two or more large speeds.
Induction: Apply the bound iteratively. m(K ∪ {v₁, v₂}) ≥ (49/64)m(K) − … . The term (7/8)^k decays exponentially. If k speeds are large, the measure drops drastically unless m(K) was initially huge. The break point is when the decay (7/8)^k outweighs the initial measure. For k = 14, (7/8)^14 ≈ 0.15, which matches the random heuristic. The bound is too weak to prove a high floor like 0.014 for sets with many large speeds; it only supports the random lower bound.
IDEA (bound is structurally insufficient for high floors).

Line B · the threshold

Replace Dirichlet.
Instead of scaling all 14 speeds to ≤ Q ≈ p^{1/14}, scale only the first k speeds to be small, leaving 14−k large. Let k = 10. Scale so v₁, …, v₁₀ ≤ p^{1/10}. The remaining 4 are treated as "large" relative to the scaled grid.
Discrete bound: D(p) ≥ (p/2)m(K_scaled) − (grid error).
Grid error for 4 large speeds ≈ 4 × (interval count) × 1.
If m(K_scaled) ≥ 97/6864 ≈ 0.014, then D(p) ≥ 0.007p − 4c.
We need 0.007p − 4c ≥ 1.
With c ≈ 100 (max intervals for 10 speeds), 0.007p ≥ 401 ⟹ p ≥ 57,000.
If we use the "one large speed" logic recursively, we might push P₀ down.

Calculation: If we can prove m(K) ≥ 0.005 for all sets (conservative), then D(p) ≥ 0.0025p − C. For D(p) ≥ 1, p ≥ 400/C. If C ≈ 20, P₀ ≈ 800.

Smallest explicit P₀ I can derive: 10,000. (Assuming m(K) ≥ 0.001 and error ≈ 20). This is far better than 28·240^14 but still above the census gap. UNFINISHED on the exact constant without the full m(K) proof.

What would close it?
Lemmas needed:
- C-floor: m(K) ≥ 97/6864 for all 14-sets. (OPEN)
- Discrete-to-Continuous error: |U(S) − (p/2)m(K)| ≤ C_err where C_err depends only on |K| and max speed ratio. (OPEN, needs uniform bound on discrepancy).
- Scaling Lemma: For any set, there exists a scaling where the "effective" measure is preserved and max speed is bounded. (KNOWN via Dirichlet, but needs refinement).

Distance to 10^4: If C-floor is true, we are very close (just need to tighten the error term). If C-floor is false (i.e., m(K) can be arbitrarily small), then P₀ might not exist or be huge. The bottleneck is Lemma 1.

Summary:
The constant 97/6864 is likely the global minimum for primitive sets, but proving it requires ruling out "large speed" perturbations that the current linear bound cannot handle. The threshold P₀ is likely in the 10^4–10^5 range if the floor holds.

--- end verbatim ---
END LETTER
