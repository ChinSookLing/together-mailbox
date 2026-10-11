BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 20:16 +08
RE: 猜公式 Round 16 (packet d712a00), send text r16_send_full.txt or r16_send_short.txt
SEAT: kimi
MODEL: Kimi K3 Thinking High
CHAT: https://www.kimi.ai/chat/1a12a239-cbb2-8558-8000-09ceeb0ce4d1

--- reply verbatim ---
[Pasted by Tuzi in Hark chat 2026-10-11 20:16 +08 from Kimi chat https://www.kimi.ai/chat/1a12a239-cbb2-8558-8000-09ceeb0ce4d1]

Kimi : All computations complete. Here is the Round 16 reply.

---

# ANSWER BLOCK

**Q1 (FACT).** The packet's crude bound fails nearly everywhere: even the best 13-set {1..5,7..13,15} (min m = 3071/102960 = 0.0298271 over all 2,496,144 sets with max ≤ 24) gives F₁(31) = −0.0545 < 0; worst is −0.2576. "Case 4" (7m/8 ≤ 97/6864) is **empty**. But the repaired pipeline (per-interval bound + certified grid + exact fallback) closes **every** 13-set with max ≤ 24 for **all** v ≥ 25: 1,282,919 sets by the 1/8-cap, 243,747 at v = 31 by the sharper bound, 969,478 via 18,526,183 grid checks (G = 2¹⁴) with exactly **one** grid failure ({1..5,7..13,15}, v = 56), cleared exactly: m = 14867/960960 = 0.015471 ≥ 97/6864. Remaining for max ≤ 30: 13-sets with 25 ≤ max ≤ 30 (117,263,706 sets, ~1 core-hour, not run).

**Q2.** Multi-speed induction needs super-increasing v: 812 → 7·10⁴ → 8·10⁶ → 10⁹ → 2·10¹¹, and breaks at step 5 (m < floor). Component growth (c: 12→16→20→26) is the killer.

**Q3 (FACT).** C-floor now verified for **all 14-sets except those with ≥ 2 speeds ≥ 25**: all C(24,14) = 1,961,256 small sets pass (min = 97/6864 exactly at K*). Largest explicit uniform c: still 240⁻¹⁴.

**Q4.** New discrete one-large-speed lemma proved (ET discrepancy), but Dirichlet replacement only works one speed at a time. P₀: unconditional ≈ 10^486.8; conditional on C-floor ≈ 10^54.6. P₀ = 10⁴ needs c₀ ≥ 58 — impossible by scaling alone.

**Q5.** Distance to P₀ ≈ 10⁴ = exactly the component-count conjecture. Census-ready.

---

# WORK

## Q1 — One-large-speed case for 13-sets

**PROOF (per-interval sharpening).** Adding speed v removes, from a safe interval of length L, at most min(L, L/8 + 1/(4v)): the v unsafe arcs have total width 1/8, and at most Lv + 2 of them meet the interval, each contributing ≤ 1/(8v). Hence m(K∪{v}) ≥ m(K) − Σᵢ min(Lᵢ, Lᵢ/8 + 1/(4v)), increasing in v, limit 7m/8. The packet's c(K)/(4v) form follows from #intervals = c.

**FACT.** Enumeration of all C(24,13) = 2,496,144 sets (float engine validated 0/300 vs exact Fraction engine):

```python
for K in combinations(range(1,25), 13):
    m, c, gaps = mc_fast(K)
    if m*7/8 <= FL + 1e-9: case4.append(K)      # -> EMPTY
    if m < CAP - 1e-9: cand24.append((K, m, tuple(gaps)))
# min m = 0.0298271173271 at (1,2,3,4,5,7,8,9,10,11,12,13,15)
# exact: mc_exact -> 3071/102960
```

**FACT.** Crude bound failures: F₁(v=31) = 7m/8 − c/124 < floor for essentially every candidate; worst F₁ = −0.257598 at (1,2,8,9,10,12,14,15,16,17,18,19,20) (m = 168737/1302336, c = 46).

**FACT (pipeline).** Direct 1/8-cap clears m ≥ floor + 1/8: 2,496,144 − 1,213,225 = **1,282,919** sets. For the rest, vectorized bisection for V₂ (smallest V with the sharper bound ≥ floor for all v ≥ V₂): 243,747 have V₂ = 31; 969,478 have V₂ > 31, max V₂ = 275, Σ(V₂−30) = 18,526,183 grid checks.

```python
G = 1<<14; THR = ceil(97/6864 * G) = 232        # grid-safe ⊆ true-safe (arcs expanded 1 cell)
for K, V2 in todo:                               # 969,478 sets
    SM = FULL & ~OR(MASKS14[k] for k in K)
    for v in range(31, V2):
        if (SM & ~MASKS14[v]).bit_count() < THR: fails.append((K, v))
# -> fails = [((1,2,3,4,5,7,8,9,10,11,12,13,15), 56)]  exactly one
```

**FACT.** The single grid failure clears exactly: m({1..5,7..13,15} ∪ {56}) = 14867/960960 = 0.0154710 ≥ 97/6864 (margin 0.00134).

**FACT.** v ∈ {25,…,30} closed separately: sharper-bound screen (≈10⁶ bound-failures per v), then exact float check of every failure with 1e-9 near-floor catch → **0 near/below floor for all six v**.

**Conclusion (FACT).** Every 14-set with **at most one speed > 24** satisfies m ≥ 97/6864. Cases remaining toward the packet's max ≤ 30: 13-sets with 25 ≤ max ≤ 30, count C(30,13) − C(24,13) = 119,759,850 − 2,496,144 = **117,263,706** (≈ 1 core-hour at the measured 34k sets/s — runnable, not run tonight).

## Q2 — Induction over several large speeds

**IDEA (formal).** Iterating: m(K∪{v₁..v_j}) ≥ (7/8)^j m(K) − Σᵢ (7/8)^{j−i} c_{i−1}/(4v_i), with c_i ≤ c_{i−1} + v_i (each new arc splits ≤ 1 component).

**FACT (crude bound vacuous from step 1).** {1..13}: m = 0.042243, c = 12. Bound for +31: (7/8)(0.0422) − 12/124 = **−0.0598**; actual m = 0.028802.

**FACT (component growth is real).** Adding 97, 101, 103, 107: c = 12 → 12 → 16 → 20 → 26 (worst case allows +v each time).

**FACT (required super-increasing sequence, 10% relative-loss budget per step, v ≥ c/(0.35m)):**

| step | v required | m after (bound) | c ≤ |
|---|---|---|---|
| 1 | 812 | 0.03327 | 824 |
| 2 | 70,740 | 0.02620 | 7.2·10⁴ |
| 3 | 7.8·10⁶ | 0.02063 | 7.9·10⁶ |
| 4 | 1.1·10⁹ | 0.01625 | 1.1·10⁹ |
| 5 | 1.9·10¹¹ | **0.01279 < floor** | — |

**Where it breaks (FACT):** (a) (7/8)^j decay caps j ≤ 8 even with zero error (0.0422·(7/8)^j crosses 97/6864 at j = 8.20); (b) the c_{i−1}/(4v_i) error forces doubly-exponential speeds; step 5 is already impossible. Multi-large-speed induction is **dead** without a component-count lemma.

## Q3 — C-floor status

**FACT.** All-small case: C(24,14) = 1,961,256 sets enumerated (106 s): **0 below floor**; minimum = 0.0141317 = 97/6864 attained at K* = {1..15}∖{6}.

**FACT.** Combined with Q1: C-floor holds for every 14-set with ≤ 1 speed ≥ 25.

**OPEN.** 14-sets with ≥ 2 speeds ≥ 25 — this is the entire remaining content of C-floor. Largest explicit uniform c today: c = 240⁻¹⁴ ≈ 4.8·10⁻³⁴ (L17). Conditional c = 97/6864.

## Q4 — Discrete one-large-speed lemma; P₀

**PROOF (L-D1).** For a prime p, H = ⌊p/16⌋, speed s, and an integer interval I of length ℓ: #{x ∈ I : ‖sx‖_p ≤ H} = #{y ∈ [−H,H] : t y mod p ∈ I} (t = s⁻¹). Erdős–Turán–Koksma over the 2H+1 consecutive y's (ht mod p permutes residues) gives error ≤ C₀ log²p. Summing over the ≤ c(S) safe runs:

**U(S∪{s}) ≥ (1 − (2H+1)/p)·U(S) − c(S)·C₀·log²p**, with (2H+1)/p ≤ 1/8 + 1/p. No Dirichlet, any s.

**FACT (numerical, p = 601, allowed).** S = {1..13}: U = 14 cells in 6 runs; adding s = 100, 251, 300 loses 1, 2, 3 cells — lemma satisfied with huge slack (crude bound 452, vacuous at this p as expected).

**FACT (P₀ arithmetic).** Transfer needs p^{1/14} > 28/(2c₀): unconditional c₀ = 240⁻¹⁴ → P₀ = (28·240¹⁴)¹⁴ = 10^486.8; conditional c₀ = 97/6864 → P₀ = (112·6864/97)¹⁴ = 7925.4¹⁴ = 10^54.59. P₀ = 10⁴ needs c₀ ≥ 112/10^(4/14) = **58.0 > 1** — impossible. **IDEA:** 10⁴ requires deleting the p^{1/14} factor, i.e., a direct discrete transfer for large-speed sets.

## Q5 — Lemma ledger

| lemma | status |
|---|---|
| per-interval loss min(L, L/8+1/(4v)) | **PROVED** |
| grid screen certifies (grid-safe ⊆ true-safe) | **PROVED** |
| C-floor, ≤ 1 speed > 24 | **PROVED** (this round, computational) |
| L-D1 discrete one-large-speed | **PROVED** (ET) |
| C-floor, ≥ 2 speeds ≥ 25 | **OPEN** — via component growth |
| component bound c(S)·log²p = o(U(S)) for large-speed S | **OPEN** — the crux |
| discrete transfer without p^{1/14} | **OPEN** — follows from component bound |

**Distance to P₀ ≈ 10⁴ (IDEA):** one conjecture away — c(S) ≤ polylog(p) for all 14-sets (observed max c = 56 over 13-sets max ≤ 24; worst-case arcs allow ~p). With it, peeling + L-D1 gives U(S) ≥ (7/8)¹⁴n − O(log³p), P₀ ≈ 10³–10⁴. Without it, P₀ stays ≥ 10^54 even granting full C-floor.
--- end verbatim ---
END LETTER
