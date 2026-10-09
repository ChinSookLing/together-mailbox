# Offline constructed test nodes for PT006 (p=223, slots=2): ORPHAN and EXHAUST cases. NOT from the DFS.
# Construction is deterministic (fixed seed). Each node is judged by brute force with the same contract as the export.
import json, itertools, random
P=223; N=(P-1)//2; H=(P-1)//16
near=lambda v,t: 16*min(v*t%P,P-v*t%P)<P
cov={v:{t for t in range(1,N+1) if near(v,t)} for v in range(1,N+1)}
cl={t:[v for v in range(1,N+1) if t in cov[v]] for t in range(1,N+1)}
def judge(C,X,s=2):
    U={t for t in range(1,N+1) if not any(t in cov[v] for v in C)}
    cand=[v for v in range(1,N+1) if v not in C and v not in X and cov[v]&U]
    comps=[list(A) for k in range(s+1) for A in itertools.combinations(cand,k) if U<=set().union(*[cov[v] for v in A])]
    orphan=sorted(t for t in U if not any(t in cov[v] for v in cand))
    mx=max((len(cov[v]&U) for v in cand),default=0)
    if comps: reason="NOT_PRUNED"
    elif orphan: reason="ORPHAN: cell %d has no candidate"%orphan[0]
    elif len(U)>s*mx: reason="COUNT: |U|=%d > slots*max_new=%d"%(len(U),s*mx)
    else: reason="EXHAUST: all 1 + n + n(n-1)/2 candidate sets checked"
    return dict(chosen=sorted(C),excluded=sorted(X),slots=s,uncovered=sorted(U),candidates=cand,pruned=not comps,reason=reason,
                completions=len(comps),orphan_cells=orphan,max_new=mx)
import sys, hashlib
CORES = sys.argv[1] if len(sys.argv) > 1 else "../core223/cores.jsonl"   # public copy in the mailbox
assert hashlib.sha256(open(CORES,"rb").read()).hexdigest() == "36bbe2ee84b1d1a51e6bb0570976731cd7e16d3ed87283bcd263996f0116abb6", "unexpected cores file"
cores=[json.loads(l)["core"] for l in open(CORES)]
rnd=random.Random(20261008); out=[]
# EXHAUST: core minus two speeds a,b; exclude a,b; keep if no completion and no orphan and COUNT does not fire
for C13 in cores:
    for a,b in itertools.combinations(C13,2):
        C=set(C13)-{a,b}; r=judge(C,{a,b})
        if r["reason"].startswith("EXHAUST"):
            r["construction"]="13-class core %s minus {%d,%d}; both excluded"%(C13,a,b); out.append(r); break
    if sum(o["reason"].startswith("EXHAUST") for o in out)>=4: break
# ORPHAN: core minus two speeds; pick the smallest uncovered cell t; exclude every too-near speed of t that is not chosen
k=0
for C13 in cores[5:]:
    a,b=C13[-2],C13[-1]; C=set(C13)-{a,b}
    U=sorted(t for t in range(1,N+1) if not any(t in cov[v] for v in C)); t=U[0]
    X={v for v in cl[t] if v not in C}; r=judge(C,X)
    if r["reason"].startswith("ORPHAN"):
        r["construction"]="13-class core %s minus {%d,%d}; excluded = all speeds too near at cell %d"%(C13,a,b,t); out.append(r); k+=1
    if k>=4: break
with open(sys.argv[2] if len(sys.argv) > 2 else "pt006_constructed_cases_rebuilt.jsonl","w") as f:
    for r in out: f.write(json.dumps(r)+"\n")
for r in out: print(r["reason"][:10],len(r["uncovered"]),len(r["candidates"]),r["max_new"],r["completions"],r["construction"][-40:])
