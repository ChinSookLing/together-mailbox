BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 16:07 +08
Subject: PT005-BRAINSTORM-GENERATION reply from DeepSeek, verbatim
Seat: DeepSeek, new chat https://chat.deepseek.com/a/chat/s/424fd439-23f0-4048-861b-dbc4dfc09c69 (title PT005 7-filter idea), DeepThink ON, Search OFF, thought 60 s. Delivery note: the long text could not be typed into DeepSeek's box, so the identical packet was attached as sent_message.txt (6.75 KB, same sha256) with one short instruction line.
Sent: the packet BEGIN..END from PT005/opus/2026-10-06T2203-packet-brainstorm-large-prime-generation.md plus scouting/LR16/opus/p401_level2/README.md verbatim (message sha256 734b4d10...7505).
Courier only: no judgment of the maths. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
SEAT · DeepSeek · REPLY_TO: this packet · read records: attached PT005 packet and attached p401_level2 README only; no web, no other chats.

SUMMARY (≤5 lines)
FACT: At p = 401 all five level-2 survivors contain speed class 7 after unit-scaling to include 1; 7 is the only common class besides 1.
IDEA: Conjecture for p ≥ 191: every level-one row alive at level 2 must contain 7.
If true, step 1 can fix 7 ∈ A, shrinking the search by roughly N/15 ≈ p/30.
ESTIMATE: p = 191 step 1 is 13 min on the author's engine, so a level-2 check is under an hour on a laptop.
WHAT KILLS IT: one level-2 survivor at p = 191 that, after scaling to include 1, does not contain 7.

THE IDEA
Use a "mod-7 filter" before generation. Canonicalize every level-one row by unit multiplication so it contains 1. Then add the hard constraint 7 ∈ A before enumerating step-1 rows. Only rows passing this filter go to the existing level-2/4/8/16 cascade. The tight row {1,2,…,15} passes; the four non-tight p = 401 level-2 survivors also pass. Rows without 7 are assumed dead at level 2.

WHY IT MIGHT WORK
FACT from the attached README: the five p = 401 level-2 survivors are exactly the tight row plus four others, and all five contain 7. Since canonicalization forces 1, 7 is the only nontrivial common speed class among them. The covering condition A + S = Z_N with S = dlog(1..⌊p/16⌋) may force a translate in the 7-direction to block the parity zoom. If this is not a p = 401 accident, it is a cheap structural filter that can be checked independently.

CHEAP TEST
Run the existing step-1 engine at p = 191 (FACT: 13 min step 1 on the author's engine), cascade to level 2, and for each level-2 survivor scale the row to include 1 and test whether 7 is in the row. Count survivors missing 7. This is under one hour on a laptop and needs no paid compute. If p = 191 is clean, optionally repeat at p = 223 if time allows.

WHAT KILLS IT
A single level-2 survivor at p = 191 — or any prime with known level-2 survivors — that after scaling to include 1 does not contain 7. That falsifies the conjecture and the 7-filter. If it passes at p = 191 but fails at p = 223 or 239, then the lemma would need a larger P0.
----- END REPLY -----
END LETTER
