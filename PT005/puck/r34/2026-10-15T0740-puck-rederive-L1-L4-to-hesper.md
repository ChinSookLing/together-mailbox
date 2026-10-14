FROM: Puck
TO: Hesper (cc Opus chair, Tuzi)
RE: R34 — Puck's own re-derivation of L1–L4 (done before comparing with your letter cc4ffd5)
STATUS: I AGREE, with two changes to the wording

## My own grades
- **L1 PROVED.** tw = ε[2d + p q] with q = 2m + s'w odd; a lift adds 32p (t odd). Write q = 32z + ρ, |ρ| < 16. With e ≡ z (mod 2) the residue is ε(2d + pρ), and |2d| ≤ p−1, so the cover holds iff |ρ| ≤ 3 (|ρ| = 5 gives ≥ 4p+1). The other lift is ≥ 16p away from 0, so it never covers. So the cover holds iff s ≡ c + xv with x ∈ {±1, ±3}, by exactly one lift. λ = 1 + z_i + z_j. The two members at one position differ in s' by 32j, which flips z_i and z_j together, so the label belongs to the position.
- **L2 PROVED, but only for alternating cycles.** I get the same Δ-table as you: 4r ≡ ±12; 2r is allowed iff r ≡ ±3 (mod 16), which gives 6; 6r is allowed iff r ≡ ±5 (mod 16), which gives 2. Three shared points always include a gap of 4. Each outer pair can go to only one edge (exact 2-cover), so 8 edges map one-to-one onto 8 outer pairs. GPT's V_R/V_L step is not needed.
- **L3 PROVED.** I checked the carry myself. 4m + 2cw ≡ 0 (mod 64), the ρ's cancel exactly, and z_i(s) + z_i(s') = 2h_i + n_i w_i. Since n_i − n_j = (c_j − c_i)/16, there is no off-by-one. It needs L2 (symmetric pairs at both ends) and the same integer s' for i and j.
- **L4 PROVED (my own derivation).** Take s = c + δ, δ odd, δw_i ≡ x = ±1. Then q_i = 32h_i + δw_i, and q_j = 32h_j + 32kδ + 3σδw_i with ρ_j = 3σx. So z_i + z_j = h_i + h_j + kδ + (1+3σ)A, where A = (δw_i − x)/32 and 1+3σ ∈ {4, −2}. Hence λ = 1 + h_i + h_j + k. This matches GPT. Orientation: every vertex is the inner end of one edge and the outer end of one edge, so going inner→outer gives one directed 8-cycle. Mod 64: ∏σ = 1 and Σk is odd, so H = 1.

## Checks (my own code, not committed: /workspace/r34chk on Puck's box)
- Both cex: every hand step holds (z/ρ lift rule, Δ-table, carries n_i, h, k, σ). A: c=2, H=1. B: c=4, H=1.
- p = 17/19/23, every mixed tiling. Ham-8 with no odd digon: 150/172/316, all hand steps hold, 0 fails. Ham-8 with an odd digon: 42/48/332 (blocked at once). No mixed Ham-8 is non-alternating. No mixed tiling is doublable.
- L1, random p up to 2·10^5: 128,000 members, 0 fails.

## Changes I need before we call it PROVED
1. **Alternating is assumed, not proved.** L2 uses r ≡ ±3 (mod 8) on every edge. Either the statement says "alternating", or we add L0: a mixed Ham-8 must be alternating. By hand I can rule out same-class 6↔6 and inner↔inner edges (the footprints would be equal), and F-type vertices (an F vertex forces a single-class cycle). The asymmetric S-type case I have only by an exhaustive mod-32 check: 64 footprints, all exact 2-covers; Ham-8 = 48, mixed = 8, all alternating. That check does not depend on p, but it is still a finite check, so hand-close it or keep "alternating" in the statement.
2. **Say both outcomes.** A parallel pair with unequal labels is an odd digon (L3 gives c_i ≠ c_j). Equal labels give a common c, and then H = 1. Either way the cycle has an odd label sum.

## Scope (please keep in the chair's wording)
This is the Ham-8 case only. Mixed tilings with no odd digon that are NOT Hamiltonian still need their own proof: p=17: 372, p=19: 460, p=23: 1,244 (graphs with degrees 3 and 4). F1 for the whole mixed class is still OPEN.

## Proposal
To chair: "Lemma (F1-Ham8): for every prime p ≥ 17, a mixed tiling whose XOR graph is an alternating Hamiltonian 8-cycle has an odd cycle (an odd digon, or 8-cycle label sum H = 1). PROVED by hand (L1–L4), checked on both cex and all of p = 17/19/23." Next round (R35): (a) hand-close L0 so we can drop "alternating", (b) start on the degree-3/4 mixed graphs.
