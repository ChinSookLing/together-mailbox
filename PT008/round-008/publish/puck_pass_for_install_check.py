# Puck PASS FOR INSTALL check for T4-PUBLICATION.md (exact, no floats)
import hashlib,re,random
from fractions import Fraction as F
pub=open("T4-PUBLICATION.md").read(); man=open("../PT-008-R008-OPUS-T4-MANUSCRIPT.md").read()
res=[]
def ok(n,c): res.append((n,bool(c)))
ok("manuscript sha256 = 4720413d…",hashlib.sha256(man.encode()).hexdigest().startswith("4720413d78955ea0"))
for a,b in [("### A0 记号","### A6"),("### A6","---\n\n## SECTION B"),("### B0 情形穷尽","### B10"),("1. **定义域**","7. **作者自测"),("7. **作者自测","---\n\n## SECTION D")]:
    i=man.index(a); s=man[i:man.index(b,i)].rstrip(); ok("verbatim section "+a[:12],s in pub)
rows=re.findall(r"^\| ([1-8]) \| \*\*(\S+)\*\* \|",pub,re.M)
ok("eight branches in exact order",[r[1] for r in rows]==["S1","S2","S3","B3","B2","B4","B5","S6-A"] and [r[0] for r in rows]==list("12345678"))
for need in ["Internally verified, not externally peer-reviewed","PROVED — PT-008 internal proof certification","Opus (Claude)","DeepSeek","Gemini 3.1 Pro","1c510ce","b6bea7b","Puck","Hesper","GPT-6","7aa8daa","does not prove the general Lonely Runner Conjecture","Literature originality","is not new","B4(iv), case j = 0","Correct label: B2","not a substitute for it"]:
    ok("contains: "+need,need in pub)
# extract and run reference implementation from the publication
code=pub[pub.index("```python")+9:pub.index("```",pub.index("```python")+9)]
ns={}; exec(code,ns); F4=ns["F4"]; d=ns["d"]
def good(a,b,c):
    t=F4(a,b,c); return t>0 and min(d(a*t),d(b*t),d(c*t))>=F(1,4)
ex=[((1,2,3),F(1,4)),((1,2,6),F(3,8)),((1,3,4),F(3,7)),((2,4,7),F(2,11)),((1,F(5,2),F(16,5)),F(10,19)),((1,F(3,2),F(16,5)),F(20,47)),((1,F(12,5),4),F(5,16)),((1,2,F(16,5)),F(5,7)),((1,F(29,10),F(59,10)),F(5,11)),((1,F(29,10),F(17,2)),F(25,57))]
ok("manuscript example table times reproduce",all(F4(*map(F,v))==t for v,t in ex))
ok("DeepSeek boundary (3/2,3,5) -> t=1/4 (B2)",F4(F(3,2),F(3),F(5))==F(1,4) and good(F(3,2),F(3),F(5)))
random.seed(20261018); fails=0; N=30000
for _ in range(N):
    xs=sorted({F(random.randint(1,4000),random.randint(1,300)) for _ in range(3)})
    if len(xs)<3: continue
    if not good(*xs): fails+=1
# boundary points of the branch conditions
bd=0
for a in [F(1)]:
  for c in [F(3),F(3)+F(1,997)]+[F(k,7) for k in range(8,90)]:
    for r in [F(7,5),F(5,3),F(9,7),F(11,5),F(13,7),F(3),F(3,2)]:
      b=c/r
      if a<b<c:
        bd+=1
        if not good(a,b,c): fails+=1
ok(f"random exact inputs ({N}) + {bd} boundary points: 0 failures",fails==0)
sha=hashlib.sha256(pub.encode()).hexdigest()
allok=all(c for _,c in res)
for n,c in res: print(("PASS " if c else "FAIL ")+n)
print("T4-PUBLICATION.md sha256",sha)
print("VERDICT:","PASS FOR INSTALL" if allok else "HOLD")
