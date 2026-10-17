from own import *
def run(name,p,vecs):
    M=p
    print("==",name)
    for w in vecs:
        print(" ",M,"open",is_open(w,M),fstats(w,M,p)); M*=2
    M//=2; lvl=[vecs[-1]]
    for step in range(2):
        nxt=set()
        for x in lvl: nxt|=set(map(tuple,open_children(x,M)))
        M*=2
        print("   next",M,"open",len(nxt), "F3",sorted({fstats(list(n),M,p)['F3'] for n in nxt}) if nxt else "")
        if not nxt: break
        lvl=[list(n) for n in sorted(nxt)][:300]
run("Astra43",43,[[2,5,5,6,8,9,13,14,16,16,17,18,19,20,21],[2,5,9,13,16,19,48,49,51,57,59,60,61,63,64],[2,13,16,48,49,51,91,95,105,143,145,146,147,149,150],[2,13,16,49,91,105,143,146,220,223,267,317,319,321,322]])
X=[1,1,3,3,3,5,6,7,7,8,8,18,19,21,22]; Y=[1,3,8,21,22,35,37,41,42,71,73,74,75,86,87]
run("Astra17",17,[[1,1,1,2,3,3,3,4,5,5,6,7,7,8,8],X,sorted(y%68 for y in Y),Y])
G=[8,113,11,49,37,73,83,11,75,50,1,15,16,3,13]
run("Grok17",17,[[8,11,11,15,3,5,15,11,7,16,1,15,16,3,13],sorted(g%34 for g in G),sorted(g%68 for g in G),G])
