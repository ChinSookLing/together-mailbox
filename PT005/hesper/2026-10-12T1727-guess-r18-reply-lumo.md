BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 17:27 +08
RE: 猜公式 Round 18 make the gate cheap (packet ab3ea04), send text r18_send_lumo.txt
SEAT: lumo
MODEL: Lumo 2.0 Lite (web search on)
CHAT: https://lumo.proton.me/u/30/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
Chat URL: https://lumo.proton.me/u/30/c/1b04e910-acf8-481d-80b9-8deeab93d8db
Model: Lumo 2.0 Lite
Approx send time (Asia/Kuala_Lumpur): 2026-10-12 ~17:28
Reply captured verbatim below (full reply; copy button showed "Copied to clipboard" but clipboard was unreadable by the agent, so this is a verbatim text capture from the chat message, end confirmed by the "100× (IDEA, based on the 223 result)." sentence immediately before the reply's action bar).

--- BEGIN LUMO REPLY ---

Cheapest Primes Order
401, 409, 419, 421, 431, 433, 439, 443, 449, 461...
Cost ~ p^5.9 * (1 - census_coverage)

Q3 · Which primes, in which order?

Strategy:
The cost of closing a gate p is dominated by the search for irredundant 15-sets (part a). When γ(p) = 15 (no 14-cover), parts (b) and (c) are empty, but part (a) still requires verifying that no 15-set covers all cells. However, the density of dead branches correlates with the "gap" between the capacity 15H and the target n.

Key Insight:
The cost drops sharply when p has a high census count of 14-covers (meaning the space is "loose" and 15-sets easily fail to be irredundant? No, wait).

Correction:
If γ(p) = 15, there are no 14-covers. The search for 15-sets must prove that every 15-set has a hole. This is harder if the "hole" is hard to find.

Better Proxy:
The number of surviving rows at L2 (from the table) is the best predictor.
p = 307: 6,909 survivors → high cost.
p = 337: 1,832 survivors → medium cost.
p = 383: 2 survivors → low cost (but high nodes due to deep dead ends).

Pattern:
The cost seems to correlate with p (mod 16). p ≡ 1, 9 (mod 16) (like 337, 401, 433, 449, 457) tend to have more 14-covers (if any) or specific structures that might make the 15-search harder?

Actually, looking at the table: 383 (p ≡ 15) had only 2 survivors but 71 CPU hours. 307 (p ≡ 3) had 6909 survivors and 30 hours.

Hypothesis:
The "dead branch" explosion happens when the set is almost a cover but fails by 1 cell. This is most likely when p is such that 15H ≈ n (tightest fit).
n = (p − 1) / 2, H = ⌊(p − 1) / 16⌋. Ratio n / (15 H) ≈ (p / 2) / (15 p / 16) = 8 / 15 ≈ 0.533.
The "slack" s = n − 15 H.
p = 307 (3): n = 153, H = 19, 15 H = 285. Wait, 15H > n? No. H = ⌊306/16⌋ = 19. 15 × 19 = 285. n=153.
Wait, 15 speeds cover 15 × 19 = 285 cells? But there are only 153 cells.
Ah, the definition: "too near" means avoiding the safe zone. A speed covers H cells where it is unsafe? No, "too near" means it hits the target.
Re-read setup: "Speed v is 'too near' at t iff ... < p". A cover is a set of speeds that are too near at every cell.
So we need 15 speeds to cover all n cells. Each speed covers H cells. Total capacity 15H.
p = 307: H = 19, 15H = 285. n=153. Capacity is almost double the target. Overlap is huge.
p = 383: H = 23, 15H = 345. n=191. Capacity ≈ 1.8 × n.
Why is 383 so expensive? Because the overlaps are structured such that many subsets look like they might work until the very end.

Prediction:
The cheapest primes are those with low census counts of 14-covers (since if 14-covers are rare, 15-covers are also likely rare or non-existent, but the search must prove it).

Wait, the goal is to close the gate. We need to prove γ(p) = 15.
If γ(p) = 15, we must exhaust the search.
If γ(p) < 15 (i.e., a 14-cover exists), the search stops early (part b/c triggers).
Therefore:
The most expensive primes are those where γ(p) = 15 (no 14-cover) AND the structure allows many near-misses.
From the census: 383, 397, 431, 433, 439, 443, 449, 461, 463, 467, 479, 487, 491, 499 are all γ = 15.
The cheapest to close are those where γ(p) < 15 (we find a 14-cover quickly).

List of γ < 15 (from data):
307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 389, 401, 409, 419, 421, 457.

Order:
Start with these. Among them, prioritize those with fewest 14-covers? No, if we find one, we stop. So we want primes where a 14-cover is easy to find (dense).
Data: 307 (4369 covers), 337 (1477), 353 (496). These are "rich". The search will find a cover instantly.
Order: 307, 337, 353, 311, 313... (descending cover count).
Then the hard ones: 383, 397, etc. (where we must search to exhaustion).

Ladder to 481.07:
Rich primes (Cheap): 307, 337, 353, 311, 313, 317, 331, 347, 349, 359, 367, 373, 379, 389, 401, 409, 419, 421, 457. (Sum logs ≈ 150).
Hard primes (Expensive): 383, 397, 431, 433, 439, 443, 449, 461, 463, 467, 479, 487, 491, 499. (Sum logs ≈ 120).
Next Batch (503+): 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599. (Predicted γ = 15 for most).

Optimal Order:
Process all γ < 15 primes first (fast wins). Then process γ = 15 primes in increasing order of p (cost grows with p).

Model vs Measurement:
The assumption that cost ∝ p^5.9 is a model. The actual cost depends on the "near-miss" structure which varies with p (mod 16).

Last Question:
If the table could build only one change: Implement the "Core Certificate" (GPT's idea) for part (a) to prune the 11–12 class branches; expected speed-up: 100× (IDEA, based on the 223 result).

--- END LUMO REPLY ---
--- end verbatim ---
END LETTER
