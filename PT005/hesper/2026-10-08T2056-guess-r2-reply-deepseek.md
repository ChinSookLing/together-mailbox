BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-08 20:57 +08
RE: 猜公式 Round 2 packet (aaa37b9), BEGIN…END block pasted verbatim
SEAT: deepseek
MODEL: DeepSeek (Tuzi's phone app; relayed by Tuzi in Hark chat 20:56 +08; supersedes f9d2189 as the Round 2 answer)
CHAT: Tuzi's own DeepSeek app (no URL)

--- reply verbatim ---
1. Referee T1

Lemma A — YES.
The argument is correct. LRC(14) is applied to exactly 13 distinct positive integers w_1,\dots,w_{13}, giving real x with \|w_i x\|\ge 1/14. Let t be the nearest integer to xp. Then

\|w_i t/p\|\ge \|w_i x\|-|w_i|\,|x-t/p|
\ge 1/14 - M/(2p)
\ge 1/14-1/112=1/16.


Since “too near” requires strict <1/16, this is enough. The step t\not\equiv 0\pmod p is also correct. If t\notin\{1,\dots,n\}, replace t by its sign-normalized cell representative; the norm is unchanged.
Weakest point: rounding from real x to integer t costs a factor p, which is exactly what makes the threshold huge.

Lemma B — YES.
Dirichlet’s simultaneous approximation gives 1\le q\le N^{13}\le p-1 with

\|q s_i/p\|\le 1/N.


Thus q s_i\equiv \pm c_i\pmod p with 1\le c_i\le p/N. If c_i=c_j, then q s_i\equiv \pm q s_j\pmod p, so s_i\equiv \pm s_j\pmod p, contradicting that the speeds are distinct up to sign. Nonzero is clear because s_i\ne0.
Weakest point: this is generic Dirichlet and does not use the special cover structure at all.

Final step — YES.
If a 13-cover S existed, then by F2 its scaled version qS would also be a 13-cover. Up to sign it is \{c_1,\dots,c_{13}\} with all c_i\le p/N. Lemma A with M=p/N requires

p\ge 56M=56p/N \iff N\ge 56 \iff p-1\ge 56^{13}.


So for p>56^{13}, qS is not a cover, contradiction. Therefore \gamma(p)\ge14.
Weakest point: dependence on F5, the computer proof of LRC(14).

Overall: T1 is correct as written, modulo F5. Its main defect is not logical but quantitative: it pays the full generic Dirichlet exponent 1/13.

---

2. Shrink the threshold

Several levers are plausible. I label them.

(a) Better margin / intervals — IDEA.
Instead of using a single real x from LRC(14), use an interval of good times. If the good set for speeds \le M contains an interval of length L, then rounding error M/(2p) can be absorbed whenever p>M/L. For 13 speeds \le M, bad times are unions of intervals of length roughly 1/(8M) around rationals with denominator \le M. A useful gap theorem could reduce the threshold from M^{13} to something like M^2. This is probably the cleanest theoretical lever.

(b) Better scaling via cover structure — IDEA.
A 13-cover is very special: 13 sets of size H\approx p/16 cover n\approx p/2 cells, so the average multiplicity is 13/8=1.625. The sets cannot be independent random sets; their intersections are forced. This may imply that the speeds cannot all be scaled to size \sim p^{12/13}. If one could prove any 13-cover can be scaled to speeds \le C p^{1/2}, the threshold would drop to roughly p\sim C^2 56^2, i.e. a few thousand. That would be decisive for the gates.

(c) Character / Fourier counting — IDEA.
For a fixed set S of 13 speeds, the number of uncovered cells is

U(S)=\sum_{t=1}^{n}\prod_{v\in S}\bigl(1-\mathbf 1_{\|vt/p\|<1/16}\bigr).


The main term is roughly n(7/8)^{13}>0. To have a cover, all lower-order Fourier corrections must cancel exactly. For large p, that cancellation is extremely rigid. A careful exponential-sum estimate could give \gamma(p)\ge14 for p above a much smaller P_0.

(d) Hybrid — IDEA.
Prove an improved T1 for p>P_1 using one of the levers above, then certify p\le P_1 computationally. The gate engine is expensive, but for P_1\sim10^6 a SAT/SMT or branch-and-bound set-cover search with symmetry breaking may be feasible. It would be much cheaper than exhaustive search over all primes to 10^{22}.

Weakest step in T1 to attack: Lemma B. The Dirichlet exponent 1/13 is the sole source of the 10^{22} threshold.

---

3. The 14 question

F3 already gives \gamma(p)\le15 for every prime p>16. So for large p, the only possible values are 14 or 15. T2, if correct, proves \gamma(p)=15 for p>120^{14}. Thus the natural expectation is:

For all sufficiently large primes, \gamma(p)=15.
There may be finitely many primes with a 14-cover, but no infinite family, unless T2 or its improved version fails for a structural reason. A 14-cover would have average multiplicity 14/8=1.75, still very tight; counting and Fourier obstructions should eventually rule it out. The data already shows 13-covers dying near p=277, so 14-covers are likely a finite transient before the stable value 15.

\gamma(p) should not keep growing: it is capped at 15 by F3.

---

4. One sentence for Tuzi

The single most promising lever is better scaling using the cover structure to force a much smaller multiplier q — ideally q\le p^{1/2} or less — because the generic Dirichlet exponent 1/13 is what creates the 20-order-of-magnitude gap between T1 and the observed threshold near 280.

--- end verbatim ---
END LETTER
