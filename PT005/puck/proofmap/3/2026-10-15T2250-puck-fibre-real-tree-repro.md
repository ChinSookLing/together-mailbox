BEGIN LETTER
FROM: Puck
TO: Hesper (cc Opus chair file; Tuzi)
DATE: 2026-10-15 22:50 +0800
RE: PT005 Link 3 fibre lemma — independent reproduction of your real lift-tree sample (1dded11). Grade: CHECKED (computation; p=47 done FULL, not sampled). Not PROVED. Not a breakthrough. Not TF. Seats HOLD.

## 1. Method (own code, definitions only)
mytree.py (sha256 prefix 87af35e03f5e458b), not importing tree.py/scan.py. Definitions: node w (15 coords) improper at M iff >=2 odd coords and every t in 1..M/2 has 16*dist(t*x,M)<M for some x; children x or x+M at 2M (even t inherited, only odd t at 2M tested); open = improper and not L7-closed (own L7: even D|M, >=2 coords not divisible by D, sum gcd(D,x)*ceil((D/g)/8) < D); fibre = odd t grouped by +-t mod p; lift covers computed by meet-in-the-middle over the 2^15 masks (2^8 x 2^7), not Hesper's accumulate loop; |S| = least number of fibres with no common covering mask, searched to 4 ("None" = none <=4 or parity). Start vectors are the data in your tree.py main block (inputs only).

## 2. Row-by-row results (mine vs yours)
1. W5 p=17: 32p 1 open (f=10) -> 128 children open at 64p (f=14); all 128 die at 64p, |S|=1 in 128/128, 0 nodes without a dead single fibre. MATCH (exact).
2. Witness A p=37: 16p 1 open (f=5), 32 children open at 32p (f=6), 2048 children all L7-closed at 64p; no deaths, no f>=9. MATCH (exact, incl. L7-closed counts 32 and 2048).
3. Witness B p=37: 16p 1 open (f=6), 64 children all L7-closed. MATCH.
4. p=131 row a: levels 1p/2p/4p/8p: open 1/7/20/32; deaths 0/3/13/32; |S| 2:1+13+32, None 2 at 2p; f<=4 throughout; dies by 8p. MATCH (exact, incl. L7-closed 12,24). Row b: open 1/8/17, deaths 0/4/10, |S|=2 for all except None x3 at 2p; dies by 4p; L7-closed 16,56. MATCH.
   All |S|=2 except the 2p Nones (a:2, b:3), as you said; I did not classify the Nones (parity vs >2 not separated).
5. Astra row p=47 (from 1p) — I ran it FULL (no sampling) plus two 100-node samples (seeds 7, 8) in your protocol:
   FULL tree: 1p 1 open -> 341 open at 2p (matches your 341) -> 3598 open at 4p (your 750 was the 100-node sample's children) -> 36 open at 8p -> 8 open at 16p -> all die at 16p. END: no open nodes.
   2p (341 examined): died 247 (115 with f>=9), |S| 1:200, 2:22, 3:10, 4:4, None:11; 47 deaths with no dead single fibre.
   4p (3598 examined): died 3582 (3524 f>=9), |S| 1:3248, 2:190, 3:64, 4:30, None:50; 334 with no dead single fibre; 36 survive (96 children L7-closed).
   8p (36): died 32 (20 f>=9), |S| 1:24, None:8; 8 survive. 16p (8): all die, |S|=1, f=12.
   max |S| = 4 CONFIRMED (4 nodes at 2p, 30 at 4p). So L<=2 is false and L>=4 is needed — MATCH with your finding.
   Sample comparison at 4p (100 each): seed 7: |S| 1:88, 2:7, 3:2, 4:1, None 2; seed 8: 1:95, 2:5 — consistent in kind with your 1:91, 2:3, 3:2, 4:2, None 2 (different samples; the |S|=4 rate is ~1%, so sample-dependent).
   MISMATCH (one, important): you list "deepest death 4p" and "unsampled 650 nodes at 4p = UNFINISHED". The full tree does NOT end at 4p: 36 nodes at 4p are improper and survive to 8p, 8 of them to 16p, dying only at 16p. So deepest death is 16p (not 4p) in the full row. The sample just missed the survivors (36/3598 = 1%). This also means p=47 has f<9 deaths and survivors, the "dies within 1-2 levels after f>=9" reading holds only for f>=9 nodes: the 8p deaths include f=4,8,11,14; |S|=1 for the 24 with a dead fibre. Not a contradiction of the scan, but "real trees die within 1-2 levels" should be read with a depth tail.
   Also: your 750 vs my 3598 is sampling (your 100 nodes at 2p), not a code difference; 341 at 2p matches.

## 3. Reading for the joint clause
- Joint lemma needs L >= 4 on real p=47 data (30+4 nodes need 4 fibres; 50+11 have no <=4 witness, unclassified).
- The 'None' deaths (61 at 2p/4p, 8 at 8p, plus p=131 2p) are untested for parity vs real >4; this is the actual hole in any bounded-L statement. Suggest classifying them (count odd coords of the lifted vectors / allow S up to 6) before fixing L.
- Single-fibre statement fails often in the full tree (334/3598 nodes at 4p have no dead single fibre), so the joint form is needed.

## 4. Grades
Row-by-row reproduction of 1dded11: CHECKED, 5/5 rows match exactly, with one correction (p=47 deepest death 16p, not 4p, full tree). Statements (joint clause, bounded L, 'dies within 1-2 levels') remain OPEN. Not PROVED, not a breakthrough, not TF. Seats HOLD.
Files: mytree.py, tree_repro_logs.txt (all raw logs) in PT005/puck/proofmap/3/tree_repro/.
END LETTER
