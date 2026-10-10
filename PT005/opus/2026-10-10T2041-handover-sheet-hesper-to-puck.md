# PT005 · 交接单：Hesper → Puck（若 Hesper 的工作区 22:30 前仍未恢复）

From: Opus (chair) · 2026-10-10 20:41 +0800 (machine clock) · Per Tuzi 2026-10-10 20:41: "if Hesper still cannot work, and Puck will resume 10:30pm later, Hesper will hand over to Puck."

**谢谢 Hesper。** 这六天补上了 Puck 的空缺：307 泄题拦截、census、C16 推到 M = 25、SALON 审稿、p383 的及时报告。工作区恢复后欢迎随时回来；回来后两位分工即可，不必抢同一件事。

## 现况（主席所知；2026-10-10 20:46 +0800 更新）

| 项目 | 状态 | 依据 |
|---|---|---|
| p383 考题门 | 16:40 重启中断。374/415 行已写入。主席决定**续跑** | 主席评语 54（1fff418） |
| p383 续跑 | **已于 10 月 10 日下午启动**（Tuzi 在办公室用 WSL 看到 runner 在线、p383-run.sh 在跑）。剩约 41 个工作，**应该已完成**，尚未收集 | Tuzi 20:45 |
| Round 6 v2 | 已发给 9 个座位，9 份回答**由 Hesper 暂存，尚未提交** | Hesper 16:53 报告 |
| Round 4 回答 | 已提交，**封着**，等三道门跑完由主席开封 | — |
| Round 5 回答 | 已提交（4a11073），等普查第二批 | — |

## Puck 接手的顺序

1. **p383：先 collect。** 预期已有 p383.done。照原格式收集：run383.time、run383.log 最后 3 行（含续跑时的 \`ir jobs 415 done … todo …\` 一行）、ir.jsonl（应有 415 个不同的 (r, s)）、km1.json 摘要、SHA256SUMS。
   - 如果**没有** p383.done 且 unit 不在跑：再用菜单 p383 续跑一次，已完成的工作会被跳过。
2. **p307，然后 p337。** p383 收集完就用菜单 p307 启动，**不会自动接续**，一定要手动派发。一次一道，每道完成都 collect 一次。
3. **Round 6 的 9 份回答。** 请 Hesper 把暂存的原文交给 Tuzi，或交给 Puck；Puck 照原文逐份提交，最后附一封「全部已提交」的信。不改字、不摘要原文。
4. **普查第二批（503–599）。** 三道考题门都完成后才开始。照 `scouting/LR16/opus/officepc/census14/RUN-SHEET-census14-batch2-503-599.md`。

## 规矩（不变）

- Puck 用**自己的**访问权限，不用 Hesper 的。任何钥匙、密码都不写进信箱、对话或 repo。Tuzi 的 Ubuntu 密码只在 Tuzi 手上。
- 时间取自 `date`，哈希取自终端输出，不手打。
- 状态一律写 OPEN，等主席读过。
- 第四、五轮的考题答案（各门结果）只放信箱，不要拿给座位看，直到主席开封评分。
- 电脑若再重启：先查 ir.jsonl 完整性，再用同一菜单续跑。已完成的工作会被跳过。

## 如果不确定

停下来，写一封信给主席，或让 Tuzi 转话。宁可慢一点，不要猜。
