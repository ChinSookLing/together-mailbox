# Puck independent exact check, PT-008 R007 Qwen (Track B) and Argon (Track C). Fractions only, small sizes.
from fractions import Fraction as F
import random, math
def d(u): u=u-math.floor(u); return min(u,1-u)
def ok(a,b,c,t): return min(d(a*t),d(b*t),d(c*t))>=F(1,4)
def fails(name,gen,rule,n):
    bad=[];
    for _ in range(n):
        a,b,c=gen()
        t=rule(a,b,c)
        if t is None: continue
        if not ok(a,b,c,t): bad.append((a,b,c,t))
    print(f"{name}: tested {n}, failures {len(bad)}", ("first "+str(bad[0]) if bad else ""))
    return bad
random.seed(7)
def rq(lo,hi,den=97): 
    return F(random.randint(math.ceil(lo*den),math.floor(hi*den)),den)
# ---- Argon B.2 rule: x>=7/3, m=floor(x/2), k=ceil((m+1/4)(b+c)/b), t=k/(b+c)
def argon(a,b,c):
    x=b/a; m=math.floor(x/2); k=math.ceil((m+F(1,4))*(b+c)/b); return F(k)/(b+c)
def g_argon():
    a=F(1); b=rq(F(7,3),12,61);
    if random.random()<0.1: b=F(7,3)
    c=b+rq(F(1,61),200,61); return a,b,c
fails("Argon rule x>=7/3 (random)",g_argon,argon,20000)
# boundary-tight: c just above b, x near 7/3 and near even integers
cnt=0;bad=0
for bn in [F(7,3),F(7,3)+F(1,1000),F(3),F(4)-F(1,1000),F(4),F(6)-F(1,999),F(6),F(25,2)]:
    for cd in [F(1,10**6),F(1,1000),F(1,7),F(1),F(13,3),F(100),F(10**5,7)]:
        a,b,c=F(1),bn,bn+cd; cnt+=1; bad+= not ok(a,b,c,argon(a,b,c))
print("Argon rule boundary set:",cnt,"cases, failures",bad)
# Argon rule below 7/3: does it fail somewhere? (shows 7/3 is needed for this proof route)
ex=[(F(1),F(22,10),F(33,10)),(F(1),F(2),F(5)),(F(1),F(23,10),F(6))]
for a,b,c in ex: print("  Argon rule at x<7/3",(b,c),"ok" if ok(a,b,c,argon(a,b,c)) else "FAILS")
# ---- Argon's stated R1 bound 'y <= 8 - x/3' vs chair's c<=8a-b (y<=8-x)
a,b,c=F(1),F(3,2),F(7)   # 5x/3=2.5<=7<=8-x/3=7.5 but y>8-x=6.5
t=F(2)/(b+c); print("Argon R1 statement test (1,3/2,7): t=2/(b+c)",t,"dists",d(a*t),d(b*t),d(c*t),"OK" if ok(a,b,c,t) else "FAILS -> 8-x/3 is wrong, true bound 8-x")
# ---- R1 and S6-A as chair stated, random + boundary
def gR1():
    x=rq(1+F(1,97),F(3)-F(1,97)); lo=F(5,3)*x; hi=8-x
    if lo>hi: return F(1),F(2),F(4)
    y=lo+(hi-lo)*F(random.randint(0,1000),1000); return F(1),x,y
fails("R1 t=2/(b+c)",gR1,lambda a,b,c:(F(2)/(b+c)) if (F(5,3)*b<=c<=8*a-b and b<c) else None,20000)
def gS6():
    y=rq(3,11); lo=F(5,12)*(1+y); hi=min(F(7,12)*(1+y),y)
    x=lo+(hi-lo)*F(random.randint(0,1000),1000); return F(1),x,y
fails("S6-A t=3/(a+c)",gS6,lambda a,b,c:(F(3)/(a+c)) if (1<b<c) else None,20000)
# ---- Qwen N1: 1<y<=3, all 1<x<y, t=1/(a+c)
def gN1():
    y=rq(1+F(1,97),3); x=1+(y-1)*F(random.randint(1,999),1000); return F(1),x,y
fails("Qwen N1 t=1/(a+c)",gN1,lambda a,b,c:F(1)/(a+c),20000)
for x,y in [(F(1001,1000),F(3)),(F(2999,1000),F(3)),(F(3,2),F(3))]:
    print("  N1 boundary",(x,y),ok(F(1),x,y,F(1)/(1+y)))
# ---- Qwen N2 pair part: x in [5/3,7] => ||2/(1+x)||>=1/4
print("N2 pair part at x=5/3,3,7:",[d(F(2)/(1+x)) for x in (F(5,3),F(3),F(7))], " just below 5/3:",d(F(2)/(1+F(5,3)-F(1,1000))))
# Qwen N2 numerical example x=3.5,y=4
a,b,c=F(1),F(7,2),F(4); t=F(2)/(a+b); print("Qwen N2 example (1,7/2,4) t=2/(a+b): dists",d(a*t),d(b*t),d(c*t),"-> c distance",d(c*t),"<1/4" if d(c*t)<F(1,4) else ">=1/4")
# Qwen claim: N2 fills y=4 gap x in (35/12,4). Need ||8/(1+x)||>=1/4.
xs=[F(35,12)+F(i,1000) for i in range(1,1084)]
good=[x for x in xs if x<4 and d(F(8)/(1+x))>=F(1,4)]
print("N2 at y=4 on x in (35/12,4): covers x from",float(min(good)),"(exact boundary 25/7 =",25/7,")")
# Qwen G3 example (1.5,3.5) said not in R1
a,b,c=F(1),F(3,2),F(7,2); print("Qwen G3 point (1.5,3.5): in R1 range?",F(5,3)*b<=c<=8*a-b,"; t=2/(b+c) ok?",ok(a,b,c,F(2)/(b+c)),[d(v*F(2)/(b+c)) for v in (a,b,c)])
# Qwen C.3 example a=1,b=2,c=100,t=25/102
a,b,c=F(1),F(2),F(100); t=F(25,102); print("Qwen C.3 (1,2,100) t=25/102: dists",d(a*t),d(b*t),d(c*t),"ok" if ok(a,b,c,t) else "FAILS (a distance 25/102 < 1/4)")
# Qwen B.1 completion: bounded-k fails for all three pair families when y=(1+x)N
x=F(3,2)
for N in (10,50):
    y=(1+x)*N; a,b,c=F(1),x,y
    best=[k for fam in ((a+b),(a+c),(b+c)) for k in range(1,6) if ok(a,b,c,F(k)/fam)]
    print(f"  bounded k<=5, x=3/2,y=(1+x)*{N}: successes {best}")
