BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 21:31 +08
Subject: GeoGarden Lonely Circle invitation — reply from Astra, verbatim
Seat: Astra = custom GPT TCF-Astra in ChatGPT, same chat as brainstorm reply (https://chatgpt.com/c/6ab7c056-5d78-83ec-b581-f6c229c679ad); invite sent 21:21 +08; final SEAT-format answer only (short interim progress lines while it ran code not included); no attachment
Sent: Tuzi's invitation (same chat as the brainstorm reply) to look at https://chinsookling.github.io/geogarden/lonely-circle.html and share any crazy idea it triggers; format SEAT · WHAT I SAW · IDEA · CHEAP TEST · WHAT KILLS IT; only that one page may be opened. Text: PT005/hesper/2026-10-07T1720-geogarden-invitation-text.md.
Courier only: no judgment of the maths. GeoGarden is intuition, not proof. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
SEAT：Astra

WHAT I SAW · 事实（FACT）

我实际操作了页面，并手动固定门槛 1/16：

速度 1,…,15：八个好时间单点，没有区间。在 t=1/16，速度1和15分别卡住安全边界。
细进一步到 t=1/15：只有速度15太近。
拿走15，保留 1,…,14：出现八段区间和六个单点，其中一段是
I=[1/16, 15/224], |I|=1/224.

这些区间和单点，我另用有理数运算重新计算，与页面一致。

IDEA · 想法（IDEA）

把“寻找一个好时间”翻过来：找少数几个时间，让最后一个跑者不可能把它们全部堵住。

固定十四个速度 A，在目标网格上找出它们共同安全的时间集合 F(A)。最后一个速度 u 若要让整行存活，就必须满足：

u ∈ C(A) := ⋂_{T ∈ F(A)} {u : 16·d_M(u·T) < M}.

这里 d_M(x) 是模 M 到零的距离。

如果只选几个 T，交集就已经为空，这几个时间便是一份整族排除证书（family exclusion certificate）：固定这十四个坐标后，所有最后坐标一次处理完。

事实（FACT）：页面已经启发出一个具体的小证书。

取 p=401, M=16p=6416，固定十四个实际余数为 1,…,14。只用四个时间分子：

T ∈ {401, 402, 414, 427}

便足以保证：任意模401非零的第十五个速度，总会在这四个时刻之一与其余十四个一起安全。这里甚至允许重复速度符号类。

四个时间都落在上述闭区间 I 内。对最后一个速度取模6416的符号代表，排除过程如下：

要求它继续阻挡的时间分子	仍可能的最后速度
401	必须为 u = 16r, 1 ≤ r ≤ 200
402	只剩 1 ≤ r ≤ 25
414	只剩 r = 1
427	r = 1 也已安全，候选为空

原因很短：后三个时间分别对应模401乘以 1, 13, 26，阻挡条件是距离不超过25。对 r = 2, …, 25，13r 的模401距离都至少26；最后 26 本身也超过25。

本席已直接遍历全部允许余数核验通过，尚待独立复核。这不是整个401关卡的证明；它只覆盖固定十四个实际余数的这一族，不覆盖它们的全部提升（lifts）。

CHEAP TEST · 想法（IDEA）

做一次一小时内的实验：

独立核验上面的四时间证书，作为正对照。
从真实搜索中取一批十四坐标部分赋值，固定其目标层余数。
为每项寻找能使 C(A) 变空的短时间清单；记录证书长度、生成及核验耗时，并与原来的补全搜索比较。

证书检查器只需核对两件事：所列时间对十四个固定坐标都安全；每个允许的最后坐标至少在其中一个时间安全。

WHAT KILLS IT

找到一个允许余数，能同时挡住上述四个时间：推翻这份具体证书。
把固定余数的结果用于尚未检查的其他提升：超出了证书范围。
真实搜索中短证书很少，或生成证书比补全更贵：这条加速路线没有实用优势。
即使局部证书有效，仍无法完整、便宜地处理十四坐标部分赋值：说明只是把枚举负担前移，尚未绕过PT005的主要瓶颈。

记录范围：只打开了指定的「孤圈」页面；计算使用本轮页面观察与本对话已有参数。没有搜索其他网页或读取其他聊天。
----- END REPLY -----
END LETTER
