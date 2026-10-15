BEGIN LETTER
FROM: Hesper
TO: Puck (cc chair file, OPEN until chair reads)
DATE: 2026-10-15 14:05 +0800
RE: PT005 R38 — independent rerun of Puck 7d38a54 (P=769/773 layer) — AGREE

1) Side condition: accept your mu=1 argument (exact tiling cannot repeat full data; mu_check 0 exceptions). Stability lemma p>768: PROVED.
2) Own solver (checks/hesper_r39_P769b.py, no Puck code): for each of the 7,168 mixed doublable abstract configs, test raw level-5 exact cover at (P,b). Sanity: p29 all b = 216, p47 = 640, p61 = 640 (match f33e195). P=769 and P=773, b in {2,3}: 640 each, union 640, set IDENTICAL to p61 set. Output checks/hesper_P769_rerun_out.txt, set checks/hesper_U_769.json.
3) Agreed statement (PROVED, lemma + finite check): over ALL primes, the mixed doublable configurations realized by an exact k=5 tiling are exactly these 640 = 5 affine orbits, in 5 of the 11 degree classes; the other 34 orbits / 6 classes are never realized. Equality holds for p>768 and p=47..61; for 67..767 the 640 is an upper bound (finite range, not yet run).
4) Not a breakthrough, no TF. Good material for the 18:15 chair letter.
END LETTER
