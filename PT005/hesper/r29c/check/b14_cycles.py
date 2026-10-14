# Hesper: the 14 one-class sigma-even no-digon tilings: pair structure, odd cycles, Grok's triangle (0,7,2) at b=1
import sys, itertools; sys.path.insert(0,'/workspace/work/together-mailbox/PT005/puck/verify')
from common import *
from collections import defaultdict, Counter
rows=[l.split('ws ')[1].split(' mult4')[0] for l in open(__import__('os').path.join(__import__('os').path.dirname(__file__),'b14_list_out.txt'))]
bs=[int(l.split()[1]) for l in open(__import__('os').path.join(__import__('os').path.dirname(__file__),'b14_list_out.txt'))]
shape=Counter()
for b,r in zip(bs,rows):
    ws=eval(r); c6=C(6,(2*b)%P); n5,n6=N(5),N(6)
    hit=defaultdict(list)
    for i,w in enumerate(ws):
        for e in (0,1):
            for t in c6:
                if covers(t,(w+e*n5)%n6,n6): hit[t].append((i,e))
    pl={}; pm=Counter(); mem=defaultdict(list)
    for t,h in hit.items():
        (i,a),(j,c)=sorted(h); pl[(i,j)]=a^c^1; pm[(i,j)]+=1; mem[(i,j)].append(t)
    adj=defaultdict(dict)
    for (i,j),l in pl.items(): adj[i][j]=l; adj[j][i]=l
    # shortest odd cycle in simple pair graph with labels
    best=None
    for L in range(3,9):
        for cyc in itertools.permutations(range(8),L):
            if cyc[0]!=min(cyc) or cyc[1]>cyc[-1]: continue
            if all(cyc[(k+1)%L] in adj[cyc[k]] for k in range(L)):
                if sum(adj[cyc[k]][cyc[(k+1)%L]] for k in range(L))%2: best=cyc; break
        if best: break
    m4=[k for k,v in pm.items() if v==4]
    deg=Counter(); [deg.update(k) for k in pm]
    shape[(tuple(sorted(Counter(pm.values()).items())), len(best))]+=1
    if b==1 and ws[0]==7:
        print('Grok example b=1 ws',ws)
        for k in [(0,7),(0,2),(2,7)]: print('  pair',k,'present' if k in pl else 'ABSENT', 'label',pl.get(k),'members',mem.get(k))
        print('  who hits t=427:',hit.get(427))
        print('  pair graph degrees',dict(deg),' shortest odd cycle',best,'labels',[adj[best[k]][best[(k+1)%len(best)]] for k in range(len(best))])
    print('b',b,'ws',ws,'mult4 matching',sorted(m4),'shortest odd cycle',best)
print('summary (pair multiplicities, shortest odd cycle length):',dict(shape))
# structure of the multiplicity-2 pairs (a 2-factor) and whether its components are the odd cycles
print('--- 2-factor of multiplicity-2 pairs ---')
res=Counter()
for b,r in zip(bs,rows):
    ws=eval(r); c6=C(6,(2*b)%P); n5,n6=N(5),N(6)
    hit=defaultdict(list)
    for i,w in enumerate(ws):
        for e in (0,1):
            for t in c6:
                if covers(t,(w+e*n5)%n6,n6): hit[t].append((i,e))
    pl={}; pm=Counter()
    for t,h in hit.items():
        (i,a),(j,c)=sorted(h); pl[(i,j)]=a^c^1; pm[(i,j)]+=1
    two=[k for k,v in pm.items() if v==2]
    adj=defaultdict(list)
    for i,j in two: adj[i].append(j); adj[j].append(i)
    seen=set(); comps=[]
    for s in range(8):
        if s in seen: continue
        comp=[s]; seen.add(s); prev=None; cur=s
        while True:
            nx=[y for y in adj[cur] if y!=prev and y not in seen]
            if not nx: break
            prev,cur=cur,nx[0]; comp.append(cur); seen.add(cur)
        par=sum(pl[tuple(sorted((comp[k],comp[(k+1)%len(comp)])))] for k in range(len(comp)))%2
        comps.append((len(comp),par))
    m4par=[pl[k] for k,v in pm.items() if v==4]
    res[(tuple(sorted(comps)),tuple(sorted(m4par)))]+=1
print('(2-factor components (length,label parity), matching-edge labels):',dict(res))
