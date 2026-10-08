# Non-author read record · km1census.py (b9ba03d)
Reader: GPT seat (ChatGPT, model shown GPT-6, Thinking Medium, web search OFF)
Chat: https://chatgpt.com/c/6ac81fdc-c84c-83ec-acd9-801539031759
Script sha256: 87e0dcb2c3b9f93d79ac87dee83a7c99f31d3f2db359e8d94ccbdf1b91dc4646 (pasted inline)
Courier: Hesper, 2026-10-09 ~06:58 +08. Reply copied verbatim below.

---
VERDICT: FAIL

独立代码审查（Independent Review）· PT005 · km1census.py

1. [FACT · CRITICAL] 子进程失败被静默忽略。 run() 未检查 returncode。km1roots 失败时，空输出可能被解释为零 roots，随后记录 covers=0。km1root 失败时，旧文件仍可能被读取，造成错误计数。建议使用 check=True，并检查预期输出。

2. [FACT · CRITICAL] 重启安全（Restart Safety）不足。 JSONL 记录是跳过 prime 的唯一依据。dedup 文件写入成功后、JSONL 追加前崩溃，会重新计算；反过来，JSONL 写入完成但未持久化或 dedup 文件损坏，也可能永久跳过。缺少原子写入（Atomic Write）与完成验证。

3. [FACT · HIGH] 旧 root 文件污染。 one(r) 执行前不删除已有 km1_P_r.txt。如果引擎失败、没有覆盖文件，程序可能读取旧结果。建议每次使用独立临时文件，检查成功后读取。

4. [FACT · HIGH] JSONL 尾部损坏导致无法重启。 json.loads(l) 对截断行、空行或无效 JSON 直接抛异常。一次中断便可能阻止整批恢复。

5. [FACT · HIGH] roots 解析缺少验证。 无条件丢弃第一行；空输出、异常标题、非整数 root 均未明确检查。重复 root 也不会去重，造成重复计算。

6. [FACT · MEDIUM] CPU 并行可能过量。 ThreadPoolExecutor(W) 同时启动最多 W 个外部进程；每个引擎若使用多线程，还可能竞争 CPU。WSL 与另一任务共享资源，需限制 W。

7. [FACT · MEDIUM] 计数依赖输出格式。 covers=len(covers) 统计的是不同的非空文本行，不一定等于数学上不同的 cover。只有引擎保证每个 cover 有唯一规范文本表示（Canonical Representation），计数才可靠。

8. [IDEA · REQUIRED TEST] 将 P=401→6、P=409→1 设为强制断言（Assertion），并增加模拟引擎失败、截断 JSONL、残留 root 文件及中途重启测试。

结论： 算法流程与宣称目标大体一致，但目前不能作为可信的无人值守（Unattended）census。尤其必须先修复静默失败与重启完整性问题。
