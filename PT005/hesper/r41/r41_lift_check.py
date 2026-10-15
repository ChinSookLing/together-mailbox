import json,os,itertools
here='/workspace/work/together-mailbox/PT005/hesper/r39'
R=[tuple(tuple(x) for x in k) for k in json.load(open(os.path.join(here,'../r38/checks/hesper_U_769.json')))]
def lift(k,beta):
    S=frozenset(s for s in range(32) if s%2==(beta+1)%2)
    O=[]
    for c,v in k:
        o=set()
        for c2 in (c//2, c//2+16):   # both half-centres mod 32 (lift bit)
            if (c//2)%2==beta: o.add(frozenset({(c2-v)%32,(c2+v)%32}))
            else:
                for e in (1,-1): o.add(frozenset({c2%32,(c2+2*e*v)%32}))
        O.append([x for x in o if len(x)==2])
    def rec(i,used):
        if i==8: return used==S
        return any(not(e&used) and rec(i+1,used|e) for e in O[i])
    return rec(0,frozenset())
fails=[(k,b) for k in R for b in (0,1) if not lift(k,b)]
print("640-set size",len(set(R)),"lift checks",2*len(R),"fails",len(fails))
