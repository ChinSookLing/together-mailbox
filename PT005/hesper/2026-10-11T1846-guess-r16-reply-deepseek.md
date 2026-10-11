BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 18:49 +08
RE: 猜公式 Round 16 (packet d712a00), send text r16_send_full.txt or r16_send_short.txt
SEAT: deepseek
MODEL: DeepSeek DeepThink (19s)
CHAT: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202

--- reply verbatim ---
**ANSWER BLOCK**

**Q1.** PROOF: For an interval \(I\) of length \(L\), the forbidden set of \(v\) contributes at most \(2(vL+2)\) intervals of width \(1/(16v)\). So safe\((v)\) inside \(I\) has length at least
\[
L-\frac{2(vL+2)}{16v}
=\frac78 L-\frac{1}{4v}.
\]
Summing over the \(c(K)\) safe intervals of \(K\) gives
\[
m(K\cup\{v\})\ge \frac78 m(K)-\frac{c(K)}{4v}.
\]
The exhaustive check over all 13-sets with max \(\le30\) is UNFINISHED; I did not run code. Remaining cases: those with at least two speeds \(>30\).

**Q2.** IDEA: Iterate the inequality. With \(r\) large speeds,
\[
m(K_0\cup\{v_1,\dots,v_r\})\ge \left(\frac78\right)^r m(K_0)
-\sum_{j=1}^r \left(\frac78\right)^{r-j}\frac{c(K_{j-1})}{4v_j}.
\]
It breaks when \(c(K_{j-1})\) grows and the error exceeds \(97/6864\).

**Q3.** CONJ: \(m(K)\ge 97/6864\) for every 14-set. FACT: L17 gives only \(240^{-14}\approx 4.75\times10^{-34}\). UNFINISHED for a larger explicit constant.

**Q4.** IDEA: Scale only 13 speeds to \(\sim p^{1/13}\), leave the 14th large, then use Q1's discrete form. Explicit \(P_0\): UNFINISHED.

**Q5.** Needed lemmas: uniform floor (OPEN, hardest), discrete-to-continuous bridge (OPEN), effective scaling (OPEN), census to \(10^4\) (COMPUTATIONAL). To reach \(10^4\), all OPEN constants must improve drastically.

**Least-sure step:** the exhaustive 13-set verification in Q1.

**Work**

FACT: \(K^*=\{1,\dots,15\}\setminus\{6\}\). The two safe intervals in \([0,1/2]\) are
\[
[33/208,31/192],\qquad [11/64,31/176].
\]
Their lengths:
\[
\frac{31}{192}-\frac{33}{208}=\frac{7}{2496},\qquad
\frac{31}{176}-\frac{11}{64}=\frac{3}{704}.
\]
Sum:
\[
\frac{7}{2496}+\frac{3}{704}
=\frac{77}{27456}+\frac{117}{27456}
=\frac{194}{27456}
=\frac{97}{13728}.
\]
Doubling gives \(m(K^*)=97/6864\).

PROOF of Q1 inequality: In one period of length \(1/v\), the forbidden set of \(v\) is two intervals of total length \(1/8\). An interval \(I\) of length \(L\) meets at most \(vL+2\) periods, hence at most \(2(vL+2)\) forbidden intervals. Each has width \(1/(16v)\). Removing them leaves at least
\[
L-\frac{2(vL+2)}{16v}=\frac78L-\frac14v.
\]
Summing over the \(c(K)\) intervals of \(K\) gives the stated inequality.

IDEA for Q2: The iterative bound is valid but pessimistic because \(c(K_{j-1})\) can grow quickly. A sharper version would track only intervals that survive the previous intersections.

FACT: \(240^{14}\approx 2.10\times10^{33}\), so \(240^{-14}\approx 4.75\times10^{-34}\).

UNFINISHED: I did not execute any code, so all exhaustive counts and explicit \(P_0\) values are left open.

--- end verbatim ---
END LETTER
