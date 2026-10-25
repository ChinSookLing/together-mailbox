import random
def nd(x,m):
    x%=m; return min(x,m-x)
random.seed(20261025)
bad1=bad2=badL=0; n=0; lem_d4=0
for _ in range(200000):
    p=random.choice([3,5,7,11,13,17,19,23,29,31,37,41,43,47])
    k=random.randint(2,9); d=random.randint(1,k-1)
    w1=random.randrange(1,4*p*2**k,2)
    if random.random()<0.2: w1=p*random.randrange(1,99,2)
    w=(2**(k-d))*w1; M=2**k*p
    T=random.randrange(1,M+1,2)
    if random.random()<0.2: T=p*random.randrange(1,2**k+1,2)
    reach=any(16*nd(T*(w+b*M),2*M)<2*M for b in (0,1))
    kimi = 8*nd(T*w1,2**d*p) < 2**d*p
    if reach!=kimi: bad1+=1
    cov=16*nd(T*w,M)<M
    if cov and not reach: bad2+=1
    if reach and d<=3 and (T*w1)%p==0: badL+=1
    if reach and d>=4 and (T*w1)%p==0: lem_d4+=1
    n+=1
print(n,"task1 mismatches",bad1,"cover-not-reach",bad2,"gcd-lemma violations d<=3",badL,"d>=4 reaches with p|Tw'",lem_d4)
