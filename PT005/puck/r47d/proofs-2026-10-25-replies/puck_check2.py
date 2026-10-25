import random
from collections import Counter
def D(x,m): r=x%m; return min(r,m-r)
def cov(T,w,M): return 16*D(T*w,M)<M
def reach(T,w,M): return any(16*D(T*(w+b*M),2*M)<2*M for b in (0,1))
# C2 counterexamples from Astra and GPT
cases=[("Astra",53,7,[6336]+[3392]*14,4965),
("GPT1",23,6,[180,644,579,1350,96,57,1366,322,777,924,1209,220,111,1400,880],115),
("GPT2",47,6,[456,138,241,1998,727,1201,1166,1042,3005,2553,956,1247,641,2751,314],2361),
("GPT3",47,7,[648,4284,1242,2697,5861,1320,4262,3749,5122,1717,3029,1013,3047,1642,4016],5421)]
for n,p,k,ws,T in cases:
    M=2**k*p
    r=[reach(T,w,M) for w in ws]; c=[cov(T,w,M) for w in ws]
    print(n,"reachers",[i for i,x in enumerate(r) if x],"parent coverers",[i for i,x in enumerate(c) if x])
# C2 part1 cover=>reach, random
rng=random.Random(20261025+1); bad=0
for _ in range(100000):
    p=rng.choice([5,7,11,13,17,19,23,29,31,37,41,43,47,53]);k=rng.randint(2,9);M=2**k*p
    w=rng.randrange(1,M);T=rng.randrange(1,M+1,2)
    if cov(T,w,M) and not reach(T,w,M): bad+=1
print("C2 part1 violations",bad)
# C5 stratified
st=Counter(); ex=Counter()
for _ in range(30000):
    p=rng.choice([5,7,11,13,17,19,23,29,31,37,41,43,47]);k=rng.randint(4,10);M=2**k*p
    d=rng.randint(1,k-3); dj=rng.randint(d+2,k-1)
    wj=2**(k-dj)*rng.randrange(1,2**dj*p,2)
    Q=2**(d+1)*p; T0=rng.randrange(1,Q,2)
    Ts=list(range(T0,M+1,Q)); N=len(Ts)
    if N%4: continue
    a=sum(reach(T,wj,M) for T in Ts)
    s=min(dj-d,4); st[s]+=1; ex[s]+= (4*a==N)
for s in sorted(st): print("dj-d",s if s<4 else ">=4","groups",st[s],"exact1/4",ex[s])
fr=Counter()
for _ in range(20000):
    p=rng.choice([5,7,11,13,17,19,23,29,31,37,41,43,47]);k=rng.randint(4,10);M=2**k*p
    d=rng.randint(1,k-3); dj=d+2
    wj=2**(k-dj)*rng.randrange(1,2**dj*p,2)
    Q=2**(d+1)*p; T0=rng.randrange(1,Q,2)
    Ts=list(range(T0,M+1,Q)); N=len(Ts)
    a=sum(reach(T,wj,M) for T in Ts); fr[(a*4)//N if N%4==0 else 'N%4']+=1
print("dj=d+2 reach fraction x4:",dict(fr))
