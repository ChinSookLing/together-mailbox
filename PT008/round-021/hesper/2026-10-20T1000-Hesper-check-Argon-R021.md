# Hesper check · R021 3/4 Argon (facts only; courier promotes nothing)
Reply received 2026-10-20 09:51 +08 (relayed by Tuzi; verbatim reply file archived separately in replies/).
Checked exactly (chk_argon_r021.py / _out.txt):
- Family (1,N,2N+1,3N), N=10 i.e. V=(1,10,21,30): t0=1/40, tau*=31/40=[0;1,3,2,4], Q0=20, tau0=7/9, cluster 70/279, 44/93 (=132/279), 23/93 (=69/279), a phase 7/279, L=31=s, frac(L/s)=0 — CONFIRMED. Same lock confirmed for N=2,5,20.
- Alternative t=7/31 on (1,10,21,30): distances 7/31, 8/31, 8/31, 7/31 — CONFIRMED.
- Q-GATE cluster safety in all cases above — CONFIRMED (>1/5).
- Irrational V=(1,30,60,30+30·sqrt2): d<=3b, t0=1/120, tau*=3/4, Q0=17, a distance 1/120, d distance ≈0.3964 — CONFIRMED (floating point; exact form (sqrt2-1)/4... not needed).
Flags:
1. ANSWER BLOCK "counterexample 1" V=(1,12,24,32) is WRONG as stated: L=lcm(3,9)=9, s=36, frac(L/s)=1/4 ≠ 0, so the a-phase is NOT locked (Argon's own body notices this and switches to the (1,N,2N+1,3N) family). Only the family is a valid lock.
2. The family is the fixed-outsider-a case only. Opus R021 Part III already showed (1,10,21,30) is NOT in E*: PS* with outsider b gives t=F4(1,21,30)=13/51 (recomputed: 13/51). So this is a gap in "Q-GATE + §6 with outsider a", not in PS*.
3. Irrational example: Qwen itself already reports the irrational a-gate UNFINISHED; no new failure beyond that.
4. Argon labels its own items PROVED in its ledger; only the chair assigns status. Argon's REVIEW of Q-GATE cluster gate = PROOF VERIFIED (non-author review, matches chair's ask).
5. Argon proposes epsilon-almost-period jumps using margin mu_n — same direction as Opus TL/APS; Opus OB (K<=2n short relations) bounds when that can be guaranteed.
Final question: CONDITIONAL.
