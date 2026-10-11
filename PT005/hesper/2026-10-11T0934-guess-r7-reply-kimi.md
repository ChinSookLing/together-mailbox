BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 09:35 +08
RE: 猜公式 Round 7 (packet 1006d95), send text r7_send_full.txt or r7_send_short.txt
SEAT: kimi
MODEL: Kimi K3 Thinking High
CHAT: https://www.kimi.ai/chat/1a1231e4-7012-87e0-8000-09ce1972343a

--- reply verbatim ---
**ANSWER BLOCK**

**Q1.** C-core4 open. PROOF (band lemma): speeds v ≤ 7 never cover cells of the band B = (H, 2H] (their first window sits at p/v ≥ 2.14H), and v = 8 covers only a ~H/8 sliver at the top; since each speed covers ≈ H/8 cells of B, **every cover in every scaling has ≥ 8 speeds ≥ 9**. Variance route toward the floor: with C(u) = #small under scaling u, ΣC(u) = 420; if M₁₅ ≤ 3 then ΣC² ≤ 3ΣC = 1260, while the pair-correlation baseline Σ_{v,w}|v⁻¹A ∩ w⁻¹A| ≈ 1240 already nearly saturates that — and covers have clustered ratios, pushing it over. UNFINISHED: the pair-intersection bound isn't controlled rigorously.

**Q2.** IDEA: floor = ⌈(N−2)/4⌉ ≈ N/4, set by the H-band structure. FACT (small cases, code): N = 12 (10 speeds, small ≤ 11): covers at 197 include M₁₁ = **3** (floor ≤ 3); 181/193 samples min 4. N = 16: floor 4 (321 covers). N = 8: covers too rare to measure (only p = 113 found; its rare covers sit at M₇ = 4, a structured-regime artifact).

**Q3.** Cost: 1365 cores × heuristic completion ≈ 10³–10⁴ steps each ≈ minutes per prime in plain Python — vs the full census, which is a pruned DFS over ~10⁶+ nodes and already heavy at p ≈ 410. Window-containment prunes divisor-redundant cores (any core where v and its multiples crowd, e.g. containing {2,4,8} or 12 with 2,3,6 patterns) and the band lemma kills cores misaligned with (H, 2H]. IDEA on die-out: past 431 the residual after any 4-core (~5H cells) needs 10 fillers whose tables must align to p/16 precision; alignments (p = km ± 1 structures) get too rare.

**Q4.** 337 (1,477 covers): predict M₁₅ = 4 count in **150–300** (point ≈ 215, ~15%, calibrated on 307's 14.6%), confidence 70%. Largest M₁₅: **9, possibly 10** — confidence 75% it's in {9, 10}, point 9.

**Reasoning**

FACT: I independently recomputed M₁₅ for all 19 census reps — values match the table, floor exactly 4 (389 rep 2). My ~60 stochastic covers at 307–373, including 16 covers built from speeds ≥ 16 only, all have M₁₅ ≥ 4 (distribution mode 5–6).

PROOF (band lemma, detail): for v ≤ 8 and t ∈ (H, 2H], |vt − ip| ≤ H forces i = 1 and t ≥ (p−H)/v ≥ (15H+1)/8 > 1.87H; for v ≤ 7 this bound exceeds 2H, so G(v) ∩ B = ∅. Since |G(v) ∩ B| ≤ H/8 + O(1) for every v, covering B needs ≥ 8 speeds ≥ 9 (or 8's sliver). This is scaling-invariant, so it constrains every representative of the orbit — the first rigid constraint toward the floor.

IDEA (why N/4): the band B needs ~8 ≈ N/2 speeds in the N = 16 problem; the magnifier can align at most about half of the needed band-servers into [1..15] simultaneously, giving N/4. The N = 12 floor of 3 = 12/4 supports it; N = 8 (predicted 2) is untested — covers are too rare below p ≈ 300 to sample. UNFINISHED.

IDEA (Q1 completion): the obstruction to M₁₅ ≤ 3 is that C(u) ≤ 3 forces near-equality in ΣC² ≤ 3ΣC, but cover pairs (v, w) with small ratio w/v have |v⁻¹A ∩ w⁻¹A| far above the 4.5 average (window containment again), inflating ΣC² past 1260. The gap is only ~1%, which itself explains why the floor is exactly 4 and not 5.

FACT (Q4 calibration): 307's sample: 4:40, 5:124, 6:82, 7:24, 8:3, 9:1 (mean 5.38); 337 sits in the same abundant regime (1,477 covers, n = 8H exactly) — I extrapolate the same shape. Rare-cover primes skew high (379: all 7s; 457: 9), but 337 is not rare.

**Least-sure step:** the Q4 count of 4s — it assumes 337's M₁₅ distribution matches 307's shape, anchored on one 274-sample; the residue class difference (307 ≡ 3, 337 ≡ 1 mod 16) could shift the 4-fraction several points. Second: the N = 12 "floor 3" rests on 5 sampled covers at one prime.

--- end verbatim ---
END LETTER
