import gzip,csv,numpy as np,collections,sys,json
rows=list(csv.DictReader(gzip.open(sys.argv[1],'rt')))
groups=collections.defaultdict(list)
for i,r in enumerate(rows): groups[(int(r['p']),int(r['M']))].append(i)
minE=np.zeros(len(rows),int); cert=np.zeros(len(rows),bool); empty=np.zeros(len(rows),bool)
for (p,M),idx in groups.items():
    T=np.arange(1,M//2+1,2,dtype=np.int64); T=T[2*T!=M]
    for c0 in range(0,len(idx),4000):
        ii=idx[c0:c0+4000]
        W=np.array([list(map(int,rows[i]['coords'].split())) for i in ii],dtype=np.int64)
        R=(T[None,:,None]*W[:,None,:])%M; D=np.minimum(R,M-R)
        near=(8*D<M)                                  # n x m x 15
        cnt=near.sum(axis=2)
        minE[ii]=cnt.min(axis=1)
        empty[ii]=(cnt==0).any(axis=1)
        single=(cnt==1)
        oddw=(W%2==1)[:,None,:]
        cert[ii]=(single & (near&oddw).any(axis=2)).any(axis=1)
surv=np.array([int(r['survival_depth']) for r in rows]); nch=np.array([int(r['n_open_children']) for r in rows])
pp=np.array([int(r['p']) for r in rows])
dead=(nch==0)
tab=collections.Counter()
for c,e,d,p in zip(cert,empty,dead,pp): tab[(bool(c or e),bool(d),'p17' if p==17 else 'p>=19')]+=1
print("nodes",len(rows))
for k in sorted(tab): print(" certificate(single-odd or empty)=%s dead=%s %s: %d"%(k[0],k[1],k[2],tab[k]))
print("certificate but has open child (would contradict lemma):",int(((cert|empty)&~dead).sum()))
print("dead nodes without certificate:",int((dead&~(cert|empty)).sum()),"of",int(dead.sum()))
print("minE histogram dead:",dict(sorted(collections.Counter(minE[dead]).items())))
print("minE histogram alive:",dict(sorted(collections.Counter(minE[~dead]).items())))
np.save("flags.npy",np.stack([cert,empty,minE]))
