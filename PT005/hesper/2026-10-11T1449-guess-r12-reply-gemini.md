BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 14:51 +08
RE: 猜公式 Round 12 (packet c9a646a), send text r12_send_full.txt or r12_send_short.txt
SEAT: gemini
MODEL: Gemini Auto (High thinking)
CHAT: https://gemini.google.com/app/9fbd6ef002471a67

--- reply verbatim ---
## PT005 Round 12 — Reply capture

- **Chat:** "PT005 · Big Picture"
- **Chat URL:** https://gemini.google.com/app/9fbd6ef002471a67
- **Account:** csllanna@gmail.com (Chin Sook Ling)
- **Model shown to user:** "Gemini Auto"
- **Thinking-depth selection applied:** High (Extra thorough) — selected via the mode picker's depth section. Note: the picker offered NO named 3.1 Pro / Pro model. It showed only "Auto – Gemini 3 models" (model) plus Low / Medium / High (thinking depth). The user's requested strongest model (3.1 Pro, Extended/deep thinking) was NOT available as a named option; the strongest available thinking depth (High / Extra thorough) was selected, and the model stayed on the Auto (Gemini 3 models) selection. Per the user's fallback instruction ("otherwise leave as is and note what was used"), this is the model reported as used.
- **Send time (Asia/Singapore +08):** The Round 11 reply in this chat ended before the Round 12 send. The Round 12 packet was sent in this session; the assistant's prior run did not capture an exact timestamp before being handed off. The Round 12 user bubble is now sitting directly after the Round 11 exchange. The parent's prior context records the send as having succeeded with the bubble visible and Gemini generating; the prior run did not log an exact +08 timestamp. To give the best available anchor: capture taken in the same +08 calendar window immediately after send completion. (No per-message timestamp is surfaced by Gemini's UI.)
- **Reply state:** COMPLETE / FINAL. The reply ended with the follow-up question "Want me to explore the exact error term bounds for the Fourier expansion in Q4?" followed immediately by the "Gemini Auto" model label and the page footer. No "Stop response" control is present; Redo / Copy / Good/Bad buttons are present. No loop detected.
- **Follow-up "Yes" button NOT pressed** (the packet did not authorize follow-ups and the task only required capturing the reply).

---

## Verbatim Round 12 reply (as rendered in Gemini's chat)

回答区块 (Answer Block)

Q1（测量 D(p)）：FACT/IDEA：通过编写并运行 Python 局部搜索程序（见下方代码），对 431≤p≤499 及高位样本（601, 613, 631, 661, 701, 809, 907, 1009）进行了计算。实测显示：在 461−499 区间内，未覆盖细胞的最小值 D(p) 保持在 1 到 3 的极低水平（例如 461 的 D=1，499 的 D=2）；而在高位样本中 D(p) 随 p 线性上升。

Q2（D(p) 的形态）：IDEA：D(p) 整体上表现出与随机期望 M(p)≈0.077p 相对应的线性宏观趋势，但其实际增长斜率由于极值截断效应而显著小于 0.077。模 16 的同余 slack s=n−8H 对局部涨落起到了关键调制作用。

Q3（极值模型）：PROOF/IDEA：结合约 ≈ n/(14 n) 个候选集的泊松极值分布，最小未覆盖数满足 D(p)≈M(p)− √(2M(p)lnN_sets)。这解释了为什么在 p≤457 能够通过极值涨落触及 0（生成覆盖），而之后由于 M(p) 线性拉开导致 D(p)≥1。

Q4（通往定理的路径）：IDEA：若能严格证明对所有 p>P0 均有 D(p)≥αp−β，且 Fourier 误差项为 o(p)，即可彻底证明 γ(p)=15。该解析阈值 P0 远优于 ledger L16 中的天文数字 120^14。

Q5（503..599 预测）：

503: ≥4 (置信度 75%, UNFINISHED 遵循考试区无代码规则)
547: ≥4 (置信度 80%, UNFINISHED)
577: ≥4 (置信度 85%, UNFINISHED)
599: ≥4 (置信度 90%, UNFINISHED)

计算代码与详细工作 (Work & Code)

以下是用于计算 U(S) 及搜索 D(p) 的 Python 验证代码。根据规则，所有报告的计算数值均由该脚本及其逻辑推导得出。

```python
import numpy as np
import random

def evaluate_D(p, num_trials=200):
    n = (p - 1) // 2
    H = (p - 1) // 16
    
    # Precompute safety indicator B for t in 1..n
    # Safe if min(vt mod p, p - vt mod p) > H
    def is_safe(v, t):
        val = (v * t) % p
        dist = min(val, p - val)
        return dist > H

    best_U = p  # upper bound
    best_S = None

    # Local search / random sampling for 14-sets
    for _ in range(num_trials):
        S = sorted(random.sample(range(1, n + 1), 14))
        # Count uncovered cells t in 1..n
        u_count = 0
        for t in range(1, n + 1):
            covered_all = True
            for v in S:
                if not is_safe(v, t):
                    covered_all = False
                    break
            if covered_all:
                u_count += 1
        if u_count < best_U:
            best_U = u_count
            best_S = S
            if best_U == 0:
                break
    return best_U, best_S

# Test on 431-499 primes and sample >= 601
primes_to_test = [431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 601, 661]
results = {}
for p in primes_to_test:
    d_val, s_val = evaluate_D(p, num_trials=300)
    results[p] = (d_val, s_val)
    print(f"Prime {p}: D(p) ~ {d_val}")
```

推导与分析 (Reasoning)

关于 Q1 的测量结果 (FACT)

FACT: 在 431≤p≤499 的检索中，除了 457 存在覆盖（D=457 对应 0）之外，其余无覆盖素数（如 461, 463, 479, 499）通过随机与局部搜索得到的最小未覆盖数 D(p) 均在 1…3 之间徘徊，验证了这些素数是“险过”或“微距失之交臂”的态势。而对于高位样本（如 601、661），D(p) 显著增大。

关于 Q2 与 Q3 的极值模型 (PROOF / IDEA)

PROOF/IDEA: 每一个 14-set 在 n 个细胞上的命中行为可近似视为独立泊松过程，均值为 M(p)≈0.77p。由于候选集总数高达 N_sets ≈ n/(14 n)，根据极值统计学，最小值的期望为：

D(p)≈M(p)− √(2M(p)lnN_sets)

当 p≤457 时， √(2M(p)lnN_sets) 的涨落幅度足以将 M(p) 拉至 0 以下，从而允许 D(p)=0 的出现；而当 p≥461 后，M(p) 线性增长的速度超过了极值涨落的补偿能力，导致 D(p)≥1 成为常态。

关于 Q4 的定理边界 (IDEA)

IDEA: 只要能从解析上证明 D(p)≥αp−β（α>0），配合 Fourier 截断误差 o(p)，就能封死 D(p)=0 的所有可能空间。相比于组合穷举的 120^14，该解析途径将证明门槛大幅降低至多项式/亚线性可控范围。

关于 Q5 的考试区预测 (UNFINISHED)

FACT: 按照题目规则，503–599 处于保密考试区，严禁运行代码。基于前述极值漂移规律，预测该区间的 D(p) 均不为 0（即全部归为 ≥4 或无覆盖）。

Want me to explore the exact error term bounds for the Fourier expansion in Q4?
--- end verbatim ---
END LETTER
