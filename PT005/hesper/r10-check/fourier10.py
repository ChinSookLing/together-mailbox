import itertools, math, random, sys
def run(p,S,K=4,W=4):
    H=(p-1)//16; n=len(S)
    def bh(k):
        k%=p
        if k==0: return 1-(2*H+1)/p
        return -(1/p)*math.sin(math.pi*(2*H+1)*k/p)/math.sin(math.pi*k/p)
    B=[1 if min(x%p,(-x)%p)>H else 0 for x in range(p)]
    U=sum(math.prod(B[v*t%p] for v in S) for t in range(p))/2
    M=p/2*bh(0)**n
    b0=bh(0); byw={}; top=[]
    ks=[k for k in range(-K,K+1) if k]
    for w in range(1,W+1):
        tot=0
        for idx in itertools.combinations(range(n),w):
            for co in itertools.product(ks,repeat=w):
                if sum(c*S[i] for c,i in zip(co,idx))%p==0:
                    term=p/2*math.prod(bh(c) for c in co)*b0**(n-w)
                    tot+=term; top.append((term,[(c,S[i]) for c,i in zip(co,idx)]))
        byw[w]=tot
    top.sort()
    return U,M,byw,top
for name,p,S in [("457cover",457,[1,2,55,60,68,111,112,113,114,115,116,117,169,221]),
                 ("337cover",337,[1,7,15,40,43,58,63,65,83,101,106,108,115,164])]+[("rand457_%d"%s,457,sorted(random.Random(s).sample(range(1,229),14))) for s in (1,2)]:
    U,M,byw,top=run(p,S)
    print(name,"U=",U,"M=%.2f"%M,"short(w<=4,|k|<=4) by weight:",{w:round(v,2) for w,v in byw.items()},"sum=%.2f"%sum(byw.values()),"needed R=%.2f"%(U-M))
    print("  most negative:",[(round(t,3),r) for t,r in top[:4]])
