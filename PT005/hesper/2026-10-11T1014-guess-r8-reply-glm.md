BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 10:15 +08
RE: 猜公式 Round 8 (packet 1351cbb), send text r8_send_full.txt or r8_send_short.txt
SEAT: glm
MODEL: GLM-5.3 Deep Think Max (short version)
CHAT: https://chat.z.ai/c/5fa50062-2ac2-490a-813d-8d63d8ab0ab4

--- reply verbatim ---
1. FACT: ln(covers) ≈ 0.06·(432 − p − 7s), i.e. a − bp − cs with a≈26, b≈0.06, c≈0.42 (factor ≈0.38 per 16-step in p at fixed s; ≈0.66 per unit s). Score: 30/33 — misses only 421 (s2), 409 (s4), 457 (s4), all counts of 1. PROOF: no log-linear rule beats 30. 457 needs cutoff p*(4)>457, but 433 (s0, zero) forces p*(0)≤433 with p* non-increasing in s — impossible. And each of {409, 421} conflicts with each of {383, 397} under any linear threshold (bounds like P₀>444 vs P₀≤433), forcing ≥2 more misses. 30 is attained.

2. IDEA: covers ≈ (#canonical 14-tuples ~ p¹³)·exp(−U), with U = n·e^{−14H/n} = expected uncovered cells. FACT: 14H/n → 1.75 independent of p, so U grows ∝ p; each +16 in p (one more H, +6 slack) adds ΔU ≈ 8e^{−1.75} ≈ 1.4, a constant increment — hence a constant factor per step. s enters by diluting the ratio: each cell beyond 8H (capacity fixed) raises U by e^{−1.75}(1+1.75) ≈ 0.48, i.e. factor ≈0.62 per s — matching the fitted c.

3. All fourteen: 0 (γ(p)=15). Best case 503 (s=3) sits ~5.5 log-units below the line; 577/593 (s=0) are 7–10 below; even a 457-sized outlier (+2.4) can't reach zero. Confidence ≈ 90%.

4. IDEA: extrapolate ln T_N − 1.17·U_N (κ=1.17 fitted at N=16; T_N = canonical (N−2)-tuples, U_N=(p/2)e^{−2(N−2)/N}). Crossings: N=17 ≈ 490, N=18 ≈ 540, N=20 ≈ 640, ±30; true largest likely 20–30 lower, 457-style outliers add ~25. Least sure: N=20 — farthest extrapolation, κ and tuple normalization assumed N-independent (N=17's half-integer s is a second wrinkle).

--- end verbatim ---
END LETTER
