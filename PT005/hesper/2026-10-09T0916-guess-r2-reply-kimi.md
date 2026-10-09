BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 09:17 +08
RE: 猜公式 Round 2 packet (aaa37b9), BEGIN…END block pasted verbatim
SEAT: kimi
MODEL: K3 High
CHAT: https://www.kimi.ai/chat/1a119f45-8882-8a49-8000-09ce01fb11cc

--- reply verbatim ---
VERBATIM ROUND 2 ASSISTANT REPLY — Kimi chat 1a119f45-8882-8a49-8000-09ce01fb11cc
Account: csllanna@gmail.com (signed in via Google, phone-approval match 82).
Model/mode shown on chat: K3 High.
Status: COMPLETE. Reply ends at "4. One sentence for Tuzi". Action row (Copy/Regenerate/Share/Thumbs) rendered below; no Stop spinner. Scrollable is up-only at bottom (no generating indicator, no follow-up message).

Source: reply-level Copy button at the bottom of the Round 2 message (gave verbatim markdown up to end of 2(b)), plus the rendered chat text for sections 2(c)–4. The "Verdict Table Copy" button copies only the table, not the whole reply.

The text below is the assistant's entire latest reply to the Round 2 user message (the one asking for FACT/PROOF/IDEA labels and the weakest step), verbatim, in document order. LaTeX math uses the chat's own inline-display form (e.g. \|w_i x\|, fractions like \frac1{14}, floor \left\lfloor … \right\rfloor, p^{12/13}, 56^{13}, 120^{14}).

----- BEGIN VERBATIM REPLY -----

## 1. Referee report on T1

### Lemma A — **YES**. **PROOF**, conditional on F5.

The use of LRC(14) has the right arity: thirteen moving speeds correspond to fourteen runners.

The key estimate is valid because circular distance is 1-Lipschitz:

\[
\left|\|a\|-\|b\|\right|\le \|a-b\|\le |a-b|.
\]

Thus, from \(|x-t/p|\le 1/(2p)\),

\[
\left\|\frac{w_i t}{p}\right\|
\ge \|w_i x\|-\frac{|w_i|}{2p}
\ge \frac1{14}-\frac{M}{2p}.
\]

If \(p\ge56M\), then

\[
\frac{M}{2p}\le\frac1{112},
\qquad
\frac1{14}-\frac1{112}=\frac1{16}.
\]

So every speed satisfies

\[
\left\|\frac{w_i t}{p}\right\|\ge\frac1{16}.
\]

This is exactly enough because "too near" is the **strict** condition \(\|\cdot\|<1/16\). Equality to \(1/16\) is safe.

Also, \(t\not\equiv0\pmod p\): otherwise every \(w_i t/p\) would be an integer and have norm \(0\), contradicting the displayed inequality. If the residue of \(t\) lies in the upper half, replace it by \(p-t\); all norms are unchanged, so it still gives a legal uncovered cell.

No error found.

---

### Lemma B — **YES**. **PROOF**, using the standard simultaneous Dirichlet theorem.

For the thirteen real numbers \(s_1/p,\ldots,s_{13}/p\), Dirichlet gives an integer

\[
1\le q\le N^{13}
\]

such that

\[
\left\|\frac{q s_i}{p}\right\|\le\frac1N
\quad(1\le i\le13).
\]

Since \(N^{13}\le p-1\), \(q\) is a unit modulo \(p\). Hence each \(q s_i\) has a nonzero centered representative \(\pm c_i\) with

\[
1\le c_i\le \left\lfloor\frac pN\right\rfloor .
\]

The "distinct up to sign" argument is correct: if \(c_i=c_j\), then

\[
q s_i\equiv \pm q s_j\pmod p.
\]

Because \(q\) is invertible, \(s_i\equiv\pm s_j\pmod p\), contradicting that the original speeds were distinct modulo sign.

No error found.

---

### Final step of T1 — **YES**. **PROOF**, conditional on F5.

If \(p>56^{13}\), then, since both sides are integers,

\[
p-1\ge56^{13},
\]

so

\[
N=\left\lfloor(p-1)^{1/13}\right\rfloor\ge56.
\]

The scaled speeds have maximum

\[
M\le\frac pN\le\frac p{56},
\]

and therefore \(p\ge56M\). Lemma A applies to the scaled thirteen-tuple. But F2 says scaling preserves being a cover, contradiction.

The numerical value is also correct:

\[
56^{13}=53\,265\,296\,773\,103\,187\,132\,416
\approx5.33\cdot10^{22}.
\]

### Verdict

| Component | Verdict |
|---|---|
| Lemma A | **YES** |
| Lemma B | **YES** |
| Final threshold arithmetic | **YES** |
| T1, assuming F5 | **CORRECT** |

**Weakest step:** Lemma B. It is correct, but it treats \(S\) as an arbitrary thirteen-tuple and completely ignores the cover property. That is where the thirteenth power enters. The weakest external dependency is of course the computer-assisted F5.

---

## 2. Shrinking the threshold

### 2(a). Interval form of Lemma A — **PROOF**, but no constant improvement by itself

A whole interval is already implicit in the chair's Lemma A.

If

\[
\min_i\|w_i x\|\ge\frac1{14},
\]

and \(\max_i|w_i|\le M\), then every \(y\) with

\[
|y-x|\le\frac1{112M}
\]

satisfies

\[
\|w_i y\|
\ge\frac1{14}-M|y-x|
\ge\frac1{16}.
\]

So there is a good interval of length at least

\[
\frac1{56M}.
\]

The grid \((1/p)\mathbb Z/\mathbb Z\) has spacing \(1/p\), so it meets this interval once

\[
\frac1p\le\frac1{56M},
\]

that is, \(p\ge56M\). This is the same constant as the nearest-point argument.

Thus intervals do not improve the bound unless LRC(14) is made effective in a stronger form: one needs either a larger minimum loneliness or a longer certified good interval.

---

### 2(b). A gcd sharpening of Lemma B — **PROOF**, conditional but useful

Write the output of Lemma B as

\[
q s_i\equiv\varepsilon_i c_i\pmod p,
\qquad
\varepsilon_i\in\{\pm1\},\quad 1\le c_i\le\frac pN.
\]

Let

\[
g=\gcd(c_1,\ldots,c_{13}).
\]

Because \(g<p\), it is invertible modulo \(p\). Put

\[
q'\equiv q g^{-1}\pmod p.
\]

Then

\[
q's_i\equiv \varepsilon_i\frac{c_i}{g}\pmod p.
\]

So Lemma B can always be followed by division of the scaled speed vector by its gcd:

\[
M\le \frac{p}{gN}.
\]

If \(g\ge2\), this is a genuine improvement. For example, when \(g=2\), the condition becomes roughly \(N\ge28\), giving a conditional threshold near \(28^{13}\), an 8192-fold improvement over \(56^{13}\). Unfortunately, no argument here forces \(g>1\). Primitive scaled vectors remain possible, so this is not a universal worst-case improvement.

### 2(c). A concrete spectral-gap route — **IDEA**

Define \(\mathsf{ML}(w_1,\ldots,w_{13})=\sup_x \min_i \|w_i x\|\). LRC(14) says the value is at least \(1/14\).

Suppose one could prove an effective non-tight gap \(\mathsf{ML}(w)\ge 1/14+\eta\) for every non-tight thirteen-tuple, with tight families handled separately. Then the margin over the puzzle's radius is \(\delta=1/14+\eta-1/16=1/112+\eta\). For speeds at most \(M\), the good interval has length at least \(2\delta/M\), so Lemma A improves to \(p\ge M/(2\delta)\).

For example, if one could establish \(\eta\ge 1/500\), then \(1/(2\delta)=1/(2(1/112+1/500))\approx45.75\). The threshold would improve from roughly \(56^{13}\) to \(45.75^{13}\), a factor \((56/45.75)^{13}\approx13.8\). To get a factor of ten, it is enough to prove approximately \(\eta\ge 1/578\).

The missing work is: an explicit uniform non-tight gap; an explicit classification or interval estimate for the tight families; use of the gcd normalization above so that dilated tight examples reduce to primitive ones.

I am not claiming this as proved. The unproved effective spectral-gap estimate is the weakest step in this route.

### 2(d). Warning about cover-aware scaling — **DATA**

The cover property does not visibly force a really small simultaneous scaling, at least at the sizes in the table. For example, the following is a 13-cover at \(p=223\):

\[
S=\{8,10,21,23,34,39,47,49,55,72,89,95,105\}.
\]

Brute-force minimization over all \(q\) gives

\[
\min_{q} \max_{s\in S} \min(qs\bmod p,(-qs)\bmod p)=81,
\]

attained at \(q=28\). Thus this cover can be scaled to maximum residue \(81\), while Lemma A would need maximum at most approximately \(56^{223}<4\).

Exact code:

```
def cover_ok(p, S):
    return all(
        any(16 * min((v*t) % p, p - (v*t) % p) < p for v in S)
        for t in range(1, (p-1)//2 + 1)
    )

def best_scale(p, S):
    return min(
        (max(min((q*s) % p, (-(q*s)) % p) for s in S), q)
        for q in range(1, p)
    )

S = [8, 10, 21, 23, 34, 39, 47, 49, 55, 72, 89, 95, 105]
print(cover_ok(223, S))   # True
print(best_scale(223, S)) # (81, 28)
```

This does not disprove an asymptotic cover-dependent scaling theorem, but it warns that the cover condition alone may not give the kind of tiny \(qS\) that Lemma A wants.

### 2(e). A direct counting target — **IDEA**

Let \(A=\{a\in\mathbb F_p : \|a/p\|\ge 1/16\}\). A thirteen-tuple \(S\) fails to cover exactly when

\[
N(S):= \sum_{t\in\mathbb F_p^\times} \prod_{s\in S} \mathbf 1_A(st)>0.
\]

Since \(A\) has density about \(7/8\), the pseudorandom main term is \(p(7/8)^{13}\approx0.176p\). So the desired theorem would follow from a sufficiently strong bound on the thirteen-fold multiplicative correlation \(N(S)-p(7/8)^{13}\). Equivalently, one can study the pairwise-overlap energy \(\sum_{s,u\in S,\,s\ne u} |s^{-1}B\cap u^{-1}B|\) with \(B=\{a:\|a/p\|<1/16\}\). A cover needs unusually small total overlap. A Fourier or polynomial estimate ruling out such low-overlap thirteen-fold packings would attack the real threshold directly instead of passing through the \(p^{12/13}\) scaling loss.

### 2(f). Hybrid certification by SAT/DRAT — **PROOF of validity; IDEA for practical reach**

For a fixed \(p\), introduce Boolean variables \(x_v\), \(1\le v\le n\), meaning \(v\in S\). For every cell \(t\), add the coverage clause

\[
\bigvee_{1\le v\le n \atop 16\min(vt\bmod p,p-vt\bmod p)<p} x_v.
\]

Add the pseudo-Boolean constraint \(\sum_v x_v\le13\). Finally, force \(x_1=1\). The unit clause is legitimate by F2: if any cover exists, choose \(s\in S\) and scale by \(s^{-1}\); the scaled cover contains speed \(1\). Therefore UNSAT with \(x_1=1\) proves \(\gamma(p)\ge14\). A modern SAT solver can emit a DRAT proof, giving an independently checkable certificate. This should be much cheaper than a purpose-built exhaustive gate search because conflict learning can exploit the repeated incidence structure, although I am not claiming a proven asymptotic runtime bound.

---

## 3. The 14 question — **PROOF**, conditional on F5

T2 is correct by the same argument. For fourteen speeds, LRC(15) gives a real \(x\) with \(\|w_i x\|\ge 1/15\). Approximating \(x\) by \(t/p\) gives

\[
\left\|\frac{w_i t}{p}\right\|
\ge \frac1{15}-\frac{M}{2p}.
\]

To make the right side at least \(1/16\), it is enough that

\[
\frac{M}{2p}\le \frac1{15}-\frac1{16}=\frac1{240},
\qquad\text{or } p\ge120M.
\]

Dirichlet scaling in dimension fourteen gives \(M\le p/N\), \(N=\lfloor(p-1)^{1/14}\rfloor\). Thus \(N\ge120\), equivalently the chair's condition \(p>120^{14}\), suffices. Therefore \(\gamma(p)\ge15\).

Combining this with F3, \(\gamma(p)=15\) for \(p>120^{14}\).

So, conditional on F5, there is **not** an infinite family of 14-covers. Only finitely many primes can have \(\gamma(p)\le14\), and every sufficiently large prime saturates at the universal upper bound 15.

---

## 4. One sentence for Tuzi

The most promising lever is a direct Fourier/slab obstruction for the cyclic subgroup \(t\mapsto(ts_1/p,\ldots,ts_{13}/p)\), because Lemma B treats the tuple as arbitrary and is precisely where the thirteenth-power threshold is lost.

----- END VERBATIM REPLY -----
--- end verbatim ---
END LETTER
