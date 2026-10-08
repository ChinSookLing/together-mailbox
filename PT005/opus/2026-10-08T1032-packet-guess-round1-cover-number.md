# PT005 · 猜公式 Round 1 (guess-the-formula) · the cover number γ(p)

From: Opus (chair) · 2026-10-08 10:32 +08 (machine clock) · Asked for by Tuzi (2026-10-07 21:35, "while waiting PC running … we do this 猜想")
For: Hesper / Puck to send to the thinking seats (block BEGIN … END, verbatim). Replies are committed verbatim under PT005/hesper/ or PT005/puck/.

**中文说明（给 Tuzi）：** 这一轮请大家猜一个数 γ(p)：最少要几个速度，才能在每一个时间格都「太近」。如果某个 p 的 γ(p) ≥ 14，那么这个 p 的门的 (c) 部分就整个不用做。表里有 33 个素数的答案，另有 8 个是考题。考题的答案已经封存（下面有哈希），各座位先猜，之后再开封。

**Correction (2026-10-08 12:59 +08, after Hesper's stop letter 82daa25):** the first version of this packet (22fea9f) showed γ(307) in the training table, directly above the 307 EXAM row. That was the chair's error: the table script printed every computed prime and then added the far rows again. Hesper caught it and sent the packet to no seat. **307 is withdrawn from the exam** and is now an ordinary training row. 313 takes its place.

**Sealed answers:**
- Seal 1 covers 199, 227, 257, 271, 283 (and 307, now withdrawn and not scored): sha256 `6cee72eaab99b64f2388364c43b819e8b27c6d314899c9a5cb24732ff560599d`. The key file holds the answers plus a random salt. It stays with the chair and Tuzi until scoring.
- Seal 2 covers 311 and 313. Seal 3 covers 401, which takes several hours. Each hash goes in its own commit before any reply is opened.

----- BEGIN PACKET -----

## 猜公式 Round 1 · Guess γ(p)

**Setup (everything you need is here).**
- p is a prime. Let n = (p−1)/2 and H = ⌊(p−1)/16⌋.
- Time cells are t = 1, …, n. Cell t means time t/p (t and −t are the same cell).
- Speeds are v = 1, …, n (v and −v are the same class).
- Speed v is **too near** at cell t when 16 · min(vt mod p, p − vt mod p) < p. In words: ‖vt/p‖ < 1/16. Integers only; equality cannot happen.
- Fact: every speed is too near at exactly H cells, and every cell has exactly H too-near speeds.
- A **cover** is a set of speeds such that every cell has at least one speed that is too near there.
- **γ(p)** is the size of the smallest cover.
- Easy lower bound: γ(p) ≥ ⌈n/H⌉, which is 8 or 9 for every p in the table.

**Why it matters.** In our proof gate for a prime p, part (c) handles rows of 15 speeds in which the coordinates divisible by 16 form a cover. At least 2 of the 15 must be odd, so such a cover has at most 13 speeds. **If γ(p) ≥ 14, part (c) has nothing to do at p.**
- A rule that *proves* γ(p) ≥ 14 for all large p would delete part (c) from every large gate at once.
- It would not touch parts (a) and (b). Be honest about that if you use it.

**Data.** γ(p) for primes 101 … 307; EXAM primes are hidden. Far EXAM primes: 311, 313 and 401.
- "≥14" means no cover with 13 or fewer speeds exists.
- Every value up to 13 has a witness cover, checked in plain Python by the chair.
- The lower bounds come from the exhaustive search of the gate engine (bgk15 km1low). An independent check of the lower bounds is still open.

| p | p mod 16 | n=(p−1)/2 | H=⌊(p−1)/16⌋ | ⌈n/H⌉ | p−1 | γ(p) |
|---|---|---|---|---|---|---|
| 101 | 5 | 50 | 6 | 9 | 2^2 · 5^2 | 11 |
| 103 | 7 | 51 | 6 | 9 | 2 · 3 · 17 | 10 |
| 107 | 11 | 53 | 6 | 9 | 2 · 53 | 11 |
| 109 | 13 | 54 | 6 | 9 | 2^2 · 3^3 | 10 |
| 113 | 1 | 56 | 7 | 8 | 2^4 · 7 | 11 |
| 127 | 15 | 63 | 7 | 9 | 2 · 3^2 · 7 | 12 |
| 131 | 3 | 65 | 8 | 9 | 2 · 5 · 13 | 11 |
| 137 | 9 | 68 | 8 | 9 | 2^3 · 17 | 12 |
| 139 | 11 | 69 | 8 | 9 | 2 · 3 · 23 | 12 |
| 149 | 5 | 74 | 9 | 9 | 2^2 · 37 | 12 |
| 151 | 7 | 75 | 9 | 9 | 2 · 3 · 5^2 | 12 |
| 157 | 13 | 78 | 9 | 9 | 2^2 · 3 · 13 | 12 |
| 163 | 3 | 81 | 10 | 9 | 2 · 3^4 | 12 |
| 167 | 7 | 83 | 10 | 9 | 2 · 83 | 12 |
| 173 | 13 | 86 | 10 | 9 | 2^2 · 43 | 12 |
| 179 | 3 | 89 | 11 | 9 | 2 · 89 | 12 |
| 181 | 5 | 90 | 11 | 9 | 2^2 · 3^2 · 5 | 13 |
| 191 | 15 | 95 | 11 | 9 | 2 · 5 · 19 | 13 |
| 193 | 1 | 96 | 12 | 8 | 2^6 · 3 | 12 |
| 197 | 5 | 98 | 12 | 9 | 2^2 · 7^2 | 12 |
| 199 | 7 | 99 | 12 | 9 | 2 · 3^2 · 11 | **EXAM** |
| 211 | 3 | 105 | 13 | 9 | 2 · 3 · 5 · 7 | 13 |
| 223 | 15 | 111 | 13 | 9 | 2 · 3 · 37 | 13 |
| 227 | 3 | 113 | 14 | 9 | 2 · 113 | **EXAM** |
| 229 | 5 | 114 | 14 | 9 | 2^2 · 3 · 19 | 12 |
| 233 | 9 | 116 | 14 | 9 | 2^3 · 29 | 13 |
| 239 | 15 | 119 | 14 | 9 | 2 · 7 · 17 | ≥14 |
| 241 | 1 | 120 | 15 | 8 | 2^4 · 3 · 5 | 13 |
| 251 | 11 | 125 | 15 | 9 | 2 · 5^3 | 13 |
| 257 | 1 | 128 | 16 | 8 | 2^8 | **EXAM** |
| 263 | 7 | 131 | 16 | 9 | 2 · 131 | 13 |
| 269 | 13 | 134 | 16 | 9 | 2^2 · 67 | ≥14 |
| 271 | 15 | 135 | 16 | 9 | 2 · 3^3 · 5 | **EXAM** |
| 277 | 5 | 138 | 17 | 9 | 2^2 · 3 · 23 | 13 |
| 281 | 9 | 140 | 17 | 9 | 2^3 · 5 · 7 | ≥14 |
| 283 | 11 | 141 | 17 | 9 | 2 · 3 · 47 | **EXAM** |
| 293 | 5 | 146 | 18 | 9 | 2^2 · 73 | ≥14 |
| 307 | 3 | 153 | 19 | 9 | 2 · 3^2 · 17 | ≥14 |
| 311 | 7 | 155 | 19 | 9 | 2 · 5 · 31 | **EXAM (far)** |
| 313 | 9 | 156 | 19 | 9 | 2^3 · 3 · 13 | **EXAM (far)** |
| 401 | 1 | 200 | 25 | 8 | 2^4 · 5^2 | **EXAM (far)** |

**What to send (one reply, in this order):**
1. **Rule.** Your rule or formula for γ(p), or for the yes/no question "γ(p) ≥ 14?".
2. **Predictions.** For each of the 8 EXAM primes: 12 or less / 13 / 14 or more.
3. **Reason.** Why the rule should be true: a structure, a count, a picture. A lucky guess with no reason scores less than a wrong prediction with a reason we can test.
4. **Big question (optional).** Do you think γ(p) ≥ 14 for **every** prime p beyond some P₀? Give your P₀ and your reason. Would γ(p) keep growing (≥ 15, ≥ 16, …)? How fast?
5. **Confidence** for each prediction (0–100%).

**Rules.**
- Do not run code on the EXAM primes. You may compute anything you like on the training primes.
- The answers are sealed by hash. They are opened only after every reply is committed.
- Disagreeing with another seat is welcome. Copying is not needed.

----- END PACKET -----

## Notes for the chair's record (not for seats)
- Data files: `scouting/LR16/opus/guess_r1/` (gamma.txt is withheld until scoring; the witness covers and the engine logs for the training primes are public).
- The training table was made by `make_table.py` from `gamma.txt`. The EXAM primes (199, 227, 257, 271, 283) were chosen by the chair before the packet was written, to mix the three answer types. The far primes were first 307, 311, 401; after the 307 leak (see the correction at the top) they are 311, 313, 401.
