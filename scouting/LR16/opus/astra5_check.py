# Chair (non-author) check of Astra answer 5 (PT005 line 16): t_14 < 1/3 and the modified flag constants, n = 15.
from fractions import Fraction as Fr
import math, itertools
n = 15; d = n - 1
B = [Fr(0)] + [Fr(2*r, (n+1)*(n+1-r))**2 for r in range(1, d+1)]
print("B_12, B_13, B_14 =", B[12], B[13], B[14])
print("B_14 - 1/3 =", B[14] - Fr(1,3), " (Astra: 83/192)", B[14] - Fr(1,3) == Fr(83,192))
Bp = B[:]; Bp[13] = Fr(391, 960)
print("B'_13 = 391/960 =", float(Bp[13]), " < 83/192:", Bp[13] < Fr(83,192), " >= B_13:", Bp[13] >= B[13])
c  = [B[i]-B[i-1] for i in range(1, d+1)]
cp = [Bp[i]-Bp[i-1] for i in range(1, d+1)]
print("c_13, c_14 =", c[12], c[13], "; c'_13, c'_14 =", cp[12], cp[13])
rat = [cp[i+1]/cp[i] for i in range(d-1)]
print("all c'_{i+1}/c'_i > 4/3:", all(r > Fr(4,3) for r in rat), " min ratio =", min(rat))
K  = math.prod(c); Kp = math.prod(cp)
print("K'/K =", Kp/K, " (Astra 6192/4675):", Kp/K == Fr(6192,4675))
print("gain (n/2) ln(K'/K) =", n/2*math.log(Kp/K))
# best split of B_14 - B_12 between c13, c14 under the ratio rule (limit), for comparison
tot = B[14]-B[12]; x = tot/(1+Fr(4,3)); print("limit c13 =", x, "B13 limit =", B[12]+x, float(B[12]+x), " limit gain =", n/2*math.log((x*(tot-x))/(c[12]*c[13])))
# Sigma a_i^2 >= 3 for nonzero integer a with a.v = 0, v distinct positive: brute force tiny check
import random
for trial in range(3):
    v = random.sample(range(1, 40), 6)
    m = min(sum(x*x for x in a) for a in itertools.product(range(-2,3), repeat=6) if any(a) and sum(ai*vi for ai,vi in zip(a,v))==0)
    print("v =", v, " min sum a^2 over relations (entries in -2..2) =", m)
# Numeric check of the identity used in step 1: for ANY basis of Lambda, 1/t_d = sum q_i a_i^2,
# with a the integer relation (a.v = 0) that represents the last E-dual basis vector.
import numpy as np
rng = np.random.default_rng(5)
for trial in range(3):
    v = np.array(sorted(rng.choice(np.arange(2, 60), 14, replace=False)).__add__([1]) if False else list(rng.choice(np.arange(2, 60), 14, replace=False)) + [1], dtype=float)
    nn = len(v); u = v / v.max(); q = 1 + 2*u - u*u
    Uf, _, _ = np.linalg.svd(np.eye(nn) - np.outer(v, v)/v.dot(v)); U = Uf[:, :nn-1]      # orthonormal basis of v-perp
    Bm = U.T[:, :nn-1]                       # columns: P e_1..P e_{n-1}, a basis of Lambda because v_n = 1
    Uni = np.linalg.qr(rng.integers(-2, 3, (nn-1, nn-1)) + 5*np.eye(nn-1))[0]  # not used; keep basis simple
    M = np.linalg.inv(U.T @ np.diag(q) @ U)  # ||y||_E^2 = y^T M y
    G = Bm.T @ M @ Bm                        # E-Gram matrix of the basis
    L = np.linalg.cholesky(G); t = np.diag(L)**2   # Gram-Schmidt squared lengths t_1..t_d
    dual = Bm @ np.linalg.inv(G)             # E-dual basis (columns)
    a = U @ (M @ dual[:, -1])                # Euclidean functional of the last dual vector, as a vector in R^n
    print("1/t_d =", 1/t[-1], " sum q a^2 =", float(np.sum(q*a*a)), " a integer:", np.allclose(a, np.round(a), atol=1e-6), " a.v =", round(float(a @ v), 9))
