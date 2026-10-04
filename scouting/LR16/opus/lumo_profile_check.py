# Chair check (scouting) of Lumo's "short-relation profile" idea, PT005 line 22.
# Question: does the set of short relations {c in {-1,0,1}^15 : c.v = 0 mod p} already pin v down
# up to a unit multiple? If yes, every unit orbit has its own profile and grouping by profile compresses nothing.
import itertools, random
import numpy as np
def short_relations(v, p, half=7):
    k = len(v); A, B = v[:half], v[half:]
    left = {}
    for ca in itertools.product((-1,0,1), repeat=len(A)):
        s = sum(c*x for c,x in zip(ca,A)) % p
        left.setdefault(s, []).append(ca)
    rels = []
    for cb in itertools.product((-1,0,1), repeat=len(B)):
        s = (-sum(c*x for c,x in zip(cb,B))) % p
        for ca in left.get(s, ()):
            c = ca + cb
            if any(c): rels.append(c)
    return rels
def rank_mod_p(M, p):
    M = [list(r) for r in M]; rank = 0; cols = len(M[0])
    for col in range(cols):
        piv = next((r for r in range(rank, len(M)) if M[r][col] % p), None)
        if piv is None: continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col] % p, p-2, p)
        M[rank] = [(x*inv) % p for x in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col] % p:
                f = M[r][col]; M[r] = [(a - f*b) % p for a,b in zip(M[r], M[rank])]
        rank += 1
    return rank
random.seed(7)
for p in (239, 307, 601):
    for trial in range(2):
        v = [random.randrange(1, p) for _ in range(15)]
        rels = short_relations(v, p)
        sample = random.sample(rels, min(400, len(rels)))
        r = rank_mod_p(sample, p)
        print(f"p={p} v[:4]={v[:4]}... short relations with c_i in {{-1,0,1}}: {len(rels)} (3^15/p = {3**15//p}); "
              f"rank mod p of 400 of them = {r} -> solution space dim {15-r} ({'v fixed up to a unit' if r==14 else 'not fixed'})")
