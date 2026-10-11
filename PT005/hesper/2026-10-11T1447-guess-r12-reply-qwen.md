BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 14:52 +08
RE: 猜公式 Round 12 (packet c9a646a), send text r12_send_full.txt or r12_send_short.txt
SEAT: qwen
MODEL: Qwen3.8-Max Thinking
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
=== PT005 Round 12 — Response 2 (selected), verbatim ===
Model shown: Qwen3.8-Max (Thinking mode). Comparison mode returned two responses; Response 2 was chosen (more complete: included ANSWER BLOCK with all 5 Qs, code, M(p) hand computations for 8 primes, PROOF of M(p), Q3 extreme-value model, Q4 Fourier bound with PROVED/NOT PROVED, and Q5 predictions for 503/547/577/599 with confidences). Response 2's own indicator showed "2/2" at the end, meaning the message was fully delivered.

Note: Qwen's Reply was in comparison mode (two side-by-side responses). Response 2 was selected by clicking its "I prefer this response" button; Qwen then promoted it to the chat as the standing reply. No Copy button was present on the promoted reply in this chat (only Copy existed on prior-round replies; the Round 12 reply surfaced no Copy control in the element list), so the reply below was captured by reading the page text via find_text/extract_content in overlapping chunks and stitched verbatim. The text matches what was shown to the user on screen.

--- BEGIN VERBATIM REPLY (Response 2) ---

Thinking completed
ANSWER BLOCK
Q1:
Code provided below (simulated annealing search). Search results: UNFINISHED (cannot execute code in this reply). M(p) hand-computed for 7 primes: 431→34.3, 449→33.6, 461→35.0, 499→37.7, 601→46.5, 701→54.8, 809→62.5, 1009→76.7.
Q2:
UNFINISHED (requires search data). However, M(p) ≈ 0.076p is linear; D(p) likely grows more slowly due to optimization over ~C(n,14)/n sets.
Q3:
IDEA:
Extreme-value reasoning: D(p) is the minimum of ~N = C(n,14)/n approximately-Poisson(M(p)) variables. When N·e^{-M(p)} ≫ 1, D=0; when ≪ 1, D grows. Transition at M(p) ≈ ln N ≈ 13 ln(p/2) − 25.
Q4:
IDEA:
If |R(S)| ≤ c·M(p) with c < 1 provable via Fourier, then D(p) ≥ (1−c)·0.076p. Round 11 shows R₄/M ≈ −0.66 universally, suggesting c ≈ 0.7–0.9 is plausible. P₀ could reach ~10⁴–10⁵, far below 120¹⁴ ≈ 10²⁹.
Q5:
503: 0 (55%), 547: ≥4 (60%), 577: ≥4 (60%), 599: ≥4 (65%).

Q1 Code (simulated annealing for D(p)):
python
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
import numpy as np
import random

def compute_D(p, iters=500000, T0=5.0, T_min=0.01, cooling=0.99995):
    n = (p - 1) // 2
    H = (p - 1) // 16

    def U_of_set(S):
        """Count cells where ALL speeds are safe."""
        count = 0
        for t in range(1, n + 1):
            all_safe = True
            for v in S:
                r = (v * t) % p
                if min(r, p - r) <= H:
                    all_safe = False
                    break
            if all_safe:
                count += 1
        return count

    def random_set():
        return sorted(random.sample(range(1, n + 1), 14))

    def neighbor(S):
        S2 = list(S)
        i = random.randint(0, 13)
        while True:
            v = random.randint(1, n)
            if v not in S2:
                S2[i] = v
                break
        return sorted(S2)

    best_S = random_set()
    best_U = U_of_set(best_S)
    S = list(best_S)
    U = best_U
    T = T0
    for it in range(iters):
        S_new = neighbor(S)
        U_new = U_of_set(S_new)
        if U_new < U or random.random() < np.exp((U - U_new) / max(T, 0.01)):
            S, U = S_new, U_new
            if U < best_U:
                best_U, best_S = U, list(S)
            if best_U == 0:
                break
        T *= cooling
    return best_U, best_S

# Run for primes 431-499 and sample from 601-1009
primes_431_499 = [431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
primes_601_1009 = [601, 641, 701, 751, 809, 907, 1009]
for p in primes_431_499 + primes_601_1009:
    D, S = compute_D(p)
    print(f"p={p}: D={D}, S={S}")

M(p) hand computations (FACT):

p     H   2H+1  (2H+1)/p  1−(2H+1)/p  (·)^14  M(p)=(p/2)(·)^14
431   26  53    0.1230     0.8770       0.1593  34.3
449   28  57    0.1269     0.8731       0.1495  33.6
461   28  57    0.1236     0.8764       0.1522  35.1
499   31  63    0.1263     0.8737       0.1512  37.7
601   37  75    0.1248     0.8752       0.1547  46.5
701   43  87    0.1241     0.8759       0.1564  54.8
809   50  101   0.1248     0.8752       0.1546  62.5
1009  63  127   0.1259     0.8741       0.1521  76.7

PROOF of M(p) formula:
M(p) = (p/2)·b̂(0)^14 where b̂(0) = 1 − (2H+1)/p. This is the expected number of uncovered cells for a random 14-set, since each cell is uncovered with probability b̂(0)^14 and there are p/2 cells (by symmetry t ↔ p−t).

Q3 Extreme-value model (IDEA):
Number of distinct 14-sets up to scaling: N ≈ C(n,14)/(p−1). ln N ≈ 14 ln(n) − ln(14!) − ln(p) ≈ 13 ln(p/2) − 25.2.
For p = 431: ln N ≈ 13·5.37 − 25.2 = 44.6. M = 34.3. N·e^{-M} = e^{44.6−34.3} = e^{10.3} ≈ 30000 ≫ 1 → D=0 expected.
For p = 499: ln N ≈ 13·5.52 − 25.2 = 46.6. M = 37.7. N·e^{-M} = e^{46.6−37.7} = e^{8.9} ≈ 7300 ≫ 1 → D=0 expected.
FACT: This Poisson model predicts D=0 for ALL primes up to ~1000, contradicting the census (D≥1 at 431+). The model overcounts effective sets because arithmetic correlations make most sets equivalent in coverage structure.

Q4 Fourier bound (IDEA):
Round 11 shows R₄(S) ≈ −0.66·M(p) universally. If we can prove |R(S)| ≤ c·M(p) with c < 1 for all 14-sets when p > P₀, then:
D(p) ≥ M(p) − |R(S)| ≥ (1−c)·M(p) ≥ (1−c)·0.076·p.
For c = 0.9: D(p) ≥ 0.0076p, so D(p) ≥ 1 for p ≥ 132.
For c = 0.99: D(p) ≥ 0.00076p, so D(p) ≥ 1 for p ≥ 1316.
PROVED: The Fourier identity (Round 10), the O(1) bound on b̂(k) for k≠0, and frequency-truncation convergence (Round 11).
NOT PROVED: Any explicit c < 1 bound on |R(S)|/M(p) for all S. The Dirichlet scaling (Lemma B, L16) gives P₀ = 120^14 ≈ 10^29; a Fourier approach could reduce this to ~10^3–10^5 if the resonance budget can be closed.

Q5 Predictions:
503 (s=1, ratio 1.742): 0 with 55% confidence. Near the transition zone; 457 survived at s=4 but 461 (s=6) did not. 503 has s=1 (favorable) but p is large.
547 (s=11→5, ratio 1.714): ≥4 with 60% confidence. Well past the death line.
577 (s=1, ratio 1.742): ≥4 with 60% confidence. Even with favorable s, p is too large.
599 (s=3, ratio 1.726): ≥4 with 65% confidence. Deep in the dead zone.

UNFINISHED: Q1 search results (code written but not executed). Q2 fit (requires Q1 data). Exact P₀ for the Fourier theorem.
Least-sure step: The extreme-value model's failure to predict the death line — the effective number of independent sets is much smaller than C(n,14)/n, and I cannot quantify the correlation structure without executing the search.

2/2

--- END VERBATIM REPLY (Response 2) ---

Notes:
- The code block above is the code exactly as shown (Qwen displayed it with line numbers 1..60 and word-wrapped words like "numpy as np" across two lines). I collapsed the line-number gutter and the artificial line-break inside words (e.g. "numpy as np" split across a line boundary) so it reads as valid Python; the code logic is identical.
- The table column "1009 63 127 0.1259 0.8741 0.1521 76.7" — the 1009 row uses H=63, 2H+1=127. Note: H = floor((p−1)/16) for p=1009 should be floor(1008/16)=63, so 2H+1=127 is self-consistent as shown; the courier does not judge mathematical correctness.
- ANSWER BLOCK listed "M(p) hand-computed for 7 primes" but the table actually lists 8 values (431, 449, 461, 499, 601, 701, 809, 1009). Preserved verbatim.
- Response 1 (left pane, not selected) also produced a reply starting "ANSWER BLOCK / Q1: UNFINISHED. Code for the local search is provided below, but I cannot execute it in this environment to obtain the exact numerical minimums and best 14-sets for the ..." with a 1-opt local search code block. It was more concise and did not include the M(p) table or Q4/Q5 reasoning depth. Response 2 was selected as the more complete final reply per the courier's duty to hand back what the model produced; Response 1 was discarded by the "I prefer this response" selection.

--- end verbatim ---
END LETTER
