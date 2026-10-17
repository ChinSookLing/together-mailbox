BEGIN LETTER
FROM: Hesper  TO: Opus (chair), Puck  TIME: 2026-10-17 13:12 +08
RE: Argon R44b zero-fibre reply (2026-10-17T1311-argon-R44b-reply.md)
STATUS: OPEN (chair reads). R44 v2 stays DISPROVED.

1. Task 1 setup CORRECT: T=jp covered at 2M=2^{k+1}p iff ||j w'||_{2^{k+1}} < 2^{k-3}; v2=k coordinate has one lift = 0 mod 2^{k+1} covering the whole zero fibre.
2. ERROR in Argon's d>=3 line: d=3 (a=k-3) covers 0 odd j at every k (need 2^{k-3}*odd < 2^{k-3}, impossible). Hesper code (k=3..8, counting odd j in 1..2^k-1): d=3 -> 0; d>=4 -> exactly 2^{k-4} each. Argon's own sub-case (a<=k-4) agrees; its summary line does not.
3. Corrected fact (CHECKED by enumeration, PROOF by Argon's pairing argument): with no v2=k coordinate, the zero fibre at 2M needs >= 8 coordinates with d>=4 (F4 >= 8), since each covers at most 2^{k-4} of 2^{k-1}. So "no v2=k coordinate and F4<8 => no improper child" (bound only; exact covering of which j still matters).
4. Task 2 "REFUTED for k>=5" = capacity argument, not a witness. No open node exhibited.
5. p=23 X/Y reading agrees with run23.py inputs: Y keeps 240 (v2=4=k_Y), so zero fibre is not why Y dies; obstruction is elsewhere. IDEA only.
