BEGIN REPLY
SEAT: Astra-rerun
CARRIED_BY: Hesper
MODEL: GPT-6 Thinking (Tuzi selected) (as shown on page)
SENT: 2026-10-13 ~12:56 +08 (Tuzi pasted rerun request)
RECEIVED: 2026-10-13 13:13 +08 (Tuzi relayed in Hark chat)
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253
PACKET: 2159b14 (Opus R21 packet) · SEND_TEXT: PT005/hesper/r21-send-texts/
NOTE: Rerun after Puck-carried a78b9c1. Relayed verbatim by Tuzi; C++ files not attached to relay. Hesper independent Python check of the p=37 witness follows in a separate letter.
---

# ANSWER BLOCK · PT005 Round 21 · Astra

VERDICT · PROOF：TARGET LEMMA IS FALSE AT \\(p=37\\).

Tuzi，我已实际重跑 R20c/R20d 的家族枚举器，并用独立程序核验反例。

FACT： \\(p=47\\) 的完整核心家族检查通过：

- Rows：165
- Improper @16p：782,408
- Live @16p：563,648
- Live satisfying L7：563,648
- Live failing L7：0

PROOF： 但在 \\(p=37\\) 的第一个核心家族，找到一个 live improper lift that fails every L7 test。

独立复核还证明：

- 它在 \\(2p,4p,8p,16p\\) 均 improper。
- 它有 64 个 improper children at \\(32p\\)。
- 其中一个 child 又有 64 个 improper descendants at \\(64p\\)。
- 全部允许的偶数 \\(D\mid16p\\) 均不满足 L7。

这不是 Lonely Runner Conjecture 的反例，而是当前 small-prime persistent-family lemma 的反例。

依照你的要求，找到此 witness 后停止其他素数的枚举。

## 1. 实际运行结果

| \\(p\\) | Core               | Rows       | Improper @16p | Live @16p  | Live L7 PASS | Live L7 FAIL |
| ------- | ------------------ | ---------- | ------------- | ---------- | ------------ | ------------ |
| 47      | 123589111213141520 | 165        | 782,408       | 563,648    | 563,648      | 0            |
| 17      |                    | UNFINISHED | UNFINISHED    | UNFINISHED | UNFINISHED   | UNFINISHED   |
| 19      |                    | UNFINISHED | UNFINISHED    | UNFINISHED | UNFINISHED   | UNFINISHED   |
| 23      |                    | UNFINISHED | UNFINISHED    | UNFINISHED | UNFINISHED   | UNFINISHED   |
| 29      | No ≤13-core        | 0          | 0             | 0          | 0            | 0            |
| 31      | No ≤13-core        | 0          | 0             | 0          | 0            | 0            |
| 37      | 1347910111216      | 1 started  | UNFINISHED    | ≥1         | UNFINISHED   | ≥1           |

FACT： \\(p=17,19,23\\) 的初始家族运行达到限时，没有完成，因此不报告推测计数。\\(p=37\\) 在第一行发现反例即终止，整行及整家族总数均未声称完成。

PROOF： 对 \\(p=29,31\\)，计算得到 \\(H=1\\)，而折叠时间格分别有 \\(14\\)、\\(15\\) 个。任何至多 13 个速度类都无法覆盖全部格子，所以相应核心家族为空。这不代表整个 prime gate 已关闭。

### \\(p=47\\) 分批计算证书

| Batch | Rows | Improper @16p | Live @16p | Live failing L7 |
| ----- | ---- | ------------- | --------- | --------------- |
| 1     | 40   | 254,528       | 196,416   | 0               |
| 2     | 40   | 178,248       | 127,040   | 0               |
| 3     | 40   | 156,416       | 107,840   | 0               |
| 4     | 45   | 193,216       | 132,352   | 0               |
| Total | 165  | 782,408       | 563,648   | 0               |

FACT： 各批实际 wall time 相加为 44.1325 秒。这是所选家族的完整实测，不是整个 \\(p=47\\) reducible branch 的估计。

## 2. \\(p=37\\) · 完整反例

FACT： 基础 row：

```
R = [1, 2, 3, 4, 5, 6, 7, 8,
     9, 10, 11, 12, 13, 14, 16]
```

它包含经过逐格验证的 9-speed covering core：

```
C = [1, 3, 4, 7, 9, 10, 11, 12, 16]
```

反例 lift \\(W\\) at \\(16p\\)：

[112, 2, 336, 448, 5, 6, 192, 8,  416, 528, 48, 160, 13, 14, 16]

&#x20;Copy witness

### A. Improperness independently verified

| Level     | \\(N\\) | Odd coordinates | Uncovered grid times |
| --------- | ------- | --------------- | -------------------- |
| \\(2p\\)  | 74      | 2               | 0                    |
| \\(4p\\)  | 148     | 2               | 0                    |
| \\(8p\\)  | 296     | 2               | 0                    |
| \\(16p\\) | 592     | 2               | 0                    |

PROOF： 全部网格时间均被覆盖，并且每层具有至少两条奇速度，因此所有 pre-odd/q2 screens 均通过。

### B. Every L7 test fails

设

\\[ L(D)=\sum\_{i:D\nmid w_i}\gcd(D,w_i) \left\lceil\frac{D/\gcd(D,w_i)}8\right\rceil. \\]

| \\(D\\) | \\(\|E\|\\) | \\(L(D)\\) | 是否 \\(L(D)\<D\\) |
| ------- | ----------- | ---------- | ---------------- |
| 2       | 2           | 2          | NO               |
| 4       | 5           | 8          | NO               |
| 8       | 5           | 8          | NO               |
| 16      | 6           | 18         | NO               |
| 74      | 15          | 150        | NO               |
| 148     | 15          | 298        | NO               |
| 296     | 15          | 588        | NO               |
| 592     | 15          | 1,170      | NO               |

PROOF： 所有偶数除数均已检查，没有一个满足 L7 的严格不等式。

### C. The lift remains live

FACT： 全部 \\(2^{15}=32768\\) 个 \\(32p\\) children 已逐一检查。

其中 64 个 improper。

第一个 improper child：

```
[704, 2, 928, 448, 5, 6, 192, 8,
 416, 1120, 640, 160, 13, 14, 608]
```

FACT： 对该 child 再完整枚举 \\(64p\\)：

- Improper children at \\(64p\\)：64
- 第一个存活向量：

```
[704, 2, 2112, 448, 5, 6, 192, 8,
 1600, 2304, 640, 1344, 13, 14, 1792]
```

独立逐格检查确认它在 \\(64p\\) 仍无 uncovered time，并满足 odd-coordinate screen。

因此：

\\[ \boxed{ \text{Improper at }16p \ \land\ \text{Live at }32p \ \land\ \neg L7 } \\]

反例成立。

## 3. 实际运行的代码

本轮使用两份 C++ 程序，均已在当前环境中编译执行。

R21 Astra · Family Enumerator

由 R20c/R20d 扩展，按精确定义生成 improper lifts、检查 L7，并检测 \\(32p\\) 存活子代。

Independent Witness Verifier

逐格检查 \\(2p\\) 至 \\(64p\\)、L7 除数，以及所有 \\(32p\\) 和指定 \\(64p\\) children。

p=37 Witness Output

实际运行日志，含 row、lift、child、全部 L7 数值与运行时间。

Independent Verification Output

独立复验的完整整数计算结果。

主要执行命令：

```

g++ -O3 -std=c++17 pt005_r21_astra.cpp -o r21

# p=47: complete family, four independent batches
./r21 47 40 0
./r21 47 40 40
./r21 47 40 80
./r21 47 45 120

# No <=13-speed cover core
./r21 29 1 0
./r21 31 1 0

# Stops on the first live L7 failure
./r21 37 1 0

# Independent verification of p=37
g++ -O3 -std=c++17 \
  pt005_r21_verify_witness.cpp -o verify

./verify

```

最关键的子代检查代码如下，直接来自本轮独立验证程序：

```

for (int mask = 0; mask < (1 << K); ++mask) {
    vector<uint64_t> covered(words, 0);

    for (int i = 0; i < K; ++i) {
        const auto& z =
            opt[i][(mask >> i) & 1];

        for (int j = 0; j < words; ++j)
            covered[j] |= z[j];
    }

    bool full = true;
    for (int j = 0; j < words; ++j) {
        if ((covered[j] & required[j])
            != required[j]) {
            full = false;
            break;
        }
    }

    if (full) {
        ++improperChildren;
    }
}

```

每个 `opt[i][bit]` 都由精确整数同余生成，只覆盖下一层的奇数时间。偶数时间由 improper parent 的条件保证。

## 给主席的结论

PROOF： \\(p=37\\) 这一条明确的 lifted row 已足以否定 Round 21 的 universal live-lift lemma。

因此不能再用：

\\[ \text{Live at }16p\Rightarrow L7 \\]

作为所有小素数家族的统一封门定理。

IDEA： 下一条可研究的修正版，是将 L7 与另一种可验证的连续 good-time 证书联合使用。但必须先处理上面这条 \\(p=37\\) witness，不能因为它通过多层 lifting 就预设它最终不会死亡。

Final status：\\(p=47\\) 所选完整家族 PASS；\\(p=37\\) 找到经过独立核验的 live L7-failing lift；Round 21 target lemma FALSE。


END REPLY
