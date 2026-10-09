BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 11:13 +08
RE: 猜公式 Round 3 packet (1aeab1c), rules header + own §A line + BEGIN…END block pasted verbatim (send text r3_send_gpt.txt)
SEAT: gpt
MODEL: GPT-5.6 Sol, Thinking High (captured via page extract; Copy button copied prompt)
CHAT: https://chatgpt.com/c/6ac85b03-445c-83ec-a984-541532353847

--- reply verbatim ---
ANSWER BLOCK

§A — PROOF: YES。
PROOF: Kimi 2(c) 的常数变换正确。若非紧致余量（non-tight gap）给 ∥𝑣𝑖𝑥∥ ≥ 1/14 + 𝜂，把 𝑥 舍入最近的 𝑡/𝑝，误差至多 𝑣𝑖/(2𝑝) ≤ 𝑀/(2𝑝)。要保持 ∥𝑣𝑖𝑡/𝑝∥ ≥ 1/16，只需 𝑀/(2𝑝) ≤ 1/14 − 1/16 + 𝜂 = 1/112 + 𝜂。因此常数变成 𝐶(𝜂) = 1 / 2(1/112 + 𝜂)。
FACT: 𝜂 = 1/500 时 𝐶 = 45.751633…，所以 45.75 正确。

§A — PROOF: YES，LP 值恰为 𝑛/𝐻。
PROOF: 原始 fractional cover 取每个速度权重 𝑥𝑣 = 1/𝐻；每个 cell 恰被 𝐻 个速度覆盖，所以可行，总权重 𝑛/𝐻。
PROOF: 对偶取每个 cell 权重 𝑦𝑡 = 1/𝐻；每个速度恰覆盖 𝐻 个 cells，所以对偶可行，总权重同为 𝑛/𝐻。
PROOF: 弱对偶（weak duality）立即夹出 optimum = 𝑛/𝐻；甚至不需要额外调用 strong duality。

§B — PROOF: 我选 1，discrepancy route。结果：目前不会改进 56。
PROOF: F5 的 1/14 点周围至少有半径 1/(112𝑀) 的安全邻域，因此 𝐿 ≥ 1/(56𝑀)。
若缩放后 𝑀 ≤ 𝑝/𝑁，则 𝐿 ≥ 𝑁/(56𝑝)。
PROOF: 配合 𝑘 ≤ ∑𝑣 ≤ 13𝑝/𝑁 和条件 𝑝𝐿 > 𝑘，只能得到 𝑁² > 728𝑝。
FACT: 这个估计没有从现有材料产生比 Lemma A 更好的统一常数；它本质上重新表达了那个 1/(56𝑀) 安全段。

§C — IDEA: 推荐 Guillem Perarnau；他最适合从 Lonely Runner 本身的组合结构审读，而不是只审计算证书。

IDEA — 我最不确定的一步： 是否能把 𝑘 ≤ ∑𝑣 利用大量端点重合或结构约束显著压低；本轮没有证明这种改进存在。

--- end verbatim ---
END LETTER
