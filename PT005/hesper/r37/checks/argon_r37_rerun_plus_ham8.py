def verify_example(name, data):
    # data: list of (w64, m32, sgn_d, c, v)
    edges = {}
    for i, (w64, m32, sgn, c, v) in enumerate(data):
        for delta in (1, -1, 3, -3):
            s = (c + delta * v) % 32
            k = (s - c - delta * v) // 32
            edges.setdefault(s, []).append((i, delta, v, k % 2))
    # Build linear system x_i ^ x_j = k_i ^ k_j ^ 1 over GF(2)
    # Check cycle parities via spanning forest
    parent = {}
    comp = 0
    odd_cycles = 0
    for u in range(len(data)):
        if u not in parent:
            comp += 1
            parent[u] = (u, 0)
            stack = [u]
            while stack:
                curr = stack.pop()
                for s, pts in edges.items():
                    (i, di, vi, ki), (j, dj, vj, kj) = pts
                    lam = ki ^ kj ^ 1
                    nxt = j if i == curr else (i if j == curr else None)
                    if nxt is not None:
                        if nxt not in parent:
                            parent[nxt] = (curr, parent[curr][1] ^ lam)
                            stack.append(nxt)
                        elif parent[curr][1] ^ parent[nxt][1] ^ lam != 0:
                            odd_cycles += 1
    print(f"{name}: components={comp}, basis_cycles={16 - 8 + comp}, odd_cycles={odd_cycles}")

p29 = [(3,0,'+',0,11),(33,3,'+',26,1),(61,4,'+',24,21),(23,5,'+',26,7),
       (29,14,'+',20,21),(63,7,'-',14,31),(29,10,'-',28,21),(1,13,'+',6,1)]
p79 = [(33,0,'+',0,1),(33,27,'+',10,1),(35,9,'+',26,11),(33,22,'+',20,1),
       (1,18,'+',28,1),(3,13,'+',2,11),(33,12,'+',8,1),(33,7,'+',18,1)]
p89 = [(1,0,'+',0,1),(33,28,'+',8,1),(1,24,'+',16,1),(1,20,'+',24,1),
       (33,16,'+',0,1),(11,13,'+',18,3),(11,24,'+',16,3),(11,3,'-',14,3)]

for name, d in [("p=29", p29), ("p=79", p79), ("p=89", p89)]:
    verify_example(name, d)

def bal(x,n):
    r=x%n; return r-n if r>n//2 else r
def red(p,b,W):
    out=[]
    for w in W:
        d=bal(b*w,p);m=(b*w-d)//p;v=pow(w,-1,32);c=(-2*m*v)%32
        out.append((w%64,m%32,'+' if d>0 else '-',c,v))
    return out
verify_example("HAM8 cexA p=103 (should be odd)", red(103,35,[1505,1481,143,263,227,1445,179,1397]))
verify_example("HAM8 cexB p=1009 (should be odd)", red(1009,500,[449,3161,1353,1167,917,1571,45,699]))
