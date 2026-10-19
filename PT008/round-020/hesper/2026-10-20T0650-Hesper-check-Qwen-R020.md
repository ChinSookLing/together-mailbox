# Hesper check · R020 2/4 Qwen (facts only; courier promotes nothing)
Reply in two pastes (journal machine copies): part 1 sha256 e561189a393f16b1… (labelled "第 1 段 / 共 6 段"), part 2 sha256 26b543b8ffc58703… (labelled "第 2 段 / 共 2 段", ends "（全文完）"). Sections §1–§9 + ledger all present; label mismatch only. Tuzi was offered two Qwen drafts; this is the Q-GATE draft.
Script hesper/chk_qwen_r020.py, output chk_qwen_r020_out.txt (exact Fractions, certified T4 from R019 check).
- Q-GATE (last continued-fraction convergent of τ*=S·F4(b,c,d) with denominator ≤ Q0=⌈20·max(1−θ,w)⌉): 20,000 random rational triples 0 failures (denominator ≤ Q0 and b,c,d distances ≥ 1/5); 5,000 triples with ~10^20 denominators 0 failures. Testing only; the proof (convergent error < 1/Q0 ≤ 1/(20M), Lipschitz) is for review.
- Note τ* > b·t0 ≥ 1/4, so the selected convergent is positive (not stated by Qwen; checked here).
- §4 example (a,b,c,d)=(1/7,1,101/100,2): τ=1/2, Q0=20, cluster distances 50/201, 101/402, 100/201 — CONFIRMED. Runner a at t=τ/S has distance 50/1407 < 1/5: Q-GATE alone does not seat a (Qwen says so: a-gate separate).
- §6 chair shape (7/20,2,5,6), t=9/8: distances 63/160, 1/4, 3/8, 1/4 — CONFIRMED.
- Q-ERC2 sufficient condition withdrawn by Qwen (matches Opus GAP FOUND). Q-ERC1 repair proof: not machine-checked here (Opus earlier found no counterexample q,q′≤40, non-strict).
- Reviews given: Opus LS PROOF VERIFIED (scope noted), PS PROOF VERIFIED, APS PROOF VERIFIED as conditional selector.
- Open per Qwen: a-gate for irrational shapes, general F5, general n.
