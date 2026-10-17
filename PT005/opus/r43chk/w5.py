from own import *
p=17; W=[189,224,72,447,176,500,144,128,384,266,80,64,48,32,16]; M=32*p
print("W5 open",is_open(W,M),fstats(W,M,p))
ch=open_children(W,M); print("open children at 64p:",len(ch))
from collections import Counter
print("F3 of children:",Counter(fstats(c,2*M,p)['F3'] for c in ch), "E:",Counter(fstats(c,2*M,p)['E'] for c in ch))
g=sum(len(open_children(c,2*M)) for c in ch); print("open grandchildren at 128p:",g)
