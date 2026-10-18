# Puck exact-Fraction check of R008 Track B (Argon 434ace8, Qwen b680387)
from fractions import Fraction as F; import random
random.seed(1018)
def nd(x): return abs(x-round(x))
def rf(lo,hi,den=10**6): return F(random.randint(int(lo*den),int(hi*den)),den)
# Argon B2: c>=3b/2, a>=(b+c)/10, a<b, 0.6(b+c)<=d<=0.9(b+c), c<d ; t=2/(b+c)
n=f=0; worst=F(1)
while n<100000:
    b=F(1); c=rf(1.5,9); a=rf(0,1); d=rf(0.6,0.9)*(b+c)
    if not (0<a<b<c<d and c>=F(3,2)*b and a>=(b+c)/10): continue
    t=F(2)/(b+c); m=min(nd(x*t) for x in (a,b,c,d)); n+=1; worst=min(worst,m)
    if m<F(1,5): f+=1
print('Argon B2 cases',n,'fails',f,'worst',worst)
print('Argon example (11/10,2,4,5) t=1/3 dists',[str(nd(x*F(1,3))) for x in (F(11,10),F(2),F(4),F(5))])
print('Argon region forces c<9b: a>=(b+c)/10 and a<b => b+c<10b')
# Qwen B2: c+d<=5a, t=1/(c+d)
n=f=0
while n<100000:
    a=F(1); b,c,d=sorted(rf(1,4) for _ in range(3))
    if not (a<b<c<d and c+d<=5*a): continue
    t=1/(c+d); m=min(nd(x*t) for x in (a,b,c,d)); n+=1
    if m<F(1,5) or m!=a/(c+d): f+=1
print('Qwen B2 cases',n,'fails',f)
print('Qwen example (2,3,4,5) t=1/9',[str(nd(x*F(1,9))) for x in (2,3,4,5)])
# Puck observation: Qwen D3 holds WITHOUT c<(a+d)/2: any a<b<c<d with d<=4a, t=1/(a+d)
n=f=0; inQ=0
while n<100000:
    a=F(1); b,c,d=sorted(rf(1,4) for _ in range(3))
    if not (a<b<c<d<=4*a): continue
    t=1/(a+d); m=min(nd(x*t) for x in (a,b,c,d)); n+=1
    if m<F(1,5) or m!=a/(a+d): f+=1
    if c+d>5*a: inQ+=1
print('Puck D3-wide (d<=4a, t=1/(a+d)) cases',n,'fails',f,'of which outside Qwen B2 region',inQ)
print('edge d=4a: (1,2,3,4) t=1/5',[str(nd(x*F(1,5))) for x in (1,2,3,4)])
