from chk import *
import chk
p=19
path=[(19,[1,2,3,4,5,6,7,8,9,11,12,15,16,17,18]),
(38,[1,21,3,23,5,25,7,8,9,11,31,15,35,17,37]),
(76,[39,59,41,61,43,25,45,8,47,49,69,15,73,55,37]),
(152,[39,59,41,61,43,101,121,8,47,125,145,15,73,55,37]),
(304,[191,59,41,213,195,101,121,160,47,125,145,15,73,207,37])]
for (M,w),nxt in zip(path,path[1:]+[None]):
    leg = nxt is None or all(b in (a,a+M) for a,b in zip(w,nxt[1]))
    print(M,'open',is_open(w,M),'cov',covered_all(w,M),'odd',sum(x%2 for x in w),'L7',l7_closed(w,M),'F1',Fj(w,M,p,1),'F3',Fj(w,M,p,3),'legal->next',leg)
M,w=path[3]
oc=open_children(w,M); print('open children of 152 parent:',len(oc)); [print(c,'F3',Fj(c,304,p,3)) for c in oc]
for c in oc:
    print('grandchildren open of',c[:4],'...:',len(open_children(c,304)))
