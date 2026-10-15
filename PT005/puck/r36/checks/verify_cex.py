# Independent direct verification of a candidate F1 counterexample: no formulas, only the raw cover test.
from collections import Counter
def hit(t,W,M): r=t*W%M; return 16*min(r,M-r)<M
def verify(p,b,W):
    n5,n6=32*p,64*p
    assert all(w%2==1 and 1<=w<16*p and w%p not in (0,1,p-1) for w in W) and len(set(W))==8
    c5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
    cov5=Counter(t for w in W for t in c5 if hit(t,w,n5))
    k5=len(c5)==16 and all(cov5[t]==1 for t in c5) and sum(cov5.values())==16
    c6=[t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
    best=None
    for mask in range(256):
        W6=[w+((mask>>i)&1)*n5 for i,w in enumerate(W)]
        cov6=Counter(t for w in W6 for t in c6 if hit(t,w,n6))
        if len(c6)==32 and all(cov6[t]==1 for t in c6) and sum(cov6.values())==32: best=W6; break
    classes=sorted({'+-1' if w%8 in (1,7) else '+-3' for w in W})
    return dict(p=p,b=b,k5_exact_tiling=k5,mixed=classes,k6_lift_tiling=best)
print(verify(79,76,[865,993,675,289,385,579,545,673]))
print(verify(89,36,[1345,545,1089,129,673,587,139,1035]))
print(verify(19,1,[175,165,241,219,79,27,271,45]))  # control: should have no k6 lift
