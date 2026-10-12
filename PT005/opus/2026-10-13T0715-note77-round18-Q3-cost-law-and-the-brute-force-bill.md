# PT005 · Chair note 77 · R18 Q3 scored: a cost law for the gate, and the brute-force bill (about 96,000 CPU-hours)

From: Opus (chair) · 2026-10-13 07:15 +0800 (machine clock) · Requested by Tuzi 07:00 ("you continue R18 Q3")
Reads: R18 Q3 answers (Qwen df753f4, Lumo d70b209, Gemini 1dbc505)
Code: PT005/opus/guess_r18/q3/costmodel.py

## 1. Cost law (chair; fitted on the 10 gates with full node counts, part (a))

    log(nodes) = 16.206 + 6.191·log p − 3.126·(n/H),   n = (p−1)/2,  H = ⌊(p−1)/16⌋

- **Fit:** leave-one-out error is median ×1.10, max ×1.19, over 191, 223, 233, 239, 241, 307, 337, 383, 401, 409.
- **Status:** SUPPORTED-MODEL quality on these 10 points. Above 409 it is extrapolation; it has not been tested beyond 409.

**Reading.**
- Cost grows about as p^6.2. This agrees with the author's p^5.9 for 15 runners.
- The second factor is n/H, which is set by p mod 16:
  - p ≡ 1 (mod 16) gives n/H = 8, the tightest case, and is the most expensive;
  - p ≡ 15 gives the largest n/H and is the cheapest. Near p ≈ 600 it is about 2× cheaper than p ≡ 1.
- γ(p) does **not** improve the fit. For example, 383 (γ = 15) and 409 (γ = 14) are both on the law.

## 2. The bill

Closing gates in ascending order from 251 reaches Σ log p > 481.07 after **75 more primes, up to p = 719**.
- Predicted cost: **about 96,000 office CPU-hours, about 500 days** on the office PC's 8 workers.
- This counts part (a) only. Primes with γ ≤ 14 also need (b) and (c).
- Reordering by cost per unit of log p gives almost the same bill. The mod-16 choice saves little, because at these sizes almost every prime must be used.
- With a faster dedicated machine the bill shrinks only by that machine's speed factor.

## 3. Seats' Q3 answers

| Seat | Answer | Chair's score |
|---|---|---|
| **Qwen** | γ = 15 primes in ascending order; prime-number-theorem tail model reaching P ≈ 861 | Honest and well labelled: it says UNFINISHED where it should. The ordering is fine. The tail is too long (the cost-ordered ladder ends at 719, because the cheap primes 251–499 count). Its γ filter is not supported by cost. Partial credit. |
| **Lumo** | "γ < 15 is cheapest, since a 14-cover is found quickly" | Wrong direction. γ < 15 adds parts (b) and (c). Also the cost is in part (a), not in finding covers. |
| **Gemini** | Avoid the high-cost region around 401; go in order to 953 | Qualitative. "401 is costly" fits the law (401 ≡ 1 mod 16). No computation. |

## 4. What this means

- Brute force can finish the job **in principle**: about 75 gates of known method.
- But it costs well over a year of one office PC. More compute only divides this.
- This is the real bottleneck.
- Tuzi (07:00): "暴力计算 — 勝之不武" ("brute force is a victory without honour"). The chair agrees that the next round should look for an idea, not more compute.
- Proposal for Round 20: a brainstorm that reviews Rounds 1–19b, plus THOOTB-style out-of-the-box framing, aimed at a way to close gates in bulk (a theorem covering many p at once) instead of one at a time.

STATUS: model and bill = chair computation (SUPPORTED-MODEL in-sample; EXPLORATORY beyond p = 409). No ledger change.
