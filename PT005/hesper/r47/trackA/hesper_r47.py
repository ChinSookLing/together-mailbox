# Hesper R47 Track A (independent of Puck measure.py): loop over t, vectorise over nodes.
import gzip, numpy as np, collections, sys
src='/workspace/work/together-mailbox/PT005/hesper/r45/widen/nodes_widen.csv.gz'
by=collections.defaultdict(list)
with gzip.open(src,'rt') as f:
    h=next(f).strip().split(',')
    for ln,line in enumerate(f,2):
        a=line.strip().split(',')
        by[int(a[2])].append((ln,int(a[0]),list(map(int,a[3].split())),int(a[10]),int(a[11])))
C=collections.Counter(); rows=[]
for M in sorted(by):
    R=by[M]; n=len(R)
    if M%2:
        for r in R: rows.append((r[0],r[1],M,r[3],r[4],'NA','NA'))
        C['oddM']+=n; continue
    W=np.array([r[2] for r in R],np.int64); odd=(W&1)==1
    cert=np.zeros(n,bool); minE=np.full(n,99); evsing=np.zeros(n,bool)
    for t in range(1,M,2):
        if 2*t==M: continue
        x=(W*t)%M; near=8*np.minimum(x,M-x)<M
        s=near.sum(1); minE=np.minimum(minE,s)
        one=s==1
        oddhit=(near&odd).sum(1)==1
        cert|=one&oddhit; evsing|=one&~oddhit
    for k,r in enumerate(R):
        rows.append((r[0],r[1],M,r[3],r[4],int(cert[k]),int(minE[k]),int(evsing[k])))
with open('/workspace/work/r47/per_node_hesper_r47.tsv','w') as o:
    o.write('csv_line\tp\tM\tn_open_children\tsurvival_depth\tcert\tminE\thas_even_singleton\n')
    for r in rows: o.write('\t'.join(map(str,r))+'\n')
E=[r for r in rows if r[5]!='NA']
dead=[r for r in E if r[3]==0]; live=[r for r in E if r[3]>0]
print('nodes',len(rows),'oddM',C['oddM'])
print('dead(n_open=0)',len(dead),'live',len(live))
print('cert total',sum(r[5] for r in E),'cert&dead',sum(r[5] for r in dead),'cert&live',sum(r[5] for r in live))
print('cert vs survival_depth col: cert with surv>0',sum(1 for r in E if r[5] and r[4]>0))
u=[r for r in dead if not r[5]]
print('dead uncert',len(u),'minE dist',collections.Counter(r[6] for r in u))
print('dead uncert minE=1 all-even-singleton check',sum(1 for r in u if r[6]==1 and r[7]))
print('live minE dist',collections.Counter(r[6] for r in live))
print('E empty any',sum(1 for r in E if r[6]==0))
