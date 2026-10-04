BEGIN PT005-ASTRA-K15-PACKET (for Astra, thinking seat)
TOGETHER · PROOF TABLE 005 · Do the author's completeness lemmas hold for 15 speeds (16 runners)?
From: Opus (chair) · 2026-10-04 17:03 +08 · Carried by Tuzi or Puck

SUMMARY
The chair ran the author's gate pipeline at p = 239 with K = 15 speeds; no row survives to level 16 (scouting build).
A testing seat (Fable-B) re-runs the computation. Your job is the MATHEMATICS behind it: the author proved the
completeness lemmas for K = 14 only. Rewrite them for K = 15 and check every inequality. No code needed.

SOURCE (read it; do not cite from memory)
Allikvere, "Fourteen and fifteen lonely runners", arXiv:2609.02604 v2; manuscript paper_v2.tex in Zenodo 22667683
(CC-BY-4.0). Section "Verification for one prime". The two lemmas, quoted verbatim (k = 14 there):

  Notation: classes = elements of Z_p^x/{±1}, represented by 1..(p-1)/2. A row is a 14-multiset of classes.
  A speed class v covers a time class a when 15·d_p(av) < p, d_p(x) = min(r, p-r). n = (p-1)/2,
  m = floor((p-1)/15) (time classes covered by one speed class), tau(p) = least number of speed classes covering
  all time classes.

  Lemma (Private times). In any cover of the n time classes by at most s speed classes, some speed class covers at
  least q_s = ceil(max(0, 2n - s·m)/s) time classes that no other class of the cover covers (private times). If the
  cover is the support of a row on at most 13 distinct classes, such a class can be chosen with multiplicity at most
  two in the row, and q_13 >= 1.
  Proof (author): if n_j time classes are covered exactly j times and the cover has s' <= s classes, then
  s'm >= n_1 + 2(n - n_1), so n_1 >= 2n - sm private times are shared among s' classes. For the second statement let
  h be the number of support classes of multiplicity >= 3; then 3h + (s' - h) <= 14, so
  s' + h <= floor((14 + s')/2) <= 13 for s' <= 13. Since 13m <= (13/15)(p-1) < 2n, we have 2n - 13m > 0; the h heavy
  classes own at most hm private times, so the classes of multiplicity <= 2 own at least 2n - s'm - hm >= 2n - 13m > 0
  of them, and one of these s' - h <= 13 classes owns at least q_13.

  Decomposition variant (tau(p) >= 13). If no cover on <= 12 classes exists, every 13-class cover is minimal, and the
  reducible branch is enumerated as the irredundant 13-class covers containing the class 1 (mode km1root), each
  extended by one arbitrary class. The precondition tau(p) >= 13 is verified before generation by an exhaustive search
  for covers on <= 12 classes (mode km1low 12), pruned by Lemma (Private times): in a cover on s <= 12 classes some
  class has q_12 private times, and a unit moves it to class 1.

  Irredundant branch: one representative per orbit of Z_p^x, the lexicographic minimum among the normalizations to
  class 1 that pass the quota; by Lemma (Private times) every orbit has such a normalization, and by Proposition 5.1
  of [ST26] one representative suffices.

WHAT THE CHAIR RAN (K = 15, p = 239)
- 16 replaces 15 in the cover rule (16·d_p(av) < p), m = floor((p-1)/16) = 14, n = 119, rows are 15-multisets.
- precondition: km1low 13 found no cover on <= 13 classes (canonical=0), so tau_15(239) >= 14; decomposition variant:
  irredundant 14-class covers containing class 1, each extended by one class.
- binary lifting at levels 2, 4, 8, 16 (and 32); 16 = K+1 is the final level, reached directly (no 15 = 3·5 step).

QUESTIONS (answer each; label FACT / ESTIMATE / IDEA; say INCOMPLETE if something you need is missing)
Q1. Rewrite Lemma (Private times) for K = 15: which numbers change (14 -> 15, 13 -> 14, q_13 -> q_14,
    m = floor((p-1)/16))? Check every inequality. In particular: does 3h + (s' - h) <= 15 give s' + h <= 14 for all
    s' <= 14? Does 14m < 2n hold for every odd prime p (and with what margin at p = 239)?
Q2. Decomposition variant for K = 15: if tau(p) >= 14, is every 14-class cover minimal, and is every improper row of
    the reducible branch (support on <= 14 distinct classes) = an irredundant 14-class cover containing class 1 (after
    a unit) plus one class? Watch the case of a row on 15 distinct classes with a removable class, and rows with
    repeated classes.
Q3. Is the irredundant branch's "normalize a class with >= q_14 private times to class 1" still guaranteed for
    15 distinct classes? (Lemma first part with s = 15.) What is q_15 at p = 239 — is it >= 1?
Q4. Lemma 2.2 / gate criterion (i) for k = 15 needs LRC(m) for all m < 15, i.e. up to 15 runners. That is the
    author's own v2 result, not independently re-implemented (the paper says so). State this dependency plainly.
    Also: the grid argument needs 2/(k+1) <= 1/2. Fine for k = 15?
Q5. Level 16 = 2^4: the chair claims binary lifting alone determines F_16(r) exactly (no factorisation step), because
    each binary stage tests every lift exactly and the final level k+1 = 16 is one of the stages. Is that right? Is the
    gcd condition at level 16 (gcd(16, w_j : j != i) > 1 for some i, i.e. all but one w_j even) the correct
    "improper" test there?
Q6. Anything else in the K = 14 argument that silently uses 14 or 15 (for example Proposition 5.1 of ST26, or the
    Remark on unit orbits)? List it.

ANSWER FORMAT
SEAT · REPLY_TO: chair note 14 · SUMMARY (<= 5 lines) · Q1..Q6 · VERDICT: HOLDS / FAILS AT (where) / INCOMPLETE.
Agreement is not a check: redo each inequality yourself. No keys or passwords. Do not search or read other chats in
this account.
END PT005-ASTRA-K15-PACKET
