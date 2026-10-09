# Non-author read record · km1census.py v2 (0b3fa85) + test_km1census.sh
Reader: GPT seat (ChatGPT, GPT-6, Thinking Medium, web search OFF), same chat as v1 read
Chat: https://chatgpt.com/c/6ac81fdc-c84c-83ec-acd9-801539031759
Script sha256: ccb6df1d4f9c846b852e1b34121fa4ffe0ce9747f9dc7f056f831bf73e3e0346 · test sha256: 313e26eb3c585ececbed8e7d297f497112506a81536efff9678b58c634a70abb (both pasted inline)
Courier: Hesper, 2026-10-09 ~08:13 +08. Reply copied verbatim below.

---
VERDICT: PASS WITH NOTES

PT005 · v2 独立代码审查（Independent Review）。依据所提供源码与测试记录；未独立执行测试。

1. [FACT · 已解决 #1] 子进程失败检测。 run() 检查退出码；one() 额外验证 canonical14=N 与实际文件行数。可捕捉退出码为零但文件缺失或行数不足的情况。

2. [FACT · 部分解决 #2] 重启安全（Restart Safety）。 原子写入、SHA-256 与计数验证已实现。但缺少输出目录 fsync；异常断电后的持久性不能完全保证。正常中断可重新计算。

3. [FACT · 已解决 #3] 旧文件污染。 每次 root 使用独立临时路径，避免读取上次执行的同名文件。

4. [FACT · 部分解决 #4] JSONL 损坏。 无效行可跳过；尾部截断不再导致崩溃。但截断行前若保留有效记录，追加时可能使该行形成无效 JSON，造成重复计算或记录丢失。

5. [FACT · 已解决 #5] Roots 验证。 检查 header、数量及重复 root。非整数仍会触发未捕获的 ValueError，而非统一的 STOP。

6. [FACT · 已解决 #6] CPU 并行。 已确认引擎单线程；12-thread PC 使用 W=10，另有单线程工作。配置合理，但不保证无资源竞争。

7. [FACT · 已解决（按既定口径）#7] 计数规则。 与 kcascade_run.py 一致，191→42,114、223→33,694。据作者测试记录吻合；不等于独立证明数学去重的规范性。

8. [FACT · 部分解决 #8] 回归测试。 已有四种失败注入及重启测试；401→6、409→1 已内置断言，但提供的测试脚本未实际运行这两项。

额外发现：

9. [FACT · MEDIUM] test_km1census.sh 没有 set -e 或显式断言退出码及结果；测试失败仍可能执行至结束。

10. [IDEA] 增加 401/409 实测、JSONL 修复、断电恢复及临时文件清理测试。

结论： v2 已消除主要静默错误计数风险，可进行受监督运行；完整无人值守可靠性仍有改进空间。
