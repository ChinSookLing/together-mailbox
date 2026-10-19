# Hesper check · R020 1/4 Opus + R019 2/4 Qwen supplement (facts only; courier promotes nothing)
Opus R020 reply sha256 aa4edfc049695089… (journal machine copy). Qwen R019 supplement sha256 614cd6cf8caa7519… (transcribed from chat message; journal copy not yet available — re-hash pending). Qwen labels it "第 1 段 / 共 2 段" but ends "（全文完）".
Script hesper/chk_r020_opus_qwen.py, output chk_r020_out.txt (exact Fractions).
Opus Track A:
- PS* (outsider u = a,b,c,d in turn, integer quadruples 1..30): 27,405 total, E* = 1,689, PS* outputs 0 failures. Matches Opus. Opus examples (1,2,3,4),(1,3,4,5),(1,3,4,7) all in E*.
- The 6 untransferred quadruples are all in E* and each has some successful time (sanity only). Transfer counts 1,201 / 482 NOT re-checked (UNFINISHED here).
Opus reviews:
- Q-ERC1 strict counterexample θ=1/5, w=7/5, m=1: non-strict R={1,2,3,4}, strict R=∅. CONFIRMED.
- |A_7| = 4 < 21/5. CONFIRMED (|A_q| ≥ 3q/5 false at q=7).
- Q-ERC2(b) strict counterexample V5 shape m=5: non-strict R={3,4,6,9,11,12}, strict R=∅. CONFIRMED.
Qwen supplement (§4.3 w=M!):
- θ=1/3, w=M!, τ∈(1/m)ℤ: for M=3..6 every m≤M has empty (non-strict) safe set — CONFIRMED (follows since τw∈ℤ). First m with strict-nonempty set: M=3→4, M=4,5,6→7.
- Scope note: this bounds the lattice denominator for integer w→∞ (τ=k/m parametrisation). It is not the θ→0 claim the chair DISPROVED for Argon.
- Qwen still states Q-ERC1 "complete proof" and Q-ERC2 "PROVED" for minimal m; Opus review found gaps (§1.3 step 3/4, density argument). Status words are the chair's.
