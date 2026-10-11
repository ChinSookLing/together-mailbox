BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 15:46 +08
RE: 猜公式 Round 13 (packet 2e9272a), send text r13_send_full.txt or r13_send_short.txt
SEAT: deepseek
MODEL: DeepSeek DeepThink
CHAT: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202

--- reply verbatim ---
DeepThink ON, Search OFF. Captured page text; the visible text begins with the tail of DeepThink's reasoning, then the ANSWER BLOCK.

(Header shown on the reply card: "Thought for 19 seconds")

Another: Section 二 PROOF "线性门槛上限 | 「a − bp − cs > 0」型规则在 33 个素数上最多对 30 个（前提 c ≥ 0） | GLM（R8）". This is a computational result, not a proof. It says "PROOF" but it's a finite check. Could be FACT.
Another: Section 三 FACT "14 类覆盖普查 307–499（33 个素数） | 办公室电脑，作者引擎 | 正面计数：主席另写程序，在 347、349、367、379、389、401 找到的覆盖数与普查完全相同；零的一面只靠作者引擎". This is correctly labeled FACT but note zero side only one source. Not error.
Another: Section 四 FORMULA "泊松计数公式... p 每增加 16，覆盖数约乘 0.3." Is that correct? If M(p) ~ 0.077p, then e^{-κU} with U ~ M. If p increases by 16, M increases by ~1.23. e^{-κ*1.23}. If κ ~ ? To get 0.3, κ ~ 1. So plausible. Not error.
Maybe no clear error. We can say "No major error found; one status label: 线性门槛上限 is a finite computation, better labeled FACT than PROOF." That's safe.
Q1 missed connections:
R4 (a) collapse and Poisson decay.
R6 window containment and R10 short relations.
R3 D=1 and R11 R_K scaling invariance: since R_K is scaling invariant, the best scaling doesn't change R_K; the 457 cover's ×4 is about making small speeds visible, not changing R_K. This corrects a possible misconception. If true, R_K cannot distinguish scalings, so core search must be separate.
Q3: We can do a hand computation to verify "R_K is scaling invariant" for small p, K=1. Let's do p=17, N=16? H=1. B(x)=1 if ||x||>1, else 0. Compute U for S={1,2}? Not 14. But scaling invariance of U_K is general. We can show algebraically, that's a proof, not code. But Q3 asks verify one thing yourself with code required. We can say UNFINISHED for code. But maybe we can do a hand computation of a small case to verify something. For example, verify "D(p)=1 exactly for 431" is impossible by hand. So UNFINISHED is okay.
Q4: Next step: prove D(p) linear growth. Because it's the bridge.
Q5: Paragraph.
Now write final answer. Ensure ANSWER BLOCK first <=300 words. Then reasoning <=500 words. Code block extra.
Let's compose.
ANSWER BLOCK
Q1.
Missed links: (1) R4’s (a)-collapse likely follows the same Poisson decay as 14-cover counts; if true, gate (a) has an analytic shortcut. (2) R6 window containment and R10 short relations are the same phenomenon; formalizing it would bound core sizes. (3) R3’s D=1 near-misses and R11’s R_K: since R_K is scaling-invariant, the one-cell gap must come from exact higher-frequency cancellation, not R4. If true, D=0 needs a separate exact test.
Q2.
Status error: §二 lists “线性门槛上限” as PROOF, but it is a finite 33-prime computation; correct label is FACT. No other clear error found.
Q3.
UNFINISHED. I cannot execute code in this reply. The code below would check R_K scaling-invariance for p=17, K=1.
Q4.
Next step: prove D(p) ≥ αp − β for large p. It pulls L16’s 120¹⁴ threshold down and generalizes to any N.
Q5.
Rounds 1–12 found an exact Fourier split (random + resonance), a Poisson formula predicting cover death, and computational evidence that 14-covers die around p≈430–460. The missing proof is uniform resonance control.
Least-sure step:
Q3’s computed verification.
Reasoning
FACT: The review’s central identity U(S) = M(p) + R(S) is exact. IDEA: The random part M(p) ∼ 0.077p explains why covers become rare; the resonance part explains the 457 and 281 exceptions.
FACT: R_K is scaling-invariant. Proof: U_K(uS) = 1/2 ∑_t ∏_v B_K(uvt). Let t′ = ut; since u is a unit, the sum is 1/2 ∑_{t′} ∏_v B_K(vt′) = U_K(S). Since M(p) is scaling-independent, R_K = U_K − M is also scaling-invariant. This corrects the R11 packet’s premise that R_K is not scaling-invariant.
IDEA: Because R_K is scaling-invariant, the best scaling of the 457 cover (×4) does not change R_K. It only makes small speeds visible for core analysis. So R_4 cannot predict the best scaling; it can only predict cover existence after the core is fixed.
IDEA: For Q4, proving D(p) linear is the most promising single step. If D(p) ≥ αp − β, then a Fourier bound with error o(p) would give γ(p) = 15 for all p > P0. This P0 could be far below 120^14. The hard part is bounding the high-frequency tail uniformly.
UNFINISHED: I did not compute Q3. Below is code that would verify R_K scaling-invariance for a small case. It is not executed here.

python
import cmath, math

def B_K(x, p, K):
    # B(x)=1 if min(x,p-x)>H, else 0, H=floor((p-1)/16)
    H = (p - 1) // 16
    B = 1 if min(x % p, p - x % p) > H else 0
    # truncated Fourier series
    s = 0
    for k in range(-K, K + 1):
        if k == 0:
            bhat = 1 - (2 * H + 1) / p
        else:
            bhat = -(1 / p) * cmath.sin(cmath.pi * (2 * H + 1) * k / p) / cmath.sin(cmath.pi * k / p)
        s += bhat * cmath.exp(2j * cmath.pi * k * x / p)
    return s.real

def U_K(S, p, K):
    n = (p - 1) // 2
    total = 0
    for t in range(1, n + 1):
        prod = 1
        for v in S:
            prod *= B_K(v * t, p, K)
        total += prod
    return total / 2

p = 17; K = 1; S = [1, 2, 3, 4]
u = 3  # unit mod 17
uS = [(u * v) % p for v in S]
print(U_K(S, p, K), U_K(uS, p, K))

This should print the same value twice if R_K is scaling-invariant.

-- END OF REPLY --

--- end verbatim ---
END LETTER
