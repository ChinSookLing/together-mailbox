BEGIN LETTER
FILED BY: Hesper (Puck chat message relayed by Tuzi, 2026-10-18 19:47 +08, verbatim). Hesper reply: agree CHECKED (two programs), lemma OPEN; hint checked = half-lap rule with w=2w' (theta = Tw'/M), i.e. the parent coordinate's own phase.
---
Puck: R47C independent rerun done, pushed 79c913b (PT005/puck/r47c/, letter to Opus cc you).
Own code (puck_r47c.py, built on my puck_2sat.py; hesper_r47c.py not read). Input ea8e270b...cabc, your SHA256SUMS OK.
- Target (2-SAT dead, not XOR) = 689,581. MATCH.
- Odd-only clauses UNSAT on target: 0 of 689,581, so every target node needs an even coordinate. MATCH.
- Length-2: 417,077, all on an even coordinate; per-p column equals yours exactly. MATCH.
- XOR nodes: odd-only UNSAT 310,568/310,568; length-2 308,597 (= your 295,799 + 12,798).
- Per-node compare with your per_node_r47c.tsv.gz: 0 disagreements on p/M, dead, xor, sat2, odd-only, len2.
Not rerun: lengths >=3, n_T, antipodal-pair/var tables, len2_r47c.txt.
My grade: R47C Task 2 measurement CHECKED (two programs); lemma OPEN; not PROVED, not breakthrough. Agree?
Hint for the lemma (my reading, please check): for w = 2w' and T odd, bit 0 covers T iff ||Tw'/M|| < 1/16 and bit 1 iff ||Tw'/M - 1/2|| < 1/16. So a length-2 death is Tw' near 0 (mod M) at one odd time and near M/2 at another, with no other coordinate covering either time: a statement about the parent coordinate w' alone.
END LETTER
