import random, subprocess
from fractions import Fraction as F
def safe(K):
    I=[(F(0),F(1))]
    for k in K:
        new=[]
        for j in range(k):
            a,b=F(16*j+1,16*k),F(16*j+15,16*k)
            for x,y in I:
                lo,hi=max(x,a),min(y,b)
                if lo<hi: new.append((lo,hi))
        I=new
    return sum(b-a for a,b in I)
random.seed(20261011)
cases=[]
for _ in range(300):
    K=sorted(random.sample(range(1,25),13)); v=random.randint(25,300); cases.append((K,v))
cases.append(([1,2,3,4,5,7,8,9,10,11,12,13,15],56))
inp="\n".join(" ".join(map(str,K+[v])) for K,v in cases)+"\n"
out=subprocess.run(["./oneLarge","test"],input=inp,capture_output=True,text=True).stdout.split("\n")
bad=0
for (K,v),line in zip(cases,out):
    n,d=map(int,line.split()); 
    if F(n,d)!=safe(K+[v]): bad+=1
print("spot checks:",len(cases),"mismatches:",bad)
