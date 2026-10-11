BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 08:27 +08
RE: 猜公式 Round 6 (packet 6f1e734, v2 5aef677) — all 10 seats committed
STATUS: OPEN until chair reads

Committed replies (PT005/hesper/, files *-guess-r6-reply-{seat}.md; date prefix in filename is 2026-10-10 by the helper even for 10-11 sends, see AS_OF inside):
- astra 2055ebd (R6 + v2 reply in one file)
- grok 3975808, grok-v2 084ef69
- qwen a26b961, qwen-v2 4f25025
- gemini 5b43195 (R6 + v2; chat 1e9f12d501ad505f, not the Big Picture chat)
- kimi eddfbdb has a stray capture line at top → superseded by kimi-fixed 20a51cd; kimi-v2 795d117
- deepseek 5ea8a39, lumo f52ff62, glm 02c6a63, gpt 55a7c5f (these four sent 10-11 with the v2 correction already folded in)
- GPT: GPT-6 failed twice ("This response couldn't load", 10-10 11:40 and 10-11 08:15); answered on GPT-5.6 Sol High.

Five lines:
1. v2 accepted by all who saw it: min core over the 19 reps = 4 (389 rep 2); no seat found a core ≤3; ≤3 is UNFINISHED everywhere.
2. Q4 claims: Kimi "≥4 small after some scaling" 33/33 (positive side by its own covers, zero side inherits census — circular); Grok same ≥4 rule 33/33 (same circularity); GPT/Astra |U_K7(p)| ≤ 63 → 30/33, wrong at 383, 397, 457; Qwen odd core 28/33; DeepSeek per-residue mod-16 cutoff 33/33 (pure fit); Gemini QR rule 24/33; Lumo/GLM no scored rule.
3. Q1 consensus: composite speeds' windows at non-coprime positions sit inside divisors' wider windows (Kimi PROOF, window containment); 12's only new windows are p/12, 5p/12 at width H/6.
4. Errors to flag: GLM writes "Min core = 3 [FACT: 389={1,4,11}]" — that is the u=1 view; the max over scalings is 4 (u=4: {4,5,7,13}). Lumo lists 433, 449 (census 0) as working.
5. Most promising thread: GPT's "multi-scale core" (389: u=1 {1,4,11}, u=2 {2,8,9}, u=4 {4,5,7,13}) and Kimi's "≥4 floor even for covers with all speeds ≥16". Ask: chair synthesis + next round.
END LETTER
