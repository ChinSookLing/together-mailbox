from fractions import Fraction as F
import itertools,io,contextlib
from math import floor,ceil
with contextlib.redirect_stdout(io.StringIO()):
    from fwcert import comps,nd
    from relay import wins
def inter(A,B): return [(max(a,c),min(b,e)) for a,b in A for c,e in B if max(a,c)<min(b,e)]
def trim(A,lo,hi): return [(max(a,lo),min(b,hi)) for a,b in A if max(a,lo)<min(b,hi)]
def PW(K,K2,d,top):
    dm=K2[0]-K[1]; dp=K2[1]-K[0]; out=[]; x=0
    while (x-2*d)/dm<top:
        lo=max((x-2*d)/dm,F(0)); hi=(x+2*d)/dp
        if lo<hi: out.append((lo,hi))
        x+=1
    return out
def setup(V,d):
    a,b=V[0],V[-1]; C=comps(V,d/a,(1-d)/a,d)
    pos=[K for K in C if K[1]>K[0]]
    U=max(2*d/(K[1]-K[0]) for K in pos)
    return a,b,C,U
def prl_sealed(V,d):
    a,b,C,U=setup(V,d); cur=[(b,U)]
    for i,j in itertools.combinations(range(len(C)),2):
        if C[i][1]==C[i][0] and C[j][1]==C[j][0]: continue
        cur=inter(cur,PW(C[i],C[j],d,U+1))
        if not cur: return True
    return False
for k,mx in ((2,25),(3,15),(4,11),(5,9)):
    d=F(1,k+2); n=s=0
    for V in itertools.combinations(range(1,mx+1),k):
        n+=1; s+=prl_sealed([F(x) for x in V],d)
    print("PRL sealed k",k,"<=",mx,":",s,"/",n)
# GRL-1 count k=3
d=F(1,5); g=0
for V in itertools.combinations(range(1,16),3):
    V=[F(x) for x in V]; a,b,C,U=setup(V,d); hit=False
    for K,K2 in zip(C,C[1:]):
        for w in V:
            p=K[1]*w+d
            if p.denominator==1 and K2[0]==(p+d)/w: hit=True
    g+=hit
print("GRL-1 inputs with single-arc gap k=3<=15:",g,"/455")
# counterexamples
def W(K,d,top): return wins(K,d,top)
for V,d,tL,KL in (([F(12,7),F(63),F(65)],F(1,5),None,None),([F(x) for x in (1,3,4,5,7)],F(1,7),None,None)):
    a,b,C,U=setup(V,d); top=U+1
    # t* = argmax min nd over J breakpoints: evaluate margin at candidate points (mids & breakpoints of nd pieces)
    cands=set()
    for v in V:
        for m in range(0,ceil(v/a)+2):
            cands.add(F(m,1)/v); cands.add((F(2*m+1,2))/v)
    for v,w in itertools.combinations(V,2):
        for m in range(0,ceil(v/a)*2+4):
            for n in range(0,ceil(w/a)*2+4):
                for sg in (1,-1):
                    den=v+sg*w
                    if den!=0:
                        t=(F(m)+sg*F(n))/den
                        cands.add(t)
    J=(d/a,(1-d)/a)
    m=lambda t:min(nd(v*t) for v in V)
    ts=max((t for t in cands if J[0]<=t<=J[1]),key=m)
    ix=[i for i,K in enumerate(C) if K[0]<=ts<=K[1]][0]; K=C[ix]
    print("V",V,"ncomp",len(C),"t*",ts,"K*#",ix+1,K)
    WK=trim(W(K,d,top),b,top)
    ok=[j+1 for j,K2 in enumerate(C) if j!=ix and not trim(inter(WK,W(K2,d,top)),b,top)]
    print(" partners OK:",ok)
    for j in (ix-1,ix+1):
        if 0<=j<len(C): print(" neighbour",j+1,trim(inter(WK,W(C[j],d,top)),b,top))
