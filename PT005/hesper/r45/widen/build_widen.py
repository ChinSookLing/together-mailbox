# Build nodes_widen.csv, nodelist_widen.txt, summary_widen.txt, exceptions_widen.tsv, roots_widen.txt (processed roots)
# from state_widen.pkl. Columns and tables as hesper_r45.py build_outputs().
import sys, os, json, pickle, hashlib, collections
from fractions import Fraction
sys.path.insert(0, '/workspace/work/r45')
from hesper_r45 import fvec, open_children
H = '/workspace/work/r45/widen'
st = pickle.load(open(H + '/state_widen.pkl', 'rb'))
ch = st['children']
W5KEY = (17, 544, tuple(sorted([189, 224, 72, 447, 176, 500, 144, 128, 384, 266, 80, 64, 48, 32, 16])))
proc = [r for r in st['roots'] if r[0] in st['status']]
unproc = [r for r in st['roots'] if r[0] not in st['status']]
labels = {}
for lab, p, M, w in proc:
    if st['status'][lab] != 'done': continue
    stack = [(p, M, tuple(sorted(w)))]
    while stack:
        k = stack.pop()
        s = labels.setdefault(k, set())
        if lab in s: continue
        s.add(lab)
        if k not in ch: ch[k] = [(k[0], 2 * k[1], c) for c in open_children(list(k[2]), k[1])]
        stack.extend(ch[k])
surv = {}
for k in sorted(labels, key=lambda k: -(k[1] // k[0])):
    kids = ch[k]; surv[k] = 0 if not kids else 1 + max(surv[c] for c in kids)
rows = []
for k in labels:
    p, M, w = k; kk = (M // p).bit_length() - 1; F = fvec(list(w), M, p)
    rows.append((p, kk, M, w, F, len(ch[k]), surv[k], '|'.join(sorted(labels[k]))))
rows.sort(key=lambda r: (r[0], r[2], r[3]))
def short(src):
    s = src.split('|'); return src if len(s) <= 3 else f"{'|'.join(s[:3])}|+{len(s) - 3}more"
with open(H + '/nodes_widen.csv', 'w') as f:
    f.write('p,k,M,coords,F0,F1,F2,F3,F4,F5,n_open_children,survival_depth,source\n')
    for p, kk, M, w, F, n, s, lab in rows:
        f.write(f"{p},{kk},{M},{' '.join(map(str, w))},{','.join(map(str, F))},{n},{s},{short(lab)}\n")
nodelist = ''.join(f"{p} {M} {' '.join(map(str, w))}\n" for p, kk, M, w, *_ in rows)
open(H + '/nodelist_widen.txt', 'w').write(nodelist)
sha = hashlib.sha256(nodelist.encode()).hexdigest()
with open(H + '/roots_widen.txt', 'w') as f:
    for lab, p, M, w in proc: f.write(f"{lab} {p} {M} {' '.join(map(str, w))}\n")
def zr(r): return Fraction(int(r[4][0] > 0)) + Fraction(r[4][4], 8)
L = ["PT005 R45 Track A WIDEN - Hesper summary (hesper_r45_widen.py on top of hesper_r45.py; same rules)",
     f"open nodes (distinct p,M,coords) in completed widen subtrees: {len(rows)}",
     f"sha256 of sorted node list (one line per node 'p M coords', sorted by p, M, coords; LF, trailing LF): {sha}",
     f"roots processed: {len(proc)} (status: {dict(collections.Counter(st['status'][r[0]] for r in proc))}); listed in roots_widen.txt in processing order",
     ""]
grp = collections.defaultdict(collections.Counter)
for lab, *_ in proc:
    g = lab.split('_#')[0] if lab.startswith('seed') else ('puck596' if lab.startswith('puck596') else lab.rsplit('_', 1)[0])
    grp[g][st['status'][lab]] += 1
L.append("roots by group: status counts")
for g in sorted(grp): L.append(f"  {g}: {dict(grp[g])}")
L.append("")
L.append("nodes per p / per level (2^k): count, max survival")
byp = collections.defaultdict(list)
for r in rows: byp[r[0]].append(r)
for p in sorted(byp):
    lv = collections.defaultdict(list)
    for r in byp[p]: lv[r[1]].append(r[6])
    L.append(f"  p={p}: {len(byp[p])} nodes; " + '; '.join(f"{2**k}p:{len(v)} (maxsurv {max(v)})" for k, v in sorted(lv.items())))
def table(name, fn, filt=lambda r: True):
    d = collections.defaultdict(list)
    for r in rows:
        if filt(r): d[fn(r)].append(r)
    L.append(""); L.append(f"== {name}: value -> nodes, max survival depth, nodes with >=1 open child; | p>=19: n, maxsurv")
    for v in sorted(d, key=lambda x: float(Fraction(x)) if isinstance(x, str) else x):
        rs = d[v]; big = [r[6] for r in rs if r[0] >= 19]
        L.append(f"  {v}: n={len(rs)} maxsurv={max(r[6] for r in rs)} with_open_child={sum(1 for r in rs if r[5] > 0)}"
                 f"  | p>=19: n={len(big)} maxsurv={max(big) if big else '-'}")
table("F3", lambda r: r[4][3]); table("F4", lambda r: r[4][4])
table("F4 restricted to F0=0", lambda r: r[4][4], lambda r: r[4][0] == 0)
def Z(r):
    p, kk, M, w, F = r[:5]; return Fraction(2 ** (kk - 1) if F[0] > 0 else 0) + Fraction(F[4] * 2 ** kk, 16)
table("zero-fibre capacity Z=[F0>0]*2^(k-1)+F4*2^(k-4) (k>=1 only)", lambda r: str(Z(r)), lambda r: r[1] >= 1)
table("Z/2^(k-1) = [F0>0] + F4/8 (k>=1 only)", lambda r: float(zr(r)), lambda r: r[1] >= 1)
L.append(""); L.append("== F0 split")
for name, f in (("survival>0", lambda r: r[6] > 0), ("survival=0", lambda r: r[6] == 0)):
    rs = [r for r in rows if f(r)]
    L.append(f"  {name}: n={len(rs)}  F0=0: {sum(1 for r in rs if r[4][0] == 0)}  F0>=1: {sum(1 for r in rs if r[4][0] >= 1)}")
exc = [r for r in rows if r[6] > 0 and r[1] >= 1 and (r[4][4] >= 1 or zr(r) > 1) and (r[0], r[2], r[3]) != W5KEY]
f0z = [r for r in rows if r[6] > 0 and r[4][0] == 0]
with open(H + '/exceptions_widen.tsv', 'w') as f:
    f.write('kind\tp\tlevel\tM\tcoords\tF0..F5\tn_open_children\tsurvival\tZ/2^(k-1)\tsource\n')
    for r in exc: f.write(f"F4>=1_or_Z>1_surv>0\t{r[0]}\t{2**r[1]}p\t{r[2]}\t{' '.join(map(str,r[3]))}\t{','.join(map(str,r[4]))}\t{r[5]}\t{r[6]}\t{float(zr(r))}\t{short(r[7])}\n")
    for r in f0z: f.write(f"F0=0_surv>0\t{r[0]}\t{2**r[1]}p\t{r[2]}\t{' '.join(map(str,r[3]))}\t{','.join(map(str,r[4]))}\t{r[5]}\t{r[6]}\t{float(zr(r))}\t{short(r[7])}\n")
L.append(""); L.append("== EXCEPTIONS (completed subtrees). Full list: exceptions_widen.tsv")
L.append(f"  nodes with (F4>=1 or Z/2^(k-1)>1) and survival>0, other than W5 itself: {len(exc)}")
c = collections.Counter((r[0], 2 ** r[1], r[6], r[4][0], r[4][4], (r[7].split('|')[0].rsplit('_', 1)[0])) for r in exc)
for (p, lv, s, f0, f4, g), n in sorted(c.items()): L.append(f"    p={p} {lv}p surv={s} F0={f0} F4={f4} rootgroup={g}: {n}")
L.append(f"  survival>0 nodes with F0=0: {len(f0z)}")
for r in f0z[:20]: L.append(f"    p={r[0]} M={r[2]} {' '.join(map(str,r[3]))} F={r[4]} surv={r[6]}")
# partial info for capped/deferred roots
L.append(""); L.append("== capped / deferred roots (left out of CSV). Partial data in partial_info.jsonl (levels expanded before stop)")
pc = collections.Counter(); pexc = 0; pexc_f0 = collections.Counter(); pmin = collections.Counter()
for l in open(H + '/partial_info.jsonl'):
    r = json.loads(l)
    for M, cw, n, F in r['nodes_with_open_child']:
        kk = (M // r['p']).bit_length() - 1
        if kk >= 1 and (F[4] >= 1 or F[0] == 0) and (r['p'], M, tuple(map(int, cw.split()))) != W5KEY:
            pexc += 1; pexc_f0[(r['p'], M // r['p'], 'F0=0' if F[0] == 0 else 'F0>=1', F[4])] += 1
L.append(f"  nodes in capped/deferred partial levels with >=1 open child (so survival>=1) and F4>=1 or F0=0: {pexc}")
for k, n in sorted(pexc_f0.items()): L.append(f"    p={k[0]} {k[1]}p {k[2]} F4={k[3]}: {n}")
L.append(""); L.append("log (caps / deferrals / not open):")
L.extend('  ' + l for l in st['log'])
L.append(""); L.append("not processed (compute budget), in roots order after the last processed root:")
ug = collections.Counter(r[0].rsplit('_', 1)[0] for r in unproc)
for g, n in ug.items(): L.append(f"  {g}: {n} roots")
open(H + '/summary_widen.txt', 'w').write('\n'.join(L) + '\n')
print(sha, len(rows), len(exc), len(f0z), pexc)
