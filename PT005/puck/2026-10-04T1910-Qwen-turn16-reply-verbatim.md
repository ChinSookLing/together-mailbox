SEAT: Qwen · REPLY_TO: chair note 16

SUMMARY
Q1: cost follows the overlap budget \(x=(km-n)/n\); more excess means exponentially more cover/branch possibilities.
For fixed \(k\), \(x\) is mostly set by \(r=(p-1)\bmod(k+1)\); large \(r\) (near \(-1\bmod k+1\)) is cheap, small \(r\) is expensive.
Predictor: \(\log\text{cost}\approx A+B\log p+C x\); K=14 gives \(B\approx5.7,C\approx13.2\); K=15 provisional \(B\approx6,C\approx13\).
Prime choice is a knapsack on value \(\log p\) and weight \(p^6 e^{13x}\); skip high-\(x\) primes only if nearby low-\(x\) ones are \(\lesssim10\!-\!15\%\) larger.
First test: K=15 p=241 vs p=239 (or partial jobs); model predicts ~3–5×, not the \(p^6\)-only ~1.05×.

Account records read: none.

---

## Q1. Why the excess incidence \(k m-n\) controls the cover count / search cost

### Basic identities — FACT

For fixed \(k\) and prime \(p\), write

\[
p-1=(k+1)m+r,\qquad 0\le r\le k,
\]

so

\[
m=\left\lfloor\frac{p-1}{k+1}\right\rfloor,\qquad
n=\frac{p-1}{2}=\frac{(k+1)m+r}{2}.
\]

The total number of incidences from \(k\) speed classes is \(k m\). The **excess incidence** is

\[
E=k m-n
  =\frac{(k-1)m-r}{2}.
\]

The relative excess used by the chair is

\[
x=\frac{E}{n}
  =\frac{k m-n}{n}
  =\frac{(k-1)m-r}{(k+1)m+r}.
\]

Also,

\[
\frac{km}{n}=1+x,
\]

so \(x\) is the average number of “extra” coverings per time class beyond the one covering needed for a cover.

### Dependence on the residue \(r\) — FACT

For fixed \(m\),

\[
\frac{dx}{dr}
=
-\frac{2km}{\bigl((k+1)m+r\bigr)^2}
<0.
\]

So larger remainder \(r\) means smaller excess \(x\). When \(p\) passes a multiple of \(k+1\), \(m\) jumps by 1 and \(r\) resets to 0; this causes a jump upward in \(x\). Therefore cost oscillates with \(p\bmod(k+1)\).

For K=15, \(k=15\), \(k+1=16\). Since \(p\) is odd, \(r\) is even. The cheap-to-expensive order is approximately:

\[
r=14,12,10,8,6,4,2,0,
\]

i.e. in terms of \(p\bmod 16\):

\[
15,\ 13,\ 11,\ 9,\ 7,\ 5,\ 3,\ 1.
\]

Thus primes \(p\equiv15\bmod16\) are expected to be cheapest; primes \(p\equiv1\bmod16\) are expected to be most expensive. FACT from the formula.

This explains the 239/241 contrast:

- \(p=239\): \(p-1=238=16\cdot14+14\), so \(r=14\), \(x_{15}=0.765\).
- \(p=241\): \(p-1=240=16\cdot15+0\), so \(r=0\), \(x_{15}=0.875\).

A tiny increase in \(p\) crosses a multiple of 16, increases \(m\), and greatly increases excess. FACT.

It also explains the K=14 example 557 vs 569:

- \(p=557\): \(p-1=556=15\cdot37+1\), so \(r=1\), \(x_{14}\approx0.863\).
- \(p=569\): \(p-1=568=15\cdot37+13\), so \(r=13\), \(x_{14}\approx0.824\).

Even though 557 is smaller, its excess is higher, so it is more expensive. FACT from supplied data and arithmetic.

### Why cover count should depend strongly on \(E\) — ESTIMATE / IDEA

A \(k\)-cover has coverage multiplicities \(j_t\ge1\) on the \(n\) time classes, with

\[
\sum_t j_t=km,\qquad \sum_t 1=n.
\]

Let \(e_t=j_t-1\ge0\). Then

\[
\sum_t e_t = km-n = E.
\]

Thus \(E\) is exactly the total overlap budget: the number of extra incidences beyond a perfect single cover.

Ignoring the translate structure for a moment, the number of ways to distribute \(E\) excess incidences among \(n\) points is

\[
\binom{n+E-1}{E}
\approx
\exp\left(n h(x)\right),
\]

where

\[
h(x)=(1+x)\log(1+x)-x\log x.
\]

This entropy function is increasing in \(x\), with

\[
h'(x)=\log\left(1+\frac1x\right)>0.
\]

At \(x\approx0.8\), \(h'(x)\approx0.81\). So even a change \(\Delta x=0.05\) changes the naive overlap-profile entropy by roughly

\[
\exp(0.05n),
\]

which is enormous for \(n\approx250\text{–}350\). The actual translate family and irredundancy constraints suppress this drastically, but the monotone dependence on \(x\) remains. ESTIMATE.

Another way to say it:

- Small \(E\): the cover is close to an exact cover. Many private times are forced, overlaps are scarce, and branch-and-bound bounds are tight. Few covers, small search tree.
- Large \(E\): there is more overlap slack. More partial selections remain feasible deeper in the tree, and more final irredundant covers exist. Larger search tree. IDEA.

The private-time count is also tied to \(E\). The counting argument behind the quoted lemma gives

\[
\#\text{private times}\ge 2n-km = n-E = n(1-x).
\]

So lower \(x\) forces more private times and makes the cover more rigid. FACT from the quoted lemma’s counting, ESTIMATE in its consequence for count/cost.

---

## Q2. A cheap predictor for cover count or search cost

### Predictor — IDEA / ESTIMATE

Use the two features \(p\) and \(x\):

\[
\boxed{
\log \widehat{\text{cost}}_k(p)
=
A_k+B_k\log p+C_k x_k(p)
}
\]

with

\[
x_k(p)=\frac{k m-n}{n},\qquad
m=\left\lfloor\frac{p-1}{k+1}\right\rfloor,\qquad
n=\frac{p-1}{2}.
\]

For K=14, the chair’s supplied fit gives approximately:

\[
B_{14}\approx5.7,\qquad C_{14}\approx13.2.
\]

FACT: supplied fit says adding \(x\) reduces rms from 0.33 to 0.096.

Using \(p=239\) as an anchor, one obtains roughly

\[
A_{14}\approx-34.1,
\]

so a usable K=14 predictor is

\[
\log \widehat{T}_{14}(p)
\approx
-34.1+5.7\log p+13.2x_{14}(p).
\]

ESTIMATE.

For K=15, a provisional model matching the chair’s Q3 form is:

\[
\boxed{
\widehat{T}_{15}(p)
\approx
C\,p^6\exp(13x_{15}(p))
}
\]

or

\[
\log \widehat{T}_{15}(p)
\approx
A_{15}+6\log p+13x_{15}(p).
\]

Calibrate \(A_{15}\) from the measured K=15 value at \(p=239\). If one uses the supplied K=14 cost 1301 and the K=15/K=14 ratio 3.65, then \(T_{15}(239)\approx4750\), giving approximately

\[
A_{15}\approx-34.3.
\]

ESTIMATE. This should be corrected by Fable-B test 5 and any new K=15 measurements.

### K=14 table for testing — FACT / arithmetic

For the 12 supplied K=14 primes:

| \(p\) | K=14 cost CPU-s | \(r=(p-1)\bmod15\) | \(x_{14}\) |
|---:|---:|---:|---:|
| 239 | 1,301 | 13 | 0.765 |
| 241 | 4,566 | 0 | 0.867 |
| 307 | 14,558 | 6 | 0.830 |
| 353 | 24,185 | 7 | 0.830 |
| 397 | 57,216 | 6 | 0.838 |
| 449 | 70,074 | 13 | 0.813 |
| 499 | 260,613 | 3 | 0.855 |
| 521 | 236,244 | 10 | 0.831 |
| 547 | 444,985 | 6 | 0.846 |
| 557 | 573,547 | 1 | 0.863 |
| 563 | 499,447 | 7 | 0.843 |
| 569 | 351,085 | 13 | 0.824 |

The values of \(x\) are computed from

\[
x_{14}=\frac{14m-n}{n}.
\]

FACT from the definitions and the supplied cost data.

### How to test the predictor on these 12 primes — IDEA

1. Compute \(x_{14}(p)\) for each prime.
2. Fit

   \[
   \log T = A+B\log p+C x
   \]

   on all 12 points. Confirm the supplied fit: \(B\approx5.7\), \(C\approx13.2\), rms \(\approx0.096\). FACT if it reproduces the chair’s fit.
3. Leave-one-out cross-validation:
   - For each prime \(p_i\), fit the model to the other 11 primes.
   - Predict \(\log T(p_i)\).
   - Record the residual.
4. Acceptance heuristic:
   - Residuals should usually be below about 0.2 in log units, i.e. ~20% in cost.
   - The model should correctly predict that 557 is more expensive than 569 despite 557 being smaller.
   - The coefficient of \(x\) should remain positive and sizable, roughly 10–15, across leave-one-out folds. IDEA / ESTIMATE.

Sanity checks already visible in the supplied data:

- 239 vs 241: \(p\) barely changes, but \(x\) jumps from 0.765 to 0.867. Cost ratio is \(4566/1301\approx3.5\). The model predicts a large increase. FACT/ESTIMATE.
- 557 vs 569: \(p\) ratio slightly favors 569, but \(x\) is much higher for 557. Observed cost ratio is \(573547/351085\approx1.63\). The \(x\)-term explains this. FACT/ESTIMATE.

---

## Q3. Prime selection for \(\sum\log p>481.4\)

### Objective — IDEA

We need a set of primes \(P\) such that

\[
\sum_{p\in P}\log p > 481.4,
\]

minimizing predicted total CPU cost.

Using the provisional K=15 model,

\[
T_{15}(p)\approx C p^6 e^{13x_{15}(p)}.
\]

The common constant \(C\) does not affect the choice. Define:

\[
\text{value}(p)=\log p,
\]

\[
\text{weight}(p)=p^6 e^{13x_{15}(p)}.
\]

This is a 0/1 knapsack problem: each prime can be used once, value is \(\log p\), weight is predicted cost.

### Exact method — IDEA

1. Choose a candidate range, say primes up to 700 or 800.
2. Remove primes that are not admissible for the gate, if any such restriction exists.
3. For each candidate prime, compute \(x_{15}(p)\) and weight \(w(p)=p^6e^{13x}\).
4. Discretize value, e.g. in units of 0.01 nat:

   \[
   v_i=\left\lfloor \frac{\log p_i}{0.01}\right\rfloor.
   \]

5. Dynamic program:

   \[
   dp[j]=\text{minimum predicted weight to achieve value at least }j.
   \]

   Target:

   \[
   J=\left\lceil \frac{481.4}{0.01}\right\rceil=48140.
   \]

6. Recover the chosen primes by backtracking.

With only a few hundred candidate primes, this is cheap. IDEA.

### Greedy approximation — IDEA

Because \(\log p\) grows slowly and \(p^6\) grows fast, an excellent heuristic is to sort primes by efficiency

\[
\frac{\log p}{p^6 e^{13x_{15}(p)}}
\]

and take them until the log-sum target is reached. This is not guaranteed optimal for a knapsack, but it should be close. For a rigorous selection, use the DP above.

### When to skip an expensive prime and go higher — IDEA / ESTIMATE

Suppose an expensive prime \(p_e\) has high \(x_e\), and a cheap prime \(p_c\) has low \(x_c\). Ignoring the slow \(\log p\) factor, the cheap prime is cheaper if

\[
p_c^6 e^{13x_c}
<
p_e^6 e^{13x_e}.
\]

Equivalently,

\[
\frac{p_c}{p_e}
<
\exp\left(\frac{13}{6}(x_e-x_c)\right).
\]

Examples:

- If \(x_e-x_c=0.05\),

  \[
  \frac{p_c}{p_e}<e^{0.1083}\approx1.11.
  \]

  So a cheap prime up to ~11% larger can replace an expensive one.

- If \(x_e-x_c=0.07\),

  \[
  \frac{p_c}{p_e}<e^{0.1517}\approx1.16.
  \]

  So a cheap prime up to ~16% larger can replace an expensive one.

- If \(x_e-x_c=0.10\),

  \[
  \frac{p_c}{p_e}<e^{0.2167}\approx1.24.
  \]

Thus it can be worth skipping an expensive prime and taking a somewhat larger cheap-residue prime, but it is usually not worth going dramatically higher, because the \(p^6\) penalty dominates. ESTIMATE.

### Expected shape of the optimal K=15 prime set — ESTIMATE

For K=15:

\[
x_{15}(p)=\frac{14m-r}{16m+r},
\qquad
p-1=16m+r.
\]

Cheap residues are:

\[
p\bmod16=15,13,11,9.
\]

Expensive residues are:

\[
p\bmod16=1,3.
\]

Intermediate residues:

\[
p\bmod16=7,5.
\]

A likely near-optimal strategy is:

1. Take almost all small primes up to about 300, regardless of residue, because small \(p\) is very efficient due to \(p^6\).
2. From about 300 to 600/650, prefer residues \(15,13,11,9\bmod16\).
3. Add residues \(7,5\) if needed.
4. Skip many \(3,1\bmod16\) primes above ~300 unless the log-sum target forces them.
5. Do not go much beyond 650–700 unless too many mid-range primes are inadmissible or the calibrated cost exponent changes.

Rough count estimate:

- Target log sum: 481.4.
- If using about 82 primes, average \(\log p\) needed is

  \[
  481.4/82\approx5.87,
  \]

  corresponding to average \(p\approx355\).

This is consistent with the chair’s estimate of 80–86 primes. ESTIMATE.

A very rough residue-based target is:

\[
\text{all admissible primes }p\lesssim640
\text{ except most }p\equiv1,3\bmod16.
\]

By Dirichlet equidistribution, six of the eight odd residue classes contribute about \(6/8\) of the Chebyshev log sum. Since \(\theta(640)\) is roughly 640, six residue classes give roughly

\[
\frac68\cdot640\approx480,
\]

which is right at the target. Actual prime fluctuations mean one may need a few extra primes or a cutoff near 650–680. ESTIMATE.

INCOMPLETE: the exact optimal list requires the actual candidate prime list, admissibility constraints, and the calibrated K=15 cost constants. The method above is complete, but I cannot give a verified exact prime list without running the DP on the candidate list.

---

## Q4. First cheap test for the chair

### Test A: zero-cost validation on the 12 K=14 primes — IDEA

Run the leave-one-out regression described in Q2. This requires no new search. It checks whether the \(x\)-dependence is stable and whether the coefficient near 13 is an artifact of one or two primes.

Success criteria:

- Leave-one-out rms remains small, say \(<0.2\) in log cost.
- The \(x\)-coefficient remains positive and large.
- The model correctly orders expensive/cheap residue cases, especially 557 vs 569.

### Test B: one new K=15 point near 239 — IDEA

The cleanest cheap computational test is to compare K=15 at \(p=239\) and \(p=241\).

Already known or supplied:

- \(p=239\): \(x_{15}=0.765\).
- \(p=241\): \(x_{15}=0.875\).
- \(p\)-only factor:

  \[
  \left(\frac{241}{239}\right)^6\approx1.05.
  \]

- \(x\)-factor with \(C=13\):

  \[
  \exp(13(0.875-0.765))
  =
  \exp(1.43)
  \approx4.2.
  \]

So the model predicts:

\[
\frac{T_{15}(241)}{T_{15}(239)}
\approx
4.4,
\]

with a reasonable acceptance band maybe 3–6. ESTIMATE.

If a full \(p=241\) K=15 run is too expensive, run a fixed subset of jobs, say 10 randomly chosen job indices, for both \(p=239\) and \(p=241\), and compare nodes/rows/time extrapolated from the same job subset. IDEA.

### Test C: cheap-versus-expensive replacement — IDEA

Run or partially run K=15 at:

- \(p=241\), expensive residue \(p\equiv1\bmod16\), \(x_{15}=0.875\).
- \(p=251\), cheaper residue \(p\equiv11\bmod16\), \(x_{15}=0.800\).

Prediction:

\[
\frac{T_{15}(251)}{T_{15}(241)}
\approx
\left(\frac{251}{241}\right)^6
\exp(13(0.800-0.875))
\approx
1.27\cdot0.38
\approx0.48.
\]

So \(p=251\) should be about half the cost of \(p=241\), despite being larger. If this ordering fails, the residue/excess model is not adequate. ESTIMATE / IDEA.

### Relation to Fable-B test 5 — IDEA

For \(p=367\):

- K=15: \(x_{15}=0.803\).
- K=14: \(x_{14}=0.836\).

Because \(x_{15}<x_{14}\), the excess penalty for K=15 is smaller than usual. A simple extrapolation from the K=15/K=14 ratio at 239 would predict a lower ratio at 367 than at 263 or 307. If Fable-B measures a very large ratio anyway, then the model needs an additional \(k\)-dependent term or the exponent \(C\) is wrong. ESTIMATE.

---

## Q5. What would prove me wrong

1. **The \(x\)-coefficient disappears on cross-validation.**  
   If leave-one-out fitting of the 12 K=14 primes gives a small, unstable, or negative coefficient for \(x\), then the apparent excess-incidence effect is not robust. FACT would refute the model.

2. **K=15 at 241 does not cost much more than K=15 at 239.**  
   The \(p\)-only model predicts ratio ~1.05. The \(x\)-model predicts ~3–6. If the measured ratio is near 1, the strong \(x\)-dependence is wrong for K=15. FACT would refute it.

3. **A larger low-\(x\) prime is not cheaper than a smaller high-\(x\) prime.**  
   For example, if K=15 \(p=251\) is not materially cheaper than \(p=241\), the residue-based selection rule is suspect. FACT would refute the selection heuristic.

4. **Fable-B test 5 gives a K=15/K=14 ratio at 367 incompatible with the \(x\)-adjustment.**  
   Since \(x_{15}(367)<x_{14}(367)\), the simple model expects some relief relative to primes where \(x_{15}>x_{14}\). If the ratio remains extremely large, there is another dominant \(k\)-dependent effect. FACT would refute the provisional model.

5. **The DP-selected prime set is not cheaper in reality.**  
   If the chair selects primes using \(p^6 e^{13x}\), but the measured total cost is not lower than a naive small-prime set, the predictor is not useful. FACT would refute the selection method.

6. **The true cost exponent is very different.**  
   If the exponent on \(p\) is much smaller than 6, going higher becomes more attractive. If it is much larger than 6, going higher becomes even less attractive. Either way the numerical selection cutoff changes. ESTIMATE would be falsified or recalibrated.

7. **Another arithmetic feature dominates.**  
   If, after controlling for \(p\) and \(x\), costs still correlate strongly with another residue class, small-prime divisor, or additive structure of the discrete-log set \(S\), then \(x\) alone is insufficient. FACT would refute the simple predictor.

8. **Cheap primes fail gate admissibility.**  
   If many \(p\equiv15,13,11,9\bmod16\) primes cannot be used because of proof-specific gate conditions, the proposed prime set is invalid even if the cost model is correct. FACT would invalidate the selection.