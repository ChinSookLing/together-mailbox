# Chair exploration (numerical, not a proof): where does the n=15 flag bound lose most?
# For each prefix inequality B_r, multiply it by 1.10 (10% stronger) and see how many log-units the
# product bound gains, with Astra's t_14 <= 1/3 kept. Bound gain = (n/2) * (new min sum log t - old).
import numpy as np, math
from scipy.optimize import minimize
import warnings; warnings.filterwarnings("ignore")
n, d = 15, 14
B0 = [0] + [(2*r/((n+1)*(n+1-r)))**2 for r in range(1, d+1)]
def minsumlog(B, t14cap=1/3, starts=150, seed=1):
    rng = np.random.default_rng(seed)
    cons = [{'type':'ineq','fun':(lambda s,r=r: np.sum(np.exp(s[:r])) - B[r])} for r in range(1,d+1)]
    cons += [{'type':'ineq','fun':(lambda s,i=i: s[i+1]-s[i]-math.log(0.75))} for i in range(d-1)]
    if t14cap: cons.append({'type':'ineq','fun':lambda s: math.log(t14cap) - s[d-1]})
    c = [B[i]-B[i-1] for i in range(1,d+1)]
    best = None
    for _ in range(starts):
        s0 = np.log(np.abs(np.array(c)) * rng.uniform(0.8, 3.0, d) + 1e-12)
        r = minimize(np.sum, s0, constraints=cons, method='SLSQP', options={'maxiter':500,'ftol':1e-12})
        if r.success and all(cn['fun'](r.x) > -1e-9 for cn in cons):
            if best is None or r.fun < best: best = r.fun
    return best
base = minsumlog(B0)
print(f"base (with t14<=1/3) min sum log t = {base:.5f}")
for r in range(1, d+1):
    B = B0[:]; B[r] *= 1.10
    g = (n/2)*(minsumlog(B) - base)
    print(f"B_{r:2d} x1.10 -> gain {g:7.3f} log-units")
