from sympy import primerange
import math
targets = {"k=14 (paper, check)": 414.779364557 - math.log(360360),
           "k=15 (16 runners)": 496.67 - math.log(720720),
           "k=16 (17 runners)": 587.25 - math.log(12252240)}
for name, T in targets.items():
    print(f"{name}: need sum log p > {T:.4f}")
    for p0 in (89, 101, 131, 151, 199, 239, 307):
        s = 0; cnt = 0
        for p in primerange(p0, 10**5):
            s += math.log(p); cnt += 1
            if s > T:
                print(f"   all primes from {p0}: up to p_max={p} ({cnt} primes)")
                break
# paper's actual P14 sanity
P14 = [89,131,149,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,241] + [p for p in primerange(239,570) if p!=241]
print("paper P14:", len(P14), round(sum(map(math.log,P14)),4))
