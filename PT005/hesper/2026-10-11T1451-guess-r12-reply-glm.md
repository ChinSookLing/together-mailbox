BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 14:56 +08
RE: 猜公式 Round 12 (packet c9a646a), send text r12_send_full.txt or r12_send_short.txt
SEAT: glm
MODEL: GLM-5.3 Deep Think High
CHAT: https://chat.z.ai/c/a5f7e437-2548-404b-a302-70a5536f7660

--- reply verbatim ---
PT005 Round 12 — GLM-5.3 Deep Think High final reply
================================================================
Site: chat.z.ai
Model: GLM-5.3 (flagship; not GLM-5.3-Flash)
Deep Think level shown: High (dropdown showed High with checkmark; button label "Deep Think High")
Web search: OFF (Advanced Search switch checked=false)
Message entry: paste_text (verbatim, single message), sent via the Send button
Send time: 14:51 Asia/Singapore, 2026-10-11 +08
Chat URL: https://chat.z.ai/c/a5f7e437-2548-404b-a302-70a5536f7660
Chat title after reply: "PT005猜公式分析及预测" (auto-renamed by the site)
Reply completed well under 25 min — no nudge sent.
Reply captured via the response Copy button; "Copying to clipboard was successful!" toast shown.
================================================================
VERBATIM REPLY (from Copy button, copied this turn via writeText):

## 1. Poisson/extreme-value model

**FACT (computed):** M = (p/2)(7/8)^14. ln(7/8) = −0.1335, ×14 = −1.8695, so (7/8)^14 = 0.1542, M = 0.0771p. ln C(n,14) ≈ 14 ln n − ln 14! = 14 ln n − 25.19; dividing by n for equivalent classes: ln N ≈ 13 ln p − 34.2.

**PROOF:** D=0 expected iff ln N > M. Solve 13 ln p − 34.2 = 0.0771p: at p=630, LHS−M = +1.02; p=645, +0.17; p=648, 49.96 vs 49.96. **Crossover ≈ p = 648.** Beyond it, min of N Poisson(M) sits at ≈ M − ln N = **0.077p − 13 ln p + 34: linear in p**, slope 0.077.

**IDEA:** Model says D=0 through 648, but D≥1 already at 431 — correlations shrink the effective pool, so real D grows linearly but earlier.

## 2. Theorem route

**IDEA — hardest step:** a *uniform* deterministic bound U(S) ≥ αp − o(p) for **every** 14-set S. Slack is only structural (each set has density ≈1/8, so 14 give mass 1.75 on a half-interval), so any o(p) Fourier error must be controlled uniformly, and with ~10^22 candidate sets union bounds are dead.

**FACT (computed):** C(250,14) ≈ e^{77.30−25.19} = e^{52.11} ≈ 4×10^22. 120^14 = (3.583×10^14)^2 ≈ 1.3×10^29. C(n,14) = 120^14 when ln n = 4.787 + 25.19/14 = 6.586, n ≈ 726, i.e. **p ≈ 1453**. So brute force "costs 120^14" only near p≈1450; plausible P₀ must be far below: **P₀ ≈ 550 ± 100** (between the observed D≥1 wall at 431 and the naive crossover 648).

## 3. Predictions (IDEA, UNFINISHED as facts)

M computed: 503→38.8, 547→42.2, 577→44.5, 599→46.2.
- 503: **D=1**, confidence ~60%
- 547: **D=1**, ~55%
- 577: **2–3**, ~40%
- 599: **2–3**, ~40%

Basis: D=1 at 383/397, D≥1 throughout 431–499, M rising ⇒ slow drift from 1 toward 2–3.
--- end verbatim ---
END LETTER
