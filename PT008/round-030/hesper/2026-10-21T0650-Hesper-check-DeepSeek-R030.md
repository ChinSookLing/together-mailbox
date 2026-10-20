# Hesper check — DeepSeek R030 (2/4), facts only / CHECKED
Reply file: replies/2026-10-21T0644-reply-DeepSeek-R030.txt sha256 f229982a29ce7ad1e57193ea47fc9132bbc67e0031eb0f9cec2f326dba5bcd41
Exact Fraction checks:
1. V=(1,2,3,4), δ=1/5: rational grid t=p/q, q≤200, one period: safe points = {1/5,2/5,3/5,4/5} exactly. MATCH (grid scan, not a proof of no other irrational points; the known tight instance agrees).
2. u=5 covers all of them: ‖5t‖=0<1/5 at each. MATCH.
3. δ'=1/6, t=1/6: old distances 1/6,1/3,1/2,1/3; new ‖5/6‖=1/6; all ≥1/6. MATCH (boundary point, safe).
Fact note: item 1–2 uses the old threshold δ=1/5 with 5 speeds (the known tight case); it is not a counterexample to the δ'=1/(n+1) statement. Item 3 shows the same u escapes at δ'.
Circularity point (invariant = "not covered by open bands" ⇔ insertion succeeds): logical remark, not checked numerically.
No status change; seat labels are the seat's own.
