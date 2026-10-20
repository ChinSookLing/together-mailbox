# Hesper check — R022 1/4 Opus (facts only; courier promotes nothing)
Received 2026-10-20 10:16 +08 (Tuzi msg a39a8e73). Verbatim reply file: to be extracted from project journal on next run → replies/2026-10-20T1016-reply-Opus-R022.txt.

Exact-Fraction checks (Python Fraction, exact breakpoint interval scan on [0,1]):
- (1,10,21,30) at t=7/31: 7/31, 8/31, 8/31, 7/31 — CONFIRMED. At t=13/51: 13/51, 23/51, 6/17, 6/17 (all ≥1/5) — CONFIRMED.
- (1,3,4,7) safe set at 1/5 = {1/5,2/5,3/5,4/5}, isolated points; t=1/5 → 1/5,2/5,1/5,2/5; t=2/5 → 2/5,1/5,2/5,1/5 — CONFIRMED (two runners at exactly 1/5 each, i.e. <1/4).
- V_n=(1..n) safe set at 1/(n+1): n=3 {1/4,3/4}; n=4 {1/5..4/5}; n=5 {1/6,5/6}; n=6 {k/7, k=1..6}; n=7 {1/8,3/8,5/8,7/8} — CONFIRMED, all isolated points (matches TF(i): t≡k/(n+1), gcd(k,n+1)=1).
- H3 argument (w_max t0 ≥ ‖w_max t0‖ ≥ 1/n > μ ⇒ t0 > h) — read, logic as stated holds (not a certification).
- Counts 1,689 / 11 core / 1,678 (1,649 a / 17 b / 12 c) and 18,090/27,405: NOT rechecked by Hesper (no exception list re-run this round) — UNFINISHED on courier side.
Status of all Opus items as reported by author: PROOF CANDIDATE / CHECKED / IDEA; awaiting chair & non-author review. Mandatory answer: CONDITIONAL.
