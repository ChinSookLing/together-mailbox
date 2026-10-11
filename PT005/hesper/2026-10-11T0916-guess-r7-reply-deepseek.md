BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 09:17 +08
RE: 猜公式 Round 7 (packet 1006d95), send text r7_send_full.txt or r7_send_short.txt
SEAT: deepseek
MODEL: DeepSeek DeepThink (Thought for 8 seconds)
CHAT: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202

--- reply verbatim ---
**ANSWER BLOCK**

**Q1.** FACT: M₁₅ ≥ 4 holds in all 321 sampled covers, including 389 at the floor. IDEA: C-core4 is plausible for p ≤ 499, but not proved. Partial route: if M₁₅ ≤ 3, then for every scaling only ≤3 speeds lie in 1..15. The mid-cells t ∈ [H+1, 2H] force cover speeds near p/t ≈ 8..16, so those few small speeds must do too much work. UNFINISHED.

**Q2.** IDEA: the floor may be tied to log₂ N. For threshold 1/N with N−2 speeds, guess floor ≈ ⌊log₂ N⌋; at N = 16 this gives 4. Low confidence.

**Q3.** IDEA: C-core4 reduces the decision to 1,365 four-element cores, each extended by 10 speeds. That is still huge, but window containment prunes cores whose small speeds cannot cover the mid-cells. FACT: it does not yet explain the post-431 die-off.

**Q4.** For 337 (1,477 covers): predict M₁₅ = 4 count range **180–260**, best **215**, confidence **55%**. Largest M₁₅ range **8–10**, best **9**, confidence **65%**.

**Least-sure step:** the 337 M₁₅ = 4 count; it extrapolates from 307’s sample, and 337’s cover population may be structurally different.

**Reasoning**

FACT: at 307, the sampled M₁₅ distribution was 4:40, 5:124, 6:82, 7:24, 8:3, 9:1 out of 274. That gives M₁₅ = 4 proportion ≈ 14.6%. Scaling to 1,477 covers gives ≈ 216, hence my range.

FACT: 337 has p ≡ 1 mod 16 and 1,477 covers, far more than most nearby primes. At 307, the maximum M₁₅ seen was 9. At 457, the unique cover had M₁₅ = 9. IDEA: with 1,477 covers, 337 may contain a 10, but no sample forces one. So range 8–10, best 9.

FACT: 389’s cover has M₁₅ = 4, attained under u = 4 as {4,5,7,13}. That shows the floor is not 5. FACT: no M₁₅ ≤ 3 has appeared. IDEA: C-core4 is the strongest clean conjecture available.

IDEA for Q2: threshold 1/N means too-near window p/N. The number of runners is N−2. The core floor may grow like log₂ N because each small speed covers roughly a dyadic pattern of cells. This is speculative.

IDEA for Q3: 1,365 cores is small, but extension is not. Window containment says composite speeds add only new cells at indices i/v with gcd(i,v)=1. That should prune many extensions. Whether it kills all cores after 431 is UNFINISHED.

Least-sure step remains the 337 M₁₅ = 4 count.

--- end verbatim ---
END LETTER
