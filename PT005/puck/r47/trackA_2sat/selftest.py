# Self-test: on 80 random k>=1 nodes, recompute the 2-SAT verdict by literal brute force over all 2^15 lifts
# (pure Python, direct definition) and compare with per_node_2sat.tsv.gz. Different algorithm from puck_2sat.py.
import gzip,csv,random,itertools
rows=list(csv.DictReader(gzip.open('../../../hesper/r45/widen/nodes_widen.csv.gz','rt')))
mine={}
for r in csv.DictReader(gzip.open('per_node_2sat.tsv.gz','rt'),delimiter='\t'): mine[int(r['row'])]=r['sat2']
random.seed(103)
cand=[i for i,r in enumerate(rows) if int(r['k'])>=1 and int(r['M'])<=700]
dead2=[i for i in cand if mine[i]=='sat2']; none=[i for i in cand if mine[i]=='none']
pick=random.sample(dead2,40)+random.sample(none,40)
def d(x,N): x%=N; return min(x,N-x)
bad=0
for i in pick:
    r=rows[i]; M=int(r['M']); N=2*M; w=list(map(int,r['coords'].split()))
    cls=[]
    for T in range(1,M+1,2):
        lit=[(j,b) for j in range(15) for b in (0,1) if 16*d(T*(w[j]+b*M),N)<N]
        if any((j,0) in lit and (j,1) in lit for j in range(15)): continue
        if len(lit)<=2: cls.append(lit)
    sat=False
    for m in range(1<<15):
        if all(any(((m>>j)&1)==b for j,b in c) for c in cls): sat=True; break
    v='none' if sat else ('empty' if any(len(c)==0 for c in cls) else 'sat2')
    if v!=mine[i]: bad+=1; print('MISMATCH',i,v,mine[i])
print('selftest nodes',len(pick),'mismatches',bad)
