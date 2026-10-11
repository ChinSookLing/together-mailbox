# PT005 · Round 17 · 出宫 (literature walk): bring back ingredients

From: Opus (chair) · 2026-10-11 18:48 +0800 (machine clock) · Requested by Tuzi 2026-10-11 18:45 ("not you only, ask help from everyone, and then you pick those like that 大长今 could use to cook the dishes for the emperor")
For: Hesper to send to **every seat**, in each seat's "PT005 · Big Picture" chat. Send the block BEGIN … END verbatim. Replies are committed verbatim.
Timing: this round runs **alongside Round 16**. A seat may answer R16 first and R17 after, or both in one reply.

**中文说明（给 Tuzi）：**
- 大长今每次考试前都会出宫走一趟，看见一样东西，拿回来做菜。这一轮就是让每个座位都出宫一趟，到文献里去找。
- 每个座位最多带回 5 样「食材」。每样都要写清楚四件事：
  1. 出处；
  2. 原文的定理；
  3. 能用在 PT005 哪一步；
  4. 真的用上以后能得到什么。
- 主席再一样一样地核对、挑选，只留下真能「做给皇上吃」的。
- 规矩最重要的一条：**不准编造文献**。没打开读过的，就必须写明「没读过」。

----- BEGIN PACKET -----

## PT005 · Round 17 · Literature walk (出宫)

**RULE (from Tuzi):** Any number you report must come from your own calculation in this reply, with the code shown or the hand computation shown. If you did not compute it, write UNFINISHED. Do not estimate or invent numbers.

**RULE (citations):** Every reference must be real. For each one, state how you know it, using exactly one of these tags:
- **READ**: you opened the paper in this session and quote it.
- **ABSTRACT**: you saw only the abstract or the listing page.
- **MEMORY**: from memory, not checked.

A fabricated citation voids your whole reply for this round. "I could not find anything for this step" is a good answer.

### What we need (the dishes)

- **Dish A · the constant.** Prove m(K) ≥ c for all 14-sets K, with c as close to 97/6864 ≈ 0.01413 as possible (the conjecture is C-floor). Today L17 gives c = 240⁻¹⁴.
  - Here m(K) = measure of {x ∈ [0,1) : ‖kx‖ ≥ 1/16 for all k ∈ K}.
- **Dish B · the threshold.** Make the "large p" step effective. Today P₀ ≈ 10⁴⁸⁷; the goal is about 10⁴, so the census can close the rest.
  - Tools: effective Kronecker/Dirichlet, discrepancy, Erdős–Turán–Koksma, Bohr-set size bounds.
- **Dish C · structure.** Why is the extremal set {1..15} ∖ {6}, and why does 6 drop out? Look for known tight or extremal instances of the lonely runner conjecture and their structure (for example, results by Goddyn–Wong).
- **Dish D · the random model.** Our count formula U ≈ n·e^(−14H/n) and the empty-coset fraction (7/8)¹⁴. Is there a theorem on random speed sets ("random runners") that matches it?
- **Dish E · finite field / mod p.** PT005 works mod p. Look for known results on the lonely runner problem, or view-obstruction, over ℤ_p or finite fields.

### Seed list from the chair (all MEMORY: verify before you use any of them)

These are starting points only. They may be misremembered. Confirm the authors, year, venue and exact statement yourself.

- **Wills (1967); Cusick (1973):** the origin of view-obstruction.
- **Bienia, Goddyn, Gvozdjak, Sebő, Tarsi (1998):** "Flows, view obstructions, and the lonely runner", J. Combin. Theory Ser. B.
- **Barajas & Serra (2008):** the seven-runner case.
- **Goddyn & Wong (2006):** tight instances.
- **Tao (2018):** "Some remarks on the lonely runner conjecture". Two items to check:
  - the reduction to bounded speeds;
  - the improved gap bound.
- **Malikiosis, Santos, Schymura (2024?):** "Linearly-exponential checking is enough for the lonely runner conjecture…". This bears on Dish B.
- **Henze & Malikiosis (2017?):** covering radius of lattice zonotopes and view-obstructions.
- **Beck, Hoşten, Schymura:** "lonely runner polyhedra" / shifted lonely runner.
- **Czerwiński & Grytczuk (2008?):** "Invisible runners in finite fields". This is likely Dish E.
- **Czerwiński (2012?):** "Random runners are very lonely". This is likely Dish D.
- **Kravitz (2021?):** "Barely lonely runners and very lonely runners". This bears on Dishes A and C.
- **Recent computer-assisted proofs for 8 or more runners (2025?):** find the authors and what method they used.
- **Bohr sets:** the size lower bound |B(S, ρ)| ≥ ρ^|S|·N (Tao–Vu, *Additive Combinatorics*, ch. 4). Is there a sharper bound for small |S|?

### What to bring back (at most 5 ingredients per seat)

Fill in this card for each ingredient:

```
Ingredient #:
Reference:       authors, title, venue, year, arXiv/DOI
Status:          READ / ABSTRACT / MEMORY
Statement:       the exact theorem, quoted or faithfully restated
Serves dish:     A / B / C / D / E
How it plugs in: which PT005 step (L16, L17, R16 Q1, census, ...) and what changes
What it gives:   the new constant or threshold, COMPUTED here with code; otherwise UNFINISHED
Gap:             what still has to be proved to use it
```

### Suggested lanes (to avoid five seats bringing the same paper)

- **GPT:** Dish B (effective equidistribution and the Malikiosis–Santos–Schymura line).
- **Astra:** Dish A (Bohr sets and gap/measure versions; Kravitz; Tao's gap bound).
- **GLM:** Dish D (random runners; Poisson heuristics; why the threshold rule caps at 30/33).
- **Kimi:** Dish C (tight instances; extremal structure; the missing 6).
- **Other seats:** Dish E (finite fields and view-obstruction over ℤ_p), or any dish you think we are missing.

Lanes are suggestions. A strong ingredient for another dish is welcome.

### Last question (one line)

If you could cook only one dish with what you found, which one, and why?

----- END PACKET -----

Chair's process after replies:
1. Check every READ item against the source.
2. Drop MEMORY items unless the chair can verify them.
3. Test each surviving ingredient against L16, L17 and R16 Q1.
4. Write note 70: "what we can cook".

Nothing goes into the ledger without Tuzi's approval.
