# Puck: parallel full-tree run + exact min dead fibre set + depth after f>=9 first reached.
import sys, json, collections, numpy as np
from multiprocessing import Pool
from puck_tree import fibre_ok, L7, v2, odd_count, canon
def exact_min_S(oks):
    # minimum number of fibres whose ok-sets have empty intersection (exact, iterative deepening DFS on bitsets)
    full=(1<<(1<<15))-1
    bs={r:int.from_bytes(np.packbits(o[::-1]).tobytes(),'big') for r,o in oks.items()}
    rs=sorted(bs,key=lambda r:bin(bs[r]).count('1'))
    allint=full
    for r in rs: allint&=bs[r]
    if allint: return None,None   # even all fibres together leave a live mask
    def dfs(cur,start,depth,chosen):
        if cur==0: return list(chosen)
        if depth==0: return None
        for j in range(start,len(rs)):
            res=dfs(cur&bs[rs[j]],j+1,depth-1,chosen+[rs[j]])
            if res: return res
        return None
    for d in range(1,len(rs)+1):
        r=dfs(full,0,d,[])
        if r: return d,r
def work(args):
    u,M,p,lvl9=args
    k=v2(M); f=sum(1 for x in u if v2(x)<k)
    oks=fibre_ok(u,M,p); alive=np.ones(1<<15,dtype=bool)
    for o in oks.values(): alive&=o
    kids=[[int(u[i])+((int(m)>>i)&1)*M for i in range(15)] for m in np.nonzero(alive)[0]]
    if lvl9 is None and f>=9: lvl9=M//p
    out=[];closed=0;pb=0
    for s in kids:
        if odd_count(s)<2: pb+=1; continue
        if L7(s,2*M) is None: out.append((canon(s,2*M),s))
        else: closed+=1
    dead=None
    if not kids:
        S,Ss=exact_min_S(oks); dead={"w":u,"f":f,"S":S,"Sset":Ss,"lvl9":lvl9,"level_p":M//p}
    return out,closed,pb,f,lvl9,dead
def run(label,w,M,p,maxM):
    lev={canon(w,M):(list(w),None)}; deads=[]
    with Pool(8) as pool:
        while lev and M<=maxM:
            res=pool.map(work,[(u,M,p,l9) for (u,l9) in lev.values()],chunksize=4)
            nxt={};st=collections.Counter();Sh=collections.Counter();fh=collections.Counter()
            for out,closed,pb,f,l9,dead in res:
                st['closedL7']+=closed; st['parity_bad_kids']+=pb; fh[f]+=1
                for c,s in out:
                    if c not in nxt or (l9 is not None and (nxt[c][1] is None or l9<nxt[c][1])): nxt[c]=(s,l9)
                if dead:
                    deads.append(dead); Sh[str(dead['S'])]+=1; st['died']+=1
                    if dead['lvl9'] is not None:
                        st['died_after_f9']+=1; st[f"death_depth_after_f9={ (M//p)//dead['lvl9'] }x"]+=1
            print(json.dumps({"label":label,"level_p":M//p,"open":len(lev),"f_hist":dict(sorted(fh.items())),**st,"S_hist":dict(Sh),"kids_open":len(nxt)}),flush=True)
            lev=nxt; M*=2
    print(json.dumps({"label":label,"END":"no open nodes" if not lev else f"{len(lev)} open at {M//p}p"}),flush=True)
    return deads
if __name__=="__main__":
    which=sys.argv[1]
    if which=="p47": d=run("Astra R p=47",[1,2,3,5,6,8,9,10,11,12,13,14,15,20,21],47,47,128*47)
    json.dump(d,open(f"dead2_{which}.json","w"))
