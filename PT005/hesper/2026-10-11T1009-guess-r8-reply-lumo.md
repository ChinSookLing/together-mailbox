BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 10:09 +08
RE: 猜公式 Round 8 (packet 1351cbb), send text r8_send_full.txt or r8_send_short.txt
SEAT: lumo
MODEL: Lumo 2.0 Lite Fast (short version)
CHAT: https://lumo.proton.me/u/19/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
Formula: log(covers) ≈ A − B·p − C·s. Fit: A ≈ 9.5, B ≈ 0.008, C ≈ 0.6. Accuracy: Correctly predicts 31/33 calls (misses 457's outlier survival and possibly 373). The linear decay in p dominates; s acts as a penalty shift.

Drop Mechanism: The count drops by a constant factor because the "alignment tolerance" for 14 speeds to cover n cells shrinks exponentially as p grows. Each speed covers a fixed fraction of the circle, but the number of ways to arrange 14 speeds to hit every cell decreases as the grid (p) refines. The term s = n - 8H represents the excess capacity margin; larger s means the 14 speeds are closer to the theoretical minimum capacity (14H < n), making successful configurations rarer and causing the "zero wall" to hit earlier for high s.

Predictions (503–599): All 0 except 521 (1–5), 569 (1–5), 577 (1–5), 593 (1–5). Overall Confidence: 80%. (High risk of false negatives for the p ≡ 1, 9 (mod 16) cases if outliers like 457 persist).

Largest p for N:
• N=17: Likely p ≈ 600 (marginally higher than N=16 due to looser constraint).
• N=18: Likely p ≈ 700.
• N=20: Likely p ≈ 900. Trend: Max p scales roughly with N^2 or N^2.5. Least-sure step: Extrapolating the "outlier" behavior (like 457) to higher N; the structural reason for 457's survival might not repeat for N=17.

--- end verbatim ---
END LETTER
