# F1' criterion check (Puck, own code)
Tilings: 8 legal odd w<16p, each covering exactly 2 level-5 members (as in the R29 census), members covered once, both-lift level-6 cover = exactly 2 everywhere (L1). b=1..(p-1)/2. p=17 gives 1660 (680 one-class / 980 mixed) as in the census. 'one class' = all w mod 8 in {1,7} or all in {3,5}.
Truth = brute force over 2^8 lifts at level 6 (exact cover once of C_6(2b)).
Astra: M=m mod 32, a=w mod 64, s in 0..31, label 1^q_i^q_j. GPT: h from ((s-c)*w) mod 64 with s,c in 0..31 and s-c taken as a RAW integer (variant 'raw'); variants (s-c) mod 32 and signed were also tested and DISAGREE (they differ by a vertex-dependent flip), so GPT's criterion is correct only with the raw reading.
Results: see out_small.txt (p=17,19,23), out_big_trimmed.txt (p=29,31), struct_out.txt (XOR-graph invariants). p=37 did not finish.
Scripts: f1check.py (python3 f1check.py 17 19 23), structure.py.
