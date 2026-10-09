BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 11:15 +08
RE: 猜公式 Round 3 packet (1aeab1c), rules header + own §A line + BEGIN…END block pasted verbatim (send text r3_send_grok.txt)
SEAT: grok
MODEL: Grok Expert (Heavy paywalled; Copy response)
CHAT: https://grok.com/c/7d2647f9-1607-4148-aaeb-2b7f5e4045b9

--- reply verbatim ---
§A — YES. Both chair refutations stand.

Qwen’s “keep only speeds aligned to multiples of 16” fails at the reduction step. FACT: L15 says {1,…,15} covers every prime p>16, and 1,6,19 sit in the 223 cover in the packet; none of those sets lie in 16ℤ. FACT: a speed v=(p−1)/2 obeys 2v≡−1 (mod p), so vt mod p is a half-turn, not a 16-scaled copy of a smaller residue. The p/2 case is exactly where the alignment map drops covering cells. IDEA: no repair that keeps the 1/16 threshold can restore it.

GLM’s “p²-size certificate” fails at the value step, not the size step. FACT (lever 4): the fractional cover number is exactly n/H≈8, and weight 1/H is optimal for primal and dual, so no pair-row matrix of size p² can certify 14. FACT: a real cover certificate is one witness speed per cell, size O(p), not p². A p² object is neither shorter nor strong enough.

§B — Pick 1 (discrepancy). It does not beat Lemma A’s 56.

FACT (packet): a piece of length ℓ holds at least pℓ−1 grid points, so L in k pieces forces at least pL−k hits; pL>k kills the cover. FACT (packet arithmetic): after scaling, k≤Σv≤13p/N, so L>13/N is the win condition. With the packet’s L≈0.114 that needs N>114, worse than 56.

PROOF (sweep; matches the packet rows: p=223 gives L=0.11364, 118 pieces, longest 0.003438; p=239 gives L=0.113778, 148 pieces, longest 0.002653):

| S | L | pieces | pL−k |
|---|---|---|---|
| 223 cover | 0.11364 | 118 | −92.7 |
| 239 near-miss | 0.11378 | 148 | −120.8 |
| {1,…,13} | 0.04224 | 12 | — |

IDEA: there is no useful uniform L₀≈0.114. Each speed forbids measure exactly 1/8, so 13 speeds can overlap down to the {1,…,13} value 0.04224 (and, under F5, to a speed-dependent speck). That pushes the naive N past 13/0.04224≈308. Options (i)–(iii) are open; the worst-case count loses.

§C — Terence Tao. Reason: the only route that still has room is a weighted piece discrepancy, which is his setting, and he has already written the lonely-runner reduction this note sits on.

Least sure: whether a weighted hit count (packet option iii), not pℓ−1, can push N below 56. Not checked line by line.

--- end verbatim ---
END LETTER
