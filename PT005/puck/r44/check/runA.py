from chk import *
A=[1,3,3,5,7,8,18,22,40,55,69,75,87,105,110]; Ac=[1,3,5,7,8,69,75,87,139,154,158,176,191,241,246]
print('A open',is_open(A,136),'child open',is_open(Ac,272))
oc=open_children(A,136); print('A open children',len(oc), any(sorted(c)==sorted(Ac) for c in oc))
