import random, math
from fractions import Fraction as F
random.seed(13)
def fl(x): return math.floor(x)
def fr(x): return x-fl(x)
def nd(x): return abs(x-math.floor(x+F(1,2)))   # distance to nearest int
def rnd(x): return math.floor(x+F(1,2))
def dist(u,t): return min(nd(x*t) for x in u)

def NW(u,N):
    d=F(1,N); k=len(u)
    lam=[None]*(k-1)
    lam[k-2]=(u[k-2]/u[k-1])*2*d
    for i in range(k-3,-1,-1): lam[i]=(u[i]/u[i+1])*(1+lam[i+1])
    if any(lam[i]>1-2*d for i in range(k-1)): return None,lam
    L=d/u[0]; intervals=[(L,L+lam[0]/u[0])]
    for i in range(1,k-1):
        X=u[i]*L
        if d<=fr(X)<=1-d-lam[i]: p=X
        else: p=math.ceil(X-d)+d
        L=p/u[i]; intervals.append((L,L+lam[i]/u[i]))
    X=u[k-1]*L; case2=False
    if nd(X)>=d: t=L
    else: t=(rnd(X)+d)/u[k-1]; case2=True
    return (t,intervals,case2),lam

def rand_speeds(n,spread):
    u=sorted(set(F(random.randint(1,spread*random.choice([1,3,7,20])),random.choice([1,1,2,3,5,7,10,13])) for _ in range(n)))
    return u

def test_nw():
    out={}
    for N in (5,6,7):
        tot=ok=fail=c2=nest=0; fails=[]
        tries=0
        while tot<30000 and tries<3000000:
            tries+=1
            u=rand_speeds(N-1,random.choice([5,20,100,1000]))
            if len(u)<N-1: continue
            res,lam=NW(u,N)
            if res is None: continue
            t,iv,case2=res; tot+=1; c2+=case2
            d=F(1,N)
            good=t>0 and dist(u,t)>=d
            # intervals nested and t in all
            nested=all(iv[i][0]>=iv[i-1][0] and iv[i][1]<=iv[i-1][1] for i in range(1,len(iv)))
            inall=all(a<=t<=b for a,b in iv)
            if not nested: nest+=1
            if not (good and inall):
                fail+=1; fails.append(u)
        out[N]=(tot,c2,fail,nest,fails[:3])
    return out

def test_nw5_conditions():
    bad=0;n=0
    for _ in range(200000):
        u=rand_speeds(4,random.choice([5,20,100]))
        if len(u)<4: continue
        a,b,c,d=u; n+=1
        _,lam=NW(u,5)
        lamok=all(x<=F(3,5) for x in lam)
        i_=b/c+2*b/(5*d)<=F(3,5); ii=3*b/(5*a)>=1+b/c+2*b/(5*d)
        if lamok!=(i_ and ii): bad+=1
    return n,bad

def nudge(d,ts):
    X=d*ts
    if nd(X)>=F(1,5): return ts
    k=rnd(X); e=X-k; sg=1 if e>=0 else -1
    return (k+F(sg,5))/d

def sln_setup(a,b,c,d):
    s=(b+c)/a; th=b/(b+c); mu=c/(5*d); ep=a/(5*d)
    return s,th,mu,ep,F(1,5)+mu,F(4,5)-mu

def sln1(a,b,c,d):
    s,th,mu,ep,Tl,Th=sln_setup(a,b,c,d)
    if not th<=F(3,5)-2*mu: return 'cond'
    if not s*(F(3,5)-2*ep)>=2+(F(2,5)+2*mu)/th: return 'cond'
    k0=math.ceil(s*(F(1,5)+ep)); x0=fr(k0*th)
    j=0 if Tl<=x0<=Th else math.ceil(fr(F(1,5)+mu-x0)/th)
    k=k0+j; ts=k/(b+c)
    return ts,k,s,ep
def slnodd(a,b,c,d):
    s,th,mu,ep,Tl,Th=sln_setup(a,b,c,d)
    k0=math.ceil(s*(F(1,5)+ep)); k=k0 if k0%2 else k0+1
    phi=1-2*th
    if not (k<=s*(F(4,5)-ep) and k*phi<=F(3,5)-2*mu): return 'cond'
    return k/(b+c),k,s,ep

def test_sln():
    res={}
    for name,fn in (('SLN1',sln1),('SLN-odd',slnodd)):
        tot=fail=0; fl_=[]; nudgebad=0; changed=0; crit_fail=0
        tries=0
        while tot<20000 and tries<3000000:
            tries+=1
            a=F(1); 
            den=random.choice([1,2,3,5,7,11])
            b=F(random.randint(1,400),den); c=F(random.randint(1,800),den); d=F(random.randint(1,1600),den)
            if not (a<b<c<d and 4*a<d<4*c): continue
            r=fn(a,b,c,d)
            if r=='cond': continue
            ts,k,s,ep=r; tot+=1
            # intermediate checks
            u=(a,b,c,d)
            t=nudge(d,ts)
            ok = t>0 and dist(u,t)>=F(1,5)
            if t!=ts: changed+=1
            if abs(t-ts)>F(1,5)/d: nudgebad+=1
            # loss bounds
            for x in (a,b,c):
                if abs(nd(x*t)-nd(x*ts))>x/(5*d): nudgebad+=1
            if not k<=s*(F(4,5)-ep): crit_fail+=1
            if not ok:
                fail+=1; fl_.append((a,b,c,d))
        res[name]=(tot,changed,fail,nudgebad,crit_fail,fl_[:3])
    return res

def inWL(a,b,c,d): return c<4*a and d>=2*a*c/(4*a-c)
def coords(a,b,c,d): return (b+c)/a,c/b,d/(b+c)
def inHB(a,b,c,d):
    s,r,w=coords(a,b,c,d)
    return F(15,8)<=s<=F(15,2) and (1<r<=F(8,7) or F(4)<=r<=F(13,2)) and F(4,5)<=w<=F(6,5)
def inC1(a,b,c,d):
    s,r,w=coords(a,b,c,d)
    return 4*a<d<4*c and F(15,8)<=s<=5 and 1<r<=F(8,7) and F(4,5)<=w<=F(9,5)
def C1t(a,b,c,d):
    s,r,w=coords(a,b,c,d)
    return 1/(b+c) if F(1,5)<=fr(w)<=F(4,5) else F(3,2)/(b+c)
def main():
    L=[]
    p=lambda *x: L.append(' '.join(str(i) for i in x))
    # (1)
    ex=NW([F(1),F(3),F(9),F(20)],5)[0]
    t=ex[0]; p("(1) worked example (1,3,9,20): t =",t,"distances",[float(nd(x*t)) for x in (1,3,9,20)],"PASS" if t==F(41,100) else "FAIL")
    r=test_nw()
    for N,(tot,c2,fail,nest,fs) in r.items(): p(f"NW N={N}: tested {tot} sets satisfying NW; case ||X_k||<δ occurred {c2}; failures {fail}; nesting violations {nest}",fs)
    n,bad=test_nw5_conditions(); p(f"NW-i/NW-ii vs lambda condition (N=5): {n} random sets, mismatches {bad}")
    # (2)
    for name,(tot,ch,fail,nb,cf,fs) in test_sln().items():
        p(f"{name}: tested {tot} points in Omega satisfying hypotheses; nudge changed t in {ch}; failures {fail}; nudge-bound violations {nb}; k<=s(4/5-eps) violated {cf}",fs)
    # (3)
    for u,tt,dd in (((1,30,60,80),F(2,9),None),((1,3,4,7),F(1,5),None)):
        a,b,c,d=map(F,u)
        s,r,w=coords(a,b,c,d); th=b/(b+c); mu=c/(5*d); ep=a/(5*d)
        ds=[nd(x*tt) for x in (a,b,c,d)]
        p(f"(3) {u}: t={tt} dists={[str(x) for x in ds]} min>=1/5: {min(ds)>=F(1,5)}; s={s} r={r} w={w} theta={th} mu={mu}")
        nwres,lam=NW([a,b,c,d],5)
        p("   TN(d<=4a)",d<=4*a,"LN(d>=4c)",d>=4*c,"Omega",4*a<d<4*c,"WL",inWL(a,b,c,d),"HB",inHB(a,b,c,d),"C1",inC1(a,b,c,d))
        p("   NW lambdas",[str(x) for x in lam],"NW applies",nwres is not None)
        p("   SLN1:", sln1(a,b,c,d) if sln1(a,b,c,d)=='cond' else 'applies', "(S1 θ<=3/5-2mu:",th<=F(3,5)-2*mu,", bound",F(3,5)-2*mu,")")
        r2=slnodd(a,b,c,d); k0=math.ceil(s*(F(1,5)+ep)); k=k0 if k0%2 else k0+1
        p("   SLN-odd:",'cond-fails' if r2=='cond' else 'applies',"k0",k0,"k",k,"k*phi",k*(1-2*th),"vs",F(3,5)-2*mu,"k<=s(4/5-eps)",k<=s*(F(4,5)-ep))
    a,b,c,d=map(F,(1,30,60,80)); th=b/(b+c)
    p("   LB(20) at (1,30,60,80): t=20/90 dists",[str(nd(x*F(2,9))) for x in (a,b,c,d)])
    # obstruction
    p("(3) obstruction: kθ with θ=1/3: ||k/3|| values", sorted({str(nd(F(k,3))) for k in range(0,60)}))
    p("   d<3c/2 <=> mu=c/(5d)>2/15 : check samples", all((c/(5*d)>F(2,15))==(d<F(3,2)*c) for c in (F(2),F(10),F(60)) for d in (F(3,2)*c-1,F(3,2)*c,F(3,2)*c+1)))
    p("   then 1/5+mu>1/3 for d<3c/2:", F(1,5)+F(2,15)==F(1,3))
    # C1 check: grid of exact points in C1 for rule sanity (extra)
    bad=tot=0
    for _ in range(30000):
        b=F(random.randint(1,300),random.choice([1,2,3,7])); rr=1+F(random.randint(1,1000),7000); c=b*rr
        a=F(1); s=(b+c)/a
        if not F(15,8)<=s<=5: continue
        w=F(random.randint(80,180),100); d=w*(b+c)
        if not (a<b<c<d and inC1(a,b,c,d)): continue
        if w in (F(4,5),) : pass
        tot+=1
        # chair endpoint: HB branch exactly for w in (4/5,6/5) ; per C1 text rule: frac(w) in [1/5,4/5] -> LB(1)
        t=C1t(a,b,c,d)
        if not (t>0 and dist((a,b,c,d),t)>=F(1,5)): bad+=1
    p(f"(extra) C1 v3 rule random exact points {tot}, failures {bad}")
    open('/workspace/r13/chk_trackA_out.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
main()
