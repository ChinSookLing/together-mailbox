# PT005 R24c: exhaustive census of improper legal lifts at p=17 from the root (residues 2..16, N=p).
# improper at level k: every T in 1..N/2 has some i with 16*||T*w_i||_N < N, N=2^k p.
# child: w_i -> w_i + b_i*N (b_i in {0,1}), new level k+1. Die-out is permanent (GLM), so BFS keeps only improper nodes.
import sys, time, json
p=17; R=list(range(2,17)); n=len(R)
def covmask(w,N):
    m=0
    for T in range(1,N//2+1):
        r=(T*w)%N; r=min(r,N-r)
        if 16*r<N: m|=1<<(T-1)
    return m
def v2(x): return (x&-x).bit_length()-1
def children(w,k):
    N=2**(k+1)*p; full=(1<<(N//2))-1
    opts=[]
    for x in w:
        a,b=x,x+N//2
        opts.append(((a,covmask(a,N)),(b,covmask(b,N))))
    # suffix unions for pruning
    suf=[0]*(n+1)
    for i in range(n-1,-1,-1): suf[i]=suf[i+1]|opts[i][0][1]|opts[i][1][1]
    out=[]
    def rec(i,acc,cur):
        if (acc|suf[i])!=full: return
        if i==n: out.append(tuple(cur)); return
        for val,m in opts[i]:
            cur.append(val); rec(i+1,acc|m,cur); cur.pop()
    rec(0,0,[]); return out
K=int(sys.argv[1]) if len(sys.argv)>1 else 9
level=[tuple(R)]; N0=p
print("k=0 improper root:", covmask_all:= all(any(16*min(T*x%N0,N0-T*x%N0)<N0 for x in R) for T in range(1,N0//2+1)),flush=True)
for k in range(0,K):
    t=time.time(); nxt=set()
    for w in level: nxt.update(children(w,k))
    level=sorted(nxt); kk=k+1; N=2**kk*p
    fr=[sum(1 for x in w if v2(x)<kk) for w in level]
    hist={f:fr.count(f) for f in sorted(set(fr))}
    print(f"k={kk} N={N} improper={len(level)} frozen_hist={hist} t={time.time()-t:.1f}s",flush=True)
    json.dump({"k":kk,"nodes":level},open(f"level{kk}.json","w"))
    if not level: print("ALL DIE at k=",kk); break
