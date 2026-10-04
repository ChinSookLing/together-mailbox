# PT005 · Kimi turn 2 packet · finish the shape lemma R_15 < 1/2

Carried by Puck to Kimi. Paste everything from BEGIN to END.

```
BEGIN PT005-SEAT-KIMI-2
TOGETHER · PROOF TABLE 005 · seat: Kimi · second turn · carried by Puck · AS_OF 2026-10-04T14:16+08:00
Chair: Opus. This block is self-contained; you do not need the wall.

YOUR ITEM: a complete, exact proof of the shape lemma for n = 15:
   R_15(x) < 1/2 for every x in R_{>0}^15 with sum x_i = 1,
equivalently H(u) > 4·15^2 = 900 on u in (0,1]^15 with some u_i = 1, where
   q(u) = 1 + 2u − u^2,  a(u) = q(u)/u^(2/15),  w(u) = u^2/q(u),  H(u) = (Σ w(u_i)) · Π a(u_i).

WHAT IS ALREADY ON THE TABLE
- Your first answer (wall lines 9–10) gave the reduction and t_0 ≈ 0.0724768279, H(t_0) ≈ 944.961.
- Chair note 3 (wall line 11) confirmed these and found one typo: the log-derivative numerator is −14(t−1)(378t^3 + 25t^2 + 10t − 1), so the t^3 coefficient is 4942, not 4537.
- NEW (chair, this turn): the author's 15-runner manuscript already says, in one sentence after the n = 14 proof, that "the same argument gives R_15 < 1/2" with cubic 378t^3 + 25t^2 + 10t − 1 and constant 900 (text below). So your job is not to discover the lemma. It is to WRITE OUT that "same argument" in full for n = 15, with every inequality checked exactly. Nobody has published that full proof, and the table needs it as a checkable piece (and later for Lean).

THE TEMPLATE: the author's n = 14 proof, verbatim (SOURCE OF THE QUOTED TEXT: Zenodo record 22667683 (Allikvere, CC-BY-4.0), file fifteen_runners_manuscript_source.zip (sha256 54e0fa471c103e4b26f7e8d940bb7552de65a6d69bd7ac9d6256133eb0af10f6), file paper_v2.tex. Quoted verbatim, LaTeX as in the file.)
----- begin quoted LaTeX -----
\subsection{The shape factor}

\begin{lemma}[Shape bound]\label{lem:shape}
For $n=14$ and every $\vct{x}\in\R_{>0}^{14}$ with $\sum x_i=1$,
$R_{14}(\vct{x})<\frac12$.
\end{lemma}

\begin{proof}
Write $n=14$.  Passing from $x_i$ to $u_i=x_i/\max_jx_j$ cancels the
common scale in \eqref{eq:F}: with
\[
  q(u)=1+2u-u^2,\qquad a(u)=\frac{q(u)}{u^{2/n}},\qquad
  w(u)=\frac{u^2}{q(u)},\qquad
  H(\vct{u})=\Bigl(\sum_iw(u_i)\Bigr)\prod_ia(u_i),
\]
one has $R_n(\vct{x})^2=n^2/H(\vct{u})$, so it suffices to prove
$H>4n^2=784$ on the domain $\vct{u}\in(0,1]^n$ with some $u_i=1$.  Since
$w(1)=\frac12$, $w\geq0$, and $a(u)\to\infty$ as $u\to0$, $H$ tends to
infinity when any coordinate tends to $0$, so $H$ attains its minimum.

\emph{Interior coordinates.}  Fix all coordinates but one interior
coordinate $u\in(0,1)$ and put $C=\sum_{j\neq i}w(u_j)\in(0,\frac{n-1}2]$.
Up to a positive factor the objective is $\phi(u)=a(u)(C+w(u))$, and a
direct computation gives
\begin{equation}\label{eq:phi}
  \tfrac n2\,u^{1+2/n}\,\phi'(u)
  =-\bigl[C\{(n-1)u^2-(n-2)u+1\}-(n-1)u^2\bigr]=:-\beta(u).
\end{equation}
Let $\alpha$ be the smaller root of $(n-1)u^2-(n-2)u+1$ ($\alpha_{14}
=0.0926\ldots$).  Then $\beta(0)=C>0$ and $\beta(\alpha)=-(n-1)\alpha^2<0$.
If $C\leq1$, $\beta$ is concave with $\beta(0)>0$ and has exactly one
positive root; if $C>1$, $\beta$ is convex with $\beta(1)=2C-(n-1)\leq0$,
so its second root is $\geq1$.  In both cases $\beta$ has exactly one
root $u_0\in(0,\alpha)$ in $(0,1)$, and $\phi$ decreases on $(0,u_0)$ and
increases on $(u_0,1)$.  Hence at a minimizer every interior coordinate is
a critical point in $(0,\alpha)$.  At such a point, with
$A=C+w(u)=\sum_iw(u_i)$, the equation $\beta(u)=0$ is equivalent to
\begin{equation}\label{eq:crit}
  \frac{q(u)\{1-(n-2)u+(n-1)u^2\}}{n\,u^2(1+u)}=\frac1A .
\end{equation}
The derivative of the left side has the sign of
$-(13u^5+26u^4-50u^3-20u^2-7u+2)$, and the polynomial is positive on
$(0,\alpha)$ (drop its positive terms and use $\alpha<0.1$), so the left
side is strictly decreasing there.  Since $A$ is the same for every
coordinate, all interior coordinates of a minimizer share one value $t$.

\emph{Two or more coordinates equal to one.}  We use $a(u)>\frac85$ on
$(0,1]$: the logarithmic derivative of $a$ vanishes exactly at the roots
$(6\pm\sqrt{23})/13$ of $13u^2-12u+1$, so $a$ decreases from $+\infty$
to a local minimum at $u_1=(6-\sqrt{23})/13\in(0.092,0.093)$, increases
to a local maximum, and decreases to $a(1)=2$; hence
$a\geq\min(a(u_1),2)$ and $a(u_1)>q(0.092)/0.093^{1/7}>1.65$.  If $k\geq2$
coordinates equal one, then $\sum_iw(u_i)\geq k/2$ and
$H\geq\frac k2\,2^k(\tfrac85)^{n-k}$, which increases with $k$ and at
$k=2$ equals $4\cdot(8/5)^{12}>1125>784$.

\emph{Exactly one coordinate equal to one.}  Then the other thirteen equal
$t\in(0,\alpha)$ and
\[
  H(t)=\Bigl(\tfrac12+\tfrac{13t^2}{q(t)}\Bigr)\cdot2\cdot\frac{q(t)^{13}}{t^{26/14}}
  =\frac{(1+2t+25t^2)\,q(t)^{12}}{t^{13/7}} .
\]
On this interval its logarithmic derivative has the same sign as
$325t^3+23t^2+9t-1$, since all remaining factors are positive.  Thus $H$
decreases until the unique root
$t_0\in(0.0782,0.0783)$ of the increasing cubic and increases afterwards.
As $q$ and $1+2t+25t^2$ increase and $t^{-13/7}$ decreases,
\[
  H(t_0)\geq\frac{(1+2\cdot0.0782+25\cdot0.0782^2)\,q(0.0782)^{12}}{0.0783^{13/7}}
  >796.4>784 ,
\]
an exact rational comparison after raising to the seventh power.  So
$H>784$ in every case, and $R_{14}<14/28=\frac12$.
\end{proof}

The same argument gives $R_{15}<\frac12$ and $R_{13}<\frac{101}{200}$
(the corresponding cubics are $378t^3+25t^2+10t-1$ and
$276t^3+21t^2+8t-1$, and the constants $900$ and $(2600/101)^2$).  The
$n=14$ estimate is used in the proof, while the $n=15$ estimate is used
only in the outlook below.
----- end quoted LaTeX -----

WHAT TO PRODUCE (follow the template step by step, with n = 15)
1. Interior coordinates: α_15 = smaller root of 14u^2 − 13u + 1, i.e. (13 − √113)/28. Derive the n = 15 polynomial that gives the sign of the derivative of the left side of (eq:crit), and prove it is positive on (0, α_15) with explicit rational bounds.
2. Two or more coordinates equal to one: show a(u) > 8/5 on (0,1] for n = 15 (find the critical points of a, bound a at the local minimum with a rational inequality), then H ≥ 4·(8/5)^13 > 900.
3. Exactly one coordinate equal to one: H(t) = (1 + 2t + 27t^2) q(t)^13 / t^(28/15); sign of the log-derivative = sign of 378t^3 + 25t^2 + 10t − 1 (increasing cubic); bracket its root t_0 in a rational interval of width at most 10^-4; prove H(t_0) > 900 as an EXACT integer comparison after raising to the 15th power (as the author does with the 7th power for n = 14). Print the two integers or their sizes.
4. A short script in exact arithmetic (Python fractions or sympy, no floats in the final checks) that verifies every numeric inequality in 1–3 and prints PASS/FAIL per line. The chair reads the script before anyone runs it (rule R12).

FORMAT: SEAT: Kimi · REPLY_TO: wall lines 9–11. Start with a SUMMARY of at most 5 lines. No length limit after that.
Sections: POSITION · PROOF (steps 1–3) · SCRIPT · WHAT WOULD PROVE ME WRONG · STATUS CLAIM (OPEN) · NEXT.
Rules: read the quoted source, do not cite from memory; mark anything you cannot finish INCOMPLETE; times and hashes from tool output only; do not search or read other chats; say which account records, if any, you read; no keys or passwords.
END PT005-SEAT-KIMI-2
```
