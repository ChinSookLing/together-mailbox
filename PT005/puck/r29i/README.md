# PT005 R29i Part A — Puck's four seats

Packet: PT005/hesper/r29i/send_R29i_A.txt @ 03b451a
All four prompts sent first (2026-10-14 19:07-19:08 +0800), then replies collected.
Web/search OFF everywhere; DeepThink ON for DeepSeek; no Stop/Regenerate/resend.
Replies copied verbatim from the chat UI (final answer only, no thinking trace).

| Seat | Route | Status | Sent | Received | File |
|---|---|---|---|---|---|
| DeepSeek | (a) | PARTIAL | 19:07 | 19:08 | 2026-10-14T1907-r29i-reply-DeepSeek.md |
| Grok | (a) | PARTIAL | 19:08 | 19:10 | 2026-10-14T1907-r29i-reply-Grok.md |
| GPT | (b) | PARTIAL | 19:07 | 19:16 | 2026-10-14T1907-r29i-reply-GPT.md |
| Astra | (b) | PARTIAL | 19:07 | 19:21 | 2026-10-14T1907-r29i-reply-Astra.md |

Puck's notes (own checks on the 8 supplied cycles, Puck's box):
- Grok's step "class-preserving 4-products {1,9,25} mod 32 reduce to {1,9,8} mod 17" mixes moduli: a ratio's residue mod 32 says nothing about its residue mod 17 (CRT, 544 = 17*32). I object to that step; Grok's route is not a proof. Its premise is true on data: w_{i+4}/w_i = -1 mod 17 in all 8 cycles (8/8 rows, all 8 positions).
- DeepSeek's reduction (distance-4 equality forces perfectly alternating P/N edge signs) is consistent with data: edge ratios mod 32 are only {3,29,11,21} = {+-3,+-11}; sign patterns are period-4 with exactly one odd-one-out per half (e.g. b=1 PNPPPNPP, b=3 PNNNPNNN), never alternating.
- Astra's c=+-9 hand lemma (no Hamiltonian hypothesis) looks sound to me on read-through, reading "A_w = w−1" as w^{-1} mod 32 (superscript likely lost in copy; with A odd, (w+16)^{-1} = w^{-1}+16 and 16-X = X give L_v = L_w). It covers only rows whose |bw|_17 = 8 class (b=1,2,3 here); b=4..8 not covered.
- Verdict suggestion: no seat closes the hand step this round. Per the one-round timebox, record (1) as CHECKED computer-assisted and move to p=19; keep Astra's c=+-9 lemma and DeepSeek's alternation reduction as partial hand results.
