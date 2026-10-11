BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 16:54 +08
RE: 猜公式 Round 14 (packet 1473ae0), send text r14_send_full.txt or r14_send_short.txt
SEAT: astra
MODEL: GPT-6 High (Astra chat)
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253

--- reply verbatim ---
=== Round 14 VERBATIM REPLY — CHUNK 1 (ANSWER BLOCK + table of contents) ===
Captured by find_text context_chars=1000 on "The Deficit Ratio and Subgroup"
Chat URL: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253

ANSWER BLOCK · GPT · Round 14
PT005 · The Deficit Ratio and Subgroup Structure

Q1 · FACT / UNFINISHED： 已独立搜索并逐格验证全部指定样本。以下是 𝐷 ( 𝑝 ) D(p) 的上界； 𝑈 / 𝐸 U/E 只是 𝛿 ( 𝑝 ) δ(p) 的上界。
𝑁 N 𝑝 p 最佳 𝑈 U 精确期望 𝐸 E 𝑈 / 𝐸 U/E
16 1499 12 115.0303 0.10432
16 1999 14 154.2057 0.09079
16 2503 17 191.8302 0.08862
16 3001 21 230.5383 0.09109
20 1009 4 74.2680 0.05386
20 1031 3 76.2204 0.03936

Q2 · FACT： 穷举 𝑝 ≤ 20000 , 𝑝 ≡ 1 ( m o d 28 ) p≤20000, p≡1(mod28)：188 个素数，仅 29、281 的子群完整覆盖。空陪集比例为 0.153464，非常接近 ( 7 / 8 ) 14 = 0.154210 (7/8) 14 =0.154210，而非 𝑒 − 3.5 e −3.5 。原因是正负配对。

Q3 · PROOF / FACT： bounded differences 只给常数量级指数。独立计算发现，在 1499、3001，所有不同时间格的阻挡速度集合两两相交；普通 Janson 依赖图因此完全稠密。

Q4 · IDEA： 优先建立「算术结构／伪随机」二分定理，再分别证明遗漏格数的统一正比例下界。最难的是高度共振的结构类。

Q5 · IDEA： 方法可推广至任意固定 𝑁 N，包括 17、18、20；但统一 𝛿 𝑁 > 0 δ N ​>0 尚未证明。

1. Q1 · 缺口比例是否稳定？
FACT： 使用上述独立搜索结果，对 𝑁 = 16 N=16 的四个 𝑈 / 𝐸 U/E 上界进行线性拟合： 𝑈 / 𝐸 ^ = 0.1125146 − 0.0…=== CHUNK 1b (Q1 detail + section 2 Q2 — from find_text "线性拟合" context_chars=1000) ===

1. Q1 · 缺口比例是否稳定？
FACT： 使用上述独立搜索结果，对 𝑁 = 16 N=16 的四个 𝑈 / 𝐸 U/E 上界进行线性拟合： 𝑈 / 𝐸 ^ = 0.1125146 − 0.00000835804 𝑝 . U/E ​ =0.1125146−0.00000835804p.
搜索上界先下降，再接近平坦；这并不能证明真实的 𝛿 ( 𝑝 ) δ(p) 下降或收敛。

最小遗漏比例的搜索上界
所有点都是已验证集合的 U/E，不是 δ(p) 的精确值。
0 0.03 0.06 0.09 0.12 1499 1999 2503 3001
1499: U/E 上界 0.1
1999: U/E 上界 0.1
2503: U/E 上界 0.1
3001: U/E 上界 0.1

UNFINISHED： 不能由这些样本判断 𝛿 ( 𝑝 ) δ(p) 最终趋向正常数、趋向零，还是振荡。

2. Q2 · 子群的真正随机模型
FACT： 对全部指定素数枚举，空陪集数 𝑒 ( 𝑝 ) e(p) 的最小二乘拟合为： 𝑒 ( 𝑝 ) ≈ 0.00551645 𝑝 − 0.342663 . e(p)≈0.00551645p−0.342663 ​ .
独立配对模型的理论斜率为 ( 7 / 8 ) 14 28 = 0.00550750. 28 (7/8) 14 ​ =0.00550750.
两个斜率接近。

28 阶子群：空陪集比例
枚举样本的加权比例，与两种独立性模型比较。
0 0.045 0.09 0.135 0.18
实测 14 对模型 28 个独立
实测: 空陪集比例 0.15346387
14 对模型: 空陪集比例 0.15421007
28 个独立: 空陪集比例 0.02378075

PROOF： 由于 𝐺 𝑝 G p ​ 含有 − 1 −1，28 个剩余元素形成 14 对 { 𝑟 , − 𝑟 } {r,−r}。每对只对应一个绝对速度，因此独立性近似应使用 14 个有效速度，而非 28 个。

FACT： 在已检查范围内，281 是最后一个完整覆盖的子群素数。

UNFINISHED： 尚未证明 281 是全体素数中的最后一个。若接受 ledger L16 的前提，L16 已能在其巨大门槛之外排除这种覆盖，但没有产生新的有效界。

为什么经典工具还不够？
IDEA： Pólya–Vinogro… [truncated — next chunk starts at full "Pólya–Vinogradov"]=== CHUNK 1c (section 3 Q3 + section 4 Q4 — Pólya–Vinogradov find_text context_chars=1000) ===

为什么经典工具还不够？
IDEA： Pólya–Vinogradov（Pólya–Vinogradov Inequality）和 Burgess Bound 主要控制字符和。这里一个固定陪集中的小元素期望数量仅为常数量级，现有一般误差界过大。 Weil Bound 对合适的有限域代数相关和很强，但要控制所有陪集同时为空或非空的高阶相关性，还需要额外结构。
目标不是证明每个陪集都有接近期望的数量，而是证明至少一个陪集为空。

3. Q3 · 传统集中不等式的障碍
PROOF： 替换一个速度至多改变 𝐻 H 个时间格的覆盖状态。由于 𝐻 H 与 𝑝 p 同阶，而 𝐸 𝑈 EU 也与 𝑝 p 同阶，直接使用 bounded differences 得到的指数不随 𝑝 p 增长。
FACT： 我独立计算阻挡速度集合 𝑊 𝑡 W t ​ 的两两交集：
𝑝 p 时间格对数 非空交集对数 比例
1499 280,126 280,126 100%
3001 1,124,250 1,124,250 100%
这使普通依赖图版本的 Janson 方法缺少稀疏结构。不过，这并不排除更精细的相关性工具。

4. Q4 · 最短引理链
引理 内容 状态
A 精确计算随机集合期望 𝐸 𝑁 ( 𝑝 ) E N ​ (p) PROVED
B 将 𝑈 𝑁 ( 𝑆 ) U N ​ (S) 写成主项加算术共振项 PROVED
C 把所有速度集合分成可控制的伪随机类与结构类 OPEN
D 对两类分别证明 𝑈 𝑁 ( 𝑆 ) ≥ 𝑐 𝑁 𝑝 U N ​ (S)≥c N ​ p OPEN
E 由 𝑐 𝑁 > 0 c N ​ >0 推出足够大素数不存在 ( 𝑁 − 2 ) (N−2)-cover PROVED，条件性
IDEA： 伪随机类可能由傅里叶谱或高阶相关性控制；结构类则需要处理连续速度、子群和短整数关系等特殊构造。
最难的单一步骤：引理 D 的结构类。
这类集合正是此前能够把大量预期遗漏格子消除的幸存者。

5. Q5 · 推广到其他跑者数
PROOF： 对固定… [truncated — next chunk picks up at Q5 detail]=== CHUNK 1d (section 5 Q5 + start of section 6 — "推广到其他跑者数" find_text context_chars=1000) ===

5. Q5 · 推广到其他跑者数
PROOF： 对固定 𝑁 N，令 𝑘 = 𝑁 − 2 k=N−2，有 𝐸 𝑁 ( 𝑝 ) = 𝑛 ( 𝑛 − 𝐻 𝑘 ) ( 𝑛 𝑘 ) , 𝐸 𝑁 ( 𝑝 ) 𝑝 ⟶ 1 2 ( 1 − 2 𝑁 ) 𝑁 − 2 . E N ​ (p)=n ( k n ​ ) ( k n−H ​ ) ​ , p E N ​ (p) ​ ⟶ 2 1 ​ (1− N 2 ​ ) N−2 .
因此随机主项对每个固定 𝑁 N 都具有线性尺度。
IDEA： 若能对每个固定 𝑁 N 建立结构敏感的统一共振限制，则同一证明架构可以推广，不必重新发明 𝑁 = 17 , 18 , 20 N=17,18,20 的方法。
但 𝑐 𝑁 c N ​ 可能依赖 𝑁 N。当前没有对所有 𝑁 N 同时有效的统一常数。

6. 完整计算证书
每次搜索调用都在一分钟内结束，搜索所得集合均使用独立的逐格计算复核。
完整 Python 搜索与验证程序
包括模拟退火、精确期望、六组覆盖证书、子群普查、回归及交集验证。
188 个子群素数完整逐项结果
每个素数的陪集总数、空陪集数及遗漏格数。

以下为实际使用的计算核心及可重跑命令：

Python Run #
核心定义（完整搜索程序见附档）
import math
import random
def expectation(p, N):
    n = (p - 1) // 2
    H = (p - 1) // N
    k = N - 2
    result = n
    for j in range(k):
        result *= (n - H - j) / (n - j)
    return result
def deficit(p, N, S):
    H = (p - 1) // N
    return sum( all(H < (v*t) % p < p-H for v in S) for t in range(1, (p+1)//2) )
def safe_masks(p, N):
    n = (p-1)//2
    H = (p-1)//N…=== CHUNK 1e (full command list + 最终研究判断 + STATUS = end of Round 14) ===
Reconstructed from the overlapping find_text match #7 (the widest single hit that shows all commands plus final STATUS, with the ChatGPT footer immediately after confirming end-of-reply).

def objective(S, masks):
    z = masks[S[0]]
    for v in S[1:]:
        z &= masks[v]
    return z.bit_count()

# 完整程序的实际搜索命令：
# python pt005_r14_compute.py search 16 1499 4000000 12 140014
# python pt005_r14_compute.py search 16 1999 4000000 12 140014
# python pt005_r14_compute.py search 16 2503 4000000 12 140014
# python pt005_r14_compute.py search 16 3001 4000000 12 140014
# python pt005_r14_compute.py search 20 1009 4000000 12 140014
# python pt005_r14_compute.py search 20 1031 4000000 12 140014
# 逐格复核全部最佳集合、计算回归
# python pt005_r14_compute.py verify
# 完整枚举所有 p<=20000 且 p%28==1 的素数
# python pt005_r14_compute.py subgroup
# 独立检查 Janson 交集稠密性
# python pt005_r14_compute.py overlap

最终研究判断 IDEA： 本轮最有价值的不是搜索曲线，而是子群结果揭示的有效独立维度（Effective Independence Dimension）。 虽然一个子群有 28 个元素，但真正参与覆盖统计的只有 14 个正负速度类。修正独立维度后，理论空陪集比例与实际枚举非常接近。 这提示一种下一步： 不要对全部速度直接假设独立；先识别整数关系形成的等价结构，再对剩余的有效自由度建立统计与确定性界。
最不确定的一步： 这种「结构压缩后的有效自由度」是否能够对任意速度集合定义，并提供足以证明统一正遗漏比例的严格下界？

STATUS：Q1 搜索完成但最优性 UNFINISHED；Q2 指定范围穷举完成；Q3 计算验证；Q4–Q5 证明路线仍 OPEN。

[Immediately followed by the ChatGPT system footer — "ChatGPT can make mistakes. Check important info. Latest response High Response complete 0.045" — confirming nothing more follows in Round 14.]

=== CAPTURE SUMMARY ===
Full verbatim Round 14 ANSWER BLOCK captured via overlapping page find_text (context_chars=1000) extractions.
Chat URL: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253
URL contains "the-civilisation-field/c/6ac97e19" as required.

Anchors verified on-page:
- "Worked for 7m 5s Analysis paused" — Round 14 metadata
- "ANSWER BLOCK · GPT · Round 14" — found exactly once
- Q1 table (N=16 p=1499..3001; N=20 p=1009,1031) — present
- Q2: 188 素数, 仅 29、281 子群完整覆盖; 空陪集比例 0.153464 ≈ (7/8)^14 = 0.154210
- Q3: bounded-differences obstruction + 1499/3001 100% intersection density
- Q4: lemmas A-E with statuses
- Q5: E_N(p)/p → (1/2)(1−2/N)^(N−2)
- Section 6: all 9 pt005_r14_compute.py commands (6 search + verify + subgroup + overlap) + inline expectation/deficit/safe_masks/objective
- STATUS (final line) immediately followed by ChatGPT footer = end of reply

Copy button: in-page Copy returned empty clipboard; verbatim reply obtained by page text extraction (find_text), per task fallback.
Reload: one reload was performed by the prior session (confirmed by the system reminder). Round 14 had already completed on its own before any nudge would have been needed, so the reserved nudge message was not sent. The rule "do NOT resend Round 14" was observed.
--- end verbatim ---
END LETTER
