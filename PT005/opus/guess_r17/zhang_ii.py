from fractions import Fraction as Fr
from math import gcd
n=16; K=[k for k in range(1,n) if k!=6]
# exact closed safe set {x in [0,1): ||kx|| >= 1/n, k in K} as intervals
I=[(Fr(0),Fr(1))]
for k in K:
    out=[]
    for a,b in I:
        for j in range(k+1):
            lo=max(a,Fr(n*j+1,n*k)); hi=min(b,Fr(n*j+n-1,n*k))
            if lo<hi: out.append((lo,hi))
    I=out
print("exact components:",[(str(a),str(b)) for a,b in I])
print("measure:",sum(b-a for a,b in I))
# Astra's stated intervals
A=[(Fr(33,208),Fr(31,192)),(Fr(11,64),Fr(31,176)),(Fr(145,176),Fr(53,64)),(Fr(161,192),Fr(175,208))]
print("Astra intervals match exact set:", sorted(A)==sorted(I))
# general check of corrected Case (ii) formula: L_p=(p/r - s/(rnF(u)), p/r - 1/(2rn)), R_p=(p/r+1/(2rn), p/r + s/(rnF(r-u)))
def F(x,r,n): return max(i for i in range(1,n) if i!=r and i%r==x%r)
def exact(n,r):
    I=[(Fr(0),Fr(1))]
    for k in range(1,n):
        if k==r: continue
        out=[]
        for a,b in I:
            for j in range(k+1):
                lo=max(a,Fr(n*j+1,n*k)); hi=min(b,Fr(n*j+n-1,n*k))
                if lo<hi: out.append((lo,hi))
        I=out
    return sorted(I)
for nn in range(5,21):
  for r in range(2,nn):
    if 2*r>nn-1: continue
    s=nn-r; pred=[]
    for p in range(r):
        if gcd(p,r)!=1: continue
        u=pow(p,-1,r); c=Fr(p,r)
        pred.append(((c-Fr(s,r*nn*F(u,r,nn)))%1 if p==0 else c-Fr(s,r*nn*F(u,r,nn)), c-Fr(1,2*r*nn)))
        pred.append((c+Fr(1,2*r*nn), c+Fr(s,r*nn*F(r-u,r,nn))))
    ok = sorted(pred)==exact(nn,r)
    if not ok: print("MISMATCH",nn,r)
print("corrected Case (ii) checked for all n=5..20, 2r<=n-1")
# Kimi's summation formula M(n,r) vs exact measure, all n=5..20, 2r<=n-1
from sympy import totient
bad=0; cnt=0
for nn in range(5,21):
  for r in range(2,nn):
    if 2*r>nn-1: continue
    s=nn-r
    M=Fr(1,r*nn)*(2*s*sum(Fr(1,F(u,r,nn)) for u in range(1,r) if gcd(u,r)==1)-int(totient(r)))
    ex=sum(b-a for a,b in exact(nn,r)); cnt+=1
    if M!=ex: bad+=1; print("M MISMATCH",nn,r,M,ex)
print("M formula cases:",cnt,"mismatches:",bad)
