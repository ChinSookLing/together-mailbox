# Tabulate per_node_r47c.tsv.gz; cross-check sat2 per node vs chair sat2_per_node.csv.gz and Hesper r47 per_node_hesper.tsv.gz.
import gzip, csv, collections
R = list(csv.DictReader(gzip.open('per_node_r47c.tsv.gz', 'rt'), delimiter='\t'))
key = lambda r: (r['p'], r['M'], r['coords'])
out = []
P = lambda *a: out.append(' '.join(str(x) for x in a))
P('k>=1 nodes', len(R))
dead = [r for r in R if r['dead'] == '1']
P('TASK 1: xor-flagged dead', sum(r['xor'] == '1' for r in dead), ' live flagged', sum(r['xor'] == '1' and r['dead'] == '0' for r in R))
P('  xor-flagged but not 2SAT', sum(r['xor'] == '1' and r['sat2'] == '0' for r in R))
s2 = [r for r in R if r['sat2'] == '1']
P('2SAT-dead', sum(r['dead'] == '1' for r in s2), ' live 2SAT', sum(r['dead'] == '0' for r in s2))
# cross-checks
chair = collections.Counter(); 
cm = {}
for r in csv.DictReader(gzip.open('../../opus/r47a/sat2_per_node.csv.gz', 'rt')):
    cm.setdefault(key(r), []).append(r['sat2'] == 'sat2')
hm = {}
for r in csv.DictReader(gzip.open('../r47/trackA_2sat/per_node_hesper.tsv.gz', 'rt'), delimiter='\t'):
    hm.setdefault(key(r), []).append(r['sat2_cert'] == '1')
dis_c = dis_h = 0
for r in R:
    v = r['sat2'] == '1'
    if any(x != v for x in cm.get(key(r), [None])): dis_c += 1
    if any(x != v for x in hm.get(key(r), [None])): dis_h += 1
P('per-node sat2 disagreements vs chair sat2_per_node:', dis_c, ' vs Hesper r47 per_node:', dis_h)
tgt = [r for r in s2 if r['xor'] == '0']
P('TASK 2 target (2SAT-dead, not xor-flagged):', len(tgt))
def hist(rows, f):
    return sorted(collections.Counter(f(r) for r in rows).items())
for lab, f in (('cyc_len', lambda r: int(r['cyc_len'])), ('n_T', lambda r: int(r['n_T'])),
               ('even_on_witness', lambda r: int(r['even_on_witness'])), ('oddonly_unsat', lambda r: int(r['oddonly_unsat'])),
               ('n_anti_pairs', lambda r: int(r['n_anti_pairs'])), ('n_vars', lambda r: int(r['n_vars']))):
    P('\n## overall', lab); [P(' ', k, v, '%.2f%%' % (100 * v / len(tgt))) for k, v in hist(tgt, f)]
ps = sorted(set(int(r['p']) for r in tgt))
for lab, f, ks in (('cyc_len', lambda r: int(r['cyc_len']), None), ('n_T', lambda r: int(r['n_T']), None), ('even_on_witness', lambda r: int(r['even_on_witness']), None), ('oddonly_unsat', lambda r: int(r['oddonly_unsat']), None)):
    ks = sorted(set(f(r) for r in tgt))
    P('\n## per p:', lab, '| columns', ks, '| total')
    for p in ps:
        sub = [r for r in tgt if int(r['p']) == p]; c = collections.Counter(f(r) for r in sub)
        P('  p=%d' % p, ' '.join(str(c.get(k, 0)) for k in ks), '|', len(sub))
P('\n## joint (cyc_len, n_T, even_on_witness) overall')
[P(' ', k, v) for k, v in hist(tgt, lambda r: (int(r['cyc_len']), int(r['n_T']), int(r['even_on_witness'])))]
P('\n## comparison: xor-flagged 2SAT-dead nodes, cyc_len / even')
xr = [r for r in s2 if r['xor'] == '1']
[P(' ', k, v) for k, v in hist(xr, lambda r: (int(r['cyc_len']), int(r['n_T']), int(r['even_on_witness'])))]
open('tables_r47c.txt', 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
