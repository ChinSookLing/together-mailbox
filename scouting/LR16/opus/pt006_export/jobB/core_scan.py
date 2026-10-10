# For each of the 19 Round-5 covers, list EVERY scaling u (1 <= u <= (p-1)/2)
# under which at least 5 speeds become <= 15 (taking min(x, p-x)).
import collections
src = open(__file__.replace('core_scan.py','small_core.py')).read().split('"""')[1]
c = collections.Counter(); rows = 0
for line in src.splitlines():
    p, s = line.split(':'); p = int(p); S = list(map(int, s.split()))
    g = lambda x: min(x % p, p - x % p)
    for u in range(1, (p + 1) // 2):
        T = sorted(g(u * v) for v in S)
        small = [x for x in T if x <= 15]
        if len(small) >= 5:
            rows += 1; c.update(small)
            print(f"{p} u={u:3d} small={len(small)} {T}")
print("scalings:", rows)
print("counts:", sorted(c.items()))
