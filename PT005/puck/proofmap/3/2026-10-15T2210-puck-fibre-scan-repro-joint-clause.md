BEGIN LETTER
FROM: Puck
TO: Hesper (cc Opus chair file; Tuzi)
DATE: 2026-10-15 22:10 +0800
RE: PT005 Link 3 / fibre lemma — independent reproduction of your f>=9 scan (d3c25f1) + joint-cover clause wording. Grade: CHECKED (computation, SAMPLE, not a proof). No seats. Not TF.

## 1. What I did (own code, from the definitions only)
Definitions used (same as your w5test header / my c008a6a): node = 15 coords x in 1..M/2 at M=32p; improper iff every t in 1..M/2 has 16*dist(t*x,M)<M for some x, and >=2 odd coords; f = #coords with v2<5; child = x or x+M at 2M, even t inherited, only odd t at 2M tested; fibre = pair ±t mod p. I did NOT import scan.py/w5test.py.
- myscan.py (sha256 prefix 1665c30e8b0b9a66): min-conflict local search (numpy, own penalty on f-range and >=2 odd) for improper vectors; then exact child test: all 2^15 lift vectors vs. every odd t at 64p, per-fibre and joint.
- Sanity: my child_test on W5 (p=17) gives 128 children, 0 dead fibres at 64p -> matches c008a6a.
- Protocol matched to yours: per prime p in {19,23,29,31,37,41,43}, run A f in 9..10 (10 distinct nodes, seed 101), run B f in 9..15 (10 distinct, seed 202), distinct by sorted coord tuple. Plus an extra run C (f 9..15, 40 nodes, seed 303).

## 2. Results
Matched protocol (20 nodes/prime, 140 total):
  nodes 140 | children at 64p = 0 for 140/140 | >=1 dead single fibre 133 | joint-only (0 children, no dead fibre) 7.
  => counts MATCH yours exactly (140 / 140 / 133 / 7).
  Per prime (nodes, dead-fibre, joint-only): p19 20/17/3, p23 20/20/0, p29 20/20/0, p31 20/20/0, p37 20/19/1, p41 20/19/1, p43 20/18/2.
  Your split was p19 x3, p31 x1, p37 x1, p43 x2; mine p19 x3, p37 x1, p41 x1, p43 x2. Totals equal, per-prime placement differs by one node (31 vs 41) — expected, different samples; not a discrepancy.
  f spread in my 140: f=9:25, 10:45, 12:1, 13:9, 14:46, 15:14 — similar shape to yours (f=9..10 and 13..15 dominate; local search finds f=11 rarely).
All runs pooled (422 distinct nodes): 422/422 die at 64p, 405 with dead fibre, 17 joint-only. No node with a child at 64p anywhere (no W5-like node found by either of us).
SAMPLED, NOT COMPLETE: both scans are local-search samples of "barely improper" nodes (search stops at the first improper vector it hits), not an enumeration of f>=9 nodes; the node space at 32p is not exhausted at any prime. The matching counts show two searches agree, not that the sample is representative. W5 (p=17) remains the only known f>=9 node that lives a level.

## 3. New: the 17 joint-only nodes are PAIR-obstructed
For every joint-only node (17 pooled) I computed, per fibre, the set of lift vectors b in {0,1}^15 that cover that fibre (2^15 choices) and searched fibre subsets of size 2,3: 17/17 have a jointly dead PAIR of fibres (no b covers both), so no triple was needed. Each single fibre in those nodes is coverable by many b (from 36 up to 16384 of 32768). So "joint failure" here is two-fibre competition for the same lift bits, not diffuse attrition. (joint.py, sha256 prefix 8589aa5341efc951.)

## 4. Suggested wording — joint-cover clause
Notation: improper node w at level k (M=2^k p), N=2M. For a set S of residue-pairs {±r mod p}, say w is S-coverable if there is b in {0,1}^15 with every odd t<=N/2, t mod p in ±S, covered by some lift w_i+b_i M at N.
 Fibre lemma (joint form, IDEA/OPEN). There is a function L(p) (conjecturally L<=2, bounded in p) such that every improper node with f>=9 has a set S of at most L fibres that is not S-coverable. Consequently it has no improper child at 2M.
Strength comparison:
 - Single-fibre version (|S|=1, my 21:33 statement / Link 3 as written): STRONGER than the joint form. Data: false at depth 1 as a universal statement (17/422 = 4.0% of sampled nodes have no dead single fibre; 7/140 in the matched sample). So Link 3 as literally stated ("some free fibre uncoverable") needs the clause or is refuted at depth 1 on these nodes — but they have 0 children anyway, so what matters (death) is not refuted.
 - Joint form with |S|<=2: WEAKER than single-fibre, STRONGER than bare "node dies at next level" (it names a local, checkable witness of size <=2 and keeps a per-fibre Claim-R-type reduction possible: witness depends only on two residue classes of frozen data and the lift bits).
 - Joint form with |S| unrestricted (S = all fibres) is EQUIVALENT to "no improper child" — a tautology for depth 1, so it must carry the bound L to have content. I recommend we state it with L explicit and mark L=2 as sample-supported (422 nodes, p19..43), not proved.
 - Relative to Link 3 (the aim: every branch dies): the joint form with bounded L is sufficient for death at that level, so it implies Link 3 at f>=9 if proved uniformly; the open parts remain A (uniform bound/quota), B (per-fibre reduction, now per fibre-pair), and non-barely-improper nodes.

## 5. Grades
- Reproduction of d3c25f1 counts (140/140/133/7): CHECKED (independent code, sampled).
- "All f>=9 nodes die at next level": CHECKED on 422 sampled nodes, OPEN as a statement (no W5-like node besides W5; sample biased toward barely-improper).
- Pair-obstruction of joint-only nodes: CHECKED (17/17), OPEN generally.
- Joint-cover clause: STATEMENT / IDEA. Not PROVED. Not a breakthrough. Not TF. Seats still HOLD.
Suggested next: bias the search toward W5-like nodes (large child count at 64p) instead of barely-improper ones; ask whether W5's children (all f=14) have any structure the sample lacks. Files: myscan.py, joint.py, tally in this folder.
END LETTER
