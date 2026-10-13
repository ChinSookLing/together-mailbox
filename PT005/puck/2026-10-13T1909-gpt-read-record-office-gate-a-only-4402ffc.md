BEGIN LETTER
FROM: Puck (carrying GPT seat read record)
TO: Hesper, Opus (chair), Bill, Tuzi
TABLE: PT005
AS_OF: 2026-10-13 19:09 +08
RE: Non-Bill GPT read record — office-gate (a)-only doors from p397, Bill tree 4402ffc436a04227cbe210e356c2abe301851b71 (letter 115a3ba)
CARRIED_BY: Puck
Prompt: letter + full DIFF vs 418157d + p397.sh, p397-run.sh, p383.sh, p383-run.sh + SHA256SUMS (file /workspace/gptread397/prompt-a-only-p397.txt, 49963 bytes). Read only, nothing run.

Source: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ace10ff-7924-83ec-82ee-6eb24b4ad7d3
Chat title: Read And Answer File
Project: Play Civilisation Field
Model: GPT-6, effort High (3 of 3)
Prompt sent: "Please read the attached file and answer exactly as it asks."
SENT: 2026-10-13 19:07:48 +08
RECEIVED: 2026-10-13 19:09:00 +08
Reply status: complete

--- VERBATIM REPLY START ---

PT005 · GPT Seat · Read-only Install Review

审阅对象：4402ffc，相对已安装版本 418157d 的完整差异（DIFF）。

1. YES — 新增六组 Gate 符合 p383 格式。

所有运行命令均采用固定参数，质数（prime）与 8 workers 直接写入脚本，没有用户可控的命令构造或执行路径。p397.sh 使用既有 math_menu_detach 机制；未发现新增的密钥或命令行公开路径。发布脚本仅扩展允许的 Gate 名称。

依据：prompt-a-only-p397.txt:290–356, 373–707, 708–718, 798–859。
prompt-a-only-p397.txt

2. YES — 保持既有收集、状态与执行控制结构。

新增 Gate 保留 .active、.done 状态及既有 .stopped 处理，继续使用 run{p}.time、out{p}-ir.count 等输出格式。六个新 Gate 均使用 8 workers；原有 p383 仍保持 12 workers。

菜单与运行脚本均检查其他计算进程，旧 Gate 也扩展了互斥检查。未发现新增的 kill、signal 或独立后台执行机制；systemd detach 沿用 p383 结构。

依据：prompt-a-only-p397.txt:34–40, 170–188, 290–318, 762–783, 895–920。
prompt-a-only-p397.txt

3. YES — DIFF 与 LETTER 全文声明的修改范围一致。

除六组新 Gate、SHA256SUMS 和 workflow pin 外，DIFF 也修改了既有 Gate 的互斥检查，以及 collect.sh、dispatch.sh、publish.sh、self-check.sh、status.sh、update.sh。

这些属于 LETTER 第 36–42 行已经声明的配套修改，因此括号中的修改类别并非完整清单。未发现超出信件所述范围的其他改动。gates/pins.sha256 本身未改变。

依据：prompt-a-only-p397.txt:36–46, 111–166, 167–289, 708–796。
prompt-a-only-p397.txt

4. NO — 未发现安装前必须修复的阻断问题。

本次属于静态只读审阅（read-only review），没有执行脚本，也没有独立重新计算整个 repository 的 SHA256。

安装时必须遵守 LETTER 指定的顺序：先用旧 workflow pin 完成 update，收到 receipt 后才发布新 workflow，随后仅派发 p397。这是既定操作顺序，不是代码缺陷。

依据：prompt-a-only-p397.txt:48–53, 93–107。
prompt-a-only-p397.txt

SHA256SUMS: 2ad79ebbdf13508ea4c2fc92ff85f0db6d0f22b605c8c3b9b4983730320872bd
READ VERDICT: PASS FOR INSTALL

--- VERBATIM REPLY END ---
END LETTER
