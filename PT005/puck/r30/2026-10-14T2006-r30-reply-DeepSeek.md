SEAT: DeepSeek
CARRIED_BY: Puck
MODEL: DeepSeek (DeepThink ON, Search OFF shown in UI)
CHAT: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202
SENT: 2026-10-14 ~20:06 +0800 (approx — sent by earlier partial step; exact seconds not visible)
RECEIVED: 2026-10-14 20:15:56 +0800 (UI: "Thought for 14 seconds", reply complete)
PACKET: PT005/hesper/p19/send_R30_p19.txt @ c02bfff
SEND_TEXT: PT005/hesper/p19/send_R30_p19.txt
STATUS: PARTIAL
---
ANSWER BLOCK

STATUS: PARTIAL. The Q+D formula is p-independent, but the needed input—that the length-8 mixed case forces all eight w mod 16 to be distinct—is not proved for general p.

Main claim. For any prime p >= 17, if a mixed length-8 Hamiltonian XOR cycle has pairwise distinct w mod 16, then H = Q + D = 0 + 1 = 1 (mod 2), so the cycle is odd and doubling fails. D depends only on the mod-8 class alternation {1,7} <-> {3,5}, hence not on p. Q depends only on w mod 16. So the formula transfers.

Where p enters. Only in the tiling constraints: the member set uses t = +-b (mod p), and the signed representative of b depends on p. The Q+D decomposition itself does not.

Check on p=19 data. Every listed length-8 mixed row has eight distinct w mod 16. Example b=1: [11,1,13,7,9,3,5,15]. So Q=0. Since the graph is one alternating 8-cycle, D=1. Hence H=1 for all eight rows. This matches "0 doublable."

Exact gap. A hand proof that every prime p >= 17 forces distinct w mod 16 in the length-8 mixed case. Without it, the transfer is conditional.

Part (2). UNFINISHED. The condition deciding single-class doubling at p=17 (b=6 only) but never at p=19 cannot be derived from only these two facts.

Least-sure step. The general-p distinctness lemma.
