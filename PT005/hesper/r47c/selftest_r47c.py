# Self-test for hesper_r47c.py output. Deterministic sample: random.Random(47003), 3000 nodes with sat2=1 & xor=0,
# plus 500 nodes with sat2=0 (k>=1). Brute force over all 2^15 lifts, coverage from the child-level definition.
# Checks: (1) witness T-set clauses alone are UNSAT; (2) irredundancy: dropping any one witness T makes it SAT
# (reported, not required); (3) for sat2=0 nodes, unit+binary clauses over all odd T<=M are SAT.
import gzip, random, numpy as np, collections
rows = [l.rstrip('\n').split('\t') for l in gzip.open('per_node_r47c.tsv.gz', 'rt')]
hdr = rows[0]; rows = rows[1:]; H = {h: i for i, h in enumerate(hdr)}
A = [r for r in rows if r[H['sat2']] == '1' and r[H['xor']] == '0']
B = [r for r in rows if r[H['sat2']] == '0']
rng = random.Random(47003); SA = rng.sample(A, 3000); SB = rng.sample(B, 500)
asg = np.arange(1 << 15, dtype=np.int64)
bits = ((asg[:, None] >> np.arange(15)) & 1).astype(bool)
def clause_ok(M, W, T):
    N = 2 * M; s = np.zeros(1 << 15, bool); n = 0
    for i, w in enumerate(W):
        for b in (0, 1):
            r = (T * (w + b * M)) % N
            if 16 * min(r, N - r) < N:
                s |= (bits[:, i] == bool(b)); n += 1
    return s, n
def sat(M, W, Ts, maxsize=2):
    ok = np.ones(1 << 15, bool)
    for T in Ts:
        s, n = clause_ok(M, W, T)
        if n <= maxsize: ok &= s
    return ok.any()
c = collections.Counter()
for r in SA:
    M = int(r[H['M']]); W = list(map(int, r[H['coords']].split())); Ts = list(map(int, r[H['witness_T']].split()))
    c['A_witness_unsat'] += (not sat(M, W, Ts))
    c['A_irredundant'] += all(sat(M, W, Ts[:j] + Ts[j+1:]) for j in range(len(Ts)))
for r in SB:
    M = int(r[H['M']]); W = list(map(int, r[H['coords']].split()))
    c['B_sat'] += sat(M, W, range(1, M + 1, 2))
print('sampleA', len(SA), 'sampleB', len(SB), dict(c))
