BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 08:25 +08
RE: 猜公式 Round 6 (packet 6f1e734), send text r6_send_gpt.txt
SEAT: gpt
MODEL: GPT-5.6 Sol, Thinking High, Worked 2m 1s (GPT-6 failed twice: 10-10 11:40 and 10-11 08:15 'This response couldn't load'); sent 2026-10-11 with r6c_send_full
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ac97e4e-95c0-83ec-bfde-afaf19d7ade8

--- reply verbatim ---

ANSWER BLOCK

(a) FACT 修正：「19/19 都可缩放出 ≥5 个小速度」错误；正确是 18/19。指定的 389-cover [1, 4, 11, 28, 29, 57, 62, 85, 94, 96, 99, 142, 143, 190] 在所有缩放下最多只有 4 个速度 ≤15。odd core {1, 3, 5, 7, 9, 11, 13} 也不是普遍核心；317、347、349、359、367 均有 cover，却无法由它加 7 fillers 完成。

(b) FACT Q2：在这 19 个样本中，最小的「最佳缩放核心」大小恰为 4，且仅上述 389 样本达到；没有样本 ≤3。对所有 p ≤ 499 是否存在 ≤3 的 14-cover：UNFINISHED。 IDEA 389 更像「多尺度核心（multi-scale core）」而非单一 small core。

(c) IDEA Q4：保留规则 14-cover > 0 ⟺ |U_K(p)| ≤ 63, K = {1, 3, 5, 7, 9, 11, 13}.
    FACT 在 33 个 census primes 上为 30/33；错误恰为 383、397、457。

[REASONING — continues below]

FACT 对小速度定义平均冗余 R(v) = avg_{p, w ≠ v} |A_v ∩ A_w| / H.
在 33 个 primes 上：
R(2) = .208, R(3) = .199, R(4) = .217, R(6) = .233
R(7) = .139, R(9) = .149, R(11) = .095, R(13) = .094
R(12) = .191

IDEA 这相当清楚地支持 Tuzi 的方向：2、3、4、6 比 7、9、11、13 更容易浪费在重复覆盖上。12 的零出现也与高冗余一致，但不能由此证明禁掉 12。

FACT 8 是例外：R(8) = .173，却出现 16 次。相对于 odd core 的残余集合，8 平均新增覆盖 19.58 格，是 1–15 中所有非核心候选最高；12 为 14.82。因此 8 高频更像承担 filler/complement 角色。

FACT 对 core-poor 的 389-cover，不同 magnifier 显露不同小块：
u = 1: {1, 4, 11}, u = 2: {2, 8, 9}, u = 4: {4, 5, 7, 13}.
没有一个统一缩放产生 ≥5。

IDEA 所以应把 Tuzi 的假说稍微扩大：
cover = 若干小型局部核心在不同尺度上的互补
而不是必须 一个 ≥5 的 small core + fillers.

IDEA 最不确定的一步：这种「多尺度核心」是否能被定义成真正的缩放不变量（scaling invariant），并由它区分 383/397 与 457。


--- end verbatim ---
END LETTER
