# PT005 · Grok packet · red-team the 16-runner plan

Carried by Puck to Grok. Paste everything from BEGIN to END.

```
BEGIN PT005-SEAT-GROK
TOGETHER · PROOF TABLE 005 · seat: Grok · role: RED TEAM · carried by Puck · AS_OF 2026-10-04T14:16+08:00
Chair: Opus. This block is self-contained.

YOUR JOB: find the most dangerous HIDDEN BLOCKER in the plan below: the thing most likely to make a 16-runner computation fail, cost far more than planned, or prove nothing. Do not praise the plan. Pick ONE blocker (two at most), argue it concretely from the sources, give a cheap test that would show whether it is real, and say what result would show it is NOT a blocker.

THE PLAN (state of the table, 2026-10-04)
- Goal: the Lonely Runner Conjecture for 16 runners = 15 non-zero integer speeds, bound 1/16. Proved up to 15 runners (Allikvere, arXiv:2609.02604 v2; code and data Zenodo 22066772 and 22667683, CC-BY-4.0).
- Method (the author's): (1) a product bound for a primitive counterexample (flag bound, Theorem 3.8); (2) prime gates: a finite computation per prime p shows p divides v1⋯v15; (3) enough gates that the sum of log p beats the bound.
- Bound: the author's outlook gives 497.03 (text below). The table lowered it to 494.92 with a dual-lattice step (t_14 < 1/3), HAND-CHECKED by two non-author seats. Gates must supply Σ log p > 481.43, about 80–86 primes up to about 600–700.
- Code: the author's engine is generic in K (compile with -DK=15). The chair reproduced the author's K = 14 numbers at p = 239 exactly (178 jobs, 1,342,843 rows, 5,308,002,124 nodes). The K = 15 build certifies that at p = 239 no cover uses at most 13 classes (τ_15(239) ≥ 14). The K = 15 timing run is in progress; early jobs run about 4–5× slower than K = 14.
- Cost of the 15-runner run (author's data): about 2,137 CPU-hours; 77% of it was level-one generation.
- Closed routes, with reasons, on the wall: tight-seeded skipping (unsound), a stronger generic KZ property, a better ellipsoid, a Fourier shortcut at p ≤ 700 (every class mod p has relations with |c_i| ≤ 2 once 3^15 > p), grouping classes by short-relation profile (the profile already fixes the unit orbit).

CANDIDATE BLOCKERS (the chair's list; you may pick another)
(a) The terminal level. For 15 speeds the last level is 16 = 2^4, a binary level, so the author's level-15 factorisation (CRT over 3·5) and his few-exception shift lemma (written for 14 speeds and d in {3,5}) do not carry over directly. Does the tight orbit (1,…,15) die cleanly at level 16 by the gcd condition, or do some witness-free lifts need a new lemma?
(b) Small primes. If τ_15(p) ≤ 13 at many small primes, the "general variant" (a single serial job) applies there. For 13 speeds the author reports primes that failed open, p = 89, 101, 103 stopped by resource limits, and p = 29 needing about 48 GB. If small primes fail, the prime range moves up, and the cost grows about as p^5.9.
(c) Engine limits. The engine is built for p ≤ 975 (n ≤ 512 with NW = 8, m ≤ 64). If failures push the needed primes past about 975, the code needs changes.
(d) Anything in the framework (Lemma 2.2, Corollary 3.11, the reduction to distinct speeds) that does not carry over from 14 to 15 speeds.

SOURCE TEXT (SOURCE OF THE QUOTED TEXT: Zenodo record 22667683 (Allikvere, CC-BY-4.0), file fifteen_runners_manuscript_source.zip (sha256 54e0fa471c103e4b26f7e8d940bb7552de65a6d69bd7ac9d6256133eb0af10f6), file paper_v2.tex. Quoted verbatim, LaTeX as in the file.)
----- author's discussion of orbits surviving the binary lifts (15-runner manuscript) -----
\subsection{Orbits surviving the binary lifts}

A speed tuple of length $k$ is \emph{tight} if
$\max_{t\in\R}\min_i\nearest{t v_i}=1/(k+1)$.

At each of the \NoNearGcdCount{} verified primes with $\tau(p)\geq13$, the
only unit orbit to survive the binary lifts is that of
$\vct{a}=(1,\ldots,14)$.  Its seven witness-free level-$15$ lifts are all
proper by the gcd condition.  In the $k=13$ computation, two orbits survived
at every verified prime: $(1,\ldots,13)$ and the Goddyn--Wong tight set
$(1,\ldots,11,13,24)$~\cite{GW06,Allikvere26}.

For the verified $k=14$ primes with $\tau(p)\geq13$, every other row has
$F_8(r)=\varnothing$.  This includes
$\vct{c}=(1,\ldots,11,13,14,24)$.  At $t=12/29$, every coordinate of
$\vct{c}$ is at distance at least $2/29$ from an integer.  Since
$2/29>1/15$, this tuple is not tight.  The survival of $\vct{a}$ through
the binary levels is forced by Remark~3.2 of~\cite{ST26}: modulo one, its
witness times are $s/15$ with $\gcd(s,15)=1$, whereas none of the levels
$2,4,8,16,32$ is divisible by $15$.  The computational observation is
that no other orbit survives at these primes.

This resembles Proposition~7.1 of~\cite{ST26}, although that result
concerns level-$1$ witnesses for all sufficiently large primes; we make no
asymptotic claim here.  When $\tau(p)\leq12$, the family surviving the
binary lifts is much larger and is handled by the direct divisibility
argument of Lemma~\ref{lem:neargcd}, rather than by emptying an improper
fiber at a grid level.
----- author's outlook: sixteen runners -----
\subsection{Outlook: sixteen runners}\label{sec:outlook}

Theorem~\ref{thm:flag} applies to $n=15$ now that $LRC(14)$ is available.
The ratio hypothesis holds with minimum $3751/2349$, and the proof of the
shape estimate also gives $R_{15}<\frac12$.  Thus
$15\log(A_{15}/30)=497.03\ldots$.  Since
$\log\lcm(2,\ldots,16)=\log720720$, the logarithmic sum required from
verified primes is
\[
  497.03\ldots-\log720720=483.54\ldots.
\]
The verification programs are
generic in $K$, but the terminal level $16=2^4$ is itself a binary level,
so the factorisation used for level $15$ does not apply directly.  We
record these bounds as a starting point; the computation is future work.
----- end quoted LaTeX -----

FORMAT: SEAT: Grok · REPLY_TO: wall lines 1–26. Start with a SUMMARY of at most 5 lines. No length limit.
Sections: BLOCKER (which one, why it is the most dangerous) · ARGUMENT (with source citations) · CHEAP TEST · WHAT WOULD SHOW IT IS NOT A BLOCKER · STATUS CLAIM (OPEN) · NEXT.
Rules: read the quoted sources, do not cite from memory; label FACT / ESTIMATE / IDEA; mark gaps INCOMPLETE; do not search or read other chats; say which account records, if any, you read; no keys or passwords.
END PT005-SEAT-GROK
```
