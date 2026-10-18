# Per-node compare of Puck per_node_puck_r47c.tsv.gz vs Hesper PT005/hesper/r47c/per_node_r47c.tsv.gz (same row order: k>=1 rows of nodes_widen.csv.gz).
import gzip,csv
H=list(csv.DictReader(gzip.open('../../hesper/r47c/per_node_r47c.tsv.gz','rt'),delimiter='\t'))
P=list(csv.DictReader(gzip.open('per_node_puck_r47c.tsv.gz','rt'),delimiter='\t'))
b=lambda x: x not in ('0','')
d=dict(pM=0,dead=0,xor=0,sat2=0,oddonly=0,len2=0); n=0
for h,p in zip(H,P):
    d['pM']+=(h['p'],h['M'])!=(p['p'],p['M']); d['dead']+=b(h['dead'])!=b(p['dead']); d['xor']+=b(h['xor'])!=b(p['xor']); d['sat2']+=b(h['sat2'])!=b(p['sat2'])
    if b(h['sat2']) and not b(h['xor']):
        n+=1; d['oddonly']+=b(h['oddonly_unsat'])!=b(p['oddonly_unsat']); d['len2']+=(h['cyc_len']=='2')!=b(p['len2'])
print('rows',len(H),len(P),'target',n,'disagreements',d)
