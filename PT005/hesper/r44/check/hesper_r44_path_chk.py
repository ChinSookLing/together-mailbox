from hesper_r44_p19_chk import *
path=[(19,[1,2,3,4,5,6,7,8,9,11,12,15,16,17,18]),(38,[1,21,3,23,5,25,7,8,9,11,31,15,35,17,37]),(76,[39,59,41,61,43,25,45,8,47,49,69,15,73,55,37]),(152,[39,59,41,61,43,101,121,8,47,125,145,15,73,55,37]),(304,[191,59,41,213,195,101,121,160,47,125,145,15,73,207,37])]
prev=None
for M,w in path:
    leg = True if prev is None else all(a in (b,b+prev[0]) for a,b in zip(w,prev[1]))
    print(M,"open",is_open(w,M),"legal",leg,"F1",F(w,M,1),"F3",F(w,M,3)); prev=(M,w)
# GLM claim: T in {19,57,95,133} at 304 covered only by coordinate 160
W=path[-1][1]; N=304
for T in (19,57,95,133):
    cov=[x for x in W if 16*min((T*x)%N,N-(T*x)%N)<N]; print("T",T,"covered by",cov)
print("residues mod 19 of 152-node:",sorted(x%19 for x in path[3][1]))
