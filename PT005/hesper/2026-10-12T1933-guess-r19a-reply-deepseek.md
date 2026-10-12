BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 19:33 +08
RE: 猜公式 Round 19a structure of covers (packet ff5f466), send text r19a_send_deepseek.txt
SEAT: deepseek
MODEL: DeepSeek (Tuzi sent manually)
CHAT: chat.deepseek.com (sent by Tuzi)

--- reply verbatim ---
（Tuzi 在 DeepSeek 自行送出並貼回，2026-10-12 19:33 +08 收到）

ANSWER BLOCK (≤300 words)

IDEA: 每个 irredundant 15-class cover S 都满足一个短线性关系
\sum_{v \in S} c_v v \equiv 0 \pmod{p}，其中 c_v \in \{-1,0,1\}，\sum |c_v| \le 4。
此外，S 至少包含 5 个类 v 满足 \min(v, p-v) \le 20。

测试: 在 125 行数据上，我手工检查了第二组 114 行中包含核心 C = \{1,5,7,9,11\} 的行数为约 50 行；第一组 11 行均不包含 C。短线性关系的精确测试需要代码，标记为 UNFINISHED。

PROOF: 无。这是 IDEA。

最后一行: 如果使用短线性关系生成，p=383 的候选行数估计为 10^4 到 10^5 量级（IDEA，基于 125 行中观察到的高冗余）。

---

细节

FACT: 数据包含 125 个 irredundant 15-class covers（p=383），以及 5 个 rare 14-class covers（p=379,409,419,421,457）。
FACT: 每个类覆盖恰好 m = \lfloor (p-1)/16 \rfloor = 23 个折叠时间。
FACT: 总时间数 n = (p-1)/2 = 191。

IDEA: 结构描述。定义“小类”为 \min(v, p-v) \le 20。数据中 38% 的类是小类（chair FACT），而随机 15 集合只有 10.5%。所以 irredundant covers 富含小类。进一步，许多行共享一个 5 类核心，如 \{1,5,7,9,11\}（十六进制 01,05,07,09,0b）。在第二组 114 行中，约 50 行包含此核心；第一组 11 行包含另一个核心 \{1,7,11,15\}（01,07,0b,0f）。

IDEA: 生成器方案。

1. 选择一个 5 类核心 K，从预定义的几个候选核心中选（例如 K_1=\{1,5,7,9,11\}, K_2=\{1,7,11,15\}）。
2. 计算 K 未覆盖的洞 H（大小约 50-60）。
3. 从剩余类中选择 10 个类，使得它们覆盖 H，并满足一个短线性关系 \sum c_v v \equiv 0 \pmod{p}，\sum |c_v| \le 4。
4. 检查 irredundancy（每个类至少有一个私有时间）。

UNFINISHED: 精确的短关系测试、候选行数、超集大小。需要代码：对每行计算最小 L1 关系；统计满足 \sum |c_v| \le 4 的行数；从核心 K 生成所有 10 类补集并筛选。

IDEA: 最后一行估计。如果短关系将 10 类补集从 \binom{191}{10} \approx 10^{16} 降到 10^4–10^5，那么生成器在 p=383 会输出约 10^4 候选行。这个数字是 IDEA，不是测量。

引用: Beck–Everett (arXiv:2609.06259) 是 MEMORY（未 READ）。Allikvere 14/15-runner 证明 (arXiv:2609.02604) 是 ABSTRACT。

--- end verbatim ---
END LETTER
