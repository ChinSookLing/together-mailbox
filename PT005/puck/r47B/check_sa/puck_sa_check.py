# Puck independent check of Hesper Lemma SA (178ff05): at k=1, t=M/2=p, no odd coordinate covers t for either bit.
import gzip,csv,sys
cov=lambda w,T,N:16*min((T*w)%N,N-(T*w)%N)<N
f='PT005/hesper/r45/widen/nodes_widen.csv.gz'
n=odd_reach=even_reach=pe=mm=0
for row in csv.DictReader(gzip.open(f,'rt')):
    p=int(row['p']);M=int(row['M']);k=int(row['k'])
    if p%2==0: pe+=1
    if M!=(2**k)*p: mm+=1
    if k!=1: continue
    n+=1;t=M//2;N=2*M
    for w in map(int,row['coords'].split()):
        for b in (0,1):
            if cov(w+b*M,t,N):
                if w%2: odd_reach+=1
                else: even_reach+=1
print("all rows: even p",pe,"M!=2^k p",mm)
print("k=1 nodes",n,"| (odd coord,bit) covering t=p:",odd_reach,"| (even coord,bit) covering t=p:",even_reach)
bad=0
for p in range(1,400,2):
    M=2*p;N=4*p
    for w in range(1,2*M,2):
        for b in (0,1):
            if cov(w+b*M,p,N): bad+=1
print("brute force, all odd p<400, all odd w<2M, b in {0,1}: counterexamples",bad)
