import re,itertools
L=[l for l in open('together-mailbox/PT005/hesper/r39/send_R40_Argon.txt') if l.startswith(('REAL','NEVER'))]
rows=[(l.split()[0],[tuple(map(int,x.split(','))) for x in re.findall(r'\((\d+,\d+)\)',l)]) for l in L]
def opts32(c,v,b):
    h=c//2; o=[]
    for beta in (0,1):
        H=h+16*beta
        if h%2==b%2: o.append(frozenset({(H-v)%32,(H+v)%32}))
        else:
            for s in (1,-1): o.append(frozenset({H%32,(H+2*s*v)%32}))
    return list(set(o))
def part32(fp):
    for b in (0,1):
        S={s for s in range(32) if s%2==(b+1)%2}
        O=[opts32(c,v,b) for c,v in fp]
        def rec(i,used):
            if i==8: return used==S
            return any(not(e&used) and rec(i+1,used|e) for e in O[i] if len(e)==2)
        if rec(0,frozenset()): return True
    return False
def opts16(c,v,b):
    h=c//2
    if h%2==b%2: return [tuple(sorted(((h-v)%16,(h+v)%16)))]
    return list({tuple(sorted((h%16,(h+2*s*v)%16))) for s in (1,-1)})
def graph(fp):
    for b in (0,1):
        for E in itertools.product(*[opts16(c,v,b) for c,v in fp]):
            deg={}
            for x,y in E:
                deg[x]=deg.get(x,0)+1; deg[y]=deg.get(y,0)+1
            if len(deg)!=8 or any(d!=2 for d in deg.values()) or any(x==y for x,y in E): continue
            # components cycle lengths
            adj={}
            for i,(x,y) in enumerate(E): adj.setdefault(x,[]).append(i); adj.setdefault(y,[]).append(i)
            seen=set(); ok=True
            for i in range(8):
                if i in seen: continue
                st=[i]; comp=set()
                while st:
                    j=st.pop()
                    if j in comp: continue
                    comp.add(j)
                    for x in E[j]: st+=adj[x]
                seen|=comp
                if len(comp)%2: ok=False
            if ok: return True
    return False
for name,f in (('exact mod32 partition',part32),('mod16 even-cycle graph',graph)):
    r=[(lab,f(fp)) for lab,fp in rows]
    good=sum((lab=='REAL')==x for lab,x in r)
    print(name, 'agree',good,'/39', 'REAL pass',sum(x for lab,x in r if lab=='REAL'),'/5','NEVER pass',sum(x for lab,x in r if lab=='NEVER'),'/34',
      'bad rows',[i+1 for i,(lab,x) in enumerate(r) if (lab=='REAL')!=x])
