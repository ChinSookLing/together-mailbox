# Hesper check · R032 1/4 Opus (reply sha256 2330ee7ddbae5339f69c9b45bab12b1c2801356480c91e79d1aa7952c7b94e1f)
Facts only, exact Fractions (hesper/copus.py, fwcert.py). CHECKED, not proof. Courier promotes nothing.

1. PCL-T: for V_k=(1..k), δ=1/(k+2), k=2..8: exact bad set on u∈(0,k(k+1)] is (0,1/(k+1)) — MATCH (Opus checked k=2..6). Four lock points 1/(k+1), k/(k+1), 1/(k+2), (k+1)/(k+2) all in S; interval [1/(k+1)−h,1/(k+1)+h], h=1/(k(k+1)(k+2)), lies inside a safe component — MATCH for k=2..8.
2. LOCK: 183 random rational triples (δ=1/5) with nonempty exact bad set; for 19 points in each bad interval and every pair (τ,mτ) of component endpoints with m∈{2,3,4}, ‖uτ‖<δ/m held: 15,124 checks, 0 violations. (A first coarse probe using sampled points as a "bad" test gave 4 false alarms; redone with exact B, 0.)
3. PCL-2 "30 not sealed" examples (1,3,4),(1,4,5),(1,8,9),(1,9,10),(1,13,14),(2,5,7): exact B = (0,1/4),(0,2/7),(0,1/4),(0,9/34),(0,1/4),(0,5/9); each B∩(b,∞)=∅ — MATCH Opus's statement that they are not FW₄ counterexamples. Hesper did not reproduce the 455/425/30 count.
4. Not checked: Opus's 13,497 witness runs; proofs of LOCK, PCL-T, PCL-2 (hand-read, no error found).
Status: all author PROOF CANDIDATE; no non-author review yet (supplement sent to DeepSeek and Kimi).
