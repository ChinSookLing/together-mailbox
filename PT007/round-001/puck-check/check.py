from fractions import Fraction as F
import random, math
random.seed(7)
def nrm(x):
    r = x - math.floor(x); return min(r, 1-r)
def inS(V,t,d): return all(nrm(u*t)>=d for u in V)
def rr(den=12,mx=40):
    return F(random.randint(1,mx*den),den)*random.choice([1,-1])
def cands(V,d,T,S0=0):
    out=set()
    for u in V:
        a=abs(u); k=max(0,math.floor(S0*a)-1)
        while (k-d)/a<=T:
            for c in ((k+d)/a,(k-d)/a):
                if S0<=c<=T: out.add(c)
            k+=1
    return sorted(out)
def goodpts(V,d,T,S0=0):
    return [c for c in cands(V,d,T,S0) if inS(V,c,d)]
res={}
# B1
d=F(1,3)
pw=[(([1,2]),F(1,3)),(([1,3]),F(1,2)),(([2,3]),F(1,5))]
ok=all(inS([F(x) for x in V],t,d) for V,t in pw)
# triple: grid over [0,1] period 1 + candidates
trip=goodpts([F(1),F(2),F(3)],d,F(3))
grid=[F(i,3600) for i in range(3601)]
trip2=[t for t in grid if inS([F(1),F(2),F(3)],t,d)]
res['B1']=(ok,len(trip),len(trip2))
# B2
res['B2']=(inS([F(1)],F(1,2),F(1,2)), inS([F(1),F(2)],F(1,2),F(1,3)))
# A4
bad=0
for _ in range(20000):
    u=rr(); t0=F(random.randint(0,10000),random.randint(1,50)); 
    d1=nrm(u*t0)
    if d1==0: continue
    d2=F(random.randint(0,999),1000)*d1
    s=(d1-d2)/abs(u)*F(random.randint(-100,100),100)
    if nrm(u*(t0+s))<d2: bad+=1
res['A4_viol']=bad
# B3
viol=0;tests=0;fail_exist=0
for _ in range(300):
    m=random.randint(1,5)
    V=[rr(4,10) for _ in range(m)]
    dl=F(random.randint(1,99),100)/(2*m)
    T=2*dl*sum(1/abs(u) for u in V)/(1-2*m*dl)*F(101,100)
    # bad measure exact
    meas=0
    for u in V:
        a=abs(u);k=0;mu=0
        while (k-dl)/a<T:
            lo=max(F(0),(k-dl)/a);hi=min(T,(k+dl)/a);
            if hi>lo: mu+=hi-lo
            k+=1
        if mu>2*dl*T+2*dl/a: viol+=1
        meas+=mu
    if not meas<T: viol+=1
    tests+=1
    if not goodpts(V,dl,T): fail_exist+=1
res['B3']=(tests,viol,fail_exist)
# nudge
def nudge(t0,w,dp):
    w=abs(w);x=w*t0;k=round(x)
    if nrm(x)>=dp: return t0
    return (k+dp)/w if x>=k else (k-dp)/w
# B4
b4fail=0;b4n=0;x1fail=0;edge=0
for _ in range(6000):
    m=random.randint(1,6)
    V=[rr(random.choice([1,3,7,12]),random.choice([3,10,30])) for _ in range(m)]
    mx=max(abs(u) for u in V)
    g=goodpts(V,F(1,m+1),F(6))
    if not g: continue
    t0=random.choice(g[:3]+g[-3:]+g)  # includes boundary points
    mode=random.random()
    if mode<0.4: wa=(m+1)*mx; edge+=1
    else: wa=(m+1)*mx*(1+F(random.randint(0,300),50))
    w=wa*random.choice([1,-1])
    # make x near integer sometimes
    if random.random()<0.3 and t0>0:
        # pick w near integer/t0 scaled: w=n/t0 if large enough
        n=math.ceil(wa*t0); w=F(n)/t0*random.choice([1,-1])
        if abs(w)<(m+1)*mx: continue
    b4n+=1
    if not t0>=1/((m+1)*mx) or not abs(w)*t0>=1: x1fail+=1
    t1=nudge(t0,w,F(1,m+2))
    if t1<0 or not inS(V+[w],t1,F(1,m+2)): b4fail+=1
res['B4']=(b4n,edge,b4fail,x1fail)
# B4'
b4pf=0;n=0
for _ in range(3000):
    m=random.randint(2,6)
    us=[F(random.randint(1,5),random.randint(1,3))]
    for j in range(2,m+1):
        us.append(us[-1]*j*(1+F(random.choice([0,0,1,5]),random.randint(1,4))))
    t=1/(2*us[0])
    for j in range(2,m+1): t=nudge(t,us[j-1],F(1,j+1))
    V=[u*random.choice([1,-1]) for u in us]
    n+=1
    if t<0 or not inS(us,t,F(1,m+1)): b4pf+=1
    # intermediate
    tt=1/(2*us[0])
    for j in range(2,m+1):
        tt=nudge(tt,us[j-1],F(1,j+1))
        if not inS(us[:j],tt,F(1,j+1)): b4pf+=1
res['B4p']=(n,b4pf, nudge(F(1,2),F(2),F(1,3)))
# B4''
def half(t,w):
    w=abs(w);x=w*t;k=math.floor(x)
    c=[F(2*kk+1,2) for kk in (k-1,k,k+1)]
    c=[y for y in c if y>0]
    y=min(c,key=lambda y:(abs(y-x),y)); return y/w
b4ppf=0;n=0;minfin=1
for m in range(2,8):
  for qq in [F(2*m,m-1), F(2*m,m-1)+F(1,10), F(3) if m>=3 else None]:
    if qq is None: continue
    for _ in range(300):
        us=[F(random.randint(1,20),random.randint(1,5))]
        for j in range(1,m): us.append(us[-1]*qq*(1+F(random.choice([0,0,1,3]),random.randint(1,8))))
        t=1/(2*us[0])
        for j in range(1,m): t=half(t,us[j])
        n+=1
        mn=min(nrm(u*t) for u in us)
        # loss bound
        if mn<F(1,m+1) or t<0: b4ppf+=1
        if mn<(qq-2)/(2*(qq-1)): b4ppf+=1000
res['B4pp']=(n,b4ppf, half(F(1,2),F(4)), q3_m2:=None)
# q=3, m=2 should fail? find counterexample
fl=0
for _ in range(2000):
    us=[F(1)];us.append(F(3)*(1+F(random.choice([0,0,1]),random.randint(1,8))))
    t=half(1/(2*us[0]),us[1])
    if min(nrm(u*t) for u in us)<F(1,3): fl+=1
res['q3_m2_fail(not claimed)']=fl
# B5
b5v=0;worst=0;n=0
for _ in range(400):
    a=F(random.randint(1,30),random.randint(1,6))
    b=a*(1+F(random.choice([1,2,5,50,100]),random.choice([1,100,10000,1000])))
    if random.random()<.3: b=a+F(1,random.randint(100,10**6))
    L=3/(2*a)
    s0=F(random.randint(0,100000),random.randint(1,50))
    # find first good point >= s0 : candidates in window
    g=goodpts([a,b],F(1,4),s0+2*L+1,s0)
    g=[c for c in g if s0<=c]
    if not g or g[0]-s0>L: b5v+=1
    else: worst=max(worst,(g[0]-s0)/L)
    n+=1
res['B5']=(n,b5v,float(worst))
# obstruction
obs=[]
for N in [10,100,1000]:
    e=F(1,N);V=[F(1),1+e]
    g=goodpts(V,F(1,3),F(6*N))
    gaps=max(b-a for a,b in zip(g,g[1:]))
    obs.append((N,float(gaps),float(gaps*e)))
res['obstruction(N,maxgap,gap*eps)']=obs
for k,v in res.items(): print(k,v)
