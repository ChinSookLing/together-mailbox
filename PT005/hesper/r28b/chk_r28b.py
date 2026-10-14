W=[3,53,59,215,269,57,219,213]
cov={3:([11,351,363,385],[159,181,193,533]),53:([227,329,431,533],[11,113,215,317]),
59:([147,295,351,499],[45,193,249,397]),215:([91,147,329,521],[23,215,397,453]),
269:([113,283,453,465],[79,91,261,431]),57:([57,249,363,419],[125,181,295,487]),
219:([45,159,283,487],[57,261,385,499]),213:([317,419,465,521],[23,79,125,227])}
# recompute covers independently
N=1088
C6=[t for t in range(1,N//2+1,2) if t%17 in (6,11)]
def covers(w):
    return sorted(t for t in C6 if 16*min(t*w%N,N-t*w%N)<N)
ok=all(covers(w)==cov[w][0] and covers(w+544)==cov[w][1] for w in W)
print("cover lists recomputed match:",ok, "len C6",len(C6))
inc={}
for w in W:
  for a in (0,1):
    for t in cov[w][a]: inc.setdefault(t,[]).append((w,a))
print("each member twice:",all(len(v)==2 for v in inc.values()),len(inc))
def lab(t,u,v):
    d=dict(inc[t]); assert u in d and v in d,(t,u,v)
    return 1^d[u]^d[v]
def cyc(name,steps):
    s=0
    for u,t,v in steps: s^=lab(t,u,v)
    print(name,"H=",s,[lab(t,u,v) for u,t,v in steps])
cyc("Astra",[(3,351,59),(59,499,219),(219,385,3)])
cyc("DeepSeek",[(3,351,59),(59,147,215),(215,329,53),(53,11,3)])
cyc("GPT",[(53,113,269),(269,91,215),(215,329,53)])
for t1 in (419,125):
 for t2 in (249,295):
  for t3 in (147,397):
   for t4 in (329,215):
    cyc(f"Grok {t1},{t2},{t3},{t4}",[(53,227,213),(213,t1,57),(57,t2,59),(59,t3,215),(215,t4,53)])
QR={1,2,4,8,9,13,15,16}
print("b=3 QR count",sum(w%17 in QR for w in W))
# GPT R formula check vs a
def R(t,w): return ((2*t*w+544)//1088)%2
print("GPT R matches a?", all(R(t,w)==a for t,l in inc.items() for w,a in l))
def A(t,w):
    r=t*w%544; return ((t*w//544)%2)^(1 if r>476 else 0)
print("Astra a formula matches?", all(A(t,w)==a for t,l in inc.items() for w,a in l))
