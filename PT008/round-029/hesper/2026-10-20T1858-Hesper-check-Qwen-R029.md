# Hesper check · Qwen R029 (3 parts; combined sha256 18101266…) · facts only, CHECKED, not proof
Parts: p1 1fa263a2…, p2 aa55bd9e…, p3 5f9d042d…. Code: hesper/chk_qwen_r029.py (exact Fractions, certified T4).
1. §1 reduction: text says ||at||=x for x<1, so condition x in [1/5,1). Fact: ||x||=min(x,1-x); x=9/10 gives ||x||=1/10. Correct range is x in [1/5,4/5]. (For x=a*T4(b,c,d) on the 5,890 integer quads, x>4/5 occurs 0 times.)
2. §4.3 examples: T4(1,2,3)=1/4, ||5/4||=1/4; T4(1,2,4)=1/3, ||7/3||=1/3; T4(1,3,5)=1/4, ||11/4||=1/4; (1,2,3,4): ||4·1/4||=0. MATCH. (1,2,3,4) has d=4a, inside chair-covered region d<=4a, not the remaining region.
3. §3 shows the small-shift sufficient condition fails in the region; it does not show every shift fails (§5 wording "必失败" is stronger than §3 "可能失败").
4. Selector coverage (4 T4 candidates, plus t=k/(5a), k=1..4):
   integer quads <=24 in remaining region 5,890: T4 candidates alone 5,170; with k/(5a) 5,643; uncovered 247, e.g. (1,3,4,5), (1,3,8,15), (1,3,8,20).
   random rationals in region 20,000: uncovered 676.
   These quads still have a first-window safe time by the earlier boundary search (5,890/5,890), so they are selector misses, not FW₄ counterexamples.
