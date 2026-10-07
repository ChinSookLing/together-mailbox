#!/usr/bin/env python3
"""Bounded feasibility scout, NOT a proof-producing solver or checker."""
import sys,time,json,re
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix,csc_matrix
from pathlib import Path
from check_model import constraints
path=Path(sys.argv[1]);limit=float(sys.argv[2])
n=int(re.search(r'#variable= (\d+)',path.read_text().splitlines()[0]).group(1))
cs=list(constraints(path));A=lil_matrix((len(cs),n));rhs=[]
for i,(terms,b) in enumerate(cs):
 for v,a in terms.items():A[i,v-1]=a
 rhs.append(b)
start=time.perf_counter()
r=milp(np.zeros(n),integrality=np.ones(n),bounds=Bounds(0,1),
       constraints=LinearConstraint(csc_matrix(A),rhs,np.full(len(cs),np.inf)),
       options={'time_limit':limit,'mip_rel_gap':0})
out={'input':path.name,'time_limit_seconds':limit,'elapsed_seconds':time.perf_counter()-start,
     'status':int(r.status),'message':r.message,'proof_file_produced':False,
     'evidence_status':'TEST_ONLY_NOT_A_CERTIFIED_UNSAT_RESULT'}
if r.x is not None:
 values={i+1:round(v) for i,v in enumerate(r.x)}
 assert all(sum(a*values[v] for v,a in terms.items())>=b for terms,b in cs)
 out['true_variables']=[v for v,x in values.items() if x]
print(json.dumps(out,indent=2))
