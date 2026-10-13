import sys,time
p=17
def mask(w,N):
    m=0
    for t in range(1,N//2+1):
        x=(t*w)%N
        if 16*min(x,N-x)<N: m|=1<<t
    return m
def children(s,k):  # s at level k-1 -> improper children at level k
    N=p*2**k; Np=N//2; full=(1<<(N//2+1))-2
    opts=[(mask(w,N),mask(w+Np,N),w) for w in s]
    # suffix possible unions
    suf=[0]*(len(s)+1)
    for i in range(len(s)-1,-1,-1): suf[i]=suf[i+1]|opts[i][0]|opts[i][1]
    out=[]
    def dfs(i,acc,cur):
        if acc|suf[i]!=full: return
        if i==len(s):
            out.append(tuple(cur)); return
        a,b,w=opts[i]
        cur.append(w); dfs(i+1,acc|a,cur); cur.pop()
        cur.append(w+Np); dfs(i+1,acc|b,cur); cur.pop()
    dfs(0,0,[])
    return out
W5=(240,496,208,464,176,432,144,128,384,96,352,64,320,32,16)
lev={W5}
t0=time.time()
for k in range(6,12):
    nxt=set()
    for s in lev: nxt.update(children(s,k))
    fz=sorted({sum(1 for w in s if w%2**k) for s in nxt})
    print(k,len(nxt),"frozen counts",fz, "%.0fs"%(time.time()-t0),flush=True)
    lev=nxt
    if not lev: break
