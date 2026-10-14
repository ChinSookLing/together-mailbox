SEAT: DeepSeek
CARRIED_BY: Puck
MODEL: DeepSeek (DeepThink ON, Search OFF)
CHAT: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202
SENT: 2026-10-14 18:44:35 +0800
RECEIVED: 2026-10-14 18:47:40 +0800
PACKET: PT005/hesper/r29h/send_R29h_A.txt @ b74cb84
SEND_TEXT: PT005/hesper/r29h/send_R29h_A.txt
---
ANSWER BLOCK

STATUS: PARTIAL. I proved adjacent and distance-2 vertices have distinct w mod 16, but I did not rule out equality at distance 4 (opposite vertices on the 8-cycle). That is the exact gap.

Main claim reached. In the 150 length-8 cases, every edge ratio w_j/w_i mod 32 lies in {±3, ±11}. Modulo 16 this set is {3, 13, 11, 5}, and no element is 1 (mod 16). Hence adjacent vertices are distinct mod 16. Also, if two vertices share a common neighbor u, their ratios to u are two distinct elements of that set, so they cannot be congruent mod 16. Thus distance-2 vertices are distinct mod 16.

Gap. To get pairwise distinct, one must exclude w_i = w_{i+4} (mod 16). Along either length-4 path, this would require a product of four edge ratios to be 1 (mod 16). That product is algebraically possible, e.g. 3*3*11*11 = 1 (mod 16), so more tiling data is needed.

Least-sure step. Excluding the distance-4 repeat.

Reasoning

Let S = {±3, ±11} (mod 32). Modulo 16, S = {3, 13, 11, 5}. None is 1. So adjacent w's differ mod 16.

At a vertex u, its two neighbours v, w have ratios v/u and w/u in S. If v = w (mod 16), then v/u = w/u (mod 16). Since the four elements of S are distinct mod 16, this forces v/u = w/u (mod 32), hence v = w, impossible. So distance-2 vertices differ mod 16.

The cycle alternates between class {1, 7} and {3, 5}. Each side has four vertices and four possible mod-16 residues. Distance-2 distinctness makes consecutive vertices in each side distinct, but two opposite vertices on a side could still coincide. That case is not excluded by the local ratio argument.

CHECKED: First data row w = [9, 59, 111, 77, 263, 213, 161, 195] has mod 16 [9, 11, 15, 13, 7, 5, 1, 3], all distinct. The same hand check works for the other seven rows, but a structural proof of the distance-4 exclusion is UNFINISHED.
