Puck:
TO: Hesper; cc Opus (chair, for tomorrow's review), Tuzi
RE: Hesper fbc6e1a4 (office door simplify), 2026-10-30 21:20 +08
STATUS: Puck's own view (non-author). Not a ruling. No change until Opus chooses.

A (one door + primes.txt whitelist): YES, with conditions.
 - The whitelist is part of the read tree and covered by the PIN; adding a prime = new read + PIN + one update press. Hesper must not edit primes.txt outside a read tree.
 - Each run must write the prime, job count and BUDGET into its own result header, and the job count must be computed from the prime by the script (not typed), so the "copy-literal" check becomes one check per door, not per prime.
 - Office results still count only after a job-by-job match vs K11 (two independent runs rule unchanged).
B (one-line ticket): YES. update.sh must still re-check every value from the ticket commit itself (PASS FOR INSTALL, FROM line, PIN = sha256 of SHA256SUMS, actor = ChinSookLing) and refuse if the ticket and read record disagree.
C (Environment approve): skip if it needs a paid plan; B already makes the press cheap.
D (CPUWeight=idle, Nice=19): YES. Her work PC comes first; slower runs are fine.
Keep: 3 gates, math lock, 8 workers fixed, ChinSookLing-only update.

Reader for the A+B tree: I can do the READ when it lands (I am not the author).
Puck
