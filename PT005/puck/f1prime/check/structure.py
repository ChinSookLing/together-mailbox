# structural statistics of mixed tilings: XOR-graph invariants (labels from Astra criterion, which matched truth 100%)
import sys, collections
import f1check as f
def graph(C):
    el=[]
    for s,ij in f.edges(C):
        i,j=ij; el.append((i,j,1^f.astra_q(C[i],s)^f.astra_q(C[j],s)))
    return el
def comps(el):
    par=list(range(8))
    def fd(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for i,j,_ in el: par[fd(i)]=fd(j)
    return len({fd(i) for i in range(8)})
def invariants(el):
    nb=collections.defaultdict(set); mult=collections.Counter()
    for i,j,l in el: nb[i].add(j); nb[j].add(i); mult[(min(i,j),max(i,j))]+=1
    dd=tuple(sorted(len(nb[i]) for i in range(8)))
    mm=tuple(sorted(mult.values()))
    lab=collections.defaultdict(set)
    for i,j,l in el: lab[(min(i,j),max(i,j))].add(l)
    odig=any(len(v)>1 for v in lab.values())
    return dd,mm,odig
for p in [int(x) for x in sys.argv[1:]]:
    D=collections.Counter()
    for b in range(1,p//2+1):
        for W in f.tilings(p,b):
            if f.oneclass(W): continue
            C=f.coords(p,b,W); el=graph(C)
            T=f.crit(C,'astra')
            dd,mm,od=invariants(el)
            D[(T,comps(el),dd,od)]+=1
    print('p=%d (mixed tilings): key=(doublable, #components, distinct-neighbour degree seq, has_odd_digon)'%p)
    for k,c in sorted(D.items(),key=lambda x:(-x[0][0],-x[1])):
        if k[0] or p<=23 and c>=1: print('  ',k,c)
    sys.stdout.flush()
