from fractions import Fraction as F
from math import floor, ceil
def nd(z): return min(z-floor(z), floor(z)+1-z)
def ok(V,t): return all(nd(u*t)>=F(1,5) for u in V)
def rule(a,b,d):
    k0=ceil(F(3)*b/(5*a))
    for k in (k0,k0+1,k0+2):
        if k%3 and nd(k*a/(3*b))>=F(1,5) and nd(k*d/(3*b))>=F(1,5): return k
    return None
V4=[F(1),F(30),F(60),F(80)]
print('V4 t=2/9',[str(nd(u*F(2,9))) for u in V4], 'rule k',rule(*map(F,(1,30,80))))
for d in [F(80),F(801,10),F(8011,100),F(81),F(82),F(774,10),F(773,10)]:
    t=F(20,90); print('d',d,'k=20 dist_d',nd(20*d/90),'ok',ok([1,30,60,d],t),'rule k',rule(F(1),F(30),d))
# neighbourhood exact: frac(20d/90) in [1/5,4/5] around 7/9
print('upper eps',(F(4,5)-F(7,9))*F(9,2),'lower eps',(F(1,5)-F(7,9))*F(9,2))
# rule failure frequency for (1,30,60,d), d in (60,240)
fails=[d for d in [F(600+i,10) for i in range(1,1800)] if rule(F(1),F(30),d) is None]
print('rule fails count',len(fails),'of 1799; first',[str(x) for x in fails[:5]])
