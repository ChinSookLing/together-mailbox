# Puck exact-Fraction check of the numeric examples and new inequality claims in the
# DeepSeek (1c510ce) and Gemini (b6bea7b) independent T4 reviews, PT-008 R008.
from fractions import Fraction as F
import math
def d(x): x=x-math.floor(x); return min(x,1-x)
def chk(name,a,b,c,t,want=None):
    ds=[d(a*t),d(b*t),d(c*t)]
    ok=t>0 and all(x>=F(1,4) for x in ds) and (want is None or ds==want)
    print(f"{name}: a,b,c={a},{b},{c} t={t} dists={[str(x) for x in ds]} r=c/b={c/b} s=(b+c)/a={(b+c)/a} -> {'OK' if ok else 'FAIL'}")
    return ok
res=[]
res.append(chk("DeepSeek S2 (1,2,6)",F(1),F(2),F(6),F(3,8),[F(3,8),F(1,4),F(1,4)]))
res.append(chk("DeepSeek 'B4 boundary' (3/2,3,5) with t=1/2",F(3,2),F(3),F(5),F(1,2),[F(1,4),F(1,2),F(1,2)]))
res.append(chk("Same point under T4 order (B2 first, r=5/3), t=1/4 per Hesper",F(3,2),F(3),F(5),F(1,4),[F(3,8),F(1,4),F(1,4)]))
a,b,c=F(1),F(21,10),F(63,20); t=3/(a+c)
res.append(chk("DeepSeek G/S6-A (1,21/10,63/20), t=3/(a+c)",a,b,c,t,[F(23,83),F(40,83),F(23,83)]))
assert t==F(60,83)
a,b,c=F(1),F(31,15),F(31,10); t=3/(a+c)
res.append(chk("Gemini G/S6-A (1,31/15,31/10), t=3/(a+c)",a,b,c,t,[F(11,41),F(20,41),F(11,41)]))
assert t==F(30,41) and F(7,5)<c/b<F(5,3) and (b+c)/a<F(16,3)
# Gemini B4(iv) identity: for a<=b/3, b(b+c)-a(5b+c) >= (2/3) b (c-b); grid check + symbolic note
import itertools
bad=0;n=0
for an,bn,cn in itertools.product(range(1,25),range(1,60),range(1,120)):
    a,b,c=F(an,4),F(bn,4),F(cn,4)
    if b>=3*a and c>b:
        n+=1
        lhs=b*(b+c)-a*(5*b+c); rhs=F(2,3)*b*(c-b)
        if not (lhs>=rhs>0): bad+=1
print(f"Gemini B4(iv) chain b(b+c)-a(5b+c) >= (2/3)b(c-b) > 0 on b>=3a, c>b: {n} grid cases, {bad} failures")
print("  symbolic: a<=b/3 and 5b+c>0 give b(b+c)-a(5b+c) >= b^2+bc-(5b^2+bc)/3 = (2/3)b(c-b)")
res.append(bad==0)
# Gemini G-region bound: r<5/3 and s<16/3 => c<10a/3
bad=0;n=0
for an,bn,cn in itertools.product(range(1,13),range(1,80),range(1,80)):
    a,b,c=F(an,3),F(bn,6),F(cn,6)
    if F(7,5)<c/b<F(5,3) and (b+c)/a<F(16,3):
        n+=1
        if not c<F(10,3)*a: bad+=1
print(f"Gemini G bound (r<5/3, s<16/3 => c<10a/3): {n} grid cases, {bad} failures")
res.append(bad==0)
# DeepSeek B4(iv) j=0 remark: j*eta=0 trivially satisfies any nonnegative upper bound (wording gap only)
print("DeepSeek B4(iv) j=0 remark: j*eta = 0 meets the same upper bound; wording fix, not a gap (agree)")
print("ALL OK" if all(res) else "SOME FAIL")
