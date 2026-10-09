BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 11:13 +08
RE: 猜公式 Round 3 packet (1aeab1c), rules header + own §A line + BEGIN…END block pasted verbatim (send text r3_send_gemini.txt)
SEAT: gemini
MODEL: Gemini 3.1 Pro Extended thinking (captured via page extract)
CHAT: https://gemini.google.com/app/1e00ae12d64748b9

--- reply verbatim ---
【答卷区块 / ANSWER BLOCK】

§A. Cross-reading

Target 1 (Kimi 2b): YES. Exact step: "Dividing by the gcd helps only when the gcd is ≥2".

FACT: 若集合的 gcd≥2，所有速度除以它会严格按比例缩小集合中的最大速度，这直接有助于满足小速度条件。

Target 2 (Chair's product bound claim): YES. Exact step: "The author's product bound (log 414.779 for 14 speeds) gives no extra margin for Lemma A."

PROOF: Lemma A 需要找到一种 Dirichlet 缩放，使得最大速度 M 满足 56M≤p（即必须将速度压缩得极小）。然而 14 种速度的 product bound 只能在理论上保证存在一种缩放使最大速度被约束在 ≈414.779 左右。因为 414.779>56，该上界处于 Lemma A 所需的安全门槛之外，因此它没有为定理提供任何可用的额外 margin。

§B. The attack (路线 1：Discrepancy route)

FACT: 依据已知对 13 个速度成立的 Lonely Runner 猜想 (F5)，必定存在一点 x∗，使得对于所有的 v∈S 皆有 ‖vx∗‖≥1/14。

PROOF: 因为 1/14>1/16，在 x∗ 附近必然存在一个安全邻域。为了维持 ‖vx‖≥1/16，只需满足 |vx−vx∗|≤1/14−1/16=1/112。因此，由最大速度 vmax 决定，在圆环上至少存在一个长度为 2/(112·vmax) 的安全片段。

FACT: 对于 13 个速度组成的集合，其生成的安全片段（safe pieces）总数 k 的理论绝对上限为 ∑_{v∈S} 2v。

IDEA: 对于 1/16 阈值下的 13 个速度，存在一个不依赖于具体速度取值的全局总长度下界 L0>0。我推测其实际极限总测度就徘徊在数据揭示的 0.113 附近。

PROOF: 假设取 L=0.114 作为下界，若想通过 pL>k 路线证明它无法构成 cover，代入 k≤13p/N，必须满足 0.114>13/N，即要求缩放因子 N>114。

FACT: 要求 N>114 明显比 Lemma A 中原本的 N≥56 条件更苛刻、更难达成。

IDEA: 综上，基于 worst-case 的朴素片段计数法必然无法击败 56 的门槛。若要在这个路线上获胜，证明必须转向 (iii) 针对网格点的加权计数（Weighted count），或 (i) 利用数论关系剔除大量重合的端点从而大幅压缩片段数 k 的上限。

§C. One name

推荐人: Terence Tao (陶哲轩)

理由: 他在 Lonely Runner Conjecture 和加性组合学（尤其是 Bohr 集合的结构与网格重合度测算）上的深刻工作，最适合审查此类高度依赖 Discrepancy 测度和局部网格点空洞分析的下界证明。

最不确定的步骤 (Least sure step):
我最不确定的是 §B 中的第一个 IDEA：即是否存在一个绝对的、与最大速度及 p 皆无关的全局总测度下界 L0≈0.113。当速度呈现高度结构化的指数跳跃或存在特殊谐波共振时，我怀疑多个 1/8 的危险区间会错开得更完美，从而将总安全测度压缩到低于 0.113 的未知极小值。
--- end verbatim ---
END LETTER
