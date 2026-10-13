import sys,time
p=17
def cls(N,b): return [t for t in range(1,N//2+1,2) if t%p in(b%p,(-b)%p)]
def cov(w,N,T): return frozenset(i for i,t in enumerate(T) if 16*min(t*w%N,N-t*w%N)<N)
legal=lambda w: w%2==1 and w%17 not in (0,1,16)
def run(k,b,levels=3):
    Ns=[17*2**(k+j) for j in range(levels)]; bs=[b*2**j%17 for j in range(levels)]
    Ts=[cls(Ns[j],bs[j]) for j in range(levels)]
    top=levels-1; Nt=Ns[top]
    sig={}
    for w in range(1,Nt,2):
        if not legal(w): continue
        cs=tuple(cov(w%Ns[j],Ns[j],Ts[j]) for j in range(levels))
        sig.setdefault(cs,[]).append(w)
    coords=[(ws[0],cs) for cs,ws in sig.items()]
    full=[frozenset(range(len(Ts[j]))) for j in range(levels)]
    found=[];nodes=[0]
    def dfs(used,acc,start_min):
        nodes[0]+=1
        if len(acc)==8:
            if all(used[j]==full[j] for j in range(levels)): found.append([w for w,_ in acc])
            return
        rem=full[top]-used[top]; i=min(rem)
        for w,cs in coords:
            if i in cs[top] and all(not(cs[j]&used[j]) for j in range(levels)):
                dfs([used[j]|cs[j] for j in range(levels)],acc+[(w,cs)],0)
    dfs([frozenset()]*levels,[],0)
    return len(coords),nodes[0],found
for k in map(int,sys.argv[1].split(',')):
  for b in range(1,9):
    t=time.time(); nc,nn,f=run(k,b,int(sys.argv[2]))
    print(f"k={k} b={b} levels={sys.argv[2]} coords={nc} nodes={nn} chains={len(f)} ex={f[:1]} {time.time()-t:.1f}s",flush=True)
