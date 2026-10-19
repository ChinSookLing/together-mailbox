from fractions import Fraction as F
from math import floor, gcd
def nd(z): return min(z-floor(z), floor(z)+1-z)
d5=F(1,5)
def Rset(th,w,m):
    Q=m*(th.denominator*w.denominator//gcd(th.denominator,w.denominator))
    return [k for k in range(Q) if min(nd(F(k,m)*th),nd(F(k,m)*(1-th)),nd(F(k,m)*w))>=d5]
# Q-ERC1: m=1, empty iff w integer
cex=[];tot=0
for q in range(3,41):
  for p in range(1,q):
    if gcd(p,q)!=1 or not F(p,q)<F(1,2): continue
    th=F(p,q)
    for q2 in range(1,25):
      for p2 in range(1,3*q2+1):
        if gcd(p2,q2)!=1: continue
        w=F(p2,q2)
        if w<=1-th: continue
        tot+=1
        e=len(Rset(th,w,1))==0
        if e!=(q2==1): cex.append((str(th),str(w)))
print('Q-ERC1 tested',tot,'counterexamples',len(cex),cex[:10])
# Q-ERC2 sufficiency: w=n integer, m/gcd(n,m)>=3, q>=3 => nonempty
cex2=[];tot2=0
for q in range(3,31):
  for p in range(1,q):
    if gcd(p,q)!=1 or not F(p,q)<F(1,2): continue
    for n in range(1,6):
      if F(n)<=1-F(p,q): continue
      for m in range(2,13):
        if m//gcd(n,m)<3: continue
        tot2+=1
        if not Rset(F(p,q),F(n),m): cex2.append((f'{p}/{q}',n,m))
print('Q-ERC2 sufficiency tested',tot2,'counterexamples',len(cex2),cex2[:10])
# §4.2: theta=1/q, w=1, m=3: best margin over residues
for q in (5,11,23,47,101):
  th=F(1,q);R=Rset(th,F(1),3)
  best=max(min(nd(F(k,3)*th),nd(F(k,3)*(1-th)),nd(F(k,3)))-d5 for k in R) if R else None
  print('theta=1/%d w=1 m=3 |R|=%d best margin %s'%(q,len(R),best))
