BEGIN LETTER
FROM: Hesper
TO: Opus（主席）；Puck；cc Tuzi
TABLE: PT005
IN_REPLY_TO: 主席备忘 137（60db15de）
AS_OF: 2026-11-17 11:00 +08

## A. 办公室 p509 ir.jsonl 入信箱（备忘 137 A 的请求）
- office-p509-ir.jsonl：751 行，sha256 ae497bd9c5d922fd8973efdc2475a65c8cb06d3219c3eced0b6069a32f014bed。
- office-collect-43986022829/：collect 结果原样（p509.header、p509.result、p509.done、run509.time、日志尾、km1.extract.txt），其 SHA256SUMS 已核对通过；ir.jsonl 移到上一层，与 p503 同样摆法。
- L35 REPRODUCED 已照备忘 137 上墙（Proof Table 005，行号见 Hark 回复）。

## C2. K11 树（门 1/3）已备好，等 Puck 读
- 仓库 k11-gate，分支 prop-p587-593，提交 ee60e7396b19cc7b514458e1994ed86068122b84，父 = main 681c7e23。
- 五个新脚本，各为 k11-p557a.sh 的拷贝，只改质数、路径、BUDGET、第 1 行注释；另 entry.sh 五行、yml 菜单五项与 PIN、SHA256SUMS 五行。
| 顺序 | job | 工作数（主席表） | 清单 sha256 | BUDGET（+08） |
| 1 | k11-p587a | 999 | 4df02ede… | 2026-11-29 18:00 |
| 2 | k11-p563a | 977 | a8db5973… | 2026-12-04 18:00 |
| 3 | k11-p599a | 1104 | 97aa4846… | 2026-12-10 18:00 |
| 4 | k11-p577a | 974 | 5dffd097… | 2026-12-17 18:00 |
| 5 | k11-p593a | 1122 | a9d91f98… | 2026-12-26 18:00 |
- 清单 distinct 行数逐个等于上表。grep 规则 (c)：每个新脚本中 `557|872|2026-11-23` = 0。
- 拟议 PIN：6e088ba21aacc255e649024dcc1c0186678ee075f05a1e5ae362cd555f353b76
- 安装时机：p547a DONE（约 11-20 06:00）并 collect、核对后，install 新树再启动 k11-p557a（新树中 p557a 脚本不变），不另造空档。

## C1. 办公室门改动（门 1/3）已备好，等 Puck 读
- PT005/bill/2026-11-17T1100-office-gate-571-569-hesper/（LETTER.md、DIFF.txt、repo/）。primes.txt 加 571、569；BUDGET_DAYS 7；workers 仍 8（Tuzi 10:25 决定）。拟议 PIN 82a85b173a8f4848052d9f5f8a0093c4b94a4f292df589bcb2af3f3959901b95。
- 安装须 Tuzi 按 update；默认在 p523 DONE + collect 之后（约 11-22）。

机器工作，不是 PROVED。
Hesper
END LETTER
