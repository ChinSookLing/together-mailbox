# Puck R38 aux checks (one file): [A] compare with Hesper's r38_k5layer.out, set equality across p, first prime per class;
# [B] affine-orbit structure; [C] probe of (w,e) pairs sharing one 48-bit mask.
# Inputs: k5_sets.json (realized config sets per p, 'all' = all reps, 'one' = one rep per footprint solution) and k5layer_out.txt.
import json, re, ast, sys
from collections import Counter, defaultdict
sys.argv=[sys.argv[0]]
from puck_r38_k5layer import degs
SETS=json.load(open('k5_sets.json'))
LINES={json.loads(l)['p']:l for l in open('k5layer_out.txt') if l.startswith('{')}
print('[A]')
H={}
for line in open('../../../hesper/r38/checks/r38_k5layer.out'):
    m=re.match(r'p=(\d+) mixed-doublings=(\d+) distinct-configs=(\d+) not-in-table=(\d+) classes=(.*)$',line.strip())
    if m: H[int(m[1])]=(int(m[2]),int(m[3]),int(m[4]),ast.literal_eval(m[5]))
sets={}; first={}
for p in (17,19,23,29,31,37,41,43,47,53,59,61):
    if str(p) not in SETS or p not in LINES:
        print(f'p={p}: not reached'); continue
    A=set(tuple(map(tuple,r)) for r in SETS[str(p)]['all'])
    O=set(tuple(map(tuple,r)) for r in SETS[str(p)]['one'])
    sets[p]=A
    for r in A: first.setdefault(degs(r),p)
    line=LINES[p]
    R=json.loads(line); mine_cls=ast.literal_eval(R['classes_one'])
    h=H.get(p)
    match = h is not None and (R['footsol_mixed'],R['distinct_one'],R['notin_one'])==h[:3] and mine_cls==h[3]
    print(f"p={p} one-rep: mixed={R['footsol_mixed']} distinct={R['distinct_one']} notin={R['notin_one']} | all-reps: mixed={R['allreps_mixed']} distinct={R['distinct_all']} notin={R['notin_all']} | one==all configs: {A==O} | matches Hesper .out line exactly: {match}")
print('first prime per degree class:',dict(sorted(first.items(),key=lambda x:x[1])))
big=[p for p in (47,53,59,61) if p in sets]
for p in big[1:]: print(f'set(p={p}) == set(p=47): {sets[p]==sets[47]}')
for p in sorted(sets):
    if p>=29 and 47 in sets: print(f'p={p} subset of set(47): {sets[p]<=sets[47]}')
TAB=set(tuple(sorted((c,min(v%32,32-v%32)) for c,v in r)) for r in json.load(open('../../../hesper/r38/checks/r38_doublable_only.json')))
U=set().union(*sets.values()) if sets else set()
print('union of realized configs:',len(U),' all in 8,704 table:',U<=TAB)
print('table mixed-doublable classes:',dict(Counter(degs(r) for r in TAB if len({v%8 in (1,7) for c,v in r})==2)))
print('realized union classes:',dict(Counter(degs(r) for r in U)))

def canon(c,v): v%=32; return (c%32,min(v,32-v))
print('[B]')
A=set(tuple(map(tuple,r)) for r in SETS['47']['all'])
T=set(tuple(sorted(canon(c,v) for c,v in r)) for r in json.load(open('../../../hesper/r38/checks/r38_doublable_only.json')))
G=[(a,t) for a in range(1,32,2) for t in range(0,32,2)]
def act(g,r): a,t=g; return tuple(sorted(canon(a*c+t,a*v) for c,v in r))
print('realized closed under affine group:',all(act(g,r) in A for g in G for r in A))
print('table closed under affine group:',all(act(g,r) in T for g in G for r in T))
seen=set(); orb=[]
for r in sorted(A):
    if r in seen: continue
    O={act(g,r) for g in G}; seen|=O; orb.append((degs(r),len(O)))
print('realized orbits (class,size):',orb)
seen=set(); to=[]
for r in sorted(T):
    if r in seen: continue
    O={act(g,r) for g in G}; seen|=O
    if len({v%8 in (1,7) for c,v in r})==2: to.append((degs(r),len(O),bool(O&A)))
print('mixed-doublable table orbits (class,size,realized):',sorted(to))

print('[C]')
def hit(t,W,M): r=t*W%M; return 16*min(r,M-r)<M
def bal(x,p): x%=p; return x if x<=p//2 else x-p
def cv(p,b,w):
    d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32); c=(-2*m*v)%32; return c,min(v,32-v)
for p in (29,31,37,41,43,47,53,59,61):
    st=Counter(); ex=None
    for b in range(1,(p+1)//2):
        c5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
        c6=[t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
        g=defaultdict(list)
        for w in range(1,16*p,2):
            if w%p in (0,1,p-1): continue
            m5=sum(1<<i for i,t in enumerate(c5) if hit(t,w,32*p))
            for e in (0,1):
                m6=sum(1<<i for i,t in enumerate(c6) if hit(t,w+e*32*p,64*p))
                g[(m5,m6)].append((w,e))
        for L in g.values():
            if len(L)>1:
                same=len({cv(p,b,w) for w,e in L})==1
                sameclass=len({w%8 in (1,7) for w,e in L})==1
                st[(len(L),'same_cv' if same else 'DIFF_cv','same_class' if sameclass else 'DIFF_class')]+=1
                if ex is None: ex=(b,L,[cv(p,b,w) for w,e in L])
    print(p,dict(st),'example',ex)
