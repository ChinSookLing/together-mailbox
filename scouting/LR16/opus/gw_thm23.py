# Goddyn-Wong (Integers 6 (2006) #A38) Theorem 2.3: [n-1] with speed r -> m*r is tight
# iff n = 2, or (n,r,m) = (3,1,4), or GCD(r,b) > 1 for every b in {n-r, ..., m(n-r)-1}.
# The b-range grows with m, so m = 2 failing means every m >= 2 fails.
from math import gcd
for n in (14, 16, 20):
    hits = [(r, m) for r in range(1, n) for m in range(2, 40)
            if all(gcd(r, b) > 1 for b in range(n - r, m * (n - r)))]
    print(f"n={n} runners: single-acceleration tight (r,m) = {hits}")
