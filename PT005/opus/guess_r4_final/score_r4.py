# Round 4 final scoring: interval hits and point log-errors. Predictions transcribed from PT005/hesper/2026-10-09T16*/17*-guess-r4-reply-*.md
from math import log10
actual={'307r':11677696,'307l':6909,'337r':7325187,'337l':1832,'383r':5171,'383l':2}
# 307/383 hits from note 63; 337 ranges and points from the replies
hits63={'GPT':4,'Astra':4,'Grok':3,'Kimi':3,'GLM':3,'DeepSeek':2,'Qwen':2,'Gemini':1,'Lumo':1}
r337={'GPT':((7e5,2e7),(100,8000)),'Astra':((8e5,3e7),(100,1e4)),'Grok':((1.5e6,6e6),(100,4000)),
 'Kimi':((1e6,1e7),(50,5000)),'GLM':((5e5,5e7),(10,2e4)),'DeepSeek':((2e5,2e6),(50,1000)),
 'Qwen':((1e5,1e6),(10,1000)),'Gemini':((2e6,2e7),(100,1000)),'Lumo':((1.5e8,7e8),(5000,5e5))}
pts337={'GPT':(5e6,1500),'Astra':(6e6,1500),'Grok':(3.2e6,700),'Kimi':(3e6,700),'GLM':(5e6,500),'Lumo':(3e8,1e5)}
print("seat  337rows 337L2  total/6")
for s,(R,Lr) in r337.items():
    a=R[0]<=actual['337r']<=R[1]; b=Lr[0]<=actual['337l']<=Lr[1]
    print(f"{s:9s} {'Y' if a else 'N'} {'Y' if b else 'N'}  {hits63[s]+a+b}/6")
print("337 point log10 errors (rows, L2):")
for s,(x,y) in pts337.items(): print(f"  {s:6s} {abs(log10(x/actual['337r'])):.3f} {abs(log10(y/actual['337l'])):.3f}")
gpt=[1e7,6000,5e6,1500,3e4,2]; ast=[1.5e7,8000,6e6,1500,2e4,2]
keys=['307r','307l','337r','337l','383r','383l']
for n,v in (('GPT',gpt),('Astra',ast)): print(n,'mean |log10 err| over 6 =',round(sum(abs(log10(v[i]/actual[k])) for i,k in enumerate(keys))/6,4))
