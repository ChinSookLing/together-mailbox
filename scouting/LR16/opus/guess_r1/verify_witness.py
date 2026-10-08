# Independent check (plain Python, not the engine): each witness row from bgk15 km1low is a cover of the stated size.
import sys,glob,re
def check(p,row):
    n=(p-1)//2; S=sorted(set(row))
    ok=all(any(16*min(v*t%p,p-v*t%p)<p for v in S) for t in range(1,n+1))
    return len(S),ok
for f in sorted(glob.glob("out/wit*.txt")):
    p=int(re.findall(r"wit(\d+)",f)[0]); h=open(f).read().split()[0]
    row=[int(h[2*i:2*i+2],16) for i in range(len(h)//2)]
    print(p,*check(p,row),sorted(set(row)))
