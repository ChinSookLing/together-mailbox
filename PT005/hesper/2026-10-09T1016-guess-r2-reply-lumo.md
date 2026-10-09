BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 10:16 +08
RE: 猜公式 Round 2 packet (aaa37b9), BEGIN…END block pasted verbatim
SEAT: lumo
MODEL: Lumo 2.0 Max (via Tuzi portal relay)
CHAT: https://lumo.proton.me/u/6/c/ccc5d5c2-449e-4b35-81ed-46c1bc6ef51c

--- reply verbatim ---
Source: Tuzi relay, pasted in chat 2026-10-09 10:16 +08 from her Lumo portal. Courier copied verbatim.

**Conclusions first: T1 is correct as stated. All three components check out, conditional on F5.**

**(1) Verdicts**

- **Lemma A: YES (PROOF).** LRC(14) is applied correctly with 13 speeds (14 runners including the stationary one ⇒ 1/14). Rounding: ‖wᵢt/p‖ ≥ ‖wᵢx‖ − wᵢ|x − t/p‖ ≥ 1/14 − M/2p. With p ≥ 56M this is exactly 1/16, and "too near" is *strictly* < 1/16, so ≥ 1/16 suffices; moreover exact equality would need 16wᵢt ≡ ±p (mod 2p), impossible by parity. Also t ≠ 0, else ‖wᵢx‖ ≤ M/2p ≤ 1/112 < 1/14. I checked line by line.
- **Lemma B: YES (PROOF).** Dirichlet with 13 targets, Q = N: some q ≤ N¹³ ≤ p−1 satisfies ‖qsᵢ/p‖ ≤ 1/N. q < p and p prime ⇒ q invertible. qsᵢ ≡ ±cᵢ with 0 < cᵢ ≤ p/N; cᵢ = ±c_j would give sᵢ ≡ ±s_j, excluded. Solid.
- **Final step: YES (PROOF).** F2 applies since q is a unit; the cᵢ are 13 distinct integers in [1, p/N]; Lemma A needs p ≥ 56p/N ⇔ N ≥ 56 ⇔ p−1 ≥ 56¹³. Wires connect cleanly.

**Caveat (not a flaw):** everything hangs on F5, the unrefereed preprint. T1 is a theorem *modulo that citation*.

**(2) Weakest step:** the dependency on F5. Internally, the tightest joint is the knife-edge 1/14 − 1/112 = 1/16 exactly — it works, but any slip in constants (e.g. LRC constant 1/14 → slightly less for 13 weights if the preprint's normalization differs) breaks it.

**(3) Best lever to shrink the threshold — the hybrid (d), via LP duality (IDEA):** for any p, fractional covers: assign weights w_t ≥ 0 to cells with every speed's total weight over its H near-cells ≤ 1; then γ(p) ≥ Σw_t. A feasible dual is a *polynomial-time checkable certificate*, verified by plain arithmetic. This replaces exhaustive search for the entire band 300 … P₁ and makes the data-threshold ~280 provable, cutting the 10²² gap at the cheap end. On the analytic side, lever (a) has real headroom: LRC optima sit on intervals, not points, so the rounding loss M/2p can be amortized over an interval — but I'd invest in the LP route first.

**(4) The 14 question:** Yes — γ(p) = 15 for all large p. T2 already proves γ ≥ 15 past ~10²⁹ (same F5 caveat), so 14-covers must die out; no infinite family. Note the ceiling: LRC(16) gives exactly 1/16 with zero margin, so this method can never prove γ ≥ 16. Since F3 caps γ ≤ 15, the answer settles at exactly 15 forever — just absurdly far out.

**(5) For Tuzi:** Build the LP-dual certificate machine — it converts "chair says ≥14" into checkable proofs for every prime from 300 upward, closing the practical end of the 20-order gap for the cost of linear programming, not exhaustive search.

--- end verbatim ---
END LETTER
