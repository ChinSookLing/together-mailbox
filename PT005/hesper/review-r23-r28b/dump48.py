exec(open('glm_dump2.py').read().split('k=5\nfor b')[0])
import itertools, json
from collections import Counter, deque
k=5;N=544
QR={1,2,4,8,9,13,15,16}
out=[]
for b in range(1,9):
    T=cls(N,b);T2=cls(2*N,2*b%17);n2=len(T2)
    sig={}
    for w in range(1,N,2):
        if not legal(w): continue
        c=cov(w,N,T);a=cov(w,2*N,T2);bb=cov(w+N,2*N,T2)
        if a&bb: continue
        sig.setdefault((c,frozenset([a,bb])),[]).append(w)
    items=list(sig.items());full=frozenset(range(len(T)))
    tilings=[]
    def dfs(used,mult,acc):
        if len(acc)==8:
            if used==full and len(mult)==n2 and all(v==2 for v in mult.values()): tilings.append(acc)
            return
        i=min(full-used)
        for key,ws in items:
            c,pr=key
            if i in c and not(c&used):
                m=mult.copy();o=True
                for x in frozenset().union(*pr):
                    m[x]+=1;o=o and m[x]<=2
                if o: dfs(used|c,m,acc+[(key,ws)])
    dfs(frozenset(),Counter(),[])
    cnt=Counter()
    for til in tilings:
        inc={}
        for i,(key,ws) in enumerate(til):
            w0=ws[0]
            for e,s in ((0,cov(w0,2*N,T2)),(1,cov(w0+N,2*N,T2))):
                for x in s: inc.setdefault(x,[]).append((i,e))
        adj={i:[] for i in range(8)}
        for x,l in inc.items():
            (u,eu),(v,ev)=l; lab=1^eu^ev
            adj[u].append((v,lab,T2[x])); adj[v].append((u,lab,T2[x]))
        best=None
        for s in range(8):
            prev={(s,0):None};dq=deque([(s,0)])
            while dq:
                u,par=dq.popleft()
                for v,lab,t in adj[u]:
                    st=(v,par^lab)
                    if st not in prev: prev[st]=((u,par),t,lab);dq.append(st)
            if (s,1) in prev:
                path=[];cur=(s,1)
                while prev[cur]:
                    pu,t,lab=prev[cur];path.append((pu[0],t,cur[0],lab));cur=pu
                path=path[::-1]
                if best is None or len(path)<len(best): best=path
        solv = best is None
        rep=[ws[0] for _,ws in til]
        uniform=all(len({w%17 in QR for w in ws})==1 for _,ws in til)
        q=sum(w%17 in QR for w in rep)
        cnt[(solv,q%2)]+=1
        if not solv and q%2==1:
            out.append({"b":b,"reps":rep,"classes":[ws for _,ws in til],"qr_uniform":uniform,"qr":q,
                        "w_mod8":[w%8 for w in rep],"w_mod16":[w%16 for w in rep],"w_mod64":[w%64 for w in rep],
                        "odd_cycle_len":len(best),
                        "odd_cycle":[[rep[u],t,rep[v],lab] for u,t,v,lab in best]})
    print(b,len(tilings),dict(cnt),flush=True)
json.dump(out,open('dead48.json','w'),indent=1)
print(len(out),Counter(d['odd_cycle_len'] for d in out),Counter(d['b'] for d in out))
