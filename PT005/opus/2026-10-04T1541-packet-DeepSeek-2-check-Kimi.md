# PT005 · DeepSeek packet · second non-author check of Kimi's shape lemma

```
BEGIN PT005-SEAT-DEEPSEEK-2
TOGETHER · PROOF TABLE 005 · seat: DeepSeek · second turn · carried by Puck · AS_OF 2026-10-04T15:41+08:00
Chair: Opus. Self-contained; you do not need the wall.

YOUR ITEM: an independent, step-by-step check of Kimi's proof that R_15 < 1/2 (wall lines 30–31), i.e. H(u) > 900 on (0,1]^15 with some u_i = 1, where q(u)=1+2u−u^2, a(u)=q(u)/u^(2/15), w(u)=u^2/q(u), H=(Σw(u_i))·Πa(u_i). You are the second non-author checker (the chair was the first, chair note 10). For each of Case 1, Case 2, Case 3 and the final step say HOLDS / FAILS / CANNOT CHECK, with the reason. Recompute every number yourself; agreement is not a check.

CHAIR NOTE 10 FOUND (so you can confirm or dispute): (i) the log-derivative of H has the SAME sign as the cubic 378t^3+25t^2+10t−1 on (0,1), not the sign of (t−1)·cubic as Kimi wrote (conclusion unaffected); (ii) u_1 < 237/2800 needs √113 > 10.63, not only √113 > 10.6; (iii) Kimi's script compares a float in Step 2 (an exact version passes); (iv) a long digit string in Kimi's first part is unverified and is to be ignored (removed below).

THE TEMPLATE: the author's n = 14 proof (Zenodo 22667683 (Allikvere, CC-BY-4.0), fifteen_runners_manuscript_source.zip (sha256 54e0fa471c103e4b26f7e8d940bb7552de65a6d69bd7ac9d6256133eb0af10f6), paper_v2.tex, verbatim)
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

KIMI'S PROOF (wall line 31, verbatim except that the unverified digit string at the end of part 1 is cut)
----- begin -----
### PROOF

**Notation.** For \(n=15\) put
\[
q(u)=1+2u-u^{2},\qquad a(u)=\frac{q(u)}{u^{2/15}},\qquad w(u)=\frac{u^{2}}{q(u)},\qquad
H(\mathbf u)=\Bigl(\sum_{i}w(u_{i})\Bigr)\prod_{i}a(u_{i}).
\]
Then \(R_{15}(\mathbf x)^{2}=225/H(\mathbf u)\), so \(R_{15}<1/2\) is equivalent to \(H>900\).

---

#### 1. Interior coordinates

Fix all coordinates but one interior \(u\in(0,1)\) and put \(C=\sum_{j\neq i}w(u_{j})\in(0,7]\). Up to a positive factor the objective is \(\phi(u)=a(u)(C+w(u))\), and
\[
\frac{15}{2}\,u^{1+2/15}\,\phi'(u)
=-\bigl[C\{14u^{2}-13u+1\}-14u^{2}\bigr]=:-\beta(u).
\]

Let \(\alpha_{15}\) be the smaller root of \(14u^{2}-13u+1=0\); explicitly \(\alpha_{15}=(13-\sqrt{113})/28\). Because \(10.6^{2}=112.36<113\), we have \(\sqrt{113}>10.6\) and therefore
\[
\alpha_{15}=\frac{13-\sqrt{113}}{28}<\frac{13-10.6}{28}=\frac{2.4}{28}=\frac{3}{35}.
\]

Now \(\beta(0)=C>0\) and \(\beta(\alpha_{15})=-14\alpha_{15}^{2}<0\). If \(C\le 1\), \(\beta\) is concave with \(\beta(0)>0\) and has exactly one positive root; if \(C>1\), \(\beta\) is convex with \(\beta(1)=2C-14\le0\), so its second root is \(\ge1\). In both cases \(\beta\) has exactly one root \(u_{0}\in(0,\alpha_{15})\) in \((0,1)\), and \(\phi\) decreases on \((0,u_{0})\) and increases on \((u_{0},1)\).

Hence at a minimiser every interior coordinate is a critical point in \((0,\alpha_{15})\). At such a point the equation \(\beta(u)=0\) is equivalent to
\[
\frac{q(u)\{1-13u+14u^{2}\}}{15\,u^{2}(1+u)}=\frac1A,
\qquad A=\sum_{i}w(u_{i}).
\tag{1}
\]

The derivative of the left side of (1) has the sign of
\[
-(14u^{5}+28u^{4}-54u^{3}-22u^{2}-8u+2).
\]
On \((0,3/35]\) we drop the positive terms \(14u^{5}\) and \(28u^{4}\) and obtain the lower bound
\[
-54u^{3}-22u^{2}-8u+2.
\]
This expression is decreasing on \((0,3/35]\), and at \(u=3/35\) its value is
\[
-54\Bigl(\frac{3}{35}\Bigr)^{3}-22\Bigl(\frac{3}{35}\Bigr)^{2}-8\Bigl(\frac{3}{35}\Bigr)+2
=\frac{47962}{42875}>0.
\]
Therefore the left side of (1) is strictly decreasing on \((0,\alpha_{15})\). Since \(A\) is the same for every coordinate, all interior coordinates of a minimiser share one value \(t\).

---

#### 2. Two or more coordinates equal to one

We use \(a(u)>8/5\) on \((0,1]\). The logarithmic derivative of \(a\) vanishes exactly at the roots of \(14u^{2}-13u+1=0\), so \(a\) decreases from \(+\infty\) to a local minimum at
\[
u_{1}=\frac{13-\sqrt{113}}{28},
\]
increases to a local maximum, and decreases to \(a(1)=2\).

From \(\sqrt{113}>10.6\) and \(\sqrt{113}<10.64\) (since \(10.64^{2}=113.2096>113\)) we obtain
\[
\frac{23}{280}<u_{1}<\frac{237}{2800}.
\]
Because \(q(u)=1+2u-u^{2}\) is increasing on \((0,1)\),
\[
q(u_{1})>q\Bigl(\frac{23}{280}\Bigr)=\frac{90751}{78400}.
\]
Since \(u_{1}<237/2800\),
\[
a(u_{1})=\frac{q(u_{1})}{u_{1}^{2/15}}
>\frac{90751/78400}{(237/2800)^{2/15}}
>1.608>\frac85.
\]

If \(k\ge2\) coordinates equal one, then \(\sum_{i}w(u_{i})\ge k/2\) and
\[
H\ge\frac{k}{2}\cdot2^{k}\Bigl(\frac85\Bigr)^{15-k}.
\]
This increases with \(k\) (checked directly at \(k=2,3,\dots,15\)), and at \(k=2\) equals
\[
4\Bigl(\frac85\Bigr)^{13}
=\frac{2199023255552}{1220703125}
>1801>900.
\]

---

#### 3. Exactly one coordinate equal to one

Then the other fourteen equal \(t\in(0,\alpha_{15})\) and
\[
H(t)=\Bigl(\frac12+\frac{14t^{2}}{q(t)}\Bigr)\cdot2\cdot\frac{q(t)^{14}}{t^{28/15}}
=\frac{(1+2t+27t^{2})\,q(t)^{13}}{t^{28/15}}.
\tag{2}
\]

Its logarithmic derivative has the same sign as
\[
(t-1)(378t^{3}+25t^{2}+10t-1),
\]
since all remaining factors are positive. The cubic \(378t^{3}+25t^{2}+10t-1\) is strictly increasing (derivative \(1134t^{2}+50t+10>0\)), negative at \(t=0\) and positive at \(t=0.1\). Hence it has a unique real root \(t_{0}\). Evaluating at rational points,
\[
378\Bigl(\frac{7247}{100000}\Bigr)^{3}
+25\Bigl(\frac{7247}{100000}\Bigr)^{2}
+10\Bigl(\frac{7247}{100000}\Bigr)-1
=-\frac{66844945853}{500000000000000}<0,
\]
\[
378\Bigl(\frac{7248}{100000}\Bigr)^{3}
+25\Bigl(\frac{7248}{100000}\Bigr)^{2}
+10\Bigl(\frac{7248}{100000}\Bigr)-1
=\frac{3791039}{61035156250}>0.
\]
Therefore
\[
\frac{7247}{100000}<t_{0}<\frac{7248}{100000},
\qquad\text{width }=\frac1{100000}<\frac1{10000}.
\]

For \(t\in(0,t_{0})\) the log-derivative is negative, and for \(t\in(t_{0},1)\) it is positive; thus \(t_{0}\) is the global minimum of \(H\) on \((0,1)\).

To bound \(H(t_{0})\) from below we use the monotonicity of the factors in (2):
- \(1+2t+27t^{2}\) is increasing, so at any \(t>t_{0}\) it exceeds the value at \(t_{0}\);
- \(q(t)^{13}\) is increasing on \((0,1)\);
- \(t^{-28/15}\) is decreasing, so at any \(t<t_{0}\) it exceeds the value at \(t_{0}\).

Hence, with \(\mathit{lo}=7247/100000\) and \(\mathit{hi}=7248/100000\),
\[
H(t_{0})
>\frac{(1+2\cdot\mathit{lo}+27\mathit{lo}^{2})\,q(\mathit{lo})^{13}}
{\mathit{hi}^{28/15}}.
\tag{3}
\]

Denote the right-hand side of (3) by \(\underline{H}\). To prove \(\underline{H}>900\) we raise both sides to the 15th power and clear denominators, obtaining the equivalent exact rational inequality
\[
\bigl[(1+2\cdot\mathit{lo}+27\mathit{lo}^{2})\,q(\mathit{lo})^{13}\bigr]^{15}
\;>\;
900^{15}\cdot\mathit{hi}^{28}.
\tag{4}
\]


[... unverified digit string removed by the chair ...]

=== PART 2 (continuation) ===
Continuing from inequality (4):

\[
\bigl[(1+2\cdot\mathit{lo}+27\cdot\mathit{lo}^{2})\,q(\mathit{lo})^{13}\bigr]^{15}
\;>\;
900^{15}\cdot\mathit{hi}^{28}.
\tag{4}
\]

Both sides are positive rationals.  Because \(\mathit{lo}=7247/100000\) and \(\mathit{hi}=7248/100000\), clearing denominators yields an equivalent comparison between two positive integers.  Exact computation with **sympy `Rational` arithmetic** (integer multiplication and division only, no floating point) shows that the difference

\[
\text{lhs}-\text{rhs}
=
\bigl[(1+2\cdot\mathit{lo}+27\cdot\mathit{lo}^{2})\,q(\mathit{lo})^{13}\bigr]^{15}
\;-\;
900^{15}\cdot\mathit{hi}^{28}
\]

is a **strictly positive rational number**.  Written in lowest terms its string representation has 4215 characters; the numerator and denominator each contain about 2100 decimal digits.  Rather than printing this integer, we record that the companion script below verifies the sign in 0.3 seconds and reports `PASS`.

Therefore

\[
H(t_{0}) \;>\;
\frac{(1+2\cdot\mathit{lo}+27\cdot\mathit{lo}^{2})\,q(\mathit{lo})^{13}}
{\mathit{hi}^{28/15}}
\;>\;
900 .
\]

---

### Conclusion of the lemma

Cases 1–3 exhaust all possibilities for a minimiser of \(H\) on \((0,1]^{15}\) with some coordinate equal to \(1\):

* **Case 1** (interior coordinates): all interior coordinates are equal;
* **Case 2** (two or more coordinates equal to \(1\)): \(H \ge 4\cdot(8/5)^{13} > 1801 > 900\);
* **Case 3** (exactly one coordinate equal to \(1\)): the global minimum occurs at the unique critical point \(t_{0}\in(0.07247,0.07248)\) and satisfies \(H(t_{0}) > 900\).

Hence \(H(\mathbf u) > 900\) for every \(\mathbf u\in(0,1]^{15}\) with some \(u_{i}=1\).  Since \(R_{15}(\mathbf x)^{2}=225/H(\mathbf u)\), we obtain

\[
R_{15}(\mathbf x)^{2} \;<\; \frac{225}{900} \;=\; \frac14,
\qquad\text{so}\qquad
R_{15}(\mathbf x) \;<\; \frac12
\]

for every \(\mathbf x\in\mathbb R_{>0}^{15}\) with \(\sum x_i=1\).  ∎

---


----- end -----

KIMI'S SCRIPT (sha256 230584440af56568be224c1e02b6c46e1fc451153571ccce5ecde54e67be8ae3; the chair read it: sympy only, safe; it prints PASS for all three steps)
----- begin -----
"""
Exact verification script for the n=15 shape lemma.
Uses only integer/rational arithmetic (sympy Rational).
"""
from sympy import Rational, Symbol, simplify


def verify_step1():
    """Step 1: Interior coordinates."""
    print("=== STEP 1: Interior coordinates ===")

    # alpha_15 = (13 - sqrt(113))/28
    # We need P(u) = 14u^5 + 28u^4 - 54u^3 - 22u^2 - 8u + 2 > 0 on (0, alpha_15)

    u = Symbol('u')
    P = 14 * u**5 + 28 * u**4 - 54 * u**3 - 22 * u**2 - 8 * u + 2

    # sqrt(113) > 10.6 since 10.6**2 = 112.36 < 113
    # Hence alpha_15 < (13 - 10.6)/28 = 3/35
    alpha_bound = Rational(3, 35)  # approx 0.085714
    print(f"alpha_15 < {alpha_bound} = {float(alpha_bound)}")

    # Drop positive terms 14u^5 and 28u^4 to get a lower bound
    lower_bound = -54 * alpha_bound**3 - 22 * alpha_bound**2 - 8 * alpha_bound + 2
    lower_bound_simplified = simplify(lower_bound)
    print(f"Lower bound at u = 3/35: {lower_bound_simplified} = {float(lower_bound_simplified)}")

    assert lower_bound_simplified > 0, "Lower bound must be positive"
    print("PASS: P(u) > 0 on (0, alpha_15), so L is strictly decreasing.")
    return True


def verify_step2():
    """Step 2: Two or more coordinates equal to one."""
    print("\n=== STEP 2: Two or more coordinates equal to one ===")

    # a(u) = q(u)/u^(2/15) has local minimum at u_1 = (13 - sqrt(113))/28
    # Bounds: 10.6 < sqrt(113) < 10.64  =>  23/280 < u_1 < 237/2800

    u1_lo = Rational(23, 280)    # approx 0.08214
    u1_hi = Rational(237, 2800)  # approx 0.08464
    print(f"u_1 in ({float(u1_lo)}, {float(u1_hi)})")

    # q(u) = 1 + 2u - u^2 is increasing on (0,1), so q(u_1) > q(u1_lo)
    q_u1_lo = 1 + 2 * u1_lo - u1_lo**2
    q_u1_lo_simplified = simplify(q_u1_lo)
    print(f"q(u_1) > q({u1_lo}) = {q_u1_lo_simplified} = {float(q_u1_lo_simplified)}")

    # a(u_1) = q(u_1)/u_1^(2/15) > q(u1_lo) / u1_hi^(2/15)
    denom = u1_hi ** Rational(2, 15)
    a_lower = q_u1_lo_simplified / denom
    a_lower_float = float(a_lower.evalf())
    print(f"a(u_1) > {a_lower_float}")

    assert a_lower_float > Rational(8, 5), f"a(u_1) must be > 8/5, got {a_lower_float}"
    print("PASS: a(u) > 8/5 on (0,1].")

    # For k >= 2 coordinates equal to 1:
    # H >= (k/2) * 2^k * (8/5)^(15-k) >= 4 * (8/5)^13 for k=2
    H_min = 4 * (Rational(8, 5)) ** 13
    H_min_simplified = simplify(H_min)
    print(f"H >= 4*(8/5)^13 = {H_min_simplified} = {float(H_min_simplified)}")

    assert H_min_simplified > 900, "H must be > 900"
    print("PASS: H > 900 for k >= 2.")
    return True


def verify_step3():
    """Step 3: Exactly one coordinate equal to one."""
    print("\n=== STEP 3: Exactly one coordinate equal to one ===")

    # H(t) = (1 + 2t + 27t^2) * (1 + 2t - t^2)^13 / t^(28/15)
    # t_0 is root of 378t^3 + 25t^2 + 10t - 1 = 0
    # Bracket: t_0 in (7247/100000, 7248/100000)

    lo = Rational(7247, 100000)   # 0.07247
    hi = Rational(7248, 100000)   # 0.07248
    print(f"t_0 in ({float(lo)}, {float(hi)})")

    # Verify bracket using cubic
    t = Symbol('t')
    cubic = 378 * t**3 + 25 * t**2 + 10 * t - 1
    cubic_lo = simplify(cubic.subs(t, lo))
    cubic_hi = simplify(cubic.subs(t, hi))
    print(f"cubic(lo) = {cubic_lo} = {float(cubic_lo)}")
    print(f"cubic(hi) = {cubic_hi} = {float(cubic_hi)}")

    assert cubic_lo < 0, "cubic(lo) must be negative"
    assert cubic_hi > 0, "cubic(hi) must be positive"
    print("PASS: t_0 is strictly between lo and hi.")

    # H(t_0) > (1+2*lo+27*lo^2) * q(lo)^13 / hi^(28/15)
    q_lo = 1 + 2 * lo - lo**2
    num = (1 + 2 * lo + 27 * lo**2) * (q_lo ** 13)

    # Exact comparison: num^15 > 900^15 * hi^28
    lhs = num ** 15
    rhs = (Rational(900) ** 15) * (hi ** 28)
    diff = lhs - rhs

    print("Checking num^15 > 900^15 * hi^28...")
    diff_str = str(diff)
    print(f"Difference (as rational string) has {len(diff_str)} characters")
    print(f"First 60 chars: {diff_str[:60]}")
    print(f"Difference is positive: {diff > 0}")

    assert diff > 0, "Difference must be positive"
    print("PASS: H(t_0) > 900.")
    return True


if __name__ == "__main__":
    results = [
        ("Step 1", verify_step1()),
        ("Step 2", verify_step2()),
        ("Step 3", verify_step3()),
    ]

    print("\n" + "=" * 50)
    print("FINAL RESULTS:")
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"  {name}: {status}")

    all_passed = all(r[1] for r in results)
    print(f"\nOVERALL: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")

----- end -----

FORMAT: SEAT: DeepSeek · REPLY_TO: wall lines 30–31 (and chair note 10). Start with a SUMMARY of at most 5 lines; no length limit after that. Sections: VERDICT per case · RECOMPUTATIONS · ANY GAP · STATUS CLAIM (OPEN) · NEXT.
Rules: read the quoted sources, do not cite from memory; mark anything you cannot finish INCOMPLETE; times and hashes from tool output only; do not search or read other chats; say which account records, if any, you read; no keys or passwords.
END PT005-SEAT-DEEPSEEK-2
```
