def cov(t,w,N):
    r=t*w%N; return 16*min(r,N-r)<N
for p,b,W,W6 in [(79,76,[865,993,675,289,385,579,545,673],[865,3521,675,289,2913,3107,3073,673]),(89,36,[1345,545,1089,129,673,587,139,1035],None)]:
    N5=32*p;N6=64*p
    print('p',p,'legal',all(w%2 and w%p not in(0,1,p-1) and w<16*p for w in W),'mod8',[w%8 for w in W])
    T5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
    c5=[sum(cov(t,w,N5) for w in W) for t in T5]; print(' k5 members',len(T5),'counts',set(c5))
    # also check full 32p range
    T5f=[t for t in range(1,32*p,2) if t%p in (b%p,(-b)%p)]
    print(' k5 full-range counts',set(sum(cov(t,w,N5) for w in W) for t in T5f))
    T6=[t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
    from itertools import product
    sols=[]
    for E in product((0,1),repeat=8):
        L=[w+32*p*e for w,e in zip(W,E)]
        if all(sum(cov(t,w,N6) for w in L)==1 for t in T6): sols.append(L)
    print(' k6 members',len(T6),'exact lifts',len(sols),sols[:2])
    if W6: print(' given W6 ok', all(sum(cov(t,w,N6) for w in W6)==1 for t in T6))
    # check other t (non-member) not needed; check b vs p range
    print(' b',b,'b<p',b<p,'2b mod p',2*b%p)
print('--- 2-cover check')
for p,b,W in [(79,76,[865,993,675,289,385,579,545,673]),(89,36,[1345,545,1089,129,673,587,139,1035])]:
    N6=64*p
    T6=[t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
    cnt=[sum(cov(t,w,N6)+cov(t,w+32*p,N6) for w in W) for t in T6]
    per=[(sum(cov(t,w,N6) for t in T6),sum(cov(t,w+32*p,N6) for t in T6)) for w in W]
    print(p,'member cover counts',sorted(set(cnt)),'per-lift',per)
for p,b,W in [(79,76,[865,993,675,289,385,579,545,673]),(89,36,[1345,545,1089,129,673,587,139,1035])]:
    T5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
    print(p,[sum(cov(t,w,32*p) for t in T5) for w in W], len(set(W)))
