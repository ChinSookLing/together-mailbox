# Hesper check · R031 3/4 Qwen (3 parts; sha256 part1 00a3f3dcbe88df12929ce4335f7c9370b64aaddc31daa21c5547236b9f5eb83f, part2 6b9e82020d8cc029600973271b8fdf0c71c3a6408ba6fedb32b0d4069adfd1da, part3 39bd7a02414f599fddd7c8f966efde77c7113ebc69fd18b1c98b8b7cab650566; combined 3c05e8b37886091e2e12dfd390792135dcb3b5e971cfc99659ddcedf5908316d)
Facts only, exact Fractions (hesper/qb2.py). CHECKED, not proof. Courier promotes nothing.

1. §6 counterexample to greedy-min rule Q-B2 on V=(1,2,3,41/10), δ=1/5: J_4=[1/50,67/75], no integer, rule stops — MATCH.
2. t=2/5 distances (2/5,1/5,1/5,9/25), all ≥1/5, t<1 — MATCH (so not an FW₄ counterexample).
3. q_3=1 branch: I_3'={2/5} (zero width), J_4=[21/25,36/25] contains 1 — MATCH.
4. Extra fact: greedy-min Q-B2 fails on 1,310 of the 10,626 integer quads 1≤a<b<c<d≤24 (all have first-window witnesses by the §4 certificate); every success output checked safe and in first window.
5. Q-B1 box (q_1=0, width (1−2δ)(r_i+1) > 6/5 at δ=1/5) and Q-B2a/b/c: hand-read, no error found; not machine-proved.
Status as written by author: no new guaranteed construction principle; Q-B2 DISPROVED as guaranteed construction; Q-B3 UNFINISHED; author recommends pausing the integer architecture. No non-author review.
