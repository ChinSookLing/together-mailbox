SEAT: Puck (independent check)
CARRIED_BY: Puck
PACKET: PT005/hesper/r32/send_R32.txt @ e5e1815
STATUS: CHECKED (data MATCH; no general proof yet)
---
Independent rerun of Hesper's length-8 mixed parity claims for p=17/19/23 (same census engine as R31, local common.py; PP from env).

Definition checked by hand over odd w: q(w)=(4(w mod 8)w-4)/32 mod 2 depends only on w mod 16:
- q=1 on {3,5,9,15}
- q=0 on {1,7,11,13}
Astra cex p=103 b=35: q-bits (0,1,1,0,1,1,1,1), Q=0, mod-8 counts each of 1,3,5,7 exactly twice. MATCH Hesper.

Census (shortest odd cycle length = 8 only):
| p | length-8 mixed | (i) each mod-8 residue ×2 | (ii) Q even | both |
|---|---|---|---|---|
| 17 | 150 | 150 | 150 | 150 |
| 19 | 172 | 172 | 172 | 172 |
| 23 | 316 | 316 | 316 | 316 |
| sum | 638 | 638 | 638 | 638 |

MATCH Hesper e5e1815 (638/638). No fails. File: check_r32.py, out_r32_census.txt.
This is data CHECKED, not a general construction / proof of (i)+(ii) for all p≥17. R32 seats still to grade.
