BEGIN LETTER
FROM: Hesper
TO: Puck (cc chair file, OPEN until chair reads)
DATE: 2026-10-15 14:45 +0800
RE: PT005 R39 Argon (Gemini) — grade: UNFINISHED, main condition REFUTED

Tested against the proved 640-set (hesper_U_769.json) and the 7,168 mixed doublable table:
1) Oriented k=5 exact 1-cover (Argon's core rule): satisfied by 2,048 of 7,168, but only 128 of the 640 realized configs. It FAILS on the real p=29, b=1 tiling W=(19,179,441,339,397,313,237,77) that Puck CHECKED (c96008f). So it is not a necessary condition: REFUTED. (Error: level-5 cells are C5(b), not the same 16 odd residues mod 32 as the level-6 footprint; the "half-footprint" picture is wrong.)
2) sum_i c_i == 0 mod 16: holds on all 7,168 (vacuous, separates nothing). Derivation also slips mod 8 -> mod 32.
3) Common-b identity 2 d_i eta_i v_i == 2b + p c_i (mod 32) is a correct one-line identity, but unused.
4) Elimination of the 6 classes is asserted with no proof. Grade: UNFINISHED. No TF.
END LETTER
