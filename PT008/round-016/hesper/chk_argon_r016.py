from fractions import Fraction as F
from math import floor
import random
def nd(z): return min(z-floor(z), floor(z)+1-z)
def D(V,t): return [str(nd(F(v)*t)) for v in V]
print('A2 (1,3,4,7) t=1/5', D((1,3,4,7),F(1,5)), 'left', D((1,3,4,7),F(1,5)-F(1,1000)),'right',D((1,3,4,7),F(1,5)+F(1,1000)))
print('A3A (1,2,4,5) t=1/5', D((1,2,4,5),F(1,5)))
print('A3B (1,3,9/2,5) t=2/5', D((1,3,F(9,2),5),F(2,5)))
print('V4 t=2/9', D((1,30,60,80),F(2,9)), 'k0=18 t=18/90', D((1,30,60,80),F(18,90)))
random.seed(7); bad=0; nwhit=0; N=20000
for _ in range(N):
    s=F(25)+F(75)*F(random.randint(0,10**6),10**6); th=F(31,100)+F(3,100)*F(random.randint(0,10**6),10**6); w=F(86,100)+F(3,100)*F(random.randint(0,10**6),10**6)
    a=F(1);S=s;b=th*S;c=S-b;d=w*S; assert a<b<c<d
    t=F(20)/S
    if min(nd(u*t) for u in (a,b,c,d))<F(1,5): bad+=1
    if b/c+2*b/(5*d)<=F(3,5): nwhit+=1
print('NF-20 box random',N,'fail',bad,'| points meeting NW-(i) b/c+2b/(5d)<=3/5:',nwhit)
