exec(open('chain.py').read().split('for k in map')[0])
import itertools
def tiles(ws,k,b):
    N=17*2**k;T=cls(N,b);cs=[cov(w%N,N,T) for w in ws]
    return sum(map(len,cs))==len(T) and len(frozenset().union(*cs))==len(T)
def lifts(ws,k,b):
    N=17*2**k
    return [e for e in itertools.product((0,1),repeat=8) if tiles([w+ei*N for w,ei in zip(ws,e)],k+1,2*b%17)]
def proj2(ws,k,b):
    N=17*2**k;N2=2*N;T=cls(N2,2*b%17);from collections import Counter
    c=Counter()
    for w in ws:
        for t in T:
            if 16*min(t*w%N2,N2-t*w%N2)<N2: c[(t if t%17==(2*b)%17 else -t)%(2**k)]+=1
    return set(c.values()), len(c)
gpt=[3+136*j for j in range(8)]; ast=[3,125,419,541,269,275,397,147]
for name,ws in (('GPT',gpt),('Astra',ast)):
    print(name,'legal',all(legal(w) for w in ws),'mod17',[w%17 for w in ws])
    for b in range(1,9):
        if tiles(ws,6,b): print('  tiles C6(%d)'%b,'proj2 counts',proj2(ws,6,b),'#lifts',len(lifts(ws,6,b)))
