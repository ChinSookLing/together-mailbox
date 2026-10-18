# Puck exact check of Qwen R011 Track B (ce7eec3). Fractions only.
from fractions import Fraction as F
from itertools import combinations
import math
def nd(x):  # distance to nearest integer
    x=x-math.floor(x); return min(x,1-x)
th=F(1,5)
def pairs(s): return [(p,q) for p,q in combinations(s,2)]
def ok(s,t,strict=False):
    v=[nd((q-p)*t) for p,q in pairs(s)]
    return all(x>th for x in v) if strict else all(x>=th for x in v)
out=[]
# 1) (3,5,11,24): integer lock t=k/16 for all k (period 16 since speeds integer), half-integer t=(2k+1)/32
s=(3,5,11,24); S=16
il=[k for k in range(S) if ok(s,F(k,S))]
hl=[k for k in range(S) if ok(s,F(2*k+1,2*S))]
out.append(f"(3,5,11,24): integer-lock successes k mod 16: {il}; half-integer successes: {hl}")
mins=[min(nd((q-p)*F(k,S)) for p,q in pairs(s)) for k in range(S)]+[min(nd((q-p)*F(2*k+1,2*S)) for p,q in pairs(s)) for k in range(S)]
out.append(f"  best min-distance over both locks = {max(mins)}")
t=F(1,5); pos=[(v*t)%1 for v in s]
out.append(f"  t=1/5 positions {pos}, min pair distance {min(nd((q-p)*t) for p,q in pairs(s))}")
# 2) ANSWER-BLOCK key theorem: half-integer tau0 strict solution + some r in (2/5,3/5) => tau1=2k0+2 integer solution with margin >=1/10.
# search small integer speeds for counterexample
cex=None; cnt=0
for d in range(4,40):
  for c in range(3,d):
    for b in range(2,c):
      for a in range(1,b):
        s=(a,b,c,d); S=b+c
        rs=[F(q-p,S) for p,q in pairs(s)]
        if not any(F(2,5)<r<F(3,5) for r in rs): continue
        for k0 in range(S):
          tau0=F(2*k0+1,2); 
          if ok(s,tau0/S,strict=True):
            tau1=2*k0+2
            m=min(nd(r*tau1) for r in rs)
            if m<th+F(1,10):
              cnt+=1
              if cex is None: cex=(s,k0,m,[ (p,q,nd(F(q-p,S)*tau1)) for p,q in pairs(s)])
out.append(f"Key theorem (tau1=2k0+2, margin>=1/10): counterexamples found with d<40: {cnt}; first: {cex}")
# 3) Section 3 exact obstruction: per pair r in (2/5,3/5), f = frac(r*tau0) with ||r tau0||>1/5. Which f make ||r(2tau0+1)||<1/5 ?
# Exact derivation: case f in (1/5,1/2): fails iff f < 3/5 - r/2 ; case f in (1/2,4/5): fails iff f > 9/10 - r/2.
# Qwen's stated set: (1/5, 1/5+(3/5-r)/2) U (4/5-(r-2/5)/2, 4/5).
bad_q=0; bad_p=0; N=0
for rn in range(201,300):           # r = rn/500 in (2/5,3/5)
  r=F(rn,500)
  for fn in range(1,1000):
    f=F(fn,1000)
    if not (th<min(f,1-f)): continue
    N+=1
    fails = nd(2*f+r) < th          # ||2(n+f)+r|| = ||2f+r||
    puck = (f<F(1,2) and f<F(3,5)-r/2) or (f>F(1,2) and f>F(9,10)-r/2)
    qwen = (th<f<th+(F(3,5)-r)/2) or (F(4,5)-(r-F(2,5))/2<f<F(4,5))
    bad_p += (fails!=puck); bad_q += (fails!=qwen)
out.append(f"Sec.3 obstruction set on grid ({N} (r,f) points): Puck formula mismatches {bad_p}; Qwen formula mismatches {bad_q}")
# 4) Sec.2 sub-case A1/B1: Qwen says distance >= 2/5 when 2/5+2delta+r <= 1. Check example r=1/2, delta=1/20.
r=F(1,2); dl=F(1,20); u=F(2,5)+2*dl+r
out.append(f"Sec.2 A1 example r=1/2, delta=1/20: 2/5+2delta+r={u}, true distance ||.||={nd(u)} (Qwen treats it as {u})")
# 5) Sec.4 line 175 step: ||k(b-a)/S||>=2/5 => one of the three d-terms >=1/5 (true, triangle) but needs all six; logical gap noted in report.
print("\n".join(out))
