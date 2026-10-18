# Puck check of the chair's new results in GPT6 R008 ruling (exact Fractions)
from fractions import Fraction as F
import itertools, random
def dist(x):
    x=x-(x.numerator//x.denominator); return min(x,1-x)
fails=0;cases=0
# (1) n-runner generalisation: speeds v_i in [a,b], b<=(n-1)a, t=1/(a+b) => all ||v t|| >= 1/n
random.seed(8)
for n in range(3,13):
    for _ in range(4000):
        den=random.randint(1,30)
        a=F(random.randint(1,60),den)
        b=a+F(random.randint(0,int(60*(n-2))),den)*a/ (60) * 1  # b in [a,(n-1)a]
        if b>(n-1)*a: b=(n-1)*a
        t=1/(a+b)
        vs=[a,b]+[a+(b-a)*F(random.randint(0,97),97) for _ in range(n-3)]
        cases+=1
        if any(dist(v*t)<F(1,n) for v in vs): fails+=1
# boundary b=(n-1)a exactly, equality cases
for n in range(3,50):
    a=F(1);b=F(n-1);t=1/(a+b);cases+=1
    if dist(a*t)!=F(1,n) or dist(b*t)!=F(1,n): fails+=1
print("n-runner t=1/(a+b):",cases,"cases, fails",fails)
# (2) Argon B2 re-proof: c>=3b/2, a>=(b+c)/10, a<b<c, 3/5 B<=d<=9/10 B, t=2/B -> all >=1/5
c2=f2=0
for b,c,a,d in itertools.product(range(1,31),range(1,61),range(1,31),range(1,61)):
    if not (a<b<c<d) or 2*c<3*b or 10*a<b+c: continue
    B=b+c
    if not (5*d>=3*B and 10*d<=9*B): continue
    t=F(2,B);c2+=1
    if any(dist(v*t)<F(1,5) for v in (a,b,c,d)): f2+=1
print("Argon B2 t=2/(b+c):",c2,"cases, fails",f2)
# (3) Qwen B2 inclusion: a<b<c<d, c+d<=5a => d<4a
c3=f3=0
for a,b,c,d in itertools.combinations(range(1,80),4):
    if c+d<=5*a:
        c3+=1
        if not d<4*a: f3+=1
print("Qwen B2 within d<4a:",c3,"cases, fails",f3)
