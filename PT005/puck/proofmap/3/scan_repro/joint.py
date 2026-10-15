import json,glob,itertools,numpy as np
from myscan import *
def fibmasks(w,p):
    M=32*p;N=2*M;tt=np.arange(1,N//2+1,2);bits=np.arange(1<<15)
    def cov(y): r=(tt*y)%N; return 16*np.minimum(r,N-r)<N
    tab=[[cov(w[i]+b*M) for b in (0,1)] for i in range(15)]
    fib={}
    for j,t in enumerate(tt):
        r=int(t%p);r=min(r,p-r);fib.setdefault(r,[]).append(j)
    ok={}
    for r,js in fib.items():
        idx=np.array(js);acc=np.zeros((1<<15,len(idx)),bool)
        for i in range(15):
            acc|=np.where(((bits>>i)&1)[:,None]==1,tab[i][1][idx][None,:],tab[i][0][idx][None,:])
        ok[r]=acc.all(axis=1)
    return ok
seen={}
for f in glob.glob('my_p*_s*.json'):
    for r in json.load(open(f)): seen[(r['p'],tuple(sorted(r['w'])))]=r
res=[]
for (p,_),r in seen.items():
    if r['children']==0 and r['ndead']==0:
        ok=fibmasks(r['w'],p); keys=list(ok); mn=None
        for k in (2,3):
            for c in itertools.combinations(keys,k):
                a=ok[c[0]].copy()
                for x in c[1:]: a&=ok[x]
                if not a.any(): mn=(k,c);break
            if mn:break
        if not mn:
            # greedy
            a=np.ones(1<<15,bool);s=[]
            for x in sorted(keys,key=lambda x:ok[x].sum()):
                a&=ok[x];s.append(x)
                if not a.any():break
            mn=(len(s),'greedy')
        res.append((p,r['f'],mn,{k:int(v.sum()) for k,v in sorted(ok.items())}))
        print(p,r['f'],mn[0],mn[1],min(int(v.sum()) for v in ok.values()),flush=True)
