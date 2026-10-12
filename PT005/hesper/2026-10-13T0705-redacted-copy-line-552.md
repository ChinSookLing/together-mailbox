遮蔽帳號名與全名（Tuzi 2026-10-13 06:18 批准）; 原行 552 不改動
CORRECTS: proof-table-005-552

BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 17:30 +08
RE: 猜公式 Round 18 make the gate cheap (packet ab3ea04), send text r18_send_qwen.txt
SEAT: qwen
MODEL: Qwen3.8-Max, Thinking on, web on (packet pasted inline; upload blocked)
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
Chat URL: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3
Model shown: Qwen3.8-Max (Thinking mode on; Web search on)
Approximate send time: 2026-10-12 ~17:30 Asia/Kuala_Lumpur (= Asia/Singapore, UTC+08:00)
Account: [已遮蔽] — "[已遮蔽]" (Plus), project chat "PT005 · Big Picture" (Play Civilisation Field project)
Delivery note: Upload blocked. Qwen's "+" / "Upload attachment" menu item never opens a file chooser in this browser, and no <input type="file"> exists in the DOM (automation CDP error -32000 "Node is not a file input element"). Per user approval, the packet text between the ==== markers was pasted inline into the composer (no code fence, no "attached" line) and sent once.
Reply capture note: Reply was captured verbatim from Qwen's Copy button; the Copy clipped inside the python code block at the "if isprime(p" line. The clipped line and the rest of the code were recovered verbatim from the chat's rendered text (find_text/extract_content). No wording was added or changed; the reply ends at "No new citations." as rendered with the Send button returned (generation finished, action row Copy/Good/Bad/Share/Regenerate visible, no "Thinking..." / status card).

--- BEGIN REPLY (verbatim) ---

ANSWER BLOCK

**Q3 (my lane).** Cheapest primes = γ(p)=15 primes in ascending order.

**FACT:** at γ=15 primes parts (b) and (c) are empty, so only part (a) runs. **FACT (census):** in [401,499] the γ=15 primes are 431,433,439,443,449,461,463,467,479,487,491,499; skip 401,409,419,421,457 (γ=14, so they also need (b),(c)). **IDEA:** part-(a) cost grows steeply with p (chair's ~p^5.9 generation law), so close small γ=15 primes first.

**My ladder (hand log sums, ln):**
ledger 27.07
+ pending 307,337,383 = +17.50 → 44.57
+ γ=15 primes 397→521 = +98.30 → 142.87
Need **+338.20** more to pass 481.07. Taking γ=15 primes ascending from 523, Σln p reaches this near **p≈860–880** (MODEL: no census ≥523, assumes all are γ=15). This beats the chair's every-prime-from-503 baseline (p≈953) because we harvest the cheap 397–499 γ=15 primes that the from-503 plan skips.

**Model vs measurement:** log-sums + γ-list = computed/census. Cost ~p^5.9 = chair's measurement, not mine. Tail γ-status, row counts, and the ≈860–880 stop = **MODEL**. I did not run the engine.

**FACT (from the 5 measured rows):** dominant cost signal is γ and row count, which collapse with p; I see **no** evidence that p mod 16 or H drives cost at this sample size. **UNFINISHED:** I cannot predict row counts for unmeasured primes.

**Last question (IDEA):** build the "cannot complete with k remaining classes" feasibility cut at depth ≤10 (LP/fractional-cover or private-time capacity). It targets the 90% of nodes sitting at depth 11–12; expect ~5–10×. Not measured.

---

## Work

### Q3 detail

**FACT (my hand computation, ln to 3 dp).** γ=15 primes in [397,521]:

| p | ln p | p | ln p |
|---|---|---|---|
| 397 | 5.983 | 467 | 6.146 |
| 431 | 6.066 | 479 | 6.171 |
| 433 | 6.071 | 487 | 6.188 |
| 439 | 6.085 | 491 | 6.196 |
| 443 | 6.094 | 499 | 6.212 |
| 449 | 6.107 | 503 | 6.220 |
| 461 | 6.133 | 509 | 6.232 |
| 463 | 6.137 | 521 | 6.255 |

Sum = **98.30** (I added column by column).

**FACT (hand).** Pending gates: ln307+ln337+ln383 = 5.727+5.820+5.948 = **17.495**.

**FACT (hand).** Running total after ledger+pending+γ15[397,521]:
27.07 + 17.50 + 98.30 = **142.87**.

**FACT (hand).** Deficit to 481.07: 481.07 − 142.87 = **338.20**.

**IDEA (model for the tail).** By the prime-number-theorem heuristic Σ_{p≤x} ln p ≈ x, the log-sum of primes from 523 to P is ≈ P − 523. Solving P − 523 ≈ 338 gives **P ≈ 861**. So a γ=15-ascending ladder reaches the threshold around p≈860–880. This is a **model**, not a measurement: I have no census for p≥523 and have not verified those primes are γ=15.

**PROOF (why γ=15-first is sound, not just cheap).** This is an ordering choice, not a pruning rule, so it cannot lose any required gate: every prime still gets closed eventually; we merely schedule cheap ones first. Hence the soundness rule is trivially satisfied (no row is ever discarded).

**IDEA (cost driver).** The measured rows are:

| p | rows | γ |
|---|---|---|
| 307 | 11.68M | 14 |
| 337 | 7.33M | 14 |
| 383 | 5,171 | 15 |
| 401 | 198,769 | 14 |
| 409 | 17,546 | 14 |

Row count does **not** monotonically track γ (409 has γ=14 but fewer rows than 337). It tracks p and structure. So my ordering uses γ only as a gate-type filter (skip (b),(c)), not as a row-count predictor. **UNFINISHED:** I have no validated row-count model for unmeasured primes.

### Code that reproduces my ladder sum

```python
import math
from sympy import isprime   # or any primality test

gamma15_known = {383,397,431,433,439,443,449,461,463,467,
                 479,487,491,499,503,509,521}
ledger = 27.07
pending = [307,337,383]

total = ledger + sum(math.log(p) for p in pending)
# add gamma15 primes 397..521
total += sum(math.log(p) for p in sorted(gamma15_known) if 397 <= p <= 521)
print("total after known gamma15 ladder:", total)   # ~142.87

# tail model: add primes ascending until > 481.07
p = 523
while total <= 481.07:
    if isprime(p):
        # MODEL: assume gamma=15 for all p>=523
        total += math.log(p)
    p += 2
print("threshold crossed near p =", p-2, "total =", total)
```

I did not execute this here; the hand values above are my own arithmetic. The code is shown so the chair can reproduce/verify. UNFINISHED until run.

### Q3 sub-question: does cost track p mod 16 or H?

**FACT (from measured rows only):** the 5 data points show row count collapsing with p and with γ, but there is no visible p-mod-16 or H pattern in a sample of 5. **IDEA:** H=⌊(p−1)/16⌋ sets per-class coverage m, but every gate uses 15 classes regardless, so H likely affects the arithmetic of rows rather than their existence. I cannot confirm without more measured gates. **UNFINISHED.**

### Red-team note on my own proposal (Q5 spirit)

**IDEA:** my ladder is an ordering, not a cut, so there is no soundness to break — it cannot drop a needed row. The only risk is the model assumption that primes ≥523 are γ=15; if some are γ=14, the gate there must also run (b),(c), raising cost but not invalidating the proof. This is a cost-model risk, not a soundness risk.

### Reference tags

I cite no papers this round (Q3 needs only the census and the chair's cost law, both internal). Allikvere arXiv:2609.02604 = MEMORY (already flagged in Round 17); Beck–Everett arXiv:2609.06259 = MEMORY (mentioned in packet, unread). No new citations.

--- END REPLY ---
--- end verbatim ---
END LETTER
