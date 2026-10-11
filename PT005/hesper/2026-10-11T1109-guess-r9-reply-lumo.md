BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 11:09 +08
RE: 猜公式 Round 9 (packet ec15a2d), send text r9_send_full.txt or r9_send_short.txt
SEAT: lumo
MODEL: Lumo 2.0 Lite, Fast mode, web off (short version)
CHAT: https://lumo.proton.me/u/20/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
Formula for P*(N): Based on "expected count = 1" and the exponential decay model, P*(N) ≈ A·N² + B·N + C. Fit: A ≈ 1.6, B ≈ −10, C ≈ 50. Errors: N=16 (pred ~310, actual 457 - underestimates outlier effect), N=17 (pred ~340, actual 479), N=18 (pred ~380, actual 523), N=20 (pred ~460, actual 661). The quadratic trend holds, but the intercept is shifted by the "consecutive block" survival mechanism.

Small N (8…15): Exhaustive searches exist for N ≤ 10 (known to be very large or infinite for small N due to density). For N=12, 14, P* is likely >1000 (search only, not exhaustive). The threshold N−2 covers become trivial for small N as capacity n≈p/2 is easily met by N−2 speeds covering p/N each.

Predictions:

P*(22): Point 760. Range 740–790. Confidence 75%.
P*(24): Point 880. Range 850–920. Confidence 70%. Scoring Note: These assume the N² scaling continues and the "outlier" boost (like 457) persists sporadically.

N=20 Survivors: The gap at 641, 653 followed by 661 indicates a scattered survivor regime, not a hard cliff. The arithmetic driver is p ≡ 1 (mod N) (or p ≡ 1 (mod N/2)), which allows the "magnifier" u ≈ N/2 to map a consecutive block of speeds to 1,…,N/2, creating a dense local cover that survives longer than random sets. Least-sure step: Assuming the N² coefficient A is constant; it might increase slightly for larger N if the "block" mechanism becomes more efficient relative to the total space.

--- end verbatim ---
END LETTER
