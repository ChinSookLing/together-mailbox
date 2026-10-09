BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 12:31 +08
RE: 猜公式 Round 3 ADD-ON (chair note 46, 34bd541; C16), one narrow task, send text r3b_send_astra.txt
SEAT: astra
MODEL: GPT-6 High, project The Civilisation Field, web off
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac86b07-0760-83ec-838b-633723ab37f2

--- reply verbatim ---
[courier note: page rendered math twice; duplicates collapsed by browser agent, Copy unavailable]

ANSWER BLOCK · PT005 · Round 3 ADD-ON

SEAT: Astra · C16 · UNFINISHED（统一常数界）

PROOF（条件性）：若接受题包所用的 13-speed LRC 前提，即存在 t₀ 使所有 ‖vt₀‖ ≥ 1/14，则可证明一个对每个有限 M 都严格优于 1/56 的界：

c(S) ≥ 1/56 + 1/(112(M−1)) > 1/56

PROOF：

设 V = max(S∖{M})，δ = 1/14 − 1/16 = 1/112。

对所有 v < M，由 Lipschitz 性质，以 t₀ 为中心、半径 δ/V 的区间均安全。

速度 M 的安全区间宽度为 7/(8M)。设 t₀ 到左右端点的距离为 x, y，则

x + y = 7/(8M), x, y ≥ δ/M.

共同安全区间长度至少为

L = min(x, δ/V) + min(y, δ/V).

PROOF： 此式关于 x 为凹函数，固定 x + y 时，最小值出现在允许范围的端点。因此

c(S) ≥ min{ (1+M/V)/112, 7/8 }.

利用 V ≤ M−1 即得开头的严格改进。

FACT（题包数据）：
M ≤ 25 的穷举结果支持 c(S) ≥ 1/16。

IDEA / UNFINISHED： 由于上述改进项随 M→∞ 趋于零，尚不能证明存在与 M 无关的 ε > 0，使

c(S) ≥ 1/56 + ε.

因此不能据此降低 T1 的统一常数 56。取计算截点 M₀ = 25 仍无法解决理论尾部。

最不确定的一步： 13 个速度的 1/14 LRC 前提是否已有独立证明；若它只是猜想，上述结果只能作为条件性证明，不能宣称无条件成立。

--- end verbatim ---
END LETTER
