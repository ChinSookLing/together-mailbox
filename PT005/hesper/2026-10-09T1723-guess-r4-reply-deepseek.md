BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 17:23 +08
RE: 猜公式 Round 4 part (a) (packet 61862ac), send text r4_send_deepseek.txt
SEAT: deepseek
MODEL: DeepSeek (Tuzi phone relay; mode as set by Tuzi)
CHAT: (phone app, no URL)

--- reply verbatim ---
[Courier note: Tuzi phone relay 2026-10-09 17:23 +08 (browser email login blocked: "Network Error" ×2). Sent text = phone version of r4_send_deepseek.txt (same data/questions, table as pipe lines). Pasted by Tuzi in chat; verbatim below.]

**ANSWER BLOCK**

**Q3 predictions** (ranges, gate closes = alive L16 = 0):

| p | rows | surv. L2 | gate closes? | confidence |
|---|---:|---:|---|---:|
| 307 | \(2\times10^6\) – \(2\times10^7\) | 500 – 5000 | yes | 45% |
| 337 | \(2\times10^5\) – \(2\times10^6\) | 50 – 1000 | yes | 40% |
| 383 | \(5\times10^4\) – \(5\times10^5\) | 1 – 100 | yes | 50% |

**Q1:** IDEA. rows(p) is driven by surplus \(15H-n\) and \(p\bmod16\); it peaks while \(H\approx15\) and \(n/H\approx8\), then collapses once \(H\gtrsim20\) because irredundant 15-covers are forced toward near-consecutive rows. 241≡1 is high; 239≡15 is lower.

**Q2:** IDEA. surv. L2 shrinks very fast with H. At 409 the lone survivor is almost certainly \(\{1,\dots,15\}\). For 307–383, expect small survivor sets containing \(\{1,\dots,15\}\).

**Q4:** IDEA. Conjecture: for large H every irredundant 15-cover is a unit scaling of a row close to \(\{1,\dots,15\}\). Test cheaply by normalizing one speed to 1, sorting, and checking max−min is bounded and gaps are small.

**Q5:** Tuzi: prove the structure theorem that large-H irredundant 15-covers are near-scalings of \(\{1,\dots,15\}\); then part (a) reduces to checking finitely many near-consecutive rows at lifts.

Least-sure step: the exact rows/survivor ranges for 307/337/383.

**Reasoning**

FACT: the data show rows explode through 241 and collapse by 401–409. PROOF: if H is small, many 15-subsets can be arranged as irredundant covers. IDEA: as H grows, the cover condition becomes too rigid; with 15 speeds each covering H cells, large H forces massive overlap, and irredundancy then forces a near-consecutive structure. This explains why 401 has only 198k rows and 409 only 17k, with L2 down to 5 and 1.

For 307, H=19, mod 3: it is past the peak but not yet in the 401 collapse. So rows should be in the millions, not hundreds of millions. For 337, H=21, mod 1: mod 1 often gives more rows, but H=21 is large, so I expect fewer than 307. For 383, H=23, mod 15: close to 401’s H=25, so rows likely hundreds of thousands or less, and L2 very small.

The survivor drop is the clearest trend. At H=15, L2 can be \(10^6\); at H=25 it is 5. H=19–23 should be intermediate but much closer to the low end. The tight row \(\{1,\dots,15\}\) is special: FACT at 401 it survives to 16p. At 409 the L2=1 row is likely that same row up to scaling. So I expect 383’s L2 to be small, possibly just the tight row plus a few.

All computed gates have alive L16=0. There is no evidence of a level-16 survivor. So I predict all three close. Confidence is higher for gate closing than for the exact row ranges.

--- end verbatim ---
END LETTER
