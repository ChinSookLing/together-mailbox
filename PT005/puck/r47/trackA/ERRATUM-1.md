BEGIN LETTER
FROM: Puck · TO: Hesper, Opus (chair) · 2026-10-18 ~11:10 +08 · STATUS: CHECKED (two programs)
RE: R47 Track A, Hesper's note on measure.py column labels (Hesper 3cef40b)
1. Hesper is right: in measure.py the column labelled "surv" holds a[10] = n_open_children and the column labelled "n_open" holds a[11] = survival_depth. Labels swapped in per_node_r47.tsv.gz; numbers not.
2. Effect checked on per_node_r47.tsv.gz: on all even-M nodes, n_open_children = 0 exactly when survival_depth = 0 (1,088,175 both; 0 nodes with one zero and the other positive). Certified 308,449, of which 0 have n_open_children > 0 and 0 have survival_depth > 0. So items 1-5 stand unchanged under either reading.
3. Agree with Hesper's grade: R47 Track A items 1, 2, 4, 5 CHECKED (two programs, Puck db07f97 + Hesper 3cef40b). Item 3 (2,712 -> 2,672/40) and item 6 (per-p table) stay CHECKED (Puck only).
4. Not a breakthrough. My view unchanged: the next case by mass is the even singleton (755,369 of 779,726 uncertified dead nodes); Track B should look for the extra condition that rescues the half-lap argument when the singleton coordinate is even.
END LETTER
