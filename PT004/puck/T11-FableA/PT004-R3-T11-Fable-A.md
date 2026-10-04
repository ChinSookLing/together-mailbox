# PT004 · Round 3 · Turn 11 · Fable-A (testing seat) · item L3-C, prime p = 83

```
BEGIN PT004-R3-T11-FABLE-A
```

LEDGER_READ: v4

- When I started (machine clock 2026-10-03T13:23:55Z = 21:23:55 +08:00) the wall still showed ledger 3 as current (STATE_VERSION 547969df, AS_OF 21:19:03, sha256 `f766b604bc8d1dec94f6049de91a2a0061e636986ff1e350a17cba9f9de5e355`). I began with the paper and the archive, using only the ledger-v4 paragraph quoted in my task block.
- I fetched the wall again at 13:43:39Z (21:43:39 +08:00): 2,723 lines, LEDGER_VERSION 4, STATE_VERSION 003575e0, AS_OF 21:39:27, END line present, sha256 `710f0f5fbd0532ab692e4227499cf8df6deb28606d458a35cd93348b5473e744`. I read ledger v4 (wall line 21) in full. Nothing in it changes my item.
- Rules v0.5.1: read in T8 (sha256 `39ee09fa…21ee`), not fetched again.

## 1. GOAL

L3-C, prime gate p = 83 (k = 13).

## 2. ACTION

Code. A new program written from the paper's definitions, tested on tiny cases against a brute-force oracle, then run for p = 83 through all three stages, and compared with the p = 83 certificate data of the archive. All in my own container (2 CPU, 7.8 GiB RAM; gcc 13.3.0; Python 3.13.16).

## 3. RESULT

### 3.1 How far I got

**All three stages ran to the end, including the level-14 step.** The whole turn takes about 3 minutes of computing; no run came near the 30-minute cap.

| Stage | Result |
|---|---|
| (1) Tiny cases | 5 cases worked out by hand, and 89 cases (180 lift routes) against a brute-force oracle that follows Definition 2.1 word by word: all agree. |
| (2) Level one, p = 83, k = 13 | **115,903 unit orbits** in I(13,83,1). Two separate implementations of mine (C and Python, different search trees) give the same list, row for row. The archive's logged counts match: 41,552 irredundant rows and 2,042 twelve-class covers. |
| (3) Binary lifts 2, 4, 8, 16, 32 | Fibers become empty at level 2 for 25,263 orbits, level 4 for 88,911, level 8 for 1,715, level 16 for 10, level 32 for 2. **Two orbits are still alive at level 32: (1,…,13) and (1,…,11,13,24)**, the two named in the paper. All 298,483 survivor rows of the archive agree with my counts at every level. |
| (3) Level 14 | The 1 + 8 level-2 members of the two orbits: each has exactly **one** lift to level 14 without a witness (out of 7¹³), that lift has every coordinate divisible by 7, so it is proper by the gcd alternative. **0 improper lifts.** Same nine tuples and same nine completions as in the archive. |

So in my run every one of the 115,903 level-one orbits has an empty improper fiber at level 2, 4, 8, 16, 32 or 14. That is the computation the paper uses for "J(13,83) = ∅". §3.6 says what this does and does not cover.

### 3.2 Sources read this turn, and what I did not read

- **Paper:** arXiv:2609.02604**v2** (J. Allikvere, last revised 24 Sep 2026), TeX source from https://arxiv.org/e-print/2609.02604v2 (sha256 `572d5bdb010c393cb737445c9f299d32c727dc3c05205a5630e5cdc28708f799`), file `paper.tex`. I read §2 (Definition 2.1, the lifts and F_l(r), Lemma 2.2, Remark 2.3), §4 up to Proposition 4.4, and §5–§6.
- **Archive:** Zenodo record 22066772, https://doi.org/10.5281/zenodo.22066772 (CC BY 4.0).
  - `CODE_GUIDE.md` (md5 `8f503e7ad4ab80beb73d42a9899bcfa4`, as in the record): read in full, before writing my code.
  - `fourteen_lonely_runners_package.zip` (174,600,959 bytes, md5 `9b6564895671a1d5e03d4ff21e124f7c`, as in the record): I listed the file names, and extracted and read **only** `small_gates/p83/` and `small_gates/certificates_p83/` (163 entries: `.json`, `.txt`, `.log`, `.stats`, `.out` files and empty marker files).
- **Not read, not run, not copied:** every program in the archive (`.cpp`, `.py`, `.sh`, `.ps1`), the separate `basegen_v66_lf.cpp`, and `st_benchmark.zip`.
- One caution for the reader: `CODE_GUIDE.md` describes the author's programs in words (the two-branch search, the pruning rules, the orbit rule). I read it, as the seat block allows. My level-one search does not use the two-branch decomposition or the private-time quota; see §3.7.

### 3.3 Definitions used, quoted from the paper, and my normalisation

- "Let p be prime and l a positive integer, and write Z_{p,l} = Z_{pl} ∖ pZ_l. Thus a vector in Z_{p,l}^k has no coordinate divisible by p."
- Definition 2.1: "A vector **v** ∈ Z_{p,l}^k is *(k,p,l)-proper* if at least one of the following holds: (a) for some i, gcd(l, v_1, …, v̂_i, …, v_k) > 1; (b) for some t ∈ (lp)^(−1)Z, ‖t v_i‖ ≥ 1/(k+1) for every i. The set of vectors for which neither condition holds is I(k,p,l). A vector **v** ∈ Z_{p,1}^k is *eventually (k,p)-proper* if some level l has no improper lift of **v**. Here a lift to level l is a vector **w** ≡ **v** (mod p) with coordinates in Z_{pl}. The set of vectors that are not eventually proper is J(k,p)."
- §2: "the c-lifts of **v** ∈ Z_{p,l}^k to level cl are the c^k vectors w_i = v_i + a_i l p, a_i ∈ {0,…,c−1}" and "F_l(r) = {**w** ∈ I(k,p,l) : **w** ≡ r mod p}".
- §4: "After folding signs, both speed classes and nonzero time classes are represented by 1,…,(p−1)/2. … A speed class v covers a time class a when (k+1)·d_p(av) < p. … At level one the gcd alternative in the definition of properness is unavailable. Thus I(k,p,1) is exactly the family of k-multisets whose speed classes cover every folded time class."
- §4: "we use the binary lifts … to compute F_l(r) at levels 2, 4, 8, 16, and 32, stopping if the set becomes empty", and "Each improper level-2 member of the two orbits … has 7¹³ lifts to level 14."
- **My normalisation (stated as asked):** a level-one tuple is taken up to order and signs, so it is a 13-multiset of classes in 1…41. Units u of Z₈₃ act by v → fold(u·v). The representative of a unit orbit is the **lexicographically smallest sorted 13-tuple** in the orbit. The paper allows these three identifications: "permutations, sign changes of coordinates, and multiplication by a unit modulo p preserve eventual properness" (§2, citing Proposition 5.1 of the framework paper).
- For p = 83, k = 13: 41 speed classes, 41 time classes, each class covers exactly 5 time classes.

### 3.4 Stage 1: tiny cases

- **By hand** (bound 1/(k+1), all vectors with signs and order counted):
  1. k = 1, p = 5, level 1: no time j/5 reaches distance 1/2, so all 4 vectors are improper. Expected 4.
  2. k = 1, p = 5, level 2: an odd w has the witness t = 1/2; an even w is proper by (a), since gcd(2, nothing) = 2. Expected 0.
  3. k = 2, p = 5, level 1: class v covers time a when 3·d₅(av) < 5, that is d = 1. Class 1 covers time 1, class 2 covers time 2 (2·2 = 4 ≡ −1). The only cover is {1,2}: 2!·2² = 8 vectors. Expected 8.
  4. k = 2, p = 5, level 2: the lifts of (1,2) mod 10 are (1,2), (6,2), (6,7), each with at most one odd coordinate, so proper by (a), and (1,7), which has the witness t = 5/10 (both at distance 1/2). Expected 0.
  5. k = 2, p = 7, level 1: 3·d₇(av) < 7 means d ≤ 2. Class 1 covers times {1,2}, class 2 covers {1,3}, class 3 covers {2,3}. The covers are the three pairs of distinct classes: 3·2!·2² = 24 vectors. Expected 24.
  The literal oracle, the fast oracle and the C program all give 4, 0, 8, 0, 24.
- **Oracle:** `pt004_l3c_tests.py` looks at every vector of Z_{p,l}^k and every time j/(lp); it uses no folding, no orbits, no covers and no lifting. A literal transcription of Definition 2.1 is checked against the faster oracle on 8 cases.
- **C program against the oracle:** 89 cases with k = 1…6, p = 3…19, levels 1…12; 41 of them have a non-empty I(k,p,l). For every level L the C program is run along **every** ordered factorisation of L into lift factors (for example 12 = 2·2·3 = 3·4 = 12), 180 routes in all, and each must give the oracle's count. At level one the sets of unit orbits must be equal too. Inside the C program every lift is computed twice, with and without the counting bound, and the two must be identical.
- Result: all tests passed (full output in §3.10).

### 3.5 Stage 2: level one at p = 83, k = 13

- **My result:** I(13,83,1) has **115,903 unit orbits**, that is 4,752,023 = 41 × 115,903 covering 13-multisets. They split as:
  - 41,552 orbits on 13 distinct classes that are irredundant covers;
  - 49,847 orbits on 13 distinct classes that contain a 12-class cover;
  - 24,504 = 12 × 2,042 orbits on 12 distinct classes with one class doubled;
  - none on fewer than 12 distinct classes: the smallest cover has 12 classes (τ(83) = 12), and there are 2,042 unit orbits of 12-class covers.
- **Second implementation:** `pt004_l3c_level1_check.py` (Python, branching on the lowest uncovered time, its own canonical form) produces the same 115,903 rows, identical row for row. The same holds at p = 43 (163,507 rows).
- **List:** `level1_p83.txt`, 115,903 lines, sha256 `547441f23f205ff5d1f7f296e24d9ba47e934493396977fd653e68c08d9f2c75`. First and last lines:

```
1 1 2 3 4 5 7 8 9 10 11 12 13
1 1 2 3 4 5 7 8 9 10 11 13 24
1 1 2 3 4 5 7 8 9 10 12 13 22
…
1 4 6 15 19 23 27 31 33 35 36 39 40
1 5 6 8 9 11 14 17 19 29 30 31 35
```

- **Comparison with the archive.** The archive does not contain its raw level-one rows (only logs and hashes of them), so the lists can be compared only where the archive lists rows, which is after level 2. What can be compared at level one:

| Archive (p = 83 certificate) | Mine | Agree |
|---|---|---|
| irredundant raw rows: 41,552 (20 job logs; `SUMMARY.json`) | irredundant orbits on 13 distinct classes: 41,552 | yes |
| 12-class cover rows under root 0: 2,042 | unit orbits of 12-class covers: 2,042, and they are the same 2,042 sets | yes |
| rows of root 0: 83,722 | 2,042 × 41 one-class extensions = 83,722 | yes |
| total rows 378,777 = 41,552 + 41 × 8,225 ("prededup") | roots 1–4 only repeat 12-class rows of root 0 | consistent |
| `CODE_GUIDE.md`: "the p = 43 regression (… 163,507 rows …)" | my orbit count of I(13,43,1): 163,507 | yes |

  The archive's 378,777 rows contain the same orbits several times; my 115,903 has each orbit once. I did not try to reproduce the archive's per-job split of the irredundant rows (the 20 `ir_r_s` files); only their total.

### 3.6 Stage 3: lifts, and the comparison row by row

- **My result**, per orbit, |F_2|, |F_4|, … until the first empty level (`cascade_p83.txt`, sha256 `3feebd2ef7e4cc2a91c11b79afcf12a3236b6aedf253ee0c645855b825f699a3`):

| F becomes empty at level | orbits |
|---|---|
| 2 | 25,263 |
| 4 | 88,911 |
| 8 | 1,715 |
| 16 | 10 |
| 32 | 2 |
| still alive at 32 | 2 |
| total | 115,903 |

- The two orbits alive at level 32 are `1 2 3 4 5 6 7 8 9 10 11 12 13` with |F_2|,…,|F_32| = 1, 6, 4, 8, 16 and `1 2 3 4 5 6 7 8 9 10 11 13 24` with 8, 4, 4, 8, 16.
- **Level 14** (factor 7 from level 2). For each of the 9 level-2 members: exactly 1 lift without a witness, all 13 coordinates divisible by 7, 0 improper after the gcd test. For (1,…,13) the lift is 665 168 833 336 1001 504 7 672 175 840 343 1008 511. My search visited 9,877,400 nodes for that member (the archive log says 17,753,408; the searches are different, so the node counts need not agree).
- **Comparison with the archive, every row** (`compare_p83.out`, 33 checks, all OK):
  - 298,483 survivor rows read from the 25 `filt/*.out` files; each is a cover; each one's orbit is in my list.
  - For **every** row, the archive's l2, l4, l8, l16, l32 equal my |F_2| … |F_32|. 0 rows differ.
  - The set of orbits among the archive's survivors (90,640) is exactly my set of orbits with F_2 not empty (90,640).
  - Rows the archive does not list because they died at level 2, predicted from my data: irredundant branch 9,347 (archive: 41,552 − 32,205 = 9,347); root 0 of the 12-cover branch 83,722 rows with 66,379 survivors (archive: the same two numbers); roots 1–4 likewise.
  - The archive's totals died_l4 = 292,316, died_l8 = 6,120, died_l16 = 31, died_l32 = 6, persistent = 10 come out the same when I put my counts on its rows.
  - Level 14: same nine level-2 tuples, each with 1 witness-free completion and 0 improper, and the same completion digits as the archive's `kill_orbit1.txt` and `kill_orbit2.txt`.
  - A literal check in Python, without my lifting code: each of the nine completions has no witness among all 1,162 times and is proper by alternative (a); 2,700 other level-14 lifts drawn pseudo-randomly all have a witness.

- **What this covers and what it does not.**
  - It is one gate, p = 83, of the 61 (or 111). It says nothing about the other primes, Theorem 3.8, Lemma 2.2, or the framework results the paper cites (Lemma 2.4 and Proposition 5.1 of the framework paper), none of which I checked.
  - My statement that the level-one list is complete rests on my own search (argument in §3.7), on two implementations of mine agreeing, and on the counts above. The 25,263 orbits that die at level 2 could be compared with the archive only by counts, not by list.
  - Same model, two programs: my C and Python level-one programs were written by the same seat. Independence of ideas needs T12 and the read.

### 3.7 How my program works (for the reader and for L3-R)

- **Level one.** Every orbit has a member that contains class 1 (multiply by the inverse of any member). The program lists every covering set S of distinct classes with 1 ∈ S and |S| ≤ 13 exactly once: at an uncovered time, S must contain a class covering it; branch on the first such class of S in a fixed order and forbid the earlier ones; when the chosen classes cover everything, add any further non-forbidden classes. The only pruning is "the classes still allowed, 5 times each, cannot cover what is left". A set is kept if it is the smallest of its orbit; then every way of giving its classes multiplicities with total 13 is written out, each brought to the smallest sorted tuple, and duplicates are removed by sorting.
- **Lifts.** For a vector w at level l and a factor c, the times are j/(c·l·p) with 1 ≤ j ≤ c·l·p/2 (the sign symmetry) and c ∤ j. If c | j the time is a level-l time, the lift does not change j·w mod 1 there, and w has no witness there; the program checks this last fact for every vector it lifts and stops if it fails. Digits are assigned one coordinate at a time. A branch is cut when the remaining coordinates cannot block all remaining times; for the level-14 step the count bound of the paper's §4 (sum of the best gains) is used as well. Every completed witness-free tuple is tested against alternative (a).
- **Departures from the paper's procedure:** no two-branch decomposition, no private-time bound, no covering-number shortcut at level one; the binary levels and the level-14 step follow the paper.
- **Limit of this build:** n = (p−1)/2 ≤ 64, so p ≤ 127. The next prime of P13, p = 139, needs a wider bitset; I did not attempt it.

### 3.8 Files

All in `PT004-R3-T11-Fable-A-files.zip` (sha256 `198664d91e2b22b4accc3185f46a5d75921b24f438300daffe035a8376ade22f`). The five program files are also sent separately.

| File | lines | bytes | sha256 |
|---|---|---|---|
| `pt004_l3c.c` | 600 | 24,989 | `1e504e26dee68d94a7144c40f6e965089805a1b18ebe1c232751f416120fcc5e` |
| `pt004_l3c_tests.py` | 193 | 7,518 | `6d59a9e68d88e412d702e46b6e2a408ff79a1d28b8bac642de0c95169880eba5` |
| `pt004_l3c_level1_check.py` | 134 | 5,143 | `085552c65353174b7c1a649e42a27c7ced9060fe2119beee54d3683756785ab1` |
| `pt004_l3c_compare.py` | 325 | 15,840 | `cd54de0e05b236ec48ebd56165e53a25bf1496a0b000dcc82736962324cb928e` |
| `pt004_l3c_run.sh` | 28 | 1,736 | `df09d8e7084a9b26e56db35161b58abda66724c1e9d92e7e58f7ed2a77d237c9` |
| `stage1_tests.out` | 107 | 5,839 | `66a98187f4b5753ef9c40a4d7ea5a3889c2e8680458dcdedc3aadfed0e06d0e2` |
| `level1_p43.log` | 14 | 976 | `882097308a2a6dba634b57f1a534829012c42d2fc934ab0b3a4c1ae01dbde8c8` |
| `level1_p43.txt` | 163,507 | 5,239,373 | `0ab17b072958bfec6102783c86c040e08a8074509ea21345fcac6564dcdbb319` |
| `level1_p83.log` | 11 | 751 | `c75673d66cf9dc10ee1db12d042f111b88e7439d847d48d54b91b123e7a657d0` |
| `level1_p83.txt` | 115,903 | 4,011,397 | `547441f23f205ff5d1f7f296e24d9ba47e934493396977fd653e68c08d9f2c75` |
| `level1_check_p43.out` | 10 | 338 | `9df20e7398b473d44d846e57f44fb332cefea113742aaaefc12539f182d6a810` |
| `level1_check_p83.out` | 7 | 296 | `2569628607fd3cb722684116c08ad2bffbcd1df528d26daee227e1873e028ca9` |
| `cascade_p83.log` | 33 | 3,084 | `da123c12f40b3daf147b01ea62c61056f3fae1136d60a7955148c9bc16266b2e` |
| `cascade_p83.txt` | 115,903 | 5,300,826 | `3feebd2ef7e4cc2a91c11b79afcf12a3236b6aedf253ee0c645855b825f699a3` |
| `compare_p83.out` | 48 | 3,834 | `434bfbc9f048edafce7f104306871618a95320a8a0c74ec8246f25e31a6ee8ff` |

- `zenodo22066772_p83_data.tar.gz` (sha256 `60b5251951fea3fd0fca8e37e3d7f7c692eafc6a6a4acb9c79c6d5e3c1db3ce6`): the unmodified p = 83 subset of the archive that the comparison reads (164 entries with a notice file; Zenodo 22066772, J. Allikvere, CC BY 4.0). It can be recreated from the official zip with the `unzip` command in its `NOTICE_SUBSET.txt`.
- The compiled binary is not sent; it is built from `pt004_l3c.c`.

### 3.9 Commands, exit codes, run times

One command runs everything, in a folder holding the five program files:

```
tar -xzf zenodo22066772_p83_data.tar.gz          # creates ./small_gates
sh pt004_l3c_run.sh small_gates > run.out 2>&1
```

- **Exit code: 0. Run time: 174.5 s** (final run, started 2026-10-03T13:53:28Z). The script prints the sha256 of the ten outputs; they are the hashes in §3.8.
- The same steps run one by one, with their times (from the first full run, total 179.1 s, every exit code 0; the C program and the other scripts already had their final bytes, and the comparison script was changed afterwards as described in §3.11, with identical output):

| Step | Command | Time |
|---|---|---|
| build | `cc -O2 -std=c11 -o pt004_l3c pt004_l3c.c` | 0.4 s |
| stage 1 | `python3 pt004_l3c_tests.py > stage1_tests.out` | 68.1 s |
| level one, p = 43 (extra) | `./pt004_l3c level1 43 13 level1_p43.txt > level1_p43.log` | 0.7 s |
| stage 2 | `./pt004_l3c level1 83 13 level1_p83.txt > level1_p83.log` | 1.0 s |
| second implementation, p = 43 | `python3 pt004_l3c_level1_check.py 43 13 level1_p43.txt > level1_check_p43.out` | 3.6 s |
| second implementation, p = 83 | `python3 pt004_l3c_level1_check.py 83 13 level1_p83.txt > level1_check_p83.out` | 31.3 s |
| stage 3 | `./pt004_l3c cascade 83 13 level1_p83.txt cascade_p83.txt > cascade_p83.log` | 45.6 s |
| comparison | `python3 pt004_l3c_compare.py level1_p83.txt cascade_p83.txt cascade_p83.log small_gates > compare_p83.out` | 28.2 s |

- The outputs contain no time and no version number. Three full runs gave byte-identical outputs.

### 3.10 Outputs in full

`run.out`:

```
== build
== stage 1: tiny cases
== level one, p = 43 (extra)
== stage 2: level one, p = 83
== second implementation, p = 43
== second implementation, p = 83
== stage 3: lifts 2..32 and 14
== comparison with the archive
== sha256 of the outputs
66a98187f4b5753ef9c40a4d7ea5a3889c2e8680458dcdedc3aadfed0e06d0e2  stage1_tests.out
882097308a2a6dba634b57f1a534829012c42d2fc934ab0b3a4c1ae01dbde8c8  level1_p43.log
0ab17b072958bfec6102783c86c040e08a8074509ea21345fcac6564dcdbb319  level1_p43.txt
c75673d66cf9dc10ee1db12d042f111b88e7439d847d48d54b91b123e7a657d0  level1_p83.log
547441f23f205ff5d1f7f296e24d9ba47e934493396977fd653e68c08d9f2c75  level1_p83.txt
9df20e7398b473d44d846e57f44fb332cefea113742aaaefc12539f182d6a810  level1_check_p43.out
2569628607fd3cb722684116c08ad2bffbcd1df528d26daee227e1873e028ca9  level1_check_p83.out
da123c12f40b3daf147b01ea62c61056f3fae1136d60a7955148c9bc16266b2e  cascade_p83.log
3feebd2ef7e4cc2a91c11b79afcf12a3236b6aedf253ee0c645855b825f699a3  cascade_p83.txt
434bfbc9f048edafce7f104306871618a95320a8a0c74ec8246f25e31a6ee8ff  compare_p83.out
== all steps finished
```

`level1_p83.log`:

```
LEVEL ONE  p=83 k=13  n=41 classes  each class covers m=5 times
  search nodes: 4639848
  covering sets with at most 13 distinct classes that contain class 1: 1212691
    size 12:      24504 sets containing class 1,      2042 unit orbits of sets
    size 13:    1188187 sets containing class 1,     91399 unit orbits of sets
  smallest number of classes in a cover (tau): 12
  unit orbits of covering 13-multisets = orbits of I(13,83,1): 115903
  covering 13-multisets (all, not up to units): 4752023
  |I(13,83,1)| as ordered vectors with signs: 216784193540692377600
  among the sets that contain class 1: irredundant covers on 13 distinct classes: 540176; covers on 12 distinct classes: 24504
  wrote 115903 orbit representatives to level1_p83.txt
```

`level1_check_p83.out`:

```
p=83 k=13: covering sets with at most 13 classes that contain class 1: 1212691
  size 12: 24504
  size 13: 1188187
  unit orbits of covering sets: 93441
  unit orbits of covering 13-multisets (this script): 115903
  rows in level1_p83.txt: 115903
RESULT: the two lists are identical, row for row
```

`cascade_p83.log`:

```
  orbit 1 2 3 4 5 6 7 8 9 10 11 12 13: alive at level 32; level-14 step over 1 level-2 members
    level-2 member 1 2 3 4 5 6 7 8 9 10 11 12 13: nodes=9877400 witness-free completions=1 improper after gcd=0
      witness-free completion, digits a_i (w_i + a_i*2p): 4 1 5 2 6 3 0 4 1 5 2 6 3  -> tuple: 665 168 833 336 1001 504 7 672 175 840 343 1008 511
  orbit 1 2 3 4 5 6 7 8 9 10 11 13 24: alive at level 32; level-14 step over 8 level-2 members
    level-2 member 1 2 3 4 5 6 7 8 9 10 11 13 24: nodes=7760054 witness-free completions=1 improper after gcd=0
      witness-free completion, digits a_i (w_i + a_i*2p): 4 1 5 2 6 3 0 4 1 5 2 3 5  -> tuple: 665 168 833 336 1001 504 7 672 175 840 343 511 854
    level-2 member 1 2 3 4 5 6 7 91 9 10 11 13 24: nodes=6842102 witness-free completions=1 improper after gcd=0
      witness-free completion, digits a_i (w_i + a_i*2p): 4 1 5 2 6 3 0 0 1 5 2 3 5  -> tuple: 665 168 833 336 1001 504 7 91 175 840 343 511 854
    level-2 member 1 2 86 4 5 89 7 8 9 93 94 13 107: nodes=6330878 witness-free completions=1 improper after gcd=0
      witness-free completion, digits a_i (w_i + a_i*2p): 4 1 1 2 6 6 0 4 1 1 5 3 1  -> tuple: 665 168 252 336 1001 1085 7 672 175 259 924 511 273
    level-2 member 1 2 86 87 5 89 7 8 9 93 94 13 107: nodes=6169724 witness-free completions=1 improper after gcd=0
      witness-free completion, digits a_i (w_i + a_i*2p): 4 1 1 5 6 6 0 4 1 1 5 3 1  -> tuple: 665 168 252 917 1001 1085 7 672 175 259 924 511 273
    level-2 member 1 2 86 87 5 89 7 91 9 93 11 13 107: nodes=1546238 witness-free completions=1 improper after gcd=0
      witness-free completion, digits a_i (w_i + a_i*2p): 4 1 1 5 6 6 0 0 1 1 2 3 1  -> tuple: 665 168 252 917 1001 1085 7 91 175 259 343 511 273
    level-2 member 1 2 86 87 5 89 7 91 9 93 94 13 107: nodes=5622716 witness-free completions=1 improper after gcd=0
      witness-free completion, digits a_i (w_i + a_i*2p): 4 1 1 5 6 6 0 0 1 1 5 3 1  -> tuple: 665 168 252 917 1001 1085 7 91 175 259 924 511 273
    level-2 member 84 2 3 4 5 6 7 91 9 10 11 13 24: nodes=6695438 witness-free completions=1 improper after gcd=0
      witness-free completion, digits a_i (w_i + a_i*2p): 0 1 5 2 6 3 0 0 1 5 2 3 5  -> tuple: 84 168 833 336 1001 504 7 91 175 840 343 511 854
    level-2 member 84 2 86 87 5 89 7 91 9 93 94 13 107: nodes=5612258 witness-free completions=1 improper after gcd=0
      witness-free completion, digits a_i (w_i + a_i*2p): 0 1 1 5 6 6 0 0 1 1 5 3 1  -> tuple: 84 168 252 917 1001 1085 7 91 175 259 924 511 273
CASCADE  p=83 k=13
  level-one orbits read: 115903
  F becomes empty at level  2: 25263 orbits
  F becomes empty at level  4: 88911 orbits
  F becomes empty at level  8: 1715 orbits
  F becomes empty at level 16: 10 orbits
  F becomes empty at level 32: 2 orbits
  still alive at level 32: 2 orbits
  of these, empty at level 14: 2; NOT empty at level 14: 0
  lift search nodes in total: 184925028
  orbits shown eventually proper: 115903 of 115903
  RESULT: every level-one orbit has an empty improper fiber at some level
  wrote cascade_p83.txt
```

`compare_p83.out`:

```
A. My level-one list, re-examined in Python
  [OK] 115903 rows, sorted, no row twice
  [OK] every row is a cover of the 41 time classes (so it lies in I(13,83,1))
  [OK] every row is the smallest sorted tuple of its unit orbit (all 41 units tried)
     13 distinct classes, irredundant: 41552
     13 distinct classes, containing a 12-class cover: 49847
     12 distinct classes with one class doubled: 24504
     fewer than 12 distinct classes: 0
     unit orbits of 12-class covers behind them: 2042
  [OK] the cascade file has the same orbits as the level-one file
     my orbits with F_2 not empty: 90640; with F_2 empty: 25263
B. The archive's logged level-one counts against mine
  [OK] archive irredundant rows: logs sum to 41552, SUMMARY says 41552; my irredundant orbits: 41552
  [OK] archive 12-class cover rows under root 0: 2042; my orbits of 12-class covers: 2042
  [OK] archive 12-cover rows over the 5 roots: 8225 (SUMMARY: 8225, 'prededup')
  [OK] archive total rows 378777 = 41552 + 41 x 8225
C. Every survivor row of the archive against my cascade (row by row)
  [OK] archive survivor rows read: 298483 (SUMMARY: 298483); each file has as many rows as its .stats says
  [OK] every archive row is a cover -- 0 are not
  [OK] every archive row's orbit is in my level-one list -- 0 missing
  [OK] for every archive row, l2, l4, l8, l16, l32 are equal to my |F_2| .. |F_32| -- 0 rows differ
  [OK] the archive's PERSISTENT mark and my 'alive at level 32' agree on every row
  [OK] set of orbits among the archive's survivors (90640) = my orbits with F_2 not empty (90640) -- only archive 0, only mine 0
D. Rows the archive does not list (they died at level 2), predicted from my data
  [OK] irredundant branch: archive survivors 32205, all different orbits, all irredundant; my irredundant orbits with F_2 not empty: 32205
  [OK] irredundant branch: archive rows that died at level 2: 9347; mine: 9347
  [OK] the 12-class rows behind root 0 of the archive are exactly my 2042 orbits of 12-class covers
  [OK] c12 root 0: archive rows 83722, survivors 66379; from my own 12-class covers x 41 extensions: rows 83722, survivors 66379
  [OK] c12 root 1: archive rows 77408, survivors 61608; from the 12-class rows seen in the archive file x 41 extensions: rows 77408, survivors 61608
  [OK] c12 root 2: archive rows 70643, survivors 55827; from the 12-class rows seen in the archive file x 41 extensions: rows 70643, survivors 55827
  [OK] c12 root 3: archive rows 64862, survivors 50960; from the 12-class rows seen in the archive file x 41 extensions: rows 64862, survivors 50960
  [OK] c12 root 4: archive rows 40590, survivors 31504; from the 12-class rows seen in the archive file x 41 extensions: rows 40590, survivors 31504
  [OK] roots 1-4 only repeat 12-class rows of root 0
E. The archive's cascade totals, recomputed with MY counts on the archive's rows
  [OK] died_l4: archive 292316, mine 292316
  [OK] died_l8: archive 6120, mine 6120
  [OK] died_l16: archive 31, mine 31
  [OK] died_l32: archive 6, mine 6
  [OK] persistent: archive 10, mine 10
     (my own orbit counts, no row twice: empty at level 2: 25263, 4: 88911, 8: 1715, 16: 10, 32: 2, alive at 32: 2)
  [OK] orbits alive at level 32 are the two named in the paper and the archive
F. The level-14 step
  [OK] level-2 members lifted to level 14: archive 9, mine 9, same tuples
  [OK] for each one: exactly 1 witness-free completion, 0 improper after the gcd test, and the same completion (same digits) as in the archive
G. Level 14 checked literally in Python on the definition (no lifting code)
  [OK] each witness-free completion has no witness among all 1162 times, has every coordinate divisible by 7, and is proper by alternative (a)
  [OK] 2700 other level-14 lifts drawn pseudo-randomly: every one has a witness
RESULT: every comparison agrees
```

`level1_p43.log` and `level1_check_p43.out`:

```
LEVEL ONE  p=43 k=13  n=21 classes  each class covers m=3 times
  search nodes: 4612
  covering sets with at most 13 distinct classes that contain class 1: 86062
    size  9:        132 sets containing class 1,        16 unit orbits of sets
    size 10:       2380 sets containing class 1,       238 unit orbits of sets
    size 11:      11913 sets containing class 1,      1083 unit orbits of sets
    size 12:      29140 sets containing class 1,      2431 unit orbits of sets
    size 13:      42497 sets containing class 1,      3269 unit orbits of sets
  smallest number of classes in a cover (tau): 9
  unit orbits of covering 13-multisets = orbits of I(13,43,1): 163507
  covering 13-multisets (all, not up to units): 3433647
  |I(13,43,1)| as ordered vectors with signs: 43361054829639106560
  among the sets that contain class 1: irredundant covers on 13 distinct classes: 0; covers on 12 distinct classes: 29140
  wrote 163507 orbit representatives to level1_p43.txt
```

```
p=43 k=13: covering sets with at most 13 classes that contain class 1: 86062
  size 9: 132
  size 10: 2380
  size 11: 11913
  size 12: 29140
  size 13: 42497
  unit orbits of covering sets: 7037
  unit orbits of covering 13-multisets (this script): 163507
  rows in level1_p43.txt: 163507
RESULT: the two lists are identical, row for row
```

`cascade_p83.txt`, first and last lines (115,903 lines in all):

```
1 1 2 3 4 5 7 8 9 10 11 12 13 : l2=18 l4=0
1 1 2 3 4 5 7 8 9 10 11 13 24 : l2=18 l4=0
1 1 2 3 4 5 7 8 9 10 12 13 22 : l2=18 l4=0
…
1 4 6 15 19 23 27 31 33 35 36 39 40 : l2=13 l4=0
1 5 6 8 9 11 14 17 19 29 30 31 35 : l2=12 l4=0
```

<details>
<summary>stage1_tests.out (107 lines)</summary>

```
STAGE 1a: cases worked out by hand (see the report), oracle and C program
  k=1 p=5 l=1: by hand 4, literal oracle 4, oracle 4, C 4  OK   (k=1: no time j/p reaches 1/2, so all 4 vectors are improper)
  k=1 p=5 l=2: by hand 0, literal oracle 0, oracle 0, C 0  OK   (k=1, level 2: w odd has the witness t=1/2; w even: gcd(2, nothing)=2)
  k=2 p=5 l=1: by hand 8, literal oracle 8, oracle 8, C 8  OK   (classes {1,2}: 1 covers time 1, 2 covers time 2; only {1,2} covers; 1*2!*2^2)
  k=2 p=5 l=2: by hand 0, literal oracle 0, oracle 0, C 0  OK   (lifts of (1,2): (1,2),(6,2),(6,7) by gcd; (1,7) has witness t=1/2)
  k=2 p=7 l=1: by hand 24, literal oracle 24, oracle 24, C 24  OK   (covers are {1,2},{1,3},{2,3}: 3*2!*2^2)
STAGE 1b: the fast oracle against the literal oracle (definition word by word)
  k=2 p=5 l=4: literal 0, fast 0  OK
  k=2 p=7 l=2: literal 0, fast 0  OK
  k=2 p=7 l=3: literal 0, fast 0  OK
  k=2 p=11 l=2: literal 0, fast 0  OK
  k=3 p=7 l=2: literal 144, fast 144  OK
  k=3 p=11 l=1: literal 240, fast 240  OK
  k=3 p=13 l=2: literal 576, fast 576  OK
  k=4 p=11 l=1: literal 4800, fast 4800  OK
STAGE 1c: C program against the oracle, every level and every lift route
  k=1 p= 3 L= 1: |I| =        2  routes  1  level-one orbits 1  OK
  k=1 p= 3 L= 2: |I| =        0  routes  1  OK
  k=1 p= 3 L= 3: |I| =        0  routes  1  OK
  k=1 p= 3 L= 4: |I| =        0  routes  2  OK
  k=1 p= 3 L= 6: |I| =        0  routes  3  OK
  k=1 p= 5 L= 1: |I| =        4  routes  1  level-one orbits 1  OK
  k=1 p= 5 L= 2: |I| =        0  routes  1  OK
  k=1 p= 5 L= 3: |I| =        0  routes  1  OK
  k=1 p= 5 L= 4: |I| =        0  routes  2  OK
  k=1 p= 5 L= 6: |I| =        0  routes  3  OK
  k=1 p= 7 L= 1: |I| =        6  routes  1  level-one orbits 1  OK
  k=1 p= 7 L= 2: |I| =        0  routes  1  OK
  k=1 p= 7 L= 3: |I| =        0  routes  1  OK
  k=1 p= 7 L= 4: |I| =        0  routes  2  OK
  k=1 p= 7 L= 6: |I| =        0  routes  3  OK
  k=2 p= 5 L= 1: |I| =        8  routes  1  level-one orbits 1  OK
  k=2 p= 5 L= 2: |I| =        0  routes  1  OK
  k=2 p= 5 L= 3: |I| =        0  routes  1  OK
  k=2 p= 5 L= 4: |I| =        0  routes  2  OK
  k=2 p= 5 L= 6: |I| =        0  routes  3  OK
  k=2 p= 5 L= 8: |I| =        0  routes  4  OK
  k=2 p= 5 L= 9: |I| =        0  routes  2  OK
  k=2 p= 5 L=12: |I| =        0  routes  8  OK
  k=2 p= 7 L= 1: |I| =       24  routes  1  level-one orbits 1  OK
  k=2 p= 7 L= 2: |I| =        0  routes  1  OK
  k=2 p= 7 L= 3: |I| =        0  routes  1  OK
  k=2 p= 7 L= 4: |I| =        0  routes  2  OK
  k=2 p= 7 L= 6: |I| =        0  routes  3  OK
  k=2 p= 7 L= 8: |I| =        0  routes  4  OK
  k=2 p= 7 L= 9: |I| =        0  routes  2  OK
  k=2 p= 7 L=12: |I| =        0  routes  8  OK
  k=2 p=11 L= 1: |I| =       40  routes  1  level-one orbits 1  OK
  k=2 p=11 L= 2: |I| =        0  routes  1  OK
  k=2 p=11 L= 3: |I| =        0  routes  1  OK
  k=2 p=11 L= 4: |I| =        0  routes  2  OK
  k=2 p=11 L= 6: |I| =        0  routes  3  OK
  k=2 p=11 L= 8: |I| =        0  routes  4  OK
  k=2 p=11 L= 9: |I| =        0  routes  2  OK
  k=2 p=11 L=12: |I| =        0  routes  8  OK
  k=2 p=13 L= 1: |I| =       72  routes  1  level-one orbits 2  OK
  k=2 p=13 L= 2: |I| =        0  routes  1  OK
  k=2 p=13 L= 3: |I| =        0  routes  1  OK
  k=2 p=13 L= 4: |I| =        0  routes  2  OK
  k=2 p=13 L= 6: |I| =        0  routes  3  OK
  k=2 p=13 L= 8: |I| =        0  routes  4  OK
  k=2 p=13 L= 9: |I| =        0  routes  2  OK
  k=2 p=13 L=12: |I| =        0  routes  8  OK
  k=3 p= 7 L= 1: |I| =       48  routes  1  level-one orbits 1  OK
  k=3 p= 7 L= 2: |I| =      144  routes  1  OK
  k=3 p= 7 L= 3: |I| =      288  routes  1  OK
  k=3 p= 7 L= 4: |I| =        0  routes  2  OK
  k=3 p= 7 L= 6: |I| =      288  routes  3  OK
  k=3 p= 7 L= 8: |I| =        0  routes  4  OK
  k=3 p=11 L= 1: |I| =      240  routes  1  level-one orbits 1  OK
  k=3 p=11 L= 2: |I| =      480  routes  1  OK
  k=3 p=11 L= 3: |I| =      960  routes  1  OK
  k=3 p=11 L= 4: |I| =        0  routes  2  OK
  k=3 p=11 L= 6: |I| =      480  routes  3  OK
  k=3 p=11 L= 8: |I| =        0  routes  4  OK
  k=3 p=13 L= 1: |I| =      672  routes  1  level-one orbits 3  OK
  k=3 p=13 L= 2: |I| =      576  routes  1  OK
  k=3 p=13 L= 3: |I| =      576  routes  1  OK
  k=3 p=13 L= 4: |I| =        0  routes  2  OK
  k=3 p=13 L= 6: |I| =      576  routes  3  OK
  k=3 p=13 L= 8: |I| =        0  routes  4  OK
  k=3 p=17 L= 1: |I| =     1152  routes  1  level-one orbits 3  OK
  k=3 p=17 L= 2: |I| =      768  routes  1  OK
  k=3 p=17 L= 3: |I| =      768  routes  1  OK
  k=3 p=17 L= 4: |I| =        0  routes  2  OK
  k=3 p=17 L= 6: |I| =      768  routes  3  OK
  k=3 p=17 L= 8: |I| =        0  routes  4  OK
  k=4 p=11 L= 1: |I| =     4800  routes  1  level-one orbits 4  OK
  k=4 p=11 L= 2: |I| =    17280  routes  1  OK
  k=4 p=11 L= 3: |I| =    32640  routes  1  OK
  k=4 p=11 L= 4: |I| =    26880  routes  2  OK
  k=4 p=13 L= 1: |I| =     4608  routes  1  level-one orbits 3  OK
  k=4 p=13 L= 2: |I| =    19584  routes  1  OK
  k=4 p=13 L= 3: |I| =    18432  routes  1  OK
  k=4 p=13 L= 4: |I| =    18432  routes  2  OK
  k=4 p=17 L= 1: |I| =    11520  routes  1  level-one orbits 5  OK
  k=4 p=17 L= 2: |I| =    16896  routes  1  OK
  k=4 p=19 L= 1: |I| =     6912  routes  1  level-one orbits 2  OK
  k=4 p=19 L= 2: |I| =    13824  routes  1  OK
  k=5 p=11 L= 1: |I| =     3840  routes  1  level-one orbits 1  OK
  k=5 p=11 L= 2: |I| =    38400  routes  1  OK
  k=5 p=13 L= 1: |I| =   101760  routes  1  level-one orbits 9  OK
  k=5 p=13 L= 2: |I| =   829440  routes  1  OK
  k=5 p=17 L= 1: |I| =    92160  routes  1  level-one orbits 4  OK
  k=6 p=17 L= 1: |I| =  3164160  routes  1  level-one orbits 19  OK
  cases: 89, of which with |I| > 0: 41; lift routes run: 180
RESULT: all tests passed
```

</details>

### 3.11 History, nothing hidden

- No run failed and no comparison disagreed, apart from the inputs I altered on purpose (last item).
- **One wrong reading on the way.** My first attempt to reproduce the archive's "41,552 irredundant rows" counted the irredundant 13-class covers that contain class 1 and give class 1 at least q₁₃ = 2 private times. That gives 331,204, which is not the archive's number. The archive's rows are one per unit orbit: 540,176 irredundant covers containing class 1, divided by 13, is 41,552. I removed the unused quota counters from the program afterwards; the level-one list did not change (checked byte for byte).
- Program changes after the first full pipeline run: printing of the witness-free level-14 completions (added), the quota counters (removed), and the comparison script made to stop cleanly when an orbit is missing instead of raising an error. The cascade and level-one outputs were identical before and after.
- Full runs: three (179.1 s, 174.1 s, 174.5 s), byte-identical outputs. The third, on the final bytes of all five files, is the one reported.
- One-off check that the comparison can fail: I altered copies of my files in four ways (one |F_4| changed; one orbit declared dead at level 2; one orbit removed from both files; one orbit removed from the list only). Each time the comparison ended with exit code 1 and named the difference.

### 3.12 The programs in full

<details>
<summary>pt004_l3c.c</summary>

```c
/*
 * TOGETHER - PROOF TABLE 004 - Round 3 - Turn 11 - item L3-C (prime gate p = 83)
 * Seat: Fable-A (testing seat).
 *
 * NEW code, written from the definitions in arXiv:2609.02604v2 (Allikvere),
 * Section 2 (Definition 2.1, c-lifts, the sets F_l(r)) and Section 4 (the cover
 * formulation of level one, binary lifting, the level-14 step).
 * The author's code was not read, run or copied.
 *
 * Definitions used (k speeds, prime p, level l; all arithmetic is exact integer):
 *
 *   Z_{p,l}  = residues mod p*l that are not divisible by p.
 *   A vector v in Z_{p,l}^k is (k,p,l)-PROPER if
 *     (a) for some i, gcd(l, v_1, .., v_i omitted, .., v_k) > 1, or
 *     (b) for some t = j/(l*p), j an integer, ||t*v_i|| >= 1/(k+1) for every i.
 *   It is IMPROPER otherwise; I(k,p,l) is the set of improper vectors.
 *   With d(x) = distance from x to the nearest multiple of l*p,
 *     ||j*v_i/(l*p)|| >= 1/(k+1)   <=>   (k+1) * d(j*v_i) >= l*p.
 *   Coordinate i "blocks" the time j when (k+1) * d(j*v_i) < l*p.
 *   So (b) fails exactly when every time j is blocked by some coordinate.
 *
 *   Level one.  Signs are folded: speed classes and time classes are 1..n, n=(p-1)/2.
 *   Class v covers time a when (k+1)*d_p(a*v) < p.  I(k,p,1) = the k-multisets of
 *   classes whose cover sets together contain every time class (gcd(1,..) = 1, so
 *   alternative (a) never applies at level one).
 *   Units u of Z_p act by v -> fold(u*v); a "unit orbit" is an orbit of this action
 *   on k-multisets.  MY NORMALISATION: the representative of an orbit is the
 *   lexicographically smallest sorted k-tuple of classes in the orbit.
 *
 *   Lifts.  For c >= 2 the c-lifts of w (level l) are w_i + a_i*l*p, a_i in 0..c-1,
 *   taken mod c*l*p.  F_l(r) = improper level-l vectors congruent to r mod p.
 *   F_{c*l}(r) = the improper c-lifts of the members of F_l(r).
 *
 * Modes:
 *   level1  P K OUT          enumerate all unit orbits of I(K,P,1), write them to OUT
 *   cascade P K ORBITS OUT   for every orbit: |F_2|,|F_4|,..,|F_32|; for an orbit that
 *                            is still alive at level 32, the level-(K+1) step from F_2
 *   tiny    P K c1,c2,..     totals of improper ordered vectors along a lift route
 *                            (used by the test driver against a brute-force oracle)
 *
 * Build:  cc -O2 -std=c11 -o pt004_l3c pt004_l3c.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef uint64_t u64;
typedef unsigned __int128 u128;

#define MAXK 16
#define MAXN 64
#define MAXC 16
#define MAXT 4096
#define MAXW (MAXT / 64)

static int P, K, N, M;
static u64 FULL1;                      /* all time classes (also: all speed classes) */
static u64 cover1[MAXN + 1];           /* cover1[v]: bit a-1 set if class v covers time a */
static u64 covby[MAXN + 1];            /* covby[a]:  bit v-1 set if class v covers time a */
static unsigned char mulf[MAXN + 1][MAXN + 1];   /* mulf[u][x] = fold(u*x) */
static unsigned char invf[MAXN + 1];             /* fold-inverse of a class */

static void die(const char *msg) { fprintf(stderr, "ERROR: %s\n", msg); exit(2); }
static inline int popc(u64 x) { return __builtin_popcountll(x); }
static inline int lowbit(u64 x) { return __builtin_ctzll(x); }

static int fold(long x)
{
    long r = x % P;
    if (r < 0) r += P;
    return (int)(r <= P - r ? r : P - r);
}

static void print_u128(u128 x)
{
    char buf[48]; int i = 47; buf[i] = 0;
    if (x == 0) buf[--i] = '0';
    while (x > 0) { buf[--i] = (char)('0' + (int)(x % 10)); x /= 10; }
    fputs(buf + i, stdout);
}

static void setup(int p, int k)
{
    if (p < 3 || p % 2 == 0) die("p must be an odd prime");
    for (int q = 3; q * q <= p; q += 2) if (p % q == 0) die("p must be prime");
    P = p; K = k; N = (p - 1) / 2;
    if (N > MAXN) die("p too large for this build (n = (p-1)/2 must be <= 64)");
    if (K < 1 || K > MAXK) die("k out of range");
    FULL1 = (N == 64) ? ~(u64)0 : (((u64)1 << N) - 1);
    memset(cover1, 0, sizeof cover1); memset(covby, 0, sizeof covby);
    for (int v = 1; v <= N; v++)
        for (int a = 1; a <= N; a++)
            if ((long)(K + 1) * fold((long)a * v) < P) {
                cover1[v] |= (u64)1 << (a - 1);
                covby[a] |= (u64)1 << (v - 1);
            }
    M = popc(cover1[1]);
    for (int u = 1; u <= N; u++)
        for (int x = 1; x <= N; x++) {
            mulf[u][x] = (unsigned char)fold((long)u * x);
            if (mulf[u][x] == 1) invf[u] = (unsigned char)x;
        }
}

/* ------------------------------------------------------------------------- */
/* Level one: all unit orbits of covering K-multisets                         */
/* ------------------------------------------------------------------------- */

typedef struct { unsigned char c[MAXK]; } Row;

static Row *rows = NULL; static size_t nrows = 0, caprows = 0;
static long long nodes1 = 0, sets_with1 = 0;
static long long sets_by_size[MAXK + 1], canon_by_size[MAXK + 1];
/* two extra counters, reported only (sets that contain class 1) */
static long long irr_K_with1 = 0;      /* irredundant covers on K distinct classes */
static long long cov_K1_with1 = 0;     /* covers on K-1 distinct classes */

static void push_row(const unsigned char *c)
{
    if (nrows == caprows) {
        caprows = caprows ? caprows * 2 : 1 << 16;
        rows = realloc(rows, caprows * sizeof(Row));
        if (!rows) die("out of memory");
    }
    memset(rows[nrows].c, 0, MAXK);
    memcpy(rows[nrows].c, c, (size_t)K);
    nrows++;
}

static void sort_small(unsigned char *t, int len)
{
    for (int i = 1; i < len; i++) {
        unsigned char x = t[i]; int j = i - 1;
        while (j >= 0 && t[j] > x) { t[j + 1] = t[j]; j--; }
        t[j + 1] = x;
    }
}

/* lexicographically smallest sorted tuple in the unit orbit of the multiset m.
   The minimum starts with class 1, so only the units inverse to a member matter. */
static void canon_multiset(const unsigned char *m, unsigned char *best)
{
    unsigned char t[MAXK];
    memcpy(best, m, (size_t)K);
    sort_small(best, K);
    for (int i = 0; i < K; i++) {
        if (i > 0 && m[i] == m[i - 1]) continue;
        int u = invf[m[i]];
        for (int j = 0; j < K; j++) t[j] = mulf[u][m[j]];
        sort_small(t, K);
        if (memcmp(t, best, (size_t)K) < 0) memcpy(best, t, (size_t)K);
    }
}

/* number of units u with u*m = m (as multisets); the orbit has N / this many members */
static int stabilizer_size(const unsigned char *m)
{
    unsigned char t[MAXK]; int s = 0;
    for (int u = 1; u <= N; u++) {
        for (int j = 0; j < K; j++) t[j] = mulf[u][m[j]];
        sort_small(t, K);
        if (memcmp(t, m, (size_t)K) == 0) s++;
    }
    return s;
}

static u64 image_set(u64 S, int u)
{
    u64 T = 0;
    while (S) { int x = lowbit(S) + 1; S &= S - 1; T |= (u64)1 << (mulf[u][x] - 1); }
    return T;
}

/* all ways to give the s classes of S multiplicities >= 1 with total K */
static void compositions(const int *cls, int s, int idx, int left, unsigned char *buf, int filled)
{
    if (idx == s - 1) {
        for (int j = 0; j < left; j++) buf[filled + j] = (unsigned char)cls[idx];
        unsigned char best[MAXK];
        canon_multiset(buf, best);
        push_row(best);
        return;
    }
    int remaining_classes = s - idx - 1;
    for (int mlt = 1; mlt <= left - remaining_classes; mlt++) {
        for (int j = 0; j < mlt; j++) buf[filled + j] = (unsigned char)cls[idx];
        compositions(cls, s, idx + 1, left - mlt, buf, filled + mlt);
    }
}

/* S is a covering set of distinct classes, contains class 1, |S| <= K */
static void process_set(u64 S)
{
    int s = popc(S);
    sets_with1++; sets_by_size[s]++;

    if (s == K - 1) cov_K1_with1++;
    if (s == K) {                          /* irredundant: every class covers some time alone */
        u64 once = 0, twice = 0, T = S;
        while (T) { int c = lowbit(T) + 1; T &= T - 1; twice |= once & cover1[c]; once |= cover1[c]; }
        u64 priv = once & ~twice;
        int irredundant = 1; T = S;
        while (T) { int c = lowbit(T) + 1; T &= T - 1; if (!(cover1[c] & priv)) irredundant = 0; }
        if (irredundant) irr_K_with1++;
    }

    /* keep S only if it is the lexicographic minimum of its unit orbit.  For two sets of
       equal size, the smaller one owns the smallest class of the symmetric difference. */
    u64 T = S & ~(u64)1;
    while (T) {
        int c = lowbit(T) + 1; T &= T - 1;
        u64 img = image_set(S, invf[c]);
        u64 d = img ^ S;
        if (d && (img & (d & (~d + 1)))) return;
    }
    canon_by_size[s]++;
    int cls[MAXK], n = 0; T = S;
    while (T) { cls[n++] = lowbit(T) + 1; T &= T - 1; }
    unsigned char buf[MAXK];
    compositions(cls, s, 0, K, buf, 0);
}

/* add any further classes (not excluded, larger index order) up to the size limit */
static void extend_free(u64 S, u64 allowed, int from, int slots)
{
    process_set(S);
    if (slots == 0) return;
    for (int c = from; c <= N; c++)
        if ((allowed >> (c - 1)) & 1)
            extend_free(S | ((u64)1 << (c - 1)), allowed, c + 1, slots - 1);
}

/* Enumerates every covering set S with 1 in S and |S| <= K exactly once.
   State: chosen (a partial cover containing class 1), excl (classes that S must avoid).
   At an uncovered time a, S must contain a class covering a; branch on the first such
   class of S in a fixed order and exclude the earlier ones.  When chosen covers every
   time, S = chosen + any non-excluded extra classes.                                  */
static void dfs_sets(int depth, u64 covered, u64 excl, u64 chosen)
{
    nodes1++;
    if (covered == FULL1) { extend_free(chosen, FULL1 & ~excl & ~chosen, 1, K - depth); return; }
    if (depth == K) return;
    u64 unc = FULL1 & ~covered;
    if ((K - depth) * M < popc(unc)) return;     /* too few classes left to cover the rest */
    int best_a = 0, best_cnt = 1 << 30;
    for (u64 t = unc; t; t &= t - 1) {
        int a = lowbit(t) + 1;
        int cnt = popc(covby[a] & ~excl);
        if (cnt < best_cnt) { best_cnt = cnt; best_a = a; }
    }
    if (best_cnt == 0) return;
    u64 cand = covby[best_a] & ~excl, e = excl;
    while (cand) {
        int c = lowbit(cand) + 1; cand &= cand - 1;
        dfs_sets(depth + 1, covered | cover1[c], e, chosen | ((u64)1 << (c - 1)));
        e |= (u64)1 << (c - 1);
    }
}

static int cmp_row(const void *a, const void *b) { return memcmp(a, b, MAXK); }

static void level_one(void)
{
    nrows = 0; nodes1 = 0; sets_with1 = 0; irr_K_with1 = 0; cov_K1_with1 = 0;
    memset(sets_by_size, 0, sizeof sets_by_size); memset(canon_by_size, 0, sizeof canon_by_size);
    if (M > 0) dfs_sets(1, cover1[1], 0, 1);
    qsort(rows, nrows, sizeof(Row), cmp_row);
    size_t w = 0;
    for (size_t i = 0; i < nrows; i++)
        if (w == 0 || memcmp(rows[i].c, rows[w - 1].c, MAXK) != 0) rows[w++] = rows[i];
    nrows = w;
}

static u128 perm_count(const unsigned char *m)   /* K! / prod(multiplicity!) */
{
    u128 r = 1; int run = 0;
    for (int i = 0; i < K; i++) {
        r *= (u128)(i + 1);
        run = (i > 0 && m[i] == m[i - 1]) ? run + 1 : 1;
        r /= (u128)run;
    }
    return r;
}

/* ------------------------------------------------------------------------- */
/* Lifts                                                                       */
/* ------------------------------------------------------------------------- */

typedef struct { int w[MAXK]; } Tup;
typedef struct { Tup *t; size_t n, cap; } TupList;

static void tl_push(TupList *L, const Tup *x)
{
    if (L->n == L->cap) {
        L->cap = L->cap ? L->cap * 2 : 64;
        L->t = realloc(L->t, L->cap * sizeof(Tup));
        if (!L->t) die("out of memory");
    }
    L->t[L->n++] = *x;
}

static int gW, gC, gLevelNew;
static long gStep;                       /* l*p : the amount added per lift digit */
static u64 gFull[MAXW];
static u64 gB[MAXK][MAXC][MAXW];         /* gB[i][a]: times blocked by coordinate i with digit a */
static u64 gSuf[MAXK + 1][MAXW];         /* union of gB[r][*] over r >= i */
static int gDigits[MAXK];
static const Tup *gBase;
static TupList *gOut;
static long long gNodes, gWitnessFree, gImproper;
static int gUseBound;
#define KEEPWF 4
static int gWfDigits[KEEPWF][MAXK];      /* digits of the first few witness-free completions */

/* alternative (a) of the definition at level L: some prime q | L divides all but at most
   one coordinate  <=>  for some i, gcd(L, all coordinates except i) > 1.                */
static int proper_by_gcd(const int *w, int L)
{
    int rest = L;
    for (int q = 2; q <= rest; q++) {
        if (rest % q) continue;
        while (rest % q == 0) rest /= q;
        int not_div = 0;
        for (int i = 0; i < K; i++) if (w[i] % q) not_div++;
        if (not_div <= 1) return 1;
    }
    return 0;
}

static void lift_dfs(int i, const u64 *cov)
{
    gNodes++;
    for (int x = 0; x < gW; x++)                    /* can the rest still block every time? */
        if ((cov[x] | gSuf[i][x]) != gFull[x]) return;
    if (i == K) {                                   /* every time is blocked: no witness */
        if (gWitnessFree < KEEPWF) memcpy(gWfDigits[gWitnessFree], gDigits, sizeof gDigits);
        gWitnessFree++;
        Tup t;
        memset(&t, 0, sizeof t);
        for (int r = 0; r < K; r++) t.w[r] = gBase->w[r] + (int)(gDigits[r] * gStep);
        if (!proper_by_gcd(t.w, gLevelNew)) { gImproper++; tl_push(gOut, &t); }
        return;
    }
    if (gUseBound) {
        /* the unassigned coordinates block at most sum_r max_a |U & B[r][a]| of the
           still unblocked times U; if that is less than |U| no completion blocks all */
        int unc = 0, sum = 0;
        for (int x = 0; x < gW; x++) unc += popc(gFull[x] & ~cov[x]);
        for (int r = i; r < K && sum < unc; r++) {
            int best = 0;
            for (int a = 0; a < gC; a++) {
                int g = 0;
                for (int x = 0; x < gW; x++) g += popc(gB[r][a][x] & ~cov[x]);
                if (g > best) best = g;
            }
            sum += best;
        }
        if (sum < unc) return;
    }
    u64 nc[MAXW];
    for (int a = 0; a < gC; a++) {
        for (int x = 0; x < gW; x++) nc[x] = cov[x] | gB[i][a][x];
        gDigits[i] = a;
        lift_dfs(i + 1, nc);
    }
}

/* Appends to `out` every improper c-lift (level c*l) of the level-l vector `base`.
   Times: t = j/(c*l*p).  By the symmetry j -> -j only 1 <= j <= c*l*p/2 is needed.
   If c | j the time is a level-l time, and `base` has no witness there (checked below),
   and a lift does not change j*w mod 1 at such a time; so only c not dividing j is used. */
static void lift_tuple(const Tup *base, int l, int c, TupList *out, int use_bound)
{
    long lp = (long)l * P, Lp = lp * c;
    if (c < 2 || c > MAXC) die("lift factor out of range");

    /* check that base really has no witness at level l (it must lie in I(K,P,l)) */
    for (long j = 1; 2 * j <= lp; j++) {
        int blocked = 0;
        for (int i = 0; i < K && !blocked; i++) {
            long x = (j * base->w[i]) % lp, d = x <= lp - x ? x : lp - x;
            if ((long)(K + 1) * d < lp) blocked = 1;
        }
        if (!blocked) die("internal: base vector of a lift has a witness");
    }

    int T = 0;
    static long tj[MAXT];
    for (long j = 1; 2 * j <= Lp; j++) if (j % c) { if (T >= MAXT) die("too many times"); tj[T++] = j; }
    gW = (T + 63) / 64; gC = c; gStep = lp; gLevelNew = l * c; gBase = base; gOut = out; gUseBound = use_bound;
    memset(gFull, 0, sizeof gFull);
    for (int t = 0; t < T; t++) gFull[t / 64] |= (u64)1 << (t % 64);
    for (int i = 0; i < K; i++)
        for (int a = 0; a < c; a++) {
            long w = base->w[i] + a * lp;
            u64 *b = gB[i][a];
            for (int x = 0; x < gW; x++) b[x] = 0;
            for (int t = 0; t < T; t++) {
                long x = (tj[t] * w) % Lp, d = x <= Lp - x ? x : Lp - x;
                if ((long)(K + 1) * d < Lp) b[t / 64] |= (u64)1 << (t % 64);
            }
        }
    for (int x = 0; x < gW; x++) gSuf[K][x] = 0;
    for (int i = K - 1; i >= 0; i--)
        for (int x = 0; x < gW; x++) {
            u64 u = gSuf[i + 1][x];
            for (int a = 0; a < c; a++) u |= gB[i][a][x];
            gSuf[i][x] = u;
        }
    u64 zero[MAXW];
    memset(zero, 0, sizeof zero);
    lift_dfs(0, zero);
}

static void row_to_tup(const unsigned char *c, Tup *t)
{
    memset(t, 0, sizeof *t);
    for (int i = 0; i < K; i++) t->w[i] = c[i];
}

/* ------------------------------------------------------------------------- */
/* Modes                                                                       */
/* ------------------------------------------------------------------------- */

static int mode_level1(const char *outname)
{
    level_one();
    printf("LEVEL ONE  p=%d k=%d  n=%d classes  each class covers m=%d times\n", P, K, N, M);
    printf("  search nodes: %lld\n", nodes1);
    printf("  covering sets with at most %d distinct classes that contain class 1: %lld\n", K, sets_with1);
    int tau = 0;
    for (int s = 1; s <= K; s++) {
        if (sets_by_size[s] == 0) continue;
        if (!tau) tau = s;
        printf("    size %2d: %10lld sets containing class 1, %9lld unit orbits of sets\n",
               s, sets_by_size[s], canon_by_size[s]);
    }
    printf("  smallest number of classes in a cover (tau): %d\n", tau);
    printf("  unit orbits of covering %d-multisets = orbits of I(%d,%d,1): %zu\n", K, K, P, nrows);
    u128 total = 0; long long multisets = 0;
    for (size_t i = 0; i < nrows; i++) {
        int orbit = N / stabilizer_size(rows[i].c);
        multisets += orbit;
        total += (u128)orbit * perm_count(rows[i].c) * ((u128)1 << K);
    }
    printf("  covering %d-multisets (all, not up to units): %lld\n", K, multisets);
    printf("  |I(%d,%d,1)| as ordered vectors with signs: ", K, P); print_u128(total); printf("\n");
    printf("  among the sets that contain class 1: irredundant covers on %d distinct classes: %lld; "
           "covers on %d distinct classes: %lld\n", K, irr_K_with1, K - 1, cov_K1_with1);
    FILE *f = fopen(outname, "w");
    if (!f) die("cannot open output file");
    for (size_t i = 0; i < nrows; i++) {
        for (int j = 0; j < K; j++) fprintf(f, j ? " %d" : "%d", rows[i].c[j]);
        fputc('\n', f);
    }
    fclose(f);
    printf("  wrote %zu orbit representatives to %s\n", nrows, outname);
    return 0;
}

static int mode_cascade(const char *inname, const char *outname)
{
    FILE *in = fopen(inname, "r"), *out = fopen(outname, "w");
    if (!in || !out) die("cannot open files");
    long long orbits = 0, died[8] = {0}, alive32 = 0, closed_terminal = 0, open_terminal = 0;
    long long total_nodes = 0;
    int levels[5] = {2, 4, 8, 16, 32};
    for (;;) {
        unsigned char c[MAXK]; int v, got = 0;
        for (int j = 0; j < K; j++) { if (fscanf(in, "%d", &v) != 1) break; c[j] = (unsigned char)v; got++; }
        if (got == 0) break;
        if (got != K) die("bad orbit file");
        orbits++;
        Tup r; row_to_tup(c, &r);
        TupList cur = {0}, nxt = {0}, f2 = {0};
        tl_push(&cur, &r);
        for (int j = 0; j < K; j++) fprintf(out, j ? " %d" : "%d", c[j]);
        fprintf(out, " :");
        int l = 1, dead_at = 0;
        for (int s = 0; s < 5; s++) {
            nxt.n = 0;
            for (size_t i = 0; i < cur.n; i++) { gNodes = 0; lift_tuple(&cur.t[i], l, 2, &nxt, 0); total_nodes += gNodes; }
            l *= 2;
            fprintf(out, " l%d=%zu", levels[s], nxt.n);
            if (s == 0) for (size_t i = 0; i < nxt.n; i++) tl_push(&f2, &nxt.t[i]);
            TupList tmp = cur; cur = nxt; nxt = tmp;
            if (cur.n == 0) { dead_at = levels[s]; died[s]++; break; }
        }
        if (!dead_at) {
            alive32++;
            if ((K + 1) % 2) die("terminal step needs K+1 even");
            int c7 = (K + 1) / 2;
            fprintf(out, " ALIVE-AT-32 | level %d from the %zu members of F_2:", K + 1, f2.n);
            long long imp_total = 0;
            printf("  orbit");
            for (int j = 0; j < K; j++) printf(" %d", c[j]);
            printf(": alive at level 32; level-%d step over %zu level-2 members\n", K + 1, f2.n);
            for (size_t i = 0; i < f2.n; i++) {
                TupList t14 = {0};
                gNodes = gWitnessFree = gImproper = 0;
                lift_tuple(&f2.t[i], 2, c7, &t14, 1);
                total_nodes += gNodes;
                imp_total += gImproper;
                printf("    level-2 member");
                for (int j = 0; j < K; j++) printf(" %d", f2.t[i].w[j]);
                printf(": nodes=%lld witness-free completions=%lld improper after gcd=%lld\n",
                       gNodes, gWitnessFree, gImproper);
                for (long long q = 0; q < gWitnessFree && q < KEEPWF; q++) {
                    printf("      witness-free completion, digits a_i (w_i + a_i*2p):");
                    for (int j = 0; j < K; j++) printf(" %d", gWfDigits[q][j]);
                    printf("  -> tuple:");
                    for (int j = 0; j < K; j++) printf(" %ld", f2.t[i].w[j] + gWfDigits[q][j] * 2L * P);
                    printf("\n");
                }
                fprintf(out, " [wf=%lld imp=%lld]", gWitnessFree, gImproper);
                fflush(stdout);
                free(t14.t);
            }
            fprintf(out, " l%d=%lld", K + 1, imp_total);
            if (imp_total == 0) closed_terminal++; else open_terminal++;
        }
        fputc('\n', out);
        free(cur.t); free(nxt.t); free(f2.t);
    }
    fclose(in); fclose(out);
    printf("CASCADE  p=%d k=%d\n", P, K);
    printf("  level-one orbits read: %lld\n", orbits);
    for (int s = 0; s < 5; s++)
        printf("  F becomes empty at level %2d: %lld orbits\n", levels[s], died[s]);
    printf("  still alive at level 32: %lld orbits\n", alive32);
    printf("  of these, empty at level %d: %lld; NOT empty at level %d: %lld\n",
           K + 1, closed_terminal, K + 1, open_terminal);
    printf("  lift search nodes in total: %lld\n", total_nodes);
    long long closed = died[0] + died[1] + died[2] + died[3] + died[4] + closed_terminal;
    printf("  orbits shown eventually proper: %lld of %lld\n", closed, orbits);
    printf("  RESULT: %s\n", closed == orbits
           ? "every level-one orbit has an empty improper fiber at some level"
           : "SOME ORBIT WAS NOT CLOSED");
    printf("  wrote %s\n", outname);
    return closed == orbits ? 0 : 1;
}

static int mode_tiny(const char *route)
{
    level_one();
    int fac[16], nf = 0;
    for (const char *s = route; *s && nf < 16; ) {
        int v = (int)strtol(s, (char **)&s, 10);
        if (v >= 2) fac[nf++] = v;
        if (*s == ',') s++; else if (*s && (*s < '0' || *s > '9')) break;
    }
    printf("TINY p=%d k=%d orbits=%zu", P, K, nrows);
    u128 total = 0;
    for (size_t i = 0; i < nrows; i++)
        total += (u128)(N / stabilizer_size(rows[i].c)) * perm_count(rows[i].c) * ((u128)1 << K);
    printf(" L1="); print_u128(total);
    TupList *cur = calloc(nrows ? nrows : 1, sizeof(TupList));
    for (size_t i = 0; i < nrows; i++) { Tup r; row_to_tup(rows[i].c, &r); tl_push(&cur[i], &r); }
    int l = 1;
    for (int s = 0; s < nf; s++) {
        total = 0;
        for (size_t i = 0; i < nrows; i++) {
            /* every lift is computed twice, without and with the counting bound; the
               two results must be identical */
            TupList nxt = {0}, nx2 = {0};
            for (size_t j = 0; j < cur[i].n; j++) lift_tuple(&cur[i].t[j], l, fac[s], &nxt, 0);
            for (size_t j = 0; j < cur[i].n; j++) lift_tuple(&cur[i].t[j], l, fac[s], &nx2, 1);
            if (nxt.n != nx2.n || (nxt.n && memcmp(nxt.t, nx2.t, nxt.n * sizeof(Tup))))
                die("internal: the counting bound changed a lift result");
            free(nx2.t);
            free(cur[i].t); cur[i] = nxt;
            total += (u128)(N / stabilizer_size(rows[i].c)) * perm_count(rows[i].c) * ((u128)1 << K) * (u128)nxt.n;
        }
        l *= fac[s];
        printf(" L%d=", l); print_u128(total);
    }
    printf("\n");
    for (size_t i = 0; i < nrows; i++) {
        printf("ORBIT");
        for (int j = 0; j < K; j++) printf(" %d", rows[i].c[j]);
        printf("\n");
    }
    return 0;
}

int main(int argc, char **argv)
{
    if (argc < 4) {
        fprintf(stderr, "usage: %s level1 P K OUT | cascade P K ORBITS OUT | tiny P K c1,c2,..\n", argv[0]);
        return 2;
    }
    setup(atoi(argv[2]), atoi(argv[3]));
    if (!strcmp(argv[1], "level1") && argc == 5) return mode_level1(argv[4]);
    if (!strcmp(argv[1], "cascade") && argc == 6) return mode_cascade(argv[4], argv[5]);
    if (!strcmp(argv[1], "tiny") && argc == 5) return mode_tiny(argv[4]);
    if (!strcmp(argv[1], "tiny") && argc == 4) return mode_tiny("");
    fprintf(stderr, "bad arguments\n");
    return 2;
}
```

</details>

<details>
<summary>pt004_l3c_tests.py</summary>

```python
#!/usr/bin/env python3
"""
TOGETHER - PROOF TABLE 004 - Round 3 - Turn 11 - item L3-C, stage 1
Seat: Fable-A (testing seat).

Tests of the C program pt004_l3c on tiny cases, against a brute-force oracle that
follows Definition 2.1 of arXiv:2609.02604v2 word by word.

  Z_{p,l} = residues mod p*l not divisible by p.
  v in Z_{p,l}^k is (k,p,l)-proper if
    (a) for some i, gcd(l, v_1, .., v_i omitted, .., v_k) > 1, or
    (b) for some t in (l*p)^(-1) Z, ||t*v_i|| >= 1/(k+1) for every i.
  I(k,p,l) = the vectors for which neither holds.

The oracle looks at EVERY vector of Z_{p,l}^k and EVERY time j/(l*p), j = 0 .. l*p - 1.
It uses no folding, no orbits, no covers and no lifting.

What is compared, for each tiny case (k, p, L):
  * |I(k,p,L)| counted by the oracle, against the C program's total, for every way of
    writing L as an ordered product of lift factors (for example 12 = 2*2*3 = 3*4 = 12);
  * at level one, the set of unit orbits (the oracle folds and canonicalises each
    improper vector itself, trying all units).
The C program also computes every lift twice (with and without its counting bound)
and stops with an error if the two differ.

Standard library only.  Runs ./pt004_l3c (must be built first).  Writes no file.
Usage:  python3 pt004_l3c_tests.py           exit code 0 if every test passed
"""
import itertools
import subprocess
import sys
from math import gcd

BINARY = "./pt004_l3c"


def dist(x, m):
    r = x % m
    return min(r, m - r)


def improper_literal(v, k, p, l):
    """Definition 2.1, literally."""
    lp = l * p
    for i in range(k):                       # alternative (a)
        g = l
        for j in range(k):
            if j != i:
                g = gcd(g, v[j])
        if g > 1:
            return False
    for j in range(lp):                      # alternative (b): t = j/(l*p)
        if all((k + 1) * dist(j * x, lp) >= lp for x in v):
            return False
    return True


def oracle(k, p, l, literal=False):
    """All improper vectors of Z_{p,l}^k.  Returns (count, set of level-one orbits)."""
    lp = l * p
    residues = [x for x in range(lp) if x % p]
    full = (1 << lp) - 1
    blocked = {}                             # blocked[x]: bit j set if x blocks time j/(lp)
    for x in residues:
        mask = 0
        for j in range(lp):
            if (k + 1) * dist(j * x, lp) < lp:
                mask |= 1 << j
        blocked[x] = mask
    n = (p - 1) // 2
    count = 0
    orbits = set()
    for v in itertools.product(residues, repeat=k):
        if literal:
            bad = improper_literal(v, k, p, l)
        else:
            m = 0
            for x in v:
                m |= blocked[x]
            bad = (m == full)                # no witness at all
            if bad:                          # then test alternative (a)
                for i in range(k):
                    g = l
                    for j in range(k):
                        if j != i:
                            g = gcd(g, v[j])
                    if g > 1:
                        bad = False
                        break
        if bad:
            count += 1
            if l == 1:
                folded = [dist(x, p) for x in v]
                orbits.add(min(tuple(sorted(dist(u * x, p) for x in folded))
                               for u in range(1, n + 1)))
    return count, orbits


def routes(L):
    """All ways to write L as an ordered product of factors >= 2 (the empty product for 1)."""
    if L == 1:
        return [[]]
    out = []
    for c in range(2, L + 1):
        if L % c == 0 and c <= 16:
            out.extend([c] + rest for rest in routes(L // c))
    return out


def run_c(p, k, route):
    args = [BINARY, "tiny", str(p), str(k)] + ([",".join(map(str, route))] if route else [])
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} failed: {res.stderr.strip()}")
    lines = res.stdout.strip().split("\n")
    totals = {}
    for field in lines[0].split():
        if field.startswith("L") and "=" in field:
            name, value = field.split("=")
            totals[int(name[1:])] = int(value)
    orbits = {tuple(int(x) for x in ln.split()[1:]) for ln in lines[1:] if ln.startswith("ORBIT")}
    return totals, orbits


def main():
    ok = True

    print("STAGE 1a: cases worked out by hand (see the report), oracle and C program")
    hand = [
        # (k, p, l, expected |I(k,p,l)|, comment)
        (1, 5, 1, 4, "k=1: no time j/p reaches 1/2, so all 4 vectors are improper"),
        (1, 5, 2, 0, "k=1, level 2: w odd has the witness t=1/2; w even: gcd(2, nothing)=2"),
        (2, 5, 1, 8, "classes {1,2}: 1 covers time 1, 2 covers time 2; only {1,2} covers; 1*2!*2^2"),
        (2, 5, 2, 0, "lifts of (1,2): (1,2),(6,2),(6,7) by gcd; (1,7) has witness t=1/2"),
        (2, 7, 1, 24, "covers are {1,2},{1,3},{2,3}: 3*2!*2^2"),
    ]
    for k, p, l, expected, comment in hand:
        lit, _ = oracle(k, p, l, literal=True)
        fast, _ = oracle(k, p, l)
        c_tot, _ = run_c(p, k, [l] if l > 1 else [])
        good = (lit == expected == fast == c_tot[l])
        ok = ok and good
        print(f"  k={k} p={p} l={l}: by hand {expected}, literal oracle {lit}, oracle {fast}, "
              f"C {c_tot[l]}  {'OK' if good else 'FAIL'}   ({comment})")

    print("STAGE 1b: the fast oracle against the literal oracle (definition word by word)")
    cases_lit = [(2, 5, 4), (2, 7, 2), (2, 7, 3), (2, 11, 2), (3, 7, 2), (3, 11, 1), (3, 13, 2), (4, 11, 1)]
    for k, p, l in cases_lit:
        a, _ = oracle(k, p, l, literal=True)
        b, _ = oracle(k, p, l)
        good = (a == b)
        ok = ok and good
        print(f"  k={k} p={p} l={l}: literal {a}, fast {b}  {'OK' if good else 'FAIL'}")

    print("STAGE 1c: C program against the oracle, every level and every lift route")
    grid = []
    for p in (3, 5, 7):
        grid += [(1, p, L) for L in (1, 2, 3, 4, 6)]
    for p in (5, 7, 11, 13):
        grid += [(2, p, L) for L in (1, 2, 3, 4, 6, 8, 9, 12)]
    for p in (7, 11, 13, 17):
        grid += [(3, p, L) for L in (1, 2, 3, 4, 6, 8)]
    for p in (11, 13):
        grid += [(4, p, L) for L in (1, 2, 3, 4)]
    grid += [(4, 17, 1), (4, 17, 2), (4, 19, 1), (4, 19, 2)]
    grid += [(5, 11, 1), (5, 11, 2), (5, 13, 1), (5, 13, 2), (5, 17, 1), (6, 17, 1)]
    tested = routes_tested = nonzero = 0
    for k, p, L in grid:
        count, orbits = oracle(k, p, L)
        tested += 1
        nonzero += count > 0
        details = []
        good = True
        for route in routes(L):
            totals, c_orbits = run_c(p, k, route)
            routes_tested += 1
            if totals.get(L) != count:
                good = False
                details.append(f"route {route}: C says {totals.get(L)}")
            if L == 1 and c_orbits != orbits:
                good = False
                details.append(f"orbit sets differ: oracle {sorted(orbits)}, C {sorted(c_orbits)}")
        ok = ok and good
        extra = f"  level-one orbits {len(orbits)}" if L == 1 else ""
        print(f"  k={k} p={p:2d} L={L:2d}: |I| = {count:8d}  routes {len(routes(L)):2d}{extra}  "
              f"{'OK' if good else 'FAIL ' + '; '.join(details)}")
    print(f"  cases: {tested}, of which with |I| > 0: {nonzero}; lift routes run: {routes_tested}")
    print(f"RESULT: {'all tests passed' if ok else 'A TEST FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
```

</details>

<details>
<summary>pt004_l3c_level1_check.py</summary>

```python
#!/usr/bin/env python3
"""
TOGETHER - PROOF TABLE 004 - Round 3 - Turn 11 - item L3-C, stage 2 (second implementation)
Seat: Fable-A (testing seat).

A second, separate implementation of level-one generation, in Python, to compare with
the list written by the C program (pt004_l3c level1 P K FILE).

Level one (arXiv:2609.02604v2, Section 4): speed classes and time classes are 1..n,
n = (p-1)/2; class v covers time a when (k+1)*d_p(a*v) < p; I(k,p,1) is the family of
k-multisets of classes that cover every time class.  Units u act by v -> fold(u*v).
Orbit representative used here and in the C program: the lexicographically smallest
sorted k-tuple of the orbit.

Differences from the C program, on purpose:
  * the search branches on the LOWEST uncovered time (the C program takes the time with
    the fewest available classes), so the search tree is a different one;
  * supports are canonicalised by an integer comparison over the member-inverse units,
    multisets by sorted tuples; nothing is shared with the C code.

Standard library only.  Reads the C program's orbit file, writes nothing.
Usage:  python3 pt004_l3c_level1_check.py P K ORBITFILE        exit code 0 if identical
"""
import sys
from itertools import combinations


def main():
    p, k, fname = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    n = (p - 1) // 2
    fold = lambda x: min(x % p, p - x % p)
    full = (1 << n) - 1
    cover = [0] * (n + 1)                       # cover[v]: bit a-1 set if v covers time a
    covby = [[] for _ in range(n + 1)]          # covby[a]: classes covering time a
    for v in range(1, n + 1):
        for a in range(1, n + 1):
            if (k + 1) * fold(a * v) < p:
                cover[v] |= 1 << (a - 1)
                covby[a].append(v)
    m = bin(cover[1]).count("1")
    mul = [[fold(u * x) for x in range(n + 1)] for u in range(n + 1)]
    inv = [0] * (n + 1)
    for u in range(1, n + 1):
        for x in range(1, n + 1):
            if mul[u][x] == 1:
                inv[u] = x

    # ---- every covering set of distinct classes that contains class 1, size <= k ----
    found = []

    def extend(S, free, idx, slots):
        found.append(S)
        if slots:
            for i in range(idx, len(free)):
                extend(S | (1 << (free[i] - 1)), free, i + 1, slots - 1)

    def rec(depth, covered, excl, chosen):
        if covered == full:
            free = [c for c in range(1, n + 1)
                    if not (excl >> (c - 1)) & 1 and not (chosen >> (c - 1)) & 1]
            extend(chosen, free, 0, k - depth)
            return
        if depth == k:
            return
        unc = full & ~covered
        if (k - depth) * m < bin(unc).count("1"):
            return
        a = (unc & -unc).bit_length()           # the lowest uncovered time
        e = excl
        for c in covby[a]:
            if (excl >> (c - 1)) & 1:
                continue
            rec(depth + 1, covered | cover[c], e, chosen | (1 << (c - 1)))
            e |= 1 << (c - 1)

    if m:
        rec(1, cover[1], 0, 1)
    by_size = {}
    for S in found:
        s = bin(S).count("1")
        by_size[s] = by_size.get(s, 0) + 1
    print(f"p={p} k={k}: covering sets with at most {k} classes that contain class 1: {len(found)}")
    for s in sorted(by_size):
        print(f"  size {s}: {by_size[s]}")
    if len(set(found)) != len(found):
        print("  ERROR: a set was produced twice")
        return 1

    # ---- canonical supports: class c gets weight 2^(n-c), so the lexicographically
    #      smallest sorted tuple is the set with the LARGEST weight ----
    weight = [0] + [1 << (n - c) for c in range(1, n + 1)]
    supports = set()
    for S in found:
        cls = [c for c in range(1, n + 1) if (S >> (c - 1)) & 1]
        best = 0
        for c in cls:
            row = mul[inv[c]]
            w = 0
            for x in cls:
                w += weight[row[x]]
            if w > best:
                best = w
        supports.add(best)
    print(f"  unit orbits of covering sets: {len(supports)}")

    # ---- all k-multisets on each canonical support, canonicalised as sorted tuples ----
    orbits = set()
    for w in supports:
        cls = [c for c in range(1, n + 1) if w & weight[c]]
        s = len(cls)
        for bars in combinations(range(1, k), s - 1):
            cuts = (0,) + bars + (k,)
            multi = []
            for i in range(s):
                multi += [cls[i]] * (cuts[i + 1] - cuts[i])
            best = tuple(multi)
            for c in cls:
                row = mul[inv[c]]
                t = tuple(sorted(row[x] for x in multi))
                if t < best:
                    best = t
            orbits.add(best)
    mine = sorted(orbits)
    print(f"  unit orbits of covering {k}-multisets (this script): {len(mine)}")

    theirs = [tuple(int(x) for x in ln.split()) for ln in open(fname)]
    print(f"  rows in {fname}: {len(theirs)}")
    same = (mine == theirs)
    print(f"RESULT: {'the two lists are identical, row for row' if same else 'THE LISTS DIFFER'}")
    return 0 if same else 1


if __name__ == "__main__":
    sys.exit(main())
```

</details>

<details>
<summary>pt004_l3c_compare.py</summary>

```python
#!/usr/bin/env python3
"""
TOGETHER - PROOF TABLE 004 - Round 3 - Turn 11 - item L3-C: comparison with the archive
Seat: Fable-A (testing seat).

Compares my own results for the prime gate p = 83, k = 13 with the p = 83 certificate data
of Zenodo record 22066772 (J. Allikvere, "Fourteen lonely runners: manuscript, gate
certificates, and audit code", CC BY 4.0).  Only certificate DATA is read:
  small_gates/certificates_p83/SUMMARY.json
  small_gates/p83/raw/*.log, c12/*.log, filt/*.stats, filt/*.out, kill_orbit1.txt, kill_orbit2.txt
No program of the archive is read or run.

My files (written by pt004_l3c):
  LEVEL1   one line per unit orbit of I(13,83,1): the lexicographically smallest sorted tuple
  CASCADE  one line per orbit: |F_2|, |F_4|, ... until the first empty level
  LOG      standard output of the cascade run (holds the level-14 details)

The archive's rows use other representatives of the same orbits, so every archive row is
first brought to my normal form (smallest sorted tuple over all 41 units), in this script.

Standard library only.  Writes nothing.
Usage: python3 pt004_l3c_compare.py LEVEL1 CASCADE LOG ARCHIVE_DIR
       ARCHIVE_DIR = the folder that contains p83/ and certificates_p83/
Exit code 0 if every comparison agrees.
"""
import glob
import json
import os
import re
import sys
from math import gcd

P, K = 83, 13
N = (P - 1) // 2


def fold(x):
    r = x % P
    return min(r, P - r)


COVER = {v: frozenset(a for a in range(1, N + 1) if (K + 1) * fold(a * v) < P) for v in range(1, N + 1)}
ALL_TIMES = frozenset(range(1, N + 1))
_canon_cache = {}


def canon(t):
    """Smallest sorted tuple in the unit orbit of the multiset t (all N units tried)."""
    key = tuple(sorted(t))
    r = _canon_cache.get(key)
    if r is None:
        r = min(tuple(sorted(fold(u * x) for x in key)) for u in range(1, N + 1))
        _canon_cache[key] = r
    return r


def is_cover(t):
    s = set()
    for v in set(t):
        s |= COVER[v]
    return s == ALL_TIMES


def is_irredundant(t):
    cls = sorted(set(t))
    for c in cls:
        s = set()
        for v in cls:
            if v != c:
                s |= COVER[v]
        if s == ALL_TIMES:
            return False
    return True


def parse_levels(text):
    return {int(a): int(b) for a, b in re.findall(r"\bl(\d+)=(\d+)", text)}


def main():
    level1_file, cascade_file, log_file, arch = sys.argv[1:5]
    p83 = os.path.join(arch, "p83")
    ok = True

    def check(label, cond, detail=""):
        nonlocal ok
        ok = ok and bool(cond)
        print(f"  [{'OK' if cond else 'DIFFERENT'}] {label}{(' -- ' + detail) if detail else ''}")

    # ------------------------------------------------------------------ A
    print("A. My level-one list, re-examined in Python")
    mine = [tuple(int(x) for x in ln.split()) for ln in open(level1_file)]
    mine_set = set(mine)
    check(f"{len(mine)} rows, sorted, no row twice", mine == sorted(mine) and len(mine_set) == len(mine))
    check("every row is a cover of the 41 time classes (so it lies in I(13,83,1))", all(is_cover(t) for t in mine))
    check("every row is the smallest sorted tuple of its unit orbit (all 41 units tried)",
          all(canon(t) == t for t in mine))
    distinct13 = [t for t in mine if len(set(t)) == 13]
    irred = set(t for t in distinct13 if is_irredundant(t))
    reducible13 = [t for t in distinct13 if t not in irred]
    doubled = [t for t in mine if len(set(t)) == 12]
    covers12 = set(canon(tuple(sorted(set(t)))) for t in doubled)
    other = len(mine) - len(distinct13) - len(doubled)
    print(f"     13 distinct classes, irredundant: {len(irred)}")
    print(f"     13 distinct classes, containing a 12-class cover: {len(reducible13)}")
    print(f"     12 distinct classes with one class doubled: {len(doubled)}")
    print(f"     fewer than 12 distinct classes: {other}")
    print(f"     unit orbits of 12-class covers behind them: {len(covers12)}")

    cascade = {}
    alive = {}
    for ln in open(cascade_file):
        left, right = ln.split(":", 1)
        t = tuple(int(x) for x in left.split())
        cascade[t] = parse_levels(right.split("ALIVE")[0])
        if "ALIVE-AT-32" in right:
            alive[t] = right
    check("the cascade file has the same orbits as the level-one file", set(cascade) == mine_set)
    if set(cascade) != mine_set:
        print("RESULT: SOME COMPARISON DIFFERS (stopped: my two files do not describe the same orbits)")
        return 1
    surv_mine = set(t for t in mine if cascade[t][2] > 0)
    print(f"     my orbits with F_2 not empty: {len(surv_mine)}; with F_2 empty: {len(mine) - len(surv_mine)}")

    # ------------------------------------------------------------------ B
    print("B. The archive's logged level-one counts against mine")
    summary = json.load(open(os.path.join(arch, "certificates_p83", "SUMMARY.json")))
    bf = summary["base_family"]
    ir_rows_log = sum(int(re.search(r"raw_irred13=(\d+)", open(f).read()).group(1))
                      for f in glob.glob(os.path.join(p83, "raw", "ir_*.log")))
    c12_log = {int(re.search(r"root=(\d+)", s).group(1)): int(re.search(r"canonical12=(\d+)", s).group(1))
               for s in (open(f).read() for f in glob.glob(os.path.join(p83, "c12", "c12_*.log")))}
    check(f"archive irredundant rows: logs sum to {ir_rows_log}, SUMMARY says {bf['irredundant_raw_rows']}; "
          f"my irredundant orbits: {len(irred)}",
          ir_rows_log == bf["irredundant_raw_rows"] == len(irred))
    check(f"archive 12-class cover rows under root 0: {c12_log[0]}; my orbits of 12-class covers: {len(covers12)}",
          c12_log[0] == len(covers12))
    check(f"archive 12-cover rows over the 5 roots: {sum(c12_log.values())} (SUMMARY: "
          f"{bf['reducible_12cover_rows_prededup']}, 'prededup')",
          sum(c12_log.values()) == bf["reducible_12cover_rows_prededup"])
    check(f"archive total rows {bf['total_rows_filtered']} = {bf['irredundant_raw_rows']} + 41 x "
          f"{bf['reducible_12cover_rows_prededup']}",
          bf["total_rows_filtered"] == bf["irredundant_raw_rows"] + 41 * bf["reducible_12cover_rows_prededup"])

    # ------------------------------------------------------------------ C
    print("C. Every survivor row of the archive against my cascade (row by row)")
    files = sorted(glob.glob(os.path.join(p83, "filt", "*.out")))
    arch_rows = 0
    not_found = not_cover = level_diff = persist_diff = stats_diff = 0
    arch_orbits = set()
    ir_orbits = []
    prefixes = {}                       # root -> set of 12-prefixes seen in c12_root.out
    surv_by_file = {}
    first_zero_counts = {}
    persistent_rows = 0
    examples = []
    for f in files:
        name = os.path.basename(f)[:-4]
        rows_here = 0
        for ln in open(f):
            base = tuple(int(x) for x in ln.split("base:")[1].split("l2=")[0].split())
            levels = parse_levels(ln)
            rows_here += 1
            if not is_cover(base):
                not_cover += 1
            c = canon(base)
            arch_orbits.add(c)
            if name.startswith("ir_"):
                ir_orbits.append(c)
            else:
                prefixes.setdefault(int(name.split("_")[1]), set()).add(base[:12])
            if c not in cascade:
                not_found += 1
                continue
            if cascade[c] != levels:
                level_diff += 1
                if len(examples) < 5:
                    examples.append((name, base, levels, cascade[c]))
            if ("PERSISTENT" in ln) != (c in alive):
                persist_diff += 1
            persistent_rows += "PERSISTENT" in ln
            zero = [l for l in sorted(cascade[c]) if cascade[c][l] == 0]
            first_zero_counts[zero[0] if zero else 0] = first_zero_counts.get(zero[0] if zero else 0, 0) + 1
        surv_by_file[name] = rows_here
        st = open(f[:-4] + ".stats").read()
        if int(re.search(r"survivors=(\d+)", st).group(1)) != rows_here:
            stats_diff += 1
        arch_rows += rows_here
    check(f"archive survivor rows read: {arch_rows} (SUMMARY: {summary['cascade']['survivor_rows']}); "
          f"each file has as many rows as its .stats says", arch_rows == summary["cascade"]["survivor_rows"] and stats_diff == 0)
    check("every archive row is a cover", not_cover == 0, f"{not_cover} are not")
    check("every archive row's orbit is in my level-one list", not_found == 0, f"{not_found} missing")
    check("for every archive row, l2, l4, l8, l16, l32 are equal to my |F_2| .. |F_32|", level_diff == 0,
          f"{level_diff} rows differ")
    for e in examples:
        print("       example:", e)
    check("the archive's PERSISTENT mark and my 'alive at level 32' agree on every row", persist_diff == 0)
    check(f"set of orbits among the archive's survivors ({len(arch_orbits)}) = my orbits with F_2 not empty "
          f"({len(surv_mine)})", arch_orbits == surv_mine,
          f"only archive {len(arch_orbits - surv_mine)}, only mine {len(surv_mine - arch_orbits)}")

    # ------------------------------------------------------------------ D
    print("D. Rows the archive does not list (they died at level 2), predicted from my data")
    ir_surv_mine = sum(1 for t in irred if cascade[t][2] > 0)
    check(f"irredundant branch: archive survivors {len(ir_orbits)}, all different orbits, all irredundant; "
          f"my irredundant orbits with F_2 not empty: {ir_surv_mine}",
          len(set(ir_orbits)) == len(ir_orbits) == ir_surv_mine and set(ir_orbits) <= irred)
    check(f"irredundant branch: archive rows that died at level 2: {ir_rows_log - len(ir_orbits)}; "
          f"mine: {len(irred) - ir_surv_mine}", ir_rows_log - len(ir_orbits) == len(irred) - ir_surv_mine)
    check("the 12-class rows behind root 0 of the archive are exactly my 2042 orbits of 12-class covers",
          prefixes[0] == covers12)
    for root in sorted(prefixes):
        rows12 = covers12 if root == 0 else prefixes[root]
        predicted = missing = 0
        for s in rows12:
            for x in range(1, N + 1):
                lv = cascade.get(canon(s + (x,)))
                if lv is None:
                    missing += 1
                elif lv[2] > 0:
                    predicted += 1
        st = open(os.path.join(p83, "filt", f"c12_{root}.stats")).read()
        a_rows = int(re.search(r"rows=(\d+)", st).group(1))
        a_surv = int(re.search(r"survivors=(\d+)", st).group(1))
        src = "my own 12-class covers" if root == 0 else "the 12-class rows seen in the archive file"
        check(f"c12 root {root}: archive rows {a_rows}, survivors {a_surv}; from {src} x 41 extensions: "
              f"rows {41 * len(rows12)}, survivors {predicted}",
              a_rows == 41 * len(rows12) and a_surv == predicted and missing == 0,
              f"{missing} extensions are not in my level-one list" if missing else "")
    check("roots 1-4 only repeat 12-class rows of root 0",
          all(prefixes[r] <= prefixes[0] for r in prefixes))

    # ------------------------------------------------------------------ E
    print("E. The archive's cascade totals, recomputed with MY counts on the archive's rows")
    cs = summary["cascade"]
    mine_tot = {"died_l4": first_zero_counts.get(4, 0), "died_l8": first_zero_counts.get(8, 0),
                "died_l16": first_zero_counts.get(16, 0), "died_l32": first_zero_counts.get(32, 0),
                "persistent": first_zero_counts.get(0, 0)}
    for key in ("died_l4", "died_l8", "died_l16", "died_l32", "persistent"):
        check(f"{key}: archive {cs[key]}, mine {mine_tot[key]}", cs[key] == mine_tot[key])
    my_dead = {l: sum(1 for t in mine if [x for x in sorted(cascade[t]) if cascade[t][x] == 0][:1] == [l])
               for l in (2, 4, 8, 16, 32)}
    print(f"     (my own orbit counts, no row twice: empty at level 2: {my_dead[2]}, 4: {my_dead[4]}, "
          f"8: {my_dead[8]}, 16: {my_dead[16]}, 32: {my_dead[32]}, alive at 32: {len(alive)})")
    check("orbits alive at level 32 are the two named in the paper and the archive",
          sorted(alive) == sorted(tuple(int(x) for x in s.split())
                                  for s in summary["persistent_orbits"]["representatives"]))

    # ------------------------------------------------------------------ F
    print("F. The level-14 step")
    arch14 = {}
    for kf in ("kill_orbit1.txt", "kill_orbit2.txt"):
        text = open(os.path.join(p83, kf)).read()
        for blk in text.split("=== level-2 tuple:")[1:]:
            tup = tuple(int(x) for x in blk.split("\n")[0].split())
            digits = tuple(int(x) for x in re.search(r"prefix:([ \d]+)", blk).group(1).split())
            wi = int(re.search(r"witness_improper=(\d+)", blk).group(1))
            ia = int(re.search(r"improper_after_gcd7=(\d+)", blk).group(1))
            arch14[tup] = (digits, wi, ia)
    mine14 = {}
    log = open(log_file).read()
    for mobj in re.finditer(r"level-2 member([ \d]+): nodes=\d+ witness-free completions=(\d+) improper after gcd=(\d+)\n"
                            r"((?:      witness-free completion.*\n)*)", log):
        tup = tuple(int(x) for x in mobj.group(1).split())
        dig = re.findall(r"digits a_i \(w_i \+ a_i\*2p\):([ \d]+)->", mobj.group(4))
        digits = tuple(int(x) for x in dig[0].split()) if len(dig) == 1 else None
        mine14[tup] = (digits, int(mobj.group(2)), int(mobj.group(3)))
    check(f"level-2 members lifted to level 14: archive {len(arch14)}, mine {len(mine14)}, same tuples",
          set(arch14) == set(mine14))
    check("for each one: exactly 1 witness-free completion, 0 improper after the gcd test, and the same "
          "completion (same digits) as in the archive", all(arch14[t] == mine14.get(t) for t in arch14),
          "" if all(arch14[t] == mine14.get(t) for t in arch14) else str([(t, arch14[t], mine14.get(t)) for t in arch14][:2]))

    # ------------------------------------------------------------------ G
    print("G. Level 14 checked literally in Python on the definition (no lifting code)")
    L = 14
    LP = L * P

    def witness(w):
        for j in range(LP):
            if all((K + 1) * min((j * x) % LP, LP - (j * x) % LP) >= LP for x in w):
                return j
        return None

    def gcd_alternative(w):
        for i in range(K):
            g = L
            for j in range(K):
                if j != i:
                    g = gcd(g, w[j])
            if g > 1:
                return True
        return False

    special_ok = True
    random_ok = True
    tried = 0
    state = 20261003
    for tup, (digits, _, _) in sorted(mine14.items()):
        if digits is None:
            special_ok = False
            continue
        w = [tup[i] + digits[i] * 2 * P for i in range(K)]
        if witness(w) is not None or not gcd_alternative(w) or any(x % 7 for x in w):
            special_ok = False
        for _ in range(300):                       # other completions, pseudo-random digits
            d = []
            for i in range(K):
                state = (state * 6364136223846793005 + 1442695040888963407) % (1 << 64)
                d.append((state >> 33) % 7)
            if tuple(d) == digits:
                continue
            tried += 1
            if witness([tup[i] + d[i] * 2 * P for i in range(K)]) is None:
                random_ok = False
    check("each witness-free completion has no witness among all 1162 times, has every coordinate divisible "
          "by 7, and is proper by alternative (a)", special_ok)
    check(f"{tried} other level-14 lifts drawn pseudo-randomly: every one has a witness", random_ok)

    print(f"RESULT: {'every comparison agrees' if ok else 'SOME COMPARISON DIFFERS'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
```

</details>

<details>
<summary>pt004_l3c_run.sh</summary>

```sh
#!/bin/sh
# TOGETHER - PROOF TABLE 004 - Round 3 - Turn 11 - item L3-C (prime gate p = 83) - Fable-A
# Every command of the turn, in order.  Needs: a C compiler (cc), python3.  No network.
# Usage:  sh pt004_l3c_run.sh [ARCHIVE_DIR]
#   ARCHIVE_DIR (optional) = folder holding p83/ and certificates_p83/ taken from
#   fourteen_lonely_runners_package.zip of Zenodo record 22066772 (small_gates/).
#   Without it the comparison with the archive is skipped; everything else still runs.
set -e
step() { echo "== $1"; }

step "build";                         cc -O2 -std=c11 -o pt004_l3c pt004_l3c.c
step "stage 1: tiny cases";           python3 pt004_l3c_tests.py > stage1_tests.out
step "level one, p = 43 (extra)";     ./pt004_l3c level1 43 13 level1_p43.txt > level1_p43.log
step "stage 2: level one, p = 83";    ./pt004_l3c level1 83 13 level1_p83.txt > level1_p83.log
step "second implementation, p = 43"; python3 pt004_l3c_level1_check.py 43 13 level1_p43.txt > level1_check_p43.out
step "second implementation, p = 83"; python3 pt004_l3c_level1_check.py 83 13 level1_p83.txt > level1_check_p83.out
step "stage 3: lifts 2..32 and 14";   ./pt004_l3c cascade 83 13 level1_p83.txt cascade_p83.txt > cascade_p83.log
if [ -n "$1" ]; then
  step "comparison with the archive"
  python3 pt004_l3c_compare.py level1_p83.txt cascade_p83.txt cascade_p83.log "$1" > compare_p83.out
else
  echo "== comparison with the archive skipped (no ARCHIVE_DIR given)"
fi
step "sha256 of the outputs"
sha256sum stage1_tests.out level1_p43.log level1_p43.txt level1_p83.log level1_p83.txt \
          level1_check_p43.out level1_check_p83.out cascade_p83.log cascade_p83.txt
[ -f compare_p83.out ] && sha256sum compare_p83.out
echo "== all steps finished"
```

</details>

## 4. CHECK

1. Check the hashes of the five program files against §3.8.
2. Read them (R12). The C file reads one orbit file and writes one output file, both named on the command line; the Python files read the files named on the command line and write nothing; `pt004_l3c_tests.py` runs `./pt004_l3c`. No network anywhere.
3. On a machine with a C compiler and Python 3, run the two commands of §3.9. Expected: exit code 0, about 3 minutes on a machine like mine, and the ten output hashes of §3.8. `compare_p83.out` must end with `RESULT: every comparison agrees`.
4. Without the archive data: `sh pt004_l3c_run.sh` runs everything except the comparison; the first nine hashes must still match.
5. For the KEY comparison with T12: the quantities that do not depend on my file format are the 115,903 orbits, their split (41,552 / 49,847 / 24,504), the level counts of §3.6, and the nine level-14 completions. My list uses the smallest sorted tuple as the orbit representative.

## 5. STATUS CLAIM

OPEN

## 6. NEXT

1. My runs are on one machine (three runs, identical outputs). A non-author reads the five files (R12), then Puck re-runs with the commands of §3.9 and compares the ten hashes (R16).
2. When Puck releases T11 and T12 together: compare the independent result with the quantities in CHECK 5.
3. L3-R can attack the completeness of my level-one search and the two reductions in the lift (§3.7), and the limits listed at the end of §3.6.

## Independence: account records read

- **This turn:** none. I did not search or read any other chat and did not read any memory file.
- On the wall I saw line 23 (T12 was returned INCOMPLETE and reassigned). I have seen no L3-C work by any other seat.
- As before, the system places a short profile of Tuzi and a list of memory file names in front of me on every turn; it contains no mathematics.

```
END PT004-R3-T11-FABLE-A
```
