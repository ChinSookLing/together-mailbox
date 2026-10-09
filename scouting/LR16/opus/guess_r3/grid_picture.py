# Exact safe set of a speed set S at threshold 1/16, and which grid points t/p fall inside. Plain Python, exact fractions.
from fractions import Fraction as F
def safe_intervals(speeds, d=F(1,16)):
    acc=[(F(0),F(1))]
    for v in speeds:
        allowed=[(F(m)/v + d/v, F(m+1)/v - d/v) for m in range(v)]
        acc=[(max(a,c),min(b,e)) for a,b in acc for c,e in allowed if max(a,c)<=min(b,e)]
    return acc
for p,S in ((223,[1,6,16,19,28,34,40,52,54,59,86,96,99]),(239,[1,9,16,19,56,65,66,73,75,92,102,108,111])):
    iv=safe_intervals(S); L=sum(b-a for a,b in iv)
    grid=[t for t in range(1,p) if any(a<=F(t,p)<=b for a,b in iv)]
    print(p,"pieces",len(iv),"length %.4f"%float(L),"longest %.5f"%float(max(b-a for a,b in iv)),"1/p %.5f"%(1/p),"grid inside",grid)
