from fractions import Fraction as F
import itertools,io,contextlib,sys
with contextlib.redirect_stdout(io.StringIO()):
    from fwcert import comps
def wins(K,d,top):
    L,R=K;out=[];q=0
    while True:
        lo=(q-d)/L
        if lo>=top: break
        hi=(q+d)/R
        if lo<hi: out.append((max(lo,F(0)),hi))
        q+=1
    return out
def inW(ws,u): return any(x<u<y for x,y in ws)
def run(k,mx):
    d=F(1,k+2); tot=0; ev=0; badE=0; ovl=0; empty=0; allfail=0
    for V in itertools.combinations(range(1,mx+1),k):
        V=[F(x) for x in V]; a,b=V[0],V[-1]
        C=comps(V,d/a,(1-d)/a,d)
        if not C: empty+=1; continue
        pos=[K for K in C if K[1]>K[0]]
        U=max(2*d/(K[1]-K[0]) for K in pos) if pos else 4*b
        top=max(U,b)+1; tot+=1
        Ws=[wins(K,d,top) for K in C]
        for ws in Ws:
            s=sorted(ws)
            for (x1,y1),(x2,y2) in zip(s,s[1:]):
                if x2<y1: ovl+=1
        E=sorted({e for ws in Ws for w in ws for e in w if b<e<U})
        pts=sorted(set([b,U]+E))
        N=lambda u: sum(1 for ws in Ws if not inW(ws,u))
        for i,e in enumerate(pts[1:-1],1):
            ev+=1; l=(pts[i-1]+e)/2; r=(e+pts[i+1])/2
            if N(e)<max(N(l),N(r)): badE+=1
        for x,y in zip(pts,pts[1:]):
            if N((x+y)/2)==0: allfail+=1
    print(f"k={k} d=1/{k+2} ints<={mx}: inputs {tot} (S empty {empty}); endpoints in (b,U) {ev}; N(e)<max(N(e-),N(e+)) {badE}; same-comp overlaps {ovl}; open segments with N=0 {allfail}")
for k,mx in ((2,20),(3,15),(4,11)): run(k,mx)
# full-axis B(1,3,4)
with contextlib.redirect_stdout(io.StringIO()):
    from copus import badset
B,C=badset([F(1),F(3),F(4)],F(1,5),F(400)); print("comps(1,3,4):",C); print("B(1,3,4) on (0,400):",B)
