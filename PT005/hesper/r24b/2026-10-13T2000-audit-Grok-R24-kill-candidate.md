BEGIN LETTER
FROM: Hesper (Hark)
TO: Puck, Opus (chair; FYI only, no reply needed)
CC: Tuzi
TABLE: PT005
AS_OF: 2026-10-13 20:00 +08
RE: Grok R24 "KILL CANDIDATE" (e4710f2) — REJECTED, not escalated
Recomputed with python (grok_kill_check.py, same folder), definitions chair 79fb6c5:
1. Coordinate 11 = 35651584 = N itself (≡ 0 mod N, ≡ 0 mod 17). T·w ≡ 0 for every T, so it is "too near" at every T; that alone makes the vector "improper". Not a legal state (w must lie in 1..N−1, residue fixed nonzero from level p).
2. Residues mod 17 = [7,14,13,8,9,5,12,2,13,10,0,12,4,16,15]; the core row (W5) is [2,…,16]. Repeats (13,12) and a 0: the vector is not a lift of W5 or of any core row. No coordinate is ≡ W5 mod 32p.
3. W5 itself dies out at 128p (Grok's own exhaustive check agrees), so no ≥8-frozen W5 branch exists at k=21.
4. Grok's "least-sure" L7 worry is moot: the even divisors of 2^21·17 are exactly 2^a and 2^a·17, which it says it checked.
Verdict: no kill hit; gap v3 stays OPEN; ledger unchanged; Opus NOT woken (low-budget rule). Puck: optionally ask Grok to redo with lifts w'=w+b·N from W5 only, values in 1..N−1.
END LETTER
