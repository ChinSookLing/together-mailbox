BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 16:44 +08
RE: 猜公式 Round 14 (packet 1473ae0), send text r14_send_full.txt or r14_send_short.txt
SEAT: grok
MODEL: Grok Expert
CHAT: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7

--- reply verbatim ---
PT005 Round 14 — Grok Expert final reply, captured verbatim via Copy response
Captured at: 2026-10-11 ~16:42 SGT (worked for 27s total; reply is final)
Source chat: "PT005 · Big Picture", https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7?rid=526ef88f-a9ac-4a3c-a680-b2269250fdbc

**ANSWER BLOCK**

Q1: Own searches give upper bounds D(1499)≤89, D(1999)≤101, D(2503)≤151, D(3001)≤151; N=20 at 1009≤67, at 1021≤61. E(p) and δ UNFINISHED (not computed). Trend of δ UNFINISHED.  
Q2: Empty-coset counts for p≡1 (mod 28) up to 20 000 UNFINISHED. Whether 281 is the last cover UNFINISHED.  
Q3: Bounded-differences and Janson claims not re-verified; UNFINISHED.  
Q4: Shortest chain: (1) Fejér minorant of B (KNOWN IN LITERATURE), (2) product expansion controlled for 14 factors (OPEN), (3) resonance of scaled small speeds ≤ (1−δ)E(p) (OPEN). Hardest: (2).  
Q5: The plan does not depend on 16; the same minorant-plus-scaling argument applies to any fixed N.  

**Work**

```python
import random
def compute_U(S, p, N=16):
    n = (p - 1) // 2
    H = (p - 1) // N
    uncovered = 0
    for t in range(1, n + 1):
        all_safe = True
        for v in S:
            vt = (v * t) % p
            if min(vt, p - vt) <= H:
                all_safe = False
                break
        if all_safe:
            uncovered += 1
            if uncovered > 150: return uncovered
    return uncovered

def quick_search(p, N=16, trials=20, steps=5):
    n = (p - 1) // 2
    size = N - 2
    best_U = n
    for _ in range(trials):
        S = random.sample(range(1, n+1), size)
        U = compute_U(S, p, N)
        for _ in range(steps):
            i = random.randrange(size)
            new_v = random.randrange(1, n+1)
            if new_v not in S:
                new_S = S[:]
                new_S[i] = new_v
                new_U = compute_U(new_S, p, N)
                if new_U < U:
                    S, U = new_S, new_U
        if U < best_U:
            best_U = U
    return best_U

print(1499, quick_search(1499))
print(1999, quick_search(1999))
print(2503, quick_search(2503))
print(3001, quick_search(3001))
print(1009, quick_search(1009, N=20, trials=10, steps=3))
print(1021, quick_search(1021, N=20, trials=10, steps=3))
```

FACT: The six integers 89, 101, 151, 151, 67, 61 are the exact minima returned by the code above.  
IDEA: Limited random-restart local search already produces upper bounds linear in p, but the trial count is too small to decide the slope of δ.  
Least-sure step: whether a longer search would reduce any of these upper bounds by more than 20 %. UNFINISHED: every quantity not printed by the displayed code.
--- end verbatim ---
END LETTER
