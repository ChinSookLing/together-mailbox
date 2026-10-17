# Puck: analysis of puck_f3_nodes.json (output of puck_f3_check.py). Prints per-tree tables, thresholds, corollary, witnesses.
import json, collections, sys
sys.path.insert(0,'.')
from puck_f3_check import open_direct, counts, open_children
import gzip
fn=sys.argv[1] if len(sys.argv)>1 else "puck_f3_nodes.json.gz"
R=json.load(gzip.open(fn,"rt") if fn.endswith(".gz") else open(fn))
KEYS=["E","F3","F4","F5"]
allrecs=[]
print("== Per-tree summary")
for label,t in R["trees"].items():
    p=t["p"]; recs=[r|{"tree":label,"level_p":r["M"]//p} for L in t["levels"] for r in L]; allrecs+=recs
    n=len(recs); f9=[r for r in recs if r["F3"]>=9]; f9k=[r for r in f9 if r["open_children"]>0]
    print(json.dumps({"tree":label,"p":p,"truncated":t["truncated"],"open_nodes_scanned":n,
        "levels":{str(L[0]["M"]//p):len(L) for L in t["levels"]},
        "open_F3>=9":len(f9),"open_F3>=9_with_open_child":len(f9k),
        "max_open_children_among_F3>=9":max([r["open_children"] for r in f9],default=None),
        "F3>=9_by_level":dict(collections.Counter(str(r["level_p"]) for r in f9)),
        "F3>=9_hist_of_open_children":dict(sorted(collections.Counter(r["open_children"] for r in f9).items()))}))
print("== Scan nodes (32p)")
S=R["scan"]; So=[r for r in S if r["open"]]
print(json.dumps({"scan_nodes":len(S),"improper":sum(r["improper"] for r in S),"open":len(So),
  "open_F3>=9":sum(r["F3"]>=9 for r in So),"open_with_open_child":sum(r["open_children"]>0 for r in So),
  "F3_hist_open":dict(sorted(collections.Counter(r["F3"] for r in So).items())),
  "E_hist_open":dict(sorted(collections.Counter(r["E"] for r in So).items())),
  "open_grandchildren_total":sum(r["open_grandchildren"] for r in So)}))
for r in So: allrecs.append({"tree":r["src"]+f" p{r['p']}","level_p":32,"w":r["w"],"open_children":r["open_children"],
                             "height":(0 if r["open_children"]==0 else (1 if r["open_grandchildren"]==0 else None)),**{k:r[k] for k in KEYS}})
print("== Thresholds: smallest t with [open node, X>=t => 0 open children] on ALL data (= 1 + max X over nodes WITH an open child)")
for k in KEYS:
    withkid=[r for r in allrecs if r["open_children"]>0]
    mx=max(r[k] for r in withkid); t=mx+1
    print(json.dumps({"measure":k,"max_over_nodes_with_open_child":mx,"threshold":t,
       "nodes_with_open_child_by_value":dict(sorted(collections.Counter(r[k] for r in withkid).items())),
       "open_nodes_with_X>=threshold":sum(r[k]>=t for r in allrecs),
       "max_X_any_open_node":max(r[k] for r in allrecs)}))
    for t2 in (8,9,10):
        bad=[r for r in allrecs if r[k]>=t2 and r["open_children"]>0]
        print(f"   {k}>={t2}: open nodes {sum(r[k]>=t2 for r in allrecs)}, with open child {len(bad)}, by tree {dict(collections.Counter(r['tree'] for r in bad))}")
print("== Threshold per tree (F3)")
for label in list(R["trees"])+["scan"]:
    rs=[r for r in allrecs if r["tree"]==label] if label!="scan" else [r for r in allrecs if "scan" in r["tree"]]
    wk=[r["F3"] for r in rs if r["open_children"]>0]
    print(f"   {label}: max F3 with open child = {max(wk) if wk else None}; max F3 overall = {max(r['F3'] for r in rs)}")
print("== Corollary: open node with E>=9 at M has no open descendant at 8M  (height = #further doublings with an open descendant)")
eh=collections.Counter(); viol=[]
for r in allrecs:
    if r["E"]>=9 and r.get("height") is not None:
        eh[(r["tree"] if "scan" not in r["tree"] else "scan",r["height"])]+=1
        if r["height"]>=3: viol.append(r)
for k,v in sorted(eh.items()): print("  ",k,v)
print("  violations (E>=9, height>=3):",len(viol), dict(collections.Counter((r["tree"],r["level_p"],r["E"]) for r in viol)))
print("== Witnesses: re-verified with the LITERAL definitions (slow path)")
def witness(tree):
    t=R["trees"][tree]; p=t["p"]; lv=t["levels"]
    for j,L in enumerate(lv):
        for r in L:
            if r["F3"]>=9 and r["open_children"]>0:
                kid=lv[j+1][r["kid_ids"][0]]
                M=r["M"]; w=r["w"]; c=kid["w"]
                lift=sorted(x%M for x in c)==sorted(w)
                return {"tree":tree,"p":p,"M":M,"level_p":M//p,"w":w,**counts(w,M,p),"open_literal":open_direct(w,M),
                        "n_open_children":r["open_children"],"child":c,"child_level_p":2*M//p,"child_is_lift":lift,
                        "child_open_literal":open_direct(c,2*M),"child_counts":counts(c,2*M,p)}
for tree in R["trees"]:
    w=witness(tree)
    if w: print(json.dumps(w))
def cor_witness(tree):
    t=R["trees"][tree]; p=t["p"]; lv=t["levels"]
    for j,L in enumerate(lv):
        for r in L:
            if r["E"]>=9 and r.get("height") is not None and r["height"]>=3:
                path=[r]; cur=r
                for d in range(3):
                    nxt=[lv[j+1+d][i] for i in cur["kid_ids"]]; cur=max(nxt,key=lambda x:x["height"]); path.append(cur)
                return {"tree":tree,"p":p,"path":[{"level_p":x["M"]//p,"w":x["w"],**counts(x["w"],x["M"],p),"open_literal":open_direct(x["w"],x["M"]),
                        "lift_of_prev":(i==0 or sorted(v%path[i-1]["M"] for v in x["w"])==sorted(path[i-1]["w"]))} for i,x in enumerate(path)]}
for tree in R["trees"]:
    w=cor_witness(tree)
    if w: print(json.dumps(w))
