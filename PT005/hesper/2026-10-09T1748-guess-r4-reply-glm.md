BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 17:48 +08
RE: 猜公式 Round 4 part (a) (packet 61862ac), send text r4_send_glm.txt
SEAT: glm
MODEL: GLM-5.3 Flash (Tuzi's session)
CHAT: (Tuzi relay)

--- reply verbatim ---
[Courier note: Tuzi sent the short R4 version herself on chat.z.ai GLM-5.3 Flash (her session; Hesper's tries at Deep Think Max and Low both ended with empty finals) and pasted the reply in Hesper chat 2026-10-09 17:48 +08. Text after the **** line is a follow-up in the same chat (self-assessment, apparently in answer to Tuzi asking if it was good enough). Verbatim below.]

结论：我预测 307、337、383 都会关门（L16=0）；337 置信度最低。行数量级：307 > 337 > 383。

[FACT] 已给完成数据中所有行最终 L16=0；401 的 tight row {1..15} 到 8p 仍活，16p 死。

1. 预测  
- 307：rows ≈ 25M，range 6M–120M；L2 ≈ 8k，range 100–100k；关门：是。置信 rows 0.40 / L2 0.30 / 关门 0.85。  
- 337：rows ≈ 5M，range 0.5M–50M；L2 ≈ 500，range 10–20k；关门：是。置信 rows 0.35 / L2 0.25 / 关门 0.65。  
- 383：rows ≈ 1M，range 70k–15M；L2 ≈ 25，range 1–1.5k；关门：是。置信 rows 0.30 / L2 0.25 / 关门 0.88。

2. [IDEA] rows(p) 不是 H 的单变量函数；应按 p mod16 / 二倍轨道签名分组，log-rows 随 H 先升后降，H≈15 后快速衰减。

3. [IDEA] 409 的唯一 L2 survivor 应是 {1..15}；它是 tight/minimal row，首次 2-lift 后仍 irredundant，其他行会碰撞或失去覆盖。

4. [UNFINISHED] 最不确定：H=15→25 的衰减外推；尤其 337 因 \(2^{21}\equiv1\) 可能造成异常。
****
够格！自评 7/10 😄

**达标的：**
- 格式全中：结论先行、FACT/IDEA 标注、≤250 字、给了点猜测+范围+置信度
- 亮点：抓到 337 的特殊结构（2²¹ ≡ 1 mod 337，确实成立，337 是 2²¹−1 的因子），这可能是它行为异常的真原因
- “全关门”的方向对——所有 H≥19 的数据都指向 L16=0

**不够好的（诚实说）：**
- rows 点猜测可能偏高：241（H15）还有 2 亿行，但 401（H25）只剩 19.8 万，暴跌了近 1000 倍。我在 H19–23 给的 25M/5M/1M 可能该更接近 1M/100k/20k 这个量级
- 409 的唯一 survivor 是 {1..15} 纯属推断，没验证
- 范围给得偏宽，有点“safe 押注”的味道

总之：结构满分，方向大概率对，数字精度一般。要打分的话老师的点猜测部分会扣分 😅

--- end verbatim ---
END LETTER
