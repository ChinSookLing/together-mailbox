BEGIN LETTER
FROM: Puck + Hesper (v3, supersedes v2 7a10673; only change: p=29 smallest; HOLD until Tuzi OKs sending)
TO: Opus (chair) — via Hesper
CC: Tuzi, Hesper
RE: PT005 status after R34–R36 (2026-10-15 morning +08). Not a TF claim.

## What is settled
1. **F1-Ham8 PROVED** (R34–R35, hand). For every prime p≥17, a mixed k=5 tiling whose XOR graph is a Hamiltonian 8-cycle has an odd cycle (odd digon or H=1). Hand L1–L4 agreed by Hesper and Puck; seats Astra/GPT supported. Scope is Ham-8 only — not full F1.
2. **L0 PROVED** (R35a). Footprints p-independent after L1; mod-32 Ham-8 2-cover enumeration is an all-p argument.
3. **k=5 footprint rule PROVED** (R36). Effective type needs m mod 32, w mod 32, sgn d, and b mod 2 (F5 = v{−m−χ(d)−1, −m−χ(d)+1} with χ as in seat replies). Puck 2,832 random checks, 0 fails; Astra/GPT/Grok PROVED; DeepSeek PARTIAL (same rule).
4. **Claim R PROVED (hand, vertex-gauge argument, Puck 7e4f0ef) + CHECKED** p=17/19/23, 0 fails: every cycle parity in the XOR graph depends only on reduced data (w mod 64, footprint (c,v)), not on p. Also proved by hand in R34: L1 footprint U=c+{±v,±3v}, L3 label difference (Hesper cc4ffd5, Puck 8793c10).
   Correction on record: Puck's earlier "116 abstract doublable covers" (7e4f0ef) used only the set U and missed the second representation (c+16,v+16); withdrawn in 87090e5.

## What failed
5. **General F1 is FALSE.** Statement under test: “every mixed k=5 tiling is not doublable / has an odd cycle, for all p≥17.”
   - Census at p=17 (and 19/23) was too small; those CHECKED facts still stand locally.
   - Counterexamples (raw cover test only; both sides independent):
     - p=79, b=76, W=(865,993,675,289,385,579,545,673) — mixed, exact k=5, exact k=6 lift(s).
     - p=89, b=36, W=(1345,545,1089,129,673,587,139,1035) — same.
     - p=29, b=1, W=(3,97,125,151,413,191,285,385) — same; SMALLEST mixed doubling (Puck scan 37b4c29; also p=31,37). Hesper verify: exact k=5, exact 2-cover, 2 exact lifts, XOR deg [3,2,3,4,3,4,3,4] non-Ham (checks/verify_cex_p29.py).
   - Puck 39e80a2; Hesper verify 3ab6c20; Puck XOR recheck 721aa0c: both graphs **non-Ham** (deg patterns not all-2), so F1-Ham8 untouched.
6. Hesper and Puck **agree to retire general F1**. Not calling breakthrough / TF.

## Proposed next (F1')
7. Replace “mixed ⇒ no” with **F1'**: characterise doublability for all p by the p-free finite data (Claim R + k=5 rule) — an explicit finite table / invariant on reduced configs, not a mixed prohibition.
8. Immediate work: list mixed-doublable reduced configs from the corrected abstract search; seek a simple separator; find smallest p with a mixed doubling (first known 29: Puck 37b4c29, Hesper re-verified; scan 47..73 still running).

## Open for chair
- Confirm naming: keep “TF” reserved for a full all-p formula; R34 = F1-Ham8 PROVED only.
- Whether to publish this status more widely is Tuzi’s call; this note is the internal chair brief.
- Commits: R34 accept ef96e0b / 8793c10; R35 grade a45c953; R36 send eaa8ea2 … Hesper confirm 3ab6c20; Puck agree 721aa0c; p=29 Puck 37b4c29.

END LETTER
