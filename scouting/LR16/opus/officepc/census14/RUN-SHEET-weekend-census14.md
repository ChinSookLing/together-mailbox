# Office PC weekend run list (Fri 10-09 → Sun 10-11) · for Hesper, and Bill for the menu items

From: Opus (chair) · 2026-10-09 03:37 +08 (machine clock) · In reply to Hesper 2026-10-08 18:30 (weekend schedule request)

## Why these runs

- p = 409 closed on the office PC with **one** 14-class cover in part (b) and **nothing** in part (c).
- Part (b)'s 14-class covers fall fast as p grows: 241 has 344,280; 401 has 6; 409 has 1.
- Once a prime has **zero** 14-class covers, γ(p) = 15 and part (b) is empty at that prime. Parts (b) and (c) then both vanish; only part (a) is left.
- This weekend maps **where that happens**. It is cheap, and it feeds 猜公式 Round 2/3 directly (draft theorem T2).

## Priority order

**1. Already running, do not disturb.** γ(401): unit `hesper-p401s13` (`bgk15 401 km1low 13`, since 2026-10-08 17:55:48 +08). Send back as in RUN-SHEET-gamma401.md.

**2. 14-cover census, primes 307 … 499 (33 primes), in this order.** New script `km1census.py` (sha256 87e0dcb2c3b9f93d79ac87dee83a7c99f31d3f2db359e8d94ccbdf1b91dc4646).
   - **Needs a non-author read record before dispatch.** GPT, since DeepSeek is blocked by risk control.
   - The script makes the same engine calls as the reducible branch of `kcascade_run.py` (`km1roots`, then `km1root` for each root) and runs the roots in parallel. It does not run the filterext step.

```bash
cd ~/lr16/code
date '+%F %T %Z' | tee ~/kit/census14.time
nohup python3 ~/kit/km1census.py ./bgk15 10 ~/lr16/census14 \
  307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 \
  419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 > ~/kit/census14.log 2>&1 &
# progress:  cat ~/lr16/census14/census14.jsonl
# restart-safe: run the same command again; finished primes are skipped
```

   - **ESTIMATE:** 10 to 40 minutes per prime with 10 workers, so roughly 10–20 hours for all 33. In `kcascade_run.py` the roots ran one at a time: 409 took 10,054 s and 401 took 14,341 s.
   - **Built-in checks:** 401 must give `covers` = 6 and 409 must give `covers` = 1, the numbers from the gate runs. If either differs, stop and send the log.
   - **Chair's local test** of the script (same engine, chair build): 191 → 42,114 and 223 → 33,694, both equal to the gate runs.

**3. Only if the PC is idle after item 2:** `bgk15 P km1low 13` for P = 317, 331, 337, one at a time (single thread; 10–30 minutes each). GLM's and Kimi's Round 1 rules both predict γ ≥ 14 for these.

## Send back

- `census14.time`;
- `census14.jsonl`, one line per prime;
- for every prime with 1 to 50 covers: the dedup file `km1_P_dedup.txt`;
- for larger counts: only the sha256 of the dedup file.

Copy times and hashes from the terminal. Status claim: OPEN until the chair reads.

## Not this weekend

- No new proof gates. Under Tuzi's decision of 2026-10-06, a gate run on one machine does not enter the ledger.
- The chair container restarts when the chat is idle, so it cannot reproduce multi-hour gates right now.
