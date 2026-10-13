import sys; sys.argv=['x']
exec(open('/workspace/work/r21/verify_64p.py').read().split('c32=children')[0].replace('p=37','p=17'))
p=17
W5=[189,224,72,447,176,500,144,128,384,266,80,64,48,32,16]
def improper(w,N):
    full=(1<<(N//2+1))-2; c=0
    for x in w: c|=covint(x,N)
    return c==full and sum(x%2 for x in w)>=2
print("W5 improper@32p",improper(W5,32*p),"L7@32p",l7(W5,32*p))
ch=children(W5,32*p); bad=[w for w in ch if l7(w,64*p) is None]
print("64p children",len(ch),"fail L7",len(bad))
g=sum(len(children(w,64*p)) for w in bad)
print("128p improper descendants of failing",g)
