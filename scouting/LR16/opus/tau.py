"""(speed class 1 fixed in the cover: units act transitively on speed classes)
tau_k(p): smallest number of folded speed classes covering all folded time classes,
where speed v covers time a iff (k+1)*d_p(a*v) < p   (Allikvere eq. (7)).
Exact via MILP (HiGHS). Usage: python3 tau.py k p1 p2 ...
Also reports the LP lower bound and whether tau > k (then J(k,p) is empty at level one).
"""
import sys, time
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csr_matrix

def dp(x, p):
    r = x % p
    return min(r, p - r)

def tau(k, p, tlim=int(__import__("os").environ.get("TLIM", "300"))):
    n = (p - 1) // 2
    rows, cols = [], []
    for a in range(1, n + 1):
        for v in range(1, n + 1):
            if (k + 1) * dp(a * v, p) < p:
                rows.append(a - 1); cols.append(v - 1)
    A = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    c = np.ones(n)
    t0 = time.time()
    res = milp(c, constraints=LinearConstraint(A, lb=1, ub=np.inf), integrality=np.ones(n),
               bounds=Bounds(np.r_[1.0, np.zeros(n-1)], 1), options={"time_limit": tlim, "disp": False})
    dt = time.time() - t0
    m = len(rows) // n
    return (round(res.fun) if res.x is not None else None), res.status, dt, m, n, getattr(res, "mip_dual_bound", None)

if __name__ == "__main__":
    k = int(sys.argv[1])
    for p in map(int, sys.argv[2:]):
        t, st, dt, m, n, lb = tau(k, p)
        print(f"k={k} p={p} n={n} per-speed={m} tau={t} status={st} dual_bound={lb} time={dt:.1f}s", flush=True)
