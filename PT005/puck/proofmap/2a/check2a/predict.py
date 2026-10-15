# p-free predictor: 6->7 doublability from reduced data ONLY: key = sorted multiset of (c mod 64, v in 1..31 odd, sg=sgn d7), no p anywhere.
import json, glob, sys
from collections import defaultdict, Counter
def foot(c,v,sg):
    W=pow(v,-1,64); M=(-c*W)%64
    lo,hi=(-8,7) if sg>0 else (-7,8)
    out={}
    for rho in range(lo,hi+1):
        if (rho-(M+1))%2==0 : continue          # j parity = M+1 (s odd, W odd)  -> rho ≡ M+1 mod 2
    return None
def foot2(c,v,sg):
    W=pow(v,-1,64); M=(-c*W)%64
    lo,hi=(-8,7) if sg>0 else (-7,8)
    out={}
    for rho in range(lo,hi+1):
        if (rho-(M+1))%2: continue
        s=((rho-M)*v)%64
        z=((M+s*W-rho)//64)%2
        assert (M+s*W-rho)%64==0 and s%2==1
        out[s]=z
    return out
def predict(key):
    F=[foot2(*k) for k in key]
    if any(len(f)!=8 for f in F): return False,'foot!=8'
    by=defaultdict(list)
    for i,f in enumerate(F):
        for s,z in f.items(): by[s].append((i,z))
    if sorted(by)!=list(range(1,64,2)) or any(len(x)!=2 for x in by.values()): return False,'not2cover'
    adj=defaultdict(list)
    for s,((i,zi),(j,zj)) in by.items():
        lam=1^zi^zj; adj[i].append((j,lam)); adj[j].append((i,lam))
    g={}; ok=True
    for r in range(8):
        if r in g: continue
        g[r]=0; st=[r]
        while st:
            u=st.pop()
            for y,l in adj[u]:
                if y not in g: g[y]=g[u]^l; st.append(y)
                elif g[y]!=g[u]^l: ok=False
    return ok,'xor'
if __name__=="__main__":
    tot=0;mis=0;kmap=defaultdict(set);kp=defaultdict(set);per=Counter();ex=[]
    for f in sorted(glob.glob('rows*_p*.json')):
        R=json.load(open(f))
        for r in R:
            key=tuple(tuple(x) for x in r[2]); pr,why=predict(key)
            tot+=1
            if pr!=r[3]:
                mis+=1
                if len(ex)<3: ex.append((f,key,pr,r[3],why))
            kmap[key].add(r[3]); kp[key].add(r[0]); 
            per[(f,r[3])]+=1
    print('rows',tot,'pred!=actual',mis,ex)
    print('distinct keys',len(kmap),'keys with conflicting actual flag',sum(len(v)==2 for v in kmap.values()))
    print('keys seen at >=2 primes',sum(len(v)>=2 for v in kp.values()),' of which doublable',sum(len(kp[k])>=2 and True in kmap[k] for k in kmap))
