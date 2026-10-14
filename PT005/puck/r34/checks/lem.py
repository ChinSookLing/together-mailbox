# Puck R34 independent check of the HAND steps of L1-L4 (not just conclusions).
from collections import defaultdict, Counter
def bal(x,p):
    d=x%p
    return d-p if d>p//2 else d
def hit(t,W,M):
    r=t*W%M; return 16*min(r,M-r)<M
def check(p,b,W,verbose=False):
    N5,N6=32*p,64*p
    out={}
    C6=[t for t in range(1,N5+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
    assert len(C6)==32
    par=[]
    for w in W:
        d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32); c=(-2*m*v)%32
        assert (2*m+c*w)%32==0
        par.append((d,m,v,c))
    # integer position s' = eps*u for each member
    mem={}
    for t in C6:
        for eps in (1,-1):
            if (t-eps*2*b)%p==0:
                u=(t-eps*2*b)//p; mem[t]=(eps,u,eps*u); break
    # --- L1 hand step: covered iff rho in {+-1,+-3}, by exactly lift e==z mod 2
    hitby=defaultdict(list); L1ok=True; Zrec={}
    for i,w in enumerate(W):
        d,m,v,c=par[i]; U={(c+x*v)%32 for x in (-3,-1,1,3)}
        for t in C6:
            eps,u,sp=mem[t]
            q=2*m+sp*w; rho=((q+16)%32)-16; z=(q-rho)//32
            E=[e for e in (0,1) if hit(t,w+N5*e,N6)]
            pred=[z%2] if abs(rho)<=3 else []
            if E!=pred: L1ok=False
            if (sp%32 in U)!=(abs(rho)<=3): L1ok=False
            for e in E: hitby[t].append((i,e)); Zrec[(i,t)]=(z,rho)
    out['L1']=L1ok
    ok2=all(len(h)==2 and h[0][0]!=h[1][0] for h in hitby.values()) and len(hitby)==32
    out['exact2cover']=ok2
    if not ok2: return out
    # label per member, and label by position mod 32
    lab={t:h[0][1]^h[1][1]^1 for t,h in hitby.items()}
    poslab=defaultdict(set); posedge=defaultdict(set)
    for t,h in hitby.items():
        s=mem[t][2]%32; poslab[(s,)].add(lab[t]); posedge[s].add(tuple(sorted((h[0][0],h[1][0]))))
        # label == 1+z_i+z_j
        (i,_),(j,_)=h
        if lab[t]!=(1+Zrec[(i,t)][0]+Zrec[(j,t)][0])%2: out['lab_z']=False
    out.setdefault('lab_z',True)
    out['label_depends_only_on_s']=all(len(x)==1 for x in poslab.values()) and all(len(x)==1 for x in posedge.values())
    # graph
    pairs=defaultdict(set)
    for s,E in posedge.items():
        for e in E: pairs[e].add(s)
    adj=defaultdict(set)
    for (i,j) in pairs: adj[i].add(j); adj[j].add(i)
    ham= len(pairs)==8 and all(len(adj[i])==2 for i in range(8))
    if ham:
        order=[0];prev=None
        while len(order)<8:
            x=order[-1]; y=[z for z in adj[x] if z!=prev and z not in order]
            if not y: ham=False;break
            prev=x; order.append(y[0])
    out['ham8']=ham
    alt=all((W[i]*pow(W[j],-1,8))%8 in (3,5) for (i,j) in pairs)
    out['alternating']=alt
    if not ham: return out
    # --- L2 hand step: deltas
    L2ok=True; inner_outer={}
    for (i,j),S in pairs.items():
        if len(S)!=2: L2ok=False; continue
        s1,s2=sorted(S)
        X={}
        for k in (i,j):
            d,m,v,c=par[k]; X[k]=[((s-c)*W[k]+16)%32-16 for s in (s1,s2)]
        di=X[i][0]-X[i][1]; dj=X[j][0]-X[j][1]
        r=(W[j]*pow(W[i],-1,32))%32
        if (dj-r*di)%32: L2ok=False
        if sorted((abs(di),abs(dj)))!=[2,6]: L2ok=False
        if not ((abs(di)==2)==((r%16) in (3,13))): L2ok=False
        inner_outer[(i,j)]=(i,j) if abs(di)==2 else (j,i)  # inner end -> outer end
    outer_used=Counter(o for (_,o) in inner_outer.values())
    inner_used=Counter(a for (a,_) in inner_outer.values())
    L2ok &= all(outer_used[k]==1 and inner_used[k]==1 for k in range(8))
    out['L2']=L2ok
    # --- L3 hand step: carries
    L3ok=True; consistent=True
    for (i,j),S in pairs.items():
        s1,s2=sorted(S)
        # use the actual integer s' of one member at each position (same rep for i and j)
        reps={}
        for t in C6:
            if mem[t][2]%32 in (s1,s2) and mem[t][2]%32 not in reps: reps[mem[t][2]%32]=(t,mem[t][2])
        (ta,a),(tb,bb)=reps[s1],reps[s2]
        lamdiff=lab[ta]^lab[tb]
        if lab[ta]!=lab[tb]: consistent=False
        nn={}
        for k in (i,j):
            ck=par[k][3]
            tot=a+bb-2*ck
            if tot%32: L3ok=False
            nn[k]=tot//32
            za,ra=Zrec[(k,ta)]; zb,rb=Zrec[(k,tb)]
            if ra!=-rb: L3ok=False
            hk=(2*par[k][1]+ck*W[k])//32
            if za+zb!=2*hk+nn[k]*W[k]: L3ok=False
        if (nn[i]-nn[j])*16!=par[j][3]-par[i][3]: L3ok=False
        if lamdiff!=(((par[i][3]-par[j][3])//16)%2): L3ok=False
    out['L3']=L3ok; out['consistent']=consistent
    out['common_c']=len({x[3] for x in par})==1
    if not (consistent and out['common_c']): return out
    # --- L4 hand step: directed cycle inner->outer, w_out=3 sig w_in+32k, lambda=1+h+h'+k
    c=par[0][3]; h=[(2*par[k][1]+c*W[k])//32 for k in range(8)]
    nxt={a:o for (a,o) in inner_outer.values()}
    L4ok=True; K=[]; Lam=[]; sig=[]
    for a,o in nxt.items():
        ks=[(sg,(W[o]-3*sg*W[a])//32) for sg in (1,-1) if (W[o]-3*sg*W[a])%32==0]
        if len(ks)!=1: L4ok=False; continue
        sg,k=ks[0]; K.append(k); sig.append(sg)
        lam=lab[next(t for t,hh in hitby.items() if {hh[0][0],hh[1][0]}=={a,o})]
        Lam.append(lam)
        if lam!=(1+h[a]+h[o]+k)%2: L4ok=False
    # directed cycle is a single 8-cycle
    x=0; seen=[]
    for _ in range(8): seen.append(x); x=nxt[x]
    L4ok &= (x==0 and len(set(seen))==8)
    prod=1
    for sg in sig: prod*=sg
    out['L4']=L4ok; out['prod_sigma']=prod; out['sumK_odd']=sum(K)%2==1; out['H']=sum(Lam)%2
    if verbose:
        out['cycle_inner_to_outer']=seen; out['K']=K; out['c']=c
    return out
if __name__=="__main__":
    A=(103,35,[1505,1481,143,263,227,1445,179,1397])
    B=(1009,500,[449,3161,1353,1167,917,1571,45,699])
    for nm,(p,b,W) in (("A",A),("B",B)):
        print(nm,check(p,b,W,True))
