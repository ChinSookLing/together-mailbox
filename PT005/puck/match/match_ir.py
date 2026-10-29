#!/usr/bin/env python3
# Puck job-by-job match of two kcascade ir.jsonl files. Key = (r, s).
# Compares every field except "secs" (wall time, machine-dependent). Usage: match_ir.py A B [ENGINE PRIME]
import json, sys, hashlib, subprocess
def load(p):
    D = {}; n = 0; dup = 0
    for l in open(p):
        l = l.strip()
        if not l: continue
        n += 1; d = json.loads(l); k = (d["r"], d["s"])
        if k in D: dup += 1
        D[k] = d
    return D, n, dup
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
A, B = sys.argv[1], sys.argv[2]
a, na, da = load(A); b, nb, db = load(B)
print(f"A {A}\n  sha256 {sha(A)} lines {na} keys {len(a)} dup {da}")
print(f"B {B}\n  sha256 {sha(B)} lines {nb} keys {len(b)} dup {db}")
fa = set().union(*[set(d) for d in a.values()]); fb = set().union(*[set(d) for d in b.values()])
fields = sorted((fa | fb) - {"r", "s", "secs"})
print("fields compared:", fields, "| field sets equal:", fa == fb)
onlyA = sorted(set(a) - set(b)); onlyB = sorted(set(b) - set(a)); both = sorted(set(a) & set(b))
diff = [k for k in both if any(a[k].get(f) != b[k].get(f) for f in fields)]
print(f"compared {len(both)} identical {len(both)-len(diff)} differing {len(diff)} onlyA {len(onlyA)} onlyB {len(onlyB)}")
for k in diff[:20]: print("  DIFF", k, {f: (a[k].get(f), b[k].get(f)) for f in fields if a[k].get(f) != b[k].get(f)})
for nm, X in (("A", a), ("B", b)):
    print(f"totals {nm}: rows {sum(x['rows'] for x in X.values())} casc_rows {sum(x['casc_rows'] for x in X.values())} "
          f"survivors_l2 {sum(x['casc_survivors'] for x in X.values())} alive_l16 {sum(len(x['deep']) for x in X.values())} "
          f"nodes {sum(x['nodes'] for x in X.values())}")
if len(sys.argv) > 4:
    E, P = sys.argv[3], sys.argv[4]
    run = lambda c: subprocess.run(c, capture_output=True, text=True, check=True).stdout
    roots = [int(l.split()[0]) for l in run([E, P, "irroots"]).splitlines()[1:]]
    jobs = {(r, int(l.split()[0])) for r in roots for l in run([E, P, "irsubroots", str(r)]).splitlines()[1:]}
    print(f"engine job list p={P}: roots {len(roots)} jobs {len(jobs)} | equals A keys {jobs == set(a)} | equals B keys {jobs == set(b)}")
ok = not diff and not onlyA and not onlyB and da == 0 and db == 0
print("MATCH" if ok else "NO MATCH")
