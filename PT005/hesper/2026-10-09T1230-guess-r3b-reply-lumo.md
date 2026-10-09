BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 12:31 +08
RE: 猜公式 Round 3 ADD-ON (chair note 46, 34bd541; C16), one narrow task, send text r3b_send_lumo.txt
SEAT: lumo
MODEL: Lumo 2.0 Max thinking, web off
CHAT: https://lumo.proton.me/u/9/c/bc367cfb-4f96-4bab-ada6-bb83440a681c

--- reply verbatim ---
[courier note: captured from rendered page; line breaks around formulas are page rendering]

ANSWER BLOCK
CONFIRMED.
The longest safe piece in [0, ½] is
[49/256, 31/160]
, with length exactly
3/1280
.
Left endpoint 49/256
= 3/16 + 1/256: made by
speed 16
, k = 3 (zone (47/256, 49/256)).
Right endpoint 31/160
= 1/5 − 1/160: made by
speed 10
, k = 2 (zone (31/160, 33/160)).
Length check (FACT): 31/160 − 49/256 = 248/1280 − 245/1280 =
3/1280
, so c = 19·3/1280 = 57/1280 ≈ 0.0445 < 1/16. ✓
PROOF (sketch):
I restricted to the three {1,2,3,4}-safe intervals on [0,½]: [1/16, 15/64], [17/64, 5/16], [17/48, 15/32], then enumerated all forbidden zones of speeds 10–19 inside each (each zone (k/v − 1/16v, k/v + 1/16v), k/v ∈ interval) and merged them.
Inside (49/256, 31/160) no zone of any speed lands: nearest left-neighbors are 16·k=3 ending at 49/256, 11·k=2 ending at 33/176 = 0.1875, 17·k=3 ending at 49/272; nearest right-neighbors are 10·k=2 starting at 31/160, 15·k=3 starting at 47/240 = 0.19583. At the endpoints themselves ||16t‖ = ||10t‖ = 1/16 exactly, so the closed piece is safe.
All other gaps are strictly shorter: 5/2912, 1/1088, 1/720, 1/544, 1/1056, 1/1792, 3/3328, 3/3040, 1/3744, 1/3808, 1/3840 — max ≈ 0.00184 < 0.00234. So 3/1280 is the global maximum (symmetry gives equal pieces near 1 − t).
Least-sure step: the hand enumeration of zones in [17/48, 15/32] — I initially missed the v=14, k=6 zone (95/224, 97/224) and v=16, k=7 zone (111/256, 113/256); a further missed zone could hide a longer piece, though the winner 3/1280 matches the computer claim, which is strong corroboration.

--- end verbatim ---
END LETTER
