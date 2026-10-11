BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 09:21 +08
RE: 猜公式 Round 7 (packet 1006d95), send text r7_send_full.txt or r7_send_short.txt
SEAT: glm
MODEL: GLM-5.3 Deep Think Max
CHAT: https://chat.z.ai/c/885e0ce0-3aa4-4e81-bcd9-be426ac37300

--- reply verbatim ---
**1. C-core4 — conclusion: unproved. Delivered: PROOF of M15 ≥ 2 for all p ≤ 419, plus a band lemma; I believe C-core4 true.**
PROOF (≥2): total small-speed visits over the n scalings = 14·15 = 210; if every scaling had ≤ 1, total ≤ n < 210 for p ≤ 419 — pigeonhole ⇒ M15 ≥ 2. (421/457 exhaust counting.)
PROOF (band lemma, normalize 1 ∈ S): speed 1 covers exactly t ≤ H. Any t ∈ (H,2H] forces i ≥ 1 and v ≥ (p−H)/2H > 7 ⇒ v ≥ 8; one window there holds ≤ 2H/9 cells (best v = 9), so ≥ 5 distinct speeds ≥ 8 meet band 1 (cap for v ≫ H needs equidistribution — IDEA).
UNFINISHED: pinning them into [8,16]. Escapees: i ≥ 2 families (v ∈ [16,32],…) — 389 genuinely uses 28, 29 there. Coprimality plus band-2/3 incidence budgets (≈8 each, only 13 speeds) should pinch; not closed. If ≥ 4 land in [8,16], at most one is 16, so with speed 1 that gives M15 ≥ 4. Counterexample hunt: covers whose band 1 avoids [8,16] entirely.

**2. IDEA: 4 = ⌈(N−1)/4⌉ at N=16** — band (H,2H] has H cells, covering speeds have v ≥ (N−1)/2, reach ≤ 2H/v. Guess: (N−2)-covers satisfy M_{N−1} ≥ ⌈(N−1)/4⌉ (N=8 ⇒ 2, N=32 ⇒ 8). Floor is extremal; observed mode 5–6 sits above it.

**3. IDEA:** 1365 cores; Σ_{v∈K}1/v ≥ ½-type band filters kill most instantly; outer 10 speeds pin to octave candidates ⇒ ~10⁸ ops vs C(n,14) ≈ 10²¹ (~13 orders) — conditional on C-core4. Die-out IDEA: architecture is p-scale-covariant except edge slack (p mod 16; leftover cells 8H+1..n); past p ≈ 430 slack can't close residual gaps ⇒ predict none past 457 (409–457: 1 each = tail).

**4. IDEA:** extrapolate 307 (mean 5.38), flattened toward 4: M15=4: ≈220 (range 140–330); 5: ≈650; 6: ≈430; 7: ≈130; 8: ≈20; 9: ≈5; 10: 0–2. Largest: 9 (range 8–10), confidence ≈55%. Least-sure steps: unbiasedness of 307's random 274; smoothness of the M15-law across the 337→347 abundance cliff.

--- end verbatim ---
END LETTER
