import random
def bal(x,n):
    r=x%n; return r-n if r>n//2 else r
def cov(t,w,N):
    r=t*w%N; return 16*min(r,N-r)<N
ps=[p for p in range(17,2000) if all(p%q for q in range(2,int(p**.5)+1))]
random.seed(7); n=f=0
for _ in range(3000):
    p=random.choice(ps); b=random.randrange(2,p-1)
    w=random.randrange(1,16*p,2)
    if w%p in (0,1,p-1): continue
    d=bal(b*w,p); m=(b*w-d)//p; A=w%64
    for t in range(1,32*p,2):
        if t%p not in ((2*b)%p,(-2*b)%p): continue
        eps=1 if (t-2*b)%p==0 else -1
        u=(t-eps*2*b)//p          # odd
        s=(eps*u)%32; h=((eps*u)-s)//32
        for a in (0,1):
            if cov(t,w+32*p*a,64*p):
                rho=bal(2*m+s*w,32)  # in (-16,16]
                z=((2*m+s*A-rho)//32)%2
                n+=1; f+= (a!=(z+h)%2) or abs(rho) not in (1,3)
print('incidences',n,'fails',f)
