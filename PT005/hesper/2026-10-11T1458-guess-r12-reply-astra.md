BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 15:11 +08
RE: 猜公式 Round 12 (packet c9a646a), send text r12_send_full.txt or r12_send_short.txt
SEAT: astra
MODEL: GPT-6 High (Astra)
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253

--- reply verbatim ---
Assembled by Hesper from browser captures (response Copy failed): prose capture + code captured in pieces from the code pane. Model GPT-6 High, Worked for 5m 35s.

METADATA
- Site: chatgpt.com
- Chat URL: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253
- Chat title: PT005 · Big Picture
- Project: The Civilisation Field
- Model shown: GPT-6 (composer model dropdown: menuitemradio checked=true on "GPT-6"; thinking-effort slider at High/valuenow=2; "High" badge shown)
- Capture method: full-page text extraction (DOM text tree); response-level Copy button was clicked twice but left the clipboard empty (no toast/checkmark observed), so Copy was not used as source.
- Turn confirmed complete: "Response complete" badge present; "Regenerate response" button enabled; no "Connection interrupted" banner in DOM text (find_text returned 0 matches for "interruption"/"interru").
- R12 anchor: "Worked for 5m 35s" + 17 × "Analyzed" badges (this is the R12 response; Round 9's "5m 24s / Analysis paused" badges are a different earlier response).
- Verbatim assembly note: text is reconstructed verbatim from the page's own DOM text (find_text + extract_content near the "5m 35s" anchor). Inline math appears in the DOM as Unicode with interspersed "MathJax alt-text" duplicates (e.g. "U=0 U = 0"); both forms are kept as the page presents them. The Python code lives in a separate InlineCodePane (center 1130,394; scrollable down:3113) that does not contribute its text to extract_content; it is captured from that pane in the CODE appendix below.

VERBATIM R12 REPLY — ANSWER BLOCK
"PT005 · 猜公式 Round 12 ANSWER BLOCK · GPT · The Deficit Curve

Q1 · FACT： 已对 431–499 的全部 13 个素数及 601–1009 的 6 个样本独立搜索、逐格复核。457 找到 𝑈 = 0 U=0；其余得到 𝐷 ( 𝑝 ) D(p) 的严格上界，而非最优性证明。全部速度集合及代码附后。

Q2 · FACT / IDEA： 对 19 个搜索上界做最小二乘拟合： 𝐷 ^ ( 𝑝 ) = − 2.31291 + 0.008590 𝑝 + 0.132407 𝑠 D (p)=−2.31291+0.008590p+0.132407s ，平均绝对误差（MAE）0.490。斜率明显小于随机项 𝑀 ( 𝑝 ) ≈ 0.077 𝑝 M(p)≈0.077p，但不能据此断言真正的 𝐷 ( 𝑝 ) D(p) 增长较慢。

Q3 · IDEA： 泊松极值模型（Poisson Extreme-Value Model）预测： 𝑚 ( 𝑝 ) Pr ⁡ ( P o i s ( 𝑀 ( 𝑝 ) ) ≤ 𝑑 ) ≈ 1 , 𝑚 ( 𝑝 ) = ( 𝑛 14 ) 𝑛 . m(p)Pr(Pois(M(p))≤d)≈1,m(p)= n ( 14 n ) . 大 𝑝 p 时，预测最低遗漏格数约为 𝑀 ( 𝑝 ) − 𝑂 ( 𝑝 log ⁡ 𝑝 ) M(p)−O( plogp )。算术相关性使它不能直接成为定理。

Q4 · UNFINISHED： 尚无严格的 𝛼 > 0 , 𝛽 α>0,β 使 𝐷 ( 𝑝 ) ≥ 𝛼 𝑝 − 𝛽 D(p)≥αp−β。因此无法给出可信的有限 𝑃 0 P 0 。若这样的下界成立， 𝑝 > 𝛽 / 𝛼 p>β/α 已足以排除覆盖，不必另加 Fourier 条件。

Q5 · IDEA：禁算素数预测
𝑝 p  𝐷 ( 𝑝 ) D(p) 预测  置信度
503  2–3  40%
547  2–3  40%
577  2–3  40%
599  2–3  35%
以上根据已拟合系数手算，未对这四个素数运行代码。"

(Continue in append)
```python
=== R12 code-block Copy — head (via code-block-level Copy button, NOT response Copy) ===
Clipboard ends with: A=np.column_stack([np.o…(truncated)
The "(truncated)" is the agent's rendering truncation; actual clipboard extent unknown yet.

import math
import random
import numpy as np

# Search certificates obtained in this round.
# Each list contains 14 distinct speeds.
W = {
431:[14,48,62,90,91,119,152,155,169,183,196,200,209,214],
433:[13,30,67,72,112,123,142,148,157,162,174,198,199,204],
439:[7,16,17,18,68,85,88,119,150,153,187,198,206,218],
443:[13,22,39,100,113,123,126,130,139,152,161,178,182,204],
449:[13,26,52,78,108,140,153,166,179,188,192,195,205,218],
457:[2,35,69,72,77,104,105,136,140,142,174,175,177,212],
461:[16,41,50,57,105,113,125,154,162,170,186,199,203,225],
463:[8,31,36,66,68,98,100,133,134,164,166,183,199,231],
467:[4,12,40,112,117,141,145,149,153,157,165,173,197,219],
479:[17,20,27,47,115,128,142,162,175,179,184,189,209,239],
487:[9,34,94,98,120,125,129,130,145,161,186,213,222,231],
491:[13,28,31,54,70,78,106,119,132,147,160,202,204,225],
499:[7,45,50,64,88,107,121,132,143,149,164,203,221,228],
601:[22,59,81,108,125,152,160,179,206,233,238,255,265,287],
631:[9,32,33,41,98,123,156,164,180,205,206,262,287,303],
701:[3,12,45,158,161,176,185,188,307,334,337,340,343,346],
809:[15,46,61,107,168,183,229,244,275,290,305,336,351,397],
907:[50,75,125,157,166,175,200,216,225,241,275,291,325,441],
1009:[15,74,89,104,163,178,193,282,356,371,386,445,460,475]
}

# Independent exact verification.
def uncovered(p, S):
    H = (p-1)//16
    n = (p-1)//2
    return [
        t for t in range(1,n+1)
        if all(
            min((v*t)%p, p-((v*t)%p)) > H
            for v in S
        )
    ]

# Bitmask acceleration for the search only.
def make_masks(p):
    n=(p-1)//2
    H=(p-1)//16
    masks=[0]*(n+1)
    for v in range(1,n+1):
        mask=0
        for t in range(1,n+1):
            r=(v*t)%p
            if H<r<p-H:
                mask |= 1<<(t-1)
        masks[v]=mask
    return masks

def search(p, iters=1200000, restarts=12, seed=20261011):
    rng=random.Random(seed+p*271)
    masks=make_masks(p)
    n=(p-1)//2
    best=10**9
    bestS=None

    def cost(S):
        z=masks[S[0]]
        for v in S[1:]:
            z &= masks[v]
        return z.bit_count()

    for rr in range(restarts):
        if rr>0 and bestS:
            S=bestS.copy()
            for i in rng.sample(range(14),rng.randrange(3,9)):
                S[i]=rng.randrange(1,n+1)
            if len(set(S))!=14:
                S=rng.sample(range(1,n+1),14)
        else:
            S=rng.sample(range(1,n+1),14)

        current=cost(S)
        if current<best:
            best,bestS=current,S.copy()

        steps=iters//restarts
        for step in range(steps):
            i=rng.randrange(14)
            v=rng.randrange(1,n+1)
            if v in S:
                continue

            j0=0 if i!=0 else 1
            z=masks[S[j0]]
            for j in range(14):
                if j!=i and j!=j0:
                    z &= masks[S[j]]
            new=(z & masks[v]).bit_count()

            delta=new-current
            progress=step/steps
            temp=0.45+3*(1-progress)**2

            if delta<=0 or rng.random()<math.exp(-delta/temp):
                S[i]=v
                current=new
                if current<best:
                    best,bestS=current,S.copy()
                    if best==0:
                        return best,sorted(bestS)

    return best,sorted(bestS)

# Search schedule:
# All listed primes: 1,200,000 proposals, 12 restarts,
# seed 20261011; then 1,800,000 proposals,
# 9 restarts, seed 3220.
# For 457, a further 1,000,000 proposals,
# 10 restarts, seed 42, found U=0.
# Run one prime at a time to keep runs short:
#
# b1,S1 = search(431,1200000,12,20261011)
# b2,S2 = search(431,1800000,9,3220)

ps=sorted(W)
y=np.array([len(uncovered(p,W[p])) for p in ps],float)

for p,val in zip(ps,y):
    assert len(W[p])==14
    assert len(set(W[p]))==14
    assert all(1<=v<=(p-1)//2 for v in W[p])
    print(p,int(val),"PASS")

assert int(y[ps.index(457)])==0

x=np.array(ps,float)
s=np.array([
    (p-1)//2-8*((p-1)//16)
    for p in ps
],float)

A=np.column_stack([np.o…(truncated)

=== END OF HEAD ===
# --- (regression middle, screenshot read) ---
=== R12 code: regression section (from InlineCodePane viewport at scroll up:2463) ===
Source: PT005 Astra chat, R12 Python InlineCodePane, read directly (not via Copy, which truncated at np.column_stack).

x=np.array(ps,float)
s=np.array([
    (p-1)//2-8*((p-1)//16)
    for p in ps
],float)

A=np.column_stack([np.ones(len(x)),x,s])
coef=np.linalg.lstsq(A,y,rcond=None)[0]
pred=A@coef

A0=np.column_stack([np.ones(len(x)),x])
coef0=np.linalg.lstsq(A0,y,rcond=None)[0]

(Next viewport down captures Poisson function header and body.)

=== R12 code: Poisson tail (from pane-at-bottom viewport, prior screenshot) ===

    H=(p-1)//16
    mu=p/2*(1-(2*H+1)/p)**14
    logsets=(
        math.lgamma(n+1)-math.lgamma(15)
        -math.lgamma(n-13)-math.log(n)
    )
    term=math.exp(-mu)
    cdf=term
    for d in range(int(mu)+1):
        if d>0:
            term*=mu/d
            cdf+=term
        if logsets+math.log(cdf)>=0:
            return d
    return None

for p in [431,457,499,601,631,701,809,907,1009]:
    print("Poisson",p,poisson_extreme(p))

print("Ledger bound:",120**14)

GAP BETWEEN THESE TWO SNIPPETS (need Poisson function header + any print/fit-comparison between coef0 and poisson_extreme):
- Need: anything printed after coef0 (e.g. print of coef, MAE comparison, the fitted coefficients that produce −2.312912 / 0.00859008 / 0.13240666)
- Need: def poisson_extreme(p): header and the lines computing n (which must be C(n,14) related)

=== END ===
# --- (bridge, pane read) ---
## R12 Python code — Poisson header bridge (verbatm)
## Source: chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253
## Captured from InlineCodePane viewport at scroll up:2743 (down:370)
## Bridges the regression fit-comparison / print("coefficients") into def poisson_extreme(p): and its n= line,
## then into the already-captured Poisson body (H=(p-1)//16 ...).
## Top row of view is a closing ],…) from the prior list-comprehension; the visible content starts at the
## regression re-statement (A=np.column_stack...), which is a duplicate of what the clipboard Copy already
## delivered. The novel material for assembly is the fit-comparison loop, the coefficients print, the comment,
## the def line, and n=(p-1)//2.

A=np.column_stack([np.ones(len(x)),x,s])
coef=np.linalg.lstsq(A,y,rcond=None)[0]
pred=A@coef

A0=np.column_stack([np.ones(len(x)),x])
coef0=np.linalg.lstsq(A0,y,rcond=None)[0]
pred0=A0@coef0

for name,res in [("p+s",pred),("p only",pred0)]:
    mae=np.mean(abs(y-res))
    rmse=np.sqrt(np.mean((y-res)**2))
    print(name,"MAE",mae,"RMSE",rmse)
print("coefficients",coef)

# Poisson extreme-value model on allowed primes only.
def poisson_extreme(p):
    n=(p-1)//2
    H=(p-1)//16
    mu=p/2*(1-(2*H+1)/p)**14
    logsets=(
    [bottom row cuts off here; the parenthesised logsets expression continues
     on the next line and is captured verbatim in r12_code_poisson_tail.txt as
     "logsets = math.lgamma(n+1)-math.lgamma(15)-math.lgamma(n-13)-math.log(n)"]

NOTE for assembly:
- The lines A=np.column_stack([np.ones(len(x)),x,s]) ... coef= ... pred= ...
  A0= ... coef0= ... pred0= ... are DUPLICATES of what the code-block Copy
  already delivered (they are the "regression setup" that the clipboard returned
  before truncating at np.linalg.lstsq's second occurrence). When assembling,
  KEEP ONLY ONE copy of this block (the clipboard's version).
- The genuinely novel lines in this file that are NOT in the clipboard copy are:
    for name,res in [("p+s",pred),("p only",pred0)]:
        mae=np.mean(abs(y-res))
        rmse=np.sqrt(np.mean((y-res)**2))
        print(name,"MAE",mae,"RMSE",rmse)
    print("coefficients",coef)

    # Poisson extreme-value model on allowed primes only.
    def poisson_extreme(p):
        n=(p-1)//2
- The line "H=(p-1)//16" and everything below it are the Poisson body captured
  separately in r12_code_poisson_tail.txt (which starts at H=(p-1)//16).
# --- (tail, pane read) ---
## R12 Python code — Poisson tail (verbatm)
## Source: chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253
## Captured from InlineCodePane's absolute bottom viewport (pane scrollable="up:3113" only,
## no downward scroll remaining — this IS the end of the code block).
## This replaces a previously saved Poisson tail that had the CDF-guard indented under
## `if d>0:`. The ACTUAL code runs `logsets+math.log(cdf)>=0` on every iteration of d,
## including d=0 (same indent as `if d>0:`), and the bottom-viewport read confirms this.
## The function header (def poisson_extreme, n=(p-1)//2) is in r12_code_poisson_header_bridge.txt;
## the `H=(p-1)//16` line at the top of this file overlaps the bottom of that bridge and
## the prior-session Poisson body — keep only one copy when assembling.

    H=(p-1)//16
    mu=p/2*(1-(2*H+1)/p)**14
    logsets=(
        math.lgamma(n+1)-math.lgamma(15)
        -math.lgamma(n-13)-math.log(n)
    )
    term=math.exp(-mu)
    cdf=term
    for d in range(int(mu)+1):
        if d>0:
            term*=mu/d
            cdf+=term
        if logsets+math.log(cdf)>=0:
            return d
    return None

for p in [431,457,499,601,631,701,809,907,1009]:
    print("Poisson",p,poisson_extreme(p))

print("Ledger bound:",120**14)

## ASSEMBLY notes
## - The CDF-guard `if logsets+math.log(cdf)>=0:` is at the SAME indent level as
##   `if d>0:` (i.e., both are direct children of `for d in range(int(mu)+1):`).
##   It is NOT nested under `if d>0:`. This means the threshold test fires on d=0 too.
## - `return None` is at function-body indent (one level up from the for-loop),
##   executed only if the loop finishes without triggering the guard.
## - The driver loop iterates 9 primes (431..1009) and prints "Poisson", p, result.
## - `print("Ledger bound:",120**14)` is the last statement in the entire code block;
##   nothing follows it.
## - The line H=(p-1)//16 appears at the top of this file AND at the bottom of
##   r12_code_poisson_header_bridge.txt. It is the join seam; keep a single copy.```

Q5 (captured): D̂ = −2.312912 + 0.00859008·p + 0.13240666·s → 503 (s=3) 2.405, 547 (s=1) 2.518, 577 (s=0) 2.644, 599 (s=3) 3.230 — all bucket 2–3.
STATUS：Q1、Q2 数值已完成并复核；Q3 为模型；Q4 UNFINISHED；Q5 为未计算考试素数的盲预测。

--- end verbatim ---
END LETTER
