# Puck independent exact-Fraction spot-check of Opus R008 T4 manuscript (8 branches)
from fractions import Fraction as F
import random, math
random.seed(20261018)
def fl(q): return q.numerator//q.denominator
def ce(q): return -((-q.numerator)//q.denominator)
def frac(q): return q-fl(q)
def dist(q): f=frac(q); return min(f,1-f)
Q=F(1,4)
def T4(a,b,c):  # Puck's own re-implementation from the manuscript table A1-A3
    if c<=3*a: return 'S1',Q/a
    if c>=3*b:
        t0=F(ce((a+b)/(3*a)),1)/(a+b); X=c*t0
        if dist(X)>=Q: return 'S2',t0
        k=fl(X+F(1,2)); e=X-k; sg=1 if e>=0 else -1
        return 'S2',(k+F(sg,4))/c
    if b>=3*a:
        th=b/(b+c); k0=ce((b+c)/(4*a)); x0=frac(k0*th)
        if Q<=x0<=3*Q: j=0
        else: j=ce(frac(Q-x0)/th)
        return 'S3',F(k0+j)/(b+c)
    r=c/b; s=(b+c)/a
    if r<=F(7,5): return 'B3',F(3)/(b+c)
    if r>=F(5,3) and s<=8: return 'B2',F(2)/(b+c)
    if F(9,7)<=r<=F(11,5) and s>=F(16,3): return 'B4',F(4)/(b+c)
    if r>=F(13,7) and s>=F(20,3): return 'B5',F(5)/(b+c)
    return 'S6A',F(3)/(a+c)
cnt={};fails=[];n=0
def test(a,b,c,tag=''):
    global n
    if not (0<a<b<c): return
    n+=1
    br,t=T4(a,b,c); cnt[br]=cnt.get(br,0)+1
    m=min(dist(a*t),dist(b*t),dist(c*t))
    if t<=0 or m<Q: fails.append((tag,a,b,c,br,t,m))
    if br=='S6A':  # must lie in G
        r=c/b;s=(b+c)/a
        assert F(7,5)<r<F(5,3) and s<F(16,3),(a,b,c)
def rf(lo,hi,den=10**6): return F(random.randint(int(lo*den),int(hi*den)),den)
# 1) whole space, a=1
for _ in range(40000):
    b=1+rf(0,12); c=b+rf(0,40); test(F(1),b,c,'whole')
# 2) inside D (b<3a, 3a<c<3b)
for _ in range(40000):
    b=1+rf(0,2); c=rf(3,float(3*b)); test(F(1),b,c,'D')
# 3) G triangle
for _ in range(10000):
    b=1+rf(0,2); r=rf(1.4,5/3); c=b*r; test(F(1),b,c,'G')
# 4) exact boundary lines and +-eps, a=1, sweep b
eps=F(1,10**6)
bounds_r=[F(7,5),F(5,3),F(9,7),F(11,5),F(13,7)]; bounds_s=[F(8),F(16,3),F(20,3)]
for i in range(1,2000):
    b=1+F(2*i,2000)
    for r in bounds_r:
        for d in (0,eps,-eps): test(F(1),b,b*(r+d),'rline')
    for s in bounds_s:
        for d in (0,eps,-eps): test(F(1),b,(s+d)-b,'sline')
    for c in (3*b,3*b+eps,3*b-eps,F(3),F(3)+eps): test(F(1),b,c,'Dedge')
for i in range(1,2000):
    b=F(3)+F(i,100)
    for c in (b+eps,3*b-eps,3*b,F(4)*b): test(F(1),b,c,'S3edge')
# 5) a != 1 scaling
for _ in range(5000):
    a=rf(0.01,50); b=a*(1+rf(0,5)); c=b*(1+rf(0,5)); test(a,b,c,'scale')
print('cases',n,'fails',len(fails)); print('branches',cnt)
for f in fails[:10]: print(f)
# 6) manuscript example table (section C.6)
ex=[((1,2,3),'S1',F(1,4)),((1,2,6),'S2',F(3,8)),((1,3,4),'S3',F(3,7)),((2,4,7),'B2',F(2,11)),
    ((1,F(5,2),F(16,5)),'B3',F(10,19)),((1,F(3,2),F(16,5)),'B2',F(20,47)),((1,F(12,5),4),'B2',F(5,16)),
    ((1,2,F(16,5)),'S6A',F(5,7)),((1,F(29,10),F(59,10)),'B4',F(5,11)),((1,F(29,10),F(17,2)),'B5',F(25,57))]
for (a,b,c),br,t in ex:
    a,b,c=F(a),F(b),F(c); B,T=T4(a,b,c)
    print((str(a),str(b),str(c)),'branch',B,'(claimed',br+')','t',T,'(claimed',str(t)+')','dists',[str(dist(x*T)) for x in (a,b,c)],'OK' if (B==br and T==t) else 'MISMATCH')
# 7) B(k,m) rectangle endpoints
for k,m in [(2,0),(3,1),(4,1),(5,1)]:
    print('B',k,m,'s',[str(F(4*k,3)),str(F(4*k))],'r',[str(F(4*k,4*m+3)-1),str(F(4*k,4*m+1)-1)])
# 8) G-in-S6A inequalities
print('10/3<11:',F(10,3)<11,' 25/11<3:',F(25,11)<3,' 10/3<49/11:',F(10,3)<F(49,11))
