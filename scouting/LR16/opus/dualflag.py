# Chair exploration (not a proof): how much can the "dual flag" lower the n=15 bound?
# Minimise prod t_i (i=1..14) subject to
#   prefix:  t_1+...+t_r >= B_r                     (Prop 3.4)
#   KZ:      t_{i+1} >= (3/4) t_i                    (Lemma 3.5)
#   dual r=1: t_14 <= 1/3                            (Astra, chair note 5)
#   dual r=2: t_13 * t_14 <= 1/8   (2-dim integer relation lattice, min norm >= 3, reduced Gram det >= 3*3-1)
# The objective is concave in t, so we use many random starts in log-space (numerical, not certified).
import numpy as np, math
from scipy.optimize import minimize
n, d = 15, 14
B = [0] + [(2*r/((n+1)*(n+1-r)))**2 for r in range(1, d+1)]
c = [B[i]-B[i-1] for i in range(1, d+1)]
logK = sum(math.log(x) for x in c)
def solve(dual1, dual2, starts=300, seed=0):
    rng = np.random.default_rng(seed)
    cons = []
    for r in range(1, d+1):
        cons.append({'type':'ineq', 'fun': (lambda s, r=r: np.sum(np.exp(s[:r])) - B[r])})
    for i in range(d-1):
        cons.append({'type':'ineq', 'fun': (lambda s, i=i: s[i+1] - s[i] - math.log(0.75))})
    if dual1: cons.append({'type':'ineq', 'fun': lambda s: math.log(1/3) - s[d-1]})
    if dual2: cons.append({'type':'ineq', 'fun': lambda s: math.log(1/8) - s[d-1] - s[d-2]})
    best = None
    for _ in range(starts):
        s0 = np.log(np.array(c) * rng.uniform(0.8, 3.0, d))
        r = minimize(lambda s: np.sum(s), s0, constraints=cons, method='SLSQP', options={'maxiter':500, 'ftol':1e-12})
        if r.success and all(cn['fun'](r.x) > -1e-9 for cn in cons):
            if best is None or r.fun < best.fun: best = r
    return best
for label, d1, d2 in [("no dual (paper)", False, False), ("dual r=1", True, False), ("dual r=1,2", True, True)]:
    r = solve(d1, d2)
    gain = (n/2)*(r.fun - logK)
    print(f"{label:16s} min sum log t = {r.fun:.6f}  gain vs paper = {gain:.4f} log-units  t13={math.exp(r.x[12]):.4f} t14={math.exp(r.x[13]):.4f}")
r0 = solve(False, False); r1 = solve(True, False)
print("paper (no dual) gain check:", (n/2)*(r0.fun - logK))
gam = {1:1, 2:4/3, 3:2**(1/3), 4:2**0.5, 5:8**(1/5), 6:(64/3)**(1/6), 7:64**(1/7), 8:2}
t = np.exp(r1.x)
print("minimiser with t14<=1/3:", np.round(t, 4))
for rr in range(1, 9):
    suf = float(np.prod(t[d-rr:]))
    cap = (gam[rr]/3)**rr          # Hermite: Gram det of r-dim relation lattice >= (3/gamma_r)^r
    print(f"r={rr}: suffix product {suf:.3e}   Hermite cap 1/det <= {cap:.3e}   binds: {suf > cap}")
