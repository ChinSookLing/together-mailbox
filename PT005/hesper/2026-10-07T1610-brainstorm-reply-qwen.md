BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 16:10 +08
Subject: PT005-BRAINSTORM-GENERATION reply from Qwen, verbatim
Seat: Qwen, new chat https://chat.qwen.ai/c/ec06f029-49e1-48e7-b383-8861422b60be (title Large Prime Generation Proof), Qwen3.8-Max, Thinking ON, web off; final answer completed about 16:10 +08 after a very long Thinking phase (thinking text not included). Copied from the browser's page extract.
Sent: the packet BEGIN..END from PT005/opus/2026-10-06T2203-packet-brainstorm-large-prime-generation.md plus scouting/LR16/opus/p401_level2/README.md verbatim (message sha256 734b4d10...7505).
Courier only: no judgment of the maths. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
SEAT: Qwen3.8
REPLY_TO: PT005-BRAINSTORM-GENERATION
SUMMARY
D2/D4: replace row generation by a machine-checkable lower-bound certificate.
Encode “bad 15 speeds on the 16p grid” as a set-cover/IP with an oddness constraint.
Certificate: LP-dual weights or cutting-plane proof showing every cover needs >15 speeds.
Symmetry breaking: sign quotient, safe unit orbits, coarse/lift grouping, dominance cuts.
Cheap test p=223/239; kill if no checked proof in 1h or proof cost exceeds row search.
Records read: only the PT005 packet and scouting/LR16/opus/p401_level2/README.md. No web, no other chats, no paid compute.

THE IDEA
Direction: D2, with a D4 flavor: do not enumerate level-one rows; prove the final 16p covering problem UNSAT by a small, independently checkable certificate.

1. The final gate is a finite set-cover problem
Let M = 16p; T = Z_M be the fine time grid; V be the allowed candidate speed residues modulo M, excluding zero and using the exact engine convention for sign/lifts; odd(v) be 1 if the representative speed is odd; β(v,t) = 1 iff speed v blocks time t on the 16p grid, using the engine’s exact boundary rule.
For example, in the usual lonely-runner normalization this is the predicate that v t mod M lies in the forbidden arc of radius p around 0, but the certificate should use whatever predicate the engine already uses.
A “bad” final configuration is then a binary choice x_v ∈ {0,1} such that:
  ∑_v x_v = 15
  ∑_v odd(v) x_v ≥ 2
  ∑_{v : β(v,t)=1} x_v ≥ 1      for every t ∈ T
plus any required “at most one lift per coarse class” constraints if the model demands them.
FACT (conditional on the engine semantics): this is exactly the statement “there are 15 speeds mod 16p, at least two odd, with no good time on the 16p grid.” Therefore proving this integer program UNSAT proves the gate empty.

2. The clean certificate: an LP dual / weighted-time proof
The most compact certificate is a fractional packing of hard times.
Find rational numbers
  w_t ≥ 0   for times t ∈ T
  η ≥ 0     for the “at least two odd” constraint
such that for every candidate speed v,
  ∑_{t : β(v,t)=1} w_t  +  η · odd(v)  ≤  1          (C_v)
but
  W = ∑_t w_t + 2η  >  15.                           (W)
IDEA: such (w, η) is a direct proof that no bad 15-speed set exists.
Proof sketch:
For any candidate bad set V satisfying coverage and having at least two odd speeds,
  |V| = ∑_{v∈V} 1
      ≥ ∑_{v∈V} ( ∑_{t:β(v,t)=1} w_t + η·odd(v) )
      = ∑_t w_t · (# selected speeds blocking t) + η · (# odd selected speeds)
      ≥ ∑_t w_t + 2η
      = W
      > 15.
So any feasible bad set would need more than 15 speeds. Contradiction.
This is the “one formula” version of the bypass:
  Find w_t ≥ 0, η ≥ 0 such that
  ∀v: ∑_{t blocked by v} w_t + η·odd(v) ≤ 1,
  but ∑_t w_t + 2η > 15.
A tiny checker can verify it by summing the weights over each speed’s blocked-time set. No row list is needed.

3. If the pure LP dual is not strong enough: cutting-plane / PB proof
ESTIMATE: the pure LP may have optimum ≤ 15 even though the integer problem is UNSAT. That is normal. The fallback is to hand the same IP/PB instance to a pseudo-Boolean or SAT solver and request a proof:
  • OPB/PB format with a cutting-plane proof checked by something like VeriPB;
  • or CNF conversion with DRAT checked by drat-trim.
The instance can include:
  coverage constraints:      ∑_{v blocks t} x_v ≥ 1
  cardinality constraint:    ∑ x_v ≤ 15  (or = 15)
  oddness constraint:        ∑ odd(v)x_v ≥ 2
  coarse-class constraints:  ∑_lift x_{class,lift} ≤ 1, if needed
The solver’s proof file is then the certificate. It can be checked repeatedly by a small independent checker.
IDEA: use the LP dual weights, when available, to seed the PB solver or to generate warm-start cuts. Even if the LP alone does not exceed 15, its positive-weight times often identify the “hard” fine times that should appear in later cuts.

4. Symmetry breaking for p = 401
At p = 401, M = 6416. The raw fine problem is already small by laptop standards: a few thousand time constraints and a few thousand candidate speed/lift variables. The main issue is not raw size but combinatorial branching and certificate size. Useful symmetry breaking:
• Sign quotient. Usually β(v,t) = β(-v,t) = β(v,-t). Keep one representative from {v, -v} and/or identify t with -t, doubling orbit weights when needed. This halves the instance safely if the engine’s boundary convention is sign-symmetric.
• Coarse class / lift grouping. Instead of variables for all residues mod 16p, group by coarse class mod p and lift/parity. There are about p coarse classes and 16 lifts, so for p = 401 roughly 3200 lift variables after sign quotient. Add at-most-one-lift-per-class constraints if required.
• Safe unit orbits. If the exact block predicate is invariant under the diagonal action (t, v) ↦ (u t, u^{-1} v) for odd units u, then aggregate time weights over those orbits. This can drastically reduce the number of LP variables. Caution: only use this after checking that the engine’s boundary convention and oddness condition are preserved. Odd units preserve parity, but the forbidden arc must also be respected via the product v t.
• Dominated-speed pruning. If two candidates have the same parity/coarse compatibility and one blocks a subset of the other’s times, the weaker one can often be removed or deprioritized. This must be done carefully if distinct-coarse-class constraints are present, but it is cheap to test.
• Do not blindly fix speed 1 when parity matters. Unit scaling can move a solution to one containing 1 at the coarse level, but if the final statement tracks odd/even lifts, the scaling must preserve the required parity pattern. Safer: use lex-leader or orbit-breaking constraints rather than globally fixing a speed unless you branch over the small number of parity/orbit cases.

WHY IT MIGHT WORK
FACT (from the packet): p = 191, 223, 239, 241, 401 all end with 0 survivors at level 16. Therefore the final 16p UNSAT statement is true for these primes.
ESTIMATE: for p = 401, the full fine-grid incidence matrix has only about 16p ≈ 6416 time rows and at most 16p speed columns; after sign/coarse reduction it is smaller. A dense LP of this size is solvable on a laptop. Certificate checking is roughly O(#speeds × average blocked times), about a few million sums for p = 401, which is seconds to minutes, not core-years.
IDEA: the cascade data suggests the final contradiction is local. Almost all level-one rows die at the first zooms. In an IP/SAT proof, those deaths become short unit-propagation or cutting-plane contradictions. The expensive part of the current method is enumerating the rows to discover that; the certificate method tries to prove the same local contradictions globally without listing the rows.
IDEA / sanity use of the five p=401 survivors: the five level-2 survivors are exactly the near-misses. They can be used as regression tests:
  • the four non-tight rows should be killed by level-4 constraints;
  • the tight row should survive until the level where the engine says it dies;
  • the dual weights or final cuts should put positive mass on the explicit free times that kill these rows.
If a certificate cannot separate these known near-misses, it is probably too blind.

CHEAP TEST
Use p = 223 or p = 239, since the answer is known to be empty and the grids are smaller than p = 401.
Concrete test plan, under one hour on a laptop:
• Export the fine block relation. From the existing engine, output the predicate β(v,t) for the 16p grid. No new search is performed.
• Build the OPB/PB instance. Include: ∑ x_v ≤ 15; ∑ odd(v)x_v ≥ 2; ∑_{v blocks t} x_v ≥ 1 for every fine time t; optional: at most one lift per coarse class.
• First try the LP dual. Solve: maximize ∑_t w_t + 2η, subject to ∑_{t blocked by v} w_t + η·odd(v) ≤ 1, w_t ≥ 0, η ≥ 0. Success if the optimum is > 15 by a safe rational margin. Convert the solution to rational weights and check with a short independent script.
• If LP alone fails, run a PB/SAT UNSAT proof. Use an open-source pseudo-Boolean solver or SAT solver with proof logging. Success means: solver returns UNSAT; produces a proof file; an independent checker accepts the proof; total wall time ≤ 60 minutes; proof file and checker time are clearly cheaper than the known row-generation cost.
• Sanity check against known rows. If available, assert the known p=223/239 level-2 or level-4 survivors as assumptions and verify the solver kills them at the correct level. This catches encoding mistakes.

WHAT KILLS IT
KILL RESULT: if, on p = 223 or p = 239, this route fails to produce an independently checkable UNSAT certificate — LP dual or PB/SAT proof — within 60 minutes and with proof/checking cost smaller than the known row-search cost, then the certificate bypass is dead for this project.
In particular, the idea is dead if the best certificate is larger or slower to check than the traditional list, or if the LP relaxation stays ≤ 15 and the PB solver must essentially enumerate the same level-one rows to prove UNSAT.
----- END REPLY -----
END LETTER
