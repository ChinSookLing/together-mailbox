import sys,json
exec(open('/workspace/work/r4search.py').read().split('p=int')[0])
def U(p,S):
    H=(p-1)//16
    return sum(all(min((v*t)%p,p-(v*t)%p)>H for v in S) for t in range(1,p))//2
out=[]
for p in [307,337,383,431,457,461,499]:
    F,M=setup(p)
    res=sorted(anneal(p,60000,s,F,M) for s in range(40))
    b=res[0]
    out.append(dict(p=p,M=round(M,3),bestR4=round(float(b[0]),3),set=b[1],U=U(p,b[1]),top5=[round(float(r),3) for r,_ in res[:5]]))
    print(out[-1],flush=True)
json.dump(out,open('r4run_out.json','w'))
