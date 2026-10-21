# Hesper check · DeepSeek consultation reply (msg 2720aab0; reply file + sha256 filed separately when journal copy lands)
Facts only. CHECKED / precise obstacle, not proof.
1. MALP output t=max_i (q_i+δ)/v_i with q_i/v_i nearly equal (=: t0 up to ε). Then v_i t ≈ q_i + δ·v_i/v_min (+ small), i.e. MALP reduces to the q=0 time t=δ/v_min shifted by a near-integer time t0. A near-integer time t0 (all v_i t0 ≈ integers) is phase-equivalent to t=0, the worst time; so lattice reduction adds nothing beyond t≈δ/v_min.
2. Exact consequence (q=0 case): t=δ/v_min is safe ⟺ δ·v_i/v_min ≤ 1−δ for all i ⟺ v_max ≤ (n−1)·v_min (all speeds within factor n−1). Outside that band MALP inherits the original problem: one needs s with v_i s ∈ [δ,1−δ] mod 1 for all i — circular.
3. Proposed test (1,19/10,2,3), δ=1/5: v_max/v_min=3 ≤ 4, so t=1/5 is safe (distances 1/5, 19/50, 2/5, 2/5). MALP would "save" it, but only through fact 2, not through LLL. Not evidence for the method.
4. Lattice B as written (row (v_1..v_k) over e_1..e_{k−1}) is not a standard simultaneous-approximation basis; no reduction bound given. LLL factor 2^{k/2} weakness acknowledged by author.
5. "PT-005 已经证明在某些离散结构下这个假设是假的" — no reference given; NOT VERIFIED.
6. Status: MALP = IDEA (author). Nonemptiness ① untouched.
