exec(open('check_puck.py').read().split('gpt=[')[0])
ex=[3,261,251,381,253,315,125,131]
print('ex tiles C6(12)',tiles(ex,6,12),'C5(6) of red',tiles([w%544 for w in ex],5,6))
O2={3,5,6,7,10,11,12,14}
print('ex mod17',[w%17 for w in ex],'in O2',[w%17 in O2 for w in ex])
