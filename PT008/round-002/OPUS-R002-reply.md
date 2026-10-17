# PT-008 · Round 002 · OPUS — Proof Audit of L2
**The Moving Safe Window**　Seat: Fixed Review（Opus 5.5）　To: GPT-6 (Chair)　Courier: Puck　Date: 2026-10-17　WEB OFF

(Archived by Puck from the text Tuzi pasted in chat at 2026-10-17 16:39 +08, original filename PT-008-R002-OPUS-AUDIT.md.)

## ANSWER BLOCK
- 审阅结论：L2 逐行核对，证明正确，无缺口。Lipschitz 界、窗口非负、负速度、最近整数平局、等号边界全部成立。建议升级为 PROVED（主席证明 + Opus 独立审阅；由 Puck 存档）。
- 最容易出错的假设：以为 L2 是"可以继续削弱的条件"。在 L2 自身的固定窗口框架里，|w| ≥ nM 是精确最优的（sharp）：对每个 n，都存在 |w| 任意接近 nM 而窗口内无解的例子——但这些例子全局有解。—— PROOF CANDIDATE
- 与 Round 001 关系：L2 与快新人引理（Fast Newcomer Lemma）数学等价（n = m+1）。L2 的写法更好：等号公式精确、非负性证明更干净。非实质性加强。
- 可加强处：用实际余量（actual margin）代替最坏情形 M，得 L2*，严格强于 L2。—— PROOF CANDIDATE
- 最薄弱的一步：不在证明内，而在用法——L2 只吃一个 t₀ 和最坏窗口 h，信息量不够跨越 |w| < nM。

## SECTION A — Mathematical Argument（逐行审阅）
行49 | ‖x‖−‖y‖| ≤ |x−y| ✅ 1-Lipschitz。
行51 d_u(t) ≥ d_u(t₀) − |u||t−t₀| ✅ 对 u<0 同样成立。
行53 窗口内 ≥ 1/n − Mh = 1/(n+1) ✅ 等号可在窗口端点取到，门槛是 ≥，无问题。
行57 ‖ut₀‖ ≤ |u|t₀ ✅
行59 t₀ ≥ 1/(nM) > h ✅ 需 V 非空（n ≥ 2）。h/t₀ ≤ 1/(n+1) < 1，故 I ⊂ (0,∞) 严格为正。
行64 ‖wt₀‖ ≥ δ ⇒ t₁=t₀ ✅
行65 取最近整数 k ✅ 平局只在 ‖wt₀‖ = 1/2 时发生，此时已走第 64 行分支，k 唯一。
行67 t₁ = (k+σδ)/w ✅ 负速度无问题：wt₁ = k+σδ，‖wt₁‖ = δ。
行68 选使 |t₁−t₀| 最小的 σ ⚠️ 正确但应写成显式规则：σ = sign(wt₀ − k)；若 wt₀ = k，两个 σ 皆可。
行70 |t₁−t₀| = (δ − ‖wt₀‖)/|w| ✅ 等式精确。
行71–72 |w| ≥ nM ⇒ |t₁−t₀| ≤ h ✅
行73 新跑者"恰好"达到 δ ✅ 但新跑者余量为 0。

隐藏问题清单（Q2）：速度符号无问题；w = −u 是 L2 之外的平凡情形，不构成漏洞；没有用 [0,1) 或周期性；L2 假设 t₀ 已给定，需递归从 n=2 的 t₀ = 1/(2|u|) 开始造（Round 001 推论 B4'）。

## SECTION B — Proof or Counterexample
B1 [审阅通过 → 建议 PROVED] L2 本身。唯一文字修正：第 68 行改为 σ = sign(wt₀ − k)。

B2 [PROOF CANDIDATE] 条件 |w| ≥ nM 在 L2 框架中是精确最优的（sharp）。
命题：对每个 n ≥ 2 与任意 ε > 0，存在 V、t₀、w，使 nM − ε < |w| < nM，且窗口 I 内没有 t 满足 ‖wt‖ ≥ 1/(n+1)。
构造：V = {1,…,n−1}，M = n−1。取 t₀ = j + 1/n。令 q = (n−1)(jn+1) − 1，w = q/t₀ = nq/(jn+1) = n(n−1) − n/(jn+1)。于是 wt₀ = q ∈ ℤ，|w| < nM，j → ∞ 时 w → nM。w·I 是以整数 q 为中心、半宽 |w|h < δ 的区间，整段落在坏区间内，故 I 内无解。∎
但全局有解：n=2, V={1}, j=1：w = 4/3，窗口 [4/3,5/3] 失败，而 t = 1/2 给出 ‖1/2‖ = 1/2、‖2/3‖ = 1/3 ≥ 1/3。
（Opus 自测：n=2..5、j=1,3,10 共 12 例精确分数核对；带符号随机速度测试 L2 零失败。仅自测。）

B3 [PROOF CANDIDATE] L2*（实际余量版）。δ = 1/(n+1)，ρ = min_{u∈V} (d_u(t₀) − δ)/|u|。
(i) J = [t₀−ρ, t₀+ρ] 内所有旧跑者 ≥ δ，且 J ⊂ (0,∞)。
(ii) 若 (δ − ‖wt₀‖)/|w| ≤ ρ，则 t₁ = (k + sign(wt₀−k)·δ)/w 成功。
(iii) 若 |w| ≥ δ/ρ，则必成功。
严格更强：ρ ≥ h 恒成立；条件 (ii) 还用到 ‖wt₀‖。

## SECTION C — Next Lemma
双窗口引理（Two-Window Lemma）——IDEA。若 t₀, t₀' ∈ S（门槛 1/n），且 ‖w(t₀ − t₀')‖ ≥ 2δ − (|w|ρ + |w|ρ')，则两个余量窗口中至少有一个含新跑者的安全时间。直觉：两段 w-像不可能同时被困住。若 V 都是整数，t₀ 与 1 − t₀ 同时合格；一般情形可用 t₀ 与 2t₀（待查，未证）。

## SECTION D — Least-sure Step
1. 最薄弱的不在证明，而在框架：单窗口框架里不能再改进，削弱高速条件必须引入 t₀ 以外的信息。
2. 本轮最不确定：Section C 相位差条件的常数是否写对，只是 IDEA。
3. 待复核：B2、B3 为 PROOF CANDIDATE，待 Puck/其他座位独立复核。B1 由本席审阅通过，建议升级 PROVED。
