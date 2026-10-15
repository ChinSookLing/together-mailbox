# Puck independent check (R39 Argon grade + R40 send-text data). Own code.
import json, itertools, re
D=[tuple(sorted(map(tuple,k))) for k in json.load(open('hesper/r38/checks/r38_doublable_only.json'))]
R=set(tuple(sorted(map(tuple,k))) for k in json.load(open('hesper/r38/checks/hesper_U_769.json')))
def norm(c,v):
    c%=32; v%=32
    return (c,v) if v<16 else (c,32-v)
def U(c,v): return frozenset((c+d*v)%32 for d in (1,-1,3,-3))
def is2cover(k):
    from collections import Counter
    C=Counter(s for f in k for s in U(*f)); return len(C)==16 and all(x==2 for x in C.values())
mixed=lambda k: not (all(v%8 in (1,7) for c,v in k) or all(v%8 in (3,5) for c,v in k))
MD=[k for k in set(D) if mixed(k)]
print('doublable',len(set(D)),'mixed doublable',len(MD),'realized',len(R),'R subset MD',R<=set(MD))
print('all 2-covers',all(is2cover(k) for k in MD))
def act(k,a,t): return tuple(sorted(norm(a*c+2*t,a*v) for c,v in k))
seen={}; orbits=[]
MDs=set(MD)
for k in sorted(MD):
    if k in seen: continue
    O=set(act(k,a,t) for a in range(1,32,2) for t in range(16))
    assert O<=MDs
    for x in O: seen[x]=len(orbits)
    orbits.append(O)
print('orbits',len(orbits),'sizes',sorted(len(o) for o in orbits),'sum',sum(len(o) for o in orbits))
real=[i for i,o in enumerate(orbits) if o&R]
print('real orbits',len(real),'fully real',all(orbits[i]<=R for i in real))
# send text rows
rows=[]
for line in open('hesper/r39/send_R40_Argon.txt'):
    m=re.match(r'(REAL|NEVER) size(\d+): (.*)',line.strip())
    if m:
        fp=tuple(sorted(norm(int(a),int(b)) for a,b in re.findall(r'\((\d+),(\d+)\)',m.group(3))))
        rows.append((m.group(1),int(m.group(2)),fp))
ok=0; hit=set()
for lab,sz,fp in rows:
    i=seen.get(fp); 
    good = i is not None and len(orbits[i])==sz and ((lab=='REAL')==(i in real))
    ok+=good; hit.add(i)
print('send rows',len(rows),'correct',ok,'distinct orbits',len(hit-{None}))
# Argon R39 oriented 1-cover rule
odds=frozenset(range(1,32,2))
def oriented(k):
    for sg in itertools.product((1,-1),repeat=8):
        S=[]
        for (c,v),s in zip(k,sg): S+= [(c+s*v)%32,(c+3*s*v)%32]
        if len(S)==16 and set(S)==odds: return True
    return False
o_all=sum(oriented(k) for k in MD); o_real=sum(oriented(k) for k in R)
print('oriented rule: MD',o_all,'realized',o_real)
print('sum c ==0 mod16: MD',sum(sum(c for c,v in k)%16==0 for k in MD),'of',len(MD))
# p=29,b=1 real tiling
p,b=29,1; W=(19,179,441,339,397,313,237,77)
fp=[]
for w in W:
    m=round(b*w/p); d=b*w-m*p; assert abs(d)<p/2
    v=pow(w,-1,32); c=(-2*m*v)%32; fp.append(norm(c,v))
fp=tuple(sorted(fp)); print('W footprint',fp,'2cover',is2cover(fp),'in MD',fp in MDs,'oriented',oriented(fp))
