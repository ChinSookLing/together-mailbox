# c(S) = max(S) * (longest 1/16-safe piece). Lemma A uses c(S) >= 1/56 (from LRC). How small can c(S) really be?
import sys, random, time
d=1/16
def pieces(S):
    acc=[(0.0,1.0)]
    for v in S:
        allowed=[((m+d)/v,(m+1-d)/v) for m in range(v)]
        new=[]; i=j=0
        while i<len(acc) and j<len(allowed):
            a,b=acc[i]; c,e=allowed[j]; lo,hi=max(a,c),min(b,e)
            if lo<=hi: new.append((lo,hi))
            if b<e: i+=1
            else: j+=1
        acc=new
    return acc
def c_of(S):
    P=pieces(S); return max(S)*max(b-a for a,b in P) if P else 0.0
if __name__=="__main__":
  M=int(sys.argv[1]); secs=float(sys.argv[2]); rnd=random.Random(int(sys.argv[3]))
  best=(9,None); t0=time.time()
  while time.time()-t0<secs:
      S=sorted(rnd.sample(range(1,M+1),13)); c=c_of(S); imp=True
      while imp and time.time()-t0<secs:
          imp=False
          for i in range(13):
              for w in rnd.sample(range(1,M+1),M):
                  if w in S: continue
                  T=sorted(S[:i]+S[i+1:]+[w]); c2=c_of(T)
                  if c2<c-1e-12: S,c,imp=T,c2,True; break
      if c<best[0]: best=(c,S)
  print(f"M={M} min c(S) found {best[0]:.5f} (1/c = {1/best[0]:.1f}) S={best[1]} | c(1..13)={c_of(list(range(1,14))):.5f} | Lemma A bound 1/56={1/56:.5f}")
