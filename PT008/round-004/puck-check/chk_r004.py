import random, math, sys
from fractions import Fraction as F
from math import floor, ceil, gcd
def nd(x): return abs(x-round(x)) if False else min(x-floor(x), ceil(x)-x)
def g(A,t): return min(nd(a*t) for a in A)
def lcm(a,b): return a*b//gcd(a,b)
def period(A):
    D=1
    for a in A: D=lcm(D,F(a).denominator)
    return D   # a*D integer
def candidates(A,T):
    S=set()
    A=sorted(set(A))
    for a in A:
        for k in range(0,int(2*a*T)+2): 
            t=F(k)/(2*a)
            if t<=T: S.add(t)
    for i,a in enumerate(A):
        for b in A[i:]:
            for c in range(0,int((a+b)*T)+2):
                t=F(c)/(a+b)
                if t<=T:S.add(t)
            if b>a:
                for c in range(0,int((b-a)*T)+2):
                    t=F(c)/(b-a)
                    if t<=T:S.add(t)
    return sorted(S)
def local_maxima(A,T=None):
    A=sorted(set(A)); 
    if T is None: T=period(A)
    C=candidates(A,T)
    res=[]
    for i in range(1,len(C)-1):
        t=C[i]
        if t==0: continue
        l=(C[i-1]+t)/2; r=(t+C[i+1])/2
        gt=g(A,t)
        if gt>g(A,l) and gt>g(A,r): res.append(t)
    return res,T
def claimed(A,t):
    """return list of (a,b,p,q,v) satisfying T1' conds 1-3 at t"""
    out=[]
    for a in A:
        for b in A:
            c=(a+b)*t
            if c.denominator!=1: continue
            p=ceil(b*t-F(1,2)); 
            if not p<b*t: continue
            r=b*t-p
            q=int(c)-p
            assert q-a*t==r and 0<r<=F(1,2)
            if all(nd(e*t)>=r for e in A): out.append((a,b,p,q,r))
    return out
def claimed_points(A,T):
    A=sorted(set(A)); P=set()
    for a in A:
        for b in A:
            for c in range(1,int((a+b)*T)+1): 
                t=F(c)/(a+b)
                if t<=T and claimed(A,t): P.add(t)
    return sorted(P)
def randset(rng,mode):
    m=rng.randint(1,4)
    if mode=='int': return sorted({F(rng.randint(1,12)) for _ in range(m)})
    D=rng.randint(2,5)
    return sorted({F(rng.randint(1,10*D),D) for _ in range(m)})
log=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); log.append(s)
# ---- 1 T1'
def t1(seed,N):
    rng=random.Random(seed); stats=dict(sets=0,lm=0,notclaimed=[],claimedviol=[],nonmax=[],strictfail=0)
    for _ in range(N):
        A=randset(rng,rng.choice(['int','rat']))
        if period(A)>12: continue
        stats['sets']+=1
        L,T=local_maxima(A)
        Ls=set(L); stats['lm']+=len(L)
        CP=set(claimed_points(A,T))
        for t in L:
            if t not in CP: stats['notclaimed'].append((A,t))
        for t in CP:
            if t not in Ls: stats['nonmax'].append((A,t))
        for t in L:
            cl=claimed(A,t)
            for (a,b,p,q,v) in cl:
                if g(A,t)!=v: stats['claimedviol'].append((A,t,'g!=v'))
    return stats
# ---- B3
def b3():
    A=[F(1),F(2),F(3)];t=F(1,3)
    return nd(F(1)*t),nd(2*t),g(A,t), t in local_maxima(A)[0]
# ---- B5 formula
def Fform(a,b):
    a,b=min(a,b),max(a,b)
    return F(ceil((a+b)/(3*a)))/(a+b)
def b5(seed,N):
    rng=random.Random(seed);fails=[];cnt=0
    for a in range(1,60):
        for b in range(a+1,60):
            cnt+=1;t=Fform(F(a),F(b))
            if g([F(a),F(b)],t)<F(1,3): fails.append((a,b))
    cint=cnt
    for _ in range(N):
        D=rng.randint(1,1000)
        a=F(rng.randint(1,10**6),D); b=F(rng.randint(1,10**6),rng.randint(1,1000))
        if a==b: continue
        cnt+=1;t=Fform(a,b)
        if g([a,b],t)<F(1,3): fails.append((a,b))
        # also check equality ||aF||=||bF||
        if nd(a*t)!=nd(b*t): fails.append(('eq',a,b))
    # tiny/huge ratios
    for _ in range(2000):
        a=F(rng.randint(1,10**6),10**6); b=a*F(rng.randint(1,10**6),rng.randint(1,10**3))
        if a==b: continue
        cnt+=1;t=Fform(a,b)
        if g([a,b],t)<F(1,3): fails.append((a,b))
    return cint,cnt,fails,Fform(F(1),F(4)),[Fform(F(1),F(2)),Fform(F(1),F(3))]
# ---- B1 max over interval = max(endpoints, T1' pts); bound
def b1(seed,N):
    rng=random.Random(seed);viol=[];bviol=[];cnt=0
    for _ in range(N):
        A=randset(rng,rng.choice(['int','rat']))
        if period(A)>10: continue
        T0=F(rng.randint(0,20),rng.randint(1,7)); T1=T0+F(rng.randint(1,30),rng.randint(1,7))
        Cs=[c for c in candidates(A,T1+1) if T0<=c<=T1]+[T0,T1]
        true_max=max(g(A,c) for c in set(Cs))   # g linear between candidates
        pts=[t for t in claimed_points(A,T1) if T0<=t<=T1]
        m=max([g(A,T0),g(A,T1)]+[g(A,t) for t in pts])
        cnt+=1
        if m!=true_max: viol.append((A,T0,T1,m,true_max))
        # count bound: #T1' pts in [0,T] <= 2*m*T*sum(a)  (m=|A|)
        T=T1; pts0=claimed_points(A,T); bound=2*len(A)*T*sum(A)
        if len(pts0)>bound: bviol.append((A,T,len(pts0),bound))
    return cnt,viol,bviol
# ---- B2
def b2(seed,N):
    rng=random.Random(seed);cnt=0;ne=0;viol=[]
    for _ in range(N):
        A=randset(rng,rng.choice(['int','rat']))
        if period(A)>12:continue
        n=len(A)+1;d=F(1,n)
        T=period(A);C=candidates(A,T)
        succ=[c for c in C if g(A,c)>=d]
        cnt+=1
        if succ:
            ne+=1
            pts=[t for t in claimed_points(A,T) if g(A,t)>=d]
            if not pts: viol.append((A,))
    return cnt,ne,viol
# ---- C2
def c2int(N=24):
    cnt=0;mm=0;md=0;both=0;mn=0;ex=[]
    for x in range(1,N+1):
        for y in range(x+1,N+1):
            for z in range(y+1,N+1):
                A=[F(x),F(y),F(z)];cnt+=1
                def ok(s): return any(g(A,F(c,s))>=F(1,4) for c in range(1,s))
                f1=not ok(x+z); f2=not ok(y+z); f3=not ok(x+y)
                mm+=f1;md+=f2;both+=(f1 and f2);mn+=f3
                if f1 and f2: ex.append((x,y,z))
                if f1: ex.append(('mm',x,y,z))
    return cnt,mm,md,both,mn,[e for e in ex if e[0]!='mm'],[e[1:] for e in ex if e[0]=='mm']
def c2rat(seed,N):
    rng=random.Random(seed);cnt=0;bad=[]
    for _ in range(N):
        D=rng.randint(2,6)
        xs=sorted({rng.randint(1,10*D) for _ in range(3)})
        if len(xs)<3: continue
        A=[F(v,D) for v in xs];cnt+=1
        # t=c/(s), s in {x+z,y+z}; period D => c up to s*D? t in (0,D]
        okk=False
        for s in (A[0]+A[2],A[1]+A[2]):
            for c in range(1,int(s*D)+1):
                if g(A,c/s)>=F(1,4): okk=True;break
            if okk:break
        if not okk: bad.append(A)
    return cnt,bad
# ---- B4 {1,sqrt2}
def b4():
    # convergents p/q of sqrt2 with p,q odd : m=q odd ; t=m/2 ; ||t||=1/2 ; ||sqrt2 t||=1/2-|sqrt2 m-p|/2 (p odd)
    out=[];p,q=1,1
    for _ in range(12):
        p,q=p+2*q,p+q
        if p%2==1 and q%2==1:
            # |sqrt2 q - p| = |2q^2-p^2|/(sqrt2 q+p) <= 1/(2p)
            err_ub=F(1,2*p)
            out.append((q,p,2*q*q-p*p,'g>=',F(1,2)-err_ub/2))
    return out
if __name__=='__main__':
    P('# chk.py output');
    for seed in (1,2,3):
        s=t1(seed,150)
        P('T1prime seed',seed,'sets',s['sets'],'localmax',s['lm'],'notclaimed',len(s['notclaimed']),s['notclaimed'][:3],'claimed-but-not-max',len(s['nonmax']),s['nonmax'][:3],'g!=v',len(s['claimedviol']))
    P('B3',b3())
    r=b5(7,20000); P('B5 int pairs',r[0],'total tested',r[1],'fails',r[2][:5],len(r[2]),'F(1,4)=',r[3],'F(1,2),F(1,3)=',r[4])
    for seed in (1,2):
        P('B1 seed',seed,b1(seed,150)[0:1],'maxviol',b1(seed,150)[1][:3],'boundviol',b1(seed,150)[2][:3])
    for seed in (1,2):
        P('B2 seed',seed,b2(seed,200))
    r=c2int(); P('C2 int 1..24 triples',r[0],'fail(min,max)',r[1],'fail(mid,max)',r[2],'both',r[3],'fail(min,mid)',r[4],'both-list',r[5],'minmax fails',r[6])
    P('C2 rat seed1',c2rat(1,300)[0],c2rat(1,300)[1][:5])
    P('B4 convergents',b4()[:5])
    open('output.txt','w').write('\n'.join(log))
