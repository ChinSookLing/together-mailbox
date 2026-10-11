import json
import numpy as np
best = {}
for f in ['d_out.jsonl', 'd_out2.jsonl']:
    for l in open(f):
        r = json.loads(l)
        if r['p'] not in best or r['bestU'] < best[r['p']]['bestU']:
            best[r['p']] = r
rows = sorted(best.values(), key=lambda r: r['p'])
P = np.array([r['p'] for r in rows], float)
D = np.array([r['bestU'] for r in rows], float)
S = np.array([r['s'] for r in rows], float)
a = np.polyfit(P, D, 1)
A = np.column_stack([np.ones_like(P), P, S])
c = np.linalg.lstsq(A, D, rcond=None)[0]
o = open('hesper-r12-findings.md', 'w')
o.write("# Hesper R12 independent D(p) search (dsearch.py, swap-annealing)\n")
o.write("Pass 1: 60 restarts x 6000 steps; pass 2: 250 x 8000 on 11 primes (no improvement). All sets re-verified by direct count. No code at 503-599. Upper bounds; where census says no 14-cover and U=1 found, D=1 exactly.\n\n")
o.write("| p | s | M(p) | best U | set |\n|---|---|---|---|---|\n")
for r in rows:
    o.write(f"| {r['p']} | {r['s']} | {r['M']} | {r['bestU']} | {r['set']} |\n")
o.write(f"\nLinear fit (23 primes): D = {a[0]:.5f} p {a[1]:+.3f}; with slack: {c[0]:.3f} + {c[1]:.5f} p + {c[2]:.3f} s\n")
o.close()
print(a, c)
print([(r['p'], r['bestU']) for r in rows])
