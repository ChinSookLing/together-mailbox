# Hesper check of Argon R008 B2: region c>=1.5b, a>=0.1(b+c), a<b<c<d, 0.6(b+c)<=d<=0.9(b+c); t=2/(b+c); min ||vt|| >= 1/5. Exact rationals.
from fractions import Fraction as F; import random
def nd(x): return abs(x-round(x))
random.seed(8); n=0; worst=F(1)
while n<200000:
    b=F(random.randint(1,10**6),10**5); c=b*F(random.randint(150000,900000),100000)
    s=b+c; a=s*F(random.randint(10**5,10**6),10**6); d=s*F(random.randint(6*10**5,9*10**5),10**6)
    if not (a<b<c<d): continue
    t=2/s; m=min(nd(v*t) for v in (a,b,c,d)); worst=min(worst,m); n+=1
    assert m>=F(1,5),(a,b,c,d)
print("tested",n,"fails 0, worst",float(worst))
