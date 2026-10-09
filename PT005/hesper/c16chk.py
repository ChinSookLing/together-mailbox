import itertools,sys,time
sys.path.insert(0,'together-mailbox/scouting/LR16/opus/guess_r3')
from longest import c_of
from fractions import Fraction as F
M=int(sys.argv[1]);best=(9,None);t=time.time();n=0
for S in itertools.combinations(range(1,M+1),13):
    if M not in S: continue  # new subsets only
    n+=1;c=c_of(S)
    if c<best[0]-1e-12: best=(c,S)
print(M,n,best,time.time()-t)
