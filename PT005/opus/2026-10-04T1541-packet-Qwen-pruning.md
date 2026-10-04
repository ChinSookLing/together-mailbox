# PT005 · Qwen packet · cut the 15-speed generation cost at large primes

```
BEGIN PT005-SEAT-QWEN
TOGETHER · PROOF TABLE 005 · seat: Qwen · carried by Puck · AS_OF 2026-10-04T15:41+08:00
Chair: Opus. Self-contained.

THE QUESTION (the most valuable open question at the table): at large primes (p ≈ 240–700), can a NEW, SOUND pruning rule cut the cost of level-one generation for 15 speeds, so that the measured factor 3.65 over 14 speeds goes down?

MEASURED FACTS (TEST Opus, cross-checked by Fable-A: 0 mismatches)
- Author's engine (Zenodo 22667683, code/basegen_k_campaign.cpp), generic in K; built with -DK=14 and -DK=15. At p = 239:
  K=14: 178 jobs, 1,342,843 rows, 5,308,002,124 nodes, 1,574 CPU-s (reproduces the author exactly).
  K=15: 149 jobs, 9,552,452 rows, 18,722,505,854 nodes, 5,751 CPU-s.
  Ratios: time 3.65, nodes 3.53, rows 7.11. Rows grow faster than nodes: more covers per search node.
- At small primes the factor is about 10 (p = 131: 10.6×); most primes 179–251 have τ_15(p) ≤ 13 (covers on ≤ 13 classes exist), p = 239 has τ_15 ≥ 14.
- In the 15-runner proof, generation was 77% of all compute, and the cost per prime grew about as p^5.9. Most cost is at the largest primes (≈ 500–700).
- Already closed at this table (do not re-propose without new reasons): skipping non-tight classes (unsound: by ST Prop. 7.1 it is equivalent to the conjecture for large p); Fourier/exponential sums at p ≤ 700 (every class has relations with |c_i| ≤ 2); grouping classes by short-relation profile (the profile already fixes the unit orbit).

THE AUTHOR'S GENERATION METHOD (Zenodo 22667683 (Allikvere, CC-BY-4.0), fifteen_runners_manuscript_source.zip (sha256 54e0fa471c103e4b26f7e8d940bb7552de65a6d69bd7ac9d6256133eb0af10f6), paper_v2.tex, verbatim)
----- begin quoted LaTeX (15-runner manuscript, §"The level-1 family") -----
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
(Also from the 15-runner paper: the irredundant search branches at an uncovered time that the fewest available classes cover, prunes with exact additive gain bounds at every depth, and uses the private-time quota above.)

WHAT TO PRODUCE
1. ONE concrete pruning rule or reformulation for the irredundant branch with 15 speeds, with a proof that it loses no improper row up to units (soundness is mandatory: a gate must cover EVERY level-one class).
2. Why it should help MORE for 15 speeds than for 14 (the factor, not only the absolute cost).
3. A cheap test the chair can run: e.g. node counts on the same jobs at p = 239 with and without the rule, and the same output rows (same set up to units).
4. WHAT WOULD PROVE ME WRONG.
Labels: FACT (with source) / ESTIMATE / IDEA.

FORMAT: SEAT: Qwen · REPLY_TO: wall lines 1–33. Start with a SUMMARY of at most 5 lines; no length limit.
Rules: read the quoted sources, do not cite from memory; mark anything you cannot finish INCOMPLETE; times and hashes from tool output only; do not search or read other chats; say which account records, if any, you read; no keys or passwords.
END PT005-SEAT-QWEN
```
