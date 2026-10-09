# Exhaustive (floats, then exact check of the minimizer): min over 13-subsets of {1..M} of c(S) = max(S) * longest safe piece.
import itertools, sys
from fractions import Fraction as F
from longest import pieces
M=int(sys.argv[1]); best=(9,None); cnt=0
for S in itertools.combinations(range(1,M+1),13):
    P=pieces(S); c=max(S)*max(b-a for a,b in P); cnt+=1
    if c<best[0]-1e-12: best=(c,S)
def exact_longest(S,d=F(1,16)):
    acc=[(F(0),F(1))]
    for v in S:
        allowed=[(F(m)/v+d/v,F(m+1)/v-d/v) for m in range(v)]
        acc=[(max(a,c),min(b,e)) for a,b in acc for c,e in allowed if max(a,c)<=min(b,e)]
    return max(b-a for a,b in acc)
L=exact_longest(best[1]); print(f"M={M} sets={cnt} min c={best[0]:.6f} at S={best[1]} exact longest={L} exact c={max(best[1])*L}")
