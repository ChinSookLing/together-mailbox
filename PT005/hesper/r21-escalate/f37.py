p=37;M=16*p;N2=32*p
W=[112,2,336,448,5,6,192,8,416,528,48,160,13,14,16]
def bits(u,N):
    b=0
    for t in range(1,N//2+1):
        r=(t*u)%N
        if 16*min(r,N-r)<N: b|=1<<t
    return b
full=sum(1<<t for t in range(1,N2//2+1))
cv=[[bits(x,N2),bits(x+M,N2)] for x in W]
S=[]
for mask in range(1<<15):
    c=0
    for i in range(15): c|=cv[i][(mask>>i)&1]
    if c==full: S.append(mask)
F=[i for i in range(15) if len({(m>>i)&1 for m in S})==2]
print(len(S),"free",F,[W[i] for i in F],"subcube",len(S)==2**len(F))
