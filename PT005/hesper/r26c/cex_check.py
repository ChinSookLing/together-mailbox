p=17
def cov(w,N,T):
    x=0
    for i,t in enumerate(T):
        r=t*w%N
        if 16*min(r,N-r)<N: x|=1<<i
    return x
def cls(N,b): return [t for t in range(1,N//2+1,2) if t%p in(b%p,(-b)%p)]
def tiles(u,k,b):
    N=p*2**k;T=cls(N,b);m=[cov(w,N,T) for w in u]
    tot=sum(bin(x).count('1') for x in m);un=0
    for x in m: un|=x
    return tot==len(T) and un==(1<<len(T))-1
def run(u,k0,b,kmax=11):
    assert tiles(u,k0,b), "base fail"
    lev={tuple(u)};out=[]
    for k in range(k0+1,kmax+1):
        b=2*b%p;N=p*2**k;h=N//2;T=cls(N,b);full=(1<<len(T))-1
        nxt=set()
        for s in lev:
            opts=[(cov(w,N,T),cov(w+h,N,T),w) for w in s]
            suf=[0]*(len(s)+1)
            for i in range(len(s)-1,-1,-1): suf[i]=suf[i+1]|opts[i][0]|opts[i][1]
            def dfs(i,acc,cur):
                if acc|suf[i]!=full: return
                if i==len(s): nxt.add(tuple(cur));return
                a,c,w=opts[i];dfs(i+1,acc|a,cur+[w]);dfs(i+1,acc|c,cur+[w+h])
            dfs(0,0,[])
        out.append((k,'±%d'%b,len(nxt)));lev=nxt
        if not lev: break
    return out
fams={'GPT':((9,29,49,67,73,93,105,125),4,1),
 'Astra':((53,207,39,59,27,11,63,81),4,7),
 'Grok':((15,5,3,63,7,13,11,1),4,2)}
for n,(u,k,b) in fams.items():
    print(n,[x%17 for x in u],run(u,k,b),flush=True)
