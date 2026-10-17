import pickle,glob,collections,json,os
SUF=os.environ.get('R46SUF','')
NODES=pickle.load(open(os.environ.get('R46NODES','nodes.pkl'),'rb'))
S1={}
for f in glob.glob('s1'+SUF+'/*.pkl'):
    d=pickle.load(open(f,'rb')); S1[d['key']]=d
R={}
for f in glob.glob('/tmp/r46w/s2'+SUF+'/*.pkl'):
    a=f.split('/')[-1][:-4].split('_'); key=(int(a[0]),int(a[1])); s=int(a[2])
    for j,r in enumerate(pickle.load(open(f,'rb'))): R[(key,s+j)]=r
keys=['nodes','children','lt1','lt1_open','lt1_covered','ge1','ge1_open','ovdeath','ovd_uncov','ovd_par','ovd_L7',
      'nodes_ge1','nodes_ge1_noopen','nodes_open','opendistinct_mismatch','tbl_mism_triples','tbl_triples']
byp=collections.defaultdict(collections.Counter); ex=[]
missing=0
for key,d in S1.items():
    p,M=key; W,O=NODES[key]
    byp[p]['tbl_mism_triples']+=d['mism']; byp[p]['tbl_triples']+=d['checked_triples']
    for i,(Dz,good,mn,mx) in enumerate(d['res']):
        r=R.get((key,i))
        if r is None: missing+=1; continue
        c=byp[p]; c['nodes']+=1; c['children']+=32768
        ge=r['cand']; assert ge==len(good)*2**(15-len(Dz))
        c['ge1']+=ge; c['lt1']+=32768-ge
        c['lt1_covered']+=r['viol']
        c['ge1_open']+=r['open']
        # open children all lie in covered&G by construction of r; opens among lt1 can only come from viol
        c['lt1_open']+=0 if r['viol']==0 else -10**12
        c['ovdeath']+=ge-r['open']; c['ovd_uncov']+=r['ovcov']; c['ovd_par']+=r['covdie_par']; c['ovd_L7']+=r['covdie_L7']
        c['nodes_ge1']+=ge>0; c['nodes_ge1_noopen']+=(ge>0 and r['open']==0); c['nodes_open']+=r['open']>0
        c['opendistinct_mismatch']+=r['open_distinct']!=r['nopen_csv']
        if ge>0: ex.append((p,M,[int(z) for z in W[i]],len(Dz),ge,r['covered'],r['open'],r['open_distinct'],r['nopen_csv'],mn,mx))
tot=collections.Counter()
for p in byp: tot.update(byp[p])
print('missing',missing)
print('TOTAL',dict(tot))
for p in sorted(byp): print(p,dict(byp[p]))
pickle.dump((dict(byp),dict(tot),ex),open('/tmp/r46w/agg'+SUF+'.pkl','wb'))
