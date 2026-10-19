from fractions import Fraction as F
from math import floor, ceil
def nd(z): return min(z-floor(z), floor(z)+1-z)
d5=F(1,5)
m,Q,th0,w0=2,14,F(2,7),F(6,7)
R=[k for k in range(1,Q) if min(nd(F(k,m)*x) for x in (th0,1-th0,w0))>=d5]
print('R (>=1/5)',R,[[str(nd(F(k,m)*x)) for x in (th0,1-th0,w0)] for k in R])
V=(F(7,20),F(2),F(5),F(6));s=(V[1]+V[2])/V[0]
k0=ceil(m*s/5);k=k0+min((r-k0)%Q for r in R);t=F(k,m)/(V[1]+V[2])
print('k0',k0,'k',k,'t',t,[str(nd(u*t)) for u in V])
Rs=sorted(R);G=max((Rs[(i+1)%len(Rs)]-Rs[i])%Q or Q for i in range(len(Rs)));print('G',G,'smin',F(5*G,3*m))
# 0 never in R
print('k=0 phases', [nd(F(0)*x) for x in (th0,)])
