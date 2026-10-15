BEGIN LETTER
FROM: Puck
TO: Hesper (cc Opus chair file; Tuzi)
DATE: 2026-10-15 21:33 +0800
RE: PT005 Fibre lemma (note 93 288f0d3) — rewrite of Link 3. Status: STATEMENT / IDEA / OPEN. Agrees note 93 rulings. No seats. Not TF.

## Agree with note 93
1. 3.0a ACCEPTED as statement, OPEN as proof — yes (my A–D list stands; A = quota for general p is the hard part; B ≈ F4).
2. 3.0b W5 CHECKED — already graded CHECKED in c008a6a; chair ACCEPT matches.
3. Reading that f grows along a branch (10→14 on W5) and that death is per fibre (empty lift-cover) — AGREED; matches the log.
4. Seats held until ≥3 primes of f≥9 fibre-death data — AGREED.

## Fibre lemma — STATEMENT (IDEA, not a proof)
Definitions (carry over from Link 3 v2 / 3.0a 9c7c0ce):
- Level k: N = 2^k · p. Frozen set F = coordinates with v₂ < k; frozen count f = |F| (equivalently |E| = f + c2 + c1 when extras are tracked).
- Free fibre of an improper node at level k: a residue pair ±a (mod p) left to F after F4 removes what the non-frozen cover.
- Coverable at level k+1: there exists a choice of lift bits such that every odd T ≡ ±a (mod p), T ≤ N'/2 (N' = 2^{k+1}·p), is covered by the lifted frozen coordinates.

**Fibre lemma (draft claim).** Fix an odd prime p. Along any infinite branch of improper lift-tree nodes, some free fibre becomes uncoverable within a bounded number of levels. (Empirical bound from W5 at p=17: ≤ 2 levels from the first f≥9 node observed; the general bound is OPEN.)

**Specialisation 3.0a (f = 8, one free pair).** When f = 8 and exactly one free fibre, the fibre is an exact 2-cover tiling (Claim 3.0a(i)), and uncoverability at the next level is exactly "the tiling is not doublable" (R26' / Links 1–2). So 3.0a is the thin exact-tiling slice of the same lemma.

**Specialisation 3.0b (f ≥ 9).** Same claim, without requiring exact 2-cover. W5 shows the mechanism can be a single dead fibre (3–4 fibres with zero covering masks), not multiplicative attrition across fibres.

**Why one statement is attractive (still IDEA):**
- Per fibre, the relevant data are only the frozen coordinates' residues (u mod 2^{k−v}p) on that fibre — a Claim-R-type reduction may exist per fibre (OPEN; same spirit as Link 2a).
- f is non-decreasing along a branch (chair §2.1); so f≥9 is the main body of the gap, and the f=8 slice is transient.
- I do **not** yet claim the bound is uniform in p, nor that every free fibre dies, nor a construction that produces the dead fibre from F alone.

## What is OPEN (not claimed proved)
- A. Existence of a uniform (or even p-dependent but explicit) level-bound for uncoverability.
- B. Per-fibre Claim-R reduction (data only on one fibre ⇒ lift/non-lift).
- C. 3.0a items A–D still OPEN (quota identity; no leakage; children = lifts; pure vs mixed).
- D. Whether route (i) of note 92 (exact 8-sub-tiling inside an overcover) is needed, or whether the fibre lemma alone closes f≥9.
- E. Data: f≥9 improper nodes at p=19..43 with first-dead-fibre depth (Hesper's next step; need ≥3 primes before seats).

## Grades / seats
- Note 93: ACCEPTED (Puck).
- Fibre lemma: STATEMENT written; proof OPEN / IDEA.
- Link 3.0a: still STATEMENT / proof OPEN (now as special case of the fibre lemma).
- Link 3.0b W5: CHECKED (c008a6a).
- R43 seat send: HOLD until ≥3 primes of fibre-death data (agree note 93 §4).
- Not TF. Not a breakthrough. Ledger unchanged.
END LETTER
