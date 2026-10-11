BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 14:56 +08
RE: 猜公式 Round 12 (packet c9a646a), send text r12_send_full.txt or r12_send_short.txt
SEAT: lumo
MODEL: Lumo 2.0 Fast
CHAT: https://lumo.proton.me/u/11/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
# PT005 Round 12 — Lumo reply capture

- Chat: PT005 · Big Picture
- Chat URL: https://lumo.proton.me/u/23/c/1b04e910-acf8-481d-80b9-8deeab93d8db
- Model/mode: Lumo 2.0 Max / Fast mode
- Web search: OFF (web-search-toggle checked=false in Tools panel)
- Send time Asia/Singapore +08: ~14:53 on 2026-10-11 (Sunday) — message sent and reply completed in the same minute
- Nudge sent: No (reply completed immediately)
- Reply completed: Yes — full reply captured verbatim from the assistant message; Copy button clicked (showed "Copied to clipboard"), but clipboard read returned empty on the next turn; verbatim text taken from the rendered message via extract_content.

---

## Verbatim reply

Model Computation:
Total sets ≈ (p/2 14)/p ≈ p^13/(14!·2^14). Probability a random set has U = 0 is P(U = 0) ≈ e^−M(p) (Poisson). Expected number of covers E ≈ p^13/C · e^−0.077p. As p → ∞, e^−0.077p dominates p^13, so E → 0. The minimum D(p) behaves like the minimum of N Poisson variables. Since E ≪ 1 for large p, the probability of finding any cover vanishes.

Prediction: D(p) is bounded (likely jumps to ≥1 permanently after a threshold) or grows very slowly (logarithmic) if rare outliers exist, but the probability of D(p) = 0 drops exponentially. It does not grow linearly.

Calculation:
At p = 500, M ≈ 38.5. E ≈ 500^13 · e^−38.5 ≈ 10^35 · 2 · 10^−17 ≈ 2 · 10^18? Wait, M(p) is the mean number of uncovered cells, not the probability of being a cover. Correction: U(S) is sum of indicators. Mean M(p) ≈ 0.077p. Variance ≈ M. We need P(U = 0). For Poisson(λ), P(0) = e^−λ. E[covers] ≈ (n 14)_p · e^−M(p). At p = 500, M ≈ 38.5. e^−38.5 ≈ 1.6 × 10^−17. (250 14) ≈ 10^25. E ≈ 10^25 · 10^−17/500 ≈ 2 × 10^4. Wait, the census shows covers vanish. My Poisson assumption for independent cells is wrong; cells are highly correlated.

Revised Logic: The "effective" number of independent constraints is much lower, or the variance is lower. However, if we trust the data (vanishing at 431+), the extreme value prediction is that D(p) becomes ≥ 1 (no covers) and stays there.

Conclusion: D(p) is bounded (specifically, it hits a floor of 1 or 2 and stays there, never returning to 0).

Theorem Route:
Hardest step: Proving the lower bound D(p) ≥ αp − β rigorously for all sets, not just random ones. Structured sets (like 457) minimize U by creating correlations. Smallest plausible P0: If the Fourier bound error is o(p), then once M(p) exceeds the maximum possible negative resonance from any structured set, D(p) > 0. Given the rapid drop in covers, P0 could be as low as 500–600, far below 120^14.

Predictions (D(p)):
503: 1 (Confidence 85%)
547: 1 (Confidence 80%)
577: 2–3 (Confidence 70%) (Outlier chance)
599: 1 (Confidence 85%)
Note: All predictions assume the "death line" at 431 holds, with only rare p ≡ 1, 9 (mod 16) survivors.
--- end verbatim ---
END LETTER
