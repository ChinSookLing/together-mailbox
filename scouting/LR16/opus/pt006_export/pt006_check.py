# Brute-force check of the PT006 export contract (plain Python, independent of the C search).
import json,sys,itertools
P=223;N=(P-1)//2
near=lambda v,t: 16*min(v*t%P,P-v*t%P)<P
bad=0
for l in open(sys.argv[1]):
    d=json.loads(l); C=d["chosen"]; U=[t for t in range(1,N+1) if not any(near(v,t) for v in C)]
    assert U==d["uncovered"], "uncovered mismatch"
    for v in d["candidates"]: assert v not in C and any(near(v,t) for t in U)
    ok=[A for k in range(3) for A in itertools.combinations(d["candidates"],k) if all(any(near(v,t) for v in A) for t in U)]
    claim_pruned = (len(ok)==0)
    if claim_pruned!=d["pruned"]: bad+=1
    if not d["pruned"]: assert all(any(near(v,t) for v in C+d["witness"]) for t in range(1,N+1))
    print(d["slots2_node_index"], "pruned" if d["pruned"] else "unpruned", "completions_found=%d"%len(ok), "AGREE" if claim_pruned==d["pruned"] else "DISAGREE")
print("disagreements", bad)
