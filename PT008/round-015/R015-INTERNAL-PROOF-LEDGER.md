# PT-008 R015 · INTERNAL PROOF LEDGER (courier record of chair ruling 2026-10-19 14:48 +08)
Chair verdict: R015 PARTIAL · TWO INTERNALLY CERTIFIED RESULTS · FIVE NEW PROOF CANDIDATES UNDER REVIEW. No wall publication.
Ruling verbatim: round-015/chair/2026-10-19T1448-Tuzi-paste-R015-ruling-and-R016-VERBATIM.txt

## Internally PROVED (strictly within original hypotheses)
| Result | PROOF VALIDITY | NEW COVERAGE |
|---|---|---|
| Qwen P1: 0<a<b<c<d, 5c/2−a ≤ d ≤ 9a ⇒ t=2/(a+d) | VERIFIED (Hesper courier check; DeepSeek R015 4/4) | NOT ESTABLISHED (interior inside R013/TN/LN; only boundary points new) |
| Qwen B1 selector: c<4a, d ≥ D1, (d ≤ 9a or d ≥ D2) ⇒ WL or 2/(a+d); c ≤ 36a/11 ⇒ all d ≥ D1 | VERIFIED (same) | NOT ESTABLISHED (open band D1<d<D2 ⊂ R013 for x0<c/a≤36/11; only d=D1 outside R013 strict region) |

## R014 coverage erratum (accepted by chair)
Hesper's R014 claim (check 9cdc06a, letter 524f2a3) that β1=(10,20,31,68), β2=(11,20,36,80) lie outside certified rules is WITHDRAWN: both are inside R013 (67.5<68<90; 79<80<99). Found by DeepSeek R015 4/4; confirmed chk_deepseek_r015.py (50,000 band points, 0 outside R013).

## PROOF CANDIDATES (independent review assigned in R016)
| Claim | Author | R016 reviewer |
|---|---|---|
| LE, LE-1 | Opus | DeepSeek |
| TE-AL, TE-AU (exact product domains) | Opus | Qwen |
| a-never-active obstruction (some u/a ∈ 5ℤ) | Opus | Argon |
| Q-B2 (b+c, τ=2) | Qwen | Opus |

## Accepted exact checks (Argon R015 3/4)
- A success time need not be a local maximum of g: (1,2,3,27/4), t=8/31, distances 8/31,15/31,7/31,8/31, c alone active and falling; (1,3/2,2,25/4), t=1/5, g rising. Scope: refutes "success ⇒ local max" only.
- Fastest runner need not be active: (1,2,3,d), 5<d<7, global max g=1/4 at t=1/4 with d inactive. Scope: this family only.
- C.3 (pair-sum menus with τ ≤ τmax fail once b > (5τmax−1)a): CHECKED; scope pair-sum anchors with bounded τ only — not all finite menus (R014 "every finite menu has a gap" stays UNFINISHED).
- DeepSeek one-sided window criterion (right window iff no active constraint at upper edge, etc.): accepted as local geometry; constructs nothing by itself.

## Witness status
V1: SLN1 (PROVED). V2: TE-AU t=4/5, Q-B2 t=2/5 (candidates). V3: TE-AL t=1/5, FNW (candidates). V4=(1,30,60,80): t=2/9 succeeds (CHECKED), component [11/50,89/400]; no deterministic rule yet — R016 priority.

## Standing
Unrestricted F5 UNFINISHED. Before any wall file for a new theorem: obtain full proof and review originals (not summaries).
