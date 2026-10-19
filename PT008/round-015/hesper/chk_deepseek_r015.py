from fractions import Fraction as F
import random
def R013(a,b,c,d): return c<4*a and max(4*a,(5*c-2*a)/2)<d<min(9*a,4*c)
for v in [(10,20,31,68),(11,20,36,80)]:
    a,b,c,d=map(F,v); print(v,'in R013',R013(a,b,c,d))
# band claim: x0<c/a<=36/11, D1<d<D2 => in R013
random.seed(9); tot=out=0
x0=(9+41**0.5)/5
for _ in range(50000):
    a=F(1); c=F(random.randint(30807,32727),10000)
    if not (c>x0 and c<=F(36,11)): continue
    D1=F(5,2)*c-a; D2=2*a*c/(4*a-c)
    if D1>=D2: continue
    d=D1+(D2-D1)*F(random.randint(1,9999),10000); b=(a+c)/2
    tot+=1; out+= not R013(a,b,c,d)
print('band points',tot,'outside R013',out)
