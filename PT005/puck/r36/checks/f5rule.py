# Puck's own k=5 rule: w covers level-5 position s5 (mod 32) iff m + s5*w == r (mod 32), r in {-1,0,1,-2*sgn d}.
# Members of C_5(b) (odd t<=16p) have s5 of parity 1+b, one member per residue -> F5 = 2 positions:
#   m == b (mod 2): F5 = v*({+1,-1} - m);  m != b (mod 2): F5 = v*({0,-2 sgn d} - m)   (mod 32)
import random
from lem import hit, bal
def F5(b,w,p):
    d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32); sg=1 if d>0 else -1
    R=(1,-1) if (m-b)%2==0 else (0,-2*sg)
    return {(v*(r-m))%32 for r in R}
def actual(b,w,p):
    S=set()
    for t in range(1,16*p+1,2):
        if t%p not in (b%p,(-b)%p): continue
        if not hit(t,w,32*p): continue
        for eps in (1,-1):
            if (t-eps*b)%p==0: S.add((eps*((t-eps*b)//p))%32); break
    return S
bad=0;n=0
random.seed(1)
for _ in range(3000):
    p=random.choice([17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,1009,10007])
    b=random.randrange(1,p); w=random.randrange(1,16*p,2)
    if w%p in (0,1,p-1): continue
    n+=1
    if F5(b,w,p)!=actual(b,w,p): bad+=1; print('FAIL',p,b,w,F5(b,w,p),actual(b,w,p)) if bad<5 else None
print('F5 rule random',n,'fails',bad)
for p,b,W in [(103,35,(1505,1481,143,263,227,1445,179,1397)),(1009,500,(449,3161,1353,1167,917,1571,45,699))]:
    U=[F5(b,w,p) for w in W]; allp=set().union(*U)
    print(p,b,[sorted(u) for u in U],'tile16:',len(allp)==16 and sum(map(len,U))==16)
