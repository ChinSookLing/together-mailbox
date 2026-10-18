import gzip,csv,collections
rows=list(csv.DictReader(gzip.open('/workspace/mbx_pt5/PT005/hesper/r45/widen/nodes_widen.csv.gz','rt')))
L=[l.rstrip('\n').split('\t') for l in open('mislabel_list.tsv')][1:]
ok=0; byp=collections.Counter(); bysrc=collections.Counter(); byk=collections.Counter()
for f in L:
    i=int(f[0]); r=rows[i]; M=int(r['M']); N=2*M; m=int(f[6]); W=list(map(int,r['coords'].split()))
    child=[w+((m>>j)&1)*M for j,w in enumerate(W)]
    if all(any(16*min((T*w)%N,N-(T*w)%N)<N for w in child) for T in range(1,N)): ok+=1
    byp[r['p']]+=1; bysrc[r['source'].split('_')[0]]+=1; byk[r['k']]+=1
print('listed',len(L),'example child fully covers all T in 1..N-1:',ok)
print('by p',sorted(byp.items(),key=lambda x:int(x[0])))
print('by k',sorted(byk.items()))
print('by source prefix',bysrc.most_common(10))
