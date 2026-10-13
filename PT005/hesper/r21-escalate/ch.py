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
cnt=0;first=None
for mask in range(1<<15):
    c=0
    for i in range(15): c|=cv[i][(mask>>i)&1]
    if c==full:
        w=[W[i]+((mask>>i)&1)*M for i in range(15)]
        if sum(x%2 for x in w)>=2:
            cnt+=1; first=first or w
print("improper children 32p:",cnt,first)
# grandchildren of Astra's first child
C=[704,2,928,448,5,6,192,8,416,1120,640,160,13,14,608]
print("Astra child in set:", all(c%M==w for c,w in zip(C,W)))
N3=64*p; full3=sum(1<<t for t in range(1,N3//2+1))
cv3=[[bits(x,N3),bits(x+N2,N3)] for x in C]
g=0
for mask in range(1<<15):
    c=0
    for i in range(15): c|=cv3[i][(mask>>i)&1]
    if c==full3: g+=1
print("improper children 64p of child:",g)
