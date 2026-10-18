# Puck job-by-job compare: K11 p431a (checkpoint 39106052178) vs office p431.
import json
def load(f):
    d={}
    for l in open(f):
        l=l.strip()
        if not l: continue
        j=json.loads(l); k=(j['r'],j['s'])
        assert k not in d, ('dup',f,k); d[k]=j
    return d
A=load('PT005/hesper/k11/p431a-results/ir.jsonl'); O=load('PT005/hesper/officepc-p431/collect/p431/ir.jsonl')
print('K11',len(A),'office',len(O),'same (r,s) set',set(A)==set(O))
fields=['rows','nodes','casc_rows','casc_survivors','deep','n_survivor_lines']
print('mismatches per field',{f:sum(A[k].get(f)!=O[k].get(f) for k in A) for f in fields})
for n,D in (('K11',A),('office',O)):
    print(n,'rows',sum(j['rows'] for j in D.values()),'casc_rows',sum(j['casc_rows'] for j in D.values()),'survivors',sum(j['casc_survivors'] for j in D.values()),
          'survivor (r,s)',sorted(k for k,j in D.items() if j['casc_survivors']),'nodes',sum(j['nodes'] for j in D.values()),'cpu_h %.2f'%(sum(j['secs'] for j in D.values())/3600))
