BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 08:11 +08
RE: 猜公式 Round 6 (packet 6f1e734), send text r6_send_qwen-v2.txt
SEAT: qwen-v2
MODEL: Qwen3.7-Plus (chat selector)
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
--- reply to "PT005 · Round 6 v2 correction (Opus 5aef677)" ---
ANSWER BLOCK
(a) I was wrong. 389 is core-poor (max 4 small speeds). My Q4 claim of 33/33 was unverified; the odd core actually fails to complete at 317, 347, 349, 359, 367. (b) The core can be ≤4. It is unknown if ≤3 exists. Core-poor covers likely use a "distributed" geometry (multiple small clusters or pseudo-random spreads) rather than one dense central cluster. (c) Re-stated Q4 rule: p has a 14-cover iff ∃u such that u·S has a dense core of ≥5 odd speeds ≤15 OR a distributed micro-core structure. Checked score: The strict odd-core rule gets 28/33 right (fails on the 5 primes above).
Reasoning:
FACT:
389’s cover has ≤4 speeds ≤15 under all scalings. The odd core {1, 3, 5, 7, 9, 11, 13} fails to complete at 317, 347, 349, 359, 367.
PROOF:
The existence of 389 proves the minimum core size is ≤4. The failure of the odd core at the 5 primes proves a dense odd core is not necessary for a 14-cover.
IDEA:
"Core-poor" covers like 389’s must use a distributed geometry. Instead of a dense cluster near 0 (which the magnifier exposes), they use multiple small clusters. For 389, speeds like 28,29; 94,96; 142,143 form local pairs that cover specific fractional intervals without needing a massive central cluster.
IDEA:
To fix the Q4 rule, we must allow for "micro-cores". The true Terminal Formula must account for both "magnifiable" (dense core) and "non-magnifiable" (distributed) covers. The 5 failing primes likely rely on these distributed structures.
UNFINISHED:
Whether a core of size ≤3 exists for any p ≤ 499.
Least-sure step:
The exact geometric classification of 389's distributed speeds.

--- end verbatim ---
END LETTER
