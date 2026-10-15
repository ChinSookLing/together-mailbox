import random
def bal(x,n):
    r=x%n; return r-n if r>n//2 else r
ps=[p for p in range(17,3000) if all(p%q for q in range(2,int(p**.5)+1))]
random.seed(11); tested=bad=0
for _ in range(20000):
    p=random.choice(ps); b=random.randrange(2,p-1); w=random.randrange(1,16*p,2)
    if w%p in (0,1,p-1): continue
    d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32); c=(-2*m*v)%32
    diffs=set()
    for delta in (1,-1,3,-3):
        s=(c+delta*v)%32
        rho=bal(2*m+s*w,32); z=((2*m+s*w-rho)//32)%2
        assert rho==delta, (rho,delta)
        k=(s-c-delta*v)//32
        diffs.add((z-k)%2)
    tested+=1; bad+= len(diffs)>1
print('coords',tested,'z-k not vertex-constant',bad)
