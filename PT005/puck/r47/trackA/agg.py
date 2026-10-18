import collections, gzip
C=collections.Counter(); byp=collections.Counter(); minEd=collections.Counter(); k2712=collections.Counter(); pairdead=collections.Counter()
n=0
for line in gzip.open('per_node_r47.tsv.gz','rt'):
    if line.startswith('csv_line'): continue
    a=line.rstrip('\n').split('\t'); n+=1
    p,M,surv,nopen=int(a[1]),int(a[2]),int(a[3]),int(a[4])
    if a[5]=='NA': C[('oddM',)]+=1; continue
    cert=int(a[5]); minE=int(a[7]); E0=int(a[9]); pair=int(a[10]); ca=int(a[11]); cc=int(a[12])
    s0 = surv==0
    C[('cert',cert,'surv0',s0)]+=1
    byp[(p,cert,s0)]+=1
    if not cert: minEd[(s0,minE)]+=1
    if not cert and s0: pairdead[('has_pair_t',pair>0,'E0',E0)]+=1
    if ca==32768 and cc==0: k2712[('cert',cert)]+=1
print('rows',n)
for k,v in sorted(C.items(),key=str): print(k,v)
print('-- by p (p,cert,surv0)'); [print(k,v) for k,v in sorted(byp.items())]
print('-- no cert: (surv0, minE) counts'); [print(k,v) for k,v in sorted(minEd.items())]
print('-- no cert & surv0: pair/E0'); [print(k,v) for k,v in sorted(pairdead.items(),key=str)]
print('-- 2712 all-pass-but-dead group:',dict(k2712))
