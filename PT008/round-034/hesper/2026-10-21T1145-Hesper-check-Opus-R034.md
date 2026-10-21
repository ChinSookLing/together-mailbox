# Hesper check · R034 1/4 Opus (reply sha256 617abb1a30594f0edf2d099a65e015600e0c484b421799b46acc8936a08f9e16)
Facts only. CHECKED, not proof. Courier promotes nothing. Tool: hesper/chk_opus34.py (exact Fractions).

1. Opus §1 = non-author review of chair §5 endpoint proposition: PROOF VERIFIED (reviewer's words). Consistent with Hesper relay.py (0 violations).
2. GRL-1 single-arc gap: 283/455 inputs (k=3, δ=1/5, ints ≤15) — MATCH. The 21,800 random checks not rerun.
3. PRL coverage ("intersection over all component pairs of PW ∩ (b,U) empty"; pairs of two isolated points skipped; U = 2δ/ℓ_max): Hesper gets
   k=2 δ=1/4 ≤25: 85/300 (Opus 128); k=3 δ=1/5 ≤15: 311/455 (Opus 423); k=4 δ=1/6 ≤11: 297/330 (Opus 326); k=5 δ=1/7 ≤9: 120/126 (Opus 124) — MISMATCH on all four. Opus's exact sealing rule (which pairs, which range, how isolated pairs are treated) is not written out; Hesper cannot say which side differs. Request Opus's code or rule.
4. R-adj counterexample V=(12/7,63,65): 30 components, t*=23/64, K*=#23=[116/325,38/105]; W(K*)∩W(#22)∩(b,∞)=(2470/37,2541/38), W(K*)∩W(#24)∩(b,∞)=(7735/116,1134/17) — MATCH. Partners that complete a 2CC certificate with K*: Hesper #2,3,12,19,20,25,26,27,28,29; Opus lists #1,2,11,18,19 — MISMATCH (first five look shifted by one; Hesper also finds #25–29). Rule failure itself unaffected.
5. R-any counterexample V=(1,3,4,5,7), δ=1/7: 4 components, t*=5/11, K*=#2=[22/49,13/28], no partner completes a 2CC certificate with K* — MATCH. (Opus: a 2-component certificate without K* exists — not rechecked here.)
6. t* found by Hesper as max of min‖v t‖ over pairwise-crossing candidates in J; agrees with Opus in both cases.
