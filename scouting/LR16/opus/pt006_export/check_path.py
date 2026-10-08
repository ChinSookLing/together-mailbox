# Replays each node's branch path with the search rule and checks chosen, excluded and the cell order.
import json,sys
P=223;N=(P-1)//2
near=lambda v,t: 16*min(v*t%P,P-v*t%P)<P
cl={t:[v for v in range(1,N+1) if near(v,t)] for t in range(1,N+1)}
bad=0
for l in open(sys.argv[1]):
    d=json.loads(l); C=[]; X=set()
    for st in d["path"]:
        cov=lambda t: any(near(v,t) for v in C)
        t=min(t for t in range(1,N+1) if not cov(t))
        ok = (t==st["cell"] and cl[t][st["index_in_cell_list"]]==st["speed"])
        X |= set(cl[t][:st["index_in_cell_list"]]); C.append(st["speed"])
        if not ok: bad+=1; break
    good = ok and sorted(C)==d["chosen"] and sorted(X-set(C))==d["excluded"]
    bad += (not good); print(d["slots2_node_index"], "PATH_OK" if good else "PATH_MISMATCH")
print("mismatches",bad)
