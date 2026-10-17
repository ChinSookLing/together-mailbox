# PT005 R45 Track A WIDEN (Hesper program). Same node rule, child rule, dedupe, cap and columns as
# PT005/hesper/r45/hesper_r45.py (imported unchanged: is_open_plain, open_children, fvec).
# Roots (roots_widen.txt, one line per root: label p M coords):
#   A  puck596_*   : Puck's p=17 nodes from PT005/puck/r43f3/check/puck_f3_nodes.json.gz, trees
#                    'Astra p17 chain @2p' and 'Grok p17 chain @2p', records with Puck's F3>=8 and open_children>=1
#                    (the 596 of analyse_f3.out line 19).
#   B  seed*_p{p}_#i : rows exactly as r43pre tree3.py pick(): random.Random(20261016), 15 x randrange(1,(p+1)//2), sorted,
#                    first improper at level p, distinct up to +/- canon. Existing seed rows (p53/59/61 #1) excluded.
#                    p>=43: level-p rows #1..#8 as roots. p=19..41: every level-p row caps at 4p (probe log), so each of
#                    rows #1..#5 contributes K open 2p children drawn by random.Random(20261017*1000+p*16+i).sample.
#                    p=31: only one improper row exists ([1..15]); p=29/31 rows distinct canon only.
#   C  W5sib_a{L}p_* : every open child of each W5 ancestor (W5 mod L*p, L=16,8,4,2,1), ordered nearest ancestor first.
# Engine: level BFS per root over a shared memo of open children; child computation in parallel (2 workers); resumable.
import sys, os, json, gzip, time, pickle, random
sys.path.insert(0, '/workspace/work/r45')
from hesper_r45 import is_open_plain, open_children, fvec

HERE = '/workspace/work/r45/widen'
STATE = HERE + '/state_widen.pkl'
CAP_ROOT = 120000
PUCK = '/workspace/work/together-mailbox/PT005/puck/r43f3/check/puck_f3_nodes.json.gz'
W5 = [189, 224, 72, 447, 176, 500, 144, 128, 384, 266, 80, 64, 48, 32, 16]
K_SUB = 3
DEFER = 5000  # W5 sibling roots only: a level with more unexpanded nodes than this is not expanded (budget)

def roots_widen():
    R = []
    d = json.load(gzip.open(PUCK))
    for tname, tag in (('Astra p17 chain @2p', 'AstraX'), ('Grok p17 chain @2p', 'Grok')):
        t = d['trees'][tname]
        for li, lev in enumerate(t['levels']):
            for j, r in enumerate(lev):
                if r['F3'] >= 8 and r['open_children'] >= 1:
                    R.append((f"puck596_{tag}_L{li}_{j}", 17, r['M'], list(r['w'])))
    picks = json.load(open(HERE + '/picks.json'))
    for p in (43, 47, 53, 59, 61):
        rows = picks[str(p)]['rows']
        for i, w in enumerate(rows[:8], 1):
            if p in (53, 59, 61) and i == 1: continue  # already in table 1 (seed20261016_p{p})
            R.append((f"seed20261016_p{p}_#{i}", p, p, list(w)))
    for p in (19, 23, 29, 31, 37, 41):
        rows = picks[str(p)]['rows'] if str(p) in picks else json.load(open(f"{HERE}/pick_{p}.json"))['rows']
        for i, w in enumerate(rows[:5], 1):
            kids = open_children(list(w), p)
            rnd = random.Random(20261017 * 1000 + p * 16 + i)
            for j in sorted(rnd.sample(range(len(kids)), min(K_SUB, len(kids)))):
                R.append((f"seed20261016_p{p}_#{i}_c{j}", p, 2 * p, list(kids[j])))
    for L in (16, 8, 4, 2, 1):
        M = L * 17
        a = sorted(x % M for x in W5)
        for j, c in enumerate(open_children(a, M)):
            R.append((f"W5sib_a{L}p_{j}", 17, 2 * M, list(c)))
    return R

def write_roots(R):
    with open(HERE + '/roots_widen.txt', 'w') as f:
        for lab, p, M, w in R:
            f.write(f"{lab} {p} {M} {' '.join(map(str, w))}\n")

def read_roots():
    R = []
    for line in open(HERE + '/roots_widen.txt'):
        a = line.split()
        R.append((a[0], int(a[1]), int(a[2]), [int(x) for x in a[3:]]))
    return R

def _work(keys):
    return [(k, [(k[0], 2 * k[1], c) for c in open_children(list(k[2]), k[1])]) for k in keys]

def init_state():
    R = read_roots()
    old = pickle.load(open('/workspace/work/r45/state.pkl', 'rb'))['children']  # table-1 memo, same function
    st = {'children': dict(old), 'status': {}, 'log': [], 'roots': R, 'cur': None}
    seenroot = set()
    for lab, p, M, w in R:
        if len(w) != 15 or not all(1 <= x <= M - 1 for x in w):
            st['status'][lab] = 'invalid'; st['log'].append(f"ROOT {lab} invalid"); continue
        if not is_open_plain(w, M):
            st['status'][lab] = 'not_open'; st['log'].append(f"ROOT {lab} p={p} M={M} NOT OPEN, skipped"); continue
    return st

def run(st, tlimit, pool):
    t0 = time.time()
    ch = st['children']
    # prefetch: joint level-synchronous memo fill for the next 400 pending roots (only fills the memo; per-root
    # BFS and cap below are unchanged). Stops if a joint level exceeds 200k nodes.
    pend = [(p, M, tuple(sorted(w))) for lab, p, M, w in st['roots'] if lab not in st['status']][:400]
    level = sorted(set(pend))
    while level and len(level) <= 20000:
        need = [k for k in level if k not in ch]
        B = 2000
        for s in range(0, len(need), 2 * B):
            parts = [need[s:s + B], need[s + B:s + 2 * B]]
            for res in pool.map(_work, [x for x in parts if x]):
                for k, v in res: ch[k] = v
            if time.time() - t0 > tlimit: return False
        nxt = set()
        for k in level: nxt.update(ch[k])
        level = sorted(nxt)
    for lab, p, M, w in st['roots']:
        if lab in st['status']: continue
        root = (p, M, tuple(sorted(w)))
        level = [root]; seen = 1
        while level:
            need = [k for k in level if k not in ch]
            if lab.startswith('W5sib') and len(need) > DEFER:
                st['status'][lab] = 'deferred'
                st['log'].append(f"DEFERRED root {lab} p={p} M={M}: compute budget, level {level[0][1] // p}p has "
                                 f"{len(level)} open nodes ({len(need)} unexpanded > {DEFER}); seen so far {seen}; left out")
                break
            B = 400
            for s in range(0, len(need), 2 * B):
                parts = [need[s:s + B], need[s + B:s + 2 * B]]
                for res in pool.map(_work, [x for x in parts if x]):
                    for k, v in res: ch[k] = v
                if time.time() - t0 > tlimit: return False
            nxt = set()
            for k in level: nxt.update(ch[k])
            seen += len(nxt); level = sorted(nxt)
            if seen > CAP_ROOT:
                st['status'][lab] = 'capped'
                st['log'].append(f"CAPPED root {lab} p={p} M={M}: subtree > {CAP_ROOT} nodes "
                                 f"(next frontier {len(level)} at {level[0][1] // p}p); left out")
                break
        if lab not in st['status']: st['status'][lab] = 'done'
    return True

if __name__ == '__main__' and sys.argv[1] == 'roots':
    R = roots_widen(); write_roots(R)
    import collections
    print(len(R), collections.Counter(l.split('_')[0] for l, *_ in R))

if __name__ == '__main__' and sys.argv[1] == 'run':
    import multiprocessing as mp
    st = pickle.load(open(STATE, 'rb')) if os.path.exists(STATE) else init_state()
    with mp.get_context('fork').Pool(2) as pool:
        done = run(st, float(sys.argv[2]), pool)
    tmp = f"{STATE}.{os.getpid()}.tmp"
    with open(tmp, 'wb') as f: pickle.dump(st, f, protocol=4)
    os.replace(tmp, STATE)
    nd = sum(1 for v in st['status'].values() if v == 'done')
    nxt = next((l for l, *_ in st['roots'] if l not in st['status']), None)
    print('DONE' if done else 'PARTIAL', 'memo', len(st['children']), 'roots_done', nd, 'status', len(st['status']),
          '/', len(st['roots']), 'next', nxt, flush=True)
