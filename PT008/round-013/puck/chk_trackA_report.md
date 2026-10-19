# R013 Puck independent check report (all exact fractions.Fraction)
Date 2026-10-19 SGT. Scripts: chk_trackA.py, chk_qwenB.py, chk_argonC.py, chk_deepseekD.py (raw outputs in chk_*_out.txt).
Opus file archived as NEAR-VERBATIM (condensed, not byte-exact), sha256 bba74e675a16c5590971bc4b5d75a234fd08fd45cbb099861b2b8389a62b32c7. Qwen and DeepSeek texts are digests (not verbatim); Argon text not saved.

## Track A (Opus, R013 1/4)
```
(1) worked example (1,3,9,20): t = 41/100 distances [0.41, 0.23, 0.31, 0.2] PASS
NW N=5: tested 30000 sets satisfying NW; case ||X_k||<δ occurred 11419; failures 0; nesting violations 0 []
NW N=6: tested 30000 sets satisfying NW; case ||X_k||<δ occurred 9571; failures 0; nesting violations 0 []
NW N=7: tested 30000 sets satisfying NW; case ||X_k||<δ occurred 8194; failures 0; nesting violations 0 []
NW-i/NW-ii vs lambda condition (N=5): 193397 random sets, mismatches 0
SLN1: tested 20000 points in Omega satisfying hypotheses; nudge changed t in 8028; failures 0; nudge-bound violations 0; k<=s(4/5-eps) violated 0 []
SLN-odd: tested 12567 points in Omega satisfying hypotheses; nudge changed t in 5046; failures 0; nudge-bound violations 0; k<=s(4/5-eps) violated 0 []
(3) (1, 30, 60, 80): t=2/9 dists=['2/9', '1/3', '1/3', '2/9'] min>=1/5: True; s=90 r=2 w=8/9 theta=1/3 mu=3/20
   TN(d<=4a) False LN(d>=4c) False Omega True WL False HB False C1 False
   NW lambdas ['11/200', '13/20', '3/10'] NW applies False
   SLN1: cond (S1 θ<=3/5-2mu: False , bound 3/10 )
   SLN-odd: cond-fails k0 19 k 19 k*phi 19/3 vs 3/10 k<=s(4/5-eps) True
(3) (1, 3, 4, 7): t=1/5 dists=['1/5', '2/5', '1/5', '2/5'] min>=1/5: True; s=7 r=4/3 w=1 theta=3/7 mu=4/35
   TN(d<=4a) False LN(d>=4c) False Omega True WL False HB False C1 False
   NW lambdas ['269/420', '129/140', '8/35'] NW applies False
   SLN1: cond (S1 θ<=3/5-2mu: False , bound 13/35 )
   SLN-odd: cond-fails k0 2 k 3 k*phi 3/7 vs 13/35 k<=s(4/5-eps) True
   LB(20) at (1,30,60,80): t=20/90 dists ['2/9', '1/3', '1/3', '2/9']
(3) obstruction: kθ with θ=1/3: ||k/3|| values ['0', '1/3']
   d<3c/2 <=> mu=c/(5d)>2/15 : check samples True
   then 1/5+mu>1/3 for d<3c/2: True
(extra) C1 v3 rule random exact points 266, failures 0
```
Verdicts:
- NW(N): PASS in tests (90000 sets N=5,6,7; the ||X_k||<δ branch exercised ~29000 times; t in every interval and nesting held every time). Proof steps (b),(c) re-read: no hole found. Hypothesis NW-i/NW-ii equals the lambda condition (0 mismatches in 193k). Worked example (1,3,9,20) t=41/100 PASS.
- SLN1 / SLN-odd: PASS in tests (20000 / 12567 points, 0 failures). Nudge shift <= 1/(5d), per-speed loss <= u/(5d) held (0 violations). Tests are random, not a proof.
- Gap examples: both solutions correct. Neither is covered by TN, LN, WL, HB, C1, NW, SLN1 or SLN-odd as the rules are stated (hypotheses checked exactly). WL does not cover (1,3,4,7) since c=4a is not < 4a. The claim that the sufficient guarantee fails is correct. Note: SLN1 criterion version (k*<=s(4/5-eps)) was not tested beyond the guarantee condition.
- Obstruction §5: arithmetic PASS (||k/3|| in {0,1/3}; d<3c/2 <=> mu>2/15; 1/5+mu>1/3). LB(20) works at (1,30,60,80). It excludes only the margin-mu-then-nudge family.

## Track B (Qwen, R013 2/4; digest only)
```
Qwen B claim t=2/(a+d): 79149 exact points (closed region, 52813 at endpoints) failures 0 []
(3, 5, 10, 25): t=2/(a+d)=1/14 dists=['3/14', '5/14', '2/7', '3/14'] min=3/14; t matches claim: True; in open region True closed True; c<4a True
(3, 5, 10, 27): t=2/(a+d)=1/15 dists=['1/5', '1/3', '1/3', '1/5'] min=1/5; t matches claim: True; in open region False closed True; c<4a True
(3, 5, 10, 22): t=2/(a+d)=2/25 dists=['6/25', '2/5', '1/5', '6/25'] min=1/5; t matches claim: True; in open region False closed True; c<4a True
(1, 3, 4, 5): t=2/(a+d)=1/3 dists=['1/3', '0', '1/3', '1/3'] min=0; t matches claim: False; in open region False closed False; c<4a False
(3,5,10,25) coverage: TN d<=4a False | LN d>=4c False | K5 c<=8a/3 False | WL needs d>= 30 False | HB r= 2 False s,w 5 5/3 | C1 r>8/7 True
§7: WL bound 2ac/(4a-c)<=9a iff c<=36a/11 (random exact): True ; for 36a/11<c<4a bound>9a>=d so outside WL
a=1,c=3.7: d range 33/4 9 nonempty True
```
Verdicts: region claim PASS in 79149 exact points incl. 52813 endpoints (closed form). Closed endpoints (3,5,10,27),(3,5,10,22) give min exactly 1/5. Non-coverage table for (3,5,10,25) confirmed. §7 WL claim confirmed (c<=36a/11 iff WL bound<=9a). Note: (1,3,4,5) is NOT covered by t=2/(a+d) (c=4a is outside c<4a; t=1/3 gives ||bt||=0). Qwen's t=4/9 is a separate solution: distances 4/9,1/3,2/9,2/9, min 2/9, PASS. Qwen's DISPROVED/NOT ESTABLISHED statements about R011/R012 not re-checked here.

## Track C (Argon, R013 3/4; digest only)
```
V= (Fraction(1, 1), Fraction(11, 10), Fraction(3, 1), Fraction(41, 10)) s= 41/10 r= 30/11 w= 1 theta= 11/41
TN d<=4a: False | LN d>=4c (4c=12): False | Omega 4a<d<4c: True
WL c<4a: True bound 2ac/(4a-c)= 6 d>=bound: False | K5 c<=8a/3: False
HB: s in [15/8,15/2] True r in set False w in [4/5,6/5] True | C1 r<=8/7: False
tL=1/5 dists ['1/5', '11/50', '2/5', '9/50'] X=dt_L= 41/50 0.82 ||X||= 9/50
nudge t=(k'+σ/5)/d: k'= 1 σ= -1 t= 8/41 =1.2/4.1: False dists [0.1951219512195122, 0.2146341463414634, 0.4146341463414634, 0.2] ||ct||= 0.4146341463414634 exact 17/41 fails c: False
T4 route t0=1/4 dists ['1/4', '11/40', '1/4', '1/40'] X= 41/40 ||X||= 1/40
  nudge from 1/4 gives t= 12/41 same as above: False min 0.12195121951219512
t=0.42 dists ['21/50', '231/500', '13/50', '139/500'] [0.42, 0.462, 0.26, 0.278] min>=1/5: True
NW(5) lambdas [1.3399852180339986, 0.4739837398373984, 0.2926829268292683] cond all<=3/5: False | NW-i True NW-ii False
SLN1 S1 theta<=3/5-2mu: True 0.2682926829268293 0.3073170731707317 | guarantee: False 2.06 4.581818181818182
SLN-odd k0 2 k 3 k<=s(4/5-eps) True k*phi<=3/5-2mu False 1.3902439024390243 0.3073170731707317
Qwen B region: c<4a True | max(4a,(5c-2a)/2)= 13/2 d= 41/10 in: False
V in Opus gap G (not covered by NW, SLN1 guarantee, SLN-odd, WL, HB, C1; and in Omega?): c>=4a? False -> R requires (c>=4a) or (c<4a and d<2ac/(4a-c)): True ; in Omega: True
LB(k) k<=59 solutions: NONE (first k with all four >=1/5)
anchor a+b tau= 5/4 t= 25/42 min 0.21428571428571427
anchor a+c tau= 7/4 t= 7/16 min 0.20625
anchor a+d tau= 11/4 t= 55/102 min 0.2107843137254902
anchor b+c tau= 7/4 t= 35/82 min 0.25
anchor b+d tau= 9/4 t= 45/104 min 0.22596153846153846
anchor c+d tau= 3 t= 30/71 min 0.2676056338028169
```
Verdicts: V=(1,11/10,3,41/10) is outside TN, LN, WL, K5, HB, C1, NW, SLN1 guarantee, SLN-odd, and Qwen's region; so V lies in Opus's R (it is not covered by anything that is stated). t=0.42 works exactly (0.42,0.462,0.26,0.278) PASS. Several simple anchors also work (e.g. b+c with tau=7/4: t=35/82, min 1/4); plain LB(k), k<60, has no solution. DISCREPANCY: Argon says the nudge from t_L=1/5 AND the T4 route (t0=1/4) both give t=1.2/4.1 with ||ct||=0.122. Exactly: the sign rule from t_L=1/5 gives t=8/41 (round down), which fails at a (0.195<0.2), not c; t=12/41=1.2/4.1 arises from the T4 route t0=1/4 (fails at c, 0.122). Both nudges fail, so the point (V is a genuine counterexample to the nudge rules outside their hypotheses) stands, but the detail "same t" is wrong. These failures show that nudge rules fail outside hypotheses only; no certified lemma is contradicted.

## Track D (DeepSeek, R013 4/4; digest only, saved deepseek_trackD_digest.txt)
```
R-L2 n=4: 5000 random exact instances (t0 from rational grid, valid for 1/n), nudge applied 2085, failures 0
R-L2 n=5: 5000 random exact instances (t0 from rational grid, valid for 1/n), nudge applied 1604, failures 0
R-L2 n=6: 5000 random exact instances (t0 from rational grid, valid for 1/n), nudge applied 1408, failures 0
w=nM boundary included in tests (choice 0 of multiplier).
n=4: TN needs d<=n*a=4a; L2-extension needs w>=nM i.e. d>=4c; gap 4a<d<4c (matches Omega).
(1,2,3,9/2): K5(i) c<=8a/3: False | (ii) d>=4c: False | TN d<=4a: False | WL bound 6 d>=bound False | Qwen (5c-2a)/2= 13/2 d> False
  s,r,w 5 3/2 9/10 HB False C1 False
  NW lambdas ['83/90', '38/45', '4/15'] NW applies False
  SLN1 S1 False guarantee False ; SLN-odd: k0 2
  SLN-odd k 3 k<=s(4/5-eps) True kphi<=3/5-2mu False
  a solution (smallest-denominator grid search, for the example only): 3/4 ['1/4', '1/2', '1/4', '3/8']
  LB(k) k= 2 t= 2/5
```
Verdicts: R-L2 proof re-derived: shift <= 1/((n+1)w); old speed u<=M loses <= u/((n+1)w) <= 1/(n(n+1)); 1/n - 1/(n(n+1)) = 1/(n+1); t>0 since t0>=1/(nM)>1/((n+1)w). No hole. Tested 15000 exact instances (n=4,5,6, w>=nM incl. boundary), 0 failures. t0 inputs are random grid values, not F_n. Gap n*m<w<n*M at n=4 is 4a<d<4c as claimed. Example (1,2,3,9/2) is in no stated tool (WL bound 6, Qwen needs d>6.5, NW lambda2=38/45>3/5, SLN1/SLN-odd fail); solutions t=3/4 (distances 1/4,1/2,1/4,3/8) and LB(2) t=2/5.
