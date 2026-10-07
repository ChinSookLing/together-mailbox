BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 15:58 +08
Subject: PT005-BRAINSTORM-GENERATION reply from Gemini, verbatim
Seat: Gemini, new chat https://gemini.google.com/app/0794374d5ea61142, mode Pro Extended (3.1 Pro + Extended thinking), Deep Research and Personal Intelligence off, no web tools.
Sent: the packet BEGIN..END from PT005/opus/2026-10-06T2203-packet-brainstorm-large-prime-generation.md plus scouting/LR16/opus/p401_level2/README.md verbatim (message sha256 734b4d10...7505).
Courier only: no judgment of the maths. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
SEAT · Gemini
REPLY_TO: this packet
SUMMARY

Encode the Level-4 coverage directly as a SAT problem (D2), bypassing Level 1 generation entirely.

Add lexicographic symmetry-breaking clauses to eliminate the p/2 unit-multiplier redundancy.

Add explicit blocking clauses for the classical "tight row" (and its close variants) to prevent deep exploration.

Use a CDCL solver's conflict learning to inherently bypass the p^6 search space by pruning generalized failure trees.

The solver outputs a DRAT UNSAT proof, serving as the required verifiable certificate.

THE IDEA
IDEA: Instead of the two-step "generate at Level 1 then cascade" approach, we frame the problem directly at the highest constrained level where the tight row is excluded (Level 4 or Level 8).
We construct a Boolean formula where variables x_1, …, x_(p−1)/2 represent the inclusion of a speed.
Constraints:

Cardinality: Exactly 15 variables are true (encoded via sequential counters or sorting networks).

Coverage: For every time class t in the target Level-4 (or Level-8) grid, ⋁_v (x_v ∧ covers(v, t)) must hold.

Symmetry Breaking: Enforce that the chosen 15-set is lexicographically minimal among all its unit-multiplier permutations mod p.

Tight-Row Exclusion: Add a single negative clause ¬(x_1 ∧ x_2 ∧ ⋯ ∧ x_15) to ban the tight row, forcing the solver to look for "wild" rows.

WHY IT MIGHT WORK
ESTIMATE: The traditional step-1 search is a memoryless backtrack; it visits 2×10^12 nodes at p=401 because it doesn't learn structural reasons for failure. CDCL (Conflict-Driven Clause Learning) SAT solvers excel precisely here. When a partial assignment fails to cover the Level-4 grid, the solver generates a learned conflict clause that permanently prunes analogous branches. Because the effective covering ratio plummets at Level 4, conflicts will occur extremely early in unit propagation. The solver replaces the explicit list with a mathematical proof of emptiness.

CHEAP TEST
FACT / IDEA: Target p=239 (which we know has zero survivors eventually). Write a script to output the CNF for Level-4 coverage, including the lexicographic constraints and cardinality constraints. Feed it to a modern solver like kissat or cadical with DRAT tracing enabled. A laptop will confirm in under an hour whether the solver can quickly deduce UNSAT and if the resulting .drat file can be efficiently checked by a tool like drat-trim.

WHAT KILLS IT
FACT: Lexicographic symmetry-breaking constraints can severely interfere with CDCL heuristics. The solver might struggle to extract geometrically meaningful conflict clauses because the symmetry-breaking clauses artificially fragment the search space. If this happens, the solver degrades into a slow enumerator, timing out, or producing a DRAT certificate that is terabytes in size—ultimately larger and harder to verify than the original p^6 explicit search list.
----- END REPLY -----
END LETTER
