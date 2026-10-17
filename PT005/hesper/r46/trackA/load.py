import gzip, numpy as np, collections, pickle
src='/workspace/work/together-mailbox/PT005/hesper/r45/widen/nodes_widen.csv.gz'
G=collections.defaultdict(list); O=collections.defaultdict(list)
with gzip.open(src,'rt') as f:
    next(f)
    for line in f:
        a=line.rstrip('\n').split(',')
        p,k,M=int(a[0]),int(a[1]),int(a[2]); w=list(map(int,a[3].split()))
        G[(p,M)].append(w); O[(p,M)].append(int(a[10]))
# table-1 nodes not in widen
t1=set()
for line in open('/workspace/work/together-mailbox/PT005/hesper/r45/hesper_nodes.csv').readlines()[1:]:
    a=line.split(','); t1.add((int(a[0]),int(a[2]),tuple(map(int,a[3].split()))))
wid=set((p,M,tuple(w)) for (p,M),L in G.items() for w in L)
extra=t1-wid
print('widen',len(wid),'table1',len(t1),'table1 not in widen',len(extra))
D={k:(np.array(v,np.int64),np.array(O[k],np.int64)) for k,v in G.items()}
pickle.dump(D,open('nodes.pkl','wb'))
pickle.dump(sorted(extra),open('extra_t1.pkl','wb'))
for k in sorted(D): print(k,len(D[k][0]))
