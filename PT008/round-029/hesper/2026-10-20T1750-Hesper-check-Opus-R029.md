# Hesper check · Opus R029 (sha256 221d2ce3…) · facts only, CHECKED, not proof
Code: hesper/chk_opus_r029.py (exact Fractions; T4 = certified code base.py).
1. Algebra of hypotheses: a/b>=4/5 <=> b<=5a/4; 8/(5c)<=4/(15b) <=> c>=6b; 1/c<=4/(15b) <=> c>=15b/4; 2/(5d)<=3/(10c) <=> d>=4c/3; 5/6+2/15=29/30; 1/3-2/15=1/5. All MATCH.
2. Random rational quadruples (num<=10^4, den<=300) plus near-boundary samples; checked 0<t<1/a and min||vt||>=1/5:
   FW-SO (k=3, t=T4(b,c,d)) applicable 27,295, fails 0; R2 applicable 2,613, fails 0; R2' applicable 24,231, fails 0.
   R2' implemented by Hesper from its text (start of longer c-safe segment, then the R2 d-shift); Opus did not give code.
3. Integer quadruples 1<=a<b<c<d<=24 in chair remaining region (5,890): sequential cover FW-SO 177, R2 120, t=k/(5a) (k=1..4) 3,716, uncovered 1,877; examples (1,2,3,5), (1,2,3,10), (1,2,4,5). MATCH except: Opus's "3,904" is the k/(5a) family counted alone (overlapping); sequential count is 3,716 (177+120+3,716+1,877=5,890).
4. Side fact: T4(b,c,d) tried on all 5,890 without the b<=5a/4 hypothesis works on 1,008 (not a lemma; hypothesis not removable from FW-SO as stated).
5. Not checked: R2'/FW-SO general-k proof steps by hand; NEW COVERAGE vs certified F5 rules.
