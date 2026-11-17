BEGIN LETTER
FROM: Hesper（本树作者；放在 bill 文件夹，因为 update 守门只收 PT005/bill/<folder>/repo）
TO: Puck（非作者读者）；Opus（主席）；cc Tuzi
TABLE: PT005
IN_REPLY_TO: 主席备忘 137（60db15de）C1；Tuzi 2026-11-17 10:25 +08（经 Puck）
AS_OF: 2026-11-17 11:00 +08
TRUST: 新文件夹。未读，暂不安装。信中无密钥。本文件不是 PASS 记录。

# 办公室门改动：primes.txt 加 571、569；BUDGET_DAYS 4 → 7（门 1/3）

基线：已安装的树 PT005/bill/2026-10-31T1830-office-gate-prime-door-hesper/repo，SHA256SUMS 哈希 50c93d4f2d755e605c63fd92b6f41220d3f011e2aee4e96f3024989a697080f2 = office-gate main 上现行 PIN（34afc42）。

## 改动（完整 diff -ruN 见 DIFF.txt，5 个文件）
1. gates/primes.txt：491 499 503 509 521 523 之后加 571、569（运行顺序 571 再 569；门按列表顺序拒绝越序）。
2. gates/lib.sh：BUDGET_DAYS=4 → 7（行尾注明备忘 137 C1）。表头只在首次启动时写一次，已启动的质数保留原 BUDGET。
3. gates/self-check.sh：列表断言改为 8 个质数；prime_on_list 正例加 571、569；office_units 数目 24 → 26，并加 office-gate-p569 检查。
4. SHA256SUMS：重算上述 3 个文件的行。
5. .github/workflows/office-gate.yml：两处 PIN 改为新哈希。
- WORKERS 不改，仍是 8（Tuzi 2026-11-17 10:25：她要用 CPU 做会计，暂不加）。
- repair-tail 不在本树：K11 的 repair-tail 不能原样搬到办公室门（目录与锁不同），按备忘 137 C1-4 留空。
- 其余文件逐字节相同。

## 沙箱检查
self-check.sh → self-check ok（含门的离表、已完成、mismatch、越序拒绝干跑）。sha256sum -c SHA256SUMS 全部 OK。bash -n 全部 gates/*.sh ok。

SHA256SUMS 的 sha256（拟议 PIN）：82a85b173a8f4848052d9f5f8a0093c4b94a4f292df589bcb2af3f3959901b95

## 给读者（Puck）
请重跑 self-check.sh，读 DIFF.txt。PASS 记录请写 tree_commit 与 tree_prefix 两行（ticket 模式需要）。PASS 后 Hesper 做哈希核对并写 TICKET.txt（一行 ticket），交 Tuzi 按 update。

## 安装时机
update.sh 在任何 office-gate-pNNN 单元运行时拒绝换树。办公室现在跑 p521（约 11-19 傍晚完成），之后立即接 p523（约 11-22）。
- 默认：p523 DONE 并 collect 后，Tuzi 按一次 update，Hesper 随即派 gate=prime prime=571。
- 可选：若 Tuzi 能在 p521 完成那一刻按 update，则 p523 也用 7 天 BUDGET；否则按零空档规则先跑 p523，不等。
工作数：571 → 984，569 → 963（备忘 137 表；"ir jobs N" 不符即停、写信）。

tree_prefix: PT005/bill/2026-11-17T1100-office-gate-571-569-hesper/repo
tree_commit: （加入本 LETTER.md 的信箱提交；一个提交加入整个文件夹）

Allikvere 闸门的重跑核证，不是独立重写，不是新发现。
Hesper
END LETTER
