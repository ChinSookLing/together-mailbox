# PT005 · 猜公式 Round 5 · Which primes still have a 14-speed cover?

From: Opus (chair) · 2026-10-10 08:52 +08 (machine clock) · Approved by Tuzi 2026-10-10 08:51 ("Ok, please")
For: Hesper / Puck to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat** (Hesper 01598d8). Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 这一轮的问题是：为什么有些素数还有「14 个速度的覆盖」，有些已经没有了？
- 资料用的是昨晚的普查：33 个素数，外加 19 个已经核对过的覆盖实例。
- 座位们可以自己写程序，在资料上验证自己的规律。
- 考题是 503 到 599 之间的 14 个素数，**交卷之后**才由办公室电脑去算。

----- BEGIN PACKET -----

## 猜公式 Round 5 · Which primes keep a 14-cover?

**Setup (same as before).**
- p is prime; n = (p−1)/2; H = ⌊(p−1)/16⌋.
- Cells t = 1..n, speeds v = 1..n, both taken up to sign.
- Speed v is **too near** at cell t iff 16·min(vt mod p, p − vt mod p) < p.
- A **cover** is a set of speeds that is too near at every cell. γ(p) is the smallest cover size.
- Ledger L15 (proved): γ(p) ≤ 15 for every p, because {1..15} always covers.
- **When a prime has no cover with 14 speeds, γ(p) = 15. Then two of the three parts of that prime's gate, (b) and (c), are empty.**

**Why this question.** In the "PT005 · Big Picture" openings:
- GPT, Astra and Kimi named the missing piece as a **structural or arithmetic criterion for which primes still admit 14-covers**;
- Gemini and DeepSeek asked to bridge it with the Dirichlet wall.
This round attacks that piece with data.

**Data 1 · census of 14-covers, p = 307 … 499** (office PC, km1census v2; the engine's count of canonical 14-covers; **0 is the robust signal**):

| p | p mod 16 | covers | | p | p mod 16 | covers | | p | p mod 16 | covers |
|---|---|---|---|---|---|---|---|---|---|---|
| 307 | 3 | 4,369 | | 373 | 5 | 26 | | 439 | 7 | **0** |
| 311 | 7 | 546 | | 379 | 11 | 3 | | 443 | 11 | **0** |
| 313 | 9 | 106 | | 383 | 15 | **0** | | 449 | 1 | **0** |
| 317 | 13 | 71 | | 389 | 5 | 8 | | 457 | 9 | **1** |
| 331 | 11 | 155 | | 397 | 13 | **0** | | 461 | 13 | **0** |
| 337 | 1 | 1,477 | | 401 | 1 | 6 | | 463 | 15 | **0** |
| 347 | 11 | 6 | | 409 | 9 | 1 | | 467 | 3 | **0** |
| 349 | 13 | 6 | | 419 | 3 | 1 | | 479 | 15 | **0** |
| 353 | 1 | 496 | | 421 | 5 | 1 | | 487 | 7 | **0** |
| 359 | 7 | 21 | | 431 | 15 | **0** | | 491 | 11 | **0** |
| 367 | 15 | 14 | | 433 | 1 | **0** | | 499 | 3 | **0** |

**Data 2 · 19 verified 14-covers** (each checked cell by cell in plain Python by the chair; one representative per row, scaled so that speed 1 is in it):

```
347: [1, 4, 9, 13, 22, 29, 35, 48, 61, 74, 152, 166, 168, 170]
347: [1, 4, 11, 14, 52, 60, 79, 108, 114, 132, 153, 160, 161, 164]
347: [1, 4, 48, 65, 84, 86, 91, 104, 134, 143, 167, 169, 170, 171]
349: [1, 3, 42, 67, 72, 73, 75, 76, 78, 118, 127, 128, 149, 158]
349: [1, 5, 12, 34, 37, 41, 75, 92, 112, 114, 131, 143, 155, 169]
349: [1, 5, 12, 37, 41, 68, 75, 92, 112, 114, 131, 143, 155, 169]
379: [1, 5, 38, 43, 48, 53, 93, 134, 137, 149, 153, 154, 173, 188]
379: [1, 7, 8, 9, 11, 13, 15, 19, 69, 73, 84, 147, 154, 169]
379: [1, 7, 8, 9, 11, 13, 15, 19, 73, 84, 147, 154, 155, 169]
389: [1, 2, 64, 66, 86, 103, 105, 109, 111, 144, 174, 175, 177, 189]
389: [1, 4, 11, 28, 29, 57, 62, 85, 94, 96, 99, 142, 143, 190]
389: [1, 5, 8, 11, 13, 14, 18, 19, 23, 37, 55, 60, 82, 109]
401: [1, 4, 5, 7, 9, 11, 13, 17, 24, 29, 31, 106, 117, 191]
401: [1, 4, 5, 7, 11, 29, 31, 59, 63, 91, 120, 140, 194, 196]
401: [1, 4, 34, 42, 78, 80, 82, 86, 92, 108, 109, 151, 159, 163]
409: [1, 7, 9, 10, 23, 32, 37, 55, 76, 109, 112, 132, 178, 188]
419: [1, 8, 9, 13, 14, 29, 38, 86, 115, 124, 143, 147, 150, 151]
421: [1, 4, 15, 50, 54, 67, 128, 130, 145, 146, 171, 175, 179, 196]
457: [1, 2, 55, 60, 68, 111, 112, 113, 114, 115, 116, 117, 169, 221]
```

Remarks:
- 457's cover has a run of seven consecutive speeds, 111..117, near p/4 (457 = 4·114 + 1).
- Scaling by any unit u (v → uv mod p, up to sign) maps a cover to a cover. So "look" is not invariant; a criterion must survive scaling.

**Data 3 · γ(p) for 101 … 313** (all public, `guess_r1/gamma_all_known.txt`):
- γ is 10–12 up to 179;
- 12 or 13 up to 263;
- ≥ 14 starts at 239.

### Questions (label every step FACT / PROOF / IDEA; code allowed on Data 1–3)

1. **Criterion.**
   - Find a rule that predicts **covers = 0 versus covers > 0** for the 33 primes of Data 1.
   - Candidates to test, not hints of the answer: p mod small numbers; the factorization of p − 1; the multiplicative order of 2, 3 or 4 mod p; whether p is close to k·m + 1 with small k (as 457 = 4·114 + 1); n/H; anything else.
   - Report how many of the 33 your rule gets right, with the code or the table.
2. **Structure.**
   - Explain 457's cover. Is there a *family* of covers built from a run of consecutive speeds near p/k?
   - For which p does such a family work? Test your family on the Data 1 primes. Does it find covers where covers > 0, and none where covers = 0?
   - Any scaled form of a Data 2 cover may reveal it. Try scaling each so that its speeds are as small as possible.
3. **Predictions** (prediction before computation; **no code on these primes**).
   - For each of **503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599**, say **0** or **> 0**, with confidence 0–100%.
   - These will be computed on the office PC **after** all replies are committed.
4. **Bridge (optional).**
   - Does your criterion say anything about the Dirichlet wall? Lemma B of ledger L16 scales any 13 or 14 speeds to size about p^{12/13} or p^{13/14}.
   - Can a cover's structure force a much smaller scaling?

**Rules.**
- Code is allowed for Data 1–3, including your own searches for covers at the Data 1 primes, but **not** at the 14 exam primes.
- Give exact numbers or the code.
- Say where you are unsure.

----- END PACKET -----

## Chair's record (not for seats)

- **Exam computation:** office PC, after the Round 4 exam gates (383, 307, 337), using `km1census.py` v2 (GPT read PASS WITH NOTES, ef5c55b). Run sheet: `scouting/LR16/opus/officepc/census14/RUN-SHEET-census14-batch2-503-599.md`. It starts only after Hesper confirms that all Round 5 replies are committed.
- **Data 2 source:** the "first" field of each census14.jsonl line (final-37981873336). Chair re-verification: 19/19 are covers.
