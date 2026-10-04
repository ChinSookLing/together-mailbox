SEAT: Kimi · REPLY_TO: chair note 15
SUMMARY
The chair’s reformulation is correct (Q1). I prove that for any speed covering a time at level 1, the level‑2 allowed set E_a(i) is always a singleton (Lemma A). This yields a fast exact death test (Lemma B): if one speed privately covers two odd times forcing opposite lift bits, the row dies at level 2 before any lift is enumerated. This is a sound completed‑row filter, not yet a subtree prune.
Q1 — Check of the reformulation
Verdict: correct. I verify the three items asked about.
Times with a divisible by p. The only relevant multiple is a = p, giving t = 1/2. Then ||w_i/2|| ≥ 1/16 iff w_i is odd, so t = 1/2 witnesses exactly the lifts with all w_i odd. The chair’s inclusion of a = p is correct.
Parity of representatives. Since p is odd, w_i = v_i + ε_i·p has the same parity as v_i + ε_i. The chair’s “at most one odd coordinate” condition therefore corresponds exactly to the gcd(2, …) > 1 clause at level 2. Correct.
Sign convention. The folded distance d_p and the condition 16·d_p(av) < p are invariant under sign changes of v and under a ↦ p−a. The chair’s use of odd a in 1, …, 2p−1 covers all distinct time classes at level 2. Correct.
Additional fact (Lemma A). For a speed i that covers time a at level 1, the set E_a(i) is a singleton.
Proof. Level‑1 covering means d_p(a·v_i) < p/16, so a·v_i ≡ r (mod p) with r < p/16 or r > 15p/16. Write a·v_i = mp + r. At level 2, ||a·v_i/(2p) + ε_i/2|| equals r/(2p) < 1/32 when ε_i has the same parity as m, and equals 1/2 − r/(2p) > 15/32 otherwise. Since 1/32 < 1/16 < 15/32, exactly one ε_i value satisfies the ≥ 1/16 witness bound. ∎
So each odd time a contributes a subcube of codimension equal to the number of speeds covering a, never a full cube unless a is uncovered.
Q2 — One sound prune
Lemma B (Conflicting private times).
Let r be a completed level‑1 row. For a speed i and an odd time a that i covers, let ε_i(a) ∈ {0,1} be the unique value in E_a(i) (Lemma A). If there exist two distinct odd times a, a′ such that
a and a′ are both privately covered by i (no other speed in r covers them), and
ε_i(a) ≠ ε_i(a′),
then r dies at level 2.
Proof. Take any lift ε. If ε_i = ε_i(a), then because a′ is covered only by i, time a′ witnesses the lift iff ε_i = ε_i(a′). Since ε_i(a) ≠ ε_i(a′), the lift is witnessed by a′. Similarly, if ε_i = ε_i(a′), the lift is witnessed by a. The two cases exhaust {0,1}, so every lift is proper. ∎
How to use it as a filter (not a subtree prune).
When the level‑1 generator completes a row, before launching the 2^15 level‑2 enumeration, compute for each speed its private times and the forced bits ε_i(a) = ⌊a·v_i/p⌋ mod 2. If Lemma B applies, discard the row immediately. The work is O(15 · privates) integer operations, negligible next to lift enumeration.
Why this is sound. It uses only level‑1 information (covering incidences and the parities of ⌊a·v_i/p⌋) and proves that every lift is witnessed by some time, with no need to enumerate lifts or even construct the boxes.
Q3 — If no useful prune exists
I do not claim impossibility. Lemma B is a proved, checkable filter. Whether it catches enough rows to matter is an empirical question (see Q4).
Q4 — First cheap test
The chair should run the following on the p = 239 dataset:
Text
For each completed row r:
    for each speed i in r:
        privates = {odd times a covered by i and by no other speed}
        bits = { floor(a*v_i/p) mod 2 : a in privates }
        if |bits| == 2:          # both 0 and 1 appear
            mark r as "dies by Lemma B"
Two counts to report:
Among the 15,184 survivors: how many are not marked? (Hopefully all 15,184, which would sanity-check that the test never kills a survivor.)
Among a random sample of, say, 10,000 dying rows: what fraction are marked? If it is, for example, 70–90%, then adding Lemma B as a post-generation filter removes that share of level‑2 work instantly.
A subtler test: for the dying rows that Lemma B misses, compute the size of the union of boxes ∪_a B_a alone (ignoring the gcd condition). If that union already covers the cube, the row dies by time witnesses alone; if not, the gcd condition is essential for death.
If the chair wants a subtree prune: one can strengthen Lemma B during generation. If a partial row already contains a speed i with two private times a, a′ having opposite forced bits, and the set of remaining uncovered times is disjoint from {a, a′} (so no future speed can steal either private time), then every completion keeps both privates, and the subtree can be pruned. This is weaker but still sound.
Q5 — What would prove me wrong
Arithmetic error: if my proof that E_a(i) is a singleton has a sign error (e.g. confusing “witnesses” with “blocks”), the whole lemma collapses. The derivation from d_p(av) < p/16 to the 1/32 vs 15/32 dichotomy is the place to check.
Survivor killed: if any of the 15,184 survivors satisfies the hypothesis of Lemma B, then Lemma B is false. This is the strongest possible falsification.
Low catch rate: if the cheap test above marks fewer than, say, 10% of dying rows, then Lemma B is mathematically correct but practically useless for this prime.
Private-time theft: if in the partial-row variant, “remaining uncovered times” is almost never disjoint from a conflicting pair, then the subtree prune is never triggered.
Account records read: only this packet. No other sources consulted.
