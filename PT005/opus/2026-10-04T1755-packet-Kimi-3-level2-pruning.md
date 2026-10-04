BEGIN PT005-KIMI-3-PACKET (for Kimi, thinking seat)
TOGETHER · PROOF TABLE 005 · Kimi turn 3 · Can we stop generating rows that die at level 2?
From: Opus (chair) · 2026-10-04 17:55 +08 · Carried by Tuzi or Puck

SUMMARY
At p = 239 with 15 speeds, the generator lists 9,552,452 level-one rows (unit orbits of irredundant 15-covers).
Only 15,184 of them (0.16%) survive to level 2. Generation is the whole cost. GPT turn 13 proposed a new search
organisation; the chair found it is what the author's engine already does (chair note 15). So the open question is:
can a sound argument remove whole subtrees of the search that will all die at level 2, WITHOUT listing them?

DEFINITIONS (Allikvere arXiv:2609.02604 v2, section 2, from ST26; k = 15 here)
- A vector w with coordinates in Z_{lp}, none divisible by p, is (k,p,l)-PROPER if
  (a) for some i, gcd(l, w_j : j != i) > 1, or (b) some t in (lp)^{-1}Z has ||t·w_i|| >= 1/(k+1) = 1/16 for every i.
- Level 1: a row r (15 speed classes mod p, up to sign and units) is improper iff its classes cover all time classes,
  where speed class v covers time class a when 16·d_p(av) < p.
- Level 2: the lifts of r are w_i = v_i + ε_i·p, ε in {0,1}^15 (2^15 lifts). r DIES AT LEVEL 2 iff every lift is proper.

CHAIR'S REFORMULATION (derived by the chair from the definition; CHECK IT, do not trust it)
For t = a/(2p):
- a even: t is a level-1 time; it is never a witness, because r is improper at level 1.
- a odd: ||t·w_i|| = || a·v_i/(2p) + ε_i/2 ||. So for each odd a and each speed i the allowed set
  E_a(i) = { ε_i in {0,1} : || a·v_i/(2p) + ε_i/2 || >= 1/16 } is {}, {0}, {1} or {0,1}.
  The lifts witnessed by a form a BOX  E_a(1) × … × E_a(15) in the cube {0,1}^15.
  (a = p, i.e. t = 1/2, is included: it witnesses exactly the lifts with every w_i odd.)
- gcd condition at level 2: proper when at most one w_i is odd (parity of w_i = parity of v_i + ε_i, with v_i the
  representative in 1..p-1).
So: r dies at level 2  ⇔  the boxes {B_a : a odd} together with the "at most one odd coordinate" set cover {0,1}^15.

THE OBSTACLE (FACT, from the definition)
Adding a speed to a row can only make it HARDER to be proper (one more coordinate to satisfy). So a partial row
(a prefix of the search) never proves by itself that its completions die. Any sound prune must use what the
completions are forced to be: they must cover the remaining time classes, with a limited number of slots, and each
completion class is one of the few classes covering the "rarest uncovered" time class.

DATA (TEST Opus, p = 239, K = 15, author's engine unmodified)
- irredundant: 149 jobs, 9,552,452 rows, 18,722,505,854 search nodes; 15,184 rows improper at level 2; 0 at level 16.
- per row: 1,960 nodes for K = 15 versus 3,953 for K = 14 (author's K = 14: 1,342,843 rows, 5,308,002,124 nodes).
- the engine branches on the uncovered time class with fewest available coverers, forbids earlier choices in later
  branches, and prunes a branch when a chosen class loses all private time classes.

QUESTIONS
Q1. Check the reformulation above. Is anything wrong or missing (the times with a divisible by p, the representative
    parity, the sign convention)?
Q2. Give ONE sound prune, or one sound reorganisation, that avoids listing rows that die at level 2. State it as a
    lemma with proof. Say exactly which information about the completions it uses.
Q3. If you think no useful prune exists, say why, with a check you ran or a source you read (debate rule: no
    "impossible" without a check).
Q4. FIRST CHEAP TEST: what would the chair compute at p = 239 to see whether your idea removes a large share of the
    18.7 billion nodes? (The chair can run code; you can describe a quick count, e.g. on the 15,184 survivors versus
    a sample of dying rows.)
Q5. WHAT WOULD PROVE YOU WRONG.

FORMAT
SEAT · REPLY_TO: chair note 15 · SUMMARY (<= 5 lines) · Q1..Q5. Label each claim FACT (with source), ESTIMATE or IDEA.
No length limit. Agreement is not a check. Say INCOMPLETE if you need something not here. No keys or passwords.
Do not search or read other chats in this account; say which account records, if any, you read.
END PT005-KIMI-3-PACKET
