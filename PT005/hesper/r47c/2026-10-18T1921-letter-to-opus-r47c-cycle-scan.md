BEGIN LETTER
TO: Opus
FROM: Hesper
THIS ROUND SERVES PROOF STEP: explain the non-antipodal 2-SAT deaths (family lemma for the 36 small gates, 157.16)
AS_OF: 2026-10-18 19:21 +08 (TZ=Asia/Kuala_Lumpur) · cc Puck
STATUS: Task 1 CHECKED (third program; matches chair and Puck). Task 2 OPEN — one program (Hesper), measurement only, full set (no sampling).

SUMMARY (≤5 lines)
1. Note 104 §2 (erratum 1523 does not change the number): own program finds **310,568** antipodal-XOR dead nodes = chair 310,568 = Puck; **0 live flagged**; 0 xor-flagged nodes outside the 2-SAT set.
2. 2-SAT reproduced in passing: 1,000,149 dead, 0 live; **0 per-node disagreements** with chair sat2_per_node.csv.gz (56fb1427…) and with Hesper r47 per_node_hesper.tsv.gz.
3. Target set = 2-SAT-dead and not XOR-flagged = **689,581** nodes. Shortest implication cycle length: 2 → 60.48%, 3 → 28.59%, 4 → 8.81%, ≥5 → 2.12% (max 13).
4. **Every one of the 689,581 needs an even coordinate** (tie-free test: unit+binary clauses on odd-only coordinates are SAT for 689,581/689,581). On the chosen witness an even coordinate appears in 100%.
5. Minimum contradictory clause set (exact for these rows): 2 times for 417,077 nodes (one even coordinate forced to opposite bits by two unit clauses at two non-antipodal times), 3 times for 199,368; the rest ≤ 4–10 (upper bounds).

## Method
Input: PT005/hesper/r45/widen/nodes_widen.csv.gz (sha256 ea8e270b…cabc), k ≥ 1 nodes only: 1,107,829 (dead 1,088,175). Code written from notes 103/104 + erratum 1523; xor.py and sat2.py were not imported or copied.
- **Literals.** Child level N = 2M, var i ∈ 0..14, bit b; lift wᵢ + bM covers odd T iff 16·min(r, N−r) < N, r = T(wᵢ+bM) mod N. Clause at odd T ∈ [1, M] = OR of covering literals (erratum: at least one, not all). Integrity counters over the whole set: tautological clauses 0, empty clauses 0, pairs (T, M−T) with E(M−T) ≠ E(T): 0, odd coordinates without complementary bit at the antipode: 0.
- **Task 1.** For odd T < M/2 with E(T) all-odd and |E(T)| ≤ 2: |E| = 1 → contradiction; |E| = 2 → bᵢ ⊕ bⱼ = aᵢ ⊕ aⱼ ⊕ 1 (a = covering bit at T). Consistency is decided by reachability (i,0) → (i,1) on the 30-vertex parity-lifted graph, using boolean Floyd–Warshall. This is not union-find and not the node-level h-formula.
- **Task 2.** Implication graph from unit clauses (¬l → l) and binary clauses (¬l₁ → l₂, ¬l₂ → l₁). Each edge is labelled with the smallest T that produces it. Min-plus Floyd–Warshall with next-hop. Witness = the var x minimising d(x,¬x) + d(¬x,x); ties go to the lowest var index, then to FW next-hop order. Recorded per node: cycle length (number of implication edges in the closed walk x ⇒ … ⇒ ¬x ⇒ … ⇒ x), distinct T, antipodal pairs among those T, distinct vars, and whether an even coordinate is on the witness. Also recorded, independent of tie-breaking: whether the node is still UNSAT using only clauses whose coordinates are all odd.
- **Self-test** (selftest_r47c.py, random.Random(47003), deterministic): 3,000 target nodes, brute force over all 2^15 lifts. The witness T-set clauses alone are UNSAT in 3000/3000, and irredundant (dropping any one T gives SAT) in 3000/3000. Also 500 non-2-SAT nodes: unit+binary over all odd T is SAT in 500/500.
- **Exactness note.** A 2-clause unsatisfiable set of ≤2-literal clauses must be two opposite unit clauses, i.e. a length-2 cycle. So for n_T = 2 and n_T = 3 rows the witness size is the true minimum. For n_T ≥ 4 it is an upper bound, and the witness is irredundant but may not be minimum.
- **Run.** Full set, 2 processes, about 3 min wall. No sampling needed.

## Tables (target: 2-SAT-dead, not XOR-flagged; 689,581 nodes)
Cycle length, overall: 2: 417,077 (60.48%) · 3: 197,154 (28.59%) · 4: 60,774 (8.81%) · 5: 3,008 · 6: 8,047 · 7: 1,621 · 8: 1,248 · 9: 234 · 10: 342 · 11: 40 · 12: 20 · 13: 16.
Distinct T, overall: 2: 417,077 · 3: 199,368 · 4: 67,224 · 5: 4,482 · 6: 962 · 7: 186 · 8: 34 · 9: 8 · 10: 240.
Antipodal pairs among the witness T: 0: 502,259 (72.84%) · 1: 142,703 · 2: 44,619.
Distinct vars: 1: 417,077 · 2: 201,306 · 3: 65,484 · 4: 4,445 · 5: 817 · 6: 180 · 7: 24 · 8: 8 · 9: 240.
Even coordinate on witness: 100% at every p. Odd-only clauses UNSAT: 0% at every p.

Cycle length per p (columns 2 3 4 5 6 7 8 9 10 11 12 13 | total):
```
p=17 245846 45066  5198  144 2726 144 608  44   8  0  0  0 | 299784
p=19  11596 14574  6116  128  122  20  44   4   0  0  0  0 |  32604
p=23  56230 47452 15856  400 1408 664 212  32  12  4  0  0 | 122270
p=29    296   988   942   40   90   0   8   0   0  0  0  0 |   2364
p=31      6    50    36    0    0   0   0   0   0  0  0  0 |     92
p=37     26   166   178   24    6   0   2   0   0  0  0  0 |    402
p=41   4338  4204   801   18    4  32  26   0   4  4  0  0 |   9431
p=43  86903 67126 25290 1450 3208 562 280 110 302 28 16 12 | 185287
p=47   1762  3717  1533   34   72   4   4   0   0  0  0  0 |   7126
p=53   7384 10618  3658  680  346 166  54  36   6  4  4  0 |  22956
p=59   2224  2122   663   83   50  29   8   8  10  0  0  4 |   5201
p=61    466  1071   503    7   15   0   2   0   0  0  0  0 |   2064
```
Distinct T per p (columns 2 3 4 5 6 7 8 9 10): in tables_r47c.txt.
Joint (length, n_T), top rows: (2,2) 417,077 · (3,3) 197,154 · (4,4) 58,560 · (6,4) 6,197 · (5,4) 2,467 · (4,3) 2,214 · (6,5) 1,711 · (7,5) 1,482.

Comparison, XOR-flagged 2-SAT nodes (310,568): (2,2,odd-only) 295,799 · (2,2,even on witness) 12,798 · others ≤ 1k. The chosen shortest witness for an XOR-flagged node can be a non-antipodal even-coordinate pair of the same length.

Extra, length-2 witnesses (len2_r47c.txt): the forced even coordinate w has v₂(w) spread from 1 to 9. The commonest is (k, v₂(w)) = (6, 4) with 184,816 rows. (T₁+T₂) mod M: the commonest value is M/2 (54,533), then 3M/16, M/16, 5M/16 and M/4. No single relation covers the set. This is a raw tabulation; no conjecture is drawn here.

## Reading (measurement, not a claim)
The non-antipodal 2-SAT deaths in this Track A set always need a clause that touches an even coordinate. Most often (60%) the contradiction is one even coordinate whose two unit clauses at two times T₁, T₂ (not antipodal) demand opposite lift bits. A family lemma for these would have to be about even coordinates, i.e. inherited coverage w = 2^j·w′, not about the antipodal swap. This is OPEN, and it has one program behind it. Puck or the chair: an independent rerun of at least the "odd-only SAT for all 689,581" and the length-2 count would make it CHECKED.

## Files (PT005/hesper/r47c/)
```
d31f6b1fcf7c0e53e6b9a56d0b6766363aabd5dd516044d57137ab997a3afd1a  hesper_r47c.py
be9eecdd921435812e37d232bbc965b424e9182d3e2990a62ffe597c45687c10  selftest_r47c.py
61d614f56b0595f9a7130e36c467667d856bc9b3ebf07243e4642150025c3e8c  tables_r47c.py
d7f70ebd60ff978b51a54c66a577911424f58d897e79458f616acb0e7f1adf49  len2_r47c.py
461968c4fe5656582b8719174684defe552bfd4b6581c2c19791b6b6f410aa03  run.out
a910412536a2e9f9fdd2e9935305e97ed1ad65db822f8a0540919a29f8928cf0  selftest.out
a41ce63b8dfea82f879c0cc3d673b05820edb75444fc9db140ca40125a281b52  tables_r47c.txt
185274cfef90653f12e55db62f183b136dfb37f3ecd36cc40a7a5b096998754b  len2_r47c.txt
ae3f2e1368f5369fce0ce6083f52a44ada3f894d8c73ac38680b5a660bd09a67  per_node_r47c.tsv.gz
4ba4c248614451a6f06bbad894675dbe174a083e18a0b62d5a43c7003935cc76  SHA256SUMS
```
Reproduce: `python3 hesper_r47c.py ../r45/widen/nodes_widen.csv.gz && python3 tables_r47c.py && python3 selftest_r47c.py && python3 len2_r47c.py` (numpy).
per_node_r47c.tsv.gz columns: p M coords dead xor sat2 cyc_len n_T n_anti_pairs n_vars even_on_witness oddonly_unsat witness_T.
END LETTER
