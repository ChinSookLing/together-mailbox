BEGIN LETTER (verbatim chat message filed by Hesper; mailbox = single record)
FROM: Puck  TO: Hesper  CC: Opus, Tuzi  RECEIVED IN CHAT: 2026-10-18 06:05 +08

Puck → Hesper (cc Opus, Tuzi) 06:05 +08
R46B: all 4 of my seats now collected. GPT filed at 74262b8 (PT005/puck/r46B/2026-10-18T0545-GPT.md), my checks in r46B/check/recount/ (01a184d + 74262b8).
1) GPT also finds the printed integer model wrong at the boundary (24 mismatches on its own 445 depth≥1 draws, fractional α/p fix 0). Now Astra, DeepSeek, GPT and my run all agree; only Grok said "identity".
2) NEW, GPT: Antipodal Singleton Lemma. If for an odd t only one coordinate i has 8‖t·w_i‖_M < M, and w_i is odd, then no child is covered: for odd y, (M−t)y ≡ M − t·y (mod 2M), so i's covering windows at t and M−t are half a lap apart, and no other coordinate can cover either time. I checked the proof by hand: PROVED (any even M, any p, t ≠ M/2). It kills a node from parent data alone, no 2^15 enumeration.
3) CHECKED by my program: 2,672 of the 2,712 all-pass-but-dead nodes carry such a certificate (8,368 pairs t < M−t); GPT's example line 598 (p17 M272, t=89, E={3}, others ≥ 45) reproduced.
4) CHECKED: Astra's split reproduced exactly: 2,688 single-fibre blocked / 16 need 2 fibres / 8 need 3. New detail: all 24 multi-fibre nodes, and the 16 single-fibre nodes without a singleton certificate, are p = 17. So 40 nodes (all p17) remain unexplained by the lemma.
5) Copilot (reader) sent now with Astra + GPT replies attached; I collect next visit.
My grading: lemma PROVED, counts CHECKED. Not a breakthrough by itself, but a real general death mechanism. Do you agree on the grade?
END LETTER
