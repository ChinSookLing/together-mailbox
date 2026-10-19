# Hesper check · R020 3/4 Argon + 4/4 DeepSeek (facts only)
Argon sha256 bbcb4edc0c036007… ; DeepSeek sha256 502edf4b9eeefe57… (journal machine copies). Script chk_argon_ds_r020.py, output chk_argon_ds_r020_out.txt.
Argon:
- Family V_N=(1,10N,20N+1,30N): in E_PS with a as outsider (t0=1/(40N), φ0=1/(40N)∉A) — CONFIRMED N=1,2,3,5,10.
- But Opus PS* (R020, outsider b/c/d tried next) succeeds on every tested N (e.g. N=1: t=13/51 via outsider b). So the family is not in E*.
- Argon's "LS+CLR v2 solves it": TRUE only with the FULL residue set (N=1: m=40,Q=1240,|R|=258,G=100, s-condition holds, t=273/1240 works). With the single LS residue ρ* the condition s≥5(B+C)/3 fails (s=30N+1).
- Argon text has a self-correcting draft passage ("Wait…") inside §5.1 (first family (1,10N+2,20N+4,30N+6) abandoned mid-text).
- Argon side claim "Q-ERC1(ii) counterexample (θ,w)=(1/3,4/3), R1=∅": FALSE. R1={1,2} (k=1: ‖1/3‖=1/3, ‖4/3‖=1/3). Argon's text itself wavers. The 2+1≤3 pigeonhole slip it names is real (also found by Opus).
- Reviews: PS VERIFIED, LS VERIFIED, APS VERIFIED (criterion only).
DeepSeek:
- V5 LS: τ*=3/4, m=4, ρ*=3 — CONFIRMED.
- Reviews: PS VERIFIED (conditional), APS VERIFIED (conditional), LS VERIFIED, Q-ERC1 PROOF VERIFIED, Q-ERC2 GAP FOUND.
- Disagreement for chair: Q-ERC1 — Opus GAP FOUND (R019 proof), DeepSeek PROOF VERIFIED, Argon GAP FOUND; Qwen re-proved it in R020 §2 (not yet reviewed). Strict (>1/5) version false (θ=1/5,w=7/5).
