BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-08 18:15 +08
RE: 猜公式 Round 2 packet (aaa37b9), BEGIN…END block pasted verbatim
SEAT: gemini
MODEL: Gemini Pro Extended (new chat; old chat 418ef994 gone), text read from page
CHAT: https://gemini.google.com/app/5b35481411c2e38f

--- reply verbatim ---
Chat URL: https://gemini.google.com/app/5b35481411c2e38f
Model/mode shown: Pro Extended
Copy source: read from page text (single continuous reply; copy button under the answer did not surface in the clipboard reader). No splicing — the reply is one block ending at the "Pro Extended / Gemini is AI and can make mistakes..." disclaimer.

----- BEGIN REPLY -----

1. Referee T1

Answer: YES (The proof of T1 is correct).

Lemma A: YES

Verification: If x satisfies ∥wᵢx∥≥1/14, and t is chosen such that ∣x−t/p∣≤1/(2p), then by the triangle inequality:

∥wᵢt/p∥=∥wᵢx−wᵢ(x−t/p)∥≥∥wᵢx∥−wᵢ∣x−t/p∣≥1/14−M/(2p)

Since p≥56M, we have M/(2p)≤1/112. Thus ∥wᵢt/p∥≥1/14−1/112=7/112=1/16.
Because ∥wᵢt/p∥≥1/16, no speed wᵢ is "too near" at cell t (since "too near" strictly requires ∥vt/p∥<1/16).

Boundary Check: t≢0(modp) because if t≡0(modp), ∥w₁t/p∥=0<1/16, contradicting ∥w₁t/p∥≥1/16.

Lemma B: YES

Verification: Applying Dirichlet's simultaneous approximation theorem to the 13 ratios s₁/p,…,s₁₃/p with limit N=⌊(p−1)^{1/13}⌋ yields an integer 1≤q≤N¹³≤p−1 such that ∥qsᵢ/p∥≤1/N.

Signs & Uniqueness: Each qsᵢ(modp) falls in an interval around 0 of radius p/N. Representing elements mod p in (−p/2,p/2], this means ∣(qsᵢmodp)∣≤p/N. Since 1≤q≤p−1 and p is prime, gcd(q,p)=1, so q is invertible mod p. Since s₁,…,s₁₃ are distinct mod p up to sign (in {1,…,n}), their images cᵢ=∣qsᵢmodp∣ are non-zero and distinct in [1,p/N].

Final Step: YES

Verification: N≥56⟹p−1≥56¹³⟹p>56¹³. All steps hold rigorously.

2. Shrink the Threshold
(a) Better Margin & Good Intervals (PROOF)

Instead of just sampling a single integer t nearest to xp, we observe that LRC(14) guarantees a continuous open interval of real numbers x where all ∥wᵢx∥>1/16.

Proof: Since x↦∥wᵢx∥ is 1/wᵢ-Lipschitz, if ∥wᵢx₀∥≥1/14, then for any x∈(x₀−δ,x₀+δ),

∥wᵢx∥≥1/14−Mδ

Setting 1/14−Mδ=1/16 yields δ=1/(112M).

The length of this valid real interval is 2δ=1/(56M).

A discrete cell t/p will land inside this interval as long as the interval length 2δ is strictly greater than the step size 1/p.

Requirement: 1/(56M)>1/p⟹p>56M. This recovers the same factor of 56, confirming that discrete rounding losses cannot be further reduced without changing the core LRC constant.

(b) Better Scaling via Cover Structure (IDEA / PROOF SKETCH)

A set S={s₁,…,s₁₃} being a cover means that every cell t∈{1,…,n} has at least one sᵢ∈S such that ∥sᵢt/p∥<1/16.

By F1, each speed covers exactly H=⌊(p−1)/16⌋ cells. The total coverage capacity of 13 speeds is 13H≈(13/16)p<(p−1)/2=n.

Combinatorial Obstruction: 13H<n for all p. Thus, no 13-speed set can ever cover all cells if the coverage sets were disjoint. However, speed coverage sets overlap heavily.

Shrinking q via Massed Distribution: Rather than applying generic Dirichlet approximation to arbitrary 13 numbers, we exploit the fact that a cover must be uniformly distributed in a precise structural sense. By Fourier/character sum bounds (e.g., Polya-Vinogradov type bounds), if M≪p^{1/2}, small speeds {1,…,M} have high visual density near 0, leaving large gaps in cell coverage elsewhere.

(d) Hybrid Approach (FACT / PROOF)

To bridge the gap between theoretical limits (p∼10^{22}) and empirical observations (p≈280):

Interval Certification via Bounding q: For p∈[300,P₁], check for the existence of a multiplier q∈{1,…,p−1} that maps candidate 13-covers into structured low-norm sets, or check the linear programming relaxation of the coverage condition.

Fast Filter (Branch and Bound): The gate engine does full exhaustive search. A fast filter checks necessary conditions for coverage:

A valid 13-cover must satisfy ∑_{i=1}^{13} 1_{∥sᵢt/p∥<1/16}≥1 for all t.

Summing over all t, we need ∑_{t=1}^{n} ∑_{i=1}^{13} 1_{∥sᵢt/p∥<1/16}=13H≥n, which fails for 13<16 unless H rounding allows it, but 13⌊(p−1)/16⌋<(p−1)/2 is always true.

Therefore, a cover is mathematically impossible if cells are treated with uniform weight without overlap. Overlaps reduce effective coverage further.

3. The 14 Question

Verdict: γ(p)=15 for all sufficiently large p.

Reason (PROOF via T2 / LRC(15)):

By F5 (LRC(15)), for any 14 distinct positive integers w₁,…,w₁₄, there exists a real x such that ∥wᵢx∥≥1/15 for all i.

Theorem T2 establishes that for any p>120^{14}, no 14-speed set can form a cover because 1/15−1/16=1/240>0, leaving a non-empty gap where no speed in S is within 1/16 of a cell t/p.

Combined with F3 (γ(p)≤15 via {1,…,15}), γ(p) is strictly bounded between 15 and 15 for all large p. Thus, 14-covers cannot exist for large p, and γ(p)=15 eventually holds universally.

4. One Sentence for Tuzi

The single most promising lever is Lever (b) — exploiting the global tiling/density constraint of covers via character sums or structural rigidity, because generic Dirichlet approximation treats S as an arbitrary set, whereas a cover's severe capacity deficit (13H<n) forces its elements to be far more structured and tightly approximable than generic integers.

Weakest step: Lever (b) structural scaling proof (currently an IDEA/SKETCH, awaiting rigorous character sum lower bounds).

----- END REPLY -----
--- end verbatim ---
END LETTER
