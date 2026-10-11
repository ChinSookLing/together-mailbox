BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 10:17 +08
RE: 猜公式 Round 8 (packet 1351cbb), all 9 seats committed

Summary (5 lines):
1. 9/9 replies committed verbatim (files PT005/hesper/2026-10-11T*-guess-r8-reply-{seat}.md). Full packet to GPT/Astra/Grok/Gemini/Qwen/Kimi/DeepSeek; short version to GLM/Lumo.
2. Q3: 7 seats predict 0 at all 14 exam primes (conf 65–90%). Dissent: Kimi 521, 569 = 1–5 (65%); Lumo 521, 569, 577, 593 = 1–5 (80%).
3. Q1: best in-sample fits 30/33 (GPT, all 33 points, misses 409/433/457; GLM, misses 409/421/457, with a claimed PROOF that no log-linear threshold rule can exceed 30/33). Others 25–31/33 (Lumo's 31 unverified).
4. Q4 (largest p with an (N−2)-cover, N=17/18/20): Kimi computed (stochastic hill-climb, lower bounds) 479 / 509 / >601 (N=20 survivors 521, 541, 563, 569, 601; 521/541/601 ≡ 1 mod 20). Astra verified subgroup covers N=18 at p=449, N=20 at 37, N=17 at 31, 61. Model predictions: GPT 463/523/601, Astra 479/541/661, GLM ~490/540/640, DeepSeek 509/577/709, Qwen ~550/750/1200, Gemini ~510/560/670, Lumo ~600/700/900, Grok 350–400/280–320/200–240 (decreasing; contradicts Astra's N=18 p=449 cover).
5. Notes: Kimi's first reply looped on Q4 and was stopped; committed reply answers a courier nudge (stated in file). Gemini forked to new chat c7bd8fb7504fcc76 (Auto+High; 3.1 Pro not offered). DeepSeek committed final answer only (thinking trace omitted). Nobody reported code at 503–599 for N=16.

Commits:
- grok 401f57c · gemini 9b113e0 · qwen b1f78f7 · astra 797ea97 · gpt 84326d6 · deepseek d6ea4f8 · lumo 1ebe980 · glm 245b80b · kimi 3d127fa

Office: p307 running (8 workers); 37/279 IR jobs at 09:37; memory 09:54 = 689Mi used / 7.4Gi, swap 0, load ~8 on 12 cores → no change to 6 threads.

Status: OPEN until chair reads.
END LETTER
