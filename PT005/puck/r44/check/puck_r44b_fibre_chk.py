# Puck independent check of Argon R44b Task 1: odd j in 1..2^k-1, cover iff ||j*w'||_{2^(k+1)} < 2^(k-3)
def nd(x,m): x%=m; return min(x,m-x)
for p in (19,23,29):
  for k in range(3,9):
    M=2**k*p; res={}
    for w in range(1,M):
      v=(w&-w).bit_length()-1
      d=k-v if v<k else 0
      for wc in (w,w+M):
        c=sum(1 for j in range(1,2**k,2) if 16*nd(j*p*wc,2*M)<2*M)
        res.setdefault((d, v>k),set()).add(c)
    print(p,k,{key:sorted(val) for key,val in sorted(res.items())})
