BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 08:20 +08
RE: 猜公式 Round 6 (packet 6f1e734), send text r6_send_deepseek.txt
SEAT: deepseek
MODEL: DeepSeek DeepThink ON, Thought for 24 seconds; sent 2026-10-11 ~08:12 +08 with r6c_send_full (correction included)
CHAT: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202

--- reply verbatim ---
ANSWER BLOCK
(a) FACT: The correction breaks my earlier tentative claim that every 14-cover has a scaling with ≥5 small speeds. 389 is a PROOF counterexample, so |K|≥5 is false. Replace with |K|≥4 observed.
(b) FACT: 389 shows core size can be 4. Whether some p≤499 cover has core ≤3 is UNFINISHED from the packet; I suspect possible but unverified. IDEA: core-poor covers use medium near-consecutive clusters—(28,29), (142,143), (94,96)—as fillers, not small odds.
(c) Q4 rule: empirical mod-16 cutoff. For each r=p mod16, let C_r be the largest Data-1 prime with a cover in that class. Predict covers>0 iff p≤C_r. Checked score: 33/33 on Round5 Data1. IDEA: data-fitted, not a terminal formula.
Q1: FACT: 7,8,9,11,13 frequent; 2,3,4,6 rare; 12 count 0. IDEA: even speeds are dominated by doubles; 11,13 avoid overlap. Q3: IDEA: 457 is sporadic; p=4m±1 family alone does not match census.

Reasoning

FACT: v is too near at t iff distance(vt,0) < p/16. PROOF: then 2v is too near iff distance(vt,0) < p/32 or distance(vt,p/2) < p/32. So if v covers a cell, 2v also covers it, when 2v is in range. This dominance helps explain why 2,3,4,6 are poor core choices: they are often replaceable by 4,6,8,12. FACT: 12 never appears in the 23 sampled scalings. IDEA: its role is already covered by 8, 11, or 13; not proved.

IDEA: 7,9,11,13 are frequent because they are odd and not small multiples of each other; 8 is frequent because dyadic powers cover many cells. FACT: the odd core {1,3,5,7,9,11,13} does NOT complete at 317,347,349,359,367. So there is no universal small core.

FACT: 457 = 4·114+1, and scaling by u=4 sends the run 111..117 to odd 1..13. IDEA: for p=4m±1, scaling by 4 can turn near-m runs into small odds, but the census shows only 457 has such a run cover; 449, 461, 467, 479 are zero. So that family is not sufficient.

FACT: my mod-16 cutoff rule fits all 33 Data-1 primes. IDEA: it may reflect a residue-specific upper bound, but it is not proved. Least-sure step: whether a core ≤3 exists at p≤499, and whether r=9 mod16 truly dies after 457.

--- end verbatim ---
END LETTER
