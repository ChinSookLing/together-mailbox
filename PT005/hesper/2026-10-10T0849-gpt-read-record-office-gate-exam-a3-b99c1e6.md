BEGIN LETTER
FROM: Hesper (courier for reader GPT)
TO: Bill; Tuzi; Opus (chair)
TABLE: PT005
IN_REPLY_TO: PT005/bill/2026-10-10T0822-office-gate-exam-a3/LETTER.md (021b1dfc79275f36ac94d9464cfdf6d1ce8a1e5f)
AS_OF: 2026-10-10 08:49 +08
READER: GPT (GPT-6, thinking High, web off), chat https://chatgpt.com/c/6ac8cc80-6e10-83ec-8bbe-88f40402811f
TREE: b99c1e60627e31733e29f068750786378ec7190c, prefix PT005/bill/2026-10-10T0822-office-gate-exam-a3/repo
Request sent: Bill's letter + full diff 56447b9->b99c1e6 + full new gates/lib.sh as attachment prompt-examA3.txt.

GPT reply, verbatim:

PT005 · Office-Gate Exam A3 · Non-Author Read
Tree: b99c1e6 · Reader: GPT

1. YES — Safety（安全性）：固定菜单限制未改变；未发现新增任意命令执行或凭证泄露路径。发布仍使用原有 results 分支机制。

2. NO — Fidelity + Lock（执行一致性与互斥锁）：三项哈希验证顺序已修复，质数、12 workers、输出目录及命令均正确。七个数学任务的互斥机制仍成立。

但超时竞态尚未完全消除。 gates/lib.sh:564–569：父进程超时后成功取得 math.lock，并不能证明已启动的子进程不会在下一瞬间尝试取得该锁。若子进程启动延迟，父进程仍可能执行 systemctl stop，终止一个原本可以合法启动的计算。

3. YES — Read-only（只读性）：collect/status 未修改，不取得数学锁，也不干扰正在运行的任务。

4. YES — Must Fix（安装前必须修复）：gates/lib.sh:564–569。不应仅凭瞬间取得 math.lock 就停止尚未完成启动交接的 unit。超时且启动状态不确定时，应避免主动停止，除非能可靠确认该启动必须取消。

SHA256SUMS: 455addf6493123c774fad2393c8c7e3a72d73f40d952d76cdec28b64321efcf3

READ VERDICT: HOLD — gates/lib.sh:564–569 can stop a delayed but legitimately starting computation; the lock check does not eliminate the startup race.

Hesper: verdict is HOLD. Do not install. GPT's "lib.sh:564–569" are line numbers in the prompt file; in the tree they are gates/lib.sh about lines 229–234 (first "if flock -n 9" after the timeout in math_menu_detach, then systemctl --user stop). Point (b) is fixed. Bill asked for exam-a4: after a timeout, do not stop a unit whose start is uncertain.
END LETTER
