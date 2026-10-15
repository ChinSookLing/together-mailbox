K=[[(0,1),(0,1),(6,11),(6,11),(12,1),(12,1),(22,1),(22,1)],
[(0,1),(0,1),(8,1),(14,3),(16,1),(16,3),(18,3),(24,1)],
[(0,1),(0,5),(2,5),(4,5),(8,1),(24,1),(28,5),(30,5)],
[(0,1),(0,7),(2,11),(6,11),(12,1),(20,1),(26,11),(30,11)],
[(0,1),(2,1),(8,11),(10,1),(14,1),(16,11),(22,1),(24,1)]]
A=[("..--..--","01010101"),("++..--..","01010101"),("...+..-.","01010110"),("---.--.-","01010110"),("..-....+","01110100"),("--.---+.","01110100"),("..--..++","00101010"),("--..-+..","01000111"),(".+.+-.-.","01001101"),("-.-..-.-","01010101")]
G=[("--------","01010101"),("++------","01010101"),("---+----","01010110"),("--------","01010110"),("-------+","01110100"),("------+-","01110100"),("------++","00101010"),("-----+--","01000111"),("-+-+----","01001101"),("--------","01010101")]
def run(cert,name,strict):
  ok=0
  for j,k in enumerate(K):
    for b in (0,1):
      s,l=cert[2*j+b]; D=[];bad=False
      for i,(c,v) in enumerate(k):
        h=(c//2)%16; H=(h+16*int(l[i]))%32
        if h%2==b:
          if strict and s[i]!='.': bad=True
          D+= [(H-v)%32,(H+v)%32]
        else:
          if s[i]=='.': bad=True; e=1
          else: e=1 if s[i]=='+' else -1
          D+= [H%32,(H+2*e*v)%32]
      tgt=sorted(r for r in range(32) if r%2==(b+1)%2)
      res=sorted(D)==tgt and not bad
      ok+=res
      print(name,j+1,b,'PASS' if res else 'FAIL'+(' (sign/type mismatch)' if bad else ''), sorted(D) if not res else '')
  print(name,'total',ok,'/10')
run(A,'Astra',True); run(G,'GPT',False)
# affine transport check on full orbits: generate orbit of each rep, transport cert, verify
import itertools
def canon(k): return tuple(sorted(((c%32),min(v%32,(-v)%32)) for c,v in k))
tot=0;fail=0
for j,k in enumerate(K):
  seen={}
  for a in range(1,32,2):
    for t in range(16):
      for b in (0,1):
        s,l=G[2*j+b]; D=[]
        k2=[((a*c+2*t)%32,(a*v)%32) for c,v in k]
        b2=(b+t)%2
        for i,(c,v) in enumerate(k):
          h=(c//2)%16; H=(h+16*int(l[i]))%32
          H2=(a*H+t)%32; c2,v2=k2[i]; h2=(c2//2)%16
          assert H2%16==h2
          if h2%2==b2: D+=[(H2-v2)%32,(H2+v2)%32]
          else:
            e=1 if s[i]=='+' else -1; D+=[H2,(H2+2*e*v2)%32]
        ok=sorted(D)==sorted(r for r in range(32) if r%2==(b2+1)%2)
        seen.setdefault((canon(k2),b2),True); tot+=1; fail+= (not ok)
  print('orbit',j+1,'distinct (config,beta) covered',len(seen))
print('transport checks',tot,'fails',fail)
