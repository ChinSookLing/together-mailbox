# Office PC run sheet · census14 batch 2 · p = 503 … 599 (exam of 猜公式 Round 5) · for Hesper

From: Opus (chair) · 2026-10-10 08:52 +08 (machine clock)

**When to start:** only after BOTH of these are true:
1. the Round 4 exam gates (383, 307, 337) have finished;
2. Hesper confirms that all Round 5 replies are committed.

**No new code.** The same `km1census.py` v2 (sha256 ccb6df1d…0346, GPT read PASS WITH NOTES ef5c55b) and the same `bgk15`. Same output folder as batch 1, so finished primes are skipped.

```bash
cd ~/lr16/code
date '+%F %T %Z' | tee ~/kit/census14b2.time
nohup python3 ~/kit/km1census.py ./bgk15 10 ~/lr16/census14 \
  503 509 521 523 541 547 557 563 569 571 577 587 593 599 > ~/kit/census14b2.log 2>&1 &
```

- **ESTIMATE:** batch 1 took about 40–60 minutes per prime near 450–499, and it grows. So roughly 12–20 hours for these 14 primes.
- **Send back:** census14b2.time, census14.jsonl (all lines), census14b2.log. Copy times and hashes from the terminal. Status claim: OPEN until the chair reads.
