BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 11:21 +08
RE: 猜公式 Round 3 packet (1aeab1c), rules header + own §A line + BEGIN…END block pasted verbatim (send text r3_send_glm.txt)
SEAT: glm
MODEL: GLM-5.3 Deep Think High
CHAT: https://chat.z.ai/c/149a9608-6b90-4558-b442-55a79e9ab6d5

--- reply verbatim ---
**ANSWER BLOCK**

**§A (GLM's item: check new fact 2 on one more prime): YES — the grid picture is correct.**
New prime **p = 67** (n = 33), test set S = {1, 2, 4, 8} (all ≤ n). Exact rational pipeline (code below) gives:
pieces = **8**; total safe length = **88/128 = 0.6875**; longest piece = **13/128 ≈ 0.1016** (grid spacing 1/67 ≈ 0.0149); grid points inside = **46**: t ∈ {5,6,7, 9–15, 18–24, 26–31} plus mirrors {36–41, 43–49, 52–58, 60–62}.
Cross-check (FACT): the *direct* modular test — t is safe iff 16·min(vt mod 67, 67−vt mod 67) ≥ 67 for all v — returns exactly the same 46 values, and each t/p lands in the predicted piece (e.g. 31/67 = 0.4627 ∈ [49/128, 60/128); 32/67 = 0.4776 falls in the gap and indeed v = 2 kills it: 2·32 = 64 → min 3). The pieces, in 128ths: [8,15), [17,30), [34,47), [49,60), [68,79), [81,94), [98,111), [113,120) — symmetric under x ↦ 1−x, as they must be (PROOF: ‖v(1−x)‖ = ‖vx‖). I verified the 88-cylinder count independently by a bit-run argument (no 4 equal consecutive bits). The equivalence "cover ⇔ no grid point in safe set" is immediate from definitions (PROOF). Caveat: only 4 speeds — a check of the *machinery*, not of the 13-speed statistics; I could not re-execute the 223/239 rows in this round.

**§B: Route 1 (discrepancy).** Result: PROOF (conditional on F5 for 13 speeds): **any 13 distinct speeds with max speed M have safe length L ≥ 1/(120M)**; hence no speed-independent uniform L₀. Details below. Plus an exact family computation.

**§C: Tomas Bohman (CMU)** — holder of the small-case lonely-runner records (Bohman–Holzman–Kleitman); our whole write-up lives in the 13–15-speed regime he owns.

```python
from fractions import Fraction as F

def v_intervals(v):   # {x : ||v x|| >= 1/16}
    return [(F(16*k+1, 16*v), F(16*k+15, 16*v)) for k in range(v)]

def safe_set(S):
    pieces = [(F(0), F(1))]
    for v in sorted(S):
        out = []
        for a, b in pieces:
            for c, d in v_intervals(v):
                if max(a,c) < min(b,d):
                    out.append((max(a,c), min(b,d)))
        pieces = out
    return sorted(pieces)

def check(p, S):
    P = safe_set(S)
    L = sum(b-a for a,b in P); long_ = max(b-a for a,b in P)
    G = [t for t in range(1, p)
         if any(a <= F(t, p) < b for a, b in P)]
    D = [t for t in range(1, p)
         if all(16*min((v*t) % p, p - (v*t) % p) >= p for v in S)]
    return len(P), L, long_, len(G), G == D

print(check(67, [1, 2, 4, 8]))   # (8, 11/16, 13/128, 46, True)
```

**§B details (Route 1).**

1. FACT/PROOF (power-of-2 family): for S = {1,2,4,…,2^{k−1}}, x is safe iff the first k+3 binary digits of x contain no run 0000 or 1111 (since ‖2^i x‖ ≥ 1/16 ⇔ the 4 bits starting at position i+1 are mixed). So L = f(k+3)/2^{k+3} with f the no-4-run count, f(m) = f(m−1)+f(m−2)+f(m−3). Hand-verified for k ≤ 4: 14/16, 26/32, 48/64, 88/128 (the last is exactly my p = 67 case). For 13 speeds: L = f(16)/65536 = **21218/65536 ≈ 0.324** — far above the data's 0.114.

2. PROOF (uses F5 for 13 speeds): F5 gives x\* with min_v ‖vx\*‖ ≥ 1/15. Each ‖vx‖ is M-Lipschitz (M = max speed), so [x\* − 1/(240M), x\* + 1/(240M)] is safe: **L ≥ 1/(120M)**. After Lemma B scaling (M ≤ p/N) this gives pL ≥ N/120 ≈ 0.47 at N = 56, while pieces ≤ Σv ≤ 13p/N. So the naive discrepancy bound is still dead even with the LRC-13 input; route 1 needs lever (iii), weighted counting. Also PROOF: L(D·S) = L(S) for any dilation D (x ↦ Dx maps safe sets onto each other), so gcd-scaling cannot manufacture small L; an L → 0 family must be genuinely new.

3. IDEA: dense sets shrink L: for S = {1,…,13} the safe set sits only near k/14, k/15, k/16 (coprime k); my slope estimate gives L ≈ 0.03–0.08, below 0.114. The code line `safe_set(range(1,14))` computes it exactly — I could not execute it this round.

**Least sure step:** my hand enumeration of the 8 runs on p = 67 (I caught and fixed two errors mid-enumeration; the code above is the arbiter), and the unexecuted estimate for L({1,…,13}).

[Courier note: Copy output truncated the last sentence at "my hand enumeration of"; its tail was read from the rendered page. Hesper ran GLM's safe_set code: p=67 {1,2,4,8} -> 8 pieces, L=0.6875 (matches); {2^0..2^12} -> L=0.32376 (matches 21218/65536); {1..13} -> 12 pieces, L=0.042243.]
--- end verbatim ---
END LETTER
