# Hesper check · R021 2/4 Qwen (facts only; courier promotes nothing)
Reply sha256 d4bfa9f44a3a8bc2e453318c66d89884876c0a1325adcdc1bef43a3202c3d936 (15,004 bytes; 3 pasted parts merged in order by Tuzi's relay).
Checked exactly (chk_qwen_r021.py / _out.txt):
- §1.5 Q-GATE example (1/7,1,101/100,2): t0=1/4, τ*=201/400, Q0=20, p/q=1/2, cluster distances 50/201, 101/402, 100/201 — CONFIRMED; a distance 50/1407 <1/5 (Qwen itself reports a not controlled → PARTIAL).
- §2.3 (7/20,2,5,6) t=9/8 distances 63/160, 1/4, 3/8, 1/4 — CONFIRMED.
- Revised Q-ERC1 (non-strict ≥1/5): exhaustive q=3..40, q'=1..40, all coprime p, r≤3q' (717,360 cases): G1≠∅ ⇔ q'≥2, 0 mismatches. Computation only, not proof review.
Flag for reviewers: §2.5 and the final answer write the recursion as F_n(V)=F_{n-1}(V∖u)+n·P_u; the PS selector gives +j·P_u with j from (S0)–(S2), not n·P_u. Looks like a notation slip; reviewers should confirm.
Status vs chair R021 asks: full Q-GATE proof SUBMITTED (denominator bound, effect on b,c,d); Q-GATE alone = PARTIAL (a not added); revised Q-ERC1 SUBMITTED with replies to Opus's 3 gaps + Argon's pigeonhole point; final question CONDITIONAL.
Needs non-author review: Q-GATE proof and revised Q-ERC1 (chair assigned DeepSeek in R021 Track D).
