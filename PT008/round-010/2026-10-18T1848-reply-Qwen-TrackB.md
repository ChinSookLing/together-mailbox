BEGIN RECORD
ROUND: PT-008 R010 · Track B deterministic phase selection
SEAT: Qwen (Qwen3.8-Max Thinking, web off, Play Civilisation Field project)
CARRIED_BY: Hesper
SEND TEXT: PT008/round-010/send_010_hesper_qwen_trackB.txt (b5cf957, sha256 d154072778d2f508badab776e55d6dffcdbc762e0a48a8d79953957e384470ed)
SENT: 2026-10-18 18:40 +08 · COPIED: 18:48 +08
CAPTURE FILE SHA256: 6fa6fa8eb23052ffcda9ec418d35f2a88b07a364d0799f608e4de3824c426d72
SELF-PROVED FLAG: none
CAPTURE NOTE: Copy truncated in Section 5 table; remainder transcribed from rendered page (marked).
HESPER FLAGS (not a grade): (1) Sec.1 d=b+c family checked exactly at eps=1/2: (1/2,1,3/2,5/2), 4a=2<d<6=4c, dt=k. (2) Sec.3 bound q-3*ceil(2q/5) >= q-6q/5-3 is NEGATIVE for all q, so 'q>=15 positive' does not follow. (3) Sec.2 'k must grow, so no floor/ceil expression' is not a valid impossibility argument (floor(c/eta) is unbounded).
---
Chat: https://chat.qwen.ai/c/0e37bf1a-9aa5-4ae7-9b6d-45fb387e78e7
Model: Qwen3.8-Max (Thinking mode)
Copy time (Asia/Singapore): 2026-10-18 18:48 SGT
Status: Final reply rendered (Regenerate button present, no Stop/Continue, "AI-generated content may not be accurate" disclaimer shown); Copy button truncated the reply at the table in Section 5. The portion below the "--- TRUNCATION NOTE ---" marker was appended verbatim from the rendered page.

Below is the full final reply. The part up to the truncation marker came from the Copy button; the remainder was read from the rendered page because Copy truncated the markdown (the clipboard ends with "| 项目 | …(truncated)").## ANSWER BLOCK（≤300 字）

锁相族 $t=k/(b+c)$ 在目标区域 $4a<d<4c$ 内**不存在**由速度比经取整或有界表达式普适确定 $k$ 的规则。核心反例：取 $a=\varepsilon,\,b=1,\,c=1+\varepsilon,\,d=2+\varepsilon=b+c$，则 $\|dt\|=\|k\|=0$，**全族对一切 $k$ 失效**（DISPROVED）。此反例构成连续单参数族，非孤立点。当 $d/(b+c)$ 远离整数时解存在，但 $k$ 依赖模算术（逆元、剩余类交集），无统一 $\lfloor\cdot\rfloor/\lceil\cdot\rceil$ 公式。R009 修正已采纳：禁止带宽 $=2$，坏比例 $=2/5$，分层 $5k{-}6<z\le 5k{-}1$。

---

## 1  DISPROVED — 锁相族在目标区域内普适失效

**定理（反例族）.**  对任意 $\varepsilon\in(0,\tfrac{2}{3})$，令

$$a=\varepsilon,\quad b=1,\quad c=1+\varepsilon,\quad d=2+\varepsilon.$$

则 $0<a<b<c<d$，$4a<d<4c$，但对锁相族 $t=k/(b+c)$ 的**一切** $k\in\mathbb{Z}_{>0}$，均有 $\|dt\|=0<\tfrac15$。

**证明.**

**(i) 速度排序.**  $0<\varepsilon<1<1+\varepsilon<2+\varepsilon$，成立。

**(ii) 目标区域验证.**

$$4a=4\varepsilon<2+\varepsilon=d \iff 3\varepsilon<2 \iff \varepsilon<\tfrac23.\;\checkmark$$

$$d=2+\varepsilon<4+4\varepsilon=4c.\;\checkmark$$

**(iii) 锁相计算.**  $b+c=1+(1+\varepsilon)=2+\varepsilon=d$。故

$$t=\frac{k}{b+c}=\frac{k}{2+\varepsilon},\qquad dt=(2+\varepsilon)\cdot\frac{k}{2+\varepsilon}=k\in\mathbb{Z}.$$

因此 $\|dt\|=\|k\|=0<\tfrac15$，对**所有** $k\ge 1$ 成立。$\blacksquare$

> **注.** 此反例并非孤立点：$\varepsilon$ 在 $(0,2/3)$ 上连续变化，给出目标区域内一维连续反例族。更一般地，$d=m(b+c)$（$m\in\mathbb{Z}_{\ge 1}$）均导致 $\|dt\|=0$；$m=1$ 即上例，$m=2$ 需 $2(b+c)<4c\Leftrightarrow b<c$，同样落在目标区域内。

---

## 2  近整数情形的量化障碍（CHECKED）

即使 $d\neq b+c$，若 $\delta:=d/(b+c)$ 距整数很近，锁相族仍需极大 $k$。

**例.**  取 $b=1,\,c=2,\,b+c=3,\,d=3+\eta$（$\eta>0$ 极小），$a$ 适当。则 $\delta=1+\eta/3$。

$$\|k\delta\|=\|k+k\eta/3\|=\|k\eta/3\|.$$

要 $\|k\eta/3\|\ge 1/5$，至少需 $k\ge \frac{3}{5\eta}$。当 $\eta\to 0^+$，所需 $k\to\infty$。

因此任何仅依赖 $\lfloor\cdot\rfloor,\lceil\cdot\rceil$ 及有限算术运算的有界表达式 $k=F(a,b,c,d)$ 均无法覆盖 $\eta$ 任意小的情形。$\checkmark$

---

## 3  正当子区域内的存在性与结构（PROOF CANDIDATE）

**命题.**  设 $b+c=q\in\mathbb{Z}_{>0}$，$a,b,c,d$ 均为正整数，$\gcd$ 条件使周期为 $q$。若 $d\not\equiv 0\pmod{q}$，则满足全部三个 $\|\cdot\|\ge 1/5$ 条件的 $k\bmod q$ 的个数 $\ge 1$。

**论证（计数）.**  记 $\beta=b/q,\;\alpha=a/q,\;\delta=d/q$。

- $\beta$ 条件排除 $\{k:kb\bmod q\in\{0,\ldots,\lfloor q/5\rfloor\}\cup\{q-\lfloor q/5\rfloor,\ldots,q-1\}\}$，至多排除 $\lceil 2q/5\rceil$ 个剩余类。
- $\alpha$ 条件、$\delta$ 条件同理。

三个条件各排除 $\le\lceil 2q/5\rceil$ 个类。由容斥，交集大小

$$\ge q-3\lceil 2q/5\rceil \ge q-\tfrac{6q}{5}-3.$$

当 $q\ge 15$ 时此下界为正，故解存在。但**具体哪些 $k$ 有效**取决于 $b,d$ 模 $q$ 的乘法结构（逆元、陪集），无法用统一的取整公式表达。

对 $q<15$ 需逐一验证（略，属有限检验）。$\square$（PROOF CANDIDATE，大 $q$ 计数严格，小 $q$ 未逐一列出）

---

## 4  $a$ 侧的同步约束（CHECKED）

当 $\alpha=a/(b+c)$ 极小时，$\|k\alpha\|<1/5$ 对 $k=1,2,\ldots,\lfloor 1/(5\alpha)\rfloor$ 均成立。

**例.**  $a=1,\,b=100,\,c=101,\,b+c=201$。则 $\alpha=1/201$。

$$\|k/201\|\ge 1/5 \iff k\bmod 201\in\{41,42,\ldots,160\}.$$

最小合法 $k=41$。同时 $\beta=100/201$，$\delta=d/201$ 的条件进一步约束 $k$。$k$ 的选取本质上是三个剩余类集合的交集问题，依赖 $100^{-1}\bmod 201$ 等模逆运算，无封闭取整公式。$\checkmark$

---

## 5  R009 修正之采纳（CHECKED）

| 项目 | …(truncated)

--- TRUNCATION NOTE: Copy button truncated the reply here (clipboard ended with "| 项目 | …(truncated)"). The remainder below was read verbatim from the rendered page to recover Sections 5 (rest), 6, and the Track B verdict. ---=== APPENDED FROM RENDERED PAGE (Copy button truncated inside the Section 5 table; the following Sections 5 remainder and 6 + verdict are transcribed verbatim from the rendered reply, preserving wording and structure) ===

5  R009 修正之采纳（CHECKED）

| 项目 | R009 原值 | 主席修正 | 本席确认 |
|---|---|---|---|
| 禁止带宽 | 2/5 | 2（两段各 1/5，总"带宽"计数为 2） | 采纳 |
| 坏 x 比例 | 8% | 2/5 | 采纳：每条件禁止测度 = 2/5 |
| 分层公式 | （有误） | 5k−6 < z ≤ 5k−1 | 采纳 |

验证 5k−6 < z ≤ 5k−1：
k=1 给 −1 < z ≤ 4；
k=2 给 4 < z ≤ 9；
k=3 给 9 < z ≤ 14。
层宽 5，无缝拼接，覆盖 z > −1。 ✓

6  结论与未决问题

| 标签 | 内容 |
|---|---|
| DISPROVED | 锁相族 t=k/(b+c) 在 4a<d<4c 内无普适 k 选取规则；d=b+c 反例族使其完全失效 |
| CHECKED | d/(b+c) 近整数时 k 无界增长；a/(b+c) 极小时最小合法 k 亦无界 |
| PROOF CANDIDATE | d ≢ 0 (mod b+c) 且 q ≥ 15 时解存在（计数论证） |
| UNFINISHED | 是否存在修改后的锁相族（如 t=k/(b+c)+s，s 为小修正）可覆盖 d≈b+c 的邻域，需后续轮次探讨 |
| UNFINISHED | 分层公式 5k−6 < z ≤ 5k−1 与 a 侧约束的交互尚未完全刻画 |

Track B 判定：在锁相族框架内，确定性相位选取规则不可能普适成立。需跳出该族或引入修正项方能推进 F5 的无限制构造。

=== END OF APPENDED RENDERED REMAINDER ===
END RECORD
