exec(open('check_puck.py').read().split('gpt=[')[0])
v2=[47,321,7,293,37,19,39,129]
print('v2 legal',all(legal(w) for w in v2),'tiles C5(6)',tiles(v2,5,6),[w%17 for w in v2])
N=544;T=cls(N,6);print('T',sorted(T))
for w in v2: print(w,sorted(cov(w,N,T)))
print('v2 lifts to C6(12):',len(lifts(v2,5,6)))
v1=[123,643,189,61,573,771,59,635]
r=[w%544 for w in v1]
print('v1 red',r,'legal',all(legal(w) for w in v1),'tiles C5(6)',tiles(r,5,6),'lifted tiles C6(12)',tiles(v1,6,12))
print('v1 mod17',[w%17 for w in v1],'red mod17',[w%17 for w in r])
