# Chair checks (Opus) of GPT turn 18 and Astra turn 17, PT005.
from fractions import Fraction as F
import math
# --- GPT Q4: exact rational test for H > 3515625/3721 (R_15 < 61/125)
a = F(18119, 250000); b = F(72477, 1000000)
q = lambda x: 1 + 2*x - x*x
P = lambda x: 378*x**3 + 25*x**2 + 10*x - 1
print("P(a)<0<P(b):", P(a) < 0 < P(b))
N = (1 + 2*a + 27*a*a) * q(a)**13; T = F(3515625, 3721)
print("N^15 > T^15 b^28:", N**15 > T**15 * b**28)
print("(1875/61)^2 == 3515625/3721:", F(1875,61)**2 == T, " 15/sqrt(T) =", 15/math.sqrt(T), " target 61/125 =", 61/125)
print("Delta B = 15 log(125/122) =", 15*math.log(125/122))
# H1 numerical minimum for comparison
H1 = lambda t: (1+2*t+27*t*t)*(1+2*t-t*t)**13 / t**(28/15)
print("min H1 ~", min(H1(0.0724 + i*1e-7) for i in range(2000)))
# tail products
print("75/784 =", 75/784, " 43/450 =", 43/450, " gain 7.5*log =", 7.5*math.log(F(75,784)/F(43,450)))
# --- Astra Q3: do the 12 classes {1,2,8,11,18,38,40,46,47,48,56,58} cover all 65 time classes at p = 131, k = 15?
p = 131; n = (p-1)//2
def dp(x): x %= p; return min(x, p-x)
S = [1,2,8,11,18,38,40,46,47,48,56,58]
cov = set(t for t in range(1, n+1) for v in S if 16*dp(t*v) < p)
print("12 classes cover", len(cov), "of", n, "time classes")
# --- Astra Q2, D = 8 specialisation: sum g*ceil(D_i/8) for residues mod 8
for r in range(8):
    g = math.gcd(8, r) if r else 8
    if r: print("u ≡", r, "mod 8: g =", g, " contribution", g*math.ceil((8//g)/8))
