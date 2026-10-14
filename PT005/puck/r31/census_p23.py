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
            mixed.append((b, ws, best, {w % 8 for w in ws}))
        else:
            n_single += 1
            if best is None:
                single_doublable_by_b[b] += 1

print("PP", P)
for k, v in sorted(tot.items()):
    print(k, v)
L = Counter(m[2] for m in mixed)
print("mixed shortest odd cycle lengths", dict(L))
print("mixed total", len(mixed), "mod8 sets", Counter(tuple(sorted(m[3])) for m in mixed))
print("by b x shortest", sorted(Counter((m[0], m[2]) for m in mixed).items()))

# mod16 distinctness by shortest-odd-cycle length (Puck care: length-4 not always universal)
m16_by_len = defaultdict(Counter)  # length -> {n_distinct: count}
for m in mixed:
    Llen = m[2]
    nd = len({w % 16 for w in m[1]})
    m16_by_len[Llen][nd] += 1
print("mod16 distinct counts by shortest-odd length:")
for Llen in sorted(m16_by_len):
    c = m16_by_len[Llen]
    n8 = c.get(8, 0)
    total = sum(c.values())
    print(f"  length-{Llen}: {n8}/{total} have 8 distinct; full={dict(c)}")

print("n_mixed", n_mixed, "n_single", n_single, "n_total", n_mixed + n_single)
print("mixed doublable (solvable)", sum(1 for m in mixed if m[2] is None))
print("single doublable total", sum(single_doublable_by_b.values()))
print("single doublable by b", dict(sorted(single_doublable_by_b.items())))
print("elapsed_s", round(time.time() - t0, 3))
