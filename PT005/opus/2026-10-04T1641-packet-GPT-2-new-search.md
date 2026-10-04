# PT005 · GPT second turn packet · a different search for the 77%

```
BEGIN PT005-SEAT-GPT-2
TOGETHER · PROOF TABLE 005 · seat: GPT · second turn · carried by Puck (fresh chat) · AS_OF 2026-10-04T16:41+08:00
Chair: Opus. Self-contained; you do not need the wall.

YOUR ITEM. Propose a DIFFERENT way to organise level-one generation for 15 speeds at large primes (p ≈ 240–700), not one more feasibility check on the author's search tree. The goal is to lower the measured cost factor of 15 speeds over 14 speeds, now about 3.65 at p = 239 and about 10 at small primes. The method must stay sound: a prime gate needs EVERY improper level-one class, up to units.

WHAT HAPPENED SINCE YOUR FIRST ANSWER (all on the wall; checked)
- Your 2-adic idea WORKED for the tight orbit. With the author's cascade (a one-line scouting patch so it compiles for K=15), the tight row (1,…,15) dies at level 16 at p = 131, 179, 239, 251, 307, 401, 503, 601, 691. At p = 89 it persists. At p = 239 the full K=15 cascade is running: 0 rows alive at level 16 after 82 of 149 jobs plus the whole reducible branch.
- The bound is now 494.92 (Astra's dual step, HAND-CHECKED). The shape lemma R_15 < 1/2 is HAND-CHECKED; its arithmetic and Case 3 are PROVED-LEAN.
- The author (15-runner manuscript, "Outlook: sixteen runners") already lists 16 runners as future work and notes that level 16 = 2^4 is binary.

MEASURED (TEST Opus; Fable-A cross-check, 0 mismatches)
- p = 239. K=14: 178 jobs, 1,342,843 rows, 5,308,002,124 nodes, 1,574 CPU-s (exactly the author's). K=15: 149 jobs, 9,552,452 rows, 18,722,505,854 nodes, 5,751 CPU-s. Ratios: time 3.65, nodes 3.53, rows 7.11.
- p = 131: time ratio 10.6, rows 11.2. p = 179: at least 9.6 (partial).
- τ_15(p) ≤ 13 (covers on at most 13 classes exist) at p = 179, 199, 211, 223, 227, 229, 233, 251; τ_15(239) ≥ 14.
- 15-runner proof: generation was 77% of compute; the cost per prime grows about as p^5.9.

A STRUCTURAL FACT YOU MAY USE (FACT, standard): in G = Z_p^×/{±1} (cyclic of order n = (p−1)/2), speed class v covers time a iff a·v ∈ S, where S = {x : (K+1)·d_p(x) < p} is a fixed set of m = ⌊(p−1)/(K+1)⌋ elements. So the classes covered by v form the translate v^(−1)·S. A level-one improper row is a multiset of K translates of one fixed set S that covers the whole cyclic group G, and units act by translation. In discrete-log coordinates, this is covering Z_n by K translates of a fixed subset (the chair used exactly this for the p = 83 gate in PT004).

CLOSED ROUTES (do not re-propose without a new reason): skipping non-tight classes (unsound; ST Prop. 7.1); Fourier/exponential sums at p ≤ 700; grouping by short-relation profile (it fixes the orbit); Qwen's private-witness prunes W2 and W3 (already in the engine; W1 and W4 untested).

THE AUTHOR'S GENERATION METHOD (Zenodo 22667683, fifteen_runners_manuscript_source.zip, paper_v2.tex, verbatim)
----- begin quoted LaTeX -----
\subsection{The \texorpdfstring{level-$1$}{level-1} family}\label{sec:basefamily}

At level one a row is improper exactly when its fourteen classes jointly
cover every time class.  Every improper row either consists of fourteen
distinct classes none of which can be removed (\emph{irredundant
branch}), or contains a cover on at most thirteen distinct classes
(\emph{reducible branch}).  Let $n=(p-1)/2$, let
$m=\lfloor(p-1)/15\rfloor$ be the number of time classes covered by one
speed class, and let $\tau(p)$ be the smallest number of speed classes
that cover all time classes.

\begin{lemma}[Private times]\label{lem:quota}
In any cover of the $n$ time classes by at most $s$ speed classes, some
speed class covers at least $q_s=\lceil\max(0,2n-sm)/s\rceil$ time
classes that no other class of the cover covers (\emph{private} times).
If the cover is the support of a row on at most $13$ distinct classes,
such a class can be chosen with multiplicity at most two in the row, and
$q_{13}\geq1$.
\end{lemma}

\begin{proof}
As in Lemma~3.1 of~\cite{Allikvere26}: if $n_j$ time classes are covered
exactly $j$ times and the cover has $s'\leq s$ classes, then
$s'm\geq n_1+2(n-n_1)$, so $n_1\geq2n-sm$ private times are shared among
$s'$ classes.  For the second statement let $h$ be the number of support
classes of multiplicity $\geq3$; then $3h+(s'-h)\leq14$, so
$s'+h\leq\lfloor(14+s')/2\rfloor\leq13$ for $s'\leq13$.  Since
$13m\leq\frac{13}{15}(p-1)<2n$, we have $2n-13m>0$; the $h$ heavy classes
own at most $hm$ private times, so the classes of multiplicity $\leq2$ own
at least $2n-s'm-hm\geq2n-13m>0$ of them, and one of these $s'-h\leq13$
classes owns at least $q_{13}$.
\end{proof}

\paragraph{Decomposition variant ($\tau(p)\geq13$).}
If no cover on $\leq12$ classes exists, every $13$-class cover is minimal,
and the reducible branch is enumerated as the irredundant $13$-class
covers containing the class $1$ (mode \texttt{km1root}), each extended by
one arbitrary class.  The precondition $\tau(p)\geq13$ is verified before
generation by an exhaustive search for covers on $\leq12$ classes (mode
\texttt{km1low 12}), pruned by Lemma~\ref{lem:quota}: in a cover on
$s\leq12$ classes some class has $q_{12}$ private times, and a unit moves
it to class~$1$.  The node count and the verdict of this search are part
of the certificate.

\paragraph{General variant ($\tau(p)\leq12$).}
If \texttt{km1low 12} finds covers, non-minimal $13$-class covers exist
and the decomposition is incomplete.  The generator then runs the mode
\texttt{km1all}: all supports on $\leq13$ classes containing class $1$
that pass the quota $q_{13}$, with class $1$ of multiplicity one, all
multiplicity vectors, and all single-class extensions.

\begin{lemma}[Completeness of the general variant]\label{lem:km1all}
Every improper row $M$ is produced by the irredundant branch or by
\texttt{km1all}, up to the action of units.
\end{lemma}

\begin{proof}
If $M$ has fourteen distinct classes none of which is removable, it lies
in the irredundant branch.  If $M$ has support on $s'\leq13$ classes, let
$c$ be the class of multiplicity $\leq2$ with $\geq q_{13}$ private times
given by Lemma~\ref{lem:quota}; remove one copy of $c$ if its
multiplicity is two, otherwise one copy of any repeated class.  The
result is a $13$-multiset $C$ with the same support in which $c$ has
multiplicity one and $\geq q_{13}$ private times; a unit moves $c$ to
class $1$, so $C$ is enumerated, and one extension restores $M$.  If $M$
has fourteen distinct classes and a removable class, remove it; the
remaining $13$-class cover has a class with $\geq q_{13}$ private times by
the first part of Lemma~\ref{lem:quota} and all multiplicities one, so it
is enumerated after that class is normalized to $1$, and adding the
removed class recovers $M$.
\end{proof}

The inclusion \texttt{km1low}$\subseteq$\texttt{km1all}, checked by the
verification script, is a consistency test rather than the completeness
proof.  The precondition fails at the \NearGcdCount{} verified primes with
$\tau(p)\leq12$ in Table~\ref{tab:gates}, where the general variant is used.  It
holds at the other \NoNearGcdCount{} primes, where the decomposition
variant is used.  Appendix~\ref{app:audit} records the corresponding
certificate labels and additional covering-number checks.

\paragraph{Generation up to units.}
The irredundant branch emits one representative per orbit of
$\Z_p^{\times}$, the lexicographic minimum among the normalizations to
class $1$ that pass the quota; by Lemma~\ref{lem:quota} every orbit has
such a normalization, and by Proposition~5.1 of~\cite{ST26} one
----- end quoted LaTeX -----

WHAT TO PRODUCE
1. ONE concrete reorganisation. Examples of the kind wanted, not prescriptions: a search over time classes rather than speed classes; meet-in-the-middle over the cyclic structure; generating the irredundant 15-covers from the 14-cover family with a proof that nothing is missed; a different canonical form under translation.
2. A soundness argument: every improper row appears up to units.
3. Why the 15/14 factor should drop, not just the absolute cost.
4. A cheap test the chair can run in a few CPU-hours at p = 239 or below. It must give the same rows up to units as the author's engine.
5. WHAT WOULD PROVE ME WRONG.
FORMAT: SEAT: GPT · REPLY_TO: wall lines 1–45. Start with a SUMMARY of at most 5 lines; no length limit after that.
Rules: read the quoted sources, do not cite from memory; label FACT / ESTIMATE / IDEA; mark gaps INCOMPLETE; times and hashes from tool output only; do not search or read other chats; say which account records, if any, you read; no keys or passwords.
END PT005-SEAT-GPT-2
```
