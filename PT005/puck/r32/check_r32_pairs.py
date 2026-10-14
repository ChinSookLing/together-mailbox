# Adapted from PT005/hesper/p19/census.py (+ mod16 line from puck/r29g/rerun_mod16.py).
# Local common.py; PP from env. Independent Puck check for p=23.
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from collections import Counter, defaultdict, deque

def onecls(ws):
    m8 = {w % 8 for w in ws}
    for c in (1, 3):
        if m8 <= {c, 8 - c}:
            return c
    return None

t0 = time.time()
tot = Counter()
mixed = []
single_doublable_by_b = Counter()
n_single = 0
n_mixed = 0

for b in range(1, (P + 1) // 2):
    n5, n6 = N(5), N(6)
    c5 = C(5, b)
    c6 = C(6, (2 * b) % P)
    cls = defaultdict(list)
    for w in legal(5):
        s = frozenset(t for t in c5 if covers(t, w, n5))
        A = tuple(
            frozenset(t for t in c6 if covers(t, (w + e * n5) % n6, n6))
            for e in (0, 1)
        )
        if s:
            cls[(s, A)].append(w)
    bym = defaultdict(list)
    for key in cls:
        bym[min(key[0])].append(key)
    cands = []

    def rec(rem, acc, hits):
        if not rem:
            if all(hits[t] == 2 for t in c6):
                cands.append(list(acc))
            return
        for key in bym[min(rem)]:
            s, A = key
            if not s <= rem or (A[0] & A[1]):
                continue
            h = hits.copy()
            ok = True
            for t in A[0] | A[1]:
                h[t] += 1
                if h[t] > 2:
                    ok = False
                    break
            if ok:
                acc.append(key)
                rec(rem - s, acc, h)
                acc.pop()

    rec(frozenset(c5), [], Counter())
    for cand in cands:
        ws = [cls[k][0] for k in cand]
        c = onecls(ws)
        hitby = defaultdict(list)
        for i, (s, A) in enumerate(cand):
            for e in (0, 1):
                for t in A[e]:
                    hitby[t].append((i, e))
        edges = [
            (h[0][0], h[1][0], h[0][1] ^ h[1][1] ^ 1) for h in hitby.values()
        ]
        adj = defaultdict(list)
        for k, (i, j, l) in enumerate(edges):
            adj[i].append((j, l, k))
            adj[j].append((i, l, k))
        best = None
        for s0 in range(len(cand)):
            dist = {(s0, 0, -1): 0}
            q = deque([(s0, 0, -1)])
            while q:
                x, p, le = q.popleft()
                d = dist[(x, p, le)]
                if best is not None and d >= best:
                    break
                for y, l, k in adj[x]:
                    if k == le:
                        continue
                    st = (y, p ^ l, k)
                    if y == s0 and p ^ l == 1:
                        best = d + 1 if best is None else min(best, d + 1)
                    if st not in dist:
                        dist[st] = d + 1
                        q.append(st)
        kind = "single" if c is not None else "mixed"
        tot[((kind, b), "solvable" if best is None else "unsolvable")] += 1
        if c is None:
            n_mixed += 1
            mixed.append((b, ws, best, {w % 8 for w in ws}, edges))
        else:
            n_single += 1
            if best is None:
                single_doublable_by_b[b] += 1



def q(w):
    x=4*(w%8)*w-4; assert x%32==0; return (x//32)%2
from collections import Counter as _C, defaultdict as _D
stat=_C(); nd2=_C()
for (b,ws,best,m8,edges) in mixed:
    if best!=8: continue
    adj=_D(set)
    for i,j,l in edges: adj[i].add(j); adj[j].add(i)
    # cycle order
    order=[0]; prev=None
    while len(order)<8:
        x=order[-1]; nxt=[y for y in adj[x] if y!=prev and y not in order]
        if not nxt: break
        prev=x; order.append(nxt[0])
    pos={v:k for k,v in enumerate(order)}
    byr=_D(list)
    for i,w in enumerate(ws): byr[w%8].append(i)
    k2=0
    for r,idx in byr.items():
        if len(idx)!=2: stat[('bad count',)]+=1; continue
        d=abs(pos[idx[0]]-pos[idx[1]]); d=min(d,8-d)
        rel = 'diff8' if (ws[idx[0]]-ws[idx[1]])%16==8 else 'equal'
        stat[(r in (3,5) and 'B' or 'A', d, rel)]+=1
        if d==2: k2+=1
    eps=sum(1 for w in ws if w%16>8)
    nd2[(k2, eps%2)]+=1
print("PP",P,dict(stat)," (#dist2 pairs, sum eps mod2):",dict(nd2))
