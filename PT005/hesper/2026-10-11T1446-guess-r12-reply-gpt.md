BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 14:58 +08
RE: 猜公式 Round 12 (packet c9a646a), send text r12_send_full.txt or r12_send_short.txt
SEAT: gpt
MODEL: GPT-6 Power High (fresh chat)
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932/c/6acb3150-2f20-83ec-8f22-82b1f371fad7

--- reply verbatim ---
PT005 Round 12 — Final nudge reply (captured via extract_content after nudge)
===================================
Chat URL: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932/c/6acb3150-2f20-83ec-8f22-82b1f371fad7
Project: Play Civilisation Field (https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932/project)
Model shown on reply: ChatGPT (the reply's "Latest response" label reads "High", i.e. Thinking effort Max/Power — consistent with GPT-6 + Power/Max). No explicit "GPT-6" model name is printed on the reply; ChatGPT's reply header only shows "ChatGPT said".
Send time Asia/Singapore (+08): UNKNOWN / UNCAPTURABLE (the ChatGPT web UI exposes no per-message timestamp; confirmed in prior session via More menu, Share prompt dialog, Recents, find_text, screenshots, and memory/Hark searches).
Completion status: Reply is FULLY COMPLETE. No "Connection interrupted" banner remains. The chat's title auto-renamed to "Review packet answers" and its sidebar entry changed to the same; the Share button became enabled; the composer reverted to "Start Voice" (no Stop button); "400 Copy response" was visible.
Note on Copy button: The Reply's Copy button (center 756,1266) consistently copies the nudge user-message text ("Please give the final answer now, ANSWER BLOCK first, UNFINISHED allowed.") instead of the assistant's reply — a known ChatGPT web-copy quirk on this chat. The verbatim reply below is taken from extract_content(full) and is the complete final reply with no truncation.

=== VERBATIM REPLY (from extract_content, final nudge reply) ===

PT005 · 猜公式 Round 12 · ANSWER BLOCK

Q1 — FACT（独立计算）

对允许区间完成了随机贪婪搜索（randomized greedy search）与单元素替换优化（local search），每个质数进行最多 85 次初始化。

431≤p≤499：找到的最佳 U(S) 为 0–3。

601≤p≤1009：抽样 7 个质数，最佳 U(S) 为 4–7。

p=457：找到并重新验证 U(S)=0。

PROOF： 搜索结果证明 D(p)≤U(S)，但除 U=0 外，不证明最小性。

Q2 — FACT / IDEA

全部样本的搜索上界线性拟合：

U_best(p)≈0.0093303p−2.24644.

高区间样本斜率约 0.00630。增长明显慢于随机均值 M(p) 的渐近斜率约 0.077，但不能据此证明 D(p) 的增长率。

余量 s=n−8H 可能有影响，目前数据不能确认因果关系。

Q3 — IDEA

独立 Poisson 极值模型预测：

Pr(D(p)≤k)≈1−exp[−K(p)Pr(Pois(M(p))≤k)], K(p)=(n choose 14)/n.

该模型低估了候选集合之间的相关性的重要程度；在已知无覆盖的部分质数上仍预测最小值为零。

Q4 — UNFINISHED

线性下界 D(p)≥αp−β 尚未证明。缺少有效的 Fourier 误差界，不能给出可信的有限 P0。

Q5 — IDEA（盲预测，低信心）

质数 | 预测类别 | 信心
503 | 2–3 | 低
547 | 2–3 | 低
577 | ≥4 | 低
599 | ≥4 | 低

这些是模型预测，不是计算得到的 D(p)。禁止区间没有执行任何代码。

WORK

1. FACT — 独立搜索结果

每一行给出可复核的完整速度组 S。
表中的 U 是实际重新计算的安全格点数，均为 D(p) 的上界。

p | U | 最佳速度组 S
431 | 2 | 4,37,62,64,66,87,105,136,167,171,194,196,198,202
433 | 2 | 24,28,37,65,79,126,127,149,163,177,186,191,205,214
439 | 2 | 22,28,47,53,75,78,103,128,131,153,172,179,213,219
443 | 2 | 13,15,19,33,34,43,53,72,87,104,121,129,140,197
449 | 1 | 20,21,41,61,82,83,102,106,118,123,143,184,204,224
457 | 0 | 1,30,34,56,57,58,118,144,170,171,172,173,201,228
461 | 2 | 6,22,34,46,55,62,99,104,106,121,150,167,173,190
463 | 3 | 1,10,72,106,107,109,138,139,140,142,160,165,215,217
467 | 3 | 8,33,34,49,53,78,90,123,131,134,164,176,192,213
479 | 2 | 26,40,42,81,107,110,115,136,152,165,178,191,217,225
487 | 2 | 30,31,51,59,61,91,92,106,137,152,167,168,229,243
491 | 2 | 3,10,26,49,118,120,127,130,153,202,205,208,228,234
499 | 2 | 19,62,76,95,107,114,126,135,145,164,183,202,221,240
601 | 4 | 20,23,56,66,72,129,138,161,164,210,230,233,253,299
607 | 4 | 7,62,69,76,100,131,162,169,176,179,231,245,251,276
613 | 4 | 32,64,69,96,102,133,160,197,224,229,239,256,261,288
701 | 5 | 23,45,68,113,136,158,181,204,226,249,271,294,317,341
809 | 5 | 32,47,64,79,111,175,190,222,254,286,301,333,365,397
907 | 7 | 23,62,101,124,163,186,225,248,287,310,349,372,411,434
1009| 6 | 13,56,69,125,138,194,263,276,332,345,401,414,470,483

2. FACT — 计算程序

以下是本次实际运行的搜索核心。种子固定，结果可复现。

Python
Run

import random

r = random.Random(12)

ps = [
    431,433,439,443,449,457,461,
    463,467,479,487,491,499,
    601,607,613,701,809,907,1009
]

def search(p, starts=85):
    n = (p-1)//2
    H = (p-1)//16
    full = (1 << n)-1

    safe = [0]*(n+1)
    for v in range(1,n+1):
        mask = 0
        for t in range(1,n+1):
            z = v*t % p
            if min(z,p-z)>H:
                mask |= 1 << (t-1)
        safe[v] = mask

    best = (n+1, [])

    for trial in range(starts):
        chosen = []
        used = set()
        remaining = full

        for j in range(14):
            cand = sorted(
                ((remaining & safe[v]).bit_count(),
                 r.random(),v)

3. FACT — 曲线及 Poisson 模型

[Chart listing of each p with its 搜索最佳 U(S), plus Poisson fitting code:]

import math
import numpy as np
from scipy.stats import poisson

data = []

for p,u,S in rows:
    n = (p-1)//2
    H = (p-1)//16
    slack = n-8*H

    M = (p/2)*(1-(2*H+1)/p)**14
    logK = (
        math.lgamma(n+1)
        - math.lgamma(15)
        - math.lgamma(n-13)
        - math.log(n)
    )

    kev = next(
        k for k in range(n+1)
        if poisson.logcdf(k,M)+logK >= 0
    )
    data.append((p,u,slack,M,logK,kev))

for subset in [data,data[:13],data[13:]]:
    x = np.array([a[0] for a in subset])
    y = np.array([a[1] for a in subset])
    s = np.array([a[2] for a in subset])

    print("linear:", np.polyfit(x,y,1))
    X = np.column_stack((np.ones(len(x)),x,s))
    print("p+slack:", np.linalg.lstsq(
        X,y,rcond=None
    )[0])

FACT — 余量回归：

全样本的拟合为
U_best ≈ −2.71421 + 0.00948102 p + 0.0994884 s.

不过这一余量系数是探索性结果，尚不足以建立结构规律。

IDEA — 极值模型的缺陷：

独立模型把约 K(p) 个集合视为独立样本。但速度集合有大量重叠，它们的未覆盖格点也共享算术结构。有效独立样本数可能远小于 K(p)。

因此应考虑：
K_eff(p) << K(p),

并通过实际集合之间的相关性来定义或估计 K_eff，而不是任意引入调整系数。

4. PROOF / UNFINISHED — 通往定理

假设未来证明：
D(p)≥αp−β, α>0

并具有统一有效的 Fourier 误差估计 E(p)=o(p)，则当

αp−β−E(p)>0

时，可排除 14-cover。

PROOF： 只要所使用的下界确实适用于所有候选集合，右侧严格为正便意味着不存在零缺口集合。

UNFINISHED： 尚未证明正的 α，也没有明确可计算的 E(p)，因此无法从本轮推出 P0。

比较基准由上面程序计算：
120 choose 14 = 128391846454886400000000000000.

5. IDEA — 禁算区间预测依据

只使用已计算的两个端点 U_best(499)=2 与 U_best(601)=4，作最简单的线性外推：

U^(p) = 2 + (p−499)/51.

以下为手算，不是禁算区间的程序运行：

503: 2+4/51≈2.078，取类别 2–3。
547: 2+48/51≈2.941，取类别 2–3。
577: 2+78/51≈3.529，取类别 ≥4。
599: 2+100/51≈3.961，取类别 ≥4。

IDEA： 这是对搜索上界的插值外推，再用就近整数映射至类别；它并不是对真实 D(p) 的可靠概率模型。因此全部标记低信心。

Least-sure step： 把随机局部搜索得到的上界曲线当作真正的最小缺口曲线，尤其在尚未完成精确最小化的高质数区间。这个推断目前没有证明。

最终状态： 计算和速度组验证已完成；线性规律、有效独立样本数、统一正下界及有限 P0 均为 UNFINISHED。
--- end verbatim ---
END LETTER
