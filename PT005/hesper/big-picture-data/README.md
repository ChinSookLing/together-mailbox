# Big Picture data files (PT005 Hesper, 2026-10-11 ~16:55 +08)
All values computed by Hesper in Python from the files named in each CSV's source column. Not peer-reviewed.
- census14_covers.csv — 33 primes 307–499, 14-speed cover counts (census14 final run 37981873336). Zeros: author engine only, no independent recount.
- d_min_found.csv — 457 (exact D=0) + the 23 rows of r12-check/hesper-r12-findings.md. Column kind: exact / upper bound. U of every set re-counted. Columns M_independent and E_exact_distinct.
- random457_seed20261011.csv — 12 random 14-sets at p=457 (Python random.Random(20261011), sample(range(1,229),14)), with U and R_K for K=4,8,16,64,full via scouting/LR16/opus/guess_r10/resonance_K.py. NOT the 12 sets of chair note 65 (those are not in any file).
- pstar_N.csv — chair note 64 table, with kind per row. N=19,21,23 absent (not computed).
- subgroup_p1mod28.csv — empty cosets of the order-28 subgroup G_p for all p≡1 (mod 28) ≤ 20000 (503–599 has none); script subgroup.py.
- subgroup_281_449_sets.csv — the 14 speeds of G_281 (U=0, a cover) and G_449 (U=56).
