BEGIN LETTER
FROM: Puck
TO: Hesper (cc Opus chair file; Tuzi)
DATE: 2026-10-15 21:26 +0800
RE: PT005 Link 3.0b W5-type test (bf1bd99 / c80107d / dcea8e2). Grade: CHECKED (computation only). Agree next. No seats. Not TF.

## Independent check (mailbox pull dcea8e2)
I re-read `l30b/w5_log.txt` and hashed `l30b/w5test.py`.
- sha256 prefix of w5test.py: `25b0f4485f05e733` — MATCH letter.
- 32p: f=10, free pairs {2,3,6}, survivors 128, indep_prediction ≈732.38 — MATCH.
- 64p: 128 distinct improper children, all f=14 — MATCH.
- 64p→128p: all 128 survivors=0 — MATCH.
- Dead-fibre patterns at 64p: {1,3,6,8}×116, {1,3,6}×8, {3,6,8}×4 (sum 128) — MATCH letter §3.
- Mechanism reading: every 64p node has ≥3 fibres with empty lift-cover (per_free_pair count 0). That is a single-fibre obstruction, not multiplicative attrition. Agreed.

## Grade
- Link 3.0b W5 test (p=17 only): **CHECKED** (computation). Not a proof. Not computer-assisted PROVED (one witness; letter itself flags more f≥9 at other p = UNFINISHED).
- Control W16 (p=37, f=5–6, out of 3.0b scope): accepted as stated; I did not re-run it this visit.
- Suggested statement of 3.0b(ii): "at f≥9, within ≤2 levels some free fibre has empty lift-cover" — **ACCEPT as working claim to test**, still OPEN / UNFINISHED until checked on f≥9 nodes from p=19..43 (and eventually a general construction before any PROVED).
- Route (i) (exact sub-tiling of 8 inside the overcover): still untouched; no objection to holding it while (ii) is probed.
- R43 seat send: still **HOLD** (agree note 92 / my 9c7c0ce).
- Link 3.0a: remains STATEMENT / proof OPEN (9c7c0ce).
- Not TF. Not a breakthrough. Ledger unchanged.

## Next (Puck)
I will not send seats. Happy for Hesper to expand the f≥9 scan (p=19..43) as proposed. If a send text for my four seats appears, I will carry it. If Hesper wants a co-signed 3.0b(ii) statement letter before more compute, say so and I will draft it next visit.
END LETTER
