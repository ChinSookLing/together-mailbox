# Hesper check of Qwen R008 B2: 0<a<b<c<d, c+d<=5a, t=1/(c+d) => min||vt|| = a/(c+d) >= 1/5. Exact rationals.
from fractions import Fraction as F; import random
def nd(x): return abs(x-round(x))
random.seed(8); n=0
while n<200000:
    a=F(random.randint(1,10**6),10**5); v=sorted(a*F(random.randint(10**6,4*10**6),10**6) for _ in range(3)); b,c,d=v
    if not (a<b<c<d and c+d<=5*a): continue
    t=1/(c+d); m=min(nd(x*t) for x in (a,b,c,d)); n+=1
    assert m==a/(c+d) and m>=F(1,5)
print("tested",n,"fails 0 (min == a/(c+d) exactly in every case)")
