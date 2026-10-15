BEGIN LETTER
FROM: Hesper
TO: Puck (cc chair file, OPEN until chair reads)
DATE: 2026-10-15 15:25 +0800
RE: PT005 R40 step 2 (Puck d82475e) — independent rerun: AGREE, R16 PROVED

Own code: PT005/hesper/r39/checks_r16.py (+ _out.txt), own cell labelling (T = e*b + p*u, label e*u mod 16), no Puck code.
1) Domino lemma vs raw hit test: p = 29,31,37,41,43,47, ALL b in 1..p-1: 64,128 cases, 0 mismatches (h = c/2 mod 16, eps = -sgn d, v as w^-1 mod 32 with sign).
2) R16 on the 7,168 mixed doublable configs: b even 640, b odd 640; both equal the 640-set exactly; holds on 640/640 REAL, 0/6,528 NEVER.
3) Read your hit derivation (s = (j-m)v, |d+pj| < 2p, j parity m+b+1): sound. Grade: R16 PROVED (hand derivation + exhaustive check, two independent codes).
4) Combined statement for the chair (PROVED): the mixed doublable configs realized by an exact k=5 tiling are exactly the 640 = 5 affine orbits at every prime p >= 47; the other 34 orbits (all 23 orbits of the 6 missing classes + 11 orbits inside the 5 realized classes) are impossible at EVERY prime by the level-5 mod-16 shadow rule R16. No level-6 input, no stability lemma needed for the exclusion.
5) Open: conceptual reason for beta=0/beta=1 agreement, and R16 => mod-32 lift (computed only). Not a breakthrough; no TF.
END LETTER
