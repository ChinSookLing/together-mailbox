from fractions import Fraction as F
import random, math
random.seed(1)
def nd(x): 
    f=x-math.floor(x); return min(f,1-f)
def rho(V,t,d): return min((nd(u*t)-d)/abs(u) for u in V)
def wmax(w,c,r):
    # max ||w t|| over [c-r,c+r]
    lo,hi=c-r,c+r
    best=max(nd(w*lo),nd(w*hi))
    a,b=sorted((w*lo,w*hi)); k=math.ceil(a-F(1,2))
    while k+F(1,2)<=b: best=max(best,F(1,2)); k+=1
    return best
def randV():
    m=random.randint(1,5); V=set()
    while len(V)<m:
        u=F(random.randint(1,12),random.choice([1,1,2,3,4]))*random.choice([1,-1]); V.add(u)
    return list(V)
def oldsafe(V,N=240,T=None):
    n=len(V)+1; L=[]
    for _ in range(4000):
        t=F(random.randint(0,N*3),N)
        if all(nd(u*t)>=F(1,n) for u in V): L.append(t)
        if len(L)>=8: break
    return L
# Claim1
hyp=viol=tests=0; near=0; tight=0
for it in range(3000):
    V=randV(); n=len(V)+1; d=F(1,n+1); L=oldsafe(V)
    if len(L)<2: continue
    for _ in range(6):
        w=F(random.randint(1,40),random.choice([1,2,3,5,7]))*random.choice([1,-1])
        ta,tb=random.sample(L,2); ra,rb=rho(V,ta,d),rho(V,tb,d)
        ok=wmax(w,ta,ra)>=d or wmax(w,tb,rb)>=d
        gap=nd(w*(ta-tb))-(2*d-abs(w)*(ra+rb))
        tests+=1
        if gap>=0:
            hyp+=1
            if not ok: viol+=1; print("VIOL",V,w,ta,tb)
        elif not ok:
            tight+=1
            if gap>-F(1,50): near+=1
print("C1 tests",tests,"hyp holds",hyp,"violations",viol,"hyp fails & both windows fail",tight,"of which gap>-1/50:",near)
# Claim1 tightness: scan for hyp-fail slightly with both failing (smallest |gap|)
# Claim2
c2=c2t=0;bad=0
for it in range(3000):
    V=randV(); n=len(V)+1; d=F(1,n+1); M=max(abs(u) for u in V); L=oldsafe(V)
    if not L: continue
    w=(n*M+F(random.randint(0,30),random.choice([1,3,7])))*random.choice([1,-1])
    for t in L[:3]:
        c2t+=1
        if wmax(w,t,rho(V,t,d))<d: bad+=1; print("C2 bad",V,w,t)
print("C2 tests",c2t,"failures",bad)
# Claim3
V=[F(1)];d=F(1,3);w=F(4,3)
print("C3 rho at 1/2:",rho(V,F(1,2),d))
res=[]
for a in range(0,6):
  for b in range(a+1,6):
    ta,tb=F(2*a+1,2),F(2*b+1,2)
    ra,rb=rho(V,ta,d),rho(V,tb,d)
    A=wmax(w,ta,ra)>=d;B=wmax(w,tb,rb)>=d
    if not A: res.append((ta,tb,B,nd(w*(ta-tb)),2*d-w*(ra+rb)))
print("C3 single window fails at",[str(x[0]) for x in res][:3]," examples (ta,tb,tb works,||w(ta-tb)||,thresh):",[tuple(map(str,r)) for r in res[:4]])
# Claim 4/5 generic
def comps(V,d,N):
    # grid points t in [0,3) ; exact component = interval where all ||u t||>=d; compute via breakpoints
    pts=set()
    for u in V:
        for k in range(int(3*abs(u))+2):
            pts.add((F(k)+d)/abs(u)); pts.add((F(k+1)-d)/abs(u))
    return sorted(p for p in pts if 0<=p<=3)
def segs(V,d,T=3):
    pts=comps(V,d,0); good=[]
    for a,b in zip(pts,pts[1:]):
        m=(a+b)/2
        if all(nd(u*m)>=d for u in V): good.append((a,b))
    # merge
    out=[]
    for a,b in good:
        if out and out[-1][1]==a: out[-1]=(out[-1][0],b)
        else: out.append((a,b))
    return out
def wmaxI(w,a,b): return wmax(w,(a+b)/2,(b-a)/2)
def test(V,w,tag):
    n=len(V)+1;d=F(1,n+1);Vw=V+[w]
    N=1200
    old=[F(i,N) for i in range(0,3*N+1) if all(nd(u*F(i,N))>=F(1,n) for u in V)]
    # Lipschitz
    lip=0;lipS=[]
    for t in old:
        r=rho(V,t,d)
        if wmax(w,t,r)>=d: lip+=1; lipS.append(t)
    S=segs(V,d)
    comp_ok=[(a,b) for a,b in S if any(a<=t<=b for t in old) and wmaxI(w,a,b)>=d]
    # global safe intervals for Vw at threshold d
    G=segs(Vw,d)
    print(tag,"V",[str(x) for x in V],"w",w,"n",n,"old safe grid pts",len(old),"| Lipschitz windows succeeding:",lip,
          "| exact comps containing old safe pt:",len([1 for a,b in S if any(a<=t<=b for t in old)]),"succeeding:",len(comp_ok),
          "| global safe intervals in [0,3]:",len(G))
    print("  global examples:",[(str(a),str(b)) for a,b in G[:6]])
    if G:
        dist=[]
        for a,b in G[:6]:
            m=(a+b)/2
            dd=min(abs(m-t) for t in old); dist.append(float(dd))
        print("  dist from global-interval midpoints to nearest old safe grid pt:",dist)
    print("  comp ok:",[(str(a),str(b)) for a,b in comp_ok[:4]])


def gpts(V,w):
    n=len(V)+1;d=F(1,n+1);Vw=V+[w]
    pts=comps(Vw,d,0); S=[]
    for p in pts:
        if all(nd(u*p)>=d for u in Vw): S.append(p)
    return S,d
if __name__=="__main__":
    test([F(1),F(2)],F(3),"C4"); test([F(1),F(3)],F(2),"C5")
    for V,w in (([F(1),F(2)],F(3)),([F(1),F(3)],F(2))):
        S,d=gpts(V,w); n=len(V)+1
        old=[F(i,1200) for i in range(0,3601) if all(nd(u*F(i,1200))>=F(1,n) for u in V)]
        print("global safe breakpoints (t in[0,3]) for",[str(x) for x in V+[w]],":",[str(s) for s in S])
        print("  dist to nearest old safe grid pt:",[ (str(s),float(min(abs(s-t) for t in old))) for s in S][:8])
        # exact comp containing each global pt: is it an old-safe comp?
