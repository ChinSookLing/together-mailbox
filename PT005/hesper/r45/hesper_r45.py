# PT005 R45 Track A (Hesper's own program). Full open subtrees from seed roots.
# Definitions (exact, from the R45 brief): level M=2^k p; node = 15 ints in 1..M-1; children at 2M = all 2^15
# choices w_i or w_i+M; covered T: some i with 16*||T w_i||_M < M; improper: all T in 1..M/2 covered and >=2 odd;
# L7-closed: some even D|M, |E_D|>=2, sum_{E_D} g_i*ceil((D/g_i)/8) < D; open = improper and not L7-closed.
# Speed: for a child of an improper parent, even T=2t (t<=M/2) inherit coverage, so only odd T<=M are tested
# (bitset OR over 2^15 lifts built by doubling). Every root is checked from scratch with the plain definition.
# Nodes deduped per (p,level) as sorted tuples (no +/- symmetry reduction).
import sys, json, math, pickle, os, time
import numpy as np
from math import gcd

def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2; c += 1
    return c

def norm(x, M):
    r = x % M; return min(r, M - r)

def is_open_plain(w, M):
    if sum(x % 2 for x in w) < 2: return False
    for T in range(1, M // 2 + 1):
        if not any(16 * norm(T * x, M) < M for x in w): return False
    for D in range(2, M + 1, 2):
        if M % D: continue
        E = [x for x in w if x % D]
        if len(E) >= 2 and sum(gcd(D, x) * (-(-(D // gcd(D, x)) // 8)) for x in E) < D: return False
    return True

def depths(w, M, p):
    k = (M // p).bit_length() - 1
    return [k - v2(x) if v2(x) < k else 0 for x in w]

def fvec(w, M, p):
    d = depths(w, M, p)
    return [sum(1 for x in d if x == 0)] + [sum(1 for x in d if x >= j) for j in range(1, 6)]

BITS = ((np.arange(1 << 15)[:, None] >> np.arange(15)[None, :]) & 1).astype(np.int64)

def open_children(w, M):
    """w open at M. Returns sorted list of distinct open children (sorted tuples) at N=2M."""
    N = 2 * M
    Ts = np.arange(1, M + 1, 2, dtype=np.int64)
    nb = len(Ts)
    def mask(y):
        r = (Ts * y) % N; d = np.minimum(r, N - r)
        return np.packbits(16 * d < N, bitorder='little')
    full = np.packbits(np.ones(nb, bool), bitorder='little')
    W = len(full)
    cov = np.zeros((1, W), np.uint8)
    for x in w:
        m0 = mask(x); m1 = mask(x + M)
        cov = np.concatenate([cov | m0, cov | m1], axis=0)
    ok = (cov == full[None, :]).all(axis=1)
    del cov
    wa = np.array(w, np.int64)
    C = wa[None, :] + BITS * M
    ok &= (C % 2).sum(axis=1) >= 2
    idx = np.nonzero(ok)[0]
    if len(idx) == 0: return []
    Cs = C[idx]
    alive = np.ones(len(idx), bool)
    for D in range(2, N + 1, 2):
        if N % D: continue
        nz = (Cs % D) != 0
        g = np.gcd(Cs, D)
        term = g * (-(-(D // g) // 8))
        s = (term * nz).sum(axis=1)
        alive &= ~((nz.sum(axis=1) >= 2) & (s < D))
    out = sorted(set(tuple(sorted(int(v) for v in row)) for row in Cs[alive]))
    return out

def load_roots():
    R = []
    R.append(("witnessA_p17", 17, 136, [1,3,3,5,7,8,18,22,40,55,69,75,87,105,110]))
    R.append(("witnessB_p17", 17, 136, [1,3,8,11,13,15,37,49,73,75,79,84,113,117,118]))
    R.append(("W5_p17", 17, 544, [189,224,72,447,176,500,144,128,384,266,80,64,48,32,16]))
    R.append(("GPT_p19_152", 19, 152, [39,59,41,61,43,101,121,8,47,125,145,15,73,55,37]))
    R.append(("Astra_p23_X_184", 23, 184, [10,26,28,56,78,94,95,99,100,121,122,142,146,162,172]))
    R.append(("R43_Grok_p17", 17, 17, [8,11,11,15,3,5,15,11,7,16,1,15,16,3,13]))
    R.append(("R43_GPT_p47", 47, 47, [2,4,5,6,7,8,10,11,13,15,17,18,19,22,23]))
    R.append(("R43_Astra_p43", 43, 43, [2,5,5,6,8,9,13,14,16,16,17,18,19,20,21]))
    R.append(("R43_Astra_p17_R", 17, 17, [1,1,1,2,3,3,3,4,5,5,6,7,7,8,8]))
    # R43 chain intermediate nodes (as committed in PT005/puck/r43/check/puck_r43_check.py)
    R.append(("R43_Grok_p17@2p", 17, 34, [8,11,11,15,3,5,15,11,7,16,1,15,16,3,13]))
    R.append(("R43_Grok_p17@4p", 17, 68, [8,11,11,49,37,5,15,11,7,50,1,15,16,3,13]))
    R.append(("R43_Grok_p17@8p", 17, 136, [8,113,11,49,37,73,83,11,75,50,1,15,16,3,13]))
    R.append(("R43_GPT_p47@2p", 47, 94, [49,51,5,6,7,55,57,11,13,62,17,18,19,69,23]))
    R.append(("R43_GPT_p47@4p", 47, 188, [143,51,5,6,7,149,57,11,107,62,17,112,113,163,23]))
    R.append(("R43_GPT_p47@8p", 47, 376, [143,51,193,194,195,149,245,199,295,62,205,112,113,351,23]))
    R.append(("R43_Astra_p43@2p", 43, 86, [2,5,9,13,16,19,48,49,51,57,59,60,61,63,64]))
    R.append(("R43_Astra_p43@4p", 43, 172, [2,13,16,48,49,51,91,95,105,143,145,146,147,149,150]))
    R.append(("R43_Astra_p43@8p", 43, 344, [2,13,16,49,91,105,143,146,220,223,267,317,319,321,322]))
    R.append(("R43_Astra_p17_X@2p", 17, 34, [1,1,3,3,3,5,6,7,7,8,8,18,19,21,22]))
    R.append(("R43_Astra_p17_Y@8p", 17, 136, [1,3,8,21,22,35,37,41,42,71,73,74,75,86,87]))
    R.append(("AstraR_p47_row", 47, 47, [1,2,3,5,6,8,9,10,11,12,13,14,15,20,21]))
    R.append(("seed20261016_p53", 53, 53, [3,5,6,7,8,9,11,14,15,17,21,23,26,26,26]))
    R.append(("seed20261016_p59", 59, 59, [1,4,5,5,6,7,11,16,17,18,20,21,23,28,29]))
    R.append(("seed20261016_p61", 61, 61, [1,2,5,6,11,11,12,14,16,18,23,26,27,29,30]))
    import glob
    for f in sorted(glob.glob('/workspace/work/l30b/scan_p*.json')):
        d = json.load(open(f)); p = d['p']; tag = os.path.basename(f)[5:-5]
        for j, n in enumerate(d['nodes']):
            R.append((f"l30b_scan_{tag}_{j}", p, 32 * p, n['w32p']))
    return R

# ---------------- driver (resumable; state in state.pkl) ----------------
# Each root gets its own full BFS (global memo of children shared). A root whose subtree exceeds CAP_ROOT distinct
# nodes is abandoned and logged CAPPED; nodes reachable only from capped roots are left out of the CSV.
CAP_ROOT = 120000
STATE = '/workspace/work/r45/state.pkl'

def init_state():
    roots = load_roots()
    st = {'children': {}, 'log': [], 'roots': roots, 'queue': [], 'status': {}, 'cur': None}
    for lab, p, M, w in roots:
        w = list(w)
        if len(w) != 15 or not all(1 <= x <= M - 1 for x in w):
            st['log'].append(f"ROOT {lab} p={p} M={M} invalid coords"); st['status'][lab] = 'invalid'; continue
        if not is_open_plain(w, M):
            st['log'].append(f"ROOT {lab} p={p} M={M} NOT OPEN, skipped"); st['status'][lab] = 'not_open'; continue
        st['queue'].append((lab, (p, M, tuple(sorted(w)))))
    return st

def step(st, tlimit):
    t0 = time.time()
    while st['cur'] or st['queue']:
        if st['cur'] is None:
            lab, key = st['queue'].pop(0)
            st['cur'] = {'lab': lab, 'root': key, 'level': [key], 'seen': 1, 'nxt': set(), 'i': 0}
        c = st['cur']
        while c['level']:
            lev = c['level']
            while c['i'] < len(lev):
                key = lev[c['i']]
                if key not in st['children']:
                    p, M, w = key
                    st['children'][key] = [(p, 2 * M, ch) for ch in open_children(list(w), M)]
                c['nxt'].update(st['children'][key])
                c['i'] += 1
                if time.time() - t0 > tlimit: return False
            c['seen'] += len(c['nxt'])
            c['level'] = sorted(c['nxt']); c['nxt'] = set(); c['i'] = 0
            if c['seen'] > CAP_ROOT:
                p, M, _ = c['root']
                st['log'].append(f"CAPPED root {c['lab']} p={p} M={M}: subtree > {CAP_ROOT} nodes "
                                 f"(next frontier {len(c['level'])} at {c['level'][0][1]//p}p); left out")
                st['status'][c['lab']] = 'capped'; break
        if st['status'].get(c['lab']) != 'capped': st['status'][c['lab']] = 'done'
        st['cur'] = None
    return True

if __name__ == '__main__' and sys.argv[1:2] == ['run']:
    st = pickle.load(open(STATE, 'rb')) if os.path.exists(STATE) else init_state()
    done = step(st, float(sys.argv[2]) if len(sys.argv) > 2 else 90)
    pickle.dump(st, open(STATE + '.tmp', 'wb')); os.replace(STATE + '.tmp', STATE)
    c = st['cur']
    print('DONE' if done else 'PARTIAL', 'memo', len(st['children']), 'queue', len(st['queue']),
          'cur', (c['lab'], c['level'][0][1] if c['level'] else None, c['i'], len(c['level']), c['seen']) if c else None)
    for l in st['log']:
        if not l.startswith('ROOT l30b'): print(' ', l)

def build_outputs():
    import hashlib, collections
    st = pickle.load(open(STATE, 'rb'))
    ch = st['children']
    labels = {}
    for lab, key in [(l, (p, M, tuple(sorted(w)))) for l, p, M, w in st['roots']]:
        if st['status'].get(lab) != 'done': continue
        stack = [key]
        while stack:
            k = stack.pop()
            s = labels.setdefault(k, set())
            if lab in s: continue
            s.add(lab); stack.extend(ch[k])
    surv = {}
    for k in sorted(labels, key=lambda k: -(k[1] // k[0])):  # deepest levels first
        kids = ch[k]
        surv[k] = 0 if not kids else 1 + max(surv[c] for c in kids)
    rows = []
    for k in labels:
        p, M, w = k
        kk = (M // p).bit_length() - 1
        F = fvec(list(w), M, p)
        rows.append((p, kk, M, w, F, len(ch[k]), surv[k], '|'.join(sorted(labels[k]))))
    rows.sort(key=lambda r: (r[0], r[2], r[3]))
    with open('/workspace/work/r45/hesper_nodes.csv', 'w') as f:
        f.write('p,k,M,coords,F0,F1,F2,F3,F4,F5,n_open_children,survival_depth,source\n')
        for p, kk, M, w, F, n, s, lab in rows:
            f.write(f"{p},{kk},{M},{' '.join(map(str, w))},{','.join(map(str, F))},{n},{s},{lab}\n")
    nodelist = ''.join(f"{p} {M} {' '.join(map(str, w))}\n" for p, kk, M, w, *_ in rows)
    sha = hashlib.sha256(nodelist.encode()).hexdigest()
    open('/workspace/work/r45/hesper_nodelist.txt', 'w').write(nodelist)
    L = []
    L.append("PT005 R45 Track A - Hesper summary (own program hesper_r45.py)")
    L.append(f"open nodes (distinct p,M,coords): {len(rows)}")
    L.append(f"sha256 of sorted node list (one line per node 'p M coords', sorted by p, M, coords tuple; LF endings, trailing LF): {sha}")
    L.append("")
    L.append("nodes per p / per level (2^k): count, max survival")
    byp = collections.defaultdict(list)
    for r in rows: byp[r[0]].append(r)
    for p in sorted(byp):
        lv = collections.defaultdict(list)
        for r in byp[p]: lv[r[1]].append(r[6])
        L.append(f"  p={p}: {len(byp[p])} nodes; " + '; '.join(f"{2**k}p:{len(v)} (maxsurv {max(v)})" for k, v in sorted(lv.items())))
    from fractions import Fraction
    def table(name, fn, filt=lambda r: True, rowsel=rows):
        d = collections.defaultdict(list)
        for r in rowsel:
            if filt(r): d[fn(r)].append(r)
        L.append("")
        L.append(f"== {name}: value -> nodes, max survival depth, nodes with >=1 open child; (max survival restricted to p>=19)")
        for v in sorted(d, key=lambda x: float(Fraction(x)) if isinstance(x, str) else x):
            rs = d[v]; big = [r[6] for r in rs if r[0] >= 19]
            L.append(f"  {v}: n={len(rs)} maxsurv={max(r[6] for r in rs)} with_open_child={sum(1 for r in rs if r[5] > 0)}"
                     f"  | p>=19: n={len(big)} maxsurv={max(big) if big else '-'}")
    table("F3", lambda r: r[4][3])
    table("F4", lambda r: r[4][4])
    table("F4 restricted to F0=0", lambda r: r[4][4], lambda r: r[4][0] == 0)
    from fractions import Fraction
    def Z(r):
        p, kk, M, w, F = r[:5]
        z = (2 ** (kk - 1) if (F[0] > 0 and kk >= 1) else 0) + (Fraction(F[4] * 2 ** kk, 16))
        return z
    table("zero-fibre capacity Z=[F0>0]*2^(k-1)+F4*2^(k-4) (k>=1 only)", lambda r: str(Z(r)) if Z(r).denominator == 1 else str(Z(r)),
          lambda r: r[1] >= 1)
    table("Z/2^(k-1) = [F0>0] + F4/8 (k>=1 only)", lambda r: float(Fraction(int(r[4][0] > 0)) + Fraction(r[4][4], 8)),
          lambda r: r[1] >= 1)
    L.append("")
    L.append("notes:")
    L.append("  survival_depth: 0 = no open child; else 1 + max over open children. Every listed node's full open subtree was computed (no partial subtrees).")
    L.append("  source: '|'-joined labels of every completed root whose subtree contains the node.")
    L.append("  Z tables use k>=1 nodes only (level-p rows k=0 omitted, 2^(k-1) undefined). Z is NOT normalised across k; the Z/2^(k-1) table is.")
    L.append("  Dedupe is exact sorted tuples (no per-coordinate sign reduction), so counts differ from canon(+/-) counts in older logs.")
    L.append("  Two level-p p=17 roots (R43 Grok, R43 Astra R) exceed the cap (4p frontier 0.5-0.9M nodes); replaced by their committed chain nodes at 2p/4p/8p as roots.")
    L.append("  Discrepancy: the committed R43 Grok p=17 8p vector [8,113,11,49,37,73,83,11,75,50,1,15,16,3,13] is NOT a lift of its 4p vector (mod 68 it has 45, not a second 11); it is open with 0 open children, and the 4p vector itself has 0 open children. Both kept as separate roots.")
    L.append("  l30b scan rows (p=19..43, 140 rows at 32p): 79 open, 61 improper-but-L7-closed or not improper (logged as NOT OPEN, skipped).")
    L.append("  Cross-check: p=53 seed row gives F3=3 -> 176 nodes, 0 with open child (matches chair R44 evidence table row).")
    L.append("")
    L.append("roots: label status")
    for lab, p, M, w in st['roots']:
        L.append(f"  {lab} p={p} M={M} {st['status'].get(lab)}")
    L.append("")
    L.append("log:")
    L.extend('  ' + l for l in st['log'])
    open('/workspace/work/r45/hesper_summary.txt', 'w').write('\n'.join(L) + '\n')
    print(sha, len(rows))

if __name__ == '__main__' and sys.argv[1:2] == ['out']:
    build_outputs()
