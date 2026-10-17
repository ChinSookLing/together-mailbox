# Puck independent F3 check for PT005 chair note 97 (§4). Own engine (numpy), built from the R43 COMMON definitions.
# Does NOT import Opus r43chk or Hesper tree3/scan code. Reuses only Puck's own chain/row vectors.
#
# Node at level M = p*2^k: 15 ints w_i in 1..M-1 (multiset).
#   covered(T): some i with 16*||T*w_i||_M < M.   improper: all T in 1..M/2 covered and >=2 odd w_i.
#   L7-closed: some even D | M with E_D={i: D∤w_i}, |E_D|>=2, sum_{E_D} g_i*ceil((D/g_i)/8) < D (g_i=gcd(D,w_i)).
#   open: improper and not L7-closed.
# Children at 2M: each coordinate w_i or w_i+M (2^15 lifts), deduplicated as multisets, kept if open at 2M.
#   Given an improper parent, even T at 2M are covered automatically (||2T'(w+bM)||_{2M} = 2||T'w||_M),
#   so a lift is improper at 2M iff all odd T<=M are covered at modulus 2M and >=2 coords are odd.
#   (Checked directly with the full definition on a random sample of children: see SELFTEST.)
# Counts at M=p*2^k: E=#{v2(w_i)<k}, F3=#{k-v2(w_i)>=3}, F4 (>=4), F5 (>=5).
import sys, json, time, glob, os, random
from math import gcd
import numpy as np

def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c
def counts(w,M,p):
    k=(M//p).bit_length()-1
    d=[k-v2(x) for x in w]
    return {"E":sum(1 for t in d if t>=1),"F3":sum(1 for t in d if t>=3),"F4":sum(1 for t in d if t>=4),"F5":sum(1 for t in d if t>=5)}

# ---------- direct (slow, literal) definitions, used for root checks and self-test ----------
def dist(x,M): r=x%M; return min(r,M-r)
def improper_direct(w,M):
    if sum(x&1 for x in w)<2: return False
    return all(any(16*dist(T*x,M)<M for x in w) for T in range(1,M//2+1))
def l7_closed_direct(w,M):
    for D in range(2,M+1,2):
        if M%D: continue
        E=[x for x in w if x%D]
        if len(E)>=2 and sum(gcd(D,x)*(-(-(D//gcd(D,x))//8)) for x in E)<D: return True
    return False
def open_direct(w,M): return improper_direct(w,M) and not l7_closed_direct(w,M)

# ---------- fast vectorised child enumeration ----------
def even_divisors(N): return [D for D in range(2,N+1,2) if N%D==0]
def l7_closed_vec(S,N):
    # S: (n,15) int64 array of nodes at modulus N. Returns bool array closed.
    closed=np.zeros(len(S),bool)
    for D in even_divisors(N):
        nz=(S%D)!=0
        g=np.gcd(S,D)
        term=g*(-(-(D//g)//8))
        tot=np.where(nz,term,0).sum(1)
        closed|=(nz.sum(1)>=2)&(tot<D)
    return closed
LOB=np.arange(128); HIB=np.arange(256)
def open_children(w,M):
    """All distinct (multiset) open children at 2M of an improper node w at M. Returns sorted list of tuples."""
    N=2*M; w=np.array(w,dtype=np.int64)
    T=np.arange(1,M+1,2,dtype=np.int64)          # odd T <= N/2
    Y=np.stack([w,w+M],1)                          # (15,2)
    R=(Y[:,:,None]*T[None,None,:])%N
    C=16*np.minimum(R,N-R)<N                       # (15,2,nt)
    P=np.packbits(C,axis=2)                        # (15,2,nb) uint8
    full=np.packbits(np.ones(len(T),bool))
    lo=P[0]                                        # (2,nb), index = bit of coord0
    for i in range(1,7): lo=np.concatenate([lo|P[i,0],lo|P[i,1]])
    hi=P[7]
    for i in range(8,15): hi=np.concatenate([hi|P[i,0],hi|P[i,1]])
    ok=np.all((hi[:,None,:]|lo[None,:,:])==full,axis=2).reshape(-1)   # index m = h*128+l
    m=np.nonzero(ok)[0]
    if len(m)==0: return [],0
    bits=(m[:,None]>>np.arange(15)[None,:])&1
    S=w[None,:]+bits*M
    S=S[(S&1).sum(1)>=2]
    if len(S)==0: return [],len(m)
    S=np.unique(np.sort(S,1),axis=0)
    S=S[~l7_closed_vec(S,N)]
    return [tuple(int(x) for x in r) for r in S],len(m)

def canon_pm(w,M): return tuple(sorted(min(x%M,(-x)%M) for x in w))

def run_tree(label,start,M0,p,maxM,log):
    """Full tree from an OPEN start node at M0. Returns list of levels; each level: list of dicts."""
    start=tuple(sorted(start))
    assert open_direct(list(start),M0), f"{label}: start not open at {M0}"
    levels=[]; cur={start:0}; M=M0; t0=time.time()
    while cur and M<=maxM:
        nodes=list(cur.keys()); recs=[]; nxt={}
        for w in nodes:
            kids,_=open_children(w,M)
            ids=[]
            for c in kids:
                if c not in nxt: nxt[c]=len(nxt)
                ids.append(nxt[c])
            r={"w":list(w),"M":M,"open_children":len(kids),"kid_ids":ids}; r.update(counts(w,M,p)); recs.append(r)
        levels.append(recs)
        line={"label":label,"level_p":M//p,"open_nodes":len(nodes),"open_nodes_pm_canon":len({canon_pm(w,M) for w in nodes}),
              "children_open_next":len(nxt),"secs":round(time.time()-t0,1)}
        print(json.dumps(line),flush=True); log.append(line)
        cur=nxt; M*=2
    truncated=bool(cur)
    if truncated: print(json.dumps({"label":label,"TRUNCATED_at_level_p":M//p,"open":len(cur)}),flush=True)
    # heights (number of further doublings with an open descendant), bottom-up
    for L in range(len(levels)-1,-1,-1):
        for r in levels[L]:
            if L+1<len(levels): r["height"]=0 if not r["kid_ids"] else 1+max(levels[L+1][i]["height"] for i in r["kid_ids"])
            else: r["height"]=0 if (not truncated or not r["kid_ids"]) else None
    return levels,truncated

if __name__=="__main__":
    out_json=sys.argv[1] if len(sys.argv)>1 else "puck_f3_nodes.json"
    random.seed(20261017)
    D="/workspace/mbx_pt5/PT005"
    trees=[]
    # (A) full real trees from the root, rows as in Hesper pre-R43 / Puck realtree runs
    trees.append(("p47 Astra row (realtree)",[1,2,3,5,6,8,9,10,11,12,13,14,15,20,21],47,47))
    trees.append(("p53 seed20261016 row",[3,5,6,7,8,9,11,14,15,17,21,23,26,26,26],53,53))
    trees.append(("p59 seed20261016 row",[1,4,5,5,6,7,11,16,17,18,20,21,23,28,29],59,59))
    trees.append(("p61 seed20261016 row",[1,2,5,6,11,11,12,14,16,18,23,26,27,29,30],61,61))
    # (B) the four counterexample chains: FULL trees from their roots (contain every chain node and all its open children)
    trees.append(("GPT p47 chain root",[2,4,5,6,7,8,10,11,13,15,17,18,19,22,23],47,47))
    trees.append(("Astra p43 chain root",[2,5,5,6,8,9,13,14,16,16,17,18,19,20,21],43,43))
    # p=17 roots: the full tree from the root has 514092 open nodes already at 4p (Astra p17) -> too large for this box.
    # Instead: FULL subtree from the chain's 2p node (contains the 4p and 8p chain nodes and ALL their open children
    # and all further descendants); the root's own open-children count is reported separately.
    trees.append(("Astra p17 chain @2p",[1,1,3,3,3,5,6,7,7,8,8,18,19,21,22],17,34))
    trees.append(("Grok p17 chain @2p",[8,11,11,15,3,5,15,11,7,16,1,15,16,3,13],17,34))
    # (C) W5 (p=17, start at 32p)
    trees.append(("W5 p17 @32p",[189,224,72,447,176,500,144,128,384,266,80,64,48,32,16],17,32*17))
    chains={  # chain nodes per level, to be located in the trees
      "GPT p47":(47,[[2,4,5,6,7,8,10,11,13,15,17,18,19,22,23],[49,51,5,6,7,55,57,11,13,62,17,18,19,69,23],[143,51,5,6,7,149,57,11,107,62,17,112,113,163,23],[143,51,193,194,195,149,245,199,295,62,205,112,113,351,23]],"GPT p47 chain root"),
      "Astra p43":(43,[[2,5,5,6,8,9,13,14,16,16,17,18,19,20,21],[2,5,9,13,16,19,48,49,51,57,59,60,61,63,64],[2,13,16,48,49,51,91,95,105,143,145,146,147,149,150],[2,13,16,49,91,105,143,146,220,223,267,317,319,321,322]],"Astra p43 chain root"),
      "Astra p17":(17,[[1,1,1,2,3,3,3,4,5,5,6,7,7,8,8],[1,1,3,3,3,5,6,7,7,8,8,18,19,21,22],[1,3,3,5,6,7,8,18,19,21,22,35,37,41,42],[1,3,8,21,22,35,37,41,42,71,73,74,75,86,87]],"Astra p17 chain @2p"),
      "Grok p17 (repaired)":(17,[[8,11,11,15,3,5,15,11,7,16,1,15,16,3,13],[8,11,11,15,3,5,15,11,7,16,1,15,16,3,13],[1,3,5,7,8,11,11,13,15,15,16,37,45,49,50],[8,113,11,49,37,73,83,11,75,50,1,15,16,3,13]],"Grok p17 chain @2p"),
    }
    # (D) f>=9 scan nodes at 32p: Hesper's 140 (vectors only, from his JSON) + Puck's own 422 (puck_scan_nodes/)
    scan=[]
    for f in sorted(glob.glob(D+"/hesper/proofmap/3/l30b/scan/*.json")):
        d=json.load(open(f))
        for n in d["nodes"]: scan.append(("Hesper scan",d["p"],n["w32p"]))
    here=os.path.dirname(os.path.abspath(__file__))
    for f in sorted(glob.glob(here+"/puck_scan_nodes/my_p*.json")):
        for n in json.load(open(f)): scan.append(("Puck scan",n["p"],n["w"]))

    result={"trees":{},"chains":{},"scan":[]}
    log=[]
    # SELFTEST: compare fast child test against literal definitions on random lifts of a few nodes
    st_ok=0; st_n=0
    for (w,M) in [([1,2,3,5,6,8,9,10,11,12,13,14,15,20,21],47),([189,224,72,447,176,500,144,128,384,266,80,64,48,32,16],544),([8,11,11,15,3,5,15,11,7,16,1,15,16,3,13],34)]:
        kids,_=open_children(w,M); ks=set(kids)
        for _ in range(300):
            m=random.getrandbits(15); s=tuple(sorted(w[i]+((m>>i)&1)*M for i in range(15)))
            st_n+=1; st_ok+= (open_direct(list(s),2*M)==(s in ks))
        for s in random.sample(kids,min(20,len(kids))): st_n+=1; st_ok+=open_direct(list(s),2*M)
    print(json.dumps({"SELFTEST_agree":st_ok,"of":st_n}),flush=True); result["selftest"]=[st_ok,st_n]

    for label,w,p,M0 in trees:
        maxM=(1<<12)*p if p==17 else 256*p
        levels,trunc=run_tree(label,w,M0,p,maxM,log)
        result["trees"][label]={"p":p,"M0":M0,"truncated":trunc,"levels":levels}
    for name,(p,vecs,tl) in chains.items():
        lv=result["trees"][tl]["levels"]; off=(result["trees"][tl]["M0"]//p).bit_length()-1; rows=[]
        for j,v in enumerate(vecs):
            s=tuple(sorted(v)); M=p<<j; jj=j-off
            hit=[r for r in lv[jj] if tuple(r["w"])==s] if 0<=jj<len(lv) else []
            row={"level_p":1<<j,"in_tree":bool(hit),"open_direct":open_direct(list(s),M)}; row.update(counts(list(s),M,p))
            if hit: row["open_children"]=hit[0]["open_children"]; row["height"]=hit[0]["height"]
            elif jj<0: row["open_children"]=len(open_children(list(s),M)[0]); row["height"]="root (not in subtree)"
            rows.append(row)
        result["chains"][name]=rows; print(json.dumps({"chain":name,"rows":rows}),flush=True)
    for src,p,w in scan:
        M=32*p; o=open_direct(list(w),M); rec={"src":src,"p":p,"w":sorted(w),"open":o,"improper":improper_direct(list(w),M)}
        rec.update(counts(w,M,p))
        if o:
            kids,_=open_children(sorted(w),M); rec["open_children"]=len(kids)
            gk=0
            for c in kids: gk+=len(open_children(c,2*M)[0])
            rec["open_grandchildren"]=gk
        result["scan"].append(rec)
    print(json.dumps({"scan_nodes":len(scan),"open":sum(r["open"] for r in result["scan"])}),flush=True)
    json.dump(result,open(out_json,"w"))
