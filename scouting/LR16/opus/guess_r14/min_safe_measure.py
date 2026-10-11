import itertools, sys
d=1/16
def m(K):
    bad=[]
    for k in K:
        for i in range(k+1):
            a=max((i-d)/k,0.0); b=min((i+d)/k,1.0)
            if a<b: bad.append((a,b))
    bad.sort(); cov=0; ca=cb=None
    for a,b in bad:
        if cb is None or a>cb:
            if cb is not None: cov+=cb-ca
            ca,cb=a,b
        elif b>cb: cb=b
    cov+=cb-ca
    return 1-cov
Mx=int(sys.argv[1]); res=[]
for K in itertools.combinations(range(1,Mx+1),14):
    if K[-1]!=Mx and Mx>14: continue   # only sets whose max is exactly Mx (others done at smaller Mx)
    res.append((m(K),K))
res.sort(); print(Mx,len(res),[(round(a,5),b) for a,b in res[:3]])
