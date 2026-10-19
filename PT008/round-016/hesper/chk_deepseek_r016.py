from fractions import Fraction as F
from math import floor
import random
def nd(z): return min(z-floor(z), floor(z)+1-z)
random.seed(16); bad=0; N=20000
for _ in range(N):
    s=F(80)+F(20)*F(random.randint(0,10**6),10**6)
    th=F(32,100)+F(2,100)*F(random.randint(0,10**6),10**6)
    w=F(88,100)+F(1,100)*F(random.randint(0,10**6),10**6)
    a=F(1); S=s*a; b=th*S; c=S-b; d=w*S
    assert a<b<c<d
    t=F(20)/S
    if min(nd(u*t) for u in (a,b,c,d))<F(1,5): bad+=1
print('R20 closed box random',N,'fail',bad)
V=[F(1),F(30),F(60),F(80)]; S=V[1]+V[2]; print('V4 s,theta,w',S,V[1]/S,V[3]/S,[str(nd(u*F(20)/S)) for u in V])
print('LE-1 example (1,3,21/5) d=1/4 t=5/12',[str(nd(u*F(5,12))) for u in (F(1),F(3),F(21,5))])
