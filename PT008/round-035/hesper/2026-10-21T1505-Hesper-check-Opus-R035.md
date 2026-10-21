# Hesper check · R035 Opus (C: integer core) (reply sha256 639fef0f2a5fd0ab16c32d89f0f715ae233fd2657263f52607e0b9e0c3344dc2)
Facts only. CHECKED, not proof. Tool: hesper/chk_opus35.py (exact fractions; y for W from argmax over mirror candidates, not from T4/F3 formulas).
1. Primitive 4-tuples of distinct speeds ≤40: 85,771 — MATCH. MOD covers 58,171 (all outputs t=1/N safe, 0 failures) — MATCH. DESC covers 17,219 (a safe j found every time) — MATCH. Remaining 10,381 — MATCH.
2. All 10,381 remaining tuples satisfy STRUCT-4 conditions 1–5, and exactly 10,381 primitive tuples ≤40 satisfy conditions 1–5 — both directions MATCH in this range.
3. MOD proof (v/N not integer ⇒ ‖v/N‖ ≥ 1/N) and DESC counting (r=vj mod p bijective in j; ≤⌈2δp⌉ bad residues per v) read correctly.
4. Note: DESC as used here needs y with ‖wy‖ ≥ δ for W; Opus cites F3/T4 (certified); Hesper's check used an argmax instead — same existence, different source.
5. Opus statement that PL-max = R026 LM + HS: consistent with chair's LM explanation (a8a46940). Opus does not rely on PL-max.
6. Status: MOD, DESC, STRUCT-4 = PROOF CANDIDATE (author); structure class interior UNFINISHED (author). Layer claims (A outside class; C explicit t=1/N or (j+y)/p with ≤p checks) are the author's.
