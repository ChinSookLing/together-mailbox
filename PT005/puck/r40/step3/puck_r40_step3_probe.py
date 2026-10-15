# Puck R40 step 3 probe: why beta=0 and beta=1 agree on R16; why R16 lifts to mod-32.
# Own code. Inputs: the two committed tables only.
import json, os, itertools
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../..'))
B = os.path.join(ROOT, 'hesper/r38/checks/')

def norm(c, v):
    c %= 32; v %= 32
    return (c, v) if v < 16 else (c, 32 - v)

Dall = set(tuple(sorted(norm(*f) for f in k)) for k in json.load(open(B + 'r38_doublable_only.json')))
R = set(tuple(sorted(norm(*f) for f in k)) for k in json.load(open(B + 'hesper_U_769.json')))
mixed = lambda k: not (all(v % 8 in (1, 7) for c, v in k) or all(v % 8 in (3, 5) for c, v in k))
MD = sorted(k for k in Dall if mixed(k))
NEVER = [k for k in MD if k not in R]
print('[data] mixed', len(MD), 'REAL', len(R), 'NEVER', len(NEVER))

def dominos(c, v, beta, mod):
    h = (c // 2) % 16
    out = set()
    for x in (h, h + 16):
        if x % 2 == beta:
            out.add(frozenset({(x - v) % mod, (x + v) % mod}))
        else:
            for e in (1, -1):
                out.add(frozenset({x % mod, (x + 2 * e * v) % mod}))
    return [tuple(sorted(o)) for o in out]

def cover(k, beta, mod, mult):
    tgt = [s for s in range(mod) if s % 2 != beta]
    opts = [dominos(c, v, beta, mod) for c, v in k]
    cnt = Counter()
    def rec(i):
        if i == 8:
            return all(cnt[s] == mult for s in tgt)
        for dm in opts[i]:
            if any(cnt[s] + dm.count(s) > mult for s in set(dm)):
                continue
            for s in dm:
                cnt[s] += 1
            if rec(i + 1):
                return True
            for s in dm:
                cnt[s] -= 1
        return False
    return rec(0)

def r16_opts(k, beta):
    """Return list of option-lists for R16 (mod 16, mult 2): each footprint -> list of 2-tuples."""
    opts = []
    for c, v in k:
        h = (c // 2) % 16
        if h % 2 == beta:
            opts.append([((h - v) % 16, (h + v) % 16)])
        else:
            opts.append([(h, (h + 2 * v) % 16), (h, (h - 2 * v) % 16)])
    return opts

def r16_has(k, beta):
    opts = r16_opts(k, beta)
    for ch in itertools.product(*opts):
        cnt = Counter(x for dom in ch for x in dom)
        if all(cnt[r] == 2 for r in range(16) if r % 2 != beta) and sum(cnt.values()) == 16:
            return True
    return False

# ---------- [A] Affine translation intertwines betas ----------
def act(k, a, t):
    return tuple(sorted(norm(a * c + 2 * t, a * v) for c, v in k))

def check_intertwine(sample_n=200):
    """R16(phi_t(k), beta) == R16(k, beta + t mod 2) for odd/even t."""
    bad = 0
    tot = 0
    # all REAL + a chunk of NEVER
    sample = list(R) + NEVER[: max(0, sample_n - len(R))]
    for k in sample:
        for t in range(16):
            kp = act(k, 1, t)
            for beta in (0, 1):
                tot += 1
                left = r16_has(kp, beta)
                right = r16_has(k, (beta + t) % 2)  # since h -> h+t, Case A when (h+t)%2==beta i.e. h%2==beta-t
                # Wait: Case A for kp at beta: (h+t)%2==beta <=> h%2 == (beta-t)%2 = (beta+t)%2 since t int
                # Actually (beta - t) mod 2 = (beta + t) mod 2. Yes.
                # Dominos shift by +t: cover of parity != beta for kp
                # <=> cover of parity != beta, shifted, of original residues of parity != (beta-t)
                # slots for (k, beta-t): parity != beta-t.
                # After +t: parity != beta-t + t = != beta. Good.
                # So R16(kp, beta) <=> R16(k, (beta-t)%2) = R16(k, (beta+t)%2)
                if left != right:
                    bad += 1
                    if bad <= 3:
                        print('  FAIL intertwine', 't', t, 'beta', beta, 'left', left, 'right', right, 'k0', k[:2])
    return tot, bad

tot, bad = check_intertwine()
print('[A] intertwine R16(act(k,1,t),beta)==R16(k,beta+t mod 2): cases', tot, 'mismatches', bad)

# ---------- [B] H-invariance (even t, odd a) of each beta separately ----------
def check_H_invariance(sample_n=100):
    bad = 0
    tot = 0
    sample = list(R) + NEVER[: max(0, sample_n - len(R))]
    for k in sample:
        for a in range(1, 32, 2):
            for t in range(0, 16, 2):  # even t only
                kp = act(k, a, t)
                for beta in (0, 1):
                    tot += 1
                    if r16_has(k, beta) != r16_has(kp, beta):
                        bad += 1
                        if bad <= 3:
                            print('  FAIL H', a, t, beta)
    return tot, bad

tot, bad = check_H_invariance()
print('[B] H-invariance (odd a, even t) of R16(.,beta): cases', tot, 'mismatches', bad)

# ---------- [C] Orbit swap: within each orbit, R16(.,0) values equal R16(.,1) of preimages ----------
# Stronger structural check: for every k, R16(k,0)==R16(k,1)
# Already known; reconfirm with own r16_has
agree = sum(1 for k in MD if r16_has(k, 0) == r16_has(k, 1))
print('[C] R16(k,0)==R16(k,1) on all MD:', agree, '/', len(MD),
      '| R16 set size beta0', sum(r16_has(k, 0) for k in MD),
      'beta1', sum(r16_has(k, 1) for k in MD))

# ---------- [D] Proof sketch test: {k: R16(k,0)} is closed under odd translation? ----------
# Equivalent to set equality. Check directly that tau=act(.,1,1) preserves the R16(.,0) set
# (which is true iff beta agreement).
# Instead: show a DIRECT involution on covers for fixed k relating beta 0 and 1.
# Candidate: residue map r |-> r+8 mod 16 (preserves parity!). Not swapping betas.
# Candidate for swapping: need something else on the SAME k.
# Try: flip all footprints' h parity via c |-> c+16? But c+16: h = c/2, (c+16)/2 = h+8.
# h+8 has SAME parity as h! So Case A/B unchanged. Dominos: {h+8±v} etc — shift by 8, parity preserved.
def shift8(k):
    return tuple(sorted(norm(c + 16, v) for c, v in k))

# c+16 changes c by 16, h by 8. R16 same beta should be equivalent via +8 on residues.
bad8 = sum(1 for k in list(R)[:50] + NEVER[:50] for beta in (0, 1)
           if r16_has(k, beta) != r16_has(shift8(k), beta))
print('[D] shift c+=16 (h+=8) preserves R16(.,beta): mismatches on 100 configs x 2:', bad8)

# ---------- [E] Direct reason attempt: count Case-A parity signature ----------
# For each config, nA(beta) = #{h even} if beta=0 else #{h odd}
def nA(k, beta):
    return sum(1 for c, v in k if ((c // 2) % 16) % 2 == beta)

# Among REAL, distribution of nA
dist = Counter(nA(k, 0) for k in R)
print('[E] nA(beta=0) among REAL:', dict(sorted(dist.items())))
distN = Counter(nA(k, 0) for k in NEVER)
print('[E] nA(beta=0) among NEVER:', dict(sorted(distN.items())))

# ---------- [F] Lift structure: for R16 configs, count mod-32 covers per beta ----------
def count_covers(k, beta, mod, mult, limit=5000):
    tgt = [s for s in range(mod) if s % 2 != beta]
    opts = [dominos(c, v, beta, mod) for c, v in k]
    cnt = Counter()
    found = [0]
    def rec(i):
        if found[0] >= limit:
            return
        if i == 8:
            if all(cnt[s] == mult for s in tgt):
                found[0] += 1
            return
        for dm in opts[i]:
            if any(cnt[s] + dm.count(s) > mult for s in set(dm)):
                continue
            for s in dm:
                cnt[s] += 1
            rec(i + 1)
            for s in dm:
                cnt[s] -= 1
    rec(0)
    return found[0]

# Sample REAL: how many mod32 covers? how many R16 choice tuples?
def count_r16_choices(k, beta, limit=5000):
    opts = r16_opts(k, beta)
    found = 0
    for ch in itertools.product(*opts):
        cnt = Counter(x for dom in ch for x in dom)
        if all(cnt[r] == 2 for r in range(16) if r % 2 != beta) and sum(cnt.values()) == 16:
            found += 1
            if found >= limit:
                break
    return found

print('[F] per-REAL-rep (one per orbit) R16-choice counts and mod32-cover counts:')
# get orbit reps of REAL
seen = {}
orbits = []
for k in MD:
    if k in seen:
        continue
    O = set(act(k, a, t) for a in range(1, 32, 2) for t in range(16))
    for x in O:
        seen[x] = len(orbits)
    orbits.append(sorted(O))

real_orbs = [O for O in orbits if O[0] in R]
print('   REAL orbits', len(real_orbs))
for O in real_orbs:
    k = O[0]
    r0 = count_r16_choices(k, 0)
    r1 = count_r16_choices(k, 1)
    m0 = count_covers(k, 0, 32, 1)
    m1 = count_covers(k, 1, 32, 1)
    print('   nA0', nA(k, 0), 'R16ch', (r0, r1), 'mod32', (m0, m1), 'rep', k)

# ---------- [G] Does every R16 choice lift? Or only some? ----------
# For each R16 solution (choice of eps for Case B), does there exist a mod32 lift?
# Build: given a mod16 choice, try to find mod32 dominos projecting to it.

def projects_to(dm32, dm16):
    return tuple(sorted(x % 16 for x in dm32)) == tuple(sorted(dm16))

def lifts_of_choice(k, beta, choice16):
    """choice16: list of 8 pairs (the chosen dominos mod 16). Return True if some mod32 cover projects to it."""
    # For each footprint i, filter mod32 dominos that project to choice16[i]
    opts32 = []
    for i, (c, v) in enumerate(k):
        dms = dominos(c, v, beta, 32)
        good = [dm for dm in dms if projects_to(dm, choice16[i])]
        if not good:
            return False
        opts32.append(good)
    cnt = Counter()
    tgt = [s for s in range(32) if s % 2 != beta]
    def rec(i):
        if i == 8:
            return all(cnt[s] == 1 for s in tgt)
        for dm in opts32[i]:
            if any(cnt[s] + dm.count(s) > 1 for s in set(dm)):
                continue
            for s in dm:
                cnt[s] += 1
            if rec(i + 1):
                return True
            for s in dm:
                cnt[s] -= 1
        return False
    return rec(0)

def all_r16_choices(k, beta):
    opts = r16_opts(k, beta)
    out = []
    for ch in itertools.product(*opts):
        cnt = Counter(x for dom in ch for x in dom)
        if all(cnt[r] == 2 for r in range(16) if r % 2 != beta) and sum(cnt.values()) == 16:
            out.append(ch)
    return out

print('[G] for each REAL orbit rep: fraction of R16 choices that lift to mod32:')
for O in real_orbs:
    k = O[0]
    for beta in (0, 1):
        chs = all_r16_choices(k, beta)
        lift_ok = sum(1 for ch in chs if lifts_of_choice(k, beta, ch))
        print('   beta', beta, 'choices', len(chs), 'lift', lift_ok, 'nA', nA(k, beta))

# ---------- [H] NEVER with R16 false: confirm none lift; and R16 true => lift on ALL MD ----------
# Reconfirm R16=>mod32 on all MD with own cover()
S0 = {k: r16_has(k, 0) for k in MD}
F0 = {}
# Only compute mod32 for R16-true (640) + a sample of false to save time
r16_true = [k for k in MD if S0[k]]
r16_false_sample = [k for k in MD if not S0[k]][:200]
print('[H] R16-true count', len(r16_true))
lift_fail = 0
for k in r16_true:
    if not cover(k, 0, 32, 1):
        lift_fail += 1
    if not cover(k, 1, 32, 1):
        lift_fail += 1
print('[H] among R16-true: mod32 cover fails (both betas checked):', lift_fail, 'of', 2 * len(r16_true))

# sample false: should not have mod32 either (from step2)
false_has32 = sum(1 for k in r16_false_sample if cover(k, 0, 32, 1) or cover(k, 1, 32, 1))
print('[H] among 200 R16-false sample: any mod32 cover:', false_has32)

# ---------- [I] Cycle-type of R16 multigraph for REAL ----------
def r16_graph_cycle_types(k, beta):
    """For each R16 choice, return sorted cycle lengths of the 2-regular multigraph on 8 residues."""
    types = []
    for ch in all_r16_choices(k, beta):
        # build adjacency multiset
        adj = defaultdict(list)
        residues = [r for r in range(16) if r % 2 != beta]
        for a, b in ch:
            adj[a].append(b)
            adj[b].append(a)
        seen_v = set()
        cycles = []
        for start in residues:
            if start in seen_v:
                continue
            # walk
            length = 0
            prev = None
            cur = start
            while cur not in seen_v:
                seen_v.add(cur)
                length += 1
                nbrs = adj[cur]
                # pick next != prev
                nxt = nbrs[0] if nbrs[0] != prev or len(nbrs) == 1 else nbrs[1]
                # handle double edge to same neighbor
                if nbrs[0] == nbrs[1]:
                    nxt = nbrs[0]
                prev, cur = cur, nxt
            cycles.append(length)
        types.append(tuple(sorted(cycles)))
    return Counter(types)

print('[I] R16 multigraph cycle types on REAL orbit reps (beta=0):')
for O in real_orbs:
    k = O[0]
    ct = r16_graph_cycle_types(k, 0)
    print('   nA', nA(k, 0), dict(ct), 'rep', k[:4], '...')

# ---------- [J] Key lemma probe: sheet-parity / lift obstruction ----------
# Classify each chosen mod16 domino as Case A (unique option) or Case B (two eps).
# For lift: Case A edges are "parallel-sheet" (both ends same sheet in the natural lifts).
# Check: for every lifting R16 choice, the Case-A / Case-B pattern allows a consistent sheet assignment.

def sheet_sign_obstruction_stats(k, beta):
    """Among R16 choices, how many have all-even cycle support for Case-A-only subgraph? exploratory."""
    opts = r16_opts(k, beta)
    # tag each footprint as A or B
    tags = []
    for c, v in k:
        h = (c // 2) % 16
        tags.append('A' if h % 2 == beta else 'B')
    n_lift = 0
    n_cho = 0
    for ch in itertools.product(*opts):
        cnt = Counter(x for dom in ch for x in dom)
        if not (all(cnt[r] == 2 for r in range(16) if r % 2 != beta) and sum(cnt.values()) == 16):
            continue
        n_cho += 1
        if lifts_of_choice(k, beta, ch):
            n_lift += 1
    return n_cho, n_lift, tags.count('A'), tags.count('B')

print('[J] lift fractions with A/B counts:')
for O in real_orbs:
    k = O[0]
    for beta in (0, 1):
        n_cho, n_lift, nA_, nB_ = sheet_sign_obstruction_stats(k, beta)
        print('   beta', beta, 'A', nA_, 'B', nB_, 'cho', n_cho, 'lift', n_lift)

print('[done]')
