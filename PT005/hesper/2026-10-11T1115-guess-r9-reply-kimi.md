BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 11:16 +08
RE: 猜公式 Round 9 (packet ec15a2d), send text r9_send_full.txt or r9_send_short.txt
SEAT: kimi
MODEL: Kimi K3 High (after stop + nudge)
CHAT: https://www.kimi.ai/chat/1a1231e4-7012-87e0-8000-09ce1972343a

--- reply verbatim ---
[Courier note: original turn looped on code and produced no ANSWER BLOCK; stopped and nudged with: "Please stop now and give the final reply: ANSWER BLOCK first (≤300 words) with Q1–Q4 using whatever you have (mark UNFINISHED where needed), then ≤300 words reasoning. Label FACT / PROOF / IDEA. Name your least-sure step." Reply to the nudge follows.]

ANSWER BLOCK

Q1. Formula: P*(N) ≈ 2n*+1 where n* solves ln C(n−1, N−3) = κ·n·e^{−2(N−2)/N} ("canonical sets × Poisson survival = 1"), one fitted constant κ = 1.20 (set so N = 16 gives 457 exactly). Errors vs best-known death lines: N=17: predicts 503, observed 479 (+5%); N=18: predicts 551, observed ≥ 523 (consistent); N=20: predicts 647, observed ≈ 661 (−2%); N=8: predicts 113, observed 113 (exact). RMS relative error ≈ 3% on the four testable points.

Q2 (search only, 10–30 restarts/prime — "found" is fact, "none" is not proof; nothing here exhaustive): P*(8) ≈ 113 (survivors 61,67,73,83,89,109,113; none found 127–270); P*(9) ≈ 127; P*(10) ≈ 131; P*(11) ≈ 167; P*(12) ≥ 229 (none found at 241). Model vs these: overshoots ~15–25% at N = 9–12 — consistent with my searches missing rare covers there.

Q3. P*(22): point 745, range 690–800. P*(24): point 843, range 780–910. Confidence ≈ 60% that each range contains the chair's observed death line (the 150 s/prime search may cut off a few percent early; ranges are centered slightly above to compensate).

Q4. IDEA: a death region, not a cliff — at N=16 zeros start at 383 yet 457 survives; at N=20, 641/653 dead but 661 alive. Late survivors have arithmetic structure: p ≡ 1 (mod N) (subgroup covers, GPT's mechanism: 661 = 20·33+1; also 521, 541) or p = km ± 1 with small k (run family: 457 = 4·114+1), plus high capacity-ratio classes (s ∈ {2,4}).

Least-sure step: P*(24)'s point — the model's N-dependence rests essentially on κ fitted at one exact point (N=16) plus noisy search lines; a systematic drift of ±8% is plausible by N=24.

Reasoning

FACT: κ = 1.202 fitted so the model hits 457 at N=16; the same κ then lands within 5% at N=17, 18, 20 without refitting — the N-dependence enters only through the set count C(n−1, N−3) and the exponent 2(N−2)/N, so this is a genuine one-constant transfer, not a per-N fit.

PROOF-sketch (model origin): canonical (N−2)-sets number C(n−1, N−3); each cell is uncovered by a random set with probability ≈ e^{−(N−2)H/n} = e^{−2(N−2)/N} (constant in p at fixed s), so expected uncovered U ≈ n·e^{−2(N−2)/N} grows linearly in n while log-set-count grows like (N−3) ln n; their crossing is the death line. FACT: the observed decay at N=16 (×~0.25 per +16 in p at fixed s) matches this form.

IDEA (Q4 detail): scattered survivors occur where window wraparounds align — p = km ± 1 makes modulus k's folded table hit short residues, and p ≡ 1 (mod N) makes the order-N subgroup a near-cover; both are lattice-coincidence events that thin but never strictly stop, so P* is ragged.

UNFINISHED: exhaustive verification of the small-N death lines; the N=20 line above 661.

--- end verbatim ---
END LETTER
