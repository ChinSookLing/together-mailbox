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




from collections import Counter as _C, defaultdict as _D
st=_C()
for (b,ws,best,m8,edges) in mixed:
    if best!=8: continue
    adj=_D(set)
    for i,j,l in edges: adj[i].add(j); adj[j].add(i)
    order=[0]; prev=None
    while len(order)<8:
        x=order[-1]; nxt=[y for y in adj[x] if y!=prev and y not in order]; prev=x; order.append(nxt[0])
    order.append(0)
    r=[(ws[order[k+1]]*pow(ws[order[k]],-1,32))%32 for k in range(8)]
    st[tuple(sorted(set(min(x,32-x) for x in r)))]+=1
print("PP",P,"unsigned directed cycle ratio sets:",dict(st))
