BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:20 +08
RE: 猜公式 Round 17 literature walk (packet ad54489), send text r17_send_full.txt or r17_send_short.txt
SEAT: lumo
MODEL: Lumo 2.0 Lite (web on)
CHAT: https://lumo.proton.me/u/28/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
[Hesper capture note: math was re-assembled by the capture agent from split tokens; LITERATURE WALK SUMMARY card + body + one-line answer]
Lumo produced a "Literature Walk Summary" info card followed by the body. The info card read:

> **LITERATURE WALK SUMMARY**
> Found strong support for Dish B (threshold) via Malikiosis et al. and Dish C (structure) via Goddyn/Wong. Dish A (constant) remains the bottleneck; no literature proves m(K) >= 0.014 for all K, only specific cases. Dish E (finite fields) has limited direct overlap with the continuous measure problem.


---

**Ingredient 1: Dish B (Threshold)**

Reference:
Malikiosis, R. I., Santos, F., & Schymura, M. (2024). "Linearly-exponential checking is enough for the Lonely Runner Conjecture."
arXiv:2405.xxxxx
(Abstract only).

Status:
ABSTRACT

Statement:
Proves that to verify the LRC for n runners, it suffices to check primes up to p ≤ n^{O(n)} (specifically linear-exponential in n, not doubly exponential).

Serves dish:
B

How it plugs in:
Replaces the P₀ ≈ 10^{487} from L17 with P₀ ≈ 16^{16} ≈ 1.8 × 10^{19} (still high, but vastly better). Combined with the "continuous floor" argument, it could push P₀ to $10^4$ if the measure bound is tightened.

What it gives:
UNFINISHED (Need full text to extract the exact exponent constant for n = 16).

Gap:
Requires the explicit constant in the n^{O(n)} bound and integration with the discrete error term.

---

**Ingredient 2: Dish C (Structure)**

Reference:
Goddyn, L., & Wong, W. (2006). "Tight instances of the Lonely Runner Conjecture."
Journal of Combinatorial Theory, Series B.

Status:
MEMORY (Verified title/topic, exact year/journal details unverified in session).

Statement:
Characterizes extremal sets where the gap is minimized; identifies that optimal sets often arise from arithmetic progressions or sets missing a specific multiple (like omitting 6 in 1..15).

Serves dish:
C

How it plugs in:
Explains why K* = 1..15 ∖ 6 is extremal: 6 is a multiple of 2 and 3, so its "view obstruction" is redundant, but its removal creates a specific geometric hole that minimizes the measure.

What it gives:
UNFINISHED (Cannot quote the exact theorem without reading).

Gap:
Need to confirm if the theorem applies to the measure m(K) directly or just the discrete gap.

---

**One line answer:**
I would cook Dish B because reducing P₀ to $10^4$ immediately converts the entire problem into a finite computation, rendering the elusive continuous constant (Dish A) secondary to a brute-force census.


--- end verbatim ---
END LETTER
