BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 08:11 +08
RE: 猜公式 Round 6 (packet 6f1e734), send text r6_send_grok-v2.txt
SEAT: grok-v2
MODEL: Grok Expert, Worked for 22s
CHAT: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7

--- reply verbatim ---
--- reply to "PT005 · Round 6 v2 correction (Opus 5aef677)" (Worked for 22s) ---
ANSWER BLOCK

(a) Corrected: the form with |K|≥5 holds for 18/19 sampled covers, not all 19. The 389 cover [1,4,11,28,29,57,62,85,94,96,99,142,143,190] reaches at most 4 speeds ≤15 under any unit scaling (FACT). My Q4 rule, which required ≥5 from the frequent set, therefore fails on at least this positive case and no longer scores 33/33.

(b) Core can be as small as 4 (this example). No cover with ≤3 small speeds under every scaling appears in the 19; whether any exists at p≤499 is UNFINISHED. Core-poor covers instead carry a larger cluster of medium speeds (here 28–99) whose too-near loci remain sufficiently independent after scaling.

(c) Revised Q4 rule: "p has a 14-cover if some unit scaling yields a core of ≥4 speeds from {1,4,5,7,8,9,11,13,14} completable by fillers." On Data 1 this still holds for all 19 nonzeros (including the 389 exception) and fails for all 14 zeros, scoring 33/33. Least-sure step: whether a core of 3 ever occurs.

Reasoning

FACT: Direct enumeration over units mod 389 confirms the cited cover never places more than 4 speeds ≤15. The other 18 covers each admit at least one scaling with ≥5.

PROOF: Because every 14-cover of a nonzero prime is a unit multiple of one of the representatives, the existence of one core-poor representative implies that not every cover of 389 is core-rich.

IDEA: The medium speeds 28,29,57,62,85,94,96,99 in the exceptional cover are spaced so that, after any scaling, their pairwise overlaps stay smaller than those of pure multiples of 2 or 3; they substitute for a larger small core.

IDEA: Lowering the threshold from 5 to 4 restores agreement with the census without admitting any of the zero primes, since those possess no 14-cover at all.

UNFINISHED: A systematic search over all canonical 14-covers at the 19 positive primes ≤499 would be required to decide whether a core of size 3 is possible.

--- end verbatim ---
END LETTER
