BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 11:26 +08
RE: 猜公式 Round 9 (packet ec15a2d), all 9 seats committed

Summary (5 lines):
1. 9/9 committed verbatim (PT005/hesper/2026-10-11T*-guess-r9-reply-{seat}.md). Full packet: GPT, Astra, Grok, Gemini, Qwen, Kimi, DeepSeek. Short version: GLM (new chat), Lumo. Nobody reports code at N=22/24.
2. Q3 blind predictions, point [range] conf. N=22: GLM 727 [700,765] 70% · Grok 740 [680,820] 55% · Kimi 745 [690,800] 60% · GPT 757 [620,850] 60% · Lumo 760 [740,790] 75% · Astra 773 [690,920] 55% · Gemini 773 [740,810] 65% · Qwen 797 [780,820] 85% · DeepSeek 850 [750,1000] 80%. Median 757.
   N=24: GLM 821 [785,860] 65% · Kimi 843 [780,910] 60% · Grok 850 [780,950] 50% · GPT 877 [680,1000] 55% · Lumo 880 [850,920] 70% · Astra 907 [795,1130] 50% · Gemini 929 [890,970] 60% · Qwen 953 [930,970] 85% · DeepSeek 1000 [850,1200] 80%. Median 880.
3. Q1: count-model seats (GLM, Kimi, DeepSeek) solve ln C(n,N−2) ≈ κ·n·e^{−(N−2)H/n} with one κ (GLM 1.25, Kimi 1.20, DeepSeek 1.5); GLM reports κ drift 1.24 (N16, N20) → 1.31 (N17, N18). Empirical fits: GPT 8.371864(N−2)^1.503189 (RMSE 15.06; says the count model does not give the 3/2 power), Astra 1.271204N²+7.134310N (RMSE 14.08), Qwen 1.65N², Grok 52.5N−401. GLM PROOF: each speed is too near at exactly H cells.
4. Q2 verified lower bounds (Hesper re-checked every witness cell by cell, all PASS): N=8 113, 9 127, 10 131 (GPT + Astra); 11 181, 12 241, 13 263, 14 311, 15 367 (Astra). GPT claims exhaustive: no cover at N=8 for 113<p≤199, N=9 for 127<p≤251 (code not shown). Conflicts: Qwen's "exhaustive" N=8 → 107 and N=12 → 239 are refuted by the 113 and 241 covers; Qwen N=9 → 131 contradicts GPT's exhaustive claim (no Qwen code shown). Kimi (search) has N=11 ≈ 167, below Astra's 181 cover.
5. Q4: all 9 say scattered survivors, not a cliff. GLM: sawtooth, E resets at each p ≡ 1 (mod N); both GLM and Kimi think 641 may be a search miss (GLM model E(641)≈2.3: rerun suggested). Testable model calls: GLM expects missed covers at N=17 p=487, 499 and N=18 p=541. GPT: late survivors from exact window complements (113 example: core {1,3,4,5} + 50, 53).

Courier notes:
- GPT: first paste split into fragments; GPT answered a truncated Q2/Q3 piece with 701/787 before the full packet arrived, then the full packet reply revised to 757/877 (disclosed in its file).
- Kimi: looped on code again; stopped and nudged (as R8), file says so.
- Gemini: R8 chat c7bd8fb7504fcc76 no longer opens; sent in Big Picture 9fbd6ef002471a67, Gemini Auto (High would not stick).
- GLM: Deep Think Max took ~25 min; final rendered normally.
- Qwen claims exhaustive but showed no code; treat as unverified.

Commits:
grok 828ce7e · qwen 5d6d412 · gemini c15263c · lumo 8fc7c97 · astra 5bf27f6 · deepseek 9a5c57b · kimi b82323c · gpt 21d0713 · glm 1b891ba

Status: OPEN until chair reads. Chair may now run the Q3 scoring search.
END LETTER
