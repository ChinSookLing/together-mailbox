# PT005 LEDGER · 16 runners · status of results

Kept by: Opus (chair) · started 2026-10-04 18:49 +08 · Each status change needs Tuzi's approval (time given).
Vocabulary: PROVED-LEAN · REPRODUCED · CHAIR-CHECKED · REFUTED · EXPLORATORY. A status applies only to its SCOPE.

---

## L1 · Shape lemma, parts A, B, C (Lean)
STATUS = PROVED-LEAN · approved by Tuzi 2026-10-04 16:35 +08 (wall line 45)
SCOPE  = the items A1–A5, B1–B6 and part C as stated in Fable-A test 2 (PT005/fable-A/test2/PT005.lean,
         sha256 d5c5d22e77311b74e753a9f3c54dcdfede26d4c68ff5a8773a045c8e77be7505).
OPEN   = rest of the shape lemma R_15 < 1/2 (Fable-A test 3, packet dad605e).

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
STATUS = EXPLORATORY (cost heuristic; not part of any proof)
DATA   = author's K = 14 cost table (12 primes): adding the rounding loss cuts the fit error from 0.33 to 0.11;
         k-factor 3.65 at 239 (full), about 7.9 at 263 (16-job samples), probably > 10 at 307 (incomplete).
TEST   = K = 15 sample at p = 367 (loss 0.875) against 307 (loss 0.125). Pending.
