# Is the Argon doublability test invariant under (a) v -> 32-v on one footprint, (b) twin (c,v)->(c+16,v+16) on one footprint?
import json
D=json.load(open('../../../hesper/r38/checks/r38_doublable_only.json'))
def kmap(c,v): return {(c+d*v)%32:((c+d*v)%32-c-d*v)//32 for d in (1,-1,3,-3)}
def dbl(conf):
    occ={}
    for a,(c,v) in enumerate(conf):
        for s,k in kmap(c,v).items(): occ.setdefault(s,[]).append((a,k))
    piv={}
    for s,((a,ka),(b,kb)) in occ.items():
        vec=(1<<a)|(1<<b); l=(1+ka+kb)&1
        while vec:
            h=vec.bit_length()-1
            if h in piv: pv,pl=piv[h]; vec^=pv; l^=pl
            else: piv[h]=(vec,l); break
        if vec==0 and l: return False
    return True
negflip=twinflip=tot=0
for conf in D:
    conf=[tuple(x) for x in conf]
    for i in range(8):
        c,v=conf[i]; tot+=1
        a=conf[:i]+[(c,32-v)]+conf[i+1:]
        b=conf[:i]+[((c+16)%32,(v+16)%32)]+conf[i+1:]
        negflip+= not dbl(a); twinflip+= not dbl(b)
print('single-footprint replacements tested',tot,'; v->32-v breaks doublability:',negflip,'; twin swap breaks:',twinflip)
