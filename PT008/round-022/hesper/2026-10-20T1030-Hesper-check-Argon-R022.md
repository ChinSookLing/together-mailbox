# Hesper check — R022 3/4 Argon (facts only; courier promotes nothing)
Received 2026-10-20 10:26 +08 (journal msg 2f320b2f; verbatim file to be extracted next run → replies/2026-10-20T1026-reply-Argon-R022.txt).
Method: exact Fraction, T4 as implemented in pt008r20/hesper/base.py; exact breakpoint scan for safe sets.

V=(1,2,9,30) — body calculations CONFIRMED:
- u=1: F4(2,9,30)=2/11, phase 2/11 ∉[1/5,4/5]; u=2: F4(1,9,30)=49/120, phase 49/60 ∉A; u=9: F4(1,2,30)=41/120, phase 3/40 ∉A; u=30: F4(1,2,9)=13/36, phase 5/6 ∉A. All g_u=1, x_u=0 → V ∈ E*_4(T4) under PS*_4 — CONFIRMED.
- LS-R on (B,C,E)=(2,9,30): τ*=2, m=1, Q=11, R={2,9} (strict and non-strict same), G=7, 5G/(3m)=35/3 > s=11 → LS-R condition fails — CONFIRMED.
- t=41/150: distances 41/150, 34/75(=68/150), 23/50(=69/150), 1/5 — CONFIRMED safe (≥1/5; d exactly at 1/5). t=3/11 alone: d at 2/11 (unsafe), as Argon says.

INCONSISTENCY in Argon's ANSWER BLOCK (do not adopt): it lists phases 1/8, 2/33, 1/35, 6/11 (or 2/31) and LS-R R={4,5,6,7}, G=8, bound 40/3. These do NOT match Argon's own body nor Hesper's computation (2/11, 49/60, 3/40, 5/6; R={2,9}, G=7, 35/3). Body figures are the correct ones.

Relation to Opus R022 CORE (facts only): (1,2,9,30) is NOT in the structural core C_4 — t=1/4 is safe (1/4, 1/2, 1/4, 1/2) and for every outsider u the other three are ≥1/4 (88 such (t,u) witnesses found in exact scan). So it is a selection-rule exception E*_4(T4)∖C_4, consistent with both Argon's "artifact" reading and Opus CORE.

Courier flags:
1. Argon labels its own counterexample "PROVED" — author self-label; chair decides.
2. Argon's REVIEW gives PROOF VERIFIED to all of Opus PS_n…OB "within their stated hypotheses" in one line, without per-item argument; H "PROOF VERIFIED WITH CLARIFICATION".
3. That SLN1 (certified rule) outputs exactly 41/150 on this V: NOT checked by Hesper (Argon's derivation is "lock (b,c), nudge d").
4. Claim that OB "keeps creating new E*_n at every layer" is a generalization beyond OB's stated scope (OB is only about TL guarantee version).
Mandatory answer: CONDITIONAL.
