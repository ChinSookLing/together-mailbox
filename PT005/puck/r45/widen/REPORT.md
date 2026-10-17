# Puck independent rerun - Hesper R45 Track A WIDEN (874deff / bc7f44d)  [not pushed, nobody messaged]
Program: puck_r45_widen.py (engine = Puck r43f3 puck_f3_check.open_children; no Hesper code). 8 procs, 248 s. Log: run.out
1. Hashes: `sha256sum -c SHA256SUMS` in widen/ -> all 16 OK (roots_widen.txt d9b0fc63...adc). Uncompressed nodelist_widen.txt.gz = 211dcd59f514bdc1ffc2aea6c7a5fce8e095cfed09393106890db84026a796bd.
2. Node list: 1,107,866 nodes, sha256 of sorted list 211dcd59...796bd = Hesper's. MATCH (byte-identical hash).
3. Full CSV (p,k,M,coords,F0..F5,n_open_children,survival_depth): 1,107,866 rows, 0 mismatches vs nodes_widen.csv.gz; first-source column also identical (0 diffs).
4. Exceptions (k>=1, survival>0, F4>=1 or Z/2^(k-1)=[F0>0]+F4/8 >1, excluding W5 itself): 1,320 = exceptions_widen.tsv exactly (0 only-Hesper, 0 only-Puck; F-vector, n_open_children, survival, Z all equal). Breakdown: p=17: 102 at 16p, 1056 at 32p, 130 at 64p (=1,288); p=23 16p: 32. 
5. F0 claim: 19,691 nodes with survival>0, F0=0 among them: 0. CONFIRMED.
6. Coverage caveats: statuses (capped/deferred) were TAKEN FROM Hesper's summary log by label, not re-derived: deferral depends on his memo/processing order. Skipped: 22 capped (not 4: 4 seed roots p19x3,p23x1 + 18 W5sib_a8p) and 267 deferred (255 W5sib_a16p, 12 W5sib_a8p) = 289 roots; 3,890 roots run. Their subtrees (partial info: ~60k nodes with F4>=1 and open child) are NOT covered; also ancestors 4p/2p/1p siblings not run. All 3890 live roots were open under my open_direct check.
7. Ambiguities resolved: (a) F0/Fj and Z definitions as in my R45 program (d_i=k-v2(w_i) or 0 if v2>=k); (b) exceptions exclude W5 (17,544) which is in the node set; (c) k>=1 only. All matched, so no discrepancy to explain.
Verdict: CHECKED by two programs for node list, every CSV column, 1,320 exceptions and the F0 fact, over the completed subtrees only. Still a measurement, not a lemma.
Files: puck_nodelist_widen.txt, puck_nodes_widen.csv, puck_exceptions_widen.tsv, roots_widen.txt, run.out, puck_r45_widen.py
