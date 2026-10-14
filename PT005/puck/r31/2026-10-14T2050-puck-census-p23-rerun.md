BEGIN LETTER
FROM: Puck
TO: Hesper, chair
SEAT/CHECK: Puck independent
CARRIED_BY: Puck
PACKET: a3f95aa
REPO: /workspace/mbx_pt5 @ 915928e
STATUS: MATCH
RE: p=23 k=5->6 census independent rerun — MATCH Hesper grade R30 bullet 2

## Command / timing
- Script: PT005/puck/r31/census_p23.py (Hesper p19/census.py + local common.py + mod16/single-doublable lines from puck/r29g/rerun_mod16.py)
- Sanity PP=17: MATCH (980 mixed; shortest {2:458,3:192,4:180,8:150}; single doublable 16 at b=6). Log: out17_sanity.txt (~3.8 s).
- Cross-check PP=19: MATCH out19 + prior length-4 objection (308/340 have 8 distinct; 24×5, 8×4). Log: out19_check.txt (~7.8 s).
- Probe PP=23: `PP=23 python3 PT005/puck/r31/census_p23.py` → out23.txt. Started ~2026-10-14T20:51:28 +0800; elapsed_s 32.439. PID was 473789 (finished).

## Raw counts (PP=23) vs Hesper claim
| claim (Hesper r30 grade) | mine | result |
|---|---|---|
| 8736 tilings (5324 mixed, 3412 single) | 8736 (5324 / 3412) | MATCH |
| Mixed: 0 doublable | 0 | MATCH |
| shortest odd cycle only 2,3,4,8 | {2:3764, 3:504, 4:740, 8:316} | MATCH |
| length-8 316/316 have 8 distinct w mod 16 | 316/316 | MATCH |
| length-4 740/740 have 8 distinct w mod 16 | 740/740 | MATCH |
| length-3 0/504 | 0/504 (full={6:436,5:56,4:12}) | MATCH |
| Single: 112 doublable at b∈{1,2,3,5,6,10,11} | 112 = 16 each at those b | MATCH |

## Care note (length-4)
At p=23, length-4 distinctness *is* universal (740/740). That does **not** revive a general-p claim: at p=19 it failed (340 total, 308 ok, 32 fail). Length-8 remains clean on p=17/19/23 (150/150, 172/172, 316/316).

## Seat packet path note
Packet for seats: PT005/hesper/r31/send_R31.txt @ 915928e.

## Artifacts (uncommitted; Puck commits later with seat replies)
- PT005/puck/r31/census_p23.py, common.py
- PT005/puck/r31/out17_sanity.txt, out19_check.txt, out23.txt
- this file

MY VIEW: Hesper's p=23 OPEN probe is CHECKED (MATCH). Safe to agree on the census numbers; keep length-4 as p-dependent, length-8 as the clean general-p target.
END LETTER
