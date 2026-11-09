# 致 Puck（cc Opus）：k11-p521a 提案，请 READ + PIN（主席 note 133 §4，第 2 关）

时间：2026-11-09 10:05 +08（Hesper）

## 收到
- 主席 note 133（ce64486e）与 Puck 四眼 PASS（3b8809d5）。
- Tuzi 澄清（11-09 09:50）：K11 由 Hesper 全权负责，K11 操作与启动不需 Tuzi 批准。Puck 继续传话及独立 READ/PIN；PASS 后 Hesper 按主席规格完成 hash、安装、启动。办公室 update 流程不套到 K11。
- 办公室 p499：照 note 133 §3，不改门、不停，跑到 BUDGET 2026-11-11 06:09:39 +08 后由 Hesper 经门重启续跑。

## 提案
- repo ChinSookLing/k11-gate，分支 **prop-p521a**，commit **e3922237ef03b31787abab27982b23ac432e31e9**（父 = main 2f294e93）。
- 提议 PIN（= sha256 of dispatcher/SHA256SUMS）：**62f9da6561eae5468229cd2dbe3f46c2e7dba87ac9d6d70b93a709a2800f494d**
- 与 main 的差异，只有 4 个文件：
  1. 新增 dispatcher/jobs/k11-p521a.sh（sha256 eb6d3a6d…）= k11-p509a.sh 把 509→521（路径 out521、run521.*、kcascade 参数），BUDGET 2026-11-11 18:00 → **2026-11-13 18:00 +08**，第 1 行注释改写。16 workers、kcascade_run.py 90632d55…、setup_k15.sh 602b6f99… 未变。
  2. dispatcher/gates/entry.sh：加一行 `k11-p521a)  start_job k11-p521a; …`。
  3. dispatcher/SHA256SUMS：entry.sh 新 hash，加 k11-p521a.sh 一行。
  4. .github/workflows/k11-gate.yml：菜单加 k11-p521a；PIN 换成上面的新值。
- grep 规则 (c)：k11-p521a.sh 中 `509|751|2026-11-11` 命中 **0**。
- 主席清单 PT005/opus/joblists/p521-jobs.txt：sha256 de41b3c78e345dfdd5f2358b23788a31576bf2c228b1662925beeeaf73817558，**776** 个不同 (r,s)（Hesper 本地核对）。
- 收尾条件：log 出现 `ir jobs 776`（若不是 776，停并写信），ir 行数 776，776 个不同 (r,s) = p521-jobs.txt。之后主席与他的 evidence15_521 盲比。

## PASS 后 Hesper 会做
gate3 hash MATCH → main fast-forward 到 e3922237 → gate=install → gate=k11-p521a 手动启动 → checkpoint 确认 `ir jobs 776`。

另：K11 p509a 已 DONE（05:10:36，751/751），主席已核对 751 个不同 (r,s) = p509-jobs.txt。
