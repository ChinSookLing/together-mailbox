# Puck exact check of Argon R011 Track C (1,3,4,5) and the solution windows
from fractions import Fraction as F
def nd(x): x=x-(x.numerator//x.denominator); return min(x,1-x)
v=(1,3,4,5); th=F(1,5)
print("corridor 4a<d<4c:",4*1<5<4*4)
for M,name in ((14,"tau/(b+c), tau in Z/2"),(12,"tau/(a+d)"),(10,"tau/(a+c)")):
    ok=[x for x in range(M) if all(nd(F(u*x,M))>=th for u in v)]
    print(name,"M=",M,"successful x mod M:",ok)
# exact success set in [0,1): endpoints are multiples of 1/(5u) etc; sample on fine grid with exact fractions
N=6000
good=[F(i,N) for i in range(N) if all(nd(F(u*i,N))>=th for u in v)]
# group into intervals
iv=[];s=p=None
for g in good:
    if s is None: s=p=g
    elif g-p==F(1,N): p=g
    else: iv.append((s,p)); s=p=g
if s is not None: iv.append((s,p))
print("success windows on grid 1/6000:",[(float(a),float(b)) for a,b in iv])
# exact window: [4/9? ] check candidates
for t in (F(2,5)+F(1,25)*1, F(11,25), F(9,20), F(89,200), F(11,20), F(14,25)):
    print(t, float(t), [str(nd(u*t)) for u in v], all(nd(u*t)>=th for u in v))
