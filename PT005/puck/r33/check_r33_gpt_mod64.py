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
            mixed.append((b, ws, best, {w % 8 for w in ws}, edges, dict(hitby), cand))
        else:
            n_single += 1
            if best is None:
                single_doublable_by_b[b] += 1





# === Puck R33 check of GPT mod-64 Hamiltonian argument ===
from collections import Counter as _C, defaultdict as _D
res=_C(); fails=[]
def bal(x,p):
    d=x%p
    if d>p//2: d-=p
    return d
for (b,ws,best,m8,edges,hitby,cand) in mixed:
    if best!=8: continue
    res['cases']+=1
    # vertex data
    m=[];c=[];v=[]
    for w in ws:
        d=bal(b*w,P); M=(b*w-d)//P; vv=pow(w,-1,32)
        m.append(M); v.append(vv); c.append((-2*M*vv)%32)
    # footprint check: t mod 32 of members covered by both lifts == c+{±v,±3v}
    fp_ok=True
    for i,(s,A) in enumerate(cand):
        T=set()
        for t in A[0]|A[1]:
            for eps in (1,-1):
                if (t-2*b*eps)%P==0:
                    u=(t-2*b*eps)//P; T.add((eps*u)%32); break
        U={(c[i]+a*v[i])%32 for a in (-3,-1,1,3)}
        if T!=U: fp_ok=False
    res['footprint_ok']+=fp_ok
    # parallel edges: group edges by vertex pair
    pair=_D(list)
    for t,h in hitby.items():
        (i,ei),(j,ej)=h
        key=tuple(sorted((i,j)))
        pair[key].append(ei^ej^1)
    npairs=len(pair)
    res[('npairs',npairs)]+=1
    consistent=all(len(set(L))==1 for L in pair.values())
    res['labels_consistent']+=consistent
    res['common_c']+= (len(set(c))==1)
    # label diff formula: lam(s) xor lam(s') == (c_i-c_j)/16 mod 2
    if not consistent or len(set(c))!=1:
        diff_ok=True
        for (i,j),L in pair.items():
            if len(L)==2:
                pred=(((c[i]-c[j])%32)//16)%2
                if (L[0]^L[1])!=pred: diff_ok=False
        res['diff_formula_ok_when_inconsistent']+=diff_ok
        res['inconsistent_cases']+=1
        continue
    # orient cycle using adjacency, choose direction with ratio ±3
    adj=_D(set)
    for (i,j) in pair: adj[i].add(j); adj[j].add(i)
    order=[0]; prev=None
    while len(order)<8:
        x=order[-1]; nxt=[y for y in adj[x] if y!=prev and y not in order]; prev=x; order.append(nxt[0])
    r=(ws[order[1]]*pow(ws[order[0]],-1,32))%32
    if r not in (3,29): order=[order[0]]+order[1:][::-1]
    lab={k:L[0] for k,L in pair.items()}
    K=[];sig=[];step_ok=True; lam_ok=True
    h=[]
    hint=True
    for i in range(8):
        x=(2*m[i]+c[0]*ws[i])
        if x%32: hint=False
        h.append(x//32)
    res['h_integer']+=hint
    for n in range(8):
        i=order[n]; j=order[(n+1)%8]
        found=False
        for s_ in (1,-1):
            dd=ws[j]-3*s_*ws[i]
            if dd%32==0: K.append(dd//32); sig.append(s_); found=True; break
        if not found: step_ok=False; K.append(0); sig.append(1)
        lam=lab[tuple(sorted((i,j)))]
        pred=(1+h[i]+h[j]+K[-1])%2
        if lam!=pred: lam_ok=False
    res['steps_pm3']+=step_ok
    res['lambda_formula_ok']+=lam_ok
    H=sum(lab.values())%2
    res['H_eq_sumK']+= (H==sum(K)%2)
    res['sumK_odd']+= (sum(K)%2==1)
    if not (fp_ok and step_ok and lam_ok and hint): fails.append((b,ws))
print("PP",P,dict(res)); print("fails",fails[:5])
