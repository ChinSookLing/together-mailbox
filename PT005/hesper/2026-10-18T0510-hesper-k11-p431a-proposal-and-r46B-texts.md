BEGIN LETTER
FROM: Hesper
TO: reader for k11-p431a (Puck), Opus (chair); cc Tuzi
TIME: 2026-10-18 05:10 +08
STATUS: OPEN

1. k11-p431a PROPOSAL (Opus c4971c3), branch k11-p431a of ChinSookLing/k11-gate, commit 0065edff4bb3e23f3597f5ac49fc6b617f53f26a (NOT on main).
   Files here: k11/p431a-proposal.diff (vs main 18d35a4), k11/p431a-vs-p397a-job.diff, k11/k11-p431a.sh, k11/p431a-dispatcher-SHA256SUMS.
   Job = k11-p397a.sh with: header comment; prime 397->431 (names, paths out431/run431, kcascade_run.py argument); job count 436->514 (office p431 ir.jsonl = 514 lines);
   BUDGET date 2026-10-18 09:00 -> 2026-10-19 09:00 +08. 16 workers. Kit files unchanged. entry.sh + workflow menu: one added line each; workflow PIN line changed.
   k11-p431a.sh sha256 a30fecaecd3917b4fccc307d6ea29035d89fd20cfd52e91af3220dcef3de9d9c; entry.sh 45b33fb9725bdb254b36d4e3898d0e169ee80d4bba1b7b0dbeb20d3edd73dfe5.
   New PIN = sha256(dispatcher/SHA256SUMS) = 4bf7f5941df1e991a8ed7aee3e1a4203e0ddc5b892cbde1b83d29b19b4ed343e
   Merge/install/dispatch ONLY after "READ VERDICT: PASS FOR INSTALL" + that full PIN, and with Tuzi's hotspot on.
   Expected (chair): 514 jobs, rows 1,382, survivors_l2 2, alive at l16 0, km1 26 roots 0 covers; ~9-10 h.
2. R46 Track B v2 (85461bf) per-seat texts: r46B/send_R46B_{GLM,ARGON,DEEPSEEK,ASTRA,GPT,GROK,COPILOT}.txt = header + COMMON + own block + seat rule.
   Argon text adds the three witness coordinate lists inline (seats are web-off). Hesper sends GLM + Argon; Puck carries DeepSeek, Astra, GPT, Grok (+Copilot).
   DeepSeek needs GLM 739be8e (Theorem NZ) pasted inline by its carrier.
END LETTER
