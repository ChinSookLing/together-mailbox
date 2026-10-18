# Hesper R47C (PT005): independent program, written from note 103/104 definitions + 1523 erratum.
# Does NOT import or copy PT005/opus/r47a/xor.py or sat2.py.
# Input: Track A node list nodes_widen.csv.gz (k>=1 nodes only, M = 2^k p even).
# Literals: child level N=2M; var i (0..14) bit b; literal index b*15+i; lift w_i+b*M covers odd T iff 16*min(r,N-r)<N, r=T(w_i+bM) mod N.
# Clause at odd T (1<=T<=M): OR of covering literals (half-lap: exactly one per coord in E_M(T)); tautologies counted (expect 0).
# Task 1 (XOR / antipodal): for odd T<M/2 with E(T) all-odd and |E|<=2, combine clauses at T and M-T:
#   |E|=1 -> contradiction; |E|=2 -> b_i xor b_j = a_i xor a_j xor 1 (a = covering bit at T). Consistency via
#   reachability on the 30-vertex parity-lifted graph (vertex (i,s)=s*15+i), Floyd-Warshall boolean closure.
#   Pairs (T,M-T) are checked: E(M-T)=E(T) and complementary bits for odd coords (mismatches counted).
# Task 2: unit+binary clauses -> implication graph (unit l: edge ~l->l; binary l1 v l2: ~l1->l2, ~l2->l1).
#   Edge label = smallest T producing it. Min-plus Floyd-Warshall with next-hop. Witness = var x minimising
#   d(x,~x)+d(~x,x) (ties: lowest var index; path ties: FW next-hop order). Report length, distinct T,
#   antipodal pairs among those T, distinct vars, even coord on witness, and (tie-free) whether 2-SAT stays
#   UNSAT using only clauses whose coords are all odd.
import gzip, csv, sys, collections, numpy as np
from multiprocessing import Pool
INF = 1000
NEG = (np.arange(30) + 15) % 30
def work(job):
    p, M, idx, W = job
    N = 2 * M; m = len(idx)
    T2 = np.arange(1, M + 1, 2, dtype=np.int64); nT = len(T2)
    L = np.empty((m, nT, 30), bool)
    for b in (0, 1):
        R = (T2[None, :, None] * (W + b * M)[:, None, :]) % N
        L[:, :, b*15:(b+1)*15] = 16 * np.minimum(R, N - R) < N
    taut = (L[:, :, :15] & L[:, :, 15:])
    ntaut = int(taut.any(2).sum())
    E = L[:, :, :15] | L[:, :, 15:]
    sz = E.sum(2)
    nempty = int((sz == 0).sum())
    oddw = (W % 2 == 1)
    # ---------------- Task 1
    half = T2[T2 * 2 < M]                 # odd T < M/2 ; antipode M-T odd, > M/2
    ti = (half - 1) // 2; tj = (M - half - 1) // 2
    Ea, Eb = E[:, ti, :], E[:, tj, :]
    mis_E = int((Ea != Eb).any(2).sum())
    bitA = L[:, ti, 15:]; bitB = L[:, tj, 15:]   # covering bit = 1 ?
    mis_bit = int((Ea & oddw[:, None, :] & (bitA == bitB)).sum())
    allodd = ~(Ea & ~oddw[:, None, :]).any(2)
    s = Ea.sum(2)
    xorflag = ((s == 1) & allodd).any(1)
    G = np.zeros((m, 30, 30), bool)
    nn, tt = np.nonzero((s == 2) & allodd)
    if len(nn):
        two = np.argsort(~Ea[nn, tt], axis=1, kind='stable')[:, :2]
        i, j = two[:, 0], two[:, 1]
        c = bitA[nn, tt, i] ^ bitA[nn, tt, j] ^ True
        c = c.astype(int)
        for sbit in (0, 1):
            u = sbit * 15 + i; v = ((sbit ^ c) * 15) + j
            G[nn, u, v] = True; G[nn, v, u] = True
    for k in range(30):
        G |= G[:, :, k:k+1] & G[:, k:k+1, :]
    xorflag |= G[:, np.arange(15), np.arange(15) + 15].any(1)
    # ---------------- Task 2
    D = np.full((m, 30, 30), INF, np.int32)
    Tm = np.full((m, 30, 30), 1 << 30, np.int64)
    Godd = np.zeros((m, 30, 30), bool)
    clauseodd = ~(E & ~oddw[:, None, :]).any(2)
    def add(nn, tt, u, v):
        D[nn, u, v] = 1
        np.minimum.at(Tm, (nn, u, v), T2[tt])
        ok = clauseodd[nn, tt]
        Godd[nn[ok], u[ok], v[ok]] = True
    nn, tt = np.nonzero(sz == 1)
    lit = L[nn, tt].argmax(1)
    add(nn, tt, NEG[lit], lit)
    nn, tt = np.nonzero(sz == 2)
    two = np.argsort(~L[nn, tt], axis=1, kind='stable')[:, :2]
    l1, l2 = two[:, 0], two[:, 1]
    add(nn, tt, NEG[l1], l2); add(nn, tt, NEG[l2], l1)
    Nx = np.broadcast_to(np.arange(30)[None, None, :], (m, 30, 30)).copy()
    for k in range(30):
        cand = D[:, :, k:k+1] + D[:, k:k+1, :]
        better = cand < D
        D = np.where(better, cand, D)
        Nx = np.where(better, np.broadcast_to(Nx[:, :, k:k+1], Nx.shape), Nx)
        Godd |= Godd[:, :, k:k+1] & Godd[:, k:k+1, :]
    a = np.arange(15)
    Lx = D[:, a, a + 15] + D[:, a + 15, a]
    best = Lx.argmin(1); Lmin = Lx.min(1)
    sat2 = Lmin < INF
    oddonly = (Godd[:, a, a + 15] & Godd[:, a + 15, a]).any(1)
    out = []
    for r in range(m):
        if not sat2[r]:
            out.append((idx[r], int(xorflag[r]), 0, -1, -1, -1, -1, -1, int(oddonly[r]), ''))
            continue
        x = int(best[r]); Ts = []; lits = []
        for (u, v) in ((x, x + 15), (x + 15, x)):
            while u != v:
                n = int(Nx[r, u, v]); Ts.append(int(Tm[r, u, n])); lits += [u, n]; u = n
        Tset = sorted(set(Ts)); vars_ = sorted(set(l % 15 for l in lits))
        anti = sum(1 for t in Tset if t < M - t and (M - t) in Tset)
        even = int(any(W[r, v] % 2 == 0 for v in vars_))
        assert len(Ts) == Lmin[r]
        out.append((idx[r], int(xorflag[r]), 1, int(Lmin[r]), len(Tset), anti, len(vars_), even, int(oddonly[r]), ' '.join(map(str, Tset))))
    return out, ntaut, nempty, mis_E, mis_bit

def jobs(rows):
    groups = collections.defaultdict(list)
    for i, r in enumerate(rows):
        if int(r['k']) >= 1: groups[(int(r['p']), int(r['M']))].append(i)
    for (p, M), idx in sorted(groups.items()):
        bs = max(1, int(1.2e7 // ((M // 2 + 1) * 30)))
        for s in range(0, len(idx), bs):
            ii = idx[s:s+bs]
            W = np.array([list(map(int, rows[i]['coords'].split())) for i in ii], dtype=np.int64)
            yield (p, M, ii, W)

if __name__ == '__main__':
    rows = list(csv.DictReader(gzip.open(sys.argv[1], 'rt')))
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    tot = collections.Counter(); res = {}
    with Pool(2) as pool:
        for out, a, b, c, d in pool.imap_unordered(work, jobs(rows)):
            tot['taut'] += a; tot['empty'] += b; tot['misE'] += c; tot['misbit'] += d
            for o in out: res[o[0]] = o[1:]
    with gzip.open('per_node_r47c.tsv.gz', 'wt') as f:
        f.write('p\tM\tcoords\tdead\txor\tsat2\tcyc_len\tn_T\tn_anti_pairs\tn_vars\teven_on_witness\toddonly_unsat\twitness_T\n')
        for i in sorted(res):
            r = rows[i]; d = int(int(r['n_open_children']) == 0)
            f.write('\t'.join([r['p'], r['M'], r['coords'], str(d)] + [str(x) for x in res[i]]) + '\n')
    print('checks', dict(tot))
