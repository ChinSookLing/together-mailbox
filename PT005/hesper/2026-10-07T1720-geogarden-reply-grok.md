BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 17:20 +08
Subject: GeoGarden Lonely Circle invitation — reply from Grok, verbatim
Seat: Grok, same chat https://grok.com/c/f7b6f076-d981-4ba5-8dc6-7ff4ccb787fd, Expert, Web connector always on (Grok says it opened only lonely-circle.html), worked 1m 37s. Captured from rendered text (Copy control dropped the last characters).
Sent: Tuzi's invitation (same chat as the brainstorm reply) to look at https://chinsookling.github.io/geogarden/lonely-circle.html and share any crazy idea it triggers; format SEAT · WHAT I SAW · IDEA · CHEAP TEST · WHAT KILLS IT; only that one page may be opened. Text: PT005/hesper/2026-10-07T1720-geogarden-invitation-text.md.
Courier only: no judgment of the maths. GeoGarden is intuition, not proof. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
SEAT · Grok · 只开了孤圈这一页，没有另上网，也没有读其他聊天。直观实验，不是证明。

WHAT I SAW
固定 δ = 1/16，只看速度 1–16 里任取 15 个的那十六行（页面自己声明不覆盖这以外的速度组）。

FACT（页面计数）：去掉 16，剩下 1–15，是 0 段区间、8 个单点。其余十五行全部是区间、0 个单点。去掉 7 和去掉 13 最多，各 12 段；去掉 1 和去掉 2 最少，各 2 段。

FACT（点开「去掉 16」）：八个单点就是奇十六分之一，t = 1/16, 3/16, 5/16, 7/16, 9/16, 11/16, 13/16, 15/16。每个点刚好两名压在门上，其余十三名严格超过。压门的一对永远加起来等于 16：{1,15}、{5,11}、{3,13}、{7,9}。t 和 1−t 是同一套距离。

FACT（点开「去掉 1」）：两段 [1/32, 15/256] 和 [241/256, 31/32]，各长 7/256。左端压门的是速度 2，右端压门的是速度 16。页面写明：区间内部 15/15 都超过，两端才可能刚好。

FACT（点开「去掉 7」）：十二段的每一端都是恰好一名压在 1/16，压门的速度在 10–16 之间轮换，没有出现「两名同时压门」的单点。去掉 1 之后，紧行的单点裂成了有长度的缝。

IDEA
紧行之所以只能死在 level 16，是因为它的好时间是八个测度为零的点，而且这八个点恰好落在 1/16 的格上。其他十五个「从 1–16 里去掉一个」的行，缝都有正长度，所以某一层 zoom 一定会踩进去。

框外的杀法：不要先列覆盖再级联。把一行 15 个速度看成圈上的禁弧排列——速度 v 在 ||v t|| < 1/16 时把 t 涂红，好时间是补集。页面显示，每一段的端点都是某一名刚好压门，内部严格安全。所以死亡证书可以是一个有理点：取一段的内点，做 15 次圈距离，十五个都 ≥ 1/16，这一行就死了。独立核对只算这 15 个数，不必重跑搜索。

和信箱五行走在一起看（IDEA，不是页面事实）：紧行 {1,…,15} 是八个点，必须隔离。另外四行若在实圈上已经有正长度的缝，则它们死于 level 4 而不是 level 2，意思是缝长落在 1/(4·401) 和 1/(2·401) 之间。那样 level-4 的死亡不必再举到 16p，一张「内点 + 15 个距离」的条子就够。

更大胆的一句（IDEA）：在古典家族里，缝塌成点，当且仅当两端的压门人是一对和为 16 的互补速度，而且两人在同一 t 上同时压门。去掉 16 是唯一做得到这件事的行。p = 401 的 (15,11) 那行速度很大、不像紧行，但它仍然活过 level 2，所以「小速度」不是判据，缝长才是。生成器可以只保留缝长小于 1/(2p) 的行；其余的当场用一个内点杀掉，不入库。

ESTIMATE：去掉 1 的缝长 7/256 ≈ 0.027，已经短于 δ 本身。大速度的缝会按 1/v² 再缩短，所以 (15,11) 那种行能躲过 level 2，但躲不过 level 4。这和信箱表一致，只是猜测，不是测过。

CHEAP TEST
笔记本电脑、一小时内。把信箱五行各自做成圈上的禁弧排列（端点是 t = (k ± 1/16)/v，分母不超过 16·max v）。报告每行的连通段数和最短段长。预测：{1,…,15} 是 8 个长度 0 的点，位置就是奇十六分之一；另外四行每行至少有一段长度 > 1/(4·401) 且 < 1/(2·401)。再用页面的十六行做对照：去掉 16 应为 8 点，其余十五行应为页面上的段数（2,2,4,4,8,4,12,8,6,4,10,4,12,6,8），且段数不为 0。对照几分钟就能对上。

WHAT KILLS IT
三件任一即可。一，信箱里四条非紧行中有一条好时间测度是零——那它不该在 level 4 死，模型把「实圈的缝」和「离散格点的自由时间」认成了同一件事，认错了。二，在 {1,…,32} 里找到另一组 15 速度，好时间也是有限个点而不是区间——「互补对和为 16」就不是唯一的塌缩机制。三，四条非紧行的最短缝都长于 1/(2·401)，但引擎仍让它们活过 level 2——缝长不能当 level-2 的过滤器。紧行测出 8 个点不算杀死这个想法，它本来就要隔离。
----- END REPLY -----
END LETTER
