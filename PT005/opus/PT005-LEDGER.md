# PT005 LEDGER · 16 runners · status of results

Kept by: Opus (chair) · started 2026-10-04 18:49 +08 · Each status change needs Tuzi's approval (time given).
Updated: 2026-10-04 19:50 +08 (L1 extended, L1a and L6 added, L5 superseded; approved by Tuzi 19:49).
Updated: 2026-10-05 09:09 +08 (L6 pending line updated; L7, L8, L9 added; approved by Tuzi 2026-10-05 09:08).
Updated: 2026-10-05 11:18 +08 (L7 CHAIR-CHECKED -> HAND-CHECKED; approved by Tuzi 2026-10-05 11:08, wall line 86).
Updated: 2026-10-05 18:12 +08 (L10 added; approved by Tuzi 2026-10-05 18:10).
Updated: 2026-10-07 21:12 +08 (L12, L13 added; approved by Tuzi 2026-10-07 21:12. L11 is reserved for p = 401, deferred by Tuzi 2026-10-06 16:24).
Updated: 2026-10-08 12:59 +08 (L14 added; approved by Tuzi 2026-10-08 12:55, carried by Hesper be482bb. Total of gate logs: 27.07 of 481.07).
Updated: 2026-10-09 10:44 +08 (L15, L16 added; approved by Tuzi in chat 2026-10-09 10:44, chair note 45. Gate total unchanged: 27.07 of 481.07).
Updated: 2026-10-11 18:35 +0800 (L17 added; approved by Tuzi in chat 2026-10-11 18:34, chair note 69. Gate total unchanged: 27.07 of 481.07).
Updated: 2026-10-11 20:30 +0800 (L18 added; approved by Tuzi in chat 2026-10-11 20:27, chair notes 70-71. Gate total unchanged: 27.07 of 481.07).
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

## L14 · Prime gate p = 241 (K = 15, 16 runners), level 16, three parts
STATUS = REPRODUCED · approved by Tuzi 2026-10-08 12:55 +08 (chair note 39; Hesper be482bb)
SCOPE  = same three-part split as L10 (p = 241 has no cover on ≤ 12 classes):
         (a) 172 jobs, 204,806,388 rows, 0 alive at level 16;
         (b) 344,280 covers. On the office route, 13,307 rows are PERSISTENT, each containing a covering 13-class subset
             (chair checked every row); the other rows die at level 4 (2,329,120) or level 8 (591), item by item equal
             to the chair's route (chair notes 35, 38);
         (c) 936 canonical cores, 6,795,360 rows; every improper lift is removed at level 4 or 8 by the early check,
             which is L7 at level 16 with D = 4 or 8 (chair note 38 section 2; DeepSeek 1 YES, 2 YES, 3 YES,
             PT005/hesper/2026-10-07T2118); 0 unhandled.
         Two machines: chair (chair notes 35, 36) and Tuzi's office PC (Hesper, PT005/hesper/officepc-p241ab and
         officepc-p241c); chair re-compared (a) job by job on 6 fields (0 differences), (b) as above, (c) with
         compare_cores.py v2 (MATCH, 936 = 936). Same code on both machines.
USES   = L7 (HAND-CHECKED), in its stated level-16 scope; read records as for L12 plus shift_rows_early.cpp 7487a9c5…
         (DeepSeek Q1 YES, 2026-10-07T1410).
OPEN DEPENDENCIES = as L10. NOT a certificate.

## L15 · The cover number is at most 15: γ(p) ≤ 15 for every prime p > 16
STATUS = HAND-CHECKED · approved by Tuzi 2026-10-09 10:44 +08 (chair notes 42, 45)
SCOPE  = Definitions as in the 猜公式 packets: n = (p−1)/2; speed v is too near at cell t iff 16·min(vt mod p, p − vt mod p) < p;
         γ(p) = the smallest number of speeds that are too near at every cell t = 1..n.
         Claim: the speeds {1, …, 15} are always a cover. Proof: among the 16 points 0, x, …, 15x (x = t/p) on the circle,
         two are within 1/16; their difference is jx with 1 ≤ j ≤ 15; equality would need 16jt = (16k ± 1)p, even = odd.
PROOF BY = GPT, Gemini, Kimi, independently (Round 1 replies 089b06c, fc91f65, adad61b); chair re-check by hand and by
         program for all 297 primes 17 < p < 2000 (0 exceptions).
USES   = nothing beyond the definitions. NOT about the full LRC; it bounds the size of covers that parts (b)/(c) of a gate use.

## L16 · Draft theorems T1, T2 (conditional on F5)
STATUS = HAND-CHECKED, CONDITIONAL on F5 · approved by Tuzi 2026-10-09 10:44 +08 (chair note 45)
SCOPE  = T1: if p > 56^13 (≈ 5.3 × 10^22) then γ(p) ≥ 14. T2: if p > 120^14 (≈ 1.3 × 10^29) then γ(p) = 15 (with L15).
         Proof (packet aaa37b9): Lemma A (13 distinct speeds ≤ M are not a cover when p ≥ 56M, by the lonely-runner theorem
         for 13 speeds and rounding x to t/p) + Lemma B (Dirichlet simultaneous approximation scales any 13 speeds to ≤ p/N,
         N = ⌊(p−1)^{1/13}⌋) + scaling invariance. T2: same with 14 speeds, margin 1/15 − 1/16 = 1/240.
F5     = the Lonely Runner Conjecture for 13 and for 14 speeds (14 and 15 runners), claimed proved by computer in
         arXiv:2609.02604 (in the paper's notation LRC(13) and LRC(14): m speeds, threshold 1/(m+1)). Not independently checked.
READERS = GPT, Grok, Gemini, Astra, Kimi, Qwen, GLM, Lumo: all YES on Lemma A, Lemma B, T1, T2 (Round 2, chair note 45).
USES   = none in any gate yet: the thresholds are astronomically larger than the primes we gate. Gate total unchanged.
NOT    = a certificate; NOT an improvement of the threshold (Round 2 found none).

## L17 · Uniform continuous floor and linear deficit (conditional on F5)
STATUS = HAND-CHECKED, CONDITIONAL on F5 · approved by Tuzi 2026-10-11 18:34 +08 (chair note 69)
SCOPE  = (i) For every set K of 14 distinct positive integers, m(K) ≥ 240^(−14), where m(K) is the Lebesgue measure of
         {x ∈ [0,1) : ‖kx‖ ≥ 1/16 for all k ∈ K}.
         Proof: F5 gives t0 with ‖k t0‖ ≥ 1/15 for all k; cut the torus image of t ↦ (k t) into 240^14 cubes; some cube has a
         preimage A of measure ≥ 240^(−14); for t ∈ A, t0 + (t − t1) is safe since 1/15 − 1/240 = 1/16; translation keeps measure.
         (ii) With Dirichlet simultaneous approximation (Q = ⌊(p−1)^{1/14}⌋) and ±1 grid error per safe interval:
         for every prime p ≥ (28·240^14)^14 + 1 and every 14-set S, U(S) ≥ p/(4·240^14); hence D(p) ≥ p/(4·240^14) and
         δ(p) = D(p)/E(p) ≥ 1/(2·240^14).
PROOF BY = GPT (Round 15, 73f831c) and Astra (Round 15, 6e1b0a0), independently.
READERS = Hesper (step-by-step), chair (note 69). F5 as in L16 (here LRC(14): 14 speeds, threshold 1/15).
MEANING = the first rigorous LINEAR lower bound on the deficit; it settles the Round 13 target "uniform δ > 0" qualitatively.
NOT    = useful numerically: 240^(−14) ≈ 4.75 × 10^(−34) against the observed minimum 97/6864 ≈ 0.0141 (conjecture C-floor,
         chair note 68); threshold ≈ 10^487. For γ(p) = 15 alone, L16 T2 (p > 120^14) is far stronger.
USES   = none in any gate. Gate total unchanged.

## L18 · One-large-speed inequality, and the C-floor when at most one speed exceeds 30 (UNCONDITIONAL)
STATUS = (i) HAND-CHECKED · (ii) CHAIR-CHECKED for the class "≤ 1 speed > 30"; the sub-class "≤ 1 speed > 24" also
         computed by Kimi's separate engine (REPRODUCED for that sub-class) · approved by Tuzi 2026-10-11 20:27 +08
         (chair notes 70, 71)
SCOPE  = m(K) = Lebesgue measure of {x ∈ [0,1) : ‖kx‖ ≥ 1/16 for all k ∈ K}; c(K) = number of its intervals.
         (i) For any finite set K of positive integers and any integer v ≥ 1:
             m(K ∪ {v}) ≥ (7/8)·m(K) − 7·c(K)/(64v); moreover the loss on each safe interval of length ℓ is at most
             min(ℓ, ℓ/8 + 7/(64v)).
             Proof: f = 1{‖vx‖ < 1/16} − 1/8 has period 1/v and mean 0; its primitive oscillates by exactly
             (1/(8v))·(7/8) = 7/(64v); so on any interval the bad measure is at most ℓ/8 + 7/(64v).
         (ii) Every 14-set K with at most one element > 30 satisfies m(K) ≥ 97/6864, with equality in that class only at
             K* = {1..15}∖{6} and 2K*. Computed exactly (integer unit 1/(16·lcm(1..30)), 128-bit losses): all
             C(30,14) = 145,422,675 subsets of {1..30}, and all C(30,13) = 119,759,850 subsets of {1..30} with any v ≥ 31
             (27,170,182 exact v-checks below the point where (i) certifies the tail; 0 failures).
             Worst one-large-speed case: K*∖{14} ∪ {56}, m = 14867/960960 (found independently by GPT, Kimi, chair).
PROOF BY = (i) GPT and Astra (Round 16, ab5b271, b0d84d9), independently; GLM and Kimi proved the weaker c(K)/(4v) form.
         (ii) chair engine PT005/opus/guess_r16/oneLarge.c (sha256 prefix d9c7897727721cd3), outputs out24.txt, out30.txt;
         301 random cases + the worst case matched an independent Fraction computation (spot.py, spot30.py).
READERS = Hesper re-computed the R16 rational values (8919f67); chair (notes 70, 71).
MEANING = the conjecture C-floor (m(K) ≥ 97/6864 for every 14-set) is now open ONLY for 14-sets with ≥ 2 speeds > 30.
         Does not depend on F5.
NOT    = the full C-floor; NOT an improvement of the threshold P₀ (conditional on full C-floor, GPT's 991^14 + 1 ≈ 8.8 × 10^41).
         Kimi's discrete lemma L-D1 (log² p error for any speed) is FALSE as stated (chair note 70) and is not part of L18.
USES   = none in any gate. Gate total unchanged.

## L19 · The deleted baseline in closed form: why 97/6864, and why 6
STATUS = PAPER + BLIND SECOND READER + CHAIR-COMPUTED for n ≤ 20 · approved by Tuzi 2026-10-12 16:19 +08 (chair notes 73, 74)
SCOPE  = For n ≥ 5 and 2 ≤ r with 2r ≤ n−1, let K = [n−1]∖{r}, s = n−r, u_p = p⁻¹ mod r,
         F(x) = max{i ≤ n−1 : i ≠ r, i ≡ x mod r}. The safe set {x : ‖kx‖ > 1/n for all k ∈ K} is the disjoint union over
         reduced p/r of (p/r − s/(rn·F(u_p)), p/r − 1/(2rn)) and (p/r + 1/(2rn), p/r + s/(rn·F(r−u_p))); its measure is
         M(n,r) = (1/(rn))·(2s·Σ_{u unit mod r} 1/F(u) − φ(r)).
         For n = 16, r = 6: four intervals (33/208, 31/192), (11/64, 31/176), (145/176, 53/64), (161/192, 175/208), and
         m(K*) = 97/6864 = (1/96)·(20·(1/13 + 1/11) − 2). Over r = 2..15 the minimum of m([15]∖{r}) is at r = 6.
PROOF BY = structure: Y. Zhang, arXiv:2608.13599 v2, Theorem 1.4 / Lemma 2.4 (preprint, unrefereed); found by Kimi (R17);
         measure summation: Kimi (R17).
READERS = Astra, blind (new chat, packet 6471e3f, reply a09c1c3): read the paper and reproduced 97/6864 by own steps;
         Hesper re-checked the arithmetic (a558201); chair exact check PT005/opus/guess_r17/zhang_ii.py
         (sha256 prefix 2d202e0f91ef5e9f): component formula and M(n,r) match the exact safe set in all 72 cases
         n = 5..20, 2r ≤ n−1, 0 mismatches. Case (ii) endpoints as captured from Astra had a typo (F for 1/F, 1/(2r));
         the corrected form above is the one that matches (note 74).
MEANING = the conjectured C-floor value 97/6864 has a closed form and a structural reason: the safe set of K* sits next to
         the fractions p/6 (Zhang's "components near p/r").
NOT    = the C-floor itself. Still UNFINISHED: (a) a reduction "every 14-set is at least as bad as some deleted baseline";
         (b) the class of 14-sets with ≥ 2 speeds > 30 (L18). For n > 20 it rests on Zhang's proof alone. Not a threshold gain.
USES   = none in any gate. Gate total unchanged.
