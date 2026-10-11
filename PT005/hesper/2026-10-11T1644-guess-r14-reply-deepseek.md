BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 16:51 +08
RE: 猜公式 Round 14 (packet 1473ae0), send text r14_send_full.txt or r14_send_short.txt
SEAT: deepseek
MODEL: DeepSeek DeepThink
CHAT: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202

--- reply verbatim ---
PT005 Round 14 — verbatim final reply (captured via the reply's Copy button, 2026-10-11 ~16:46 SGT)
Chat: PT005 · Big Picture
Chat URL: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202
Model/mode: DeepSeek Chat (DeepThink ON / thinking ON, Search OFF); "Thought for 11 seconds" shown.
Attachment: r14_send_full.txt (3.11KB) — uploaded and shown attached.

VERBATIM REPLY BELOW (from the Reply's Copy, via writeText):

**ANSWER BLOCK**

**Q1.** UNFINISHED. I did not run code in this reply, so I report no D, E, or δ values. The code below would compute them; without execution, any number would violate Tuzi’s rule.

**Q2.** UNFINISHED for the empty-coset counts up to 20,000. IDEA: the Poisson picture predicts a constant fraction of empty cosets. Pólya–Vinogradov may already suffice asymptotically, because the interval length \(2H+1\approx p/8\) eventually dominates its error \(O(\sqrt p\log p)\). Burgess is stronger but likely unnecessary asymptotically; Weil is not directly an interval bound. Whether 281 is the last cover is UNFINISHED.

**Q3.** IDEA: the chair’s quick check is broadly right. Bounded differences gives only a constant exponent because one speed can change \(U\) by \(\Theta(p)\). Janson fails because the unsafe sets \(W_t\) overlap heavily. A structural tool is needed: Dirichlet scaling plus Fourier resonance.

**Q4.** Lemma plan: (1) L16 scaling to make speeds \(\lesssim p^{13/14}\) — PROVED/known. (2) Small speeds force many short relations — IDEA/FACT. (3) Uniform upper bound: for any 14-set, \(-R(S)\le(1-\delta)M(p)\) — OPEN, hardest. (4) Combine with \(U=M+R\) to get \(\delta(p)\ge\delta>0\) — OPEN.

**Q5.** IDEA: the plan should generalize to \(N\) runners by replacing 14 with \(N-2\) and \(H\) by \(\lfloor(p-1)/N\rfloor\), but constants and the hardest resonance bound change.

**Least-sure step:** Q2’s asymptotic claim that Pólya–Vinogradov suffices.

**Reasoning**

FACT: I cannot execute code here. Therefore every code-required number is UNFINISHED. Below is code shown but not run.

```python
# Q1: local search for small U(S) at N=16
import random, math

def U(S, p):
    n = (p-1)//2
    H = (p-1)//16
    cnt = 0
    for t in range(1, n+1):
        ok = True
        for v in S:
            r = (v*t) % p
            if min(r, p-r) <= H:
                ok = False
                break
        if ok:
            cnt += 1
    return cnt

def search(p, trials=100, steps=2000):
    n = (p-1)//2
    best = 10**9
    bestS = None
    for _ in range(trials):
        S = random.sample(range(1, n+1), 14)
        cur = U(S, p)
        T = 2.0
        for _ in range(steps):
            i = random.randrange(14)
            v = random.randrange(1, n+1)
            if v in S:
                continue
            newS = S.copy()
            newS[i] = v
            newU = U(newS, p)
            if newU <= cur or random.random() < math.exp((cur-newU)/T):
                S, cur = newS, newU
            T *= 0.999
        if cur < best:
            best, bestS = cur, S.copy()
    return best, sorted(bestS)
```

```python
# Q2: empty cosets of order-28 subgroup
def empty_cosets(p):
    # assumes p % 28 == 1
    H = (p-1)//16
    # find generator of order 28 subgroup
    # (requires primitive root; omitted for brevity)
    pass
```

IDEA for Q2: if every coset of the order-28 subgroup contains some \(r\) with \(|r|\le H\), then \(G_p\) is not a cover. To prove this, one needs an interval discrepancy bound for multiplicative characters of order dividing 28. Pólya–Vinogradov gives \(O(\sqrt p\log p)\), which is smaller than the average count \(O(p)\) for large \(p\), so it may suffice asymptotically. Burgess improves the exponent but is not needed for the asymptotic statement. Weil bounds are for polynomial sums over \(\mathbb F_p\), not directly for intervals.

IDEA for Q4: the hardest lemma is (3). It must control the Fourier resonance \(R(S)\) uniformly over all 14-sets, including the worst-case scaling from L16. Small speeds create many short relations, so this is exactly where cancellation is strongest. A proof must show that even this cannot reach the full cancellation \(R(S)=-M(p)\) for large \(p\).

Least-sure: the claim that Pólya–Vinogradov alone gives the needed coset emptiness for all large \(p\equiv1\pmod{28}\).
--- end verbatim ---
END LETTER
