BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 14:01 +08
RE: 猜公式 Round 10 (packet 0104439), send text r10_send_full.txt or r10_send_short.txt
SEAT: glm
MODEL: GLM-5.3 Deep Think High
CHAT: https://chat.z.ai/c/c1437b0d-c8b6-42a9-8381-c17c2252250d

--- reply verbatim ---
Model: GLM-5.3, Deep Think High (retry; first attempt with Deep Think Max in chat ff57c06f gave thinking only, no final). Very-short text (includes Hesper's +43.21 check fact).
Chat: https://chat.z.ai/c/c1437b0d-c8b6-42a9-8381-c17c2252250d

Conclusion first: the formula is character orthogonality; short relations are dead as an explanation; a no-cover theorem needs one global bound on long relations.

1. PROOF. Expand B(x)=p⁻¹Σ_k b̂(k)ω^{kx}. Then U(S)=(1/2)Σ_t Π_v [p⁻¹Σ_{k_v} b̂(k_v)ω^{k_v v t}] and Σ_t ω^{(Σk_v v)t}=p·1[Σk_v v≡0 mod p], giving U(S)=(p/2)Σ_{Σk_v v≡0} Π b̂(k_v). ∎

2. IDEA — no. FACT: the ≤4-term truncation is +43.21 (needs −35.39) and matches random sets (+40): short relations carry no cover-specific signal. Instead sum the complement — the shell of relations with many nonzero k_v — grouped by orbit under scaling t·S mod p and weighted by divisor/lattice-point counts, so the many tiny b̂(k) terms are estimated collectively, not enumerated.

3. UNFINISHED — yes, in principle. Strategy: show R(S) ≫ −M(p) uniformly, since M(p) is exponentially small. Missing step: a large-sieve/dispersion bound showing high-weight relations (≥5 nonzero coefficients) cannot contribute enough negative mass to cancel M(p).

4. IDEA for Tuzi. Fourier turns "product of indicators + additive vanishing" into an exact resonance spectrum indexed by integer relations, where Poisson gives only average spacing. Least-sure step: tail control — proving the sum over large |k| genuinely converges rather than hiding the cover there.

--- end verbatim ---
END LETTER
