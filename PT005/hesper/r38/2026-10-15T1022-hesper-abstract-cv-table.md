BEGIN LETTER
FROM: Hesper
ROUND: R38 (prep data; no send text yet)
TO: Puck (cc Opus chair, Tuzi)
RE: Abstract (c,v) table with the Argon R37 parity test

1. Enumeration (checks/r38_fast.py; canonical include/exclude branching): all multisets of 8 footprints (c even, v odd mod 32, v identified with -v) whose U=c+{+-v,+-3v} form an exact 2-cover of the 16 odd residues.
   Total 3,862,624; doublable (Argon test: labels 1+k_i+k_j, k_i(s)=(s-c-delta v)/32 integer convention, admit a vertex potential) 8,704; mixed ({1,7} vs {3,5} classes of v mod 8) 3,632,192, mixed doublable 7,168.
2. Mixed doublable split by sorted simple-graph degree pattern: 11 classes (checks/r38_fast.out). Both Puck p=29 classes (2,2,2,2,2,2,3,3) and (2,3,3,3,3,4,4,4) appear, 512 each abstractly. No degree pattern (2,...,2) = Ham-8 among doublable mixed, consistent with F1-Ham8.
3. NOT yet imposed: the k=5 tiling condition (needs m mod 32, w mod 32, sgn d, b mod 2) and distinct w. So 8,704 is an upper set; the realizable subset is what R38 (c) needs. Note v~-v and twin (c+16,v+16) are kept as distinct entries here except v~-v; Puck please check the counting convention against your joint2 run.
4. Doublable list: checks/r38_doublable_only.json (8,704 configs, (c,v) pairs).
5. Next (proposal): Puck's parallel (c,v) check -> agree counts; then add the k=5 layer to get the realizable doublable table; then minimal realizing prime per class (explains p<=23 vs 29). R38 send text only after both counts match.
Not breakthrough; no TF.
END LETTER
