BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 16:57 +08
RE: 猜公式 Round 14 (packet 1473ae0), send text r14_send_full.txt or r14_send_short.txt
SEAT: lumo
MODEL: Lumo 2.0 Fast
CHAT: https://lumo.proton.me/u/25/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
=== FULL FINAL REPLY — PT005 Round 14 short version ===
Source: https://lumo.proton.me/u/25/c/1b04e910-acf8-481d-80b9-8deeab93d8db
Chat: PT005 · Big Picture (project "Play Civilisation Field")
Mode at send: Lumo 2.0 Max / Fast mode (Thinking mode tab inactive; Fast mode tab selected/active). Web search toggle: OFF (web-search-toggle checked=false).
Sent: 2026-10-11 ~16:51 +08 (same minute as system "Current time" line).
Reply finalized: ~16:52 +08 (Copy enabled, no stop button, no typing indicator; reply ends at "L2's uniform tail — everything downstream inherits its absence.").

--- VERBATIM REPLY STARTS ---

Worked through your question

1. Subgroup class (G_p, order-28 subgroup, p ≡ 1 mod 28).

Needed: every multiplicative coset C of G_p contains an element with |r| ≤ H = ⌊(p−1)/16⌋ (then U(G_p)=0 fails... conversely, one empty coset kills the cover).

Averaging computation: #cosets up to sign = (p−1)/56; small residues |r| ≤ H number 2H+1 ≈ p/8. Expected small elements per coset: μ = (p/8) / (p/56) = 7. So emptiness of a coset has naive probability e^{−7} ≈ 9×10⁻⁴ (hand: e⁷ ≈ 1096.6), and the expected number of empty cosets is ≈ 9×10⁻⁴ · p/56 ≈ 1.6×10⁻⁵ p — linear in p. So heuristically G_p ceases to be a cover well before p ≈ 60,000 (where expected empty cosets ≈ 1: solve 1.6×10⁻⁵ p = 1 → p ≈ 62,500), matching the data trend (281 covers, 449 already has 4 empty cosets).

To make it deterministic you need a bound on sums of the 28-torsion characters over the interval [−H, H]:

Pólya–Vinogradov: error ≤ √p·ln p per character. Main term per coset ≈ p/112 ≈ 0.0089p. Need √p ln p < 0.0089p, i.e. p > (112 ln p)². At p = 10⁶: ln p = 13.8, (112·13.8)² ≈ 2.39×10⁶ > 10⁶. At p = 10⁸: (112·18.4)² ≈ 4.26×10⁶ ≪ 10⁸. So PV suffices only for p ≳ 5×10⁶ (bracketing by hand). Failure: window of applicability.

Burgess (subconvex) pushes this down substantially (roughly to p ~ 10⁴–10⁵ range, order-of-magnitude) but is designed for intervals of length ≪ √p, awkward here since H ≈ p/16 is huge — in that regime PV is actually fine.

Weil-bound / DCFK-type equidistribution would give the right statement (uniform spread of subgroup elements among short intervals), but no off-the-shelf theorem gives every coset simultaneously — that's the missing piece.

UNFINISHED / OPEN.

2. Chair's IDEA — agree, both points.

Bounded differences: swapping one speed v → v′ changes U only at cells where v was the sole coverer; each speed is near at exactly H cells, so Lipschitz constant c_i ≤ H ≈ p/16. McDiarmid: Σc_i² ≤ 14·(p/16)² = 0.0547p². For deviation t = E − D ≈ 0.077p − δp, take t = 0.069p: exponent = 2t²/Σc_i² = 2(0.069p)²/(0.0547p²) = 0.174. So P(U ≤ E − 0.069p) ≤ e^{−0.17} ≈ 0.84 — no decay at all, versus the needed e^{−M} = e^{−38}. Constant exponent confirmed.

Janson: the bad events A_t = "cell t uncovered" are strongly positively correlated: cells t, t′ with t′ = t ± 1 share coverer whenever some v has ‖v(t−t′)‖ small; a single speed v is near at H consecutive-ish cells, so neighborhoods of unsafe cells overlap heavily → Δ ≫ μ, Janson's SRI never activates. Agree, and this is structural, not fixable by sieve variants.

3. Lemma chain for δ(p) ≥ δ.

L1 (PROVED, R10/R11):
Fourier identity U(S) = (p/2)Σ_{Σk_v v≡0} Πb̂(k_v); cover ⟺ R(S) = −M(p).

L2 (OPEN — hardest):
Frequency-truncation tail: |R(S) − R_K(S)| ≤ E_K(p) uniformly in S, with E_K = o(p). Needs control of the multiset of integer relations among 14 residues — no current tool (minorants break the 14-fold product; R11).

L3 (OPEN, entry point exists):
Extremal bound on R_K: sup_S(−R_K(S)) ≤ (1−δ)M(p). Dirichlet enters here: simultaneous approximation lets any 14 speeds be scaled so all lie in a box of side ≲ p^{13/14}+1 (pigeonhole on (v₁,…,v₁₃) mod v₁₄-class argument), which both restricts the candidate families to check and organizes which short relations can exist. Not yet a proof — the sup is over structured sets (457's run), and no optimizer bound exists.

L4 (trivial given L2+L3):
D(p) = min U ≥ M − sup(−R) ≥ δ·E(p) → γ(p) = 15 for p > P₀.

Hardest: L2. L3 has a clear attack surface; L2 currently has none.

4. Dependence on 16:

No — the chain is N-generic: replace H by ⌊(p−1)/N⌋, 14 by N−2, and the subgroup class by the order-N subgroup (expected small elements per coset = N/2·(N/2)/((p−1)/(N))… i.e., the analogue of μ=7 becomes N/4). Only constants and P₀ change. IDEA.

Least-sure step: L2's uniform tail — everything downstream inherits its absence.

--- VERBATIM REPLY ENDS ---

Note on verbatim fidelity: the reply above is captured from the chat DOM of the PT005 · Big Picture chat on lumo.proton.me. The "Worked through your question" thinking path was collapsed (its content is not part of the rendered reply). The model produced an attached file alongside the reply; this file's contents were not opened per the rules (only the chat's own text is the reply). The reply text was read from extract_content with region=near_viewport once the reply had finalized (Copy enabled, no stop button, no typing indicator), and the end matched the screenshot confirmation.
--- end verbatim ---
END LETTER
