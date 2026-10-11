BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 17:04 +08
RE: 猜公式 Round 14 (packet 1473ae0), send text r14_send_full.txt or r14_send_short.txt
SEAT: glm
MODEL: GLM-5.3 Deep Think Max
CHAT: https://chat.z.ai/c/755b3610-a5f8-4365-89a8-237c83a456fe

--- reply verbatim ---
Source: https://chat.z.ai/c/755b3610-a5f8-4365-89a8-237c83a456fe
Model: GLM-5.3 (Deep Think Max)
Chat title after completion: 猜公式 Round 14 解析与结论
Prompt: PT005 · 猜公式 Round 14 · short version (Opus packet 1473ae0), sent at 16:49 +08.
Completion observed: ~17:12 +08 (page went from Thinking.../Stop to Thought Process/Copy+Regenerate/Send).
Capture: full text of the final rendered reply (not the internal thinking pane).

---BEGIN FINAL ANSWER (verbatim)---
Conclusions. Q1 OPEN — PV, Burgess, Weil each lose ≥ p^(1/2−ε) against the O(1)-precision needed; subgroup sets aren't extremal anyway. Q2 AGREE — both chair claims verified. Q3: L0 PROVED → L1 OPEN (hardest, inverse) → L2 OPEN (⊃ Q1) → γ ≤ 15 in-game; δ₀ ≈ 0.08. Q4: constants only.

Q1. FACT: data primes ≡ 1 (mod 28): 112=4·28, 196=7·28, 280=10·28, 420=15·28, 448=16·28. Need a coset of μ₂₈ (−1 ∈ μ₂₈ ⇒ symmetric) avoiding [1,H]; H=63=⌊1009/16⌋ (1009/16=63.06). Per-coset mean λ=28·63/1008=1.75; P(empty)≈e^(−1.75)=0.174 (Poisson: IDEA).
• PV: |S_χ(p/16)| ≤ √p·ln p = 31.8·6.9 ≈ 220; over 36=1008/28 characters it only yields: every coset meets [1, O(√p ln p)] ≪ [1, p/16] — pro-cover. FAILS.
• Burgess: at L=p/16, r=2: (p/16)^(1/2)·p^(3/16) ≈ p^(11/16); yields cosets meet [1, O(p^(1/4+ε))] — again pro-cover. FAILS.
• Weil: complete sums only; completing [1,H] costs ~p modes × √p each. FAILS.
Needed: CLT-strength control of coset counts — beyond the art (Konyagin–Shparlinski need subgroup order ≥ p^(1/3); here 28). UNFINISHED.
IDEA: U(G_p)|₁₀₀₉ ≈ 14·0.174·36 = 87.7 ≫ D ≤ 6 — subgroup sets not extremal; Q1 is defensive, not the road to δ.

Q2. AGREE.
(i) FACT: one speed moves U by ≤ H=63. McDiarmid: Σc²=14·63²=55566; exponent 2(E/2)²/Σc² = 2·37.85²/55566 = 2865/55566 = 0.052 → bound e^(−0.052)=0.95 — constant. Chair right. (E=75.7 given; PROOF-check: M(1009)=504.5·(882/1009)^14=76.7=E+1 ✓, 882=1009−127, 127=2·63+1.)
(ii) FACT: μ=75.7; mean overlap 504·63²/504² = 3969/504 = 7.9 classes ⇒ all pairs dependent; typical pair (1−2·63/504+7.9/504)^14=(49/64)^14=0.0238 (14·ln(49/64)=−3.739); Δ ≈ 254016·0.0238 ≈ 6045 ≈ 80μ — "unsafe sets overlap" ✓. Refined Janson: P(cover) ≤ e^(−75.7²/(75.7+6045)) = e^(−0.936) = 0.39; first-moment needs exponent ≥ ln C(504,14) = 14·ln497.5 − ln14! = 86.9−25.2 = 61.7 — have 0.94.
IDEA: dilate rigidity makes correlations genuine — Janson unfixable; and even perfect concentration bounds typical S, while δ>0 is worst-case. Needs an inverse theorem, not probability.

Q3. L0 [PROVED, R10–13]: exact E, M, D. L1 [OPEN — hardest]: U(S)<δE ⟹ S near a coset of μ_m (m=O(1)); no literature (sum-product gives no uniform U bound). L2 [OPEN]: structured candidates all have U ≥ δE; ⊃ Q1. L3 [in-game KNOWN; UNFINISHED here]: γ ≤ 15. L1∧L2 ⟹ δ ≥ δ₀ — data: 6/75.7=0.079; 0.009/0.076=0.118 (76.7/1009=0.076) FACT — with L3: γ(p)=15 ∀ p>P₀. Hardest: L1.

Q4. Only constants move (FACT): λ=2(N−2)/N: 28/16=1.75 → 2, e^(−2)=0.135; E≈(p/2)(1−2/N)^(N−2): (7/8)^14=0.154 (14·ln(7/8)=−1.869) ⇒ 0.0771p → e^(−2)·p/2=0.0677p; subgroup order 2N−4 ⇒ congruence p ≡ 1 (mod 2N−4). IDEA: λ=O(1) ∀ N≥4 — same regime, same failure points of PV/Burgess/Weil. D≈0.009p−2.6 is N=16-only.
---END FINAL ANSWER (verbatim)---
--- end verbatim ---
END LETTER
