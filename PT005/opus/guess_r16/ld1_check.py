# Test Kimi's L-D1: for any unit s, #{x in I : ||s x||_p <= H} = (2H+1)/p * |I| + O(log^2 p)?
from math import log
for p in (601, 1009, 4001):
    H = (p-1)//16
    ell = p//8                      # interval I = [1, ell]
    best=(0,None)
    for s in range(1,p):
        killed = sum(1 for x in range(1,ell+1) if min((s*x)%p, p-(s*x)%p) <= H)
        dev = killed - (2*H+1)/p*ell
        if abs(dev)>abs(best[0]): best=(dev,s)
    s=(p-1)//2
    k2 = sum(1 for x in range(1,ell+1) if min((s*x)%p, p-(s*x)%p) <= H)
    print(f"p={p} H={H} |I|={ell} expected={(2*H+1)/p*ell:.2f} worst dev={best[0]:.2f} at s={best[1]}; s=(p-1)/2 kills {k2}; log^2 p={log(p)**2:.1f}")
from fractions import Fraction as F
print("97/6864-14/991 =", F(97,6864)-F(14,991))
print("991^14+1 digits:", len(str(991**14+1)))
