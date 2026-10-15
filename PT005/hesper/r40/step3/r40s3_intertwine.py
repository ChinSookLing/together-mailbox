import sys; sys.argv=['x']
__file__='/workspace/work/together-mailbox/PT005/hesper/r39/checks_r16.py'; exec(open('checks_r16.py').read().split('# Domino lemma')[0].replace('for beta in (0,1):','for beta in ():'))
def tau(k,t): return tuple(sorted(canon(c+2*t,v) for c,v in k))
def mul(k,a): return tuple(sorted(canon(a*c,a*v) for c,v in k))
bad=tot=0
for k in MD:
    for t in range(16):
        for beta in (0,1):
            tot+=1; bad+= r16(tau(k,t),beta)!=r16(k,(beta+t)%2)
print("intertwine cases",tot,"mismatches",bad)
ba=0
for k in MD:
    for a in (3,5,7,9,11,13,15,17,19,21,23,25,27,29,31):
        for beta in (0,1): ba+= r16(mul(k,a),beta)!=r16(k,beta)
print("multiplier invariance mismatches",ba)
agree=sum(r16(k,0)==r16(k,1) for k in MD); print("beta agree",agree,"of",len(MD))
