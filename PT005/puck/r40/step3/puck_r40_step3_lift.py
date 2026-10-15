# Puck R40 step 3b: sharpen beta-agreement lemma + mod-32 lift structure.
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

def act(k, a, t):
    return tuple(sorted(norm(a * c + 2 * t, a * v) for c, v in k))

def r16_has(k, beta):
    opts = []
    for c, v in k:
        h = (c // 2) % 16
        if h % 2 == beta:
            opts.append([((h - v) % 16, (h + v) % 16)])
        else:
            opts.append([(h, (h + 2 * v) % 16), (h, (h - 2 * v) % 16)])
    for ch in itertools.product(*opts):
        cnt = Counter(x for dom in ch for x in dom)
        if all(cnt[r] == 2 for r in range(16) if r % 2 != beta) and sum(cnt.values()) == 16:
            return True
    return False

def overfill(k, beta):
    f = Counter()
    for c, v in k:
        h = (c // 2) % 16
        if h % 2 == beta:
            f[(h - v) % 16] += 1; f[(h + v) % 16] += 1
        else:
            f[h % 16] += 1
    return max(f.values(), default=0) > 2

seen = {}; orbits = []
for k in MD:
    if k in seen: continue
    O = set(act(k, a, t) for a in range(1, 32, 2) for t in range(16))
    for x in O: seen[x] = len(orbits)
    orbits.append(sorted(O))

Hgens = [(a, t) for a in range(1, 32, 2) for t in range(0, 16, 2)]

print('[1] G-orbits: 128:', sum(1 for O in orbits if len(O)==128),
      '256:', sum(1 for O in orbits if len(O)==256),
      'REAL@128:', sum(1 for O in orbits if len(O)==128 and O[0] in R),
      'REAL@256:', sum(1 for O in orbits if len(O)==256 and O[0] in R))

# Classify: is tau(k) in H·k?
rows = []
for O in orbits:
    k = O[0]
    Horbit = set(act(k, a, t) for a, t in Hgens)
    tauk = act(k, 1, 1)
    tau_in = tauk in Horbit
    rows.append((len(O), len(Horbit), tau_in, r16_has(k,0), r16_has(k,1),
                 overfill(k,0), overfill(k,1), k in R))

print('[2] (Gsize, Hsize, tau_in_H) distribution:',
      Counter((g, h, t) for g, h, t, *_ in rows))
print('[3] among tau_in_H=True: beta agree?', all(r0==r1 for g,h,t,r0,r1,*_ in rows if t))
print('[3] among tau_in_H=False: beta agree?', all(r0==r1 for g,h,t,r0,r1,*_ in rows if not t))
print('[3] tau_in_H=False count', sum(1 for *_,t,r0,r1,ov0,ov1,real in
      [(g,h,t,r0,r1,ov0,ov1,real) for g,h,t,r0,r1,ov0,ov1,real in rows] if not t))

# Fix tuple unpack in print above - redo cleanly
n_in = sum(1 for g,h,t,r0,r1,ov0,ov1,real in rows if t)
n_out = sum(1 for g,h,t,r0,r1,ov0,ov1,real in rows if not t)
agree_in = all(r0==r1 for g,h,t,r0,r1,ov0,ov1,real in rows if t)
agree_out = all(r0==r1 for g,h,t,r0,r1,ov0,ov1,real in rows if not t)
print('[3b] tau_in_H True:', n_in, 'agree', agree_in, '| False:', n_out, 'agree', agree_out)

# Size 256 details
r256 = [row for row in rows if row[0]==256]
print('[4] size256: all fail R16 both?', all(not r0 and not r1 for g,h,t,r0,r1,ov0,ov1,real in r256))
print('[4] size256: all overfill beta0?', all(ov0 for g,h,t,r0,r1,ov0,ov1,real in r256))
print('[4] size256: all overfill BOTH?', all(ov0 and ov1 for g,h,t,r0,r1,ov0,ov1,real in r256))
print('[4] size256: tau_in_H?', Counter(t for g,h,t,*_ in r256))
print('[4] size128: tau_in_H?', Counter(t for g,h,t,*_ in rows if g==128))

# H-orbit sizes on size128
print('[4] size128 H-orbit sizes', Counter(h for g,h,*_ in rows if g==128))
print('[4] size256 H-orbit sizes', Counter(h for g,h,*_ in rows if g==256))

# ---------- Proof check: on every orbit where tau_in_H, agreement is identity ----------
# Already: if tau_in_H then R16(k,0)=R16(tau k,0)=R16(k,1).
# Verify the chain numerically once more for all MD points in such orbits
bad = 0
for O in orbits:
    k = O[0]
    Horbit = set(act(k, a, t) for a, t in Hgens)
    if act(k, 1, 1) not in Horbit:
        continue
    # find h with h·k = tau k
    for a, t in Hgens:
        if act(k, a, t) == act(k, 1, 1):
            # R16(k,0) should equal R16(k,1)
            if r16_has(k, 0) != r16_has(k, 1):
                bad += 1
            break
print('[5] forced-agreement orbits: mismatches', bad)

# For split orbits (tau not in H): show both R16 false via overfill at beta0
split_rows = [row for row in rows if not row[2]]
print('[6] split orbits', len(split_rows),
      'R16_0 false', sum(1 for g,h,t,r0,r1,ov0,ov1,real in split_rows if not r0),
      'overfill0', sum(1 for g,h,t,r0,r1,ov0,ov1,real in split_rows if ov0),
      'REAL', sum(1 for g,h,t,r0,r1,ov0,ov1,real in split_rows if real))

# ---------- Lift analysis ----------
def dominos32(c, v, beta):
    h = (c // 2) % 16
    out = []
    for x in (h, h + 16):
        if x % 2 == beta:
            out.append(('A', tuple(sorted([((x - v) % 32), ((x + v) % 32)]))))
        else:
            for e in (1, -1):
                out.append(('B', tuple(sorted([x % 32, (x + 2 * e * v) % 32]))))
    return out

def sheet(s):
    return 0 if (s % 32) < 16 else 1

def has_same_sheet_lift(c, v, beta, dm16):
    target = tuple(sorted(dm16))
    for kind, dm in dominos32(c, v, beta):
        if tuple(sorted(x % 16 for x in dm)) != target:
            continue
        a, b = dm
        if sheet(a) == sheet(b):
            return True
    return False

def r16_choices(k, beta):
    opts = []
    for c, v in k:
        h = (c // 2) % 16
        if h % 2 == beta:
            opts.append([((h - v) % 16, (h + v) % 16)])
        else:
            opts.append([(h, (h + 2 * v) % 16), (h, (h - 2 * v) % 16)])
    out = []
    for ch in itertools.product(*opts):
        cnt = Counter(x for d in ch for x in d)
        if all(cnt[r] == 2 for r in range(16) if r % 2 != beta) and sum(cnt.values()) == 16:
            out.append(ch)
    return out

# Case A/B sheet capability census on all footprints of R16 configs
A_same = A_cross = B_same = B_cross = 0
for k in MD:
    if not r16_has(k, 0):
        continue
    for beta in (0, 1):
        for c, v in k:
            h = (c // 2) % 16
            for kind, dm in dominos32(c, v, beta):
                a, b = dm
                same = sheet(a) == sheet(b)
                if kind == 'A':
                    A_same += same; A_cross += (not same)
                else:
                    B_same += same; B_cross += (not same)
print('[7] among R16 configs, all A/B mod32 options: A same/cross', A_same, A_cross, 'B same/cross', B_same, B_cross)

# Every Case A option is same-sheet? (A_cross should be 0)
# Every Case B?

# For each R16 choice, check universal same-sheet availability
def choice_all_same_sheet(k, beta, ch):
    return all(has_same_sheet_lift(c, v, beta, ch[i]) for i, (c, v) in enumerate(k))

n_configs_with_ss = [0, 0]
n_choices = [0, 0]
n_choices_ss = [0, 0]
for k in MD:
    if not r16_has(k, 0):
        continue
    for beta in (0, 1):
        chs = r16_choices(k, beta)
        n_choices[beta] += len(chs)
        ss = [ch for ch in chs if choice_all_same_sheet(k, beta, ch)]
        n_choices_ss[beta] += len(ss)
        if ss:
            n_configs_with_ss[beta] += 1
print('[8] beta0: configs with same-sheet R16 choice', n_configs_with_ss[0], '/640; choices ss/all', n_choices_ss[0], '/', n_choices[0])
print('[8] beta1: configs with same-sheet R16 choice', n_configs_with_ss[1], '/640; choices ss/all', n_choices_ss[1], '/', n_choices[1])

# Constructive lift from same-sheet choice via 2-edge-coloring
def lift_by_edge_coloring(k, beta, ch):
    """Proper 2-edge-color the 2-regular graph; each color-sigma edge uses same-sheet-sigma lift.
    Return True if exact cover obtained."""
    # build edge list with footprint indices
    edges = []  # (u, v, fp_index) with u<v in mod16
    adj = defaultdict(list)
    for i, dm in enumerate(ch):
        a, b = sorted(dm)
        edges.append((a, b, i))
        adj[a].append((b, i))
        adj[b].append((a, i))
    # 2-edge-color each cycle
    edge_color = {}
    residues = [r for r in range(16) if r % 2 != beta]
    seen_e = set()
    for start in residues:
        # find an unused edge at start
        unused = [item for item in adj[start] if item[1] not in edge_color]
        if not unused:
            continue
        # walk the cycle
        prev = None
        cur = start
        color = 0
        while True:
            nbrs = adj[cur]
            # pick edge not equal to previous edge index
            cand = None
            for nb, ei in nbrs:
                if ei in edge_color:
                    continue
                if prev is not None and ei == prev:
                    continue
                cand = (nb, ei)
                break
            if cand is None:
                break
            nb, ei = cand
            edge_color[ei] = color
            prev = ei
            cur = nb
            color ^= 1
            if cur == start:
                break
    if len(edge_color) != 8:
        return False  # failed to color all
    # Now for each edge, pick same-sheet lift with sheet = color
    chosen = []
    for i, dm16 in enumerate(ch):
        sigma = edge_color[i]
        c, v = k[i]
        target = tuple(sorted(dm16))
        found = None
        for kind, dm in dominos32(c, v, beta):
            if tuple(sorted(x % 16 for x in dm)) != target:
                continue
            a, b = dm
            if sheet(a) == sheet(b) == sigma:
                found = dm
                break
        if found is None:
            return False
        chosen.append(found)
    # verify partition
    cnt = Counter(x for dm in chosen for x in dm)
    tgt = [s for s in range(32) if s % 2 != beta]
    return all(cnt[s] == 1 for s in tgt) and sum(cnt[s] for s in tgt) == 16

# Test constructive lift on all R16 configs
ok_construct = [0, 0]
fail_construct = [0, 0]
for k in MD:
    if not r16_has(k, 0):
        continue
    for beta in (0, 1):
        chs = r16_choices(k, beta)
        ss = [ch for ch in chs if choice_all_same_sheet(k, beta, ch)]
        if not ss:
            fail_construct[beta] += 1
            continue
        # try first same-sheet choice
        if lift_by_edge_coloring(k, beta, ss[0]):
            ok_construct[beta] += 1
        else:
            # try all ss choices
            if any(lift_by_edge_coloring(k, beta, ch) for ch in ss):
                ok_construct[beta] += 1
            else:
                fail_construct[beta] += 1
print('[9] constructive 2-edge-color lift: beta0 ok/fail', ok_construct[0], fail_construct[0],
      '| beta1 ok/fail', ok_construct[1], fail_construct[1])

# Also verify: whenever choice_all_same_sheet, the coloring lift works
color_ok = color_fail = 0
for k in MD:
    if not r16_has(k, 0):
        continue
    for beta in (0, 1):
        for ch in r16_choices(k, beta):
            if not choice_all_same_sheet(k, beta, ch):
                continue
            if lift_by_edge_coloring(k, beta, ch):
                color_ok += 1
            else:
                color_fail += 1
print('[10] all same-sheet R16 choices: coloring-lift ok', color_ok, 'fail', color_fail)

print('[done]')
