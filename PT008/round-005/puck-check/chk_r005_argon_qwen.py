from fractions import Fraction as F
from math import floor, gcd
import random, itertools
from functools import reduce
def nd(x):
    r = x - floor(x); return min(r, 1-r)
def g(t,A): return min(nd(u*t) for u in A)
def lcm(a,b): return a*b//gcd(a,b)
random.seed(5)
print("== (a) Argon V={2,4,15}, n=4, thr 1/4")
A=[2,4,15]
cands=set()
for s in A:
  for s2 in A:
    for m in range(0,s+s2+1):
      t=F(m,s+s2); cands.add(t%1)
for s in A:
  for m in range(0,2*s+1): cands.add(F(m,2*s)%1)
cands=sorted(cands)
best=max(g(t,A) for t in cands)
argmax=[t for t in cands if g(t,A)==best]
print("candidate-set max g =",best,"at",[str(t) for t in argmax])
for t in argmax: print("  t=",t,{u:str(nd(u*t)) for u in A})
N=reduce(lcm,[4,6,8,17,19,30,2,4,15*2]);print("grid N",N)
gb=F(0);am=[]
for j in range(N):
    t=F(j,N); v=g(t,A)
    if v>gb: gb=v;am=[t]
    elif v==gb: am.append(t)
print("fine-grid max",gb,"argmax",[str(x) for x in am])
print("max for {2,4}:",max(g(t,[2,4]) for t in cands), "argmax",[str(t) for t in cands if g(t,[2,4])==max(g(x,[2,4]) for x in cands)])
print("15 active at global maximizers?",[nd(15*t)==best for t in am])
succ=[t for t in cands if g(t,A)>=F(1,4)]
act=[t for t in succ if nd(15*t)==g(t,A)]
print("candidate success times (g>=1/4):",len(succ),"; with 15 active:",len(act))
print("  3/19:",g(F(3,19),A),{u:str(nd(u*F(3,19))) for u in A})
print("  some 15-active success times:",[str(t) for t in act[:8]], [str(g(t,A)) for t in act[:8]])
print("  max g among times where 15 active:",max(g(t,A) for t in cands if nd(15*t)==g(t,A)))
print("== (b) Qwen")
def f1(a,b,c): return F(1,2*c)
def f2(a,b,c): return F(1,4*a)
def ok(t,T): return g(t,T)>=F(1,4)
viol=[];cnt=0;c1=c2=both=either=0;tot=0
def test(a,b,c):
    global c1,c2,both,either,tot
    T=[a,b,c];tot+=1
    i1=c<=2*a; i2=(b<=3*a and c<=3*a)
    if i1 and not ok(f1(a,b,c),T): viol.append(("fam1",a,b,c))
    if i2 and not ok(f2(a,b,c),T): viol.append(("fam2",a,b,c))
    c1+=i1;c2+=i2;both+=(i1 and i2);either+=(i1 or i2)
for a,b,c in itertools.combinations(range(1,61),3): test(a,b,c)
print("integer triples a<b<c<=60:",tot,"fam1",c1,"fam2",c2,"both",both,"either",either,"coverage %.2f%%"%(100*either/tot),"violations",len(viol))
print("fam1 subset of fam2?", "yes" if c1==both else "no (fam1-only %d)"%(c1-both))
viol2=[];r=0
while r<300:
    xs=sorted(set(F(random.randint(1,60),random.randint(1,12)) for _ in range(3)))
    if len(xs)<3: continue
    a,b,c=xs;r+=1;T=xs
    if c<=2*a and not ok(f1(a,b,c),T): viol2.append(("fam1",a,b,c))
    if b<=3*a and c<=3*a and not ok(f2(a,b,c),T): viol2.append(("fam2",a,b,c))
print("300 random rational triples violations:",len(viol2),viol2[:3])
# also random rational triples forced into each family
v3=0
for _ in range(300):
    a=F(random.randint(1,40),random.randint(1,9)); b=a*(1+F(random.randint(1,200),100)); c=b*(1+F(random.randint(1,100),100))
    if c<=2*a and not ok(f1(a,b,c),[a,b,c]): v3+=1
    if c<=3*a and not ok(f2(a,b,c),[a,b,c]): v3+=1
print("300 targeted-in-family rational triples violations:",v3)
# boundary
print("boundary c=2a (1,1.5,2):",ok(f1(1,F(3,2),2),[1,F(3,2),2]),"b=c=3a (1,3,3 not strict) (1,2,3):",ok(f2(1,2,3),[1,2,3]),"(1,2.9,3):",ok(f2(1,F(29,10),3),[1,F(29,10),3]))
print("F(1,2,3): F(1,2)=",F(-(-3//3),3),"t=1/3 g=",g(F(1,3),[1,2,3]),"; t=1/4 g=",g(F(1,4),[1,2,3]))
for name,t in [("(a,b)",F(1,3)),("(a,c)",F(1,2)),("(b,c)",F(1,5))]: print(" pair",name,"t=",t,"g=",g(t,[1,2,3]),{u:str(nd(u*t)) for u in [1,2,3]})
print("Qwen UNFINISHED ex (1,4,7) t=3/8:",{u:str(nd(u*F(3,8))) for u in [1,4,7]},"g=",g(F(3,8),[1,4,7]))
print("(1,4,7) neither family:",not(7<=2) and not(4<=3))
# does any triple fail to have success at all? (exact candidate search, ints<=40)
bad=[]
for a,b,c in itertools.combinations(range(1,41),3):
    T=[a,b,c];best=max(g(F(m,s+s2),T) for s in T for s2 in T for m in range(s+s2+1))
    if best<F(1,4): bad.append((a,b,c))
print("integer triples<=40 with no success time:",len(bad))
