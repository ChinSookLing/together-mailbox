BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:49 +08
RE: 猜公式 Round 17 literature walk (packet ad54489), send text r17_send_full.txt or r17_send_short.txt
SEAT: kimi
MODEL: K3 High (web)
CHAT: https://www.kimi.ai/chat/1a12ef65-62b2-86ef-8000-09cef7f03a3f

--- reply verbatim ---
[Hesper capture note: Kimi Copy/Share truncate; reply captured page-text in 9 overlapping sections; '=== ... ===' lines are the capture agent's seam markers, not the seat's; overlap text repeats at seams. Earlier send-task capture (Conclusions + Ingredient 1 head) agreed.]

=== ROUND 17 REPLY — SECTION 1 (rendered plain text, anchor: "Seat Kimi — Dish C lane") ===
Note: Captured as the page renders it. The chat's Copy produces markdown (**) but truncates; Share/Copy link only reproduced the same truncated markdown. This is the untruncated rendered reply. Bold/emphasis markup was used in rendering; plain text preserves all content, numbers, and structure.

--- BEGIN REPLY ---
PT005 · Round 17 · Seat Kimi — Dish C lane, with one cross-lane find for A/B

Conclusions first

FACT (my own exact computation — PROOF by exact rational arithmetic, code run in this session). m({1..15}∖{6}) = 97/6864 exactly. The good set is exactly 4 slivers: [33/208, 31/192], [11/64, 31/176], and their mirrors under x ↦ 1−x. Among all 14-subsets of {1..16} and of {1..17}, {1..15}∖{6} is the unique minimizer (float screen; winner certified exactly; exact certification of the full screen UNFINISHED — the runner-up 101/6435 differs by 1.6×10⁻³, far above float error).

FACT (cross-validated). The magic constant 97/6864 is already in the literature, as a formula: Zhang (arXiv:2608.13599, July 2026), Theorem 1.4 computes exactly the components of U(n,r) = {t : ‖it‖ > 1/n ∀ i ∈ [n−1]∖{r}} — which for (n,r) = (16,6) is precisely PT005's good set. I implemented his formula independently and it reproduces my exact measures for all 14 values r = 2,…,15, 14/14 matches. This upgrades 97/6864 from "census output" to "closed form."

FACT + I…

=== END OF SECTION 1 (truncated by the 2000 context_chars cap; next section will overlap) ====== SECTION 2 (anchor: "FACT + IDEA") — overlaps Section 1 at "FACT + I…"; begins new content at "FACT + IDEA (the "why 6" answer)" ===

FACT + IDEA (the "why 6" answer). Summing Zhang's component lengths gives (punctured regime 2r ≤ n−1), with s = n−r and F(u) = largest speed ≤ n−1 congruent to a unit u mod r: M(n,r) = (1/(rn))·(2s·Σ_{u unit mod r} 1/F(u) − φ(r)) (my derivation from his Thm 1.4; verified exact against all 14 cases). Deleting r leaves wells only at t = p/r with gcd(p,r)=1 (Zhang, READ). r=6 wins because 6 is the largest r ≤ 15 with φ(r) ≤ 2: fewest wells (just 1/6 and 5/6), each punctured at the center by 2r = 12 and pinched by 11 and 13. r = 2,3,4 also have φ ≤ 2 but fatter wells (smaller F, larger s); r = 5,7,… have φ ≥ 4 → many wells. Hand check of the constant: slivers have widths (2s−13)/(2·6·16·13) = 7/2496 and (2s−11)/(2·6·16·11) = 3/704; total = 2·(77/27456 + 117/27456) = 2·194/27456 = 97/6864 ✓.

FACT (computed here). LR({1..15}∖{6}) = 2/23, attained at t = 4/23 (crossing of the k=11, k=12 sawteeth: 11t = 2−2/23, 12t = 2+2/23) — the argmax lies inside the good sliver [11/64, 31/176]. The set is not tight (2/23 > 1/15), consistent with Zhang's classification (r=6 falls in 3 ≤ r ≤ (n−1)/2, no tight one-entry modification) [citation], and consistent with Kravitz's rigidity conjecture (2/23 ≥ 1/14). Also: adding 6 back gives the tight baseline {1..15} with LR = 1/16 and m = 0 — speed 6 collapses the good set from 4 slivers to isolated points, because at t ≈ 1/6, 6t ≡ 0 (mod 1): 6's bad zones sit exactly on the deepest wells.

=== Section 2 ends where Conclusions 4 ends. Next anchor "Dish B cross-lane note" should overlap. ====== SECTION 3 (anchor: "Dish B cross-lane note") — overlaps Section 2 through "speed 6 collapses..." ===

Dish B cross-lane note (computed here). Malikiosis–Santos–Schymura reduce LRC checking for 15 runners to speeds ≤ C(15,2)¹³ = 105¹³ = 188564914232323560791015625 ≈ 10^26.3 (my arithmetic). Big improvement over P₀ ≈ 10⁴⁸⁷, still far from 10⁴. The practical closing technology is the Rosenfeld–Trakulthongchai prime sieve, not a threshold bound.

Dish D/E (verified anchors). Czerwiński 2012 (random runners are very lonely, ML ≥ 1/2−ε whp) — qualitative support that the extremal set must be arithmetic, not random; no quantitative match to U ≈ n·e^(−14H/n): UNFINISHED. Sungkawichai–Trakulthongchai have a genuine mod-p statement: speeds ≡ (1,2,…,k) mod p satisfy LRC when k+1 and p > k²+k are both odd primes — this is a ℤ_p result about the baseline, directly PT005-flavored.

Ingredient cards
---
Ingredient #: 1
Reference: Yuhan Zhang, "Tight instances of the Lonely Runner Conjecture" (v1 title: "Single-speed modifications of the tight Lonely Runner instance: an effective bound…
[Ingredient 1 continues; captured in detail below via its own anchor.]

=== Section 3 ends where Ingredient 1 starts. Next: Ingredient 1 full card. ====== SECTION 4 (Ingredient 1 full + start of Ingredient 2, anchor: "Lemma 2.2 (LR attained at t = (2a+1)/2v") ===

Ingredient #: 1
Reference: Yuhan Zhang, "Tight instances of the Lonely Runner Conjecture" (v1 title: "Single-speed modifications of the tight Lonely Runner instance: an effective bound and the complete classification for r=2"), arXiv:2608.13599, July 2026 (preprint; data/code on Zenodo+GitHub)
Status: READ (full HTML; Theorems 1.1–1.8, Lemmas 2.1–2.3, §3 proofs)
Statement: Thm 1.4: for 2 ≤ r ≤ n−1, s = n−r, every component of U(n,r) = {t: ‖it‖ > 1/n ∀i∈[n−1]∖{r}} lies in the 1/(rn)-neighborhood of a single p/r with gcd(p,r)=1; for 2r ≤ n−1 it is the punctured pair 1/(2rn) < ±δ < s/(rnF(±u)), u = p⁻¹ mod r; longest component has length ℓ(n,r) = (2s−I)/(2rnI), I = min over units of min(F(u),F(r−u)).
Serves dish: A and C
How it plugs in: PT005's m(K) for K = {1..15}∖{6} IS meas U(16,6). His formula turns "C-floor for deleted baselines" into closed-form evaluation. Lemma 2.2 (LR attained at t = (2a+1)/2v, b/(v+w), b/(w−v)) also certifies LR values finitely — my LR code is an independent instance.
What it gives: m({1..15}∖{6}) = 2·(7/2496 + 3/704) = 97/6864 — COMPUTED here, matches my independent exact sweep on all r=2..15 (14/14). Also gives c = 97/6864 for the whole deleted-baseline family (min over r attained at r=6 — my screen of all r).
Gap: (i) Only covers K = [n−1]∖{r}; need a reduction lemma "some deleted baseline is at least as bad as any K" — UNFINISHED. (ii) Preprint, not yet refereed — mitigated: I reproduced its numbers exactly. (iii) His margin is strict >, ours ≥; measures equal.

Ingredient #: 2
Reference: L. Goddyn & E. B. Wong, "Tight instances of the lonely runner", Integers 6 (2006), #A38 — as quoted verbatim (Thms 2.3, 2.4, Lemma 2.2 observation) inside Zhang 2026
Status: ABSTRACT for the paper itself (not opened); READ for the statements I use (quoted in Zhang 2026, which I opened)
...
[Ingredient 2 body continues below.]

=== Section 4 ends. Next: Ingredient 2 body. ====== SECTION 5 (Ingredient 2 full + start of 3, anchor: "Prop 1.3 of Zhang (r") ===

Ingredient #: 2
Reference: L. Goddyn & E. B. Wong, "Tight instances of the lonely runner", Integers 6 (2006), #A38 — as quoted verbatim (Thms 2.3, 2.4, Lemma 2.2 observation) inside Zhang 2026
Status: ABSTRACT for the paper itself (not opened); READ for the quoted statements in Zhang (web_search:6#8 shows the original PDF exists on Semantic Scholar; venue confirmed in 4 independent bibliographies)
Statement: (Thm 2.3) LR([n−1]_{r↦mr}) ≥ 1/n, equality iff n=2, (3,1,4), or gcd(r,b)>1 ∀b∈{s,…,ms−1}. (Thm 2.4) for fixed r only finitely many tight non-multiple replacements. (Lemma 2.2 obs.) if 2x ≥ n then at t=1/x every speed of [n−1]∖{x} is ≥ 1/x > 1/n from ℤ.
Serves dish: C
How it plugs in: the Lemma-2.2 observation is exactly the "well at t=1/r" mechanism behind my computed slivers; Prop 1.3 of Zhang (r | w divisibility forced for r > (n−1)/2) explains why large deletions stay tight only via multiples — i.e., why the extremal deletion must be a SMALL r, and among small r the φ(r)=2 analysis picks 6.
What it gives: qualitative; the quantitative content is via Ingredient 1. Numbers here are mine only (φ-table: r=2,3,4,6 have φ≤2).
Gap: middle range n/6 ≤ r ≤ (n−1)/2 tightness classification is Zhang's open Question 5.1 — irrelevant for measure but relevant if PT005 wants the full tight-set list at n=15,16.

Ingredient #: 3
Reference: N. Kravitz, "Barely lonely runners and very lonely runners: a refined approach to the Lonely Runner Problem", Comb. Theory 1 (2021), #17; arXiv:1912.06034
Status: READ (abstract page)
Statement: Conjecture (rigidity): for every speed set, ML = s/(ns+1) for some s ∈ ℕ, or ML ≥ 1/n. Proved: n ≤ 3; n = 4, 6 with one s…

=== Section 5 ends. Next: continue Kravitz card. ====== SECTION 6 (Ingredient 3 full + start of 4, anchor: "n = 4, 6 with one s") ===

Ingredient #: 3
Reference: N. Kravitz, "Barely lonely runners and very lonely runners: a refined approach to the Lonely Runner Problem", Comb. Theory 1 (2021), #17; arXiv:1912.06034
Status: READ (abstract page)
Statement: Conjecture (rigidity): for every speed set, ML = s/(ns+1) for some s ∈ ℕ, or ML ≥ 1/n. Proved: n ≤ 3; n = 4, 6 with one speed much faster than the rest.
Serves dish: C (and A)
How it plugs in: predicts a spectral gap above the tight value — supports the C-floor picture that near-extremal sets snap to discrete types. My computed data point: LR({1..15}∖{6}) = 2/23 ≥ 1/14, i.e. the "≥ 1/n branch" — consistent, n=14 speeds not covered by his theorems. Sister paper Giri–Kravitz (arXiv:2304.01462, READ abstract): accumulation points of the n-th spectrum = the (n−1)-th spectrum.
What it gives: no new constant — UNFINISHED for PT005 numerics.
Gap: rigidity is conjectural beyond n ≤ 3 (and 4,6 special case).

Ingredient #: 4
Reference: M. Rosenfeld, arXiv:2509.14111 (8 runners, 2025); T. Trakulthongchai, arXiv:2511.22427 (9–10, EJC to appear 2026); T. Sungkawichai & T. Trakulthongchai, arXiv:2604.23906 (11–13, 2026)
Status: READ (abstract pages; chunks of the EJC paper)
Statement: LRC…

=== Section 6 ends. Next: continue Ingredient 4. ====== SECTION 7 (Ingredient 4 full, anchor: "Sungkawichai & T. Trakulthongchai, arXiv:2604.23906") ===

Ingredient #: 4
Reference: M. Rosenfeld, arXiv:2509.14111 (8 runners, 2025); T. Trakulthongchai, arXiv:2511.22427 (9–10, EJC to appear 2026); T. Sungkawichai & T. Trakulthongchai, arXiv:2604.23906 (11–13, 2026)
Status: READ (abstract pages; chunks of the EJC paper)
Statement: LRC holds for k+1 ≤ 13 runners; method = bound the product of speeds of a minimal counterexample + prime sieve: ∏_{p∈S₈}p > 10⁸², ∏_{p∈S₉}p > 10¹¹² (their numbers, QUOTED not computed by me). Rosenfeld: "computer verification and … bounding the size of a minimal counterexample". ST26 add the mod-p polynomial lemma (above).
Serves dish: B (and E)
How it plugs in: this is the census technology PT005 needs at n=15 — note LRC itself is OPEN at n=14,15 runners (Allikvee arXiv:2609.02604 claims 14–15, unverified per cairn-commons listing, ABSTRACT-level). PT005 only needs the *measure* version at margin 1/16, weaker.
What it gives: no threshold number computed by me — UNFINISHED; but the sieve ("product must be divisible by many primes" + interval-emptiness I(k,k+1,p) = ∅) is the realistic closing method for Dish B at n=15. ST26's mod-p polynomial lemma is additionally useful for Dish E (PT005 mod p).
Gap: sieve method cost is exponential in k; not yet adapted to measure/C-floor.

=== Section 7 ends. Next: Ingredient 5. ====== SECTION 8 (Ingredient 5 full + Remaining seed list + Last question, anchor: "Ingredient #: 5") ===

Note: This window is the authoritative fuller wording for Ingredient 4's "What it gives" too (overlaps Section 7's paraphrase). Authoritative Ingredient 4 "What it gives" + "Gap" from this window:

Ingredient 4 (What it gives, authoritative): no threshold number computed by me — UNFINISHED; but the sieve ("product must be divisible by many primes" + interval-emptiness I(k,k+1,p) = ∅) is the realistic route 10⁴⁸⁷ → 10⁴.
Ingredient 4 (Gap, authoritative): method cost is exponential in k; not yet adapted to measure/C-floor.

Ingredient #: 5
Reference: R. D. Malikiosis, F. Santos, M. Schymura, "Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants", Forum of Mathematics, Sigma 13 (2025), e164; arXiv:2411.06903
Status: READ (abstract via arXiv HTML listing)
Statement: to prove LRC for n+1 runners it suffices to check positive integer velocities up to C(n+1,2)^{n−1} ≤ n^{2n} (improving Tao's n^{O(n²)}).
Serves dish: B
How it plugs in: replaces the "effective Kronecker" threshold by a zonotope covering-radius argument; for PT005 (14 speeds) gives 105^13 = 188564914232323560791015625 ≈ 1.9×10^26 — COMPUTED here.
Gap: 10^26 ≫ 10^4 goal; and it bounds SPEEDS, while PT005's census also needs the measure statement; the sieve (Ingredient 4) must close the rest.

Remaining seed list — verification status (brief)
Wills 1967 (Monatsh. Math. 71:263–269), Cusick 1973 (Aequat. Math…

=== Section 8 ends inside the Remaining seed list. Continue below. ====== SECTION 9 (Remaining seed list full + Last question, bridge at "verification status (brief)" overlaps Section 8; full text of the end of the reply) ===

Remaining seed list — verification status (brief)

Wills 1967 (Monatsh. Math. 71:263–269), Cusick 1973 (Aequationes Math. 9:165–170), Bienia–Goddyn–Gvozdjak–Sebő–Tarsi 1998 (JCTB 72:1–9), Barajas–Serra 2008 (EJC 15 #R48, arXiv:0710.4495) — all citations confirmed real; papers not opened: ABSTRACT

Tao 2018, Contrib. Discrete Math. 13(2):1–31, arXiv:1701.02048 — READ abstract: gap 1/(2n) + c·log n/(n²(log log n)²); reduction to speeds n^{O(n²)}

Czerwiński–Grytczuk 2008, IPL 108(2):64–67 — ABSTRACT (statement seen via Chow–Rimanić's quotation): one may delete s runners and keep loneliness (s+1)/(2k) for the rest

Czerwiński 2012, JCTA 119(6):1194–1199 — READ abstract (publication data per Wikipedia listing)

Beck–Hoşten–Schymura, "Lonely Runner Polyhedra", arXiv:1606.01783 — READ abstract: polyhedral ansatz + a family of affirmative instances defined by parities of the speeds

Henze–Malikiosis 2017, Aequationes Math. 91(2):331–352 — ABSTRACT (seen in Giri–Kravitz's reference list)

Bohr-set bound |B(S,ρ)| ≥ ρ^|S| N (Tao–Vu ch. 4) — MEMORY, not verified this session; sharper bounds for small |S|: UNFINISHED — I could not find anything sharper in this session.

Perarnau–Serra survey "The Lonely Runner Conjecture turns 60", Comput. Sci. Rev. 58 (2025) 100798 — ABSTRACT (listing + chunks); good map of the whole terrain.

Last question (one line)

Dish C — it's the only dish where the target constant now has a published closed form (Zhang Thm 1.4) that I reproduced exactly (97/6864 = 2·(7/2496 + 3/704)), the "missing 6" has a one-line arithmetic reason (largest r with φ(r) ≤ 2, fewest and narrowest wells, punctured by 2r = 12), and what remains is a single reduction lemma rather than new machinery.

=== END OF ROUND 17 REPLY ===
[The "All files / View or download files / Preview / Reference" card and the per-message action bar (copy/regenerate/share/thumbs) follow immediately; those are UI chrome, not reply content.]
--- end verbatim ---
END LETTER
