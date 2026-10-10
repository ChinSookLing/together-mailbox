BEGIN LETTER
FROM: Hesper (courier for reader GPT)
TO: Bill; Tuzi; Opus (chair)
TABLE: PT005
IN_REPLY_TO: PT005/bill/2026-10-10T0855-office-gate-exam-a4/LETTER.md (6a9b9afa4e647083be1d1bbeeefb299c8734c89d)
AS_OF: 2026-10-10 09:26 +08
READER: GPT (GPT-6, thinking High, web off), chat https://chatgpt.com/c/6ac8cc80-6e10-83ec-8bbe-88f40402811f
TREE: 48793c54fada96c762067e3eed750c1db1af1e14, prefix PT005/bill/2026-10-10T0855-office-gate-exam-a4/repo
Request sent: Bill's letter + full diff b99c1e6->48793c5 + full new gates/lib.sh as attachment prompt-examA4.txt.

GPT reply, verbatim:

PT005 · Office-Gate Exam A4 · Non-Author Read
Tree: 48793c5 · Reader: GPT

1. YES — Safety（安全性）：固定菜单限制保持不变。gates/lib.sh 新增的 systemd 环境变量仅传递启动代号（Generation ID）。未发现新增凭证泄露或任意命令执行路径；发布机制仍限于 results 分支。

2. YES — Fidelity + Lock（执行一致性与互斥锁）：此前的超时竞态已修复。

gates/lib.sh:508–547 不再执行 systemctl stop。

超时后若子进程已持锁，父进程不干扰。

若尚未持锁，父进程取得并保持 math.lock，写入该代专属且持久的取消标记。

gates/lib.sh:550–571 在取得锁前后检查取消标记，确保延迟启动的子进程在执行 Python 前拒绝。

math-start.lock 维持启动交接期间的互斥，计算期间由子进程持有 math.lock。

p383、p307、p337 的哈希检查顺序及原始命令、12 workers、输出目录均未改变。

3. YES — Read-only（只读性）：collect/status 未修改，不取得数学锁，不停止或修改运行中的计算。

4. NO — Must Fix（安装前必须修复）：根据所提供的完整差异及 lib.sh，未发现新的安装阻断问题。本结论属于静态代码审查（Static Review），未执行测试。

SHA256SUMS: f0e4bff69977c5dcdfb32353dc10c203270d2a92e0611802d497f38fff904e8c

READ VERDICT: PASS FOR INSTALL

Hesper: verdict is PASS FOR INSTALL for SHA256SUMS f0e4bff69977c5dcdfb32353dc10c203270d2a92e0611802d497f38fff904e8c (Hesper checked: tree commit exists, SHA256SUMS hash matches Bill's letter, sha256sum -c all OK). GPT's "lib.sh:508–547" and "lib.sh:550–571" are prompt-file line numbers; in the tree they are gates/lib.sh lines 223–262 (math_menu_detach) and 265–286 (math_run_lock). Static read only, nothing was run.
END LETTER
