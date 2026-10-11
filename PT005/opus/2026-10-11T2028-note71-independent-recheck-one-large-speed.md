# PT005 · Chair note 71 · Independent re-check: the C-floor holds whenever at most one speed exceeds 30

From: Opus (chair) · 2026-10-11 20:28 +0800 (machine clock) · Requested by Tuzi 20:21 ("另一台引擎独立重跑")
Engine: PT005/opus/guess_r16/oneLarge.c (sha256 prefix d9c7897727721cd3). Written from scratch by the chair. It shares no code with Kimi, Astra or GPT.

## Method

**Arithmetic.** All arithmetic is exact integer arithmetic.
- The unit is 1/L, with L = 16·lcm(1..30) = 37,265,433,004,800.
- Every safe-interval endpoint (16j ± 1)/(16k), for k ≤ 30, is an integer in this unit.
- Losses from a new speed v are computed in units of 1/(L·v), using 128-bit integers.

**Enumeration.**
- (i) Every 14-subset of {1..30}.
- (ii) Every 13-subset K′ of {1..30}, combined with every v ≥ 31.

**Infinite tail.** This uses the R16 Q1 per-interval bound (GPT, Astra), loss ≤ min(len, len/8 + 7/(64v)).
- The bound is proved: the primitive of 1_B − 1/8 oscillates by exactly 7/(64v).
- It is non-increasing in v.
- So once it certifies some V, it certifies every v ≥ V. Every v below that V is checked exactly.
- A shortcut: if m(K′) − 1/8 ≥ 97/6864, the set passes for every v, because the loss is never more than 1/8.

**Self-checks.**
- 301 random (K′, v) cases (seed 20261011), plus Kimi's worst case, were compared with an independent Python `Fraction` computation.
- This was done for both the max-24 and the max-30 builds: 0 mismatches each.

## Results (fails = 0 everywhere)

| Class | Sets | Exact v-checks | Minimum | Where |
|---|---|---|---|---|
| 14-subsets of {1..24} | 1,961,256 = C(24,14) | n/a | 97/6864 | K* = {1..15}∖{6} |
| 13-subsets of {1..24}, plus any v ≥ 25 | 2,496,144 = C(24,13) | 1,064,594 | 14867/960960 | K*∖{14}, plus v = 56 |
| 14-subsets of {1..30} | 145,422,675 = C(30,14) | n/a | 97/6864 | K* and 2K* (2K* = K* scaled by 2) |
| 13-subsets of {1..30}, plus any v ≥ 31 | 119,759,850 = C(30,13) | 27,170,182 | 14867/960960 | K*∖{14} + 56, and its double |

- Wall time for the whole run was about 1.5 minutes on 2 cores.
- The first run missed 8,568 + 3,060 sets whose smallest speed is ≥ 13, because of a loop cap. This was fixed and those sets were run. The counts above match C(30,13) and C(30,14) exactly.

## Status

**FACT (chair engine, independent of the seats).** Every 14-set K with **at most one speed > 30** satisfies m(K) ≥ 97/6864.
- Within that class, equality holds only at K* and its scaling 2K*.

What this confirms:
- Kimi's R16 claim (at most one speed > 24): confirmed, and extended to 30.
- Astra's claim (all 13-subsets of {1..30} with speed 31 added): covered as a special case. The chair did not separately print the minimum at v = 31 alone.
- GPT, Kimi and Hesper's worst case 14867/960960 (K*∖{14}, plus speed 56): reproduced.
- The earlier seat claims "max ≤ 26/28/30, unique minimum K*": now also re-run by the chair (max ≤ 30).

**Still OPEN.** The C-floor for 14-sets with **two or more speeds > 30**.

**Ledger.** This is a candidate L18, to be proposed to Tuzi with the one-large-speed inequality. It is not written into the ledger without her approval.

**Office PC.** It is not needed for this. The Astra-scale job (about 1.2 × 10⁸ sets) ran here in about 1.5 minutes.
