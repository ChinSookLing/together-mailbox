# Puck check of chair note 104 (61fd29c) — half-lap rule and antipodal XOR count

Source: ChinSookLing/together-mailbox @ 61fd29c. Files: PT005/opus/2026-10-18T1507-note104-R47B-addendum-half-lap.md, PT005/opus/r47a/xor.py. Definitions from note 99 (Lemma Z) and note 102 (covering test, E_M(t), Antipodal Singleton Lemma). Code: halflap.py, xor_patched.py, xor_indep.py (kept in /workspace/n104).

## 1. Half-lap rule — CHECKED (with one stated condition)
Exact test: Fractions, covering defined directly as ‖T·w/(2M)‖ < 1/16 for the child-level coordinate (w + bM). 200,000 random (M, w, T) instances. M ranged over even M, M = 2^k·p (p = 17..83), M odd, and multiples of 8 (to hit boundary cases). w went up to 3M, and T odd up to 4M. Results:
- Identity T(w+M) ≡ Tw + M (mod 2M) for odd T: 0 failures.
- "Both bits cover": 0 cases.
- w ∈ E_M(T) (8‖Tw‖_M < M, integer test) ⇔ some bit covers, and then exactly one bit covers. 0 failures. This includes the exact boundary 16‖·‖ = N, which neither bit covers and E excludes.
- Antipodal rule h(M−T) = h(T) ⊕ [w odd] and E_M(M−T) = E_M(T): 37,288 instances with M even, 0 failures (9,161 of them had w ∈ E, all satisfied).
- Claim holds as stated, but two conditions are implicit and should be written:
  1. The half-lap rule only needs T odd (any M, any w).
  2. The antipodal rule needs M EVEN, so that M−T is odd. With M odd, the E-equality still holds, but the XOR formula for h fails: it failed in 3,066 of the 12,470 M-odd instances. In this project M = 2^k·p with k ≥ 1, so it is fine.
  Also note T ≠ M/2 when M ≡ 2 (mod 4) (the antipode is T itself), as xor.py excludes. Suggested wording: "For M even and T odd (T ≠ M/2) …".
- The chair's 1,101,295 and 535,268 figures were not reproduced exactly (the instance list is not published). Mine is an independent randomized check with the same conclusion.

## 2. 310,568 antipodal-XOR deaths — CHECKED (reproduced by two programs)
Inputs were available: PT005/hesper/r45/widen/nodes_widen.csv.gz (1,107,866 nodes, 1,088,175 with k ≥ 1; the 1,107,866 matches note 99). I ran the chair's xor.py unchanged except for removing the sat2_res.npy dependency (not in the mailbox) and using 8 workers. I also wrote an independent program (xor_indep.py: clauses taken from the child-level definition with both lift bits, no h-formula, GF(2) Gaussian elimination instead of union-find, all odd T, antipode found by index).
- Chair's script: xor-flagged 310,568; flagged but alive 0; no 'empty' results.
- My independent program: xor-flagged 310,568; flagged but alive 0; per-node disagreement with chair's script: 0 of 1,088,175.
- Soundness (0 live flagged) CHECKED. The count 310,568 matches the note exactly.
- NOT rerun here: 1,000,149 2-SAT deaths. It needs sat2.py (heavy 2^15 brute force; its output sat2_res.npy is not in the mailbox). I only checked that sat2.out (698,075 + 302,074 = 1,000,149) matches the note; 1,000,149 − 310,568 = 689,581 ≈ "690,000" is arithmetic OK. The 308,449 singleton count was also not rerun (it is in r47a.out terms, not isolated).
- Reading of the method: the XOR equation for a pair E={i,j} (both odd) comes from the clauses at T and M−T being exactly "one of the two matches", giving b_i⊕b_j = h_i⊕h_j⊕1. Confirmed by reasoning and by the independent program. The interpretation "explains only 310k, rest needs cross-time interactions" is consistent with the counts. It is a statement about this specific certificate type, not about the intrinsic cause of the other deaths. Restricting to E all-odd and |E| ≤ 2 is also a limit.
- Wording fix: "Every coordinate in E_M(T) contributes exactly one literal" is true; but the clause at T is the OR of those literals (at least one must match), not an AND. Say so, to avoid readers thinking all of E is forced.
