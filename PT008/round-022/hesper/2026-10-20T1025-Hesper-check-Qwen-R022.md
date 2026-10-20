# Hesper check — R022 2/4 Qwen (facts only; courier promotes nothing)
Received 2026-10-20 10:20–10:23 +08 in 3 parts (journal msgs 1cf1f93d, 9d3334d9, b396f336). Verbatim: replies/2026-10-20T1020-reply-Qwen-R022-part{1,2,3}of3.txt.

Exact checks:
- (1,N,2N+1,3N): S=s=L=3N+1, frac(L/s)=0 for N=2,5,10 — CONFIRMED (matches Hesper R021 check N=2,5,10,20). General: with integer a | S, L/s = a ∈ ℤ, so frac(L/s)=0 holds whenever q_θ=q_w=S; Qwen's §2.3 condition is consistent.
- N=10: 31/40 = [0;1,3,2,4], convergents 0/1,1/1,3/4,7/9,31/40; last q≤20 → 7/9; a-phase 7/279 < 1/5 — CONFIRMED.
- τ=7 (t=7/31): 7/31, 8/31, 8/31, 7/31 — CONFIRMED; (7−7/9)/31 = 56/279 ∉ ℤ, so τ=7 is off the 7/9 L-orbit — CONFIRMED.
- PS correction: F_n(V)=F_{n-1}(V∖u)+j·P_u — now matches PS.

Courier flags (for chair; no ruling implied):
1. Qwen §3 calls E*_n a "rule artifact" using the definition "structural = no safe time exists". Opus R022 TF/CORE uses a different notion: C_n (every solution leaves ≥2 runners below 1/n) is a genuine obstruction for the whole old-threshold-preserving class (PS, PS*, any F swap). λ(1,…,n) and (1,3,4,7) lie in C_4-type core (Hesper confirmed their safe sets are isolated points). The two claims use different definitions; Qwen's evidence covers only the (1,N,2N+1,3N) family, which is NOT in the core.
2. Q-ERC1 non-strict: unchanged status — one non-author VERIFIED (DeepSeek R021); still PROOF CANDIDATE per author.
3. Mandatory answer: CONDITIONAL; missing hypothesis = gap-bounded safe-time family, not automatically preserved (same direction as Opus §5.3/§5.4 and DeepSeek track item 4).
