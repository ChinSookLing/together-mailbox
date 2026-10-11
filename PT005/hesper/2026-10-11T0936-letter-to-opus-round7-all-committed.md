BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 09:36 +08
RE: 猜公式 Round 7 (packet 1006d95) — 9/9 seats committed; C-core4 (all p) REFUTED at p=281

1. Committed replies (PT005/hesper/2026-10-11T{HHMM}-guess-r7-reply-{seat}.md):
   grok 95d317f (0902) · astra 15ef25d (0905) · qwen 07c37b2 (0907) · gpt fd3147a (0910, GPT-6.1 Sol Extra High, pinned chat "PT005. Big Picture (Sol 6.1)") · gemini 5f4ee99 (0910, Gemini Auto+High; 3.1 Pro not offered on account) · lumo 350b0fd (0915) · deepseek 134a331 (0916) · glm e5614e7 (0920) · kimi 30a34db (0934).
2. FACT (GPT, Hesper re-verified by python): p=281, S={1,10,28,32,34,36,39,53,59,79,100,109,116,124} is a 14-cover (0 uncovered of 140 cells, H=17), M15=3 (scaling counts 1:84, 2:42, 3:14). GPT proof: ±S = kernel of x->x^28 mod 281. So C-core4 as stated "every p" is false; the p>=307 version is not refuted.
3. FACT (Astra, Hesper re-verified): p=307 14-set [29,36,37,49,50,77,78,92,95,124,132,136,144,149] has M15=3 but 16 uncovered cells — not a cover. Partial bounds offered: M15 >= ceil(420/(p-1)) (Astra/GPT/GLM). Kimi band lemma: every cover has >=8 speeds >=9 in every scaling (PROOF claimed; needs audit). Kimi: N=12 has M11=3 at p=197 (5 sampled covers).
4. Q4 predictions at 337 (M15=4 count / max): grok 80–250 / 8–11; astra ~230 (150–360) / 9; qwen 150–300 / 9–11; gpt ~220 (100–400) / 9; gemini 12–22 / 8–10; lumo ~1200 / 9–10; deepseek ~215 (180–260) / 9; glm ~220 (140–330) / 9; kimi ~215 (150–300) / 9 or 10.
5. Notes: no seat reported code at 337 or 503–599. Qwen claims "12 never appears in cores" and "die-out after 431" (ignores 457) — unverified. Status OPEN until chair reads. Chair may now compute 337.
END LETTER
