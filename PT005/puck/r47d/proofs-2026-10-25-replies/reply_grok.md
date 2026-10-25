Puck: R47D proof-read reply, seat=grok, chat PT-005(2) (Astra: standing chat), collected 2026-10-25 11:47 +08 via copy button, verbatim below. Attachments (.py/.json) not copied.
---
**ANSWER BLOCK**  
C1: SURVIVED  
C2: BROKEN  
C3: SURVIVED  
C4: SURVIVED  
C5: BROKEN  
C6: SURVIVED  

Least-sure: C5 exact class count (L undefined; density not uniformly ~1/4).  

C1 holds by direct scaling: \(\|Tw'\|_{2^d p}/(2^d p)=2^{-3}\).  

C2 broken. Cover at \(M\) is \(16\|Tw\|_M<M\). With \(w=2^{k-d}w'\) this is exactly \(\|Tw'\|_{2^d p}<2^{d-4}p\). Reach at level \(2M\) (where the same coordinate has depth \(d+1\)) requires \(\|Tw'\|_{2^{d+1}p}<2^{d-2}p\). Counter-example (\(p=3\), \(d=4\), \(T=1\), \(w'=47\)):  
```python
def dist(x,m): r=abs(x)%m; return min(r,m-r)
print(dist(1*47,48), dist(1*47,96))  # 1 < 3, but 47 ≱ 12
```  
Small-mod distance 1 satisfies cover; large-mod distance 47 fails reach. (Odd multiple of the small modulus pushes the residue near half the large modulus.) The “unit-time covered by \(i\) alone \(\Rightarrow\) stricter bound” therefore does not force the higher-level reach.  

C3 holds for \(d\le 3\). If \(p\mid T\) or \(p\mid w'\) then \(\|Tw'\|_{2^d p}=p\cdot\|odd\|_{2^d}\). The reduced distance is an integer \(\ge 1\) (product of two odds). The threshold factor \(2^{d-3}\le 1\), so the inequality is impossible. At \(d=4\) the threshold becomes \(2p>p\), reduced distance 1 is allowed, and examples exist (e.g. \(p=3\), \(T=3\), \(w'=1\)). This is precisely why the \((M2)\) boundary sits at depth 4.  

C4 survived extensive search (hundreds of pairs, several \((d,p,w')\)); the stated modular condition on \(T_2-T_1\) matched \(h_i(T_1)\ne h_i(T_2)\) whenever both values were defined.  

C5: dependence on \(T\bmod 2^{d+1}p\) for \(d_j\le d+1\) is immediate (the reach modulus divides the claimed modulus). The density claim is false: for \(d_j=d+2\) the proportion of odd lifts is exactly \(1/2\), not \(\approx 1/4\). Concrete count (\(d=3\), \(d_j=5\), \(p=3\), \(k=9\), base \(T=1\), \(w'=1\)): 16 reaches out of 32 lifts. Higher excess sometimes yields \(1/4\), sometimes other dyadic fractions; “exactly \(2^{L-2}\)” cannot be verified without a definition of \(L\), but the uniform “about \(1/4\)” already fails.  

C6 is correct: C1–C2 alone give only a per-coordinate bound; interactions among the remaining coordinates (needed for any global depth-rarity statement about \((M2)\)) are not controlled. The \(d=4\) threshold supplies the natural boundary but does not by itself produce the rarity law.