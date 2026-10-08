BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-08 16:50 +08
RE: 猜公式 Round 1 packet (ebc63af), BEGIN…END block pasted verbatim
SEAT: kimi
MODEL: Kimi K3 High (Copy button truncated at end of section 4; rest read from page text)
CHAT: https://www.kimi.ai/chat/1a119f45-8882-8a49-8000-09ce01fb11cc

--- reply verbatim ---
## 1. Rule

Let  
\[
I_p=\{\pm1,\pm2,\ldots,\pm H\}\subset\mathbb F_p^\times,
\qquad H=\left\lfloor\frac{p-1}{16}\right\rfloor .
\]

For a speed set \(S\), put \(R=\{s^{-1}:s\in S\}\). Then \(S\) is a cover exactly when

\[
R I_p=\mathbb F_p^\times.
\]

Indeed, \(t\) is covered by \(s\) precisely when \(st\in I_p\), equivalently \(t\in s^{-1}I_p\). Hence the exact problem is

\[
\boxed{\gamma(p)=
 \min\{|R|:R\subset\mathbb F_p^\times,\ RI_p=\mathbb F_p^\times\}.}
\]

For an empirical decision rule, write

\[
p=16H+r,\qquad r=p\bmod 16\in\{1,3,\ldots,15\}.
\]

The following residue boundary fits every training row:

\[
\gamma(p)\le12
\quad\text{if}\quad
\begin{cases}
H\le10,\\
H=11,\ r\le3,\\
H=12,\\
H=14,\ r\le5;
\end{cases}
\]

\[
\gamma(p)=13
\quad\text{if}\quad
\begin{cases}
H=11,\ r\ge5,\\
H=13,\\
H=14,\ 7\le r\le13,\\
H=15,\\
H=16,\ r\le11,\\
H=17,\ r\le7;
\end{cases}
\]

and

\[
\gamma(p)\ge14
\quad\text{if}\quad
\begin{cases}
H=14,\ r=15,\\
H=16,\ r\ge13,\\
H=17,\ r\ge9,\\
H\ge18.
\end{cases}
\]

This is an interpolation of the training table, not a theorem. Its main content is that, once \(H\) is fixed, increasing \(r\) makes covering harder; the critical residue then decreases as \(H\) grows.

## 2. Predictions

| \(p\) | \(H\) | \(p\bmod16\) | Prediction |
|---:|---:|---:|:---|
| 199 | 12 | 7 | **12 or less** |
| 227 | 14 | 11 | **13** |
| 257 | 16 | 1 | **13** |
| 271 | 16 | 15 | **14 or more** |
| 283 | 17 | 11 | **14 or more** |
| 311 | 19 | 7 | **14 or more** |
| 313 | 19 | 9 | **14 or more** |
| 401 | 25 | 1 | **14 or more** |

## 3. Reason

The counting picture is

\[
n=\frac{p-1}{2}=8H+\frac{r-1}{2}.
\]

Thirteen speeds supply \(13H\) incidences, counted with multiplicity, so the required average multiplicity is

\[
\frac{13H}{n}
 =\frac{26H}{16H+r-1}
 \approx \frac{13}{8}.
\]

A random choice of thirteen speeds would leave approximately

\[
n\left(1-\frac Hn\right)^{13}
 \approx n e^{-13/8}
 \approx 0.20n
\]

cells uncovered. Thus a 13-cover cannot look random: its thirteen translates of \(I_p\) must be an unusually efficient, low-overlap multiplicative packing.

This explains the two main training patterns:

- At fixed \(H\), increasing \(r\) increases the number of cells while leaving every speed’s coverage at \(H\). Hence \(r=13,15\) becomes dangerous before \(r=1,3,5\).
- As \(H\) grows, even the low-residue cases eventually cross from 13 to at least 14.

The smoothness of \(p-1\) can create exceptions because \(\mathbb F_p^\times\) then has many subgroups and cosets with which translates of \(I_p\) can align. I did not give that effect its own correction term: on the training table it was less stable than the \(H,r\) boundary. This is why \(257\), \(271\), and \(401\) remain the structurally dangerous predictions.

The rule is directly testable: to refute a predicted \(\gamma(p)\ge14\), exhibit thirteen residues \(R\) with \(RI_p=\mathbb F_p^\times\); to prove it, show that every thirteen-element \(R\) leaves at least one residue outside \(RI_p\).

## 4. Big question

My empirical guess is

\[
\boxed{\gamma(p)\ge14\quad\text{for every prime }p\ge307,}
\]

so I would take \(P_0=307\), while stressing that this is a small-data conjecture rather than a proved threshold.

There is, however, a rigorous upper cap:

\[
\boxed{\gamma(p)\le15\quad\text{for every }p.}
\]

For any cell \(x=t/p\), consider the sixteen points

\[
0,x,2x,\ldots,15x
\]

on the circle \(\mathbb R/\mathbb Z\). Two are within circular distance at most \(1/16\). Their difference has the form \(jx\) with \(1\le|j|\le15\). Equality with \(1/16\) is impossible, since it would give

\[
16jt=(16k\pm1)p,
\]

with even left side and odd right side. Therefore the fixed speed set \(\{1,\ldots,15\}\) always covers every cell.

Consequently:

- \(\gamma(p)\ge15\) may eventually occur;
- \(\gamma(p)\ge16\) can never occur;
- the long-term “growth” can consist only of the final step from 14 to 15.

This is also the modular shadow of the Lonely Runner problem. A September 2026 preprint reports a computer-assisted proof of the conjecture for fourteen and fifteen runners. Qualitatively, the thirteen-speed result supports an eventual \(\gamma(p)\ge14\), and the fourteen-speed result suggests that \(\gamma(p)=15\) may eventually be forced. The extra issue is approximation: a real Lonely Runner witness must be approximated by a grid point \(t/p\). The margin between \(1/14\) or \(1/15\) and the puzzle’s radius \(1/16\) makes that plausible for sufficiently large \(p\), but it does not by itself supply a small effective \(P_0\).

Finally, even a complete proof that \(\gamma(p)\ge14\) for all large \(p\) would eliminate part (c) at those primes only. It would not settle or simplify parts (a) and (b).

## 5. Confidence

| p | Prediction | Confidence |
|---|---|---|
| 199 | 12 or less | 62% |
| 227 | 13 | 68% |
| 257 | 13 | 55% |
| 271 | 14 or more | 58% |
| 283 | 14 or more | 74% |
| 311 | 14 or more | 78% |
| 313 | 14 or more | 80% |
| 401 | 14 or more | 70% |

--- end verbatim ---
END LETTER
