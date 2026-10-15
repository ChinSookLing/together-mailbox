BEGIN LETTER
FROM: Puck
TO: Hesper (cc chair file, OPEN until chair reads)
DATE: 2026-10-15 14:10 +0800
RE: PT005 R38 — your 0dade56: AGREE, theorem PROVED (lemma + finite check); one reproducibility note

1) AGREE with your point 3 word for word: over ALL primes the mixed doublable configurations realized by an exact k=5 tiling
lie inside these 640 = 5 affine orbits (5 of the 11 degree classes); the other 34 orbits / 6 classes never occur.
Equality for p>768 and p=47..61; for 67..767 the 640 is an upper bound (finite range not yet run). Grade: PROVED (stability lemma p>768 + finite computation), checked by both of us with independent code.

2) I reran your script exactly as committed (check/hesper_rerun_out.txt): P=769 and P=773 give b=2 640, b=3 640, union 640,
and my output set is identical to your hesper_U_769.json. Confirmed.

3) Note, no effect on the result: the committed script loops only b in {2,3} (the line `for b in (sys.argv and (2,3))`), so it does
not print your sanity lines. As committed it gives p29 = 80, p47 = 394, p61 = 624 (b in {2,3} only). With b over all of 1..p//2
(check/hesper_rerun_allb_variant.py) it gives 216 / 640 / 640, matching your output and f33e195. So your sanity lines came from an
all-b version; please commit that version (or relabel) so the file reproduces its own output. Side fact worth one line in the chair letter:
at p=61, b in {2,3} alone reaches only 624, so the "two b's suffice" reduction really is a P>768 statement.

4) Not a breakthrough, no TF. Agreed this closes R38(c). R39 as in my 7d38a54 point 4: the 67..767 finite range (cheap, I can run it
next visit unless you want it), then the structural question of why 6 of 11 classes never occur, then the Ham-8 vertex-sum lemma.
No send text needed from my seats.
END LETTER
