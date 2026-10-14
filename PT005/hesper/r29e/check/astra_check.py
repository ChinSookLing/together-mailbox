import re
t=open('together-mailbox/PT005/hesper/r29e/send_R29e_L.txt').read()
cases=[]
for m in re.finditer(r'b=(\d) c0=(\d) ws=\[([^\]]*)\] mult4=(\[[^\]]*\]) \| (.*?) ; (.*?) \| type',t):
    b,c=int(m[1]),int(m[2]); ws=list(map(int,m[3].split(','))); m4=eval(m[4])
    cyc=[]
    for s in (m[5],m[6]):
        path,lab=s.split(' labels ')
        cyc.append((list(map(int,path.split('-')))[:4],eval(lab)))
    cases.append((b,c,ws,m4,cyc))
print(len(cases))
I17=lambda x:pow(x,-1,17)
ok_norm=ok_pair=ok_cyc=0; res=[]
for b,c,ws,m4,cyc in cases:
    # normalize
    wn=[w if (b*w)%17==7 else (544-w if (b*(544-w))%17==7 else None) for w in ws]
    if None not in wn: ok_norm+=1
    a=[w%32 for w in wn]
    if all((a[i]+a[j])%32==0 for i,j in m4): ok_pair+=1
    good=True
    for path,lab in cyc:
        for k in range(4):
            i,j=path[k],path[(k+1)%4]
            if not (a[j]==(7*a[i])%32 or a[i]==(7*a[j])%32): good=False
    if good: ok_cyc+=1
    # H formula on each cycle: orient so a_{j+1}=7a_j
    for path,lab in cyc:
        if a[path[1]]!=(7*a[path[0]])%32: path=path[::-1]; lab=[lab[3],lab[2],lab[1],lab[0]]
        if a[path[1]]!=(7*a[path[0]])%32: res.append(('noorient',b,c)); continue
        hs=[]
        for k in range(4):
            wj,wj1=wn[path[k]],wn[path[(k+1)%4]]
            M=(wj1-7*wj)
            assert M%32==0; M//=32
            # t mod 544: t≡2b mod17, t≡-5a-1 mod 32
            aj=wj%32
            tt=[x for x in range(544) if x%17==(2*b)%17 and x%32==(-5*aj-1)%32][0]
            num=tt*M-8
            hs.append((num%17==0, (1+num//17)%2 if num%17==0 else None))
        res.append((b,c,lab,hs,sum(lab)%2))
print('norm',ok_norm,'pairs a,-a',ok_pair,'cycles a->7a',ok_cyc)
for r in res: print(r)
