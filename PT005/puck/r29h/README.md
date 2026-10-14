# PT005 R29h Part A — Puck's four seats

Packet: PT005/hesper/r29h/send_R29h_A.txt @ b74cb84
All four prompts sent first (2026-10-14 ~18:44 +0800), then replies collected.
Web/search OFF everywhere; DeepThink ON for DeepSeek; no Stop/Regenerate pressed.

| Seat   | Status | Sent | Received | File |
|--------|--------|------|----------|------|
| Astra  | PROVED (computer-assisted proof) | 18:44 | 18:52 | 2026-10-14T1844-r29h-reply-Astra.md |
| GPT    | PROVED (finite computational proof) | 18:44 | 18:57 | 2026-10-14T1844-r29h-reply-GPT.md |
| DeepSeek | PARTIAL | 18:44 | 18:49 | 2026-10-14T1844-r29h-reply-DeepSeek.md |
| Grok   | PARTIAL | 18:44 | 18:49 | 2026-10-14T1844-r29h-reply-Grok.md |

ANSWER BLOCK statuses:
- Astra: PROVED — Task (1) via computer-assisted proof; stronger structural reduction; independent Python generator checks all conditions, "No mod-16 collisions: PASS".
- GPT: PROVED (finite computational proof) — mod-16 distinctness under canonical representatives 1<=w<272, via exact-partition enumeration with complement-footprint obstruction; all 8 rows PASS, 0 complementary conflicts. Least-sure step: still relies on finite-search certificate, not yet a pure symbolic identity.
- DeepSeek: PARTIAL — adjacent and distance-2 vertices have distinct w mod 16; exact gap is ruling out equality at distance 4 (opposite vertices on the 8-cycle).
- Grok: PARTIAL — proved distance-2 distinctness from edge-ratio argument; exact gap is excluding distance-4 equality (would need product of four edge ratios = 1 mod 16, which is algebraically possible, so more tiling data needed).

No blockers. All four full replies saved with headers.
