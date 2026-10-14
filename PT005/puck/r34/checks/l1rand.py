import random
def isprime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
random.seed(34)
bad=0;n=0
def bal(x,p):
    d=x%p; return d-p if d>p//2 else d
def hit(t,W,M):
    r=t*W%M; return 16*min(r,M-r)<M
PR=[q for q in range(17,200000) if isprime(q)]
for _ in range(4000):
    p=random.choice(PR); b=random.randrange(1,(p+1)//2)
    w=random.randrange(1,16*p,2)
    if w%p in (0,1,p-1): continue
    d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32); c=(-2*m*v)%32
    U={(c+x*v)%32 for x in (-3,-1,1,3)}
    for eps in (1,-1):
        for u in range(-3,35):
            t=eps*2*b+p*u
            if not (1<=t<=32*p and t%2): continue
            n+=1
            E=[e for e in (0,1) if hit(t,w+32*p*e,64*p)]
            s=(eps*u)%32
            if (s in U)!=(len(E)==1) or len(E)>1: bad+=1
print("members tested",n,"bad",bad)
