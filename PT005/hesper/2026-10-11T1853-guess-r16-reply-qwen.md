BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 18:57 +08
RE: 猜公式 Round 16 (packet d712a00), send text r16_send_full.txt or r16_send_short.txt
SEAT: qwen
MODEL: Qwen3.8-Max Thinking
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
[Qwen3.8-Max Thinking. Assembled verbatim from Copy-button head + page-text reads (Copy display truncated); math in A2–B5 as rendered text, head in LaTeX source.]

ANSWER BLOCK

**Line A.**  
**Q1:** **PROOF:** a sharper one-speed bound is  
\[
m(K\cup\{v\})\ge \frac78 m(K)-\frac{9\,c(K)}{64v}.
\]
The requested finite check over primitive 13-subsets of \(\{1,\dots,30\}\) at worst \(v=31\): **UNFINISHED** (code shown). I hand-computed \(\binom{30}{13}=119{,}759{,}850\) total cases.  
**Q2:** Induction: \(m_{i+1}\ge \frac78m_i-\frac{9c_i}{64v_i}\), \(c_{i+1}\le c_i+v_i\). It breaks for close large speeds; my hand check shows consecutive \(31,32,33,34\) already drives this lower bound negative.  
**Q3:** I do **not** prove C-floor here. No unconditional \(c\ge 0.01\) is proved in this reply. The only explicit ledger constant available is L17’s conditional \(240^{-14}\). My own better constant: **UNFINISHED**.

**Line B.**  
**Q4:** Improved explicit \(P_0\) by selective scaling: **UNFINISHED**. The smallest explicit proved bound I can quote is L16’s \(P_0=120^{14}+1\) (conditional on F5); my hand log gives \(\log_{10}P_0\approx29.1085\). L17’s threshold has \(\log_{10}\approx486.7816\).  
**Q5:** To reach \(10^4\): C-floor **OPEN**; discrete transfer with \(o(p)\) error at \(10^4\) **OPEN**; non-Dirichlet core extraction **OPEN**; arithmetic exceptions **OPEN**. Dirichlet-style with \(Q\approx28/m^*\approx1981\) gives \(P_0\approx Q^{14}\approx10^{46.2}\), still ~42 decimal orders too high.

---

## Line A · one large speed

### A1. One-speed interval loss bound

**PROOF.** Let the safe set of \(K\) be a disjoint union of \(c=c(K)\) intervals
\[
A=\bigcup_{r=1}^c I_r,\qquad |I_r|=L_r,
\]
so \(m(K)=\sum_r L_r\).

For speed \(v\), the unsafe windows are
\[
W_v=\bigcup_{j=0}^{v-1}\left(\frac{j}{v}-\frac1{16v},\frac{j}{v}+\frac1{16v}\right),
\]
each of length \(1/(8v)\).

Fix one safe interval \(I\) of length \(L\). A window intersects \(I\) only if its center \(j/v\) lies in the interval expanded by \(1/(16v)\) on both sides, whose length is
\[
L+\frac1{8v}.
\]
The number of grid points \(j/v\) in any interval of length \(\ell\) on the circle is at most \(v\ell+1\). Therefore the number of \(v\)-windows intersecting \(I\) is at most
\[
v\left(L+\frac1{8v}\right)+1=vL+\frac98.
\]
Thus the length removed from \(I\) is at most
\[
\left(vL+\frac98\right)\frac1{8v}
=
\frac{L}{8}+\frac{9}{64v}.
\]
Summing over all \(c\) safe intervals, the total loss is at most
\[
\frac{m(K)}8+\frac{9c(K)}{64v}.
\]
Hence
\[
m(K\cup\{v\})
\ge m(K)-\frac{m(K)}8-\frac{9c(K)}{64v}
=
\frac78m(K)-\frac{9c(K)}{64v}.
\]
This is sharper than the requested \(\frac78m(K)-c(K)/(4v)\), since \(9/64<1/4\).

A still sharper but less convenient version is
\[
|I\cap W_v|
\le
\frac{1}{8v}\left\lfloor vL+\frac98\right\rfloor,
\]
and one may also cap this by \(L\).

### A1. Conditional finite reduction

**PROOF (conditional).** Suppose \(K'\) is a 13-set with all elements \(\le 30\), and \(v>30\). The bound
\[
\frac78m(K')-\frac{9c(K')}{64v}
\]
is weakest at the smallest allowed \(v\), namely \(v=31\). Therefore, if for every primitive 13-set \(K'\subset\{1,\dots,30\}\),
\[
\frac78m(K')-\frac{9c(K')}{64\cdot31}
\ge
\frac{97}{6864},
\]
then every 14-set whose largest element exceeds 30 and whose other 13 elements are \(\le30\) also satisfies
\[
m(K)\ge \frac{97}{6864}.
\]

**FACT (hand computation).** The number of 13-subsets of \(\{1,\dots,30\}\) is
\[
\binom{30}{13}=119{,}759{,}850.
\]
I computed this from
\[
\binom{30}{13}
=
\binom{30}{15}\frac{15\cdot14}{17\cdot16}
=
155{,}117{,}520\cdot\frac{105}{136},
\]
and
\[
155{,}117{,}520/136=1{,}140{,}570,\qquad
1{,}140{,}570\cdot105=119{,}759{,}850.
\]

**UNFINISHED.** I did not execute the exact interval computation over these 13-sets, so I cannot report which cases pass or fail.

A1. Code for the finite check

from fractions import Fraction as F
from itertools import combinations
from math import gcd
from functools import reduce

def merge(intervals):
    intervals = sorted(intervals)
    out = []
    for a, b in intervals:
        if not out or a > out[-1][1]:
            out.append([a, b])
        elif b > out[-1][1]:
            out[-1][1] = b
    return [(a, b) for a, b in out]

def safe_intervals(K, N=16):
    bad = []
    for k in K:
        r = F(1, N*k)
        for j in range(k):
            a = F(j, k) - r
            b = F(j, k) + r
            if a < 0:
                bad.append((F(0), b))
                bad.append((1 + a, F(1)))
            elif b > 1:
                bad.append((a, F(1)))
                bad.append((F(0), b - 1))
            else:
                bad.append((a, b))
    bad = merge(bad)
    safe = []
    cur = F(0)
    for a, b in bad:
        if a > cur:
            safe.append((cur, a))
        if b > cur:
            cur = b
    if cur < 1:
        safe.append((cur, F(1)))
    return safe

def m_and_c(K, N=16):
    S = safe_intervals(K, N)
    m = sum(b - a for a, b in S)
    c = len(S)
    return m, c

target = F(97, 6864)
bad_cases = []
for K in combinations(range(1, 31), 13):
    if reduce(gcd, K) != 1:
        continue
    m, c = m_and_c(K, 16)
    bound = F(7, 8) * m - F(9, 64) * F(c, 31)
    if bound < target:
        bad_cases.append((K, m, c, bound))
# bad_cases is the list of remaining cases for the one-large-speed step.

UNFINISHED. No output is reported because I did not run this code in this reply.

---

A2. Two or more large speeds

IDEA / PROOF of formal induction.
Let K_i be the set after adding i large speeds v_1,…,v_i, and let m_i = m(K_i), c_i = c(K_i).
Repeated use of the one-speed bound gives
m_{i+1} ≥ (7/8) m_i − 9 c_i / (64 v_{i+1}).

Also, adding speed v_{i+1} can increase the number of safe intervals by at most v_{i+1}, since there are only v_{i+1} unsafe windows and each can split at most one safe interval. Thus
c_{i+1} ≤ c_i + v_{i+1}.

Unrolling,
m_s ≥ (7/8)^s m_0 − Σ_{i=1}^s (7/8)^{s−i} · 9 c_{i−1} / (64 v_i).

FACT (hand computation showing where this breaks).
Start with K_0 = ∅, so m_0 = 1, c_0 = 1. Try consecutive large speeds 31, 32, 33, 34.

Step 1, v=31: m_1 ≥ 7/8 − 9/(64·31) = 0.875 − 9/1984 ≈ 0.87046, and c_1 ≤ 31.
Step 2, v=32: m_2 ≥ (7/8)(0.87046) − (9·31)/(64·32) ≈ 0.76166 − 0.13623 ≈ 0.62543, and c_2 ≤ 31+32 = 63.
Step 3, v=33: m_3 ≥ (7/8)(0.62543) − (9·63)/(64·33) ≈ 0.54725 − 0.26847 ≈ 0.27878, and c_3 ≤ 63+33 = 96.
Step 4, v=34: m_4 ≥ (7/8)(0.27878) − (9·96)/(64·34) ≈ 0.24393 − 0.39706 < 0.

So this crude induction cannot handle several close large speeds.

IDEA. The induction should work if the large speeds grow fast enough, because then c_i / v_{i+1} is small. It breaks when large speeds are close together, because the boundary error terms accumulate and the interval count grows.

---

A3. Constant status

OPEN. I cannot prove m(K) ≥ 97/6864 for all 14-sets K.

KNOWN (ledger L17, conditional on F5). An explicit but very small uniform floor is m(K) ≥ 240^{−14} for every 14-set K.

UNFINISHED. I do not obtain an unconditional explicit c ≥ 0.01 in this reply.

---

Line B · threshold

B4. Replacing Dirichlet

IDEA. The desired replacement would be:
- Scale so that a small core K_0 is bounded, perhaps even K_0 = {1}.
- Treat remaining speeds using the discrete analogue of the one-large-speed bound: each safe interval loses about 1/8 of its cells, plus a boundary error of order 1/v.
- If the safe core has sufficiently many interval components under control, iterate this to get a positive linear lower bound for U(S).

UNFINISHED. I cannot turn this into an explicit P_0 in this reply.

FACT (hand log of existing explicit bounds). The L16 bound gives p > 120^14 ⇒ γ(p) = 15, so one may take P_0 = 120^14 + 1. I compute log_10(120) = 2.079181246…, 14 log_10(120) = 29.1085374…, so 120^14 ≈ 1.28 × 10^29.

The L17 threshold quoted in the packet is p ≥ (28 · 240^14)^14 + 1. I compute log_10(240) = 2.380211242…, 14 log_10(240) = 33.3229574…, log_10(28) = 1.447158031…, so log_10(28 · 240^14) = 34.7701154…, and therefore 14 · 34.7701154… = 486.781615…. Thus the L17 threshold is about 6.05 × 10^486.

FACT (hand computation of a naive Dirichlet-style target). If one needed 28/Q < m* = 97/6864, then Q > 28/m* = (28·6864)/97 = 192192/97 = 1981 + 35/97 ≈ 1981.36. Then a Dirichlet-all-small proof with p ≳ Q^14 would give log_10 Q ≈ 3.29697, 14 log_10 Q ≈ 46.1576, so P_0 ≈ 1.4 × 10^46. If one needs a safety factor of 2, Q ≈ 3962.72, giving 14 log_10 Q ≈ 50.37, or about 2.3 × 10^50. These are still enormously above 10^4.


B5. What would close the gap to 10^4?
Lemma list.
Lemma | Status | Distance to 10^4
- C-floor: m(K) ≥ 97/6864 for all 14-sets — OPEN. Exhaustive to max ≤ 30 is known from other seats, but I did not recompute it; one-large reduction needs the finite check above; multi-large case open.
- Discrete transfer: U(S) ≥ p/2 · m(K) − E with E < p/2 · m* − 1 at p = 10^4 — OPEN. L17-style bounds are off by hundreds of decimal orders; my hand estimate gives L17 threshold ~10^486.78.
- Core extraction without all-small Dirichlet — OPEN. Dirichlet with Q ≈ 28/m* ≈ 1981 would require p ≳ Q^14 ≈ 10^46.2, still ~42 decimal orders above 10^4.
- Control of arithmetic exceptions (subgroups, run-type resonances) — OPEN. Subgroup Poisson picture predicts linearly many empty cosets, but no explicit proof is given here.

IDEA. The critical missing step is a discrete transfer lemma that does not require making all speeds bounded by a constant. The one-large-speed inequality is the continuous form of such a lemma; a discrete version with explicit grid errors is the natural next object to prove.

UNFINISHED. I do not have an explicit P_0 = 10^4-compatible proof.

--- end verbatim ---
END LETTER
