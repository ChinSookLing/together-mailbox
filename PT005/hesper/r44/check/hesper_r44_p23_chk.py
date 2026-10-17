from hesper_r44_p19_chk import *
M=184
X=[10,26,28,56,78,94,95,99,100,121,122,142,146,162,172]
Y=[26,28,94,95,99,100,142,146,162,194,240,262,305,306,356]
print("X open",is_open(X,M),"F1",F(X,M,1),"F3",F(X,M,3))
ch=children_open(X,M); print("X open children",len(ch))
print("Y in children",tuple(sorted(Y)) in ch,"Y open",is_open(Y,2*M),"F1",F(Y,2*M,1),"F3",F(Y,2*M,3),"Y mod 184 = X",sorted(y%M for y in Y)==sorted(X))
g=children_open(Y,2*M); print("Y open children",len(g))
