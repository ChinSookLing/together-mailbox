# TEST (Opus) · compare our per-orbit level-2 fibers with the archive's p = 83 survivor rows (data only, no author code).
import glob, re
P = 83
fold = [min(x % P, P - x % P) for x in range(P)]
mul = [[fold[(u * v) % P] for v in range(P)] for u in range(P)]
def canon(t):
    return min(tuple(sorted(mul[u][v] for v in t)) for u in range(1, 42))
ours = {}
for line in open('lift_p83_per_orbit.txt'):
    rep, f = line.strip().split('|'); f = list(map(int, f.split()))
    ours[canon(tuple(map(int, rep.split())))] = f
arch = {}; rows = 0; conflict = 0
for fn in sorted(glob.glob('/home/claude/pt004/archive/fourteen_lonely_runners/small_gates/p83/filt/*.out')):
    for line in open(fn):
        m = re.match(r'SURVIVOR base: ([\d ]+) l2=(\d+) tight=\w+ l4=(\d+)', line)
        if not m: continue
        rows += 1
        c = canon(tuple(map(int, m.group(1).split())))
        v = (int(m.group(2)), int(m.group(3)))
        if c in arch and arch[c] != v: conflict += 1
        arch[c] = v
print("our orbits with |F_2|>0:", len(ours))
print("archive survivor rows:", rows, "-> distinct orbits:", len(arch), " rows of one orbit disagreeing on (l2,l4):", conflict)
only_ours = set(ours) - set(arch); only_arch = set(arch) - set(ours)
print("orbits only in ours:", len(only_ours), " only in archive:", len(only_arch))
mism = [c for c in set(ours) & set(arch) if (ours[c][0], ours[c][1]) != arch[c]]
print("common orbits:", len(set(ours) & set(arch)), " with different (|F_2|,|F_4|):", len(mism))
for c in mism[:5]: print("  e.g.", c, "ours", ours[c][:2], "archive", arch[c])
print("sum |F_2| ours:", sum(f[0] for f in ours.values()), " archive (per orbit):", sum(v[0] for v in arch.values()))
print("sum |F_4| ours:", sum(f[1] for f in ours.values()), " archive (per orbit):", sum(v[1] for v in arch.values()))
