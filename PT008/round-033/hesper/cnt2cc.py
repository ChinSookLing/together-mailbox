from fractions import Fraction as F
import itertools,sys
sys.argv=['x']
import io,contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from fwcert import comps
def W(K,d,top):
    L,R=K;out=[];q=0
    while True:
        lo=(q-d)/L
        if lo>=top:break
        hi=(q+d)/R
        if lo<hi: out.append((max(lo,F(0)),min(hi,top)))
        q+=1
    return out
def inter(A,B):
    return [(max(a[0],c[0]),min(a[1],c[1])) for a in A for c in B if max(a[0],c[0])<min(a[1],c[1])]
def need(V,d):
    a,b=V[0],V[-1];C=comps(V,d/a,(1-d)/a,d)
    pos=[K for K in C if K[1]>K[0]]
    if not pos: return None
    top=max(2*d/(K[1]-K[0]) for K in pos)+1
    Ws=[ [w for w in W(K,d,top) if w[1]>b] for K in C]
    trim=lambda ws:[(max(w[0],b),w[1]) for w in ws if w[1]>b]
    for i,K in enumerate(C):
        if K[1]>K[0] and not trim(Ws[i]): return 1
    for i,j in itertools.combinations(range(len(C)),2):
        if (C[i][1]>C[i][0] or C[j][1]>C[j][0]) and not trim(inter(Ws[i],Ws[j])): return 2
    return 3
for k,mx in ((3,15),(4,11),(5,9)):
    d=F(1,k+2);cnt={}
    for V in itertools.combinations(range(1,mx+1),k):
        r=need([F(x) for x in V],d);cnt[r]=cnt.get(r,0)+1
    print(k,mx,cnt)
