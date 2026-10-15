# Hesper independent check of Puck R16 (d82475e): own code.
# For config (c_i,v_i), h=c/2 mod 16. Level b parity beta. If h==beta mod 2: domino {h-v,h+v}; else {h, h+2*eps*v}, eps free (=-sgn d).
# R16: exists eps-choices such that the 16 domino entries mod 16 cover every residue of parity beta+1 exactly twice.
import json,itertools,sys,os
from collections import Counter
here=os.path.dirname(os.path.abspath(__file__))
mixed=lambda k: not (all(v%8 in (1,7) for c,v in k) or all(v%8 in (3,5) for c,v in k))
def canon(c,v): v%=32; return (c%32,min(v,32-v))
D=set(tuple(sorted(canon(c,v) for c,v in r)) for r in json.load(open('/workspace/work/r38_doublable_only.json')))
MD=[k for k in D if mixed(k)]
R=set(tuple(tuple(x) for x in k) for k in json.load(open(os.path.join(here,'../r38/checks/hesper_U_769.json'))))
def r16(k,beta):
    opts=[]
    for c,v in k:
        h=(c//2)%16
        if h%2==beta: opts.append([((h-v)%16,(h+v)%16)])
        else: opts.append([(h,(h+2*v)%16),(h,(h-2*v)%16)])
    for ch in itertools.product(*opts):
        cnt=Counter(x for dom in ch for x in dom)
        if all(cnt[r]==2 for r in range(16) if r%2!=beta) and sum(cnt.values())==16: return True
    return False
for beta in (0,1):
    S=set(k for k in MD if r16(k,beta))
    print("b parity",beta,"R16 holds on",len(S),"of",len(MD),"| on REAL",len(S&R),"of",len(R),"| equals 640-set:",S==R)

# Domino lemma check vs raw hit test (own labelling: t = e*b + p*u, label = e*u mod 16)
def hit(t,w,M): r=t*w%M; return 16*min(r,M-r)<M
def bal(x,p): x%=p; return x if x<=p//2 else x-p
bad=tot=0
for p in (29,31,37,41,43,47):
    for b in range(1,p):
        M=32*p; cells=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
        lab={}
        for t in cells:
            e=1 if t%p==b%p else -1; u=(t-e*b)//p; lab[t]=(e*u)%16
        for w in range(1,16*p,2):
            if w%p in (0,1,p-1): continue
            got=sorted(lab[t] for t in cells if hit(t,w,M))
            d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32); c=(-2*m*v)%32; h=(c//2)%16; eps=-1 if d>0 else 1
            # v stored with sign as computed (no canon) so eps orientation is meaningful
            pred=sorted([(h-v)%16,(h+v)%16]) if h%2==b%2 else sorted([h,(h+2*eps*v)%16])
            tot+=1; bad+= got!=pred
print("domino lemma: cases",tot,"mismatches",bad)
