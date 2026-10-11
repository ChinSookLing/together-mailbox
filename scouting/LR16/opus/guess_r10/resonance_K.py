# Frequency-truncated resonance R_K(S) = U_K(S) - M(p), where U_K uses the Fourier series of B
# truncated at |k| <= K (all relation lengths kept). K = (p-1)/2 gives the exact U(S) - M(p).
import math, random, sys
def RK(p, S, K):
    H = (p-1)//16
    bh = lambda k: 1-(2*H+1)/p if k == 0 else -math.sin(math.pi*(2*H+1)*k/p)/math.sin(math.pi*k/p)/p
    BK = [sum(bh(k)*math.cos(2*math.pi*k*x/p) for k in range(-K, K+1)) for x in range(p)]
    return 0.5*sum(math.prod(BK[v*t % p] for v in S) for t in range(p)) - p/2*bh(0)**len(S)
if __name__ == "__main__":
    p = 457; cover = [1,2,55,60,68,111,112,113,114,115,116,117,169,221]
    for K in (4, 8, 16, 64, 228): print(p, K, round(RK(p, cover, K), 2))
