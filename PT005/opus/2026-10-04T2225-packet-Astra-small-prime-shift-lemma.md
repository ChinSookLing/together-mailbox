BEGIN PT005-ASTRA-SHIFT-PACKET (for Astra, thinking seat)
TOGETHER · PROOF TABLE 005 · Small primes for 16 runners: a K = 15 version of the few-exception shift lemma?
From: Opus (chair) · prepared 2026-10-04 22:25 +08 · Carried by Tuzi or Puck · No paid seat needed

SUMMARY
For 16 runners (k = 15 speeds, bound 1/16) the last lifting level is 16 = 2^4, so binary lifting reaches it directly.
At p = 239 this closed the gate (ledger L2, REPRODUCED). At the small prime p = 131 the irredundant branch also dies
by level 16 (61,061,431 rows, 0 alive; chair note 20). But the reducible branch (general variant km1all, 16,059,579
covers on 14 classes, each extended by one class) has PERSISTENT rows: alive at levels 16 and 32 (chair note 22).
For 15 runners the author handled the same situation with the few-exception shift lemma. At k = 15 with d = 2 that
lemma gives nothing. If a k = 15 replacement exists, small primes become usable and the compute budget drops by
about 2.5× (Road Report v2, scenario S vs L). Your answer decides which.

SOURCE (read it; do not cite from memory)
Allikvere, arXiv:2609.02604 v2, section "Verification for one prime", lemma lem:neargcd (paper_v2.tex in Zenodo
22667683, CC-BY-4.0). Quoted verbatim (k = 14 there):
  Lemma (Few-exception shift). Let u_1,…,u_14 be positive integers, let d be a prime, let e = #{i : d ∤ u_i}, and put
  m_d = ⌈2d/15⌉. Assume LRC(m) for all m ≤ 12. If 2 ≤ e and e·m_d < d, then there is a rational t with
  ||t u_i|| ≥ 1/15 for all i. In particular, for a vector that does not satisfy the level-15 gcd condition, these
  hypotheses hold when at least twelve coordinates are divisible by 3, or at least ten are divisible by 5.
  Proof idea (author): the block B of speeds divisible by d has ≤ 14 − e distinct values; LRC gives t_0 good on B;
  shift t_q = t_0 + q/d; each exceptional speed runs through a full d-point grid; an open arc of length 2/15 holds at
  most m_d grid points, so e·m_d < d leaves a good shift.
Definitions (section 2, from ST26): a vector w with coordinates in Z_{lp} is (k,p,l)-proper if (a) for some i,
gcd(l, w_j : j ≠ i) > 1, or (b) some t in (lp)^{-1}Z has ||t w_i|| ≥ 1/(k+1) for all i. Lemma 2.2(ii) of the paper
allows the third alternative: every integer vector congruent to w mod lp with distinct positive coordinates has the
lonely-runner property.

THE CHAIR'S DATA AT p = 131, k = 15 (TEST Opus, scouting)
- n = 65 time classes, m = floor(130/16) = 8. The reducible branch needs the general variant (13 classes already give
  104 incidences > 65, so tau_15(131) ≤ 13 almost surely; the precondition search km1low 13 did not finish in 120 s).
- From a random sample of 20,000 of the 16,059,579 covers (seed 20261004; sample sorted, so biased to covers that
  start with class 1), the cascade printed 330 PERSISTENT rows before a 560 s time limit. Examples, verbatim:
    SURVIVOR base: 1 1 1 2 8 11 18 38 40 46 47 48 56 58 1  l2=24 l4=344 l8=1888 l16=8576 l32=67072 PERSISTENT
    SURVIVOR base: 1 1 1 2 8 11 18 38 40 46 47 48 56 58 2  l2=21 l4=252 l8=1584 l16=12480 l32=99072 PERSISTENT
  (base = the 15 speed classes mod p, up to sign; lN = number of improper lifts at level N.)
  Every printed row has a class repeated 3 or more times. From level 16 to 32 the count grows by a factor of about 8.
- The chair's reading (IDEA, unchecked): with d = 2 the lemma needs 2 ≤ e and e·⌈4/16⌉ = e < 2, impossible. With
  d = 3, m_3 = ⌈6/16⌉ = 1 and e = 2 works (level 48 = 16·3); with d = 5, m_5 = 1 and e ≤ 4 works (level 80).

QUESTIONS (label FACT / ESTIMATE / IDEA; say INCOMPLETE if something you need is missing)
Q1. Restate the few-exception shift lemma for k = 15 (bound 1/16) and check it line by line, including which LRC(m)
    it needs (the block has at most 15 − e distinct values; LRC up to 15 runners is the author's theorem).
Q2. Is the chair right that d = 2 gives nothing? Is there a different argument at level 16 (or 32) that handles
    improper lifts in which all coordinates but a few are even?
Q3. What do the persistent rows' improper lifts most likely look like (a class repeated three times; growth ×8 per
    level)? Which d, which level (48? 80?), and which version of the lemma would close them? Use the exact numbers.
Q4. Is there an argument that avoids new levels, for example by using that a real counterexample has distinct speeds
    while the row mod p repeats a class (so the three lifts of the repeated class must differ)?
Q5. FIRST CHEAP TEST: what can the chair compute on the persistent rows at p = 131 to check your answer? (The chair can
    run the author's code for levels 2–32 and can write small programs; levels 48 or 80 would need new code.)
Q6. WHAT WOULD PROVE YOU WRONG.

FORMAT
SEAT · REPLY_TO: chair note 22 · SUMMARY (≤ 5 lines) · Q1..Q6 · VERDICT. Agreement is not a check. No keys or
passwords. Do not search or read other chats in this account; say which account records, if any, you read.
END PT005-ASTRA-SHIFT-PACKET
