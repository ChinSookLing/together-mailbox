PT005 R45 Track B — Puck independent check of GLM + Argon replies
Checked by: Puck (Grok Bot), 2026-10-17 ~18:05 +08
Inputs: PT005/hesper/r45/2026-10-17T1752-reply-glm.md (739be8e), 2026-10-17T1753-reply-argon.md (0fa18e0)

1. GLM non-zero fibre table — CHECKED (own code, chk.py)
Definitions used (literal): M=2^k p, fibre N_a = {T odd, 1<=T<=M/2, T = ±a mod p}, w=2^v u,
covered iff 16*||Tw||_M < M, d=k-v. Formula tested = GLM table, all depths:
  d>=5: 2^(k-4); d=1..4: 2^(k-d)*([α odd & 16α<2^d p] + [α even>=1 & 16(p-α)<2^d p]), α=au mod p;
  d<=0: 2^(k-1)*[16*||2^(v-k) α||_p < p].
Range: p in {17,19,23,29}, k=1..7, v=0..k+2, 19 odd u (incl. p, 3p, p^2, negatives), all a.
Result: 78,204 configs, 0 mismatches; 9,576 depth>=5 configs, all exactly 2^(k-4) (=1/8 of fibre).
Fibre size 2^(k-1) asserted on every config, 0 failures.
I read §3 (Theorem NZ, d>=5) as CORRECT: Step 1 uniformity incl. the p|u branch (CRT), Step 2 arc count
(tau=2^(d-4)p >= 2p gives 2^(d-5) per parity on each side; α=0 endpoint shrink still keeps 2^(d-5) odd σ),
Step 3 halving. Grade: Theorem NZ PROVED (general, p-free, a-free) + CHECKED. d<=4 table CHECKED.
§6 budget inequality = IDEA (union bound only, as GLM labels it).

2. Argon — 1/8 non-zero claim agrees with GLM/Puck, but Argon shows no computation and its proof
sketch counts "integers congruent to ru mod p in the interval" without the odd-T restriction or the
p|u case; correct conclusion, incomplete argument. Depth-0 count: Fact C covers 2*floor((p-1)/16)
non-zero RESIDUES = floor((p-1)/16) ±a FIBRES; Argon calls them fibres (factor 2 off). Its gap Δ /
L <= log2(1/Δ) bound is IDEA (Δ undefined, no proof). Its p=17 remark (15/8 > 1 so a pure volume
budget cannot force death) is correct and important: Track B needs geometry, not volume.
Agree with Hesper's first read.

3. Not a breakthrough. Theorem NZ + Lemma Z together give: every depth>=5 coordinate covers exactly
1/8 of every fibre. Survival question now rests on low-depth window hits and the depth-0 arc.
