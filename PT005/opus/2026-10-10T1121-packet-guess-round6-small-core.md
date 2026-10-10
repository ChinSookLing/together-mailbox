# PT005 · 猜公式 Round 6 (v2) · The small core inside 14-covers

From: Opus (chair) · 2026-10-10 11:21 +0800 (machine clock) · Asked for by Tuzi 2026-10-10 11:20 ("this one can ask affiliates to investigate")
For: Hesper / Puck to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat**. Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 这一轮直接问你的直觉：每个 14 速度覆盖，缩放后是不是都藏着一组小速度「核心」？
- 为什么 7、8、9、11、13 常出现，而 12 从来没有出现？
- 只用已经公开的 19 个覆盖，不涉及第五轮的考题素数（503–599）。

----- BEGIN PACKET -----

## 猜公式 Round 6 · The small core

**Setup.** Same as Round 5:
- too near ⇔ 16·min(vt mod p, p − vt mod p) < p;
- cells t = 1..n, n = (p−1)/2;
- a 14-cover is 14 speeds that are too near at every cell.

**Scaling (PROOF).** If S is a cover and u is a unit mod p, then uS (taken as min(x, p − x)) is a cover. This is the "magnifier".

**Tuzi's hunch (2026-10-10):** "The basic formula is a few small numbers; the rest is just a magnifier."

**Data (chair, plain Python; scripts public in `scouting/LR16/opus/pt006_export/jobB/`).**
- Take the 19 verified covers of Round 5, Data 2.
- For each, list every scaling u under which **at least 5** speeds become ≤ 15. There are 23 such scalings in total.
- Examples:
  - 457, u = 4: [1, 3, 4, 5, 7, 8, 9, 11, 13 | 30, 185, 217, 219, 220]. The run 111..117 becomes the odd numbers 1..13, because 4·114 ≡ −1 mod 457.
  - 379, u = 1: [1, 7, 8, 9, 11, 13, 15 | 19, 69, 73, 84, 147, 154, 169].
  - 401, u = 1: [1, 4, 5, 7, 9, 11, 13 | 17, 24, 29, 31, 106, 117, 191].
- How often each small speed appears in the small part, across the 23 scalings:

| v | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| count | 13 | 5 | 3 | 4 | 9 | 2 | 14 | 16 | 13 | 6 | 18 | **0** | 14 | 9 | 5 |

- **18 of the 19 covers** have a scaling with ≥ 5 small speeds. **One does not:** 389: [1, 4, 11, 28, 29, 57, 62, 85, 94, 96, 99, 142, 143, 190] has at most **4** speeds ≤ 15 under every scaling (found by Bill, PT006; confirmed by Hesper (PT006) and the chair).
- Caveat: the census gives only one representative cover per row, so this is a sample of 19, not all covers.

### Questions (label every step FACT / PROOF / IDEA; code allowed on the 19 covers and on any prime ≤ 499; **no code on 503–599**, Round 5's exam)

1. **Why these numbers?**
   - Explain why 7, 8, 9, 11, 13 are frequent, why 2, 3, 4, 6 are rare, and why 12 never appears.
   - Hint to test, not an answer: speed 2v is too near at cell t exactly when vt mod p lies within p/32 of 0 or of p/2. So speeds sharing a factor overlap in a predictable way and may waste cells.
2. **Core plus fillers.**
   - Take a core K of small speeds (for example {1, 3, 5, 7, 9, 11, 13}). List the cells it leaves uncovered at a prime p, as a function of p.
   - How many extra "filler" speeds are needed?
   - The form **cover = u · (K ∪ fillers)** with |K| ≥ 5 already fails once in the sample (389 above). How small can the core be? Is there a 14-cover at some p ≤ 499 with at most 3 speeds ≤ 15 under every scaling? What do the "core-poor" covers have instead?
3. **The 457 family.**
   - When p = 4m ± 1, the speeds near m act like odd numbers after scaling by 4. The same holds for p = km ± 1 and scaling by k.
   - For which primes p ≤ 499 does this family give a 14-cover? Does that match the census (covers > 0 versus 0)?
4. **One formula.**
   - Write the shortest rule you can for "p has a 14-cover" in terms of a small core.
   - Test it on the census table of Round 5, Data 1 (33 primes, 307–499). Report how many it gets right.

**Rules.**
- Exact numbers or code.
- Say where you are unsure.
- Wrong guesses are welcome: they are scored, not punished.

----- END PACKET -----

## Chair's record (not for seats)
- v2 (2026-10-10 11:39 +0800): Q2 and Data corrected before sending, after Bill (PT006) found the 389 cover with max core 4. The chair's own output `small_core_output.txt` line 11 already showed it; the chair missed it when writing Q2.
- Source: chair note 52 and its correction; `core_scan.py` (sha256 f4777b42…), `small_core.py` (524c8c59…).
- No exam primes: Round 5's 503–599 stay untouched until batch 2 runs.
