BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-10 10:01 +08
RE: 猜公式 Round 5 (packet 4640c52), send text r5_send_astra.txt
SEAT: astra
MODEL: GPT-6 Thinking High (Astra project)
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253

--- reply verbatim ---
[Courier note: Astra seat (ChatGPT project "The Civilisation Field"), model GPT-6, Thinking High, web off, worked 4m 55s. The reply heads itself "GPT" — the GPT and Astra headers appear swapped this round.]

ANSWER BLOCK · GPT · Round 5

Q3 · IDEA：预测 14 个考试素数全部为 0。 置信度是主观估计，并非统计校准概率。最不确定的是 521。

素数 p | 预测 | 置信度 | 素数 p | 预测 | 置信度
503 | 0 | 72% | 563 | 0 | 91%
509 | 0 | 84% | 569 | 0 | 76%
521 | 0 | 62% | 571 | 0 | 90%
523 | 0 | 80% | 577 | 0 | 88%
541 | 0 | 85% | 587 | 0 | 92%
547 | 0 | 89% | 593 | 0 | 92%
557 | 0 | 89% | 599 | 0 | 94%

Q1 · IDEA：31/33 正确。 规则：p ≤ 421，或 p ≡ 9 (mod 16) 且 p ≤ 457，预测 >0；其余预测 0。仅误判 383、397。这是拟合规则，不是结构定理。

Q2 · PROOF/DATA： 457 的连续七速其实是缩放后的奇数核心（Odd Core）{1, 3, 5, 7, 9, 11, 13}。337 也存在这种核心的 14-cover；但该家族并不解释所有正例。

Q4 · IDEA： 应研究「缩放后的小核心 + 剩余速度的覆盖能力」，而不是单独研究 p mod 16。这可能连接 Dirichlet 障碍，但尚未证明。

推理与验证

1. Q1 规则复核

FACT： 以下代码仅使用 Data 1，可复现 31/33。

```python
P = [
    307,311,313,317,331,337,347,349,353,359,367,
    373,379,383,389,397,401,409,419,421,431,433,
    439,443,449,457,461,463,467,479,487,491,499
]

POS = {
    307,311,313,317,331,337,347,349,353,359,
    367,373,379,389,401,409,419,421,457
}

def predict(p):
    return p <= 421 or (p % 16 == 9 and p <= 457)

wrong = [p for p in P if predict(p) != (p in POS)]
print(33 - len(wrong), wrong)
# 31 [383, 397]
```

IDEA： 457 的例外支持保留少量非零预测概率，但不能证明模 16 的规律能外推。

2. Q2 奇数核心的结构解释

PROOF： 对任何足够大的奇素数，取最接近 p/4 的整数 m。

若 p = 4m+1，则 4(m+j) ≡ 4j−1 (mod p)。

若 p = 4m−1，则 4(m+j) ≡ 4j+1 (mod p)。

当 j = −3,…,3，七个连续速度乘以 4，再按正负归一化，恰好成为七个奇数：O7 = {1, 3, 5, 7, 9, 11, 13}。

因此，457 的七连速不是模 16 特有现象。

FACT： 利用 Data 2，457 的 14-cover 乘以 4 后成为

O7 ∪ {4, 8, 30, 185, 217, 219, 220}.

另外，对 337，我找到并逐格验证了：

O7 ∪ {8, 31, 96, 118, 154, 157, 159}.

DATA： 对 347 固定 O7、再选至多七速的整数规划（MILP）返回 infeasible；这不是形式证明。已完成的只是部分家族测试，不能宣称穷举所有 33 个素数。

3. Q4 一个具体的缩放线索

FACT： 457 的覆盖还可乘以 8，压缩到最大速度 87：

{2, 6, 8, 10, 14, 16, 17, 18, 19, 22, 23, 26, 60, 87}.

PROOF： 这个固定速度集合存在长度为 5/2958 的安全时间区间。因此对同一整数速度集合，p ≥ 592 时必有网格安全点，不可能继续覆盖。

IDEA： 这提示我们寻找覆盖结构的统一压缩界，但不能推出所有 14-cover 在 p ≥ 592 消失。

最不确定的一步： 457 的奇数核心与极小缩放，究竟代表可推广的覆盖家族，还是孤立的有限素数现象？

--- end verbatim ---
END LETTER
