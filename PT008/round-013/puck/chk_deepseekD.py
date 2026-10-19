import math, random
from fractions import Fraction as F
random.seed(4)
nd=lambda x: abs(x-math.floor(x+F(1,2)))
L=[]; p=lambda *x: L.append(' '.join(map(str,x)))
def dist(u,t): return min(nd(x*t) for x in u)
for n in (4,5,6):
    tot=fail=nudged=0; tries=0
    while tot<5000 and tries<2000000:
        tries+=1
        u=sorted(set(F(random.randint(1,40),random.choice([1,2,3,5])) for _ in range(n-1)))
        if len(u)<n-1: continue
        M=u[-1]
        q=random.choice([7,11,13,17,19,23,29,31]); t0=F(random.randint(1,q*12),q)*F(1,random.choice([1,2,3]))
        if t0<=0 or dist(u,t0)<F(1,n): continue
        w=n*M*(1+F(random.choice([0,0,1,5,20,100]),random.choice([1,3,7])))
        X=w*t0
        if nd(X)>=F(1,n+1): t=t0
        else:
            k=math.floor(X+F(1,2)); e=X-k; sg=1 if e>=0 else -1; t=(k+F(sg,n+1))/w; nudged+=1
            if abs(t-t0)>F(1,(n+1))/w: fail+=1
        tot+=1
        if not(t>0 and dist(u+[w],t)>=F(1,n+1)): fail+=1; p("FAIL",n,u,w,t0)
    p(f"R-L2 n={n}: {tot} random exact instances (t0 from rational grid, valid for 1/n), nudge applied {nudged}, failures {fail}")
# boundary w = nM exact
p("w=nM boundary included in tests (choice 0 of multiplier).")
# gap TN/L2
p("n=4: TN needs d<=n*a=4a; L2-extension needs w>=nM i.e. d>=4c; gap 4a<d<4c (matches Omega).")
# example
a,b,c,d=F(1),F(2),F(3),F(9,2)
p("(1,2,3,9/2): K5(i) c<=8a/3:",c<=F(8,3)*a,"| (ii) d>=4c:",d>=4*c,"| TN d<=4a:",d<=4*a,"| WL bound",2*a*c/(4*a-c),"d>=bound",d>=2*a*c/(4*a-c),"| Qwen (5c-2a)/2=",(5*c-2*a)/2,"d>",d>(5*c-2*a)/2)
s=(b+c)/a;r=c/b;w=d/(b+c);th=b/(b+c);mu=c/(5*d);ep=a/(5*d)
p("  s,r,w",s,r,w,"HB",F(15,8)<=s<=F(15,2) and (1<r<=F(8,7) or 4<=r<=F(13,2)) and F(4,5)<=w<=F(6,5),"C1",r<=F(8,7))
l3=2*c/(5*d);l2=(b/c)*(1+l3);l1=(a/b)*(1+l2)
p("  NW lambdas",[str(x) for x in (l1,l2,l3)],"NW applies",max(l1,l2,l3)<=F(3,5))
p("  SLN1 S1",th<=F(3,5)-2*mu,"guarantee",s*(F(3,5)-2*ep)>=2+(F(2,5)+2*mu)/th,"; SLN-odd: k0",math.ceil(s*(F(1,5)+ep)))
k0=math.ceil(s*(F(1,5)+ep));k=k0 if k0%2 else k0+1
p("  SLN-odd k",k,"k<=s(4/5-eps)",k<=s*(F(4,5)-ep),"kphi<=3/5-2mu",k*(1-2*th)<=F(3,5)-2*mu)
sol=[]
for q in range(1,41):
    for m in range(1,q*10):
        t=F(m,q)
        if t>5: break
        if dist((a,b,c,d),t)>=F(1,5): sol.append(t); break
    if sol: break
t=sol[0] if sol else None
p("  a solution (smallest-denominator grid search, for the example only):",t,[str(nd(x*t)) for x in (a,b,c,d)] if t else "")
# also simple known: LB(k)
for kk in range(1,40):
    t=F(kk)/(b+c)
    if dist((a,b,c,d),t)>=F(1,5): p("  LB(k) k=",kk,"t=",t); break
else: p("  LB(k) k<40: none")
open('chk_deepseekD_out.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
