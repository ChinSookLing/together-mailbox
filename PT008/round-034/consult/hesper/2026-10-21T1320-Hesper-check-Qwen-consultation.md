# Hesper check · Qwen consultation reply "CTA-RS" (msg 56657ecf)
Facts only. CHECKED / exact counterexample, not proof.
1. ERROR (Step C, "直接生成公式"): at t0=(2k+1)Q/2, (P_i/Q)t0=(2k+1)P_i/2. For EVEN P_i this is an integer for every k, distance 0 — no choice of k (incl. k=∏ even P_i) fixes it. The claim "对所有 i，‖(P_i/Q)t0‖≥1/2" is false whenever some P_i is even.
   Exact counterexample (rational input, so u=P/Q exact, ε=0): V=(1,2): Q=2, P=(1,2), k=2, t=5/2 → distances 1/2, 0. V=(1,2,3) (project test input): Q=3, P=(1,2,3), k=2, t=5/2 → distances 1/2, 0, 1/2. Mechanism fails on the project's own test input. Attacks: the CTA-RS rule (not FW₄, not TF).
2. Section 3 revised formula (c_j∈{0,1}, 2^{n−1} combinations of LLL basis vectors): no proof that any combination lands phases in [1/2−η,1/2+η]; author lists the needed bound as unproved. IDEA.
3. "n=3 坏集测度 8/9": 1−(1/3)²=8/9 for 2 speeds at δ=1/3 (torus measure) — MATCH; note it is a measure statement on the torus, not a time statement for dependent speeds.
4. Nonemptiness ① untouched; "直接性" claim rests on the unproved bound.
