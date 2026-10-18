# Extra measurement on the cyc_len=2 witnesses of the TASK 2 target: one coordinate w, two times T1<T2 (units, opposite bits).
# Tabulate v2(w) relative to k (M=2^k p), and (T1+T2) mod M, (T2-T1) mod M as fractions of M.
import gzip, csv, collections
from fractions import Fraction
R = csv.DictReader(gzip.open('per_node_r47c.tsv.gz', 'rt'), delimiter='\t')
cv = collections.Counter(); cs = collections.Counter(); cd = collections.Counter(); n = 0
def v2(x):
    c = 0
    while x % 2 == 0: x //= 2; c += 1
    return c
for r in R:
    if r['sat2'] != '1' or r['xor'] != '0' or r['cyc_len'] != '2': continue
    n += 1; M = int(r['M']); p = int(r['p']); k = v2(M)
    T1, T2 = map(int, r['witness_T'].split()); W = list(map(int, r['coords'].split()))
    N = 2 * M
    # find the coordinate: covered by a unit at both T's
    cand = [w for w in W if all(any(16 * min((T * (w + b * M)) % N, N - (T * (w + b * M)) % N) < N for b in (0, 1)) for T in (T1, T2))]
    w = cand[0] if len(cand) == 1 else None
    cv[(k, v2(w) if w else 'amb')] += 1
    cs[str(Fraction((T1 + T2) % M, M))] += 1; cd[str(Fraction((T2 - T1) % M, M))] += 1
out = ['len-2 target witnesses: %d' % n, '(k, v2(w)) counts:'] + ['  %s %d' % kv for kv in sorted(cv.items(), key=str)]
out += ['(T1+T2) mod M as fraction of M, top 15:'] + ['  %s %d' % kv for kv in cs.most_common(15)]
out += ['(T2-T1) mod M as fraction of M, top 15:'] + ['  %s %d' % kv for kv in cd.most_common(15)]
open('len2_r47c.txt', 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
