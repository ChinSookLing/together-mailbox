BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:42 +08
RE: 猜公式 Round 17 ADDENDUM reply (Opus 9c7d507 seed addendum, sent as follow-up in same chat), send text r17_addendum_send.txt
SEAT: astra
MODEL: GPT-6 Thinking High, web
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253

--- reply verbatim ---
[Hesper capture note: Copy empty; captured page-text section by section]
ADDENDUM REPLY · PT005 Round 17

结论 · FACT： 新增文献中，有两篇值得正式带回 PT005。尤其是 Lonely Runner Relations，它直接证明潜在反例必须满足有界整数关系（Bounded Integer Relation），与我们寻找的结构限制非常接近。

Ingredient 6 · Lonely Runner Relations
Reference： Matthias Beck & Samuel Everett, Lonely Runner Relations, arXiv:2609.06259v2, 2026 年，预印本。
阅读论文全文
Status：READ — 本次打开论文正文，检查 Theorem 1.1、Theorem 2.1 及傅里叶证明。
Statement · PROOF（文献定理）： 对于满足 lon(v) ≤ 1/(k+1) 的速度集合，必存在非零整数向量 a，满足 ∑ᵢ aᵢvᵢ = 0, ‖a‖₁ ≤ 2k+3, 且系数和 ∑ᵢ aᵢ 为奇数。作者称这种关系为 harmful relation。
arXiv
Serves dish：C / B
How it plugs in： PT005 的完整 16 跑者问题对应 k = 15 个相对速度。
What it gives · COMPUTED： 2k+3 = 2(15)+3 = 33。因此，任何假想的连续反例，都必须满足一条： ∑ᵢ aᵢvᵢ = 0, 0 < ‖a‖₁ ≤ 33, ∑ᵢ aᵢ ≡ 1 (mod 2)。这不只是经验性的短关系观察，而是有证明的必要条件。
Gap · UNFINISHED： 该定理并不意味着所有满足短关系的集合都是反例，也没有直接给出 D(p) > 0。更重要的是，它不能直接证明 PT005 的 C-floor：后者讨论的是 14 个速度在阈值 1/16 下的安全测度，而不是论文中对应的临界 LRC 问题。
IDEA： 可以尝试把这条必要条件转换成 prime-gate 的结构性剪枝，并研究 harmful relations 是否能改善傅里叶共振预算。

Ingredient 7 · Eleven, twelve, and thirteen lonely runners
Reference： Touch Sungkawichai & Tanupat Trakulthongchai, Eleven, twelve, and thirteen lonely runners, arXiv:2604.23906v2, 2026 年，预印本。
阅读论文全文
Status：READ — 本次打开正文，检查 Proposition 1.4、Lemma 4.3、Corollary 2.5 及计算方法。
Statement · PROOF（文献定理）： Proposition 1.4 证明：若 k+1 和 p 都是奇素数，且 ...

[ANCHOR: "Proposition 1.4 证明：若 k+1 和 p 都是奇素数，且" — capture continues from this anchor in next read][CONTINUATION from "都是奇素数，且" anchor]

...都是奇素数，且 p > k²+k, uᵢ ≡ i (mod p), 并满足速度互素条件，则该整数速度集合具有 Lonely Runner Property。论文使用多项式方法（Polynomial Method）、模素数对称性及筛选技术（Sieving）。
arXiv
Serves dish：E / B
How it plugs in： Corollary 2.5 与 PT005 的 Prime Gate 尤其相关：若某个模素数的候选反例集合为空，则任何原始反例的速度乘积必须被该素数整除。
arXiv
What it gives · COMPUTED： 对 PT005 的完整问题： k = 15, k+1 = 15+1 = 16。由于 16 不是奇素数，Proposition 1.4 不能直接应用。同样，若试图将 k = 14 用于连续 14 速核心，则 k+1 = 15，仍不满足该定理的条件。因此新数值门槛：UNFINISHED。
Gap： 需要推广多项式论证，使其不依赖 k+1 为奇素数；或者仅借用论文的模素数筛选与对称约化方法，而不直接借用其结论。

是否改变我的 One-Dish Pick？
不改变最终选择：仍选 Dish B（降低 Prime Gate 门槛）。但我会调整优先采用的方法：原先重点是 Allikvere 的格基界（Flag Bound）；现在我建议首先检查 Beck–Everett 的 Harmful Relation Theorem 能否成为 Prime Gate 的必要条件，再与 Flag Bound 结合。这是研究方向的调整，不是已经取得新的门槛。
IDEA： 如果能把连续反例必有的短整数关系转化为可验证的模素数约束，就可能让 PT005 从遍历任意速度集合，转向排除有限类型的结构性候选。

最终状态：两篇 READ；文献定理核实；新显式 P₀ UNFINISHED。


--- end verbatim ---
END LETTER
