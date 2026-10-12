BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 17:42 +08
RE: Round 18 (packet ab3ea04) — collection status, 8/9 full + Kimi partial
STATUS: OPEN (chair has not read)

1. Received (verbatim, PT005/hesper/2026-10-12T*-guess-r18-reply-*.md): Grok 5a41a3f, Gemini 1dbc505, DeepSeek 960a8d2, Lumo d70b209, Qwen df753f4, GPT d38a2be, Astra 2b42acd, GLM 1ccb8ee. Kimi: PARTIAL 3e7cc49 (still running code on p=101/103, no final text at 17:41).
2. Capture caveats: DeepSeek — browser Google sign-in failed; Tuzi sent the file herself and pasted the reply (mode/URL not recorded). Qwen — upload blocked, packet pasted inline. GPT/Astra/Gemini/Lumo/Kimi — Copy empty, page-section capture with [seam]. GPT reply header calls itself "Astra" (project instructions leak). GLM answered after ~40 min Deep Think Max (not empty this round).
3. Courier flags for audit (not verdicts): (a) Grok's Q5 "p=101 counterexample" (true 15-cover, residual LP 3.7<4) and GPT's Q5 (LP needs 4, integral 4 fails) both look like LP-weakness examples, not LP-cut unsoundness, since LP ≤ integer optimum always — please check what each actually refutes. (b) DeepSeek's disjoint-candidate packing cut has a short integral proof; no node counts (UNFINISHED). (c) Qwen says 401/409/419/421/457 are γ=14 and lists γ=15 set 431–499; census14 recorded covers=0 for 383,397,431…499 and 1 cover at 457 — 401–421 status should be checked against our records. (d) Threshold reruns differ: Astra p=971 (ledger only) / 953 (with 307/337/383); GPT 71 gates to p=883 (Σ=485.55); Qwen ~860–880 MODEL. (e) Lumo's p^5.9 cost law is quoted, not computed.
4. Lanes: Q1 sound pruning proposals with PROOF from GPT (weighted dual certificate), Astra (pair-union cut), DeepSeek (packing cut); Q4 inequalities from Astra and GLM (overlap lemma, m ≥ 1/72 on chair set).
5. Next: Kimi full reply if it finishes; await nightly RELEASE. Nothing posted to wall.
END LETTER
