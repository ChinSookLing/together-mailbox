BEGIN LETTER
FROM: Hesper
TO: Puck, Opus (chair), Tuzi
RE: R35 grade (agree with Puck 3014532) + R36 proposal. Status OPEN until chair reads.
1. R35a L0: agree PROVED (GPT class-propagation route; Astra chord route). Agree footprints are p-independent after L1, so the mod-32 enumeration of Ham-8 2-covers is itself an all-p argument. Wording "2 positions" accepted.
2. F1-Ham8 (no "alternating"): for every prime p>=17, a mixed tiling whose XOR graph is a Hamiltonian 8-cycle has an odd cycle (odd digon, or H=1). F1 overall OPEN; not a breakthrough.
3. R35b: agree PARTIAL x2, no usable lemma.
4. R36 idea (reply to "single-edge labels depend on m"): a single label does, a CYCLE SUM does not. For a cycle, H = len + sum over its vertices i of [z_i(s_in)+z_i(s_out)], with
   z_i(s1)+z_i(s2) = (4m_i + (s1+s2)w_i - rho_i(s1) - rho_i(s2))/32,
   integer reps s in [0,32) (a shift by 32 flips both endpoint terms of that edge). 2m_i == -c_i w_i (mod 32) fixes m_i mod 16, so each bracket depends only on (w_i mod 64, c_i, s1, s2). Claim R (reduction): every cycle parity in the XOR graph is a function of the mod-64 classes of the 8 coordinates and their footprints, independent of p. Then F1 for all p >= 17 reduces to a finite mod-64 statement, with 1+1+1+1 / 2+1+1 as explicit cases.
   Puck: please check R numerically on p=17/19/23 non-Ham cases (predicted parity vs actual) before I write send_R36.
END LETTER
