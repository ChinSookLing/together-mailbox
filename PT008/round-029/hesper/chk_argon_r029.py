exec(open('/workspace/work/pt008r20/hesper/base.py').read().split('A=lambda')[0])
import random; random.seed(29005)
from decimal import Decimal as D, getcontext; getcontext().prec=60
f5=F(1,5)
def ok(V,t): return 0<t<1/V[0] and min(nd(v*t) for v in V)>=f5
V=(1,25,30,55); t=F(19,85); print('A:',[nd(v*t) for v in V], ok(V,t), 'region',V[3]>4*V[0] and V[2]<V[3]<4*V[2])
t=F(21,85); print('A t=21/85 b:',nd(25*t))
phi=(1+D(5).sqrt())/2; Vd=[D(1),D(5),5*phi,10*phi]
def ndd(x): f=x-int(x); return min(f,1-f)
for tt in [D('0.3'),D('0.24'),D('0.52')]: print('golden t=',tt,[float(ndd(v*tt)) for v in Vd])
# Bundle: d<=c+1/(20 T4(a,b,c))
def rnd(): return F(random.randint(1,10**4),random.randint(1,300))
n=f=0
while n<20000:
    a,b,c=sorted({rnd() for _ in range(3)}) if True else 0
    if not a<b<c: continue
    t0=F4(a,b,c); d=c+F(random.randint(1,1000),1000)/(20*t0)
    n+=1; f+= not ok((a,b,c,d),t0)
print('Bundle tests',n,'fails',f)
# WL as described
def WL(a,b,c,d):
    tL=1/(5*a)
    if nd(d*tL)>=f5: return tL
    k=round(d*tL); return (k+f5)/d
n=f=0; ex=None
while n<20000:
    a=F(1); b=1+rnd()%3; c=b+rnd()%3
    if not (a<b<c<4*a): continue
    d=max(F(2)*a*c/(4*a-c),c)*(1+F(random.randint(0,10**4),10**4))
    if not d>c: continue
    n+=1
    if not ok((a,b,c,d),WL(a,b,c,d)): f+=1; ex=ex or (b,c,d)
print('WL (c<4a, d>=2ac/(4a-c)) tests',n,'fails',f,ex)
n=f=0; ex=None
while n<20000:
    a=F(1); b=1+rnd()%3; c=b+rnd()%3
    if not (a<b<c<4*a): continue
    lo=max(F(5,2)*c-a,c); hi=9*a
    if lo>hi: continue
    d=lo+(hi-lo)*F(random.randint(0,10**4),10**4)
    if not d>c: continue
    n+=1
    if not ok((a,b,c,d),2/(a+d)): f+=1; ex=ex or (b,c,d)
print('P1 t=2/(a+d) (c<4a, 5c/2-a<=d<=9a) tests',n,'fails',f,ex)
# c<=2a, d>4a: WL or P1
n=f=0; ex=None
while n<20000:
    a=F(1); b=1+F(random.randint(1,9999),10**4); c=b+(2-b)*F(random.randint(1,9999),10**4)
    d=4+rnd()%40
    if not(d<4*c): continue
    n+=1
    if not(ok((a,b,c,d),WL(a,b,c,d)) or ok((a,b,c,d),2/(a+d))): f+=1; ex=ex or (b,c,d)
print('c<=2a, 4a<d<4c via WL or P1 tests',n,'fails',f,ex)
print('36/11 check',2*F(36,11)/(4-F(36,11)),' 3/55 check',F(12,11)/20)
