# Hesper independent reproduction of chair note 103 (PT005 R47 Track A), written from the note's definitions.
# Method: per (p,M) group, numpy batches. 2-SAT decided by Floyd-Warshall transitive closure on 30 literals.
# Coverage: child level N=2M, lift w or w+M covers odd T iff 16*||T*w/N||*N < N, i.e. 16*min(r,N-r) < N.
# Singleton (sec 1): node level M, odd T <= M/2, 2T != M, "near" iff 8*min(r,M-r) < M;
#   certified iff some T has no near coord, or exactly one near coord and it is odd.
import gzip, csv, sys, collections, numpy as np
rows = list(csv.DictReader(gzip.open(sys.argv[1], 'rt')))
n = len(rows)
P = np.array([int(r['p']) for r in rows]); K = np.array([int(r['k']) for r in rows])
Mv = np.array([int(r['M']) for r in rows]); dead = np.array([int(r['n_open_children']) == 0 for r in rows])
W = np.array([list(map(int, r['coords'].split())) for r in rows], dtype=np.int64)
assert W.shape[1] == 15
sat2 = np.zeros(n, bool); emptycl = np.zeros(n, bool); single = np.zeros(n, bool)
groups = collections.defaultdict(list)
for i in range(n): groups[(P[i], Mv[i])].append(i)
NEG = (np.arange(30) + 15) % 30
for (p, M), idx in sorted(groups.items()):
    idx = np.array(idx); N = 2 * M
    T2 = np.arange(1, M + 1, 2, dtype=np.int64)            # odd T <= M (child level)
    T1 = np.array([t for t in range(1, M // 2 + 1, 2) if 2 * t != M], dtype=np.int64)
    bs = max(1, int(3e7 // (len(T2) * 30)))
    for s in range(0, len(idx), bs):
        ii = idx[s:s + bs]; w = W[ii]; m = len(ii)
        # ---- sec 1 singleton
        R = (T1[None, :, None] * w[:, None, :]) % M
        near = 8 * np.minimum(R, M - R) < M
        cnt = near.sum(2)
        oddnear = (near & (w % 2 == 1)[:, None, :]).sum(2)
        single[ii] = ((cnt == 0) | ((cnt == 1) & (oddnear == 1))).any(1)
        if M % 2 == 1:  # k=0: sec 2 not applicable
            continue
        # ---- sec 2 2-SAT
        L = np.empty((m, len(T2), 30), bool)
        for b in (0, 1):
            R = (T2[None, :, None] * (w + b * M)[:, None, :]) % N
            L[:, :, b * 15:(b + 1) * 15] = 16 * np.minimum(R, N - R) < N
        taut = (L[:, :, :15] & L[:, :, 15:]).any(2)
        sz = L.sum(2)
        emptycl[ii] = ((sz == 0) & ~taut).any(1)
        G = np.zeros((m, 30, 30), bool)
        node, tt = np.nonzero((~taut) & (sz == 1))
        lit = L[node, tt].argmax(1)
        G[node, NEG[lit], lit] = True
        node, tt = np.nonzero((~taut) & (sz == 2))
        two = np.argsort(~L[node, tt], axis=1, kind='stable')[:, :2]
        l1, l2 = two[:, 0], two[:, 1]
        G[node, NEG[l1], l2] = True; G[node, NEG[l2], l1] = True
        for k in range(30):
            G |= G[:, :, k:k + 1] & G[:, k:k + 1, :]
        sat2[ii] = (G[:, np.arange(15), np.arange(15) + 15] & G[:, np.arange(15) + 15, np.arange(15)]).any(1) | emptycl[ii]
k1 = K >= 1; p17 = P == 17
print("nodes", n, "k>=1", int(k1.sum()), "k=0", int((~k1).sum()))
print("SEC2 (k>=1):")
for lab, msk in (("p17", p17), ("p>=19", ~p17), ("total", np.ones(n, bool))):
    mk = msk & k1
    print(f"  {lab}: dead+2SAT {int((mk&dead&sat2).sum())}  dead-no-cert {int((mk&dead&~sat2).sum())}  live-flagged {int((mk&~dead&sat2).sum())}  empty-clause {int((mk&emptycl).sum())}")
print("SEC1:")
print(f"  k>=1 certified {int((single&k1).sum())}  of which dead {int((single&k1&dead).sum())}  with open child {int((single&k1&~dead).sum())}")
print(f"  k=0 certified {int((single&~k1).sum())}  with open child {int((single&~k1&~dead).sum())}")
print(f"  dead total {int(dead.sum())}  k>=1 dead {int((dead&k1).sum())}")
with gzip.open("per_node_hesper.tsv.gz", "wt") as f:
    f.write("p\tM\tcoords\tdead\tsingle_cert\tsat2_cert\n")
    for i, r in enumerate(rows):
        f.write(f"{r['p']}\t{r['M']}\t{r['coords']}\t{int(dead[i])}\t{int(single[i])}\t{int(sat2[i])}\n")
