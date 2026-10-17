from fractions import Fraction as F
import random
def nd(x): return abs(x-round(x))
# B2 family
res=[]
for n in range(2,8):
  for j in (1,2,3,10,50):
    V=list(range(1,n)); M=n-1; d=F(1,n+1); h=F(1,n*(n+1)*M)
    t0=j+F(1,n)
    assert all(nd(u*t0)>=F(1,n) for u in V)
    q=(n-1)*(j*n+1)-1; w=q/t0
    assert w*t0==q and n*M-1<w<n*M or w<n*M
    # window fails: check dense grid + endpoint analytic
    lo,hi=t0-h,t0+h
    fail=all(nd(w*(lo+(hi-lo)*F(i,2000)))<d for i in range(2001))
    # analytic: |w|h<d
    an = w*h<d
    # also rest of old runners safe, so only new one fails
    res.append((n,j,float(w),float(n*M-w),fail,an))
print("B2 family rows",len(res),"all window-fail:",all(r[4] and r[5] for r in res))
print("all w<nM:",all(r[3]>0 for r in res))
# V={1}, w=4/3, window and global
t0=F(1);V=[1];n=2;d=F(1,3);h=F(1,2*3*1)
w=F(4,3)
print("t0 for V={1} j=1 :",F(3,2), "window", F(3,2)-h, F(3,2)+h)
# the Opus example t0=j+1/n=3/2, w=q/t0: q=(1)(2*1+1)-1=2 -> w=4/3
print("w",F(2)/F(3,2), "t=1/2 safe:",nd(F(1,2))>=F(1,3), nd(w*F(1,2))>=F(1,3))
# L2* random test with exact fractions
random.seed(7);tested=bad=0;strict=0
for _ in range(15000):
    n1=random.randint(1,6);n=n1+1;V=set()
    while len(V)<n1:V.add(random.choice([-1,1])*random.randint(1,12))
    V=list(V);M=max(abs(u) for u in V);d=F(1,n+1)
    cands=[F(random.randint(1,4000),random.randint(1,300)) for _ in range(300)]
    t0=next((t for t in cands if all(nd(u*t)>=F(1,n) for u in V)),None)
    if t0 is None: continue
    w=random.choice([-1,1])*random.randint(1,n*M*2)
    if w in V or w==0 or -w in V and False: continue
    rho=min((nd(u*t0)-d)/abs(u) for u in V); h=F(1,n*(n+1)*M)
    assert rho>=h
    if rho>h: strict+=1
    e=w*t0-round(w*t0)
    if abs(e)>=d: t1=t0
    else:
        k=round(w*t0); s=1 if e>0 else -1 if e<0 else 1; t1=(k+s*d)/w
        if (d-abs(e))/abs(w)>rho: continue   # condition (ii) not met
    tested+=1
    ok=t1>0 and all(nd(u*t1)>=d for u in V+[w])
    if not ok: bad+=1
print("L2* cond(ii) cases",tested,"fail",bad,"rho>h cases",strict)
