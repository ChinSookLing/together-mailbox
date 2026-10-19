from fractions import Fraction as F
import random, math
def dist(x):
    f = x - math.floor(x)
    return min(f, 1-f)
def rnd(x): return math.floor(x+F(1,2))
def solve(U,N):
    U=sorted(set(U)); m=U[0]; w=U[-1]; M=U[-2] if len(U)>1 else m
    d=F(1,N)
    if w<=(N-1)*m: return 1/(m+w),'TN'
    tl=d/m; X=w*tl
    if dist(X)>=d: return tl,'t_L'
    k=rnd(X); return (k+d)/w,'shift'
def ok(U,N,t): return t>0 and all(dist(u*t)>=F(1,N) for u in U)
# worked examples
for U,N in [([F(1),F(3,2),F(5,2),F(23,5)],5),([F(1),F(2),F(3),F(7,2),F(31,4)],6)]:
    t,b=solve(U,N);print(U,N,t,b,ok(U,N,t))
for U,t in [([F(1),F(2),F(5),F(6)],F(1,4)),([F(1),F(2),F(3),F(9,2)],F(3,4))]:
    print('E5',U,t,ok(U,5,t),[str(dist(u*t)) for u in U])
# random test of K_N
random.seed(7); fails=0; n=0
for _ in range(60000):
    N=random.randint(3,9); s=random.randint(1,N-1)  # |U|=N-1 max; use fewer allowed (merged)
    cnt=random.randint(2,N-1)
    m=F(random.randint(1,20),random.randint(1,6))
    Mmax=(N-1)**2*m/(N+1)
    vals=sorted({m*(1+F(random.randint(0,100),100)*(Mmax/m-1)) for _ in range(cnt-1)}|{m})
    M=vals[-1]
    w=M+F(random.randint(1,4000),random.randint(1,50))
    U=vals+[w]
    if M>Mmax or len(U)>N-1: continue
    t,b=solve(U,N); n+=1
    if not ok(U,N,t): fails+=1
print('random',n,'fails',fails)
