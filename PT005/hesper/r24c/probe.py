import random,time,sys
sys.argv=['x','0']
exec(open('enum17.py').read().split("K=int")[0])
from itertools import product
# rebuild k=1 nodes
lvl=children(tuple(R),0)
cand=[w for w in lvl if sum(1 for x in w if v2(x)<1)>=8]
print(len(lvl),len(cand))
random.seed(1);S=random.sample(cand,30)
t=time.time()
for depth in range(1,6):
    nxt=set()
    for w in S: nxt.update(children(w,depth))
    print("from sample: k=",depth+1,"nodes",len(nxt),"t",round(time.time()-t,1),flush=True)
    S=list(nxt)
    if len(S)>3000: S=random.sample(S,3000)
    if not S: break
