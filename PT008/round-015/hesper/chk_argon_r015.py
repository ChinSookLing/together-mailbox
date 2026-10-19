from fractions import Fraction as F
from math import floor, ceil, sqrt
def nd(z): return min(z-floor(z), ceil(z)-z)
def ds(V,t): return [nd(v*t) for v in V]
def g(V,t): return min(ds(V,t))
e=F(1,10**6)
VA=[F(1),F(3,2),F(2),F(25,4)]; VB=[F(1),F(2),F(3),F(27,4)]
print('VA WL hyp c<4a, d>=2ac/(4a-c)=',2*2/(4-2), 'd',VA[3])
for t in [F(1,5),F(4,29),F(4,11),F(8,29)]:
    print('VA t',t,[str(x) for x in ds(VA,t)],'g',g(VA,t),'left',g(VA,t-e)<g(VA,t),'right',g(VA,t+e)<g(VA,t))
print('VB region',max(4,F(13,2)),'<',VB[3],'<',min(9,12))
t=F(8,31); print('VB t',t,[str(x) for x in ds(VB,t)],'g',g(VB,t),'g(t-e)>g',g(VB,t-e)>g(VB,t),'g(1/4)',g(VB,F(1,4)))
for d in [F(51,10),F(6),F(27,4),F(69,10)]:
    V=[F(1),F(2),F(3),d]; print('C2 d',d,[str(x) for x in ds(V,F(1,4))])
# g_abc <= 1/4 grid
print('max g_abc grid', max(g([F(1),F(2),F(3)],F(k,4000)) for k in range(4001)))
Vh=[F(11),F(15),F(30),F(45)]; print('Vharm t=1/20',[str(x) for x in ds(Vh,F(1,20))],'first-window max at',F(11,15)*F(4,15))
# (b,2b,3b) safe band grid
band=[F(k,600) for k in range(600) if g([F(1),F(2),F(3)],F(k,600))>=F(1,5)]
print('band x-range', band[0], max(x for x in band if x<F(1,2)), min(x for x in band if x>F(1,2)), band[-1])
r=sqrt(2); print("V'irr m=0 max at",0.8/(4*r),' m=1 at range',1.2/(4*r),(19/15)/(4*r))
