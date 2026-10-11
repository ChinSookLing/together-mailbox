BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 11:10 +08
RE: 猜公式 Round 9 (packet ec15a2d), send text r9_send_full.txt or r9_send_short.txt
SEAT: astra
MODEL: GPT-6 High (Astra, Civilisation Field project), worked 5m 24s
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253

--- reply verbatim ---
ANSWER BLOCK · GPT · Round 9

Q1 · IDEA / FACT：死亡线模型
采用两参数经验式：
P̂(N) = 1.271204 N^2 + 7.134310 N

[Fit table]
N | 已发现最大p | 模型值 | 误差
16 | 457 | 439.58 | −17.42
17 | 479 | 488.66 | +9.66
18 | 523 | 540.29 | +17.29
20 | 661 | 651.17 | −9.83

FACT：平均绝对误差 13.55，RMSE 14.08。这是对目前已发现最大值的拟合，不是对真正 P*(N) 的证明。

Q2 · FACT：搜索取得的严格下界

N | P*(N) ≥ | 方法
8 | 113 | Search + verified
9 | 127 | Search + verified
10 | 131 | Search + verified
11 | 181 | Search + verified
12 | 241 | Search + verified
13 | 263 | Search + verified
14 | 311 | Search + verified
15 | 367 | Search + verified

所有覆盖均独立逐格验证；没有宣称完整穷举。

Q3 · IDEA：盲预测

N | 点预测 | 预测区间 | 置信度
22 | 773 | 690–920 | 55%
24 | 907 | 795–1130 | 50%

预测的是主席规定的六个连续未发现素数停止规则下的观测死亡线。没有对 N = 22, 24 进行覆盖计算。

Q4 · FACT / IDEA：
死亡线更可能是有零星幸存者的过渡区域（Transition Region），而非单一断崖。641 与 661 都满足 p ≡ 1 (mod 20)，却表现不同，因此模数和覆盖容量不足以独立解释幸存者。

Reasoning

1. 从计数模型到死亡线

IDEA：设 k = N − 2，采用近似式：
log Ĉ_N(p) = A + B·log((k/n)·n) − C·n·(1 − H/n)^k.

死亡线由 log Ĉ_N(p) = 0 近似确定。
第一项随候选组合增加，第二项惩罚未覆盖格子。两者竞争，使覆盖数量在某个区域快速下降。
但随机独立近似忽略乘法相关性，所以我没有声称可以严格推出二次式。所给两参数公式是 N = 16 至 20 的局部经验拟合。

IDEA：不使用三参数精确插值，是为了减少四个数据点造成的过拟合。这个选择牺牲了样本内精度，但可能提高外推稳定性。

2. Q2 可复验的覆盖证书

FACT：以下八组速度集合均具有恰好 N − 2 个速度，全部时间格得到覆盖。

witnesses = {
  8:  (113, [1,18,34,43,44,52]),
  9:  (127, [1,8,32,39,40,48,56]),
  10: (131, [1,13,15,16,28,41,54,62]),
  11: (181, [1,7,9,20,23,26,38,53,66]),
  12: (241, [1,7,8,22,30,38,56,63,64,65]),
  13: (263, [1,3,5,7,8,11,13,18,19,60,117]),
  14: (311, [1,4,5,6,7,9,11,13,91,117,143,147]),
  15: (367, [1,27,28,29,30,55,83,85,86,113,114,168,174])
}
for N, (p, S) in witnesses.items():
    n = (p-1)//2
    H = (p-1)//N
    assert len(S) == N-2
    assert len(set(S)) == N-2
    assert all(any(min(v*t%p, p-(v*t%p)) <= H for v in S) for t in range(1, n+1))
    print(N, p, "PASS")

FACT：对全部八组，验证输出均为 PASS。

3. 为什么不能把死亡线当作单调阈值？

FACT：对 N = 20：641 ≡ 661 ≡ 1 (mod 20).
两者都有最大可能覆盖比例：H/n = 2/20.
但搜索未在 641 找到覆盖，却在 661 找到覆盖。

IDEA：真正决定后期幸存者的，可能是速度集合的乘法关系、模素数结构，以及未覆盖格子的排列，而非平均覆盖容量。
这也意味着 P*(N) 的经验预测不能简单依赖连续递减的覆盖数量。

4. 对 Terminal Formula 的意义

IDEA：我建议将研究对象拆成两个层次：
Death Region + Arithmetic Survivors
第一层由覆盖计数模型预测大致范围；第二层需要结构定理，证明是否存在穿越该范围的特殊速度集合。
如果第二层能找到统一的结构性排除条件，才可能把经验死亡线变成严格上界。

最不确定的一步：
两参数模型从 N = 16 – 20 外推到 22、24 是否保持稳定，尤其当罕见的算术幸存者能够远超平均死亡区域时。

STATUS：UNFINISHED。
已取得 N = 8 – 15 的可验证新下界；真正的 P*(N) 尚未确定。

--- end verbatim ---
END LETTER
