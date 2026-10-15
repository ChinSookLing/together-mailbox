#!/usr/bin/env python3
"""PT005 R37 Puck grading checks (independent).
1) z-formula: lift bit of coordinate w covering member t equals z(s)+h mod 2,
   z(s) = (2M + s*A - rho)/32 mod 2, A = w mod 64, M = m mod 32, s in 1..31 odd,
   t = eps*(2b + p*(s+32h)). Tested on random (p,b,w).
2) lambda = 1^z_i^z_j equals brute-force label a^c^1 on all 32 members of the 3 examples;
   seat tables (Astra pair/label rows, GPT endpoint/label strings, lift vectors) checked.
3) cycle rank of the 3 graphs.
4) Astra (b0=64/65, p>16640) and GPT (B=5/6, p>12288) realisation constructions run on
   the 3 example reduced configs at large primes; reduced data, k=5 tiling, doubling re-checked.
"""
import random
from itertools import product
from collections import defaultdict

def bal(x,p):
    r=x%p; return r-p if r>p//2 else r
def covers(t,w,N):
    r=(t*w)%N; return 16*min(r,N-r)<N
def members(p,r,top):
    return [t for t in range(1,top+1,2) if t%p in (r%p,(-r)%p)]
def red(p,b,w):
    d=bal(b*w,p); m=(b*w-d)//p
    v=pow(w,-1,32); c=(-2*m*v)%32
    return (w%64,m%32,'+' if d>0 else '-',c,v)
def z(A,M,s):
    x=(2*M+s*A)%32
    rho={1:1,3:3,31:-1,29:-3}.get(x)
    if rho is None: return None
    return ((2*M+s*A-rho)//32)%2
def pos(p,b,t):
    for eps in (1,-1):
        if (t-eps*2*b)%p==0:
            u=(t-eps*2*b)//p          # t = eps*2b + p*u
            # want t = eps*(2b + p*(s+32h)), s in 1..31  -> eps*u = s+32h
            x=eps*u; s=x%32; h=(x-s)//32
            return s,h
    raise ValueError

def isprime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True

# ---- 1) z-formula on random coordinates
fails=0; tests=0
primes=[q for q in range(17,3000) if isprime(q)]
random.seed(37)
for _ in range(3000):
    p=random.choice(primes); b=random.randrange(1,p)
    w=random.randrange(1,16*p,2)
    if w%p in (0,1,p-1): continue
    A,M,_,c,v=red(p,b,w)
    N6=64*p
    for t in members(p,2*b,32*p):
        for a,L in enumerate((w,w+32*p)):
            if covers(t,L,N6):
                tests+=1
                s,h=pos(p,b,t)
                zz=z(A,M,s)
                if zz is None or (zz+h)%2!=a: fails+=1
print(f"[1] z-formula lift-bit test: {tests} (member,lift) incidences, fails={fails}")

EX=[(29,1,(3,97,125,151,413,191,285,385)),
    (79,76,(865,993,675,289,385,579,545,673)),
    (89,36,(1345,545,1089,129,673,587,139,1035))]
ASTRA_TAB={
29:"14/0 38/0 48/0 78/1 58/1 16/0 36/0 46/0 67/1 45/1 15/1 23/1 23/1 27/0 27/0 15/1",
79:"16/1 16/1 37/1 27/0 27/0 27/0 26/0 38/0 48/0 48/0 48/0 46/1 35/1 35/1 15/1 15/1",
89:"15/1 15/1 28/0 27/0 26/0 28/0 37/1 36/1 38/1 37/1 46/1 48/1 47/1 46/1 15/1 15/1"}
ASTRA_EPS={29:(0,1,0,0,1,0,1,0),79:(0,1,0,0,1,1,1,0),89:(0,0,1,1,1,0,0,0)}
GPT_PHI={29:"01001010",79:"01001110",89:"00111000"}
GPT_LAB={29:"0001100011111001",79:"1110000000011111",89:"1100001111111111"}
GPT_END={29:"03 27 37 67 47 05 25 35 56 34 04 12 12 16 16 04",
         79:"05 05 26 16 16 16 15 27 37 37 37 35 24 24 04 04",
         89:"04 04 17 16 15 17 26 25 27 26 35 37 36 35 04 04"}

def analyse(p,b,W,verbose=True):
    N5,N6=32*p,64*p
    C5=members(p,b,16*p); C6=members(p,2*b,32*p)
    tiling=all(sum(covers(t,w,N5) for w in W)==1 for t in C5)
    R=[red(p,b,w) for w in W]
    lifts=[(w,w+32*p) for w in W]
    edges={}  # s -> (i,j,lambda_brute,lambda_formula)
    ok=True
    for t in C6:
        cs=[(i,a) for i in range(8) for a in (0,1) if covers(t,lifts[i][a],N6)]
        if len(cs)!=2 or cs[0][0]==cs[1][0]: ok=False; continue
        (i,a),(j,c)=cs
        s,h=pos(p,b,t)
        lb=a^c^1
        lf=1^z(R[i][0],R[i][1],s)^z(R[j][0],R[j][1],s)
        if s in edges and edges[s][:3]!=(i,j,lb): ok=False
        edges[s]=(i,j,lb,lf)
        if lb!=lf: ok=False
    sols=[ch for ch in product((0,1),repeat=8)
          if all(sum(covers(t,lifts[i][ch[i]],N6) for i in range(8))==1 for t in C6)]
    return tiling,R,edges,ok,sols

print()
for p,b,W in EX:
    tiling,R,edges,ok,sols=analyse(p,b,W)
    S=sorted(edges)
    print(f"[2] p={p}: tiling={tiling} positions={len(S)} labels brute==formula & both members per position same pair/label: {ok}")
    mine=[f"{edges[s][0]+1}{edges[s][1]+1}/{edges[s][2]}" for s in S]
    ast=ASTRA_TAB[p].split()
    def norm(x): pr,l=x.split('/'); return (''.join(sorted(pr)),l)
    da=[s for s,m_,a_ in zip(S,mine,ast) if norm(m_)!=norm(a_)]
    print(f"    Astra table vs computed: diffs at s={da}")
    if da: print("     mine :"," ".join(mine)); print("     astra:",ASTRA_TAB[p])
    ge=GPT_END[p].split(); gl=GPT_LAB[p]
    dg=[s for k,s in enumerate(S) if (''.join(sorted(ge[k])),gl[k])!=(''.join(sorted(f"{edges[s][0]}{edges[s][1]}")),str(edges[s][2]))]
    print(f"    GPT endpoints/labels vs computed: diffs at s={dg}")
    if dg:
        print("     mine :"," ".join(f"{edges[s][0]}{edges[s][1]}" for s in S),"".join(str(edges[s][2]) for s in S))
        print("     gpt  :",GPT_END[p],gl)
    e=ASTRA_EPS[p]; g=tuple(map(int,GPT_PHI[p]))
    print(f"    brute-force lift solutions: {sols}")
    print(f"    Astra eps in sols: {e in sols};  GPT phi in sols: {g in sols};  same vector: {e==g}")
    simple={(i,j) for (i,j,_,_) in edges.values()}
    # components
    par=list(range(8))
    def f(x):
        while par[x]!=x: x=par[x]
        return x
    for i,j in simple: par[f(i)]=f(j)
    comps=len({f(x) for x in range(8)})
    print(f"    cycle rank: position-graph (16 edges) = {16-8+comps}; simple graph ({len(simple)} edges) = {len(simple)-8+comps}; components={comps}")
    # identical (c,v) footprint pairs
    same=[(i,j) for i in range(8) for j in range(i+1,8) if R[i][3:]==R[j][3:]]
    print(f"    coordinate pairs with identical (c,v): {same}")

# ---- 4) realisation constructions at large p
def nextprime(n):
    while not isprime(n): n+=1
    return n

def astra_build(p,Rd,bpar):
    b0=64 if bpar==0 else 65; Mod=64*b0
    used=set(); W=[]
    for k,(A,M,sg,_,_) in enumerate(Rd):
        m=256+M+32*k          # distinct, in 256..767, == M mod 32
        r=(b0*A-p*m)%Mod
        cands=[r+Mod*j for j in range(-2,3)]
        cands=[d for d in cands if (d>0)==(sg=='+') and d not in (0,b0,-b0) and abs(d)<=2*Mod]
        d=min(cands,key=abs)
        assert (p*m+d)%b0==0
        W.append((p*m+d)//b0)
    return b0,W

def gpt_build(p,Rd,bpar):
    B=6 if bpar==0 else 5
    W=[]; taken=set()
    for (A,M,sg,_,_) in Rd:
        ms=32+M; dl=1 if sg=='+' else -1
        lo,hi=sorted([p*(ms+dl/8)/B,p*(ms+dl*3/8)/B])
        w=int(lo)+1
        while w%64!=A or w in taken: w+=1
        assert w<hi
        taken.add(w); W.append(w)
    return B,W

print()
for p0,b,W in EX:
    tiling,R,_,_,sols0=analyse(p0,b,W)
    for name,P0,build in (("Astra",16640,astra_build),("GPT",12288,gpt_build)):
        P=nextprime(P0+1)
        bb,W2=build(P,R,b%2)
        legal=all(w%2==1 and 1<=w<16*P and w%P not in (0,1,P-1) for w in W2) and len(set(W2))==8
        t2,R2,e2,ok2,s2=analyse(P,bb,W2)
        print(f"[4] {name}: p0={p0} config -> p={P}, b={bb}: legal&distinct={legal} reduced same={R2==R} tiling={t2} labels ok={ok2} doublable={bool(s2)} #sols={len(s2)} (orig {len(sols0)})")
