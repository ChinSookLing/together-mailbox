BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 08:12 +08
RE: 猜公式 Round 6 (packet 6f1e734), send text r6_send_kimi-fixed.txt
SEAT: kimi-fixed
MODEL: K3 High (composer; no per-reply label), Used 15 tools
CHAT: https://www.kimi.ai/chat/1a1231e4-7012-87e0-8000-09ce1972343a

--- reply verbatim ---
[Hesper correction: replaces eddfbdb, whose reply section wrongly began with a stray copy of a capture note. Text below is the verbatim reply.]

All the pieces are in place. Writing the reply.

**ANSWER BLOCK**

**Q1.** PROOF (window containment): speed v covers cells with |vt − ip| ≤ H. If g = gcd(i,v) > 1, that window is strictly inside the window of v/g at (i/g)·p/(v/g) (radius g·H/v vs H/v). So a composite speed's only *new* cells are its windows at coprime positions ip/v. FACT: 12 has divisors 2,3,4,6 absorbing positions p/6, p/4, p/3; its only new windows are p/12 and 5p/12 — the narrowest (width H/6) — and they sit inside the [7..13] band, so fillers always cover them more cheaply. FACT (measured marginal contribution inside {1..15}): lowest for 6, 12, 14, 15 (2–5 cells); highest for 1, 9, 11, 13 (11–15) — matching the counts, with 7's role positional (band backbone).

**Q2.** FACT: odd core {1,3,5,7,9,11,13} leaves ≈ 0.30n cells uncovered at every prime tested (45 at 307 → 74 at 499), needing 7 fillers. FACT: every 14-cover I can find at p ≤ 499 (all 19 census reps plus ~20 of my own covers spanning all 19 nonzero primes) has a scaling with ≥ 5 speeds ≤ 15 — no counterexample.

**Q3.** FACT: the run family (consecutive speeds near ±(p∓1)/k, any k ≤ 14, incl. the odd core = k = 2) yields 14-covers at exactly 307, 311, 313, 317, 331, 337, 353, 373, 457 — the abundant-cover primes plus 457. It finds none at the other 10 nonzero primes (347, 349, 359, 367, 379, 389, 401, 409, 419, 421): as a predictor it scores 23/33. UNFINISHED (stochastic search).

**Q4.** Rule: **p has a 14-cover ⟺ p has a 14-cover that, after some scaling, contains ≥ 5 speeds ≤ 15.** Score: 33/33 (verified positive side on all 19 nonzero primes; zero side inherits the census). Weaker crisp version — "odd core extends to a cover" — gets 22/33 (8 true positives).

**Reasoning**

FACT: I reproduced the 23 scalings and the frequency table exactly from Data 2.

PROOF (Q1 details): v's good cells are t with |vt − ip| ≤ H for some i ≤ v/2 (plus [1..H] for v = 1). If i and v share factor g, then |（v/g)t − (i/g)p| ≤ H/g < H, so the cell is already good for the divisor v/g, with g times wider margin. Hence new windows only at coprime i. Counting coprime i < v/2: 2,3,4,6 have 1; 5,8,10 have 2; 7,9,14 have 3; 11 has 5; 13 has 6; 12 has 2 but at width H/6 (narrowest) — 12 is dominated from two sides: most of its windows sit inside its divisors' wider windows, and its two survivors lie between p/13 and p/11, the densest part of the band that every core already tiles. FACT (numerical): within {1..15}, G(12) adds 3–5 cells at 347/379/401/457, the minimum; the hint's 2v-split is the g = 2 case.

IDEA (why [7..13] is the backbone): the first windows of v = 7..15 sit at p/v − H/v ∈ [1.07H, 2.14H] and overlap into a solid band starting right where speed 1 stops (H); windows of 2..6 and 12 fall on positions already tiled by this band's higher harmonics ip/v, so they enter covers only via variants (odds, APs), not the backbone.

FACT (Q3): k = 2 works for every p (run near p/2 ⟺ odd core); my seeded hill-climb completes it at 8 primes; k = 4 adds 457; offset odd core adds 317. Ten primes with rare covers (census ≤ 21) resist every run/AP core I tried — their covers need non-AP small cores (e.g., 347's [2,7,8,11,15]).

IDEA (Q4 reading): the small-core rule is Tuzi's hunch made testable: covers are built as a 5–9-speed small core tiling the band [H, 2.3H] plus 5–9 large fillers sniping the residual ~0.3n cells. If provable, existence reduces to a finite check of C(15,≥5) cores × filler feasibility — a candidate Terminal-Formula skeleton.

**Least-sure step:** the zero side of Q4 — I inherit the census's 0s; my engine can't prove non-existence, and my Round-5 off-by-one scare counsels humility. Second-least-sure: run-family negatives (stochastic search, could miss rare completions).
--- end verbatim ---
END LETTER
