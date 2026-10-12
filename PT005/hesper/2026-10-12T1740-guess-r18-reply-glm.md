BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 17:40 +08
RE: 猜公式 Round 18 make the gate cheap (packet ab3ea04), send text r18_send_glm.txt
SEAT: glm
MODEL: GLM-5.3 Deep Think Max
CHAT: https://chat.z.ai/c/c3a42880-545c-4f8d-a62a-6178d72a2446

--- reply verbatim ---
Chat URL: https://chat.z.ai/c/c3a42880-545c-4f8d-a62a-6178d72a2446
Model: GLM-5.3 (Deep Think Max)
sent ≈17:18 +08

[seam]

ANSWER BLOCK · Q4 (GLM lane) · conclusions first
[seam]

C1 · PROOF (deliverable). Lemma below: a closed form for the overlap of two bad sets {t: ⟨dt⟩ < c}, in which a short relation between the two large speeds appears as an explicit term. Rigorous base inequality: m(K₀ ∪ {v,w}) ≥ 1/(2|D*|), D* = distinct pairwise differences of the 14 speeds; every duplicate-type relation (v − w = u − u′, or v − u ∈ D(K₀)) deletes a value from D* and raises the floor.
[seam]

C2 · FACT (hand-computed, chair's set). Speeds > 30: 31, 42; gcd 1; 4·31 − 3·42 = 124 − 126 = −2. At c = 0.018 this relation is inert (it would enter only at c ≥ 2/73 ≈ 0.027): the pair's overlap is 2c/42 + 2(0.018/31 + 0.018/42 − 1/1302) = 0.000857 + 0.000484 = 0.001341 ≈ 1.04·4c² — essentially the independent value. Contrast (Lemma corollary): 7·30 = 5·42 = 210, so (30,42) reduces to (5,7), overlap 2c/7 = 0.00514 ≈ 3.97·4c².
[seam]

C3 · FACT (computed). D(K₀) = {1..12} ∪ {16..29} (26 values); 31 − K₀ adds exactly one value (30); 42 − K₀ adds nine (13, 31, 33, 34, 35, 37, 39, 40, 41); 42 − 31 = 11 ∈ D(K₀). So |D*| = 26+1+9 = 36 of 91 = 14·13/2 pairs, giving m ≥ 1/72 ≈ 0.0139 — just under L18's 97/6864 ≈ 0.0141 (chair's 0.018234 is theirs, MEMORY, not mine).
[seam]

C4 · IDEA+FACT (where a relation-only inequality must fail). The live optimum (C2) has coprime, mutually far v, w: the v–w term is empty there. The binding structure is 3-term: v − w = u − u′ and v = u + d against the baseline (C3).
[seam]

C5 · FACT (caveat). Start-version m is impossible here: averaging gives m ≥ 1/28 ≈ 0.0357 for any 14 integer speeds (each bad set has measure 2c; 28c < 1), above 0.0183 — so m must be difference-based or rescaled (packet does not restate it; my transfer to it is IDEA). Arc-merge certificate on the chair's set: UNFINISHED.
[seam]

Lemma · PROOF. For integers d, d′, 0 < c ≤ ½, g = gcd(d,d′), (d₁,d₁′) = (d,d′)/g: μ{t: ⟨dt⟩<c ∧ ⟨d′t⟩<c} = Σ min(c/d₁ + c/d₁′ − |j d₁′ − k d₁|/(d₁d₁′), 2c/max(d₁,d₁′)) over j < d₁, k < d₁′ with |j d₁′ − k d₁| < c(d₁+d₁′). Proof: t ↦ gt mod 1 preserves measure; bad sets are arc unions (j/d₁ ± c/d₁); intersect termwise; (j,k) ↦ j d₁′ − k d₁ is injective mod d₁d₁′ (coprimality), so each small δ occurs once. Corollary (PROOF): a relation a·d₁ − b·d₁′ = δ₀ with b < d₁, a < d₁′ contributes min((c(d₁+d₁′) − |δ₀|)/(d₁d₁′), 2c/max) — the asked-for explicit term. C2's check: only δ ∈ {0, ±1} contribute (42·17 − 31·23 = 1).
[seam]

Inequality · PROOF. μ(⋃_{d∈D*} B_d(c)) ≤ 2c|D*|; if this is < 1 an uncovered t exists, so m ≥ c; c = 1/(2|D*|) gives C1. Exact refinement: merge all arcs and measure the union directly (UNFINISHED here).
[seam]

Last question · IDEA. Build the depth-10 "cannot finish with 4 more classes" feasibility cut (fractional-cover test before descending): the chair's node table puts ~90% of nodes at 11–12 classes, so I expect ~5–10× fewer nodes — unmeasured.
[seam]

Citations. Allikvere 2609.02604, Beck–Everett 2609.06259, chair data: MEMORY (this packet; no web this run, nothing READ). All other numbers are my own hand computations, shown inline.

--- end verbatim ---
END LETTER
