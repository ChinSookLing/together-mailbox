# Hesper check · Copilot consultation reply (msg 81a68eea; reply file + sha256 filed when journal copy lands)
Facts only. CHECKED / precise obstacles, not proof.
1. FBC algebra: (q_{r+1}−δ)/v_{i_{r+1}} ≤ (q_r+δ)/v_{i_r} ⟺ q_{r+1}v_{i_r} − q_r v_{i_{r+1}} ≤ δ(v_{i_r}+v_{i_{r+1}}) — algebra MATCH.
2. ERROR (strictness): the failure arcs I_r are OPEN. If two adjacent arcs only touch (equality), the common endpoint is uncovered, i.e. a safe point (this is exactly how isolated safe points arise). A cover requires STRICT inequality: q_{r+1}v_{i_r} − q_r v_{i_{r+1}} < δ(v_{i_r}+v_{i_{r+1}}). With ≤ the method would lose isolated points — the very case Copilot wants to protect.
3. Same-speed arcs: centres 1/v apart, half-width δ/v, gap (1−2δ)/v > 0 for δ<1/2 — MATCH; adjacent labels must differ.
4. Descent gap: a cover of [0,T] exists for every input when T < F^min (the first safe time). So deleting a label and obtaining a (k−1)-speed cover of [0,T] contradicts F_{k−1} only if F_{k−1} guarantees a safe time ≤ T. The descent therefore needs a time bound T (same as UB_n in Hesper's reply), otherwise no contradiction. Threshold direction is fine: a safe time at δ'=1/(n−1) is also safe at δ=1/n.
5. Link (fact): for any input, the first "crack" of the minimal cover of [0,T], T→∞, is min S = F^min, the same time as Hesper MIN / Puck ECT (left endpoint (z+δ)/v_i).
6. Status: FBC private-witness step = PROOF CANDIDATE (standard minimal-cover argument, correct); compression theorem = UNFINISHED (author says so).
