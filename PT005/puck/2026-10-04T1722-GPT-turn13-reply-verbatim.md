SEAT: GPT · REPLY_TO: wall lines 1–45.

SUMMARY  
**IDEA:** replace speed-first row generation by a dual **minimal-cover search on time classes**, then close the minimal supports to all 15-multisets.  
**FACT:** at \(p=239\), \(n=119\), \(m_{14}=15\), \(m_{15}=14\), hence \(14m_{14}=15m_{15}=210\): the two problems have exactly the same total incidence budget.  
**FACT:** a first-coverer partition makes the dual recursion exhaustive without duplicate search paths; translation canonicalisation then gives one unit-orbit representative.  
**ESTIMATE:** the core K=15/K=14 search ratio should become much closer to 1 than 3.65; the decisive test is an exact row-for-row comparison at \(p=239\).

### 1. Concrete reorganisation

**IDEA — “minimal core first, multiplicities last”.**

Work in the supplied discrete-log model
\[
G=\mathbf Z_n,\qquad B_c=c+S,
\]
where a shift \(c\) is a speed class and \(B_c\) is the set of time classes it covers.

Do **not** build a 15-multiset of speed classes directly.

Instead:

1. enumerate every **inclusion-minimal covering support**
   \[
   M\subseteq G,\qquad |M|\le15,\qquad \bigcup_{c\in M}B_c=G;
   \]
2. from those minimal covers generate every covering support \(C\), \(|C|\le15\), by adding arbitrary shifts;
3. only then generate every positive multiplicity vector on \(C\) whose sum is 15.

Coverage is tested only in step 1. Multiplicity never enters the covering search.

That is the organisational change.

---

### 2. The dual recursion

**FACT:** for a time class \(t\), the shifts that cover it are
\[
D(t)=\{c:t\in B_c\}=t-S,
\]
so \(|D(t)|=m\).

Normalize initially by demanding \(0\in M\). Every nonempty translation orbit has such a normalization.

A recursion state is

\[
(A,F),
\]

where \(A\) is the selected support and \(F\) is a set of shifts forbidden by the duplicate-elimination rule below.

Let
\[
U=G\setminus \bigcup_{c\in A}B_c.
\]

If \(U\neq\varnothing\), choose an uncovered time \(t\), preferably one minimizing
\[
|D(t)\setminus(A\cup F)|.
\]

Order its admissible coverers
\[
c_1<c_2<\cdots<c_r.
\]

Branch as

\[
(A\cup\{c_i\},\;F\cup\{c_1,\ldots,c_{i-1}\})
\]
for \(i=1,\ldots,r\).

I will call this the **first-coverer partition**.

#### Why that partition matters

**FACT:** every completion \(M^\ast\supseteq A\) must contain at least one member of \(D(t)\), because \(t\) is still uncovered.

Let \(c_i\) be the first member of the ordered list belonging to \(M^\ast\).

Then \(M^\ast\) survives **exactly** branch \(i\):

- \(c_i\) is selected there;
- all earlier \(c_j\) are forbidden, and by definition none belongs to \(M^\ast\);
- later coverers remain available.

So a support is not reached once for every selected block covering \(t\); it has a unique branch at this decision.

This is a different search tree from choosing the next speed class.

---

### 3. Cheap sound prunes

All of these preserve completeness.

**FACT — budget prune.**
If \(|A|>15\), stop.

**FACT — uncovered-capacity prune.**
If \(u=|U|\), at least
\[
\left\lceil\frac{u}{m}\right\rceil
\]
additional translates are required. Therefore stop when
\[
|A|+\left\lceil\frac{u}{m}\right\rceil>15.
\]

A stronger safe version can replace \(m\) by the largest currently attainable new-coverage counts.

**FACT — dead selected block prune.**
For \(c\in A\), define its present private set
\[
P_c=B_c\setminus\bigcup_{d\in A\setminus\{c\}}B_d.
\]

If \(P_c=\varnothing\), stop.

Reason: adding more blocks can only shrink \(P_c\), never create a private point. Therefore \(c\) can never belong to an inclusion-minimal final cover.

This prune is particularly natural in the minimal-cover formulation.

**FACT:** when \(U=\varnothing\), record \(A\). Because of the previous prune, every member has a private point, hence \(A\) is an inclusion-minimal cover.

Stop that branch immediately: no strict superset can itself be minimal.

---

### 4. Translation quotient

A minimal cover can be found under several choices of which member was moved to \(0\).

Use the canonical representative
\[
\kappa(C)=
\min_{c\in C}^{\mathrm{lex}}
\operatorname{sort}(C-c).
\]

**FACT:** it is enough to subtract elements of \(C\), not all \(n\) translations. A lexicographically least translated nonempty set must contain \(0\); otherwise subtracting its least element makes its first entry smaller.

Keep only \(C=\kappa(C)\).

The same rule works for a multiset, retaining multiplicities while translating.

---

## 5. Why this gives every improper row

Let \(R\) be any improper 15-multiset and let \(C=\operatorname{supp}(R)\).

**FACT:** coverage depends only on \(C\), so
\[
\bigcup_{c\in C} B_c=G.
\]

Every finite cover contains an inclusion-minimal subcover \(M\subseteq C\).

Translate \(R,C,M\) together so that some member of \(M\) is \(0\).

By the first-coverer induction above, the dual recursion contains a unique path leading to that anchored \(M\). Hence its translation orbit is recorded.

Now the closure step adds the elements of \(C\setminus M\), producing \(C\).

Finally the multiplicity step assigns exactly the multiplicities present in \(R\), since they are positive on \(C\) and sum to 15.

Canonicalising the resulting multiset therefore produces the unit orbit of \(R\).

So every improper row occurs.

Conversely, everything emitted covers \(G\), because it contains a recorded minimal cover. Thus there are no false improper rows.

**FACT: completeness is therefore independent of a private-time quota, of \(\tau\), and of whether a cover is “tight”.**

---

## 6. Why \(p=239\) is especially attractive

From the supplied formula:

\[
n=(239-1)/2=119.
\]

For 14 speeds,
\[
m_{14}=\left\lfloor\frac{238}{15}\right\rfloor=15.
\]

For 15 speeds,
\[
m_{15}=\left\lfloor\frac{238}{16}\right\rfloor=14.
\]

Therefore

\[
14m_{14}=14\cdot15=210,
\]
and
\[
15m_{15}=15\cdot14=210.
\]

**FACT:** the total incidence capacity is exactly identical.

The unavoidable excess incidence of any cover is consequently also identical:

\[
210-119=91.
\]

Meanwhile an uncovered time has only 14 possible covering shifts in the K=15 dual problem, versus 15 in K=14.

That is the main reason I think the measured 3.65 factor is largely an artefact of the present organisation rather than an intrinsic K=15 covering explosion.

**ESTIMATE:** a time-first minimal-cover tree should make K=14 and K=15 look much more alike at \(p=239\).

For \(p\le700\), \(n\le349\), so every coverage set occupies at most six 64-bit words. Thus union, private-set, uncovered-set and popcount operations are very small fixed bitset operations.

---

## 7. The particularly simple \(p=239\) closure

You report

\[
\tau_{15}(239)\ge14.
\]

Therefore there are no covering supports of size \(\le13\).

So every minimal core has size 14 or 15.

This makes the closure almost trivial.

### Minimal 15-cover
It directly gives one support-15 row: every multiplicity is 1.

### Minimal 14-cover
It gives:

- its support-14 rows: exactly one of its 14 classes is doubled;
- every support-15 cover obtained by adjoining one new class.

Canonicalise/deduplicate those support-15 extensions.

No enumeration over support sizes \(1,\ldots,13\) is needed.

**FACT:** for this prime, the entire reducible/multiplicity structure follows from the minimal 14-covers by one deterministic closure operation.

That is the version I would test first.

---

## 8. Why the 15/14 factor should fall

There are three separate reasons.

**FACT 1 — multiplicities disappear from the expensive search.**  
The core search sees only sets. Repeated speeds cannot create new coverage, so they are postponed until after every coverage decision is finished.

**FACT 2 — local branching does not grow from 14 to 15.**  
At \(p=239\), a chosen uncovered time has at most 14 possible new K=15 blocks, compared with 15 in K=14.

**FACT 3 — the total incidence budget is identical at \(p=239\).**  
Both problems have 210 block-time incidences available. Thus the dual covering constraints do not acquire the sort of 3.5× increase seen in the present node counts.

**ESTIMATE:** I would expect the **minimal-cover search** K=15/K=14 node and CPU ratio to be around \(1\)–\(2\), not 3.5–10.

There remains an unavoidable caveat:

**FACT:** the final K=15 answer contains 9,552,452 rows versus 1,342,843 for K=14. Any scheme that physically writes every row must pay an output cost.

Therefore my claim is not that total work becomes \(1\times\). The claim is that the expensive combinatorial generation should cease scaling with that row multiplicity.

The closure/multiplicity stage should be a tight streaming loop, not a search tree.

**INCOMPLETE:** I cannot prove from the supplied measurements alone that the full end-to-end ratio will be below 3.65. That is the empirical part of the proposal.

---

## 9. Cheap decisive test

I would make \(p=239\) the main test because its \(\tau\ge14\) result makes the closure especially simple.

### A. Implement only the dual minimal-cover engine

For both K=14 and K=15:

- construct \(S\) and all translates as bitsets;
- start from \(A=\{0\}\);
- use first-coverer branching;
- use the budget, capacity and dead-selected-block prunes;
- canonicalise completed minimal covers under translation.

Record separately:

- minimal-cover count by size;
- recursion nodes;
- CPU time.

No cascade is needed.

### B. Produce the full K=15 row file

At \(p=239\):

1. take every minimal 14-cover;
2. create its 14 doubled-class multisets;
3. add every possible fifteenth distinct class to obtain support-15 covers;
4. include minimal 15-covers;
5. canonicalise each multiset under translation;
6. external-sort and unique.

Encode a canonical row simply as 15 sorted shift indices.

With \(n=119\), one byte would even hold a shift, although a fixed `uint16` representation is less fragile.

### C. Compare against the author's output exactly

Canonicalise the author's 9,552,452 rows with the **same** translation rule and encoding.

External-sort both files and compare them byte-for-byte.

That checks exact equality of orbit representatives without relying on a probabilistic hash.

The required verdict is:

- no row present only on the author's side;
- no row present only on the dual side.

A preliminary \(p=131\) run is useful as a quick debugging check, but \(p=239\) is the meaningful benchmark.

---

## 10. Performance criterion

Run the same dual implementation for K=14 and K=15 at \(p=239\).

There are two ratios worth reporting.

### Core ratio
\[
\rho_{\rm core}
=
T_{\rm minimal}(15)/T_{\rm minimal}(14).
\]

**ESTIMATE:** I expect this below 2.

### Full-generation ratio
\[
\rho_{\rm full}
=
T_{\rm complete}(15)/T_{\rm complete}(14),
\]
including closure, multiplicity expansion, canonicalisation and output.

The proposal succeeds for the stated purpose only if this is materially below the measured 3.65.

---

## WHAT WOULD PROVE ME WRONG

1. **Soundness failure:** after exact translation canonicalisation, the dual generator misses even one author's row or emits even one extra row at \(p=239\). That falsifies either the implementation or a claimed completeness step; it must not be used for a gate.

2. **No structural saving:** if the K=15 minimal-cover recursion still requires roughly the present \(18.7\) billion-scale search effort, then changing to the time-class dual has not removed the source of the explosion.

3. **Bad 15/14 ratio:** if an exact same-code benchmark gives a minimal-core K=15/K=14 ratio near the present 3.5 or worse, my “same incidence geometry” performance argument is wrong.

4. **Output dominates:** even if the core ratio is good, if full exact generation at \(p=239\) remains at or above the present 3.65 ratio because canonicalisation/9.55M-row emission dominates, then this reorganisation does **not** solve the requested computational problem. It may still be mathematically cleaner, but that is not enough.

5. **Pathological minimal-core multiplicity at larger primes:** if primes \(240\)–\(700\) produce so many minimal covers that their number itself rises much faster from K=14 to K=15, then the hoped-for scaling improvement is not robust. The same benchmark should therefore be repeated at one larger prime after \(p=239\).

**ACCOUNT RECORDS READ:** none.  
**OTHER CHATS READ:** none.  
I used only the packet and the quoted manuscript text supplied in this turn.