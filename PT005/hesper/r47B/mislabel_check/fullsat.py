# Hesper independent full check: for every dead (n_open_children==0), k>=1 node that is NOT 2-SAT-dead
# (per Hesper's own per_node_hesper.tsv.gz), decide the FULL clause set over all odd T<=M exactly by
# enumerating all 2^15 lifts as packed bitmasks. A satisfying lift = a child covering every odd T<=M at 2M.
import gzip, csv, sys, numpy as np
from multiprocessing import Pool
A = np.arange(1 << 15, dtype=np.uint32)
LIT = np.zeros((30, 512), dtype=np.uint64)
for i in range(15):
    for b in (0, 1):
        bits = (((A >> i) & 1) == b).astype(np.uint8)
        LIT[b * 15 + i] = np.packbits(bits, bitorder='little').view(np.uint64)
def solve(job):
    idx, p, M, w = job
    w = np.array(w, dtype=np.int64); N = 2 * M
    T = np.arange(1, M + 1, 2, dtype=np.int64)
    L = np.empty((len(T), 30), bool)
    for b in (0, 1):
        R = (T[:, None] * (w + b * M)[None, :]) % N
        L[:, b * 15:(b + 1) * 15] = 16 * np.minimum(R, N - R) < N
    L = L[~(L[:, :15] & L[:, 15:]).any(1)]
    if (~L.any(1)).any(): return idx, 0, -1
    acc = np.full(512, np.uint64(0xFFFFFFFFFFFFFFFF))
    for s in range(0, len(L), 64):
        blk = L[s:s + 64]
        cm = np.bitwise_or.reduce(np.where(blk[:, :, None], LIT[None], np.uint64(0)), axis=1)
        acc &= np.bitwise_and.reduce(cm, axis=0)
        if not acc.any(): return idx, 0, -1
    bits = np.unpackbits(acc.view(np.uint8), bitorder='little')
    sols = np.nonzero(bits)[0]
    return idx, len(sols), int(sols[0])
if __name__ == '__main__':
    rows = list(csv.DictReader(gzip.open(sys.argv[1], 'rt')))
    flags = [l.rstrip('\n').split('\t') for l in gzip.open(sys.argv[2], 'rt')][1:]
    jobs = []
    for i, (r, f) in enumerate(zip(rows, flags)):
        if int(r['k']) >= 1 and f[3] == '1' and f[5] == '0':
            jobs.append((i, int(r['p']), int(r['M']), list(map(int, r['coords'].split()))))
    print("candidates", len(jobs), flush=True)
    out = open('fullsat_satisfiable.tsv', 'w'); out.write("csv_row_1based_data\tp\tk\tM\tcoords\tsource\tn_solutions\tfirst_lift_bits\n")
    cnt = 0; bysrc = {}
    with Pool(2) as pool:
        for idx, n, s in pool.imap_unordered(solve, jobs, chunksize=200):
            if n > 0:
                r = rows[idx]; cnt += 1
                src = r['source'].split('_')[0]; bysrc[(src, r['p'], r['k'])] = bysrc.get((src, r['p'], r['k']), 0) + 1
                out.write(f"{idx+1}\t{r['p']}\t{r['k']}\t{r['M']}\t{r['coords']}\t{r['source']}\t{n}\t{s}\n")
    out.close()
    print("dead-labelled but satisfiable (has covering child):", cnt)
    for k in sorted(bysrc): print(" ", k, bysrc[k])
