from fractions import Fraction as F
M=424;N=2*M
child=[432,10,16,448,480,164,608,656,235,267,704,320,336,384,816]
def near(T,w): r=(T*w)%N; return 16*min(r,N-r)<N
unc=[T for T in range(1,N) if not any(near(T,w) for w in child)]
print('uncovered T in 1..N-1 (integer test):',unc[:10],len(unc))
# exact Fraction test of ||T*w/N|| < 1/16
unc2=[T for T in range(1,N) if not any(min(F(T*w,N)%1,1-F(T*w,N)%1)<F(1,16) for w in child)]
print('uncovered (Fraction):',len(unc2))
parent=[8,10,16,24,56,164,184,232,235,267,280,320,336,384,392]
def nearM(t,w): r=(t*w)%M; return 8*min(r,M-r)<M
print('parent uncovered t in 1..M-1:',[t for t in range(1,M) if not any(nearM(t,w) for w in parent)][:10])
