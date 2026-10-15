FROM: Puck
TO: Hesper
DATE: 2026-10-15 13:30 +0800
RE: PT005 R38 — Argon answer collected + Puck independent check + proposed grade

1) Collection. You were right: the R38 prompt was NOT at the bottom of the Argon chat (the pasted answer was stale R37). I sent send_R38_Argon.txt @ 822308d once, same chat (ChatGPT tab "Prove F1 Criterion", mode "High, 3 of 3", no web toggle present), ~13:02; Argon worked 7m31s. Answer file: PT005/puck/r38/2026-10-15T1310-Argon.md (close English translation, not verbatim; code box truncated, no output shown).

2) Puck independent checks (check/argon_r38_check.py, check/argon_r38_stability_probe.py, outputs *_out.txt):
- p=29 b=1 W=(3,97,125,151,413,191,285,385): exact k=5 tiling YES, mixed, brute doublable YES, F1' YES, simple degree seq (2,3^4,4^3) = Argon's type. CHECKED.
- p=29 b=1 W=(19,179,441,339,397,313,237,77) (NEW to us as a stated example): exact tiling YES; level-5 cover pairs exactly Argon's (1,291),(57,233),(59,463),(115,405),(117,173),(175,347),(231,407),(289,349); mixed; brute doublable YES; simple degree seq (2^6,3,3) = Argon's type. CHECKED.
- p=89 b=36 cex: tiling YES, doublable YES, simple degree seq (1,1,3^6). CHECKED.
- F1'' (dim ker L = dim ker L0) agrees on all three (kerL=kerL0=1,1,2). Note: F1'' is the standard signed-graph Laplacian restatement of F1' (balanced component <=> kernel vector); correct but not new structure.
- Stability recipe (p>768): I transported all three configs exactly by Argon's recipe (keep m mod 32, w mod 32, sgn d, b mod 2; b*=3 or 2; first w in class with 0<±(b*w-mP)<P/2, w mod P not 0,±1) to P = 769, 773, 787, 1009, 2003: 15/15 reduced data same, exact tiling YES, doublable YES. Probe-CHECKED; the interval/pigeonhole proof sketch reads correct to me (it leans on the PROVED k=5 rule). Improves our 12288/16640 bounds to 768 (census says 47).

3) Proposed grade (please agree/object):
- (A) PARTIAL. F1'' correct but equivalent to F1'; Ham-8 corollary still open (Argon's own gap: show the vertex class function sum_i[n_i(r_A)+n_i(r_B)] is odd for mixed Ham-8). The reduction of Ham-8 parity to that vertex sum is a useful, checkable lemma — candidate next target.
- (B) PARTIAL (strong). Constructions CHECKED 3/3. Stability lemma p>768: I propose PROVED-candidate (general construction + 15/15 probe), PROVED once you read the interval argument. Small-prime exclusion (17,19,23) and first prime per class: UNFINISHED.
- Not a breakthrough. No TF.

4) Suggestion for R39: (i) close Ham-8 via the vertex-sum lemma (prove mixed => odd or odd digon on the two-matching 8-cycle; finite check over (c,v) footprints is 16 residues, should be exhaustible by hand table); (ii) lower 768 toward 47 by sharpening the interval count; (iii) small primes stay census (finite, already exhaustive) unless someone gives a structural reason.
