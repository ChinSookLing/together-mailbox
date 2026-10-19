src=open('base.py').read(); exec(src[:src.index("ok=lambda")])
from fractions import Fraction as F
import random; random.seed(20020)
from math import ceil
def conv_last(x,Q0):
    # last convergent of x with denom <= Q0
    p0,q0,p1,q1=0,1,1,0; y=x
    best=None
    while True:
        a=y.numerator//y.denominator
        p0,p1=p1,a*p1+p0; q0,q1=q1,a*q1+q0
        if q1>Q0: return best
        best=F(p1,q1)
        fracy=y-a
        if fracy==0: return best
        y=1/fracy
def qgate(b,c,d):
    S=b+c; th=b/S; w=d/S; M=max(1-th,w); Q0=ceil(20*M)
    t0=F4(b,c,d); ts=S*t0; tau=conv_last(ts,Q0)
    return tau,Q0,th,w
bad=0;maxden=0;n=0
for _ in range(20000):
    x=sorted(F(random.randint(1,10**7),random.randint(1,10**5)) for _ in range(3))
    if len(set(x))<3: continue
    b,c,d=x; tau,Q0,th,w=qgate(b,c,d); n+=1
    if tau is None or tau<=0 or tau.denominator>Q0 or min(nd(tau*u) for u in (th,1-th,w))<F(1,5): bad+=1
print('Q-GATE random',n,'fail',bad)
# huge-denominator ('near irrational') triples
bad=0
for _ in range(5000):
    x=sorted(F(random.randint(1,10**30),random.randint(10**20,10**21)) for _ in range(3))
    b,c,d=x; tau,Q0,th,w=qgate(b,c,d)
    if tau is None or tau.denominator>Q0 or min(nd(tau*u) for u in (th,1-th,w))<F(1,5): bad+=1
print('Q-GATE big-denominator 5000 fail',bad)
tau,Q0,th,w=qgate(F(1),F(101,100),F(2)); print('example (1/7,1,101/100,2): tau',tau,'Q0',Q0,[str(nd(tau*u)) for u in (th,1-th,w)], 'a dist at t=tau/S', nd(F(1,7)*tau/(F(201,100))))
V=(F(7,20),2,5,6); t=F(9,8); print('chair shape t=9/8',[str(nd(u*t)) for u in V])
