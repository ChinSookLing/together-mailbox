# Puck exact-Fraction checks of PT-008 R010 Track B (Qwen), Track C (Argon), Track D (LN reviews) numeric claims.
from fractions import Fraction as F
import math
def nd(x):  # distance to nearest integer, exact
    f=x-math.floor(x); return min(f,1-f)
fifth=F(1,5); out=[]; fails=0
def ok(name,cond):
    global fails
    out.append(("OK  " if cond else "FAIL")+" "+name); fails+= (not cond)
# ---- Track C (Argon) tuple (1,2,3,10)
a,b,c,d=F(1),F(2),F(3),F(10)
ok("C: corridor 4a<d<4c for (1,2,3,10)",4*a<d<4*c)
ok("C: t=k/(b+c)=k/5 gives ||dt||=0 for k=1..1000",all(nd(d*F(k,5))==0 for k in range(1,1001)))
good11=[k for k in range(1,12) if all(nd(u*F(k,11))>=fifth for u in (a,b,c,d))]
ok("C: t=k/11 (a+d lock) no k in 1..11 works (period 11) -> found %s"%good11, good11==[])
ok("C: valid k mod 11 for a is {3..8}",[k for k in range(11) if nd(F(k,11))>=fifth]==[3,4,5,6,7,8])
t0=F(2,5)
ok("C: k=2: ||b t0||=1/5 and ||c t0||=1/5 and ||d t0||=0",nd(b*t0)==fifth and nd(c*t0)==fifth and nd(d*t0)==0)
# dead nudge: for small delta of either sign, b or c drops below 1/5
ok("C: k=2 nudge dead for delta=+-1/10^j, j=2..8",all(min(nd(b*(t0+s*F(1,10**j))),nd(c*(t0+s*F(1,10**j))))<fifth for j in range(2,9) for s in (1,-1)))
t=F(23,100); ok("C: t=0.23 works, dists %s"%[str(nd(u*t)) for u in (a,b,c,d)],all(nd(u*t)>=fifth for u in (a,b,c,d)))
t=F(1,4); ok("C: t=1/4 works, dists %s"%[str(nd(u*t)) for u in (a,b,c,d)],all(nd(u*t)>=fifth for u in (a,b,c,d)))
# delta window for k=1: exact interval of delta in [0,1/10] with t=1/5+delta working (grid 1/3000)
win=[F(i,3000) for i in range(0,301) if all(nd(u*(F(1,5)+F(i,3000)))>=fifth for u in (a,b,c,d))]
ok("C: k=1 window min=%s max=%s (Argon says [0.02, 0.066..])"%(win[0],win[-1]), win[0]==F(1,50) and win[-1]==F(1,15))
# ---- Track B (Qwen)
for e in (F(1,2),F(1,10),F(1,3),F(65,100)):
    a,b,c,d=e,F(1),1+e,2+e
    ok("B: eps=%s ordering+corridor and d=b+c, ||d k/(b+c)||=0 k=1..500"%e, 0<a<b<c<d and 4*a<d<4*c and d==b+c and all(nd(d*F(k)/(b+c))==0 for k in range(1,501)))
ok("B: sec4 ||k/201||>=1/5 iff k mod 201 in 41..160",[k for k in range(201) if nd(F(k,201))>=fifth]==list(range(41,161)))
ok("B: sec3 lower bound q-3*ceil(2q/5) is negative for every q in 1..10000 (Hesper flag 2 confirmed, so 'q>=15 positive' does not follow)",all(q-3*math.ceil(2*q/5)<0 for q in range(1,10001)))
# search counterexamples to sec3 proposition: integers a<b<c<d, q=b+c>=15, d%q!=0, no k mod q with ||ka/q||,||kb/q||,||kd/q||>=1/5
cex=[]
for q in range(15,41):
    for b in range(1,(q+1)//2):
        c=q-b
        if not b<c: continue
        for a in range(1,b):
            for d in range(c+1,4*q+1):
                if d%q==0: continue
                if math.gcd(math.gcd(a,b),math.gcd(c,d))!=1: continue
                if not any(all(nd(F(k*u,q))>=fifth for u in (a,b,c,d)) for k in range(1,q)):
                    cex.append((a,b,c,d)); break
            if len(cex)>=5: break
        if len(cex)>=5: break
    if len(cex)>=5: break
out.append("INFO B: sec3 proposition search q=15..40 (integer speeds, gcd 1, d%%q!=0, d<=4q): first counterexamples (no k works for lock t=k/(b+c)) = %s"%cex)
# ---- Track D: LN worst-case boundary d=4c, nudge 1/(5d): loss c/(5d)=1/20
for c in (F(1),F(7,3),F(10)):
    d=4*c; ok("D: d=4c loss c*(1/(5d))=1/20 at c=%s"%c, c*F(1,5)/d==F(1,20))
out.append("FAILS %d"%fails)
print("\n".join(out))
