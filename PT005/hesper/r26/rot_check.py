p=17
def run(F5,a0,kmax=12):
    lev={F5}; a=a0
    for k in range(6,kmax+1):
        a=(2*a)%p; N=p*2**k; Np=N//2
        T=[t for t in range(1,N//2+1,2) if t%p in (a,p-a)]
        full=(1<<len(T))-1
        cache={}
        def m(w):
            if w not in cache:
                x=0
                for i,t in enumerate(T):
                    r=t*w%N
                    if 16*min(r,N-r)<N: x|=1<<i
                cache[w]=x
            return cache[w]
        nxt=set()
        for s in lev:
            opts=[(m(w),m(w+Np),w) for w in s]
            suf=[0]*9
            for i in range(7,-1,-1): suf[i]=suf[i+1]|opts[i][0]|opts[i][1]
            def dfs(i,acc,cur):
                if acc|suf[i]!=full: return
                if i==8: nxt.add(tuple(cur)); return
                a0_,b0,w=opts[i]
                dfs(i+1,acc|a0_,cur+[w]); dfs(i+1,acc|b0,cur+[w+Np])
            dfs(0,0,[])
        print(k,"±%d"%a,len(nxt),flush=True)
        lev=nxt
        if not lev: return k
F5=tuple(w%544 for w in (784,1040,1296,1552,1808,2064,2320,3824))
print("Astra frozen family dies at",run(F5,2))
