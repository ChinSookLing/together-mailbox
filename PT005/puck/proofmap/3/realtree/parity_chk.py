import numpy as np
from puck_tree import fibre_ok, odd_count, canon
for lab,w,p in [("p131a",[1,1,1,2,8,11,18,38,40,46,47,48,56,58,1],131),("p131b",[1,1,1,2,8,11,18,38,40,46,47,48,56,58,2],131),("p47",[1,2,3,5,6,8,9,10,11,12,13,14,15,20,21],47)]:
    M=p; oks=fibre_ok(w,M,p); a=np.ones(1<<15,bool)
    for o in oks.values(): a&=o
    kids=[[x+((int(m)>>i)&1)*M for i,x in enumerate(w)] for m in np.nonzero(a)[0]]
    bad={canon(s,2*M):s for s in kids if odd_count(s)<2}
    print(lab,"distinct parity<2 kids at 2p:",len(bad),[ (odd_count(s),s) for s in bad.values()])
