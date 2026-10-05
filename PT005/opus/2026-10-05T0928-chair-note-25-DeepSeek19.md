# PT005 主席评语 25 · DeepSeek 第 19 号（墙 79–80）：L7 的第二位读者

主席：Opus · 2026-10-05 09:28 +08（取自机器时钟）
读了：Puck 信 49a0910；DeepSeek 原文全文（sha256 7a4b1403…，4,353 字节，与信中一致）

## DeepSeek 的结论

- **引理本身：HOLDS。** Q1 的 (a) 到 (e) 逐项核对。特别是 (b)：开弧最多含 ⌈D_i/8⌉ 个格点，D_i 是 8 的倍数和 D_i < 8 两种情形都单独检查了，没有差一的错。D = 8 的表也对。
- **在作者 Lemma 2.2(ii) 里的用法：INCOMPLETE。** 理由是：引理要求 e ≥ 2，但主席的包没有说明，为什么每个不当提升都满足 e ≥ 2。

## 主席的回应：这个缺口是真的，但已经有答案，只是主席的包没附上

在二进制层级 L = 2ʲ：

1. 如果一个提升最多只有 1 个奇数坐标，那就取 i 为那个奇数坐标（没有奇数坐标时，i 任取）。其余坐标全是偶数，所以 gcd(L, 其余坐标) ≥ 2 > 1。按定义的 (a)，这个提升是 **proper**（合格）。
2. 所以**每个不当（improper）提升至少有 2 个奇数坐标**。
3. 奇数不会被任何偶数 D 整除，而主席用的 D 全是偶数（2、4、8、16）。所以奇数坐标全在 E 里，**e ≥ 2 对每个不当提升都成立**。

出处：
- Astra 的说明文件 README.md 第 45 行原文："an improper lift at a binary level has at least two odd coordinates, since otherwise it satisfies the gcd condition"；
- 第 110 行还说明了：在更高的二进制层级，奇偶性不变（加上的是 l·p，l 为偶数）；
- 程序里也有对应的检查：shift_check.cpp 第 60 行 `if(odd<2)return false;`，cover_and_shift.py 第 26 行 `assert … >= 2`。

**这是主席的疏漏：** 给 DeepSeek 的包只引了引理，没有引这一段。DeepSeek 在材料不全的情况下标出 INCOMPLETE，是正确的读者做法。

DeepSeek 另外提到 (d) 用到了"总共 15 个速度"。这个前提在 16 名跑者的设定里本来就成立，主席同意要写明。

## 建议（等 Tuzi 批准）

把 L7 从 CHAIR-CHECKED 升为 **HAND-CHECKED**，范围写成：

> 引理本身由主席、DeepSeek 两位非作者核对。用于 Lemma 2.2(ii) 时，要求 D 是偶数且整除 L·p，而 e ≥ 2 由上面三行的奇偶论证得到。这个论证由主席补上，出处是 Astra 的说明。

**谨慎起见：** 如果 Tuzi 希望这三行奇偶论证也有第二位读者，可以把本评语转给 DeepSeek 再看一次。这只需一条消息，不花钱。
