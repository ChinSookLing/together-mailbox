# Chair: orbit-by-orbit cross-check of T11 (Fable-A) against sealed T12 (TEST Opus). Read-only on both outputs.
import re
P = 83
fold = [min(x % P, P - x % P) for x in range(P)]
mul = [[fold[(u * v) % P] for v in range(P)] for u in range(P)]
def canon(t): return min(tuple(sorted(mul[u][v] for v in t)) for u in range(1, 42))
# T12 level-one orbits: supports (canonical by log); expand multisets
t12 = set()
for line in open('l3c/level1_p83_orbits.txt'):
    s, cl = line.strip().split(':'); cl = list(map(int, cl.split(',')))
    if int(s) == 13: t12.add(canon(cl))
    else:
        for x in cl: t12.add(canon(cl + [x]))
t11 = {tuple(map(int, l.split())) for l in open('t11/zip/level1_p83.txt')}
print("T12 orbits", len(t12), " T11 orbits", len(t11), " equal sets:", t12 == t11)
# per-orbit fibers
t12f = {}
for line in open('l3c/lift_p83_per_orbit.txt'):
    rep, f = line.strip().split('|'); t12f[canon(tuple(map(int, rep.split())))] = tuple(map(int, f.split()))
diff = 0; n = 0; t11_nonempty = 0
for line in open('t11/zip/cascade_p83.txt'):
    head, rest = line.split(':', 1); key = tuple(map(int, head.split()))
    ls = dict((int(a), int(b)) for a, b in re.findall(r'\bl(\d+)=(\d+)', rest))
    f = tuple(ls.get(L, 0) for L in (2, 4, 8, 16, 32)); n += 1
    if f[0] > 0: t11_nonempty += 1
    mine = t12f.get(key, (0, 0, 0, 0, 0))
    if mine != f: diff += 1
print("cascade rows", n, " orbits with F_2 nonempty (T11)", t11_nonempty, " (T12)", len(t12f), " orbits whose (|F_2|..|F_32|) differ:", diff)
