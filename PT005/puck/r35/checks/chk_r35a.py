# Puck independent check of Astra's and GPT's R35a local claims (mod 32 model from L1)
fp={}
for c in range(0,32,2):
    for v in range(1,32,2):
        U=frozenset((c+k*v)%32 for k in (-3,-1,1,3))
        fp.setdefault(U,set()).add((c,v))
def cls(U): 
    s={v%8 in (1,7) for c,v in fp[U]}; assert len(s)==1; return 'A' if s.pop() else 'B'
U0=frozenset({29,31,1,3}); print("U0 class",cls(U0))
# Astra table: for each 2+2 split of U0, which neighbour classes possible (neighbour shares exactly that pair)
splits=[({1,31},{3,29}),({1,29},{3,31}),({1,3},{29,31})]
for P,Q in splits:
    out=[]
    for X in (P,Q):
        cand=[U for U in fp if U&U0==X]
        out.append(sorted({cls(U) for U in cand}))
    print("split",sorted(P),sorted(Q),"neighbour classes",out)
# junction: P={1,3} same class A, Q={29,31} class B
S=[U for U in fp if U&U0=={1,3} and cls(U)==cls(U0)]
C=[U for U in fp if U&U0=={29,31} and cls(U)!=cls(U0)]
print("S cands",[sorted(u) for u in S]); print("C cands",[sorted(u) for u in C])
bad=0
for s in S:
  for c in C:
    if s&c: continue
    rest=c-U0
    D=[U for U in fp if U&c==rest and not U&U0]
    for d in D:
        if not d&s: bad+=1; print("no chord:",sorted(s),sorted(c),sorted(d))
print("junction survivals without chord",bad)
# reverse orientation (A on {29,31}, B on {1,3})
S2=[U for U in fp if U&U0=={29,31} and cls(U)==cls(U0)]
C2=[U for U in fp if U&U0=={1,3} and cls(U)!=cls(U0)]
bad2=0
for s in S2:
  for c in C2:
    if s&c: continue
    for d in [U for U in fp if U&c==(c-U0) and not U&U0]:
        if not d&s: bad2+=1
print("reverse survivals",bad2)
# GPT: footprints containing {31,1}
base=frozenset({29,31,1,3})
cand=[U for U in fp if {31,1}<=U]
print("GPT cands",[(sorted(U),len(U&base),cls(U)) for U in cand])
