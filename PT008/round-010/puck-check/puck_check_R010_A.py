# Puck exact-Fraction check of Opus PT-008 R010 Track A (HB half-lock box, C1 connected region + selection rule, obstruction, examples).
from fractions import Fraction as F
import math
def nd(x): f=x-math.floor(x); return min(f,1-f)
fifth=F(1,5); out=[]; fails=0; n=0
def ok(name,cond):
    global fails; out.append(("OK  " if cond else "FAIL")+" "+name); fails+=(not cond)
def speeds(s,r,w):  # a=1, b+c=s, c/b=r, d=w(b+c)
    b=s/(1+r); c=s*r/(1+r); return F(1),b,c,w*s
def works(v,t): return t>0 and all(nd(u*t)>=fifth for u in v)
def grid(lo,hi,N,open_lo=False):
    pts=[lo+(hi-lo)*F(i,N) for i in range(N+1)]
    return pts[1:] if open_lo else pts
# A3: HB t=3/(2(b+c)) on s in [15/8,15/2], r in (1,8/7] U [4,13/2], w in [4/5,6/5]
bad=[]; cnt=0
for s in grid(F(15,8),F(15,2),40):
    for r in grid(F(1),F(8,7),30,True)+grid(F(4),F(13,2),30):
        for w in grid(F(4,5),F(6,5),30):
            v=speeds(s,r,w); cnt+=1
            if not works(v,F(3,2)/(v[1]+v[2])): bad.append((s,r,w))
ok("A3 HB succeeds on exact grid incl. all closed edges (%d points), failures=%d"%(cnt,len(bad)),not bad)
# A4: C1 = Omega ∩ {15/8<=s<=5, 1<r<=8/7, 4/5<=w<=9/5}; rule: frac(w) in [1/5,4/5] -> t=1/(b+c), else t=3/(2(b+c))
bad=[]; cnt=0; inOm=0; hbused=0
for s in grid(F(15,8),F(5),50):
    for r in grid(F(1),F(8,7),40,True):
        for w in grid(F(4,5),F(9,5),100):
            v=speeds(s,r,w); a,b,c,d=v; cnt+=1
            om = 4*a<d<4*c and a<b<c<d
            inOm+=om
            fw=w-math.floor(w)
            t = 1/(b+c) if fifth<=fw<=4*fifth else (hbused:=hbused+1) and F(3,2)/(b+c)
            if not works(v,t): bad.append((s,r,w,om))
ok("A4 C1 selection rule succeeds on exact grid (%d points, %d inside Omega, HB branch used %d), failures=%d (rule checked on whole box, not only Omega)"%(cnt,inOm,hbused,len(bad)),not bad)
ok("A4 boundary w=6/5: frac=1/5 in A, both LB(1) and HB succeed at s=5,r=8/7",works(speeds(F(5),F(8,7),F(6,5)),1/(speeds(F(5),F(8,7),F(6,5))[1]+speeds(F(5),F(8,7),F(6,5))[2])) and works(speeds(F(5),F(8,7),F(6,5)),F(3,2)/(speeds(F(5),F(8,7),F(6,5))[1]+speeds(F(5),F(8,7),F(6,5))[2])))
# Omega coordinate form equivalence on random-ish grid
eqv=all(((4*1<w*s) == (F(4)/s<w)) and ((w*s<4*(s*r/(1+r))) == (w<4*r/(1+r))) for s in grid(F(1),F(10),20,True) for r in grid(F(1),F(7),20,True) for w in grid(F(1,10),F(4),20))
ok("Omega <=> 4/s < w < 4r/(1+r) (a=1 scaling)",eqv)
# A2 obstruction examples
for v,j in [((F(1),F(3),F(4),F(7)),1),((F(1),F(2),F(3),F(10)),2),((F(1),F(6,5),F(4),F(78,5)),3)]:
    a,b,c,d=v
    ok("A2 %s: d=%d(b+c), in Omega, ||d k/(b+c)||=0 for k=1..300"%([str(x) for x in v],j), d==j*(b+c) and 4*a<d<4*c and a<b<c<d and all(nd(d*F(k)/(b+c))==0 for k in range(1,301)))
v=(F(1),F(3),F(4),F(7)); ok("B2 (1,3,4,7) t=1/5 works, dists %s; tau=(b+c)t=7/5"%[str(nd(u*F(1,5))) for u in v], works(v,F(1,5)) and (v[1]+v[2])*F(1,5)==F(7,5))
ok("C4 (1,3,4,7) not in C1: s=7>5, r=4/3>8/7", F(7)>5 and F(4,3)>F(8,7))
v=(F(1),F(216,100),F(234,100),F(45,10)); a,b,c,d=v
ok("B4 example (1,2.16,2.34,4.5): s=9/2 r=13/12 w=1 in Omega; t=1/3 dists %s"%[str(nd(u*F(1,3))) for u in v], b+c==F(9,2) and c/b==F(13,12) and d/(b+c)==1 and 4*a<d<4*c and works(v,F(1,3)) and F(3,2)/(b+c)==F(1,3))
ok("D3 (1,3,4,7): t=1/5 locks a+c=5 and b+d=10", (v:=(1,3,4,7)) and 1+4==5 and 3+7==10 and F(1,5)==F(2,10))
out.append("FAILS %d"%fails); print("\n".join(out))
# Extra (Puck): is the LB obstruction set really only w in {1,2,3}? Test integer-speed points with w not an integer.
out2=[]
for v in [(3,5,11,24),(1,7,9,24)]:
    a,b,c,d=map(F,v); q=b+c; w=d/q
    allfail=all(not works((a,b,c,d),F(k)/q) for k in range(1,int(q)+1))  # integer speeds: period of t=k/q in k is q
    ts=[F(i,2000) for i in range(1,2001) if works((a,b,c,d),F(i,2000))]
    out2.append(("OK  " if (allfail and 4*a<d<4*c and a<b<c<d and w.denominator!=1) else "FAIL")+" EXTRA %s in Omega, w=%s NOT integer, every LB(k) t=k/%s fails (all k mod %s); a working time exists, e.g. t=%s"%(v,w,q,q,ts[0] if ts else None))
print("\n".join(out2))
