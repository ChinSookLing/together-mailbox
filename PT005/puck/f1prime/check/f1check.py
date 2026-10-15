import sys, itertools, collections, json
def bal(x,p):
    r=x%p
    return r-p if r>p//2 else r
def members(p,b,lvl):   # lvl5: odd t<=16p, t=+-b ; lvl6: odd t<=32p, t=+-2b
    if lvl==5: return [t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
    return [t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
def cov(t,w,N):
    r=t*w%N; return 16*min(r,N-r)<N
def tilings(p,b):
    """exact k=5 tilings: 8 legal w, each covering exactly 2 level-5 members (as in Hesper/Puck census),
    members covered once, and over both lifts the 8 w cover every level-6 member exactly twice (L1)."""
    M=members(p,b,5); N=32*p; n=len(M)
    M6=members(p,b,6); N6=64*p
    W=[]
    for w in range(1,16*p,2):
        if w%p in (0,1,p-1): continue
        mk=0
        for i,t in enumerate(M):
            if cov(t,w,N): mk|=1<<i
        if bin(mk).count('1')!=2: continue
        u=[0]*len(M6)
        for e in (0,1):
            for i,t in enumerate(M6):
                if cov(t,w+e*N,N6): u[i]+=1
        W.append((w,mk,u))
    res=[]; full=(1<<n)-1
    def dfs(cur,chosen,U):
        if cur==full:
            if all(x==2 for x in U): res.append(tuple(chosen))
            return
        i=(~cur&(cur+1)).bit_length()-1
        for w,mk,u in W:
            if mk>>i&1 and mk&cur==0:
                U2=[a+c for a,c in zip(U,u)]
                if max(U2)>2: continue
                dfs(cur|mk,chosen+[w],U2)
    dfs(0,[],[0]*len(M6))
    return [tuple(sorted(x)) for x in res]
def doublable(p,b,W):
    M6=members(p,b,6); N6=64*p; full=(1<<len(M6))-1
    L=[]
    for w in W:
        l=[]
        for e in (0,1):
            ww=w+e*32*p; mk=0
            for i,t in enumerate(M6):
                if cov(t,ww,N6): mk|=1<<i
            l.append(mk)
        L.append(l)
    for es in itertools.product((0,1),repeat=len(W)):
        tot=0; ok=True
        for l,e in zip(L,es):
            m=l[e]
            if tot&m: ok=False;break
            tot|=m
        if ok and tot==full: return True
    return False
def coords(p,b,W):
    out=[]
    for w in W:
        d=bal(b*w,p); m=(b*w-d)//p
        v=pow(w,-1,32); c=(-2*m*v)%32
        out.append(dict(w=w,d=d,m=m,v=v,c=c))
    return out
def foot(c,v): return {(c+a*v)%32 for a in (-3,-1,1,3)}
def edges(C):
    E=[]
    for s in range(1,32,2):
        ij=[i for i,x in enumerate(C) if s in foot(x['c'],x['v'])]
        E.append((s,ij))
    return E
def coboundary(n,elist):  # elist (i,j,label)
    adj=collections.defaultdict(list)
    for i,j,l in elist: adj[i].append((j,l)); adj[j].append((i,l))
    col={}
    for st in range(n):
        if st in col: continue
        col[st]=0; stack=[st]
        while stack:
            u=stack.pop()
            for v,l in adj[u]:
                if v not in col: col[v]=col[u]^l; stack.append(v)
                elif col[v]!=col[u]^l: return False
    return True
def astra_q(x,s,Mrep=None):
    M=x['m']%32; a=x['w']%64
    X=2*M+s*a
    rho=[r for r in (-3,-1,1,3) if (X-r)%32==0]
    if len(rho)!=1: return None
    return ((X-rho[0])//32)%2
def gpt_h(x,s,mode):
    sc={'mod32':(s-x['c'])%32,'signed':((s-x['c']+16)%32)-16,'raw':s-x['c']}[mode]
    r=(sc*x['w'])%64
    if r in (1,3,61,63): return 0
    if r in (29,31,33,35): return 1
    return None
def crit(C,which):
    E=edges(C); el=[]
    for s,ij in E:
        if len(ij)!=2: return None
        i,j=ij
        if which=='astra':
            qi,qj=astra_q(C[i],s),astra_q(C[j],s)
        else:
            qi,qj=gpt_h(C[i],s,which),gpt_h(C[j],s,which)
        if qi is None or qj is None: return None
        el.append((i,j,1^qi^qj))
    return coboundary(len(C),el)
def oneclass(W):
    s={w%8 for w in W}; return s<= {1,7} or s<= {3,5}
def graphinfo(C):
    E=edges(C); deg=[0]*8
    for s,ij in E:
        for i in ij: deg[i]+=1
    return tuple(sorted(deg))
if __name__=='__main__':
    primes=[int(x) for x in sys.argv[1:]] or [17,19,23]
    modes=['astra','mod32','signed','raw']
    for p in primes:
        stat=collections.Counter(); dis=collections.defaultdict(list); conf=collections.Counter()
        for b in range(1,p//2+1):
            for W in tilings(p,b):
                C=coords(p,b,W); mixed=not oneclass(W)
                T=doublable(p,b,W)
                stat['tilings']+=1; stat['mixed' if mixed else 'oneclass']+=1
                if T: stat['doub_mixed' if mixed else 'doub_one']+=1
                for md in modes:
                    r=crit(C,md)
                    if r is None: stat[md+'_undef']+=1
                    elif r==T: stat[md+'_agree']+=1
                    else:
                        stat[md+'_dis']+=1
                        if len(dis[md])<3: dis[md].append((b,W,T,r))
                if T and mixed:
                    red=tuple(sorted((x['w']%64,x['m']%32,x['d']>0,x['c'],x['v']) for x in C))
                    conf[(b%2,red,graphinfo(C))]+=1
        print('p=%d'%p,dict(stat),flush=True)
        for md in dis: print('  disagreement',md,dis[md])
        for k,c in conf.items(): print('  DOUBLED-MIXED b%%2=%d degs=%s count=%d red=%s'%(k[0],k[2],c,k[1]))
