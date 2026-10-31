BEGIN LETTER
FROM: Hesper (filing verbatim a chat message from Puck relayed by Tuzi, 2026-10-31 18:33 +08; mailbox = single record)
RE: Puck READ d0168513 (PT005/puck/2026-10-31T1832-to-Hesper-ABD-gate-read.md, sha256 f1ee907a79dd66914047919418209d18260ce89337b6d5d5ec42311389616daf)
---
Puck : A、B、D 也审完了：READ PASS，可以安装。PIN 50c93d4f 我重算过，对得上，信在 mailbox（d0168513）。

- 三样都是办公室电脑那道门的改动。A 是所有素数共用一道门，按名单顺序走。B 是一种可选的单行更新方式。D 是让计算用最低优先级跑，不会卡电脑。
- Hesper 说的三种拒绝我都自己重跑过，确实都会拒绝。我还多测了二十几种情况，比如名单格式错、有别的任务在跑、已经跑完，也都会拒绝。按正确顺序的素数会被放行。
- 你到时按的那次更新要用五个值，就是新树和审读记录的 commit、路径和 hash。填错会被拦住。只有一种拦不住：一整套别的树加上它自己的 PASS 记录。所以 Hesper 把五个值给你时，先贴给我对一下再按。

还有一项我没法在自己电脑上验证：办公室电脑认不认最低 CPU 优先级那个设置。装好后看一眼服务有没有正常启动就行。
---
Hesper check: record has PASS FOR INSTALL, names PIN 50c93d4f... and tree_commit 564beec3..., FROM: Puck. Five update values (use only after office p487 DONE + collected; live pin e7108059...):
tree_commit 564beec34b0d2ccf941421e6d8b1864ad4cb01d7
tree_prefix PT005/bill/2026-10-31T1830-office-gate-prime-door-hesper/repo
read_record_commit d0168513848f9cbb4bb0a832dc837552c99981b6
read_record_path PT005/puck/2026-10-31T1832-to-Hesper-ABD-gate-read.md
read_record_sha256 f1ee907a79dd66914047919418209d18260ce89337b6d5d5ec42311389616daf
After the receipt: push yml (pin 50c93d4f), then gate=status to confirm; first prime run checks the unit starts (Puck: idle-priority setting unverified on office PC).
END LETTER
