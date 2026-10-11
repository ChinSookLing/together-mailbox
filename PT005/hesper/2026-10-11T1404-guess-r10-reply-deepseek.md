BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 14:04 +08
RE: 猜公式 Round 10 (packet 0104439), send text r10_send_full.txt or r10_send_short.txt
SEAT: deepseek
MODEL: DeepSeek DeepThink
CHAT: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202

--- reply verbatim ---
## DeepSeek Round 10 reply — PT005 · Big Picture

Chat URL: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202
Account: csllanna@gmail.com (Log in with Google, phone approval on Apple iPhone 11 Pro Max)
DeepThink: ON (pressed=true)
Search: OFF (pressed=false)
Confirmation of completion: send button became disabled, no "Thinking" indicator present on the Round 10 reply, reply ended with "Least-sure: the exact 457 partial sum." and the new-message textarea was active for the next turn.

---

### Full final reply (verbatim, final rendered reply only — not the thinking trace)

ANSWER BLOCK
Q1.
PROOF: Expand B(vt) = ∑_k b̂(k) e(kvt). Multiplying and summing over t ∈ Z/p leaves only ∑_v k_v v ≡ 0, giving U(S) = (p/2) ∑_{∑ k_v v ≡ 0} ∏_v b̂(k_v). The b̂ values follow from the geometric sum over |j| ≤ H.
Q2.
UNFINISHED: At 457 the obvious dominant short relations are 4·114 + 1 ≡ 0, the run relations 112 − 111 − 1, …, 117 − 116 − 1, and variants like 2·114 − 112 − 116. I cannot give the exact partial sum without running code. Random 14-sets have almost none; 307/337 covers have fewer, longer relations.
Q3.
IDEA: A budget is |R(S)| ≤ ∑_{m ≥ 2} (14 choose m)(2A)^m (1/8)^m, where A bounds coefficient size. A cover needs |R| ≈ M(p) ∼ 0.077 p, so it forces Ω(p) short relations. This can explain rarity and vanish-off, but not yet 457 exactly.
Q4.
IDEA: Proving "for p > P0, no 14-set has R = −M" seems plausible via a uniform short-relation bound. Dirichlet scaling enters as the worst case: scaling speeds to p^{13/14} creates many short relations, so any proof must control that regime. Not proved.
Q5.
IDEA: Fourier adds exact resonance/cancellation; Poisson only gives the expected uncovered-cell term.
Least-sure step: the exact 457 resonance sum and the constants in the budget.

Reasoning
FACT: The Fourier identity is exact. PROOF: B is a function on Z/p; the product expansion and orthogonality give the relation sum. FACT: b̂(0) = 1 − (2H+1)/p, and for k ≠ 0, b̂(k) = −(1/p) sin(π(2H+1)k/p) / sin(πk/p).
FACT: For p = 457, H = 28, so 2H + 1 = 57, and M(457) = (457/2)(1 − 57/457)^14 ≈ 35.39. IDEA: The relation 4·114 + 1 ≡ 0 is the signature of the scaled run 111..117 → 1, 3, 5, …, 13. FACT: The run gives many three-term relations v − (v − 1) − 1 ≡ 0. Each has small Fourier weight, but there are several. IDEA: They likely dominate the first few percent of R(457). The exact total −35.39 probably requires many longer relations too.
FACT: A random 14-set has no such designed run, so its resonance sum is typically much smaller than M(p). IDEA: That is why random sets fail to be covers. The 281 subgroup cover has many multiplicative relations; the 337 cover has only M_15 = 3, so its relations are weaker.
IDEA for Q3: To cancel M(p) ∼ 0.077 p, the number of short relations must grow linearly with p. If one can prove that for p > P0 every 14-set has too few short relations, then γ(p) = 15 for p > P0. FACT: Lemma B says any 14 speeds can be scaled to size p^{13/14}. IDEA: That scaling makes additive relations more likely, so it is exactly the case a proof must handle. UNFINISHED: no such uniform bound is proved here.
Least-sure: the exact 457 partial sum.
--- end verbatim ---
END LETTER
