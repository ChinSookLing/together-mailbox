Hesper local checks, Round 11 (p ≤ 499 only; nothing at 503–599)
Scripts: r4search.py (R_4 via U_4(S)=(1/2)Σ_t Π_v B_4(vt), B_4 = Fourier series of B cut at |k|≤4), r4run.py (simulated annealing, 40 restarts × 60000 steps per prime; speeds in 1..(p−1)/2).

FACT (reproduces chair): 457 cover R_4 = −18.950705; 337 cover R_4 = −12.967999.

Q2 best R_4 found (all 40 restarts converge to the same value at every prime):
p   M(p)    best R_4   ratio   U(best set)  set
307 22.912  −15.792    0.69    4   [2,35,39,47,62,84,86,88,90,96,125,129,133,137]
337 24.926  −17.245    0.69    5   [1,21,22,32,54,65,87,98,109,120,131,151,152,164]
383 30.629  −19.430    0.63    7   [1,12,25,38,49,62,99,110,111,123,148,149,160,173]
431 34.328  −21.907    0.64    11  [3,22,53,72,75,78,100,103,128,147,153,172,184,203]
457 35.392  −23.297    0.66    6   [1,55,56,57,58,60,61,115,169,170,172,173,175,176]
461 36.324  −23.456    0.65    8   [1,86,90,91,92,94,96,98,177,181,183,186,187,189]
499 37.711  −25.489    0.68    7   [1,28,29,30,57,59,88,117,146,175,205,206,233,237]
→ FACT: best R_4 ≈ −(0.63–0.69)·M(p) at every prime, γ=15 primes and cover primes alike. At 457 the best R_4 set is NOT the cover (cover −18.95 is far from best −23.30). R_4 alone does not separate cover from no-cover primes.

Q4 FACT (PROOF, one line): R_K as defined is EXACTLY scaling-invariant: U_K(uS) = (1/2)Σ_t Π_v B_K(u v t) = U_K(S) by t → u⁻¹t (B_K is a function on Z/p, even). Numerically all 228 scalings of the 457 cover give R_4 = −18.950705 (spread 4e−15). The packet premise "R_K is not scaling-invariant" is false for this definition (it would hold only if K were applied to representatives in a fixed window, e.g. relation coefficients after reducing speeds).
