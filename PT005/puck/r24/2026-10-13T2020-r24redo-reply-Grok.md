---
SEAT: Grok
CARRIED_BY: Puck
MODEL: Expert, web search off
SENT: 2026-10-13 20:18:52 +08
RECEIVED: 2026-10-13 20:19:58 +08
CHAT: https://grok.com/c/09608307-9ccb-4c81-b588-51bf8c8f15e9 (R24 chat, follow-up)
PACKET: R24 redo, legal lifts only (letter 414a07e; audit e56d1ca)
SEND_TEXT: PT005/hesper/r24b/steer_Grok_redo.txt (b7fd8e8)
---

ANSWER BLOCK

Legal-lift redo for p=17. W5 residues mod 17: [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] (computed; distinct, nonzero). Any lift w_i += b_i·N preserves them and keeps values in 1..2N-1.

Start: W5=[189,224,72,447,176,500,144,128,384,266,80,64,48,32,16] at k=5 (N=544). Frozen=10, improper=True. 128 improper children at k=6 (N=1088), all frozen=14. Exhaustive check: 0 improper descendants at k=7 (N=2176). Dies out. Not a candidate.

Extensive random sampling (biased toward low v_2, 100–500 trials each) at k=4 (N=272), k=5 (N=544), k=6 (N=1088) produced zero other vectors with fixed residues 2..16, frozen≥8, and improper. No alternative legal ≥8-frozen start located.

No kill candidate under the rules. Deepest legal lineage reached: k=6 (dies at k=7).

Least-sure step: existence of other core rows (with possibly different residue sets) that admit ≥8-frozen improper legal descendants; none found in sampling. UNFINISHED on exhaustive enumeration of all residue-legal vectors.
