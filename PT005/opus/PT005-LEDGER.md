# PT005 LEDGER · 16 runners · status of results

Kept by: Opus (chair) · started 2026-10-04 18:49 +08 · Each status change needs Tuzi's approval (time given).
Updated: 2026-10-04 19:50 +08 (L1 extended, L1a and L6 added, L5 superseded; approved by Tuzi 19:49).
Updated: 2026-10-05 09:09 +08 (L6 pending line updated; L7, L8, L9 added; approved by Tuzi 2026-10-05 09:08).
Updated: 2026-10-05 11:18 +08 (L7 CHAIR-CHECKED -> HAND-CHECKED; approved by Tuzi 2026-10-05 11:08, wall line 86).
Updated: 2026-10-05 18:12 +08 (L10 added; approved by Tuzi 2026-10-05 18:10).
Updated: 2026-10-07 21:12 +08 (L12, L13 added; approved by Tuzi 2026-10-07 21:12. L11 is reserved for p = 401, deferred by Tuzi 2026-10-06 16:24).
Vocabulary: PROVED-LEAN · REPRODUCED · CHAIR-CHECKED · HAND-CHECKED · REFUTED · SUPPORTED-MODEL · EXPLORATORY.
  HAND-CHECKED = checked by hand by at least two readers who are not its author; no machine proof, no independent
  computation. SUPPORTED-MODEL = an empirical model whose predictions were stated before the test and then met;
  not a theorem. A status applies only to its SCOPE.

---

## L1 · Shape lemma for n = 15: H > 900 (Lean)
STATUS = PROVED-LEAN · parts A, B, C approved by Tuzi 2026-10-04 16:35 +08 (wall line 45);
         extended to the full statement, approved by Tuzi 2026-10-04 19:49 +08
SCOPE  = theorem `shape_lemma`: for u : Fin 15 → ℝ with every u_i ∈ (0,1] and some u_i = 1,
         H u = (Σ w(u_i))·(Π a(u_i)) > 900, with q x = 1 + 2x − x², a x = q x / x^(2/15), w x = x²/q x.
         Files: PT005/fable-A/test2/PT005.lean (sha256 d5c5d22e77311b74e753a9f3c54dcdfede26d4c68ff5a8773a045c8e77be7505)
         and PT005/fable-A/test3/PT005Shape.lean (sha256 9713a45e28cb67c8cbbcbc991bcfc43b87ba7257ac094b2921526a2d4fae2f0a).
         Axioms: propext, Classical.choice, Quot.sound only. Read by the chair (note 18, R12); re-run by Puck
         (stdout identical, 5f7cc89). D4 uses Fable-A's own reduction, not the author's β-analysis; same statement.

## L1a · Link from H > 900 to R_15 < 1/2
STATUS = HAND-CHECKED · approved by Tuzi 2026-10-04 19:49 +08
SCOPE  = the author's identity R_n(x)^2 = n^2 / H(u), u_i = x_i / max_j x_j (Allikvere v2, proof of lemma lem:shape),
         at n = 15: R_15 < 1/2 ⇔ H > 900. Checked by the chair (chair note 3) and DeepSeek (turn 11). Not in Lean.
OPEN   = the step from R_15 < 1/2 to the product bound (Theorem 3.8 flag bound with Astra's dual step) is also
         not in Lean.

## L2 · Prime gate p = 239 (K = 15, 16 runners)
STATUS = REPRODUCED · approved by Tuzi 2026-10-04 18:49 +08
SCOPE  = p = 239 gate computation only.
         All 149 irredundant jobs and 14 reducible roots reproduced by two seats (Opus 0cefce4; Fable-B test 4,
         b485460) on different CPUs and engine code paths (VEC=0 / VEC=1; plus a clang, non-AVX-512 sample of
         34 jobs, byte-identical rows). Rows and nodes equal job by job; 0 rows alive at level 16 in both branches.
         Cascade independently reimplemented (Fable-B oracle): all 35,819 level-2 survivors and 8,000 sampled
         rows match; the remaining level-2 deaths are checked by sample only.
         Cascade patch (line 71 static_assert) affects printed labels and selftest only: confirmed by two readers.
         Completeness lemmas carried to K = 15 with quota q_15 (Astra turn 14); the engine uses q_15 (chair note 15).
OPEN DEPENDENCIES =
  1. an independent generator compared row by row with the author's 9,552,452-row level-one input;
  2. independent verification of the 15-runner prerequisite LRC(14) (Allikvere v2; not yet independently
     re-implemented, as the paper itself says).
NOT a certificate. NOT an independent reproduction of the full theorem chain.

## L3 · Kimi turn 15, Lemma A (level-2 forced bit is unique for a covering speed)
STATUS = CHAIR-CHECKED (one check: all v and all covered times at p = 239, 0 violations; chair note 16)
NOTE   = the bit formula floor(a·v/p) mod 2 in Kimi's text is wrong in 3,332 of 6,664 cases; the correct bit is
         floor(a·v/p)+1 when the remainder is below p/2, floor(a·v/p) otherwise (mod 2).

## L4 · Kimi turn 15, Lemma B (conflicting private times ⇒ dies at level 2)
STATUS = REFUTED (chair note 16; scouting/LR16/opus/kimi3/)
SCOPE  = as stated, with level-1 privacy: it marks all 569 real level-2 survivors of job (0,1) at p = 239.
         Kimi's own falsifier 2 ("a survivor satisfies the hypothesis") was triggered.
KEPT   = the corrected form (every other speed has 8·d_p(a·v_j) ≥ p) is sound, but caught 0 of 2,000 sampled
         dying rows at p = 239. The subtree prune built on Lemma B falls with it.

## L5 · Cost depends on the rounding loss of (p−1)/(k+1)
STATUS = SUPERSEDED by L6 (19:49).

## L6 · Generation-cost model: log T ≈ A + B·log p + C·x, x = (k·m − n)/n
STATUS = SUPPORTED-MODEL (generation cost only) · approved by Tuzi 2026-10-04 19:49 +08
SCOPE  = cost of the irredundant level-one generation for primes p ≥ 239. m = floor((p−1)/(k+1)), n = (p−1)/2,
         so x is set mainly by r = (p−1) mod (k+1): large r is cheap (for k = 15: p ≡ 15, 13, 11, 9 mod 16).
         Proposed by the chair (note 16), explained and turned into tests by Qwen (turn 16), tests run by the chair
         (note 19, scouting/LR16/opus/qwen2/):
           A. leave-one-out on the author's 12 K = 14 primes: error 0.150 (0.457 without x); C between 12.6 and 15.2.
           B. K = 15, T(241)/T(239): predicted 3–6, measured 3.71.
           C. K = 15, T(251)/T(241): predicted about 0.48, measured 0.555 (the larger prime is cheaper).
         K = 15 fit, fixed B = 6, C = 13: A ≈ −34.17; residuals within ±0.15 at 239, 241, 251, 263.
NOT    = a theorem; NOT a total-cost model. It leaves out the lifting cost, which dominates at small primes
         (author: p = 131 generation 32 s, lifting and level 15 about 328,000 s). Some primes may fail the gate.
PENDING = Fable-B test 5 (K = 15 at 307 and 367, raw numbers only; the old SURVIVES / REFUTED rule in the packet
         is withdrawn). Model prediction: T(367)/T(307) ≈ 1.35 (p^6 alone: 2.9).
UPDATE  = test 5 PARTIAL (chair note 21): K = 15 at 367, 11 of 12 jobs, about 357 s per job; model predicted about
         318 s on the chair's machine, about 7% low after machine adjustment (4th prospective hit). 307 not measured.

## L7 · Composite-denominator shift lemma for k = 15 (Astra turn 17)
STATUS = HAND-CHECKED · approved by Tuzi 2026-10-05 11:08 +08 (wall line 86); was CHAIR-CHECKED from 09:08
SCOPE  = 15 non-zero integer speeds u_1..u_15 (stated explicitly, as DeepSeek asked). For an integer D ≥ 2 with
         E = {i : D ∤ u_i}, |E| ≥ 2, g_i = gcd(D, u_i), D_i = D/g_i: if Σ_{i∈E} g_i·⌈D_i/8⌉ < D and LRC(m) holds for
         m ≤ 13, some rational t has ||t u_i|| ≥ 1/16 for all i. With D = 8: a + 2b + 4c < 8 (a = #odd,
         b = #(2 mod 4), c = #(4 mod 8)).
USE    = third alternative of the author's Lemma 2.2(ii) at binary levels L = 16 or 32, with D EVEN and D | L·p
         (stated explicitly, as DeepSeek asked). e ≥ 2 holds for every improper lift: an improper lift at a binary
         level has at least two odd coordinates (otherwise the gcd condition makes it proper), and odd coordinates are
         not divisible by an even D (Astra README line 45; chair note 25).
CHECKED = chair (chair note 24, line by line; chair note 25, parity step) and DeepSeek (turns 19 and 20, wall lines
         79–80 and 83–84). Mailbox PT005/astra/turn17/.

## L8 · Sharper shape factor R_15 < 61/125; bound B = 494.558 (GPT turn 18)
STATUS = CHAIR-CHECKED · approved by Tuzi 2026-10-05 09:08 +08
SCOPE  = H > 3515625/3721 (≈ 944.8065) for n = 15, hence R_15 < 61/125 and ΔB = 15·log(125/122) = 0.3644;
         B goes from 494.922 to 494.558; the gates must supply Σ log p > 481.07.
         The exact rational test was re-run by the chair (PASS; scouting/LR16/opus/turn17-18/checks.out).
         The minimiser reduction it uses is the author's; for n = 15 a different route is in Lean at threshold 900
         (L1, `H_gt_at_min`); a Lean version at threshold 944.8065 would need only the last step changed. Not done.

## L9 · p = 131, K = 15: sampled persistent rows are handled by L7 (scouting)
STATUS = TEST (Opus) · approved for recording by Tuzi 2026-10-05 09:08 +08
SCOPE  = 330 persistent rows from a biased sample of 20,000 of the 16,059,579 general-variant covers: 2,644,800
         improper lifts at level 16, per-row counts equal to the author's cascade; all pass the L7 criterion with
         D ∈ {2, 4, 8, 16} (Astra's code, read then run by the chair; chair note 24).
         Irredundant branch at p = 131: 61,061,431 rows, 0 alive at level 16 (chair note 20).
OPEN   = the full reducible branch at p = 131 (about 1.04 billion extension rows) and every other small prime.
         NOT a gate result.

## L10 · Prime gate p = 223 (K = 15, 16 runners), level 16, three parts
STATUS = REPRODUCED · approved by Tuzi 2026-10-05 18:10 +08 (chair note 31)
SCOPE  = p = 223 gate at binary level 16, split into three parts that together contain every row (p = 223 has no
         cover on ≤ 12 classes: `bgk15 223 km1low 12` gives 0):
         (a) irredundant branch: 132 jobs, 15,177,679 rows, 0 alive at level 16;
         (b) reducible branch (km1root covers, 33,694, each extended by one class, 3,740,034 rows): 222,478 die at
             level 4, 34 at level 8, 513 PERSISTENT, and each of the 513 contains a covering 13-class subset;
         (c) every row containing one of the 65 canonical 13-class cores: 404,040 rows, 32,240,000 improper lifts
             at level 16, all handled by L7 (D ∈ {2, 4, 8, 16}); 0 unhandled.
         Two machines: chair (chair notes 29–30) and Tuzi's office PC (wall 119–120; Puck 404da8e, 4beb600);
         chair re-compared (c) with compare_cores.py v2 (MATCH) and (a) job by job on 6 fields (0 differences);
         (b) counts equal and the 513 persistent rows equal as a set (Puck's comparison; km1.json sha bdfabad5…).
         Same code on both machines (not an independent re-implementation).
USES   = L7 (HAND-CHECKED); unit-orbit reduction of rows to canonical cores (chair note 29; read by DeepSeek,
         HOLDS, 19ff2fc); code read records: kcascade_run.py and compare_239.py (p = 239 kit), run_cores.py v2,
         compare_cores.py v2, shift_rows223.cpp (DeepSeek, wall 111–117).
OPEN DEPENDENCIES = the same two as L2 (independent generator; independent LRC(14)), plus a second reader of the
         completeness of the (a)/(b)/(c) split as stated here.
NOT a certificate. The forced-family lemma (chair note 30) explains the count 496,000 but is not used by this gate.

## L12 · Prime gate p = 233 (K = 15, 16 runners), level 16, three parts
STATUS = REPRODUCED · approved by Tuzi 2026-10-07 21:12 +08 (chair note 38)
SCOPE  = same three-part split as L10 (p = 233 has no cover on ≤ 12 classes):
         (a) 146 jobs, 49,184,257 rows, 0 alive at level 16;
         (b) 88,134 covers, 10,223,544 extension rows: 489,626 die at level 4, 69 at level 8, 1,316 PERSISTENT, each
             containing a covering 13-class subset;
         (c) 117 canonical cores, 793,962 rows, 63,652,160 improper level-16 lifts, all handled by L7; 0 unhandled.
         Two machines: chair (chair note 32) and Tuzi's office PC (Hesper, PT005/hesper/officepc-p233); chair re-compared
         (c) with compare_cores.py v2 (MATCH), (a) job by job on 6 fields (0 differences), (b) counts equal and the 1,316
         persistent rows equal as a set. Same code on both machines.
USES   = L7 (HAND-CHECKED); unit-orbit reduction (chair note 29, DeepSeek HOLDS); read records as for L10 plus
         run_cores.py v3 and shift_rows.cpp v3 (DeepSeek, b0f5aef).
OPEN DEPENDENCIES = as L10. NOT a certificate.

## L13 · Prime gate p = 191 (K = 15, 16 runners), level 16, three parts
STATUS = REPRODUCED · approved by Tuzi 2026-10-07 21:12 +08 (chair note 38)
SCOPE  = same three-part split as L10 (p = 191 has no cover on ≤ 12 classes):
         (a) 96 jobs, 12,083,620 rows, 0 alive at level 16;
         (b) 42,114 covers, 4,000,830 extension rows: 366,021 die at level 4, 484 at level 8, 2,349 PERSISTENT, each
             containing a covering 13-class subset;
         (c) 260 canonical cores, 1,185,600 rows, 99,751,808 improper level-16 lifts, all handled by L7; 0 unhandled.
         Two machines: chair (chair note 34) and Tuzi's office PC (Hesper, PT005/hesper/officepc-p191); chair re-compared
         as for L12 (all MATCH; 2,349 persistent rows equal as a set). Same code on both machines.
USES   = as L12. OPEN DEPENDENCIES = as L10. NOT a certificate.

