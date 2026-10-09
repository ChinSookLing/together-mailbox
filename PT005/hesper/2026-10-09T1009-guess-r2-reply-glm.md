BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 10:10 +08
RE: 猜公式 Round 2 packet (aaa37b9), BEGIN…END block pasted verbatim
SEAT: glm
MODEL: GLM (chat.z.ai, via Tuzi portal relay; model label not shown)
CHAT: https://chat.z.ai/c/85432466-232e-4546-b6f2-cfd2086927b6

--- reply verbatim ---
Source: Tuzi relay, pasted in chat 2026-10-09 10:09 +08 from her chat.z.ai portal (GLM). Courier copied verbatim.

Yes — exactly. One turn, one reply; there is no "reply 2 unless you prompt." So the fix is: **push blocks out inside a single reply, front-loaded, with minimal pre-thinking.** Doing that right now — this is the whole Round 2 answer, complete:

**(1) Referee verdicts.**
- **Lemma A: YES (PROOF).** LRC(14) is used correctly (13 speeds ↔ 14 runners). The rounding chain ‖wᵢt/p‖ ≥ 1/14 − M/(2p) ≥ 1/16 needs p ≥ 56M ✓. Strict/non-strict is fine: "too near" is < 1/16, so ≥ 1/16 suffices, and the parity argument handles equality anyway. t ≢ 0 because ‖w₁t/p‖ ≥ 1/16 > 0 ✓.
- **Lemma B: YES (PROOF).** Dirichlet gives q ≤ N¹³ ≤ p−1, q a unit, ‖qsᵢ/p‖ ≤ 1/N. Distinct-up-to-sign is preserved because q is a unit: qsᵢ ≡ ±qsⱼ ⟹ sᵢ ≡ ±sⱼ, excluded. cᵢ ≥ 1 since p ∤ qsᵢ.
- **Final step: YES (PROOF).** F2 scaling is legitimate (cell permutation preserves ‖·‖), Lemma A applies with M = p/N, N ≥ 56 ⟺ p−1 ≥ 56¹³ ✓. T1 stands. T2's arithmetic also checks (1/15 − 1/16 = 1/240, p ≥ 120M).

**(2) Weakest step:** Lemma B, line 1 — not because it's wrong but because it's *lossy*: Dirichlet's p^(12/13) blowup is exactly where the threshold grows from ~280 to 10²². Second weakness: T1 inherits F5, which is computer-verified, not human-checked.

**(3) Best shrink lever (IDEA):** (b) with F2 normalization. A 13-cover must satisfy 13H ≥ n with total slack 5(p−1)/16 — tight overlap structure. Quotient the search by F2 (p/2 scalings) and by ±t, and force one normalized representative small; this turns "no 13-cover" into a certificate search of roughly p² size instead of exponential — plain-Python feasible far past 300, though not to 10²². Honest label: practical certification, not a proof for all p. Pure-math route: 13 Bohr sets of density 1/8 with step sizes ≤ p/56 covering Z_p is a rigid combinatorial configuration — likely provable directly, but I won't claim it inside this budget.

**(4) 14 question (IDEA):** γ(p) = 15 for all large p. Reason: T2's method already gives it beyond 120¹⁴, and the same rigidity argument that kills 13-covers applies a fortiori to 14 — but the true threshold is probably astronomically below 10²⁹, so an infinite 14-cover family seems unlikely though unproven.

**(5) For Tuzi:** Take lever (b) — F2 scaling quotient — because it converts the 20-order-of-magnitude gap into a p²-sized certificate the gate engine can actually run.

--- end verbatim ---
END LETTER
