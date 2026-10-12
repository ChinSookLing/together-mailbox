BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:49 +08
RE: 猜公式 Round 17 ADDENDUM reply (Opus 9c7d507 seed addendum, sent as follow-up in same chat), send text r17_addendum_send.txt
SEAT: kimi
MODEL: K3 High (web)
CHAT: https://www.kimi.ai/chat/1a12ef65-62b2-86ef-8000-09cef7f03a3f

--- reply verbatim ---
[Hesper capture note: Kimi Copy truncates; addendum reply captured in 3 partial page-text pieces (start, Card #6 rest, Card #7 + rest), joined at marked seams; may not be gap-free — if Opus needs exact text, Tuzi can paste from the chat.]

[piece 1/3]
# ADDENDUM REPLY — verbatim capture (streaming)
Chat: https://www.kimi.ai/chat/1a12ef65-62b2-86ef-8000-09cef7f03a3f
Reply started emitting after the second Thinking block completed. The reply begins with the header "PT005 · Round 17 · ADDENDUM REPLY (Seat Kimi)".

--- SECTION 1 (so far) ---
PT005 · Round 17 · ADDENDUM REPLY (Seat Kimi)

Verification verdict per seed: all five seeds are real and opened in this session. Two are strong enough to card. Sungkawichai–Trakulthongchai (arXiv:260
[TRUNCATED mid-sentence — to be continued in next append]--- CONTINUING from "Sungkawichai–Trakulthongchai (arXiv:260" ---

Sungkawichai–Trakulthongchai (arXiv:2604.23906) was already carded as part of my Ingredient #4 (its mod-p polynomial lemma is quoted there). One cross-confirmation worth flagging immediately: Allikvere's sieve has exactly two persistent orbits at k=13, "the second is the Goddyn–Wong example" (1,…,11,13,24) — the same tight set Zhang's census found (his Thm 1.8(iii)). Two independent papers, same exceptional set. FACT.

Ingredient #: 6
Reference: M. Beck & S. Everett, "Lonely Runner Relations", arXiv:2609.06259v2 (22 Sep 2026), dedicated to Wills
Status: READ (full HTML: Thm 1.1, Thm 2.1 incl. proof, Thm 3.2, Cor 3.3)
Statement: Thm 1.1: any counterexample or tight instance n of LRC (k speeds) satisfies m·n = 0 for some m ∈ ℤ^k with 0 < ‖m‖₁ ≤ min(2k+3, ((k+1)/(k−1))·flt(k)); the 2k+3 branch can be tak…

[TRUNCATED by find_text's 4000 context — next sentence captured below]--- CONTINUING Card #6 Statement from "the 2k+3 branch can be" ---

the 2k+3 branch can be taken harmful (coordinate sum odd) with ‖m‖₂ ≤ 2(k+1)/√(k−1) (Thm 2.1). Thm 3.2: the same with flt(k)/(1−2λ) for the λ-margin zonotope, any shifts. Cor 3.3: random n ⊂ {1..j} has lon(n,s) ≥ λ whp as j→∞ (generalizes Czerwiński 2012, shifted). Serves dish: C (and D as bonus) How it plugs in: (i) STRUCTURE FILTER: any tight/near-extremal 14-set must lie on a hyperplane with ‖m‖₁ ≤ 2·14+3 = 31 (computed here) — a finite, enumerable relation set; the authors note the baseline (1,…,k) sits on 2x₁−x

[TRUNCATED at "sits on 2x₁−x" — next anchor: "sits on"]--- CONTINUING past "sits on" ---

…sits on 2x₁−x₂=0 and suggest exactly this search playground. (ii) FOURIER SKELETON: their H(t) = ∏ W_h(v_j t) with h = 1/2 − 1/16 = 7/16 is positive exactly on PT005's good set; eq. (2.5) expands H in frequencies indexed by relations c·n = 0 — this is the rigorous version of the "empty-coset / relation" intuition behind the random model (Dish D). What it gives: no

[TRUNCATED at "What it gives: no" — next anchor: "What it gives: no"]--- CONTINUING Card #6 "What it gives" ---

What it gives: no new constant; a theorem that extremals are low-height — the hyperplane search is a finite computation per k. UNFINISHED: running the relation census for k=14 and checking whether {1..15}∖{6}'s measure-extremality is forced by its relation set. Gap: theorem applies to tight/counterexample at margin 1/(k+1); PT005's extremal is at sub-tight margin 1/16 (LR = 2/23 > 1/15, computed last round), so Thm 1.1 does not apply to it directly — the λ-form of Thm 3.2 does: hollow at λ ⇒ relation with ‖m‖₁ ≤ flt(k)/(1−2λ), i.e. ≤ 8·flt(14) at λ = 1/16 (quoted constant, not computed).

Ingredient #: 7 Reference: [TRUNCATED]--- CONTINUING Card #7 (Allikvere) ---

Ingredient #: 7
Reference: J. Allikvere, "Fourteen and fifteen lonely runners", arXiv:2609.02604v2 (Sep 2026; v1 covered 14 only; code+certificates on Zenodo 22066772 / 22667683)
Status: READ (full HTML: Thm 1.1, flag bound Thm 3.8, Lemma 3.10, §5–6)
Statement: LRC holds for 14 and 15 runners (k = 13, 14 speeds). Method: KZ-basis flag bound using all n−1 prefix inequalities (Prop 3.4: t₁+⋯+t_r > (2r/((n+1)(n+1−r)))²) + forced divisor lcm(2,…,n+1) | v₁⋯v_n + prime sieve with binary lifting and a 15 = 3·5 CRT split + few-exception shift lemma.
Serves dish: B (census technology), with a Dish-C side observation
How it plugs in: replaces PT005's P₀ ≈ 10⁴⁸⁷ step by the operative route: log-product bound + forced divisor + Σ_{p∈P} log p. For 15 runners: bound 810.074 → 414.7794 ("nearly halves": my ratio = 0.5120); arithmetic check mine: ln lcm(2..15) = 12.79486, and 12.7948 + 401.9846 = 414.7794 exactly as in Cor 3.11. For 14 runners: 111 → 61 primes; I recomputed P₁₃: |P₁₃| = 61 and Σ ln p = 353.772559… > 341.032 = their n=13 bound ✓ (also C(110,12) = 3,517,322,746,798,575 ✓, computed).
What it gives: if correct, LRC(15) settles PT005's nonemptiness (m(K) > 0) outright — margin 1/15 > 1/16. It also shows tight sets are exactly the sieve's persistent obstructions ((1,…,13) and the Goddyn–Wong set survive all binary lifts) — Dish C meets Dish B. The 810.074 / 341.031991 / 408.8233 figures are QUOTED (not recomputed here — UNFINISHED), though every identity I could check

[TRUNCATED — reply still streaming; send button still a disabled stop; input "Keep asking, messages will be queued…"]
[piece 2/3]
# ADDENDUM REPLY verbatim — intro + Card #6 opening
(Chat https://www.kimi.ai/chat/1a12ef65-62b2-86ef-8000-09cef7f03a3f, reply immediately following the user's Round 17 ADDENDUM message)

---

PT005 · Round 17 · ADDENDUM REPLY (Seat Kimi)

Verification verdict per seed: all five seeds are real and opened in this session. Two are strong enough to card. Sungkawichai–Trakulthongchai (arXiv:2604.23906) was already carded as part of my Ingredient #4 (its mod-p polynomial lemma is quoted there). One cross-confirmation worth flagging immediately: Allikvere's sieve has exactly two persistent orbits at k=13, "the second is the Goddyn–Wong example" (1,…,11,13,24) — the same tight set Zhang's census found (his Thm 1.8(iii)). Two independent papers, same exceptional set. FACT.

```
Ingredient #: 6
Reference: M. Beck & S. Everett, "Lonely Runner Relations", arXiv:2609.06259v2 (22 Sep 2026), dedicated to Wills
Status: READ (full HTML: Thm 1.1, Thm 2.1 incl. proof, Thm 3.2, Cor 3.3)
Statement: Thm 1.1: any counterexample or tight instance n of LRC (k speeds) satisfies m·n = 0 for some m ∈ ℤ^k with 0 < ‖m‖₁ ≤ min(2k+3, ((k+1)/(k−1))·flt(k)); the 2k+3 branch can be taken harmful (coordinate sum odd) with ‖m‖₂ ≤ 2(k+1)/√(k−1) (Thm 2.1). Thm 3.2: the same with flt(k)/(1−2λ) for the λ-margin zonotope, any shifts. Cor 3.3: random n ⊂ {1..j} has lon(n,s) ≥ λ whp as j→∞ (generalizes Czerwiński 2012, shifted).
Serves dish: C (and D as bonus)
How it plugs in: (i) STRUCTURE FILTER: any tight/near-extremal 14-set must lie on a hyperplane with ‖m‖₁ ≤ 2·14+3 = 31 (computed here) — a finite, enumerable relation set; the authors note the baseline (1,…,k) sits…
```
(end of match-1 context window; continued in next append)

[piece 3/3]
# Card #6 continuation (through Gap) — verbatim

(Card #6's "How it plugs in" from "the authors note the baseline" through end of Gap)

How it plugs in: (i) STRUCTURE FILTER: any tight/near-extremal 14-set must lie on a hyperplane with ‖m‖₁ ≤ 2·14+3 = 31 (computed here) — a finite, enumerable relation set; the authors note the baseline (1,…,k) sits on 2x₁−x₂=0 and suggest exactly this search playground. (ii) FOURIER SKELETON: their H(t) = ∏ W_h(v_j t) with h = 1/2 − 1/16 = 7/16 is positive exactly on PT005's good set; eq. (2.5) expands H in frequencies indexed by relations c·n = 0 — this is the rigorous version of the "empty-coset / relation" intuition behind the random model (Dish D).
What it gives: no new constant; a theorem that extremals are low-height — the hyperplane search is a finite computation per k. UNFINISHED: running the relation census for k=14 and checking whether {1..15}∖{6}'s measure-extremality is forced by its relation set.
Gap: theorem applies to tight/counterexample at margin 1/(k+1); PT005's extremal is at sub-tight margin 1/16 (LR = 2/23 > 1/15, computed last round), so Thm 1.1 does not apply to it directly — the λ-form of Thm 3.2 does: hollow at λ ⇒ relation with ‖m‖₁ ≤ flt(k)/(1−2λ), i.e. ≤ 8·flt(14) at λ = 1/16 (quoted constant, not computed).

---

# Card #7 (Allikvere) — verbatim

Ingredient #: 7
Reference: J. Allikvere, "Fourteen and fifteen lonely runners", arXiv:2609.02604v2 (Sep 2026; v1 covered 14 only; code+certificates on Zenodo 22066772 / 22667683)
Status: READ (full HTML: Thm 1.1, flag bound Thm 3.8, Lemma 3.10, §5–6)
Statement: LRC holds for 14 and 15 runners (k = 13, 14 speeds). Method: KZ-basis flag bound using all n−1 prefix inequalities (Prop 3.4: t₁+⋯+t_r > (2r/((n+1)(n+1−r)))²) + forced divisor lcm(2,…,n+1) | v₁⋯v_n + prime sieve with binary lifting and a 15 = 3·5 CRT split + few-exception shift lemma.
Serves dish: B (census technology), with a Dish-C side observation
How it plugs in: replaces PT005's P₀ ≈ 10⁴⁸⁷ step by the operative route: log-product bound + forced divisor + Σ_{p∈P} log p. For 15 runners: bound 810.074 → 414.7794 ("nearly halves": my ratio = 0.5120); arithmetic check mine: ln lcm(2..15) = 12.79486, and 12.7948 + 401.9846 = 414.7794 exactly as in Cor 3.11. For 14 runners: 111 → 61 primes; I recomputed P₁₃: |P₁₃| = 61 and Σ ln p = 353.772559… > 341.032 = their n=13 bound ✓ (also C(110,12) = 3,517,322,746,798,575 ✓, computed).
What it gives: if correct, LRC(15) settles PT005's nonemptiness (m(K) > 0) outright — margin 1/15 > 1/16. It also shows tight sets are exactly the sieve's persistent obstructions ((1,…,13) and the Goddyn–Wong set survive all binary lifts) — Dish C meets Dish B. The 810.074 / 341.031991 / 408.8233 figures are QUOTED (not recomputed here — UNFINISHED), though every identity I could check arithmetically did check.
Gap: author's own §6: "The full computation has not been independently reimplemented or formally verified" — matches the automated review's single-implementation flag; contrasts with Zhang's dual-path certification. And it says NOTHING about the measure m(K): PT005's C-floor survives even if LRC(15) is proven.

---

# Verified but not carded (brief) — verbatim

Jensen, "Mixed thresholds in the Lonely Runner Conjecture", arXiv:2605.27941 — READ abstract: unequal per-runner thresholds d_i, exact characterization for k=2, and Fourier series of distance-threshold indicators with "an exact two-function integral formula for unequal thresholds". Potentially useful if PT005 ever needs unequal margins; not usable for the uniform 1/16 problem as-is → not carded.

Poliakova, "More (shifted) runners, less loneliness", arXiv:2609.23952 — READ abstract: shifted LRC (disproved by Blanco–Criado–Santos, smallest counterexample (1,2,3,4,5)) fails linearly: E_n ≥ ⌊n/287⌋, and E_n ≥ 1 for n ≥ 95. Kept strictly separate from the unshifted problem per the chair's warning; its only message for us is a boundary marker: no proof of the unshifted C-floor may pass through a statement that would also hold shifted.

Blanco–Criado–Santos, arXiv:2603.24784 — seen only as a citation inside both papers above: ABSTRACT (not opened).

---

# Conclusion — verbatim

Does this change my one-dish pick? No — still Dish C, and the addendum strengthens the case: Beck–Everett give the first structural theorem explaining why extremals must be arithmetic (short harmful relations), and Allikvere — if it stands — removes existence (the easy part of Dish B) from the table entirely while explicitly leaving the measure question untouched. The C-floor (97/6864, its 4 slivers, the missing 6) is now the sharpest open piece, and its explanation runs through wells at unit fractions (Zhang), relation hyperplanes (Beck–Everett), and tight-set obstructions (Goddyn–Wong; both censuses).

(Followed by Kimi's post-reply "All files / View or download files Preview Reference" footer — the reply end.)

--- end verbatim ---
END LETTER
