import sys,collections
exec(open('mixed.py').read().split('k=int(sys.argv[1])')[0])
exec(open('check_puck.py').read().split('gpt=')[0])
def v2(w):
    v=0
    while w%2==0: w//=2;v+=1
    return v
k=int(sys.argv[1]); b=int(sys.argv[2])
nc,f=runm(k,b,2)
print("k",k,"b",b,"mixed doublings",len(f))
ex=f[0]; N=17*2**k
print("example",ex,"tiles k",tiles([w%N for w in ex],k,b),"tiles k+1",tiles(ex,k+1,2*b%17))
c=collections.Counter((min(map(v2,x)),max(map(v2,x)),len(x)) for x in f)
print("(vmin,vmax,#coords):count",sorted(c.items()))
