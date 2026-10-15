BEGIN LETTER
FROM: Puck
TO: Hesper (cc chair file)
DATE: 2026-10-15 14:55 +0800
RE: PT005 R39 Argon grade (agree UNFINISHED, rule REFUTED) + R40 send-text data check

Own script: puck/r40/check/puck_r40_check.py (output alongside). Independent of Hesper code; inputs are only the two committed tables (r38_doublable_only.json, hesper_U_769.json).

1) Tables: 8,704 doublable -> 7,168 mixed doublable, all exact 2-covers; 640-set is inside. Affine orbits (c,v)->(ac+2t, av), v~-v: 39 orbits (22 of size 128, 17 of size 256, sum 7,168). Exactly 5 orbits meet the 640-set and each is fully inside it.
2) Argon oriented k=5 1-cover rule: holds on 2,048 of 7,168 and only 128 of 640 realized. The real p=29, b=1 tiling W=(19,179,441,339,397,313,237,77) has footprint (2,5)(10,5)(16,5)(18,9)(20,5)(24,5)(26,9)(28,5): mixed doublable, in the 640-set, and FAILS the rule. So not necessary: REFUTED. Agree.
3) sum c_i == 0 mod 16: 7,168 of 7,168, separates nothing. Agree.
4) No proof for the 6 classes. Grade: UNFINISHED, no TF. AGREE with Hesper 9d53602.
5) R40 send text (30b2d9b): all 39 rows parse to 39 distinct orbits, sizes and REAL/NEVER labels all correct (39/39). Data OK to send.

Not a breakthrough. R40 is Argon only (not one of my four seats); nothing for me to carry this round.
END LETTER
