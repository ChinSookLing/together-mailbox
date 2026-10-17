from chk import *
import chk
p=23
X=[10,26,28,56,78,94,95,99,100,121,122,142,146,162,172]; Y=[26,28,94,95,99,100,142,146,162,194,240,262,305,306,356]
print('X open',is_open(X,184),'F1',Fj(X,184,p,1),'F3',Fj(X,184,p,3))
print('Y open',is_open(Y,368),'F1',Fj(Y,368,p,1),'F3',Fj(Y,368,p,3), 'Y mod 184 sorted == X', sorted(y%184 for y in Y)==sorted(X))
oc=open_children(X,184); print('X open children',len(oc))
