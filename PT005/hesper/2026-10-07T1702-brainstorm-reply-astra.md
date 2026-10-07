BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 17:02 +08
Subject: PT005-BRAINSTORM-GENERATION reply from Astra, verbatim
Seat: Astra = custom GPT TCF-Astra (GPT-6 Astra / Max / Persistent) in ChatGPT, chat https://chatgpt.com/c/6ab7c056-5d78-83ec-b581-f6c229c679ad. First turn stalled after a connection drop (~48 min); Hesper pressed Stop and sent one recovery line, no answer in ~45 min. Tuzi then talked to Astra herself and pasted this final answer plus the ZIP to Hesper at 17:00 +08. Astra's interim progress notes (choose D2; raw D2 must be corrected at p=223; LP has a fractional feasible point; 45 s integer try INCONCLUSIVE) preceded the final text and are summarised here, not quoted.
Sent: the packet BEGIN..END from PT005/opus/2026-10-06T2203-packet-brainstorm-large-prime-generation.md plus scouting/LR16/opus/p401_level2/README.md verbatim (message sha256 734b4d10...7505).
Courier only: no judgment of the maths. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
Tuzi，**这一轮提案已经可以交了，不需要你继续等。** 但要把提案变成证明，还缺一份实际生成、独立核验通过的证书；多想一会儿并不能保证补上它。中断前的模型和检查结果都在，我把答复补齐：

**SEAT：Astra · REPLY_TO：PT005-BRAINSTORM-GENERATION**

**SUMMARY（≤5行）**  
事实（FACT）：已建立 \(p=401\) 的小模型：600 个布尔变量、1,177 条约束。  
想法（IDEA）：直接证明“第2层不存在已知五个轨道之外的不可约存活解”。  
事实（FACT）：五行的后续提升已经本席两种算法交叉检查，全部死亡。  
事实（FACT）：45秒整数求解试跑超时，尚无不可满足证书（UNSAT certificate）。  
范围：这是一条可测试的替代路径，尚未证明加速，也未完成整个素数关卡。

**THE IDEA**

不先列出全部第1层行，直接编码以下存在性问题：

> 能否选出15个模 \(802\) 的速度符号类，至少两个为奇数，挡住全部网格时间，其模401覆盖不可约（irredundant），而且不属于附件中的五个已知轨道？

用“每个被选速度都有一个仅由它阻挡的时间类”精确编码不可约性。把一个奇数速度通过单位变换规范化为1；五个轨道在此规范化下共有22个代表，逐一排除。

**五个轨道的完整性没有被假设进去——它正是模型要求证明的事情。**

另须纠正原始D2：有13类核心的素数可以存在强制族（forced family），同时满足“无网格好时间、至少两个奇数”。所以完整第16层模型还必须排除已被L7处理的家族，不能直接期待原始问题为UNSAT。

**WHY IT MIGHT WORK**

事实（FACT）：新模型同时施加覆盖、奇偶提升与不可约性约束，使求解器能够直接排除整批候选。

本席已交叉核验五行：

| 附件行 | 第2层存活数 | 后续结果 |
|---|---:|---|
| 紧行 \(1,\ldots,15\) | 1 | 第4层2个、第8层4个、第16层0个 |
| 其余四行 | 各1 | 第4层全部死亡 |

但**模型小，不代表搜索或证明文件一定小**。而且其线性规划松弛（LP relaxation）存在已核验的分数可行解，因此原始LP对偶不可行证书走不通；需要整数或布尔推理。

**CHEAP TEST**

对附件中的 `p401-level2-ir-except-five.opb` 做一次限时实验：

- 准备与正对照：最多5分钟。
- 支持证明日志的伪布尔求解器（proof-logging PB solver）：最多35分钟。
- 独立证明检查器（proof checker）：最多15分钟。

核验通过的UNSAT，才证明这五个轨道穷尽了该不可约分支；结合五行提升检查及**另行完整处理的可约分支**，才能作关卡结论。超时一律记为未定（UNKNOWN）。

**WHAT KILLS IT**

- 找到经过直接核验的第六个轨道：推翻五轨道完整性。
- 找到合法存活解被规范化或不可约编码误删：推翻编码的完备性。
- 限时内得不到可核验证书，或证书过大、检查过慢：本次实验没有建立实用加速优势。

**记录范围：** 数学依据来自本包及五行附件、本对话、此前本席生成的模型与检查日志；未搜索网页或读取其他聊天。

附件含小模型、生成与检查脚本、五行提升程序及原始输出。**其中的编码检查脚本不是UNSAT证明检查器。**

[Attachment: PT005-Astra-Generation-20261007.zip, 3,530,052 bytes, sha256 fa389d275398657ee5aa05ec2ef7f8b58f13646eaf8488144638bbd311a02e8f; unzipped, SHA256SUMS 20/20 OK; committed file by file under PT005/hesper/astra-generation-20261007/ (last commit 71c1cbf).]
----- END REPLY -----
END LETTER
