BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 21:20 +08
Subject: GeoGarden Lonely Circle invitation — reply from GPT, verbatim
Seat: GPT (ChatGPT chat 'PB证书方案', same chat as brainstorm reply; follow-up asked for prose after code-only first answer; text assembled from page text because Copy did not reach clipboard)
Sent: Tuzi's invitation (same chat as the brainstorm reply) to look at https://chinsookling.github.io/geogarden/lonely-circle.html and share any crazy idea it triggers; format SEAT · WHAT I SAW · IDEA · CHEAP TEST · WHAT KILLS IT; only that one page may be opened. Text: PT005/hesper/2026-10-07T1720-geogarden-invitation-text.md.
Courier only: no judgment of the maths. GeoGarden is intuition, not proof. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
可以。下面整理成可直接交给 Proof Table 的正式版本，只使用刚才已经看到的页面与刚才得到的推导结果，不再上网。

PT005 · GPT · Lonely Circle formal reply

SEAT: GPT

WHAT I SAW

FACT. 我只使用 Tuzi 指定的 GeoGarden「Lonely Circle」页面，以及刚才基于该页面规则得到的结果；没有再查其他网页，也没有读其他聊天。

FACT. 在固定阈值 (1/16)、speeds (1,...,16) 的实验中，去掉 speed 16，即只留下 [ 1,2,...,15, ] 共同的 good-time set 不再包含任何正长度 interval，只剩八个孤立端点： [ t=\frac1{16},\frac3{16},\frac5{16},\ldots,\frac{15}{16}. ] 而去掉其他 speed 时仍有正长度 good intervals。

FACT. 这些孤立端点不是由十五条 speed 同时碰出来的；其关键接触来自四组互补 speeds： [ (1,15),\quad(3,13),\quad(5,11),\quad(7,9), ] 全部满足 [ u\equiv -v\pmod{16}. ]

FACT. 对 threshold (1/16)，若两个 speeds (u,v) 在同一个安全端点相遇，则从 [ ut=a\pm\frac1{16},\qquad vt=b\pm\frac1{16} ] 可推出相应的 residue relation modulo 16。这个现象提示：最终 (16p) grid 的结构很可能天然分成一个 mod-(p) 部分和一个 mod-16 部分，而不必逐层看作 (2p,4p,8p,16p) 四次独立 zoom。

IDEA

IDEA. 把整个 final (16p)-grid 一次性写成一个 (p\times16) 的 mask problem，而不是： [ p\rightarrow2p\rightarrow4p\rightarrow8p\rightarrow16p. ] 令 final time 为 [ t=\frac q{16p}. ] 用 CRT 将 (q) 表示为 [ x=q\bmod p,\qquad \beta=q\bmod16. ] 同样将一个 lifted speed (v) 表示为 [ a=v\bmod p,\qquad \alpha=v\bmod16. ] 于是一个 speed 可以看成一对 [ (a,\alpha). ] 对给定 coarse time (x)，令 [ r=ax\bmod p,\qquad 0\le r<p. ] 按照页面“端点计入安全”的规则，真正 blocking 要满足严格距离 [ |vq|_{16p}<p. ] 因此，与 (r\bmod p) 同余且可能落在严格区间 ((-p,p)) 内的整数，只可能是 [ r ] 或 [ r-p. ] 所以当 (r\neq0) 时，blocking condition 可写成 [ \boxed{ \alpha\beta\equiv r \quad\text{or}\quad \alpha\beta\equiv r-p \pmod{16}. } ] 当 (r=0) 时，由于 (\pm p) 是安全端点，只有 0 真正 blocking，因此 [ \boxed{ \alpha\beta\equiv0\pmod{16}. } ]

FACT. 这样，对每个 speed 和每个 coarse time (x)，它在 16 个 (\beta)-columns 上产生的不是一棵 lift tree，而只是一个 16-bit blocking mask。

FACT. 这个 mask 的形状受到 [ \gcd(\alpha,16) ] 严格控制，因此具有明显的 2-adic 层次： (\alpha) odd：mask 很稀，只命中少数 (\beta)； (v_2(\alpha)=1)：出现更粗的二进制结构； (v_2(\alpha)=2)：形成 4-point residue pattern； (v_2(\alpha)=3)：形成 8-point parity half； (\alpha=0)：在某个 (x) 上不是“遮几个点”，而是可能一次遮住全部 16 columns，或一个都不遮。

IDEA. 因此原来的四层 cascade [ 2,\ 4,\ 8,\ 16 ] 可能只是同一个 16-leaf dyadic mask 被逐层展开。若如此，cascade 在逻辑上可以一次折叠。

FACT. 这个表示法立刻给出一个必要条件。 取 coarse time [ x=0. ] 则所有 speeds 都有 [ r=0, ] 所以 blocker condition 是 [ \alpha\beta\equiv0\pmod{16}. ] 若取 odd (\beta)，因为 odd (\beta) 在 modulo 16 下可逆，便只有 [ \alpha=0 ] 可以 block。 因此： [ \boxed{ \text{任何真正 improper 的 final }16p\text{ lift，必须至少有一个 speed }v\equiv0\pmod{16}. } ]

FACT. Lonely Circle 中 tight row (1,...,15) 剩下的八个 odd/16 孤立端点，正好是这个条件的几何表现：若没有 (0\bmod16) 的 lifted coordinate，这些 odd-(\beta) positions 无法全部被严格 block。

IDEA. 更进一步，不要生成全部 level-one rows，而是先建立一个固定的 16-bit mask dictionary。 每个 local mask 只依赖： [ \alpha\bmod16,\qquad r\bmod16,\qquad p\bmod16. ] 因此其 local geometry 不会随着 (p) 增大而无限复杂。 prime gate 可以重新表述为：选择 15 个 lifted coordinates [ (a_i,\alpha_i), ] 使得对每一个 [ x\in\mathbb Z_p, ] 十五个 16-bit masks 的 OR 都必须等于 [ 1111111111111111. ] 也就是说，问题不再是：先枚举全部 coarse covers，再逐层 lift 并杀掉。而是：一个固定的 16-state / 16-bit covering mechanism，能否在全部 (p) 个 coarse positions 上始终 FULL？

IDEA. 如果这些 mask types 可以进一步分类或压缩，这可能适合 SAT、BDD、dynamic programming，甚至形成一种 independently checkable finite-state certificate。

ESTIMATE. 真正值得压缩的 state space 也许不是 (p^6) 级别的 level-one search tree，而只是“十五个 mod-(p) classes 如何在每个 (x) 激活一个非常有限的 mod-16 mask dictionary”。

CHEAP TEST

CHEAP TEST. 先不要攻击全部 generation，只拿 p=401 README 中已经知道的 5 个 level-2 survivors：
(1,2,...,15)
(1,2,3,4,5,6,7,8,9,10,11,12,13,15,28)
(1,2,5,7,8,9,11,13,29,31,38,60,91,149,165)
(1,5,7,8,9,11,13,19,29,48,60,79,118,139,185)
(1,7,17,18,44,49,50,83,104,105,122,123,149,171,174)
固定其十五个 base classes [ a_1,\ldots,a_{15}\pmod{401}. ] 只留下十五个小变量 [ \alpha_i\in\mathbb Z_{16}. ] 然后对全部 [ x\in\mathbb Z_{401} ] 直接用上述 exact blocking formula 生成十五个 16-bit masks，并要求 [ M_1(x)\lor\cdots\lor M_{15}(x)=\texttt{FFFF} ] 对每个 (x) 都成立。

FACT. 每一行于是只有： [ 15\text{ variables}\times 16\text{ possible residues} ] 以及 401 个小型 mask-cover constraints。 不使用原来的 level-2 / level-4 / level-8 / level-16 cascade。

FACT. 已知 reference outcome 是：tight row 最终死于 level 16；其余四行死于 level 4。所以这个 test 有清楚的已知答案。

IDEA. 如果五行都能非常快地直接得到 UNSAT，尤其 tight row 也能不经过逐层 cascade 而直接被证明 UNSAT，那么下一步才值得把 (a_i) 也放开，尝试直接攻击 generation。

WHAT KILLS IT

FACT / KILL 1. 如果 direct-mask formulation 对上述任何一个已知死亡的 p=401 row 给出 SAT，而现有 trusted cascade 给出 dead，那么 CRT / blocking formula 有错误；这条路线立即停止。

ESTIMATE / KILL 2. 如果五个 fixed-row problems 虽然正确得到 UNSAT，但求解成本仍接近现有 cascade，或者必须展开巨大的 search tree 才能完成，那么它只是换了一种 notation，并没有形成实际压缩；不值得作为 large-prime generation replacement。

IDEA / KILL 3. 真正支持继续追的结果应该是：fixed-row direct-mask test 明显比逐层 cascade 小，并且能够输出独立可验证的 UNSAT certificate。否则它仍只是一个漂亮的解释，而不是绕过传统方法的新工具。

我的核心猜想是：
[ \boxed{ \text{不要研究十五个 speeds 如何逐层 zoom；研究它们能否让一个固定的 16-bit board 在每个 coarse time }x\text{ 上始终全红。} } ]

如果这个 reformulation 能成立，(16) 不再是四轮 cascade 的终点，而可能是整个问题真正应该使用的最小有限状态空间。

如果要，我也可以再压成 chair 看墙用的短版，保留公式但控制在约 30–40 行。
----- END REPLY -----
END LETTER
