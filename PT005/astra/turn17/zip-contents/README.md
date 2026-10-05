# PT005 · Astra · Composite shift at the existing binary levels

SEAT: Astra (thinking seat; own exploratory computation additionally labelled TEST Astra)
REPLY_TO: chair note 22 and PT005-ASTRA-SHIFT-PACKET
STATUS: mathematical derivation for review; two-row computation OPEN pending another seat's independent check
TIME: the precise package build time is in BUILD-INFO.txt, obtained from the execution clock.
The courier's timestamp correction is accepted: the input packet was pushed at 2026-10-04T22:18:55+08:00.
Account records read: this conversation and its attached packet only. No other chats searched or read. The public PT005 wall was read earlier in this conversation. This run used the packet and public primary sources.

## Summary

The prime-denominator shift lemma extends to k=15 and needs LRC(m) only for m<=13, not m=14. More usefully, primality is unnecessary if the grid size is computed separately for each exceptional speed. Divisors 4 and 8 of the existing levels give a sufficient certificate. A separately written exact lifting program reproduced all ten counts for the two quoted rows. Every survivor at level 16 in those two fibers passes the divisor-8 criterion. This is not a completed gate for p=131 or an independently checked proof of 16 runners.

## Sources actually read

- https://arxiv.org/html/2609.02604v2 (HTML retrieved directly; the search-service open endpoint failed).
- https://zenodo.org/api/records/22667683 (record and file list).
- https://zenodo.org/api/records/22667683/files/fifteen_runners_manuscript_source.zip/content (downloaded and read paper_v2.tex).
- In paper_v2.tex: lem:neargcd, its proof and following paragraph; lem:gate and its proof; the definition of properness; sec:pipeline. The archive title is *Fifteen lonely runners: manuscript, gate certificates, and audit code*. Its manuscript title/section numbering differs from the combined arXiv HTML, so the exact TeX labels identify what was read.
- Downloaded source zip SHA-256: 54e0fa471c103e4b26f7e8d940bb7552de65a6d69bd7ac9d6256133eb0af10f6.
- Extracted paper_v2.tex SHA-256: 5c4ade983f6d2fe0c89fd5a328e19004a1e23981a957786e6768d826a78cbcd3.

These sources supply the original shift argument and gate framework. The composite-denominator calculation below is this seat's derivation. No novelty claim is made. External LRC results are assumed, not independently reproved here.

## Q1 · Prime-denominator k=15 lemma (FACT: derivation)

Let u_1,...,u_15 be positive integers, d a prime, E={i:d does not divide u_i}, e=|E|, and m_d=ceil(d/8). Assume LRC(m) for all 1<=m<=13. If 2<=e and e*m_d<d, then some rational t satisfies ||t*u_i||>=1/16 for all i. Distinctness and primitivity are not required for this lemma.

Proof. Let B be the divisible speeds. After repetitions are removed it has m<=15-e<=13 distinct values. The hypotheses imply e<8, so B is nonempty. LRC(m) gives a time t_* at which all speeds in B have distance >=1/(m+1)>=1/14>1/16. Continuity and this strict margin allow a rational t_0 with all those distances still >1/16. For q=0,...,d-1, the shifts t_0+q/d preserve B modulo one. For an exceptional speed, coprimality gives a full d-point grid. Its bad arc is open and has length 2/16=1/8, containing at most ceil(d/8) points. A union bound excludes at most e*m_d<d shifts. One remaining rational shift works. Boundary distance exactly 1/16 is good.

Thus d=2 provides no case with e>=2; d=3 permits e=2 (at least 13 divisible speeds); d=5 permits e=2,3,4 (at least 11 divisible speeds). The full prime-divisibility criterion lem:gate for k=15 still separately assumes LRC(m) for m<15, including LRC(14), i.e. the author's fifteen-runner result. Do not confuse that dependency with the weaker input of this shift lemma.

## Q2 · Composite-denominator lemma (FACT: derivation)

Let D>=2 be any integer, B={i:D divides u_i}, E its complement, e>=2. For i in E set g_i=gcd(D,u_i), D_i=D/g_i. Assume LRC(m), 1<=m<=13, and

    S_D = sum_{i in E} g_i * ceil(D_i/8) < D.

Then every u_i is simultaneously at distance >=1/16 at some rational time.

Proof. Each summand is at least D/8, so the displayed inequality implies e<8 and B is nonempty. Choose rational t_0 good for B exactly as in Q1. As q runs through 0,...,D-1, the exceptional coordinate visits D_i distinct equally spaced points, each g_i times. At most ceil(D_i/8) distinct points lie in the open bad arc, so that coordinate forbids at most g_i*ceil(D_i/8) shift indices. Their union has size at most S_D<D. This proves the claim.

For D=8, write (a,b,c,z) for the counts of coordinates respectively odd, 2 mod 4, 4 mod 8, and 0 mod 8. Then S_8=a+2b+4c. The certificate is simply a+2b+4c<8 (with e>=2).

In particular, an improper lift at a binary level has at least two odd coordinates, since otherwise it satisfies the gcd condition. If at least twelve of its fifteen coordinates are divisible by 8, it has at most three exceptions. Two odd exceptions forbid at most two shifts, and the possible third exception at most four. Hence S_8<=6<8. This handles the class with no new level and uses only LRC up to thirteen speeds.

For D=4, writing a=#odd and b=#(2 mod 4), the sufficient test is a+2b<4. It covers additional cases; failure of any sufficient test is not a counterexample.

Uniformity: at level L=16 or 32, D=4 or 8 divides L*p. Divisibility and gcd(D,u_i) are identical for every integer vector congruent to the lift modulo L*p. Therefore a passing residue vector certifies ALL positive integer speed vectors in its class. The rational time may depend on the actual speeds. This is the third alternative in lem:gate(ii); it does NOT change the definition of properness or assert the grid fiber is empty.

## Q3 · What the two rows actually show (FACT: own exploratory computation)

shift_check.cpp was written for this task without reading or importing the author's lifting code. It starts with the two rows quoted in the packet and enumerates full fibers at levels 2,4,8,16,32, with exact integer distance tests and the binary-level gcd condition. run-output.txt is the output. The ten counts match the packet:

| row | level 2 | level 4 | level 8 | level 16 | level 32 |
|---|---:|---:|---:|---:|---:|
| A: last coordinate 1 | 24 | 344 | 1888 | 8576 | 67072 |
| B: last coordinate 2 | 21 | 252 | 1584 | 12480 | 99072 |

All their level-16 survivors have exactly one of the following signatures:

| (odd,2mod4,4mod8,0mod8) | row A | row B | S_8 |
|---|---:|---:|---:|
| (2,0,0,13) | 1920 | 2496 | 2 |
| (2,0,1,12) | 1536 | 2304 | 6 |
| (2,1,0,12) | 3072 | 4608 | 4 |
| (3,0,0,12) | 2048 | 3072 | 3 |
| total | 8576 | 12480 | all <8 |

Both fibers are therefore entirely covered at level 16 by the composite shift lemma, conditional on correctness of this enumeration and the stated LRC input. At level 32 every surviving lift also passes. This is a fresh single-seat implementation, NOT independent mathematical/code review or Lean verification. Its experimental status remains OPEN until another seat checks it.

The counts do not say twelve coordinates are always divisible by the FULL level: at level 16 each row has 768 lifts with only eleven coordinates divisible by 16. Nevertheless, all have at least twelve divisible by 8. Merely reading growth near 8 as three free coordinates would miss this distinction. The exact ratios are 67072/8576 and 99072/12480, approximately 7.821 and 7.938, not exactly eight.

There is a concrete explanation for much of that growth. The twelve distinct classes C={1,2,8,11,18,38,40,46,47,48,56,58} cover all 65 time classes at p=131 under 16*d_p(a*r)<131. The small Python check verifies this. Thus tau_15(131)<=12; the incidence count alone would not prove it, and equality is not asserted. Across index subsets of A and B, cover histograms are respectively {12:4,13:6,14:4,15:1} and {12:6,13:9,14:5,15:1}.

For any binary level L, set the twelve coordinates of such a covering core to 0 mod L, using CRT with their fixed residues mod p. On the L*p grid they still cover every time, because division by L rotates the p-time classes by a unit. The remaining three coordinates are free modulo L. Choose at least two odd, making the lift gcd-improper. This constructs nonempty improper fibers at arbitrarily high binary levels for these rows. It is compatible with the continuous-time shift certificate: a good rational time need not be on the L*p grid. This argument concerns the displayed rows and powers of two, not all lifting levels or all other rows.

There is no evidence here that d=3 at 48, or d=5 at 80, handles any particular remaining class. Those routes require divisibility data at those moduli and their own complete enumeration. Neither is needed for the two tested level-16 fibers. The other 328 printed rows and unsampled rows are not covered by these measurements.

## Q4 · Distinct speeds do not license deleting repeated residues (FACT)

Actual speeds u_i=w and u_j=w+L*p can be distinct while having the same residue modulo L*p. In particular, the three positions of a repeated mod-p class need not have different lifting digits at any fixed finite level. Deleting equal residue coordinates or requiring unequal digits would lose permitted vectors. The composite shift lemma avoids this invalid inference entirely: it is valid with or without repetitions.

## Q5 · First cheap test (IDEA / proposed next action)

1. Review the proof above and rerun the provided program for the two quoted rows; compare counts and full valuation signatures, not only a success label.
2. In the chair's existing level-16 output loop, compute a,b,c for EVERY remaining improper lift and test a+2b+4c<8. Optionally also use D=4,16,32 when D divides the current level. No new lifting level is required. Save counts and the first failures, including their full vectors and 2-adic signatures.
3. Apply this first to the preserved 330-row sample, then to every row of the complete gate computation. Sampling is not a gate certificate. Keep distinct counters: improper_by_definition, certified_by_shift, unresolved. Do not claim J(15,131) is empty merely because unresolved becomes zero.

The cheap part is adding an O(15) divisibility check per already-generated survivor; this does not remove the cost of generating all relevant rows/lifts. Nor does a successful p=131 test prove scenario S for the other small primes or its estimated budget.

## Q6 · What would prove the proposed closure wrong

- A reproducible discrepancy in the complete two-row fiber lists or histograms defeats the reported computational coverage, even if a total count happens to match.
- One level-16 survivor from those two rows with S_8>=8 defeats the universal D=8 coverage statement for them; it does not refute the sufficient lemma.
- An unhandled survivor in another row defeats extrapolation to the whole p=131 gate. Preserve it as the next mathematical target.
- Using a D not dividing L*p destroys the class-uniformity justification unless a new argument is supplied.
- A flaw in the per-coordinate grid count, union bound, or LRC input defeats the mathematical certificate; none is bypassed by model agreement or matching computations.

VERDICT: composite-shift derivation HOLDS subject to the stated smaller-LRC input (HAND-CHECKED by Astra); two-row experimental coverage OPEN pending independent rerun/review; full p=131 gate INCOMPLETE; scenario-S budget not established.

## Reproduction

    g++ -O3 -std=c++17 shift_check.cpp -o shift_check
    ./shift_check > fresh-output.txt
    python3 cover_and_shift.py

Environment of this run: g++ (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0. Timing fields are observations of this run and will vary. Compare integer counts/signatures after ignoring seconds.

Enumeration argument: every parent has 2^15 children. For each odd grid numerator the child bits satisfying all fifteen good-distance conditions form a subcube; the program removes exactly that subcube. Even numerators reduce to an already rejected parent grid; numerator M-T is equivalent by distance symmetry. At level 2 the gcd condition is checked explicitly. At later binary levels parity is unchanged and the parent already has at least two odd coordinates. The initial rows have no p-grid witness by the separate cover calculation. Thus the intended invariant is the full improper fiber, with no unit quotient or deduplication of coordinate positions.

Implementation sanity checks: an intentionally different direct full-grid loop compares the ENTIRE level-2 set over all 32768 children for each row. At levels 16 and 32 it directly checks 128 evenly spaced survivors in each fiber, including nonunit grid numerators. These spotchecks do not independently prove completeness of the higher-level enumeration. Complete independent reimplementation/inspection remains necessary under table rules.
