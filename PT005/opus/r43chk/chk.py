from own import *
p=47; chainv=[[2,4,5,6,7,8,10,11,13,15,17,18,19,22,23],[49,51,5,6,7,55,57,11,13,62,17,18,19,69,23],[143,51,5,6,7,149,57,11,107,62,17,112,113,163,23],[143,51,193,194,195,149,245,199,295,62,205,112,113,351,23]]
M=p
for i,w in enumerate(chainv):
    lift = i==0 or all(any((a-b)%(M//2)==0 for b in chainv[i-1]) for a in w) and sorted(x%(M//2) for x in w)==sorted(chainv[i-1])
    print(M, "open",is_open(w,M), fstats(w,M,p), "legal" , lift)
    M*=2
# extend: open descendants of the 376 node
w=chainv[-1]; M=376
lvl=[w]
for step in range(2):
    nxt=[]
    for x in lvl: nxt+=open_children(x,M)
    nxt=sorted(set(map(tuple,nxt))); M*=2
    print("level",M,"open nodes",len(nxt), "F3 range", (min(fstats(list(n),M,p)['F3'] for n in nxt), max(fstats(list(n),M,p)['F3'] for n in nxt)) if nxt else None)
    lvl=[list(n) for n in nxt][:200]
    if not nxt: break
