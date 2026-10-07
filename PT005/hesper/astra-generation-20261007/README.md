# PT005 — direct proof of level-2 exception completeness

SEAT: Astra
REPLY_TO: PT005-BRAINSTORM-GENERATION, chair Opus, 2026-10-06 22:03 +08
STATUS: IDEA plus local finite encoding checks; no UNSAT certificate obtained.
SCOPE: p = 401, the irredundant branch. This is not a proof that the entire prime gate closes.
RECORDS: The packet and its five-row attachment, definitions already supplied in this conversation, and locally available self-authored checking code. No web search and no other chats/account records were read.

## Main proposal

Instead of generating every coarse cover and then testing its lifts, encode the existence of an irredundant level-2 survivor outside five known orbits. The input has 600 Boolean variables and 1,177 pseudo-Boolean constraints. A checked UNSAT proof would establish that the five orbits exhaust this branch. Their further lifts are small enough to check directly.

The five exceptions are not assumed complete. The missing certificate is exactly what would establish their completeness. The reducible branch still requires its own complete check. Smaller input is not a claim of smaller proof or faster search.

Main solver input: p401-level2-ir-except-five.opb
Base positive-control input: p401-level2-ir-base.opb
Generator and seed checks: level2_exceptions.py
Seed orbits: p401-level2-exceptions.json
Finite lift checker: five_rows.cpp
Observed results: five-rows-output.txt and level2-milp-scout.json

## Exact model and equivalence argument

Let p = 401, M = 802, N = 200. Write d_m(a) = min(r,m-r), where r is a mod m. A grid time T/M is bad for a coordinate u exactly when 16*d_M(T*u) < M. Equality is good.

The model is restricted to coarse covers whose 15 classes are all necessary. Such a row has 15 distinct classes modulo p up to sign: any repeated class would be removable. The restriction is intentional and does not cover the reducible branch.

For each signed residue u = 1,...,400 use a Boolean x_u. The partner of u in the same coarse class is p-u. For c = 1,...,200 put z_c = x_c + x_(p-c).

1. Select exactly 15 coordinates: sum x_u = 15.
2. Require z_c <= 1 for every c.
3. Require at least two selected odd u. For the power-of-two level 2 this is exactly failure of the paper's gcd properness condition.
4. Set x_1 = 1. This loses no orbit: an odd selected coordinate is a unit modulo 802, so multiply every coordinate by its inverse, then independently change signs and sort. Multiplication by this unit permutes grid times, preserves parity, and preserves the coarse covering relation and irredundancy.
5. For each nontrivial time impose sum_{u:16*d_802(T*u)<802} x_u >= 1. Times T and 802-T have identical distances. Because x_1=1 already blocks T=1,...,50, retain only T=51,...,401. T=0 is automatically bad. There are 351 retained time inequalities.

The use of d_m implements the directed covering relation directly. No symmetrization of the discrete-log shape S into S union -S is introduced.

Irredundancy needs only 200 auxiliary Boolean variables q_t. Define

A_tc = 1 if 16*d_401(t*c) < 401, and 0 otherwise;
h_t = sum_c A_tc*z_c, for t = 1,...,200.

Impose, for every t:
    h_t >= 1;
    h_t + 14*q_t <= 15.

For every c impose:
    sum_{t:A_tc=1} q_t >= z_c.

If q_t=1, these inequalities force h_t=1. Thus q_t can certify a private time. Each selected class must own at least one flagged private time; therefore it is indispensable. Conversely every irredundant cover has a private time for each selected class and satisfies these inequalities by flagging all times with h_t=1. This proves the auxiliary encoding is exact, not a heuristic restriction.

The explicit h_t>=1 constraints are redundant with full level-2 grid coverage, but make the coarse semantics inspectable.

Constraint count before exception blocks:
- exact cardinality: 2
- odd count and normalization: 2
- paired-class exclusions: 200
- retained grid times: 351
- h_t lower bounds and q_t implications: 400
- private witness requirements: 200
Total: 1,155.

## Excluding five orbits without assuming completeness

The local lift check found exactly one improper level-2 lift for each of the five supplied coarse rows. The seeds are recorded in level2_exceptions.py and the output log.

For every odd coordinate a of each seed, multiply the entire seed by a^(-1) modulo 802, take its signed representatives 1,...,400, and sort. Deduplicate the resulting sets E. There are respectively 8,8,2,2,2 normalizations, and 22 distinct sets overall.

These are ALL members of those orbits satisfying x_1=1: any unit that sends a coordinate to +/-1 is +/- its inverse, and the two choices give the same signed set.

For each such 15-set E add:
    sum_{u in E} x_u <= 14.

Because exactly 15 coordinates are selected, this excludes precisely E. It cannot accidentally exclude a different 15-set. The final formula has 1,177 constraints.

A SAT assignment would be another normalized irredundant level-2 survivor, subject to direct checking. It would not be a counterexample to the continuous Lonely Runner Conjecture.
A checked UNSAT proof would show that the five listed orbits are complete for this branch.
An UNKNOWN or time limit establishes neither statement.

## Local finite checks actually completed

Two differently organized algorithms were compared:
- a bit-cube lift routine tests sets of child choices using odd grid numerators;
- direct_improper enumerates every grid numerator for an individual child using integer arithmetic.

At every stage, all 2^15 children of every surviving parent were checked, and the complete surviving sets were compared. This includes stage 16's empty result; it is not merely a check of reported survivors. Across the five rows the number of individually checked child tuples is 524,288. Both routines were assembled by Astra in this environment; this is algorithmic cross-checking, not independent external authorship.

| Attached row order | Level 2 | Level 4 | Level 8 | Level 16 | Odd coordinates in its level-2 survivor |
|---|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 4 | 0 | 8 |
| 2 | 1 | 0 | 0 | 0 | 8 |
| 3 | 1 | 0 | 0 | 0 | 2 |
| 4 | 1 | 0 | 0 | 0 | 2 |
| 5 | 1 | 0 | 0 | 0 | 2 |

Every one of the 22 normalized seeds satisfies the base OPB formula and is rejected by exactly its own exception-block inequality. No constraint restricts unknown survivors to having 2 or 8 odd coordinates.

These checks establish only facts about the supplied five rows, their orbits, and the encoding controls. They do not certify absence of a sixth orbit.

A bounded SciPy/HiGHS integer-programming scout on the final formula ran for 45 seconds and reached its time limit without an incumbent. The recorded result is INCONCLUSIVE. That interface produced no independently checkable infeasibility proof. No proof-logging SAT/PB solver or proof checker was installed here, and none was fetched.

## A concrete obstruction to an LP-only proof

The LP relaxation of this very 600-variable model is feasible, even with all 22 exception blocks:

    x_1 = 1;
    x_400 = 0;
    all other x_u = 7/199;
    every q_t = 1/2.

level2_exceptions.py checks this exactly with common denominator 398 against every generated inequality, including bounds 0<=variable<=1.

Therefore a dual infeasibility certificate for the unstrengthened LP cannot prove this integer formula UNSAT. The search must use Boolean/integer reasoning. This does not exclude stronger valid cuts with checked derivations, branch proofs, or other integer proof systems.

## One cheap test for the chair

Use the fixed p401-level2-ir-except-five.opb with a proof-logging pseudo-Boolean solver, or a checked CNF translation plus a proof-logging SAT solver. Do not rerun level-one generation.

Budget suggestion: 5 minutes for controls and setup, at most 35 minutes solver time, and at most 15 minutes independent proof checking. Stop inside 55 minutes. If a suitable tool is unavailable or checking does not finish, report UNKNOWN rather than enlarging the budget in this test.

Retain: exact input, solver/version/options, full proof, independently checked result, peak memory, times, byte counts, and hashes. Check the proof against the fixed formula and separately check its mathematical encoding. check_model.py in this package checks encodings; it is NOT a proof checker.

Interpretation:
- Valid SAT outside the 22 normalized seeds: the proposed five-orbit completeness claim fails. Inspect the new orbit, not the LRC conclusion.
- Verified UNSAT: exception completeness established for the irredundant level-2 branch. Combine with checked lifting of the five exceptions and separately checked coverage of the reducible branch before any gate claim.
- Timeout/no checked proof: this cheap test did not show a speedup.
- A proof that is huge or slow to check may defeat the practical purpose even if valid.

Success at p=401 does not justify assuming five exceptions, the same exceptions, or a bounded number of exceptions at any other prime.

## Secondary D2 correction: the raw formula can be SAT at a closed small-prime gate

The full level-16 model is supplied as a secondary experiment, not the recommended first test.

For a prime with a 13-class coarse cover C, the residues 16*C plus two odd coordinates have no grid-good time modulo 16p: the 16*C coordinates already block every time not divisible by p, and block multiples of p as well. They can still be disposed of by the composite shift lemma L7, with D=4.

Consequently the raw request "15 speeds, no good grid time, at least two odd" need not be UNSAT merely because the gate was closed using L7. This affects primes with such cores, including the packet's small-prime examples. The positive control here is at p=233:
C = [1,7,10,12,31,32,43,45,50,65,85,91,110].
Take 16*C + [1,1]. Repeated modular residues are allowed: actual distinct speeds could use 1 and 1+16p instead.

The full residual encoding excludes already handled L7 families. Let A,B,C,D count residues that are respectively odd, 2 modulo 4, 4 modulo 8, 8 modulo 16. Necessary failure conditions for the D=4,8,16 shift tests are:
    A + 2B >= 4;
    A + 2B + 4C >= 8;
    2A + 2B + 4C + 8D >= 16.

These follow from the shift-grid bound for each exceptional coordinate u:
    gcd(u,D) * ceil((D/gcd(u,D))/8).
A strict sum below D guarantees a free shift. Because at least two coordinates are odd, the divisible block has at most 13 coordinates. This use of L7 depends on the previously supplied lower-speed LRC input and the validity of that shift argument. It is not re-proved by the OPB solver.

In the full model, each signed residue has multiplicity 0,...,15 represented by four Boolean bits and one presence bit. Repeated residues are NOT removed. Normalizing one odd coordinate to 1 and identifying signs are valid unit symmetries.

File names:
- p17-residual.opb: positive satisfiability control.
- p233-raw.opb: forced-family positive satisfiability control.
- p233-residual.opb: same family rejected by L7-failure constraints.
- p239-residual.opb and p401-residual.opb: unhandled full-grid inputs, not solved.

check_model.py independently regenerates each bad-residue set via modular inverses rather than the builder's direct multiplication. It verifies the supplied encodings and exact assignments. run_checks.py reproduces these controls.

The full models also have exact fractional feasible assignments, so an LP-only certificate is insufficient there too:
m_1=m_2=m_3=m_4=m_8=1; m_(16v)=10/N for v=1,...,N; all other multiplicities zero. At p=239 and p=401, the contribution of the divisible-by-16 residues is already at least one at every grid time. Details are checked exactly in the code.

## Reproduce

Run from this folder with Python 3 and g++:

    python3 run_checks.py
    g++ -O3 -std=c++17 five_rows.cpp -o /tmp/pt005-five-rows
    /tmp/pt005-five-rows

The encoding checks use the standard library. Optional try_milp.py uses SciPy; it is a scouting tool and cannot supply the required proof certificate.

SHA256SUMS records the preserved package files; generated outputs with elapsed timings need not be byte-identical when rerun. Original logs are preserved in this package.

## What would refute or defeat the proposal

- A valid irredundant survivor has no assignment after normalization: encoding or symmetry argument is wrong.
- A block removes a non-equivalent orbit: symmetry exclusion is wrong.
- A directly verified model outside the five orbits: five-orbit completeness is false.
- A proof cannot be verified against the fixed input: no certified result.
- The bounded experiment cannot deliver a manageable independently checked proof: no practical improvement established. This is not a proof that every solver-based route must fail.

No general structural classification, asymptotic speedup, new LRC theorem, or complete prime gate is claimed in this package.

