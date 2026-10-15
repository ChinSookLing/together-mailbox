# PT005 Link 3.0b — W5-type test (Hesper). Definitions as verify_gpt_w5.py / verify_64p.py:
# node w (15 coords) at modulus M=2^k p is improper iff every t in 1..M/2 has 16*dist(t*x,M)<M for some x, and >=2 odd coords.
# children: x -> x or x+M, checked at 2M. Even t at 2M are always covered (inherited), so only odd t matter.
# frozen at modulus M=2^k p: v2(x)<k. fibre of odd t at 2M = pair {+-t mod p}.
import sys, numpy as np, json
def v2(x):
    c=0
    while x%2==0 and x: x//=2; c+=1
    return c
def covered(t,x,N): r=(t*x)%N; return 16*min(r,N-r)<N
def improper(w,M):
    if sum(x%2 for x in w)<2: return False
    return all(any(covered(t,x,M) for x in w) for t in range(1,M//2+1))
def analyse(w,M,p):
    k=v2(M)
    N=2*M
    frozen=[i for i,x in enumerate(w) if v2(x)<k]
    nonfz=[i for i in range(15) if i not in frozen]
    # free pairs at node level (odd t at M, covered by non-frozen only?) -> use fibres of odd t at 2M
    odd=[t for t in range(1,N//2+1,2)]
    pairs={}
    for t in odd:
        r=t%p; r=min(r,p-r); pairs.setdefault(r,[]).append(t)
    # which pairs are covered at 2M by nonfrozen coords under BOTH lifts (lift-independent coverage)
    res={}
    bits=np.arange(1<<15,dtype=np.int64)
    alive_all=np.ones(1<<15,dtype=bool)
    if sum(1 for x in w if x%2)<2: pass
    for r,ts in sorted(pairs.items()):
        nw=(len(ts)+63)//64
        acc=np.zeros((1<<15,nw),dtype=np.uint64)
        for i,x in enumerate(w):
            tab=np.zeros((2,nw),dtype=np.uint64)
            for b in (0,1):
                y=x+b*M
                for j,t in enumerate(ts):
                    if covered(t,y,N): tab[b,j//64]|=np.uint64(1)<<np.uint64(j%64)
            acc|=tab[(bits>>i)&1]
        full=np.zeros(nw,dtype=np.uint64)
        for j in range(len(ts)): full[j//64]|=np.uint64(1)<<np.uint64(j%64)
        ok=np.all(acc==full,axis=1)
        nf_cov=all(any(covered(t,w[i]+b*M,N) for i in nonfz) for t in ts for b in (0,)) and \
               all(any(covered(t,w[i]+M,N) for i in nonfz) for t in ts)
        res[r]={"n_t":len(ts),"children_ok":int(ok.sum()),"nonfrozen_cover_both_lifts":nf_cov}
        alive_all&=ok
    # >=2 odd coords in child: lift doesn't change parity (M even), so same as parent
    nodd=sum(x%2 for x in w)
    surv=[ [w[i]+((m>>i)&1)*M for i in range(15)] for m in np.nonzero(alive_all)[0]] if nodd>=2 else []
    free=[r for r in res if res[r]["children_ok"]<(1<<15)]
    nodefree=sorted({min(t%p,p-t%p) for t in range(1,M//2+1,2) if not any(covered(t,w[i],M) for i in nonfz)})
    nodefree=sorted({min(t%p,p-t%p) for t in range(1,M//2+1,2) if not any(covered(t,w[i],M) for i in nonfz)})
    tot=1<<15
    prod=1.0
    for r in free: prod*=res[r]["children_ok"]/tot
    return {"M_over_p":M//p,"f":len(frozen),"frozen_count_E":len(frozen),
            "node_free_pairs_opus_def":nodefree,"child_fibres_dead":[r for r in free if res[r]["children_ok"]==0],
            "per_free_pair":{r:res[r]["children_ok"] for r in free},
            "survivors":len(surv),"indep_prediction":round(prod*tot,2)}, surv
def canon(w,M): return tuple(sorted(min(x%M,(-x)%M) for x in w))
def track(w,M,p,maxlev,label,out):
    lev=[(w,M)]; 
    while lev and lev[0][1]//p<=maxlev:
        nxt=[];seen=set()
        for (u,Mu) in lev:
            info,surv=analyse(u,Mu,p)
            info["label"]=label
            out.append(info); print(json.dumps(info),flush=True)
            for s in surv:
                c=canon(s,2*Mu)
                if c not in seen: seen.add(c); nxt.append((s,2*Mu))
        print(f"# {label}: level {lev[0][1]//p}p nodes {len(lev)} -> {len(nxt)} distinct improper children at {2*lev[0][1]//p}p",flush=True)
        lev=nxt
if __name__=="__main__" and sys.argv[1:]==["p37"]:
    out=[];p=37;W16=[112,2,336,448,5,80,192,8,416,528,48,160,13,236,16]
    print("W16 improper@16p",improper(W16,16*p))
    track(W16,16*p,p,128,"W16 p=37",out)
    json.dump(out,open("w16p37_out.json","w"),indent=1)
elif __name__=="__main__" and sys.argv[1:]==["p37"]:
    out=[];p=37;W16=[112,2,336,448,5,80,192,8,416,528,48,160,13,236,16]
    print("W16 improper@16p",improper(W16,16*p))
    track(W16,16*p,p,128,"W16 p=37",out)
    json.dump(out,open("w16p37_out.json","w"),indent=1)
elif __name__=="__main__":
    out=[]
    p=17; W5=[189,224,72,447,176,500,144,128,384,266,80,64,48,32,16]
    print("W5 improper@32p",improper(W5,32*p))
    track(W5,32*p,p,256,"W5 p=17",out)
    json.dump(out,open("w5test_out.json","w"),indent=1)
