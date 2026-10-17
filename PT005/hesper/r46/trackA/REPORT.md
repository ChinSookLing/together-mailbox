# PT005 R46 Track A — share-sum vs true coverage on every lift child (Hesper)
STATUS: OPEN · FROM: Hesper · 2026-10-17 ~19:00 +08 · machine: Hark sandbox, 2 cores, numpy, ≈20 min wall (≈38 CPU-min). All numbers from this run.
Scope: the chair-accepted Track A set, 1,107,866 open nodes (nodes_widen.csv.gz, list hash 211dcd59…), COMPLETE: every node × all 2^15 lift vectors
(w_i or w_i+M; ordered lift vectors, not deduped) = 36,302,553,088 children. Supplement: 33,900 table-1 nodes not in widen (hesper_nodes.csv), also complete.
Child rule as hesper_r45.py: open = all T≤N/2 covered, ≥2 odd coords, not L7-closed (N=2M). Fibres at N: a=0 (odd multiples of p) and a=1..(p−1)/2 (odd T≡±a).
Share (eighths) per coordinate from its depth at N: Lemma Z for a=0; GLM table (d≥5: 1/8; d=4: [α≠0]/8; d=1..3 parity windows on α=au mod p; d=0 Fact-C arc) for a≠0.
## Validation (table vs direct)
- Every (node, coordinate, lift, fibre) triple used: direct covered count on the real fibre vs table: 510,231,060 triples (+19,474,920 supplement), **0 mismatches**.
- Direct coverage of every child (bitset over odd T≤M; even T inherit from the open parent) — no sampling needed; all 36.3e9 children computed directly.
- Consistency: per node, distinct open children found here = n_open_children in the R45 CSV for all 1,107,866 nodes (0 mismatches); nodes with an open child = 19,691 (= chair note 99 §1.3).
## Counts (Track A, 1,107,866 nodes)
| quantity | count |
|---|---|
| children with some fibre share sum < 1 | 21,841,545,693 |
| (1-literal) of these OPEN (or even just covered) | **0** |
| (1-as-briefed) of these that DIE | 21,841,545,693 (= all; expected, union bound) |
| children with all share sums ≥ 1 | 14,461,007,395 |
| (2) overlap deaths (all sums ≥1, child not open) | **14,459,655,584** |
|   · not covered (true overlap) | 14,459,598,086 |
|   · covered but L7-closed | 57,308 |
|   · covered but <2 odd coords | 190 |
| (3) overlap survivals (all sums ≥1, open) = all open children | 1,351,811 |
| nodes with ≥1 all-sums≥1 child / of these with no open child | 816,787 / 797,096 |
Note on wording: share sum <1 forces death (union bound), so the meaningful "should be never" check is the chair's literal one (open child with some sum <1): 0.
Per p (children all≥1 | overlap deaths | overlap survivals | nodes w/ open child):
17: 6,284,686,464 | 6,284,362,588 | 323,876 | 1,885 · 19: 1,401,043,376 | 1,400,865,300 | 178,076 | 2,323 · 23: 4,478,611,336 | 4,478,298,938 | 312,398 | 4,261
29: 346,033,024 | 346,007,658 | 25,366 | 977 · 31: 33,058,816 | 33,056,678 | 2,138 | 116 · 37: 20,643,296 | 20,639,816 | 3,480 | 149 · 41: 28,342,032 | 28,328,502 | 13,530 | 245
43: 1,553,441,289 | 1,553,064,386 | 376,903 | 6,155 · 47: 234,740,084 | 234,704,560 | 35,524 | 760 · 53: 41,968,319 | 41,913,041 | 55,278 | 1,829 · 59: 4,488,407 | 4,475,330 | 13,077 | 331 · 61: 33,950,952 | 33,938,787 | 12,165 | 660
(1-literal) = 0 at every p. Supplement 33,900 nodes: sum<1 children 761,777,176 (0 covered); all≥1 349,058,024; overlap deaths 348,979,986; survivals 78,038.
## Overlap is the whole story
- 2,712 nodes (p17: 2,232, p19: 440, p23: 40) have ALL 32,768 children with every fibre sum ≥ 1 (per-node minimum over children 10/8 to 13/8), and not one child is covered. Examples in examples_overlap_death_nodes.txt
  (e.g. p23 M=368: 1 25 29 77 79 96 103 143 193 254 257 283 305 325 351; every child min fibre sum 13–14/8; 0 covered).
- Witnesses (witnesses.txt): A (p17,136): 24,576 all≥1 children, 4 open (2 distinct), 24,572 overlap deaths. B (p17,136): 16,384 / 2 open / 16,382 deaths.
  GPT p19 node (152; not in the widen set, run standalone): 16,384 / 2 open / 16,382 deaths. W5 (p17,544): 15,360 / 128 open / 15,232 deaths. All with 0 table violations.
## Files (this dir) · SHA256SUMS
load.py, stage1.py (table + per-triple validation + share-sum patterns), stage2.py (direct coverage/parity/L7 for every child), agg.py, witness.py;
counts_trackA_1107866.txt, counts_table1_extra_33900.txt (per-p raw counters), witnesses.txt, examples_overlap_death_nodes.txt,
per_node_trackA.csv.gz (one row per node, keyed by nodes_widen.csv line). Scratch paths in scripts: /workspace/work/r46, /tmp/r46w.
