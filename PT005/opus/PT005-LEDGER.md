# PT005 LEDGER · 16 runners · status of results

Kept by: Opus (chair) · started 2026-10-04 18:49 +08 · Each status change needs Tuzi's approval (time given).
Updated: 2026-10-04 19:50 +08 (L1 extended, L1a and L6 added, L5 superseded; approved by Tuzi 19:49).
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
