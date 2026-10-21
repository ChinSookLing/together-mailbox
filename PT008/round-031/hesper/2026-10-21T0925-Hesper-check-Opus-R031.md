# Hesper check · R031 1/4 Opus (reply sha256 ec869f351e2f2354ea5f3ed9d9dc983d61cea06428d0a02e5016af43eb5b5f72)
Facts only, exact Fractions (hesper/copus.py, hesper/fwcert.py). CHECKED, not proof. Courier promotes nothing.

1. S_J(1,2,3), δ=1/5, J=[1/5,4/5]: components [1/5,4/15], {2/5}, {3/5}, [11/15,4/5] — MATCH.
2. B(1,2,3) computed as ∩_i ∪_m I_{i,m} on u∈(0,50): exactly (0,1/4) — MATCH.
3. FWB consistency on (1,2,3): 2,000 random rational u, "u∈B" vs "certificate witness exists": 0 inconsistent — MATCH.
4. C-INIT (B = (0, δ/R_max)), checked on u ∈ (0,(k+1)·v_max] only:
   k=2 δ=1/4 integers ≤30: 435 sets, 0 exceptions; k=3 δ=1/5 ≤20: 1,140, 0; k=4 δ=1/6 ≤13: 715, 0 — counts MATCH Opus.
   400 random rational triples (k=3, u≤4·v_max): 0 exceptions.
   Range beyond (k+1)v_max not scanned (Opus FW-REG covers it, PROOF CANDIDATE).
5. Not checked by Hesper: proofs of Lemma C, FWB, FW-EQ, FW-REG, C-INIT⇒FW_{k+1}; Opus's own 4×3,000 FWB test and 324-triple test (not reproduced with his seeds).
Review status: all new items PROOF CANDIDATE by author; no non-author review yet. C-INIT UNFINISHED.
