# Brute-force check of the 2-SAT verdict: for sampled k>=1 nodes, enumerate all 2^15 lifts and test the
# unit+binary clause subset literally (pure python, no numpy shortcuts shared with hesper_r47a.py).
import gzip, csv, sys, random
random.seed(1018)
rows = [r for r in csv.DictReader(gzip.open(sys.argv[1], 'rt')) if int(r['k']) >= 1]
sample = random.sample(rows, int(sys.argv[2]))
def cov(T, w, N):
    r = (T * w) % N
    return 16 * min(r, N - r) < N
out = []
for r in sample:
    M = int(r['M']); N = 2 * M; w = list(map(int, r['coords'].split()))
    clauses = []
    for T in range(1, M + 1, 2):
        lits = [(i, b) for i in range(15) for b in (0, 1) if cov(T, w[i] + b * M, N)]
        if any((i, 0) in lits and (i, 1) in lits for i in range(15)): continue
        if len(lits) <= 2: clauses.append(lits)
    unsat = True
    for a in range(1 << 15):
        if all(any(((a >> i) & 1) == b for i, b in cl) for cl in clauses):
            unsat = False; break
    out.append((r['p'], r['M'], r['coords'], unsat))
for o in out: print(*o, sep='\t')
