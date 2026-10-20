# Hesper check — R024 1/4 Opus, 2/4 Qwen, 3/4 Argon (facts only; courier promotes nothing)
Received 11:43 Opus (msg 09332c2f), 11:43 Qwen (f8213c33), 11:44 Argon (f95de4ee). Note: Track C packet was redrafted for Kimi at 11:41, but the 3/4 reply came from Argon.
## Opus (exact Fraction, independent code)
- B_V1: 14 breakpoints, list identical to Opus's (0,0)…(1/2,0) — CONFIRMED. |B_V2|=48, |B_V3|=152 — CONFIRMED.
- §5 table, δ'=1/(k+2): (1) ℓ1/3 r2/3 ratio 2; (1,2) 1/8,1/2,4; (1,2,3) 1/15,2/5,6; (1,2,3,4) 1/24,1/3,8; V1 1/24,1/3,8; V2 1/45,31/90,31/2; V3 11/1440,31/90,496/11 — all CONFIRMED.
- Densities at 1/6: (1,2,3,4) 5/36, V1 8/63, V2 7/30, V3 157/720 — CONFIRMED.
- MZ n=4: S_{1/6}(1,…,5) has measure 0, points 1/6, 5/6 in [0,1); distances at 1/6: 1/6,1/3,1/2,1/3,1/6 — CONFIRMED.
- Not checked: general MZ proof, GLC/GLC-FAIL/DU/FU/EQ proofs (PROOF CANDIDATE by author).
## Qwen
- S_{1/6}(V1): six intervals [1/6,5/24], [7/18,17/42], [19/42,11/24], [13/24,23/42], [25/42,11/18], [19/24,5/6]; widths 1/24,1/63,1/168,1/168,1/63,1/24; total 8/63 — CONFIRMED, except typo: Qwen writes 4th interval as [13/24, 19/42]; correct right end is 23/42 (width 1/168 as stated).
- §5 integer criterion ⌈uα−1+δ'⌉ ≤ ⌊uβ−δ'⌋: correct as a restatement of overlap.
- §2 sufficient condition w>1/u is valid but weaker than Opus GLC(i) (w ≥ 2δ'/u suffices).
## Argon
- Reviews Opus SPC. Claim "C DISPROVED" rests on a hypothetical V with no safe time; no concrete V given, no numbers. Opus did not claim C (Opus R023/R024: nonempty ⇔ the layer's existence theorem). Uses older bound form (n−1)(σ+1) = Opus R024 k(σ+1).
- "Bound and interpolation logic CHECKED by hand": no calculation shown.
