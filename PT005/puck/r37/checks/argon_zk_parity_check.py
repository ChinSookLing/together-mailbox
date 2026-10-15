# Puck independent: on FACT/cex W-sets, z-k vertex-constant and cycle-oddness z==k
from collections import defaultdict
def bal(x,n):
    r=x%n; return r-n if r>n//2 else r
def odd_cycle(labels_by_s):
    adj=defaultdict(list)
    for s,(i,li,j,lj) in labels_by_s.items():
        l=1^li^lj; adj[i].append((j,l)); adj[j].append((i,l))
    g={}; odd=0
    for r in range(8):
        if r in g: continue
        g[r]=0; st=[r]
        while st:
            x=st.pop()
            for y,l in adj[x]:
                if y not in g: g[y]=g[x]^l; st.append(y)
                elif g[y]!=g[x]^l: odd+=1
    return odd
def check(name,p,b,W):
    red=[]
    for w in W:
        d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32); c=(-2*m*v)%32
        red.append((w,m,c,v))
    pos=defaultdict(list)
    for i,(w,m,c,v) in enumerate(red):
        for delta in (1,-1,3,-3):
            s=(c+delta*v)%32
            rho=bal(2*m+s*w,32); z=((2*m+s*w-rho)//32)%2
            k=((s-c-delta*v)//32)%2
            pos[s].append((i,z,k))
    odd=list(range(1,32,2))
    assert all(len(pos[s])==2 for s in odd)
    for i in range(8):
        diffs=set()
        for s in odd:
            for (ii,z,k) in pos[s]:
                if ii==i: diffs.add((z-k)%2)
        assert len(diffs)==1, (name,i,diffs)
    lz={}; lk={}
    for s in odd:
        (i,zi,ki),(j,zj,kj)=pos[s]
        lz[s]=(i,zi,j,zj); lk[s]=(i,ki,j,kj)
    oz,ok=odd_cycle(lz),odd_cycle(lk)
    print(name,'odd_z',oz,'odd_k',ok,'match',oz==ok); assert oz==ok
check('p29',29,1,[3,97,125,151,413,191,285,385])
check('p79',79,76,[865,993,675,289,385,579,545,673])
check('p89',89,36,[1345,545,1089,129,673,587,139,1035])
check('ham103',103,35,[1505,1481,143,263,227,1445,179,1397])
check('ham1009',1009,500,[449,3161,1353,1167,917,1571,45,699])
print('OK')
