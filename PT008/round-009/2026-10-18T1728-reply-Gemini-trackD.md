# PT-008 Round 009 · Track D independent review · Gemini (fresh chat, not Argon)
FROM: Hesper (carrier) · TO: Puck → GPT-6 (chair)
SEAT: Gemini (fresh chat, not Argon) · MODEL: Gemini 3.1 Pro, Thinking High, Personal Intelligence OFF · WEB: OFF · NEW CHAT
CHAT: https://gemini.google.com/app/8508333ee32ba2a5
COPIED: 2026-10-18 17:28 +08
SEND TEXT: PT008/round-009/send_009_hesper_trackD_review.txt (commit 6eead36). Pasted text = header + statement + chair R008 proof excerpt; the full chair brief appendix in the committed file was NOT pasted.
VERDICT (seat's own): PROOF VERIFIED — reviewer verdict only; seats do not grant PROVED.
REPLY SHA256 (body below, UTF-8): c0f04455b074de4a3cda799bfdba6f672a6c519f374fedbc586d677757d040f6

--- REPLY VERBATIM ---

ANSWER BLOCK
PROOF VERIFIED
主席提出的跑者引理及构造性证明逻辑严密、完全正确。该证明巧妙利用非参考跑者相对速度绝对值的上下界，直接构造出使所有非参考位置同时落在安全区 [1/n, 1−1/n] 的时间 t=1/(a+b)。此结论不依赖有理数或整数假设，且绝对值变换在圆周距离 ∥x∥=∥−x∥ 的性质下完全合法。证明不存在缺口，是一条极为完备且优美的条件性引理。

SECTION A — 逐项核对
等号情形：当 b=(n−1)a 时，t=1/(na)。最慢的非参考跑者位置 at=1/n，最快的非参考跑者位置 bt=(n−1)/n=1−1/n，两者的圆周距离均为 1/n，完美满足。速度相等或重复时（如 a=b），只要 n≥2，不等式 a≤(n−1)a 依然成立，逻辑畅通无阻。
实数速度：证明全过程仅使用了线性不等式的放缩（a≤v≤b），完全适用于实数域，不需要假设速度为整数或有理数。
参考速度变换：将参考跑者设为 0，其他跑者取相对速度的绝对值（ui=|vi−vref|）是绝对正确的。因为题目考察的是圆周上的最短距离，具有对称性 ∥x∥=∥−x∥，所以负方向的速度不影响与起点的绝对距离。且 a>0 保证了没有非参考跑者相对静止，避开了零速度异常。
适用人数：n 明确代表总人数（包含 1 名参考跑者与 n−1 名非参考跑者）。目标界限是 1/n。代入验证：当 n=2 时，条件为 b≤a（即 a=b），t=1/(2a)，距离 1/2≥1/2，完全自洽；对任意 n≥2 均成立。
证明是否完整：完整。隐含了一个非常坚实的几何事实：只要变量 X∈[1/n, 1−1/n]，其距离最近整数的距离就必定 ≥1/n。证明一次性把所有速度"压缩"到了第一个周期内，没有越界跨周期的问题，无任何逻辑漏洞。

SECTION B — 缺口或反例
无。

SECTION C — 自己做的计算
设非参考跑者的相对速度绝对值为 ui，已知对于所有 i 有：0 < a ≤ ui ≤ b ≤ (n−1)a。
选取时间 t=1/(a+b)。
计算各跑者的位置 uit：
下界：uit = ui/(a+b) ≥ a/(a+b)。因为 b≤(n−1)a，所以 a+b≤na，故 a/(a+b) ≥ 1/n。
上界：uit = ui/(a+b) ≤ b/(a+b) = (a+b−a)/(a+b) = 1 − a/(a+b)。结合前述 a/(a+b) ≥ 1/n，可得 b/(a+b) ≤ 1−1/n = (n−1)/n。
因此，所有非参考跑者在时刻 t 的位置满足：uit ∈ [1/n, (n−1)/n]。
在该区间内，实数到最近整数的距离即为 min(uit, 1−uit)，显然有：∥vit∥ = ∥uit∥ ≥ 1/n。
计算确认无误。

SECTION D — 未完成部分
无。（该引理是一条"条件性引理"，正如主席所述，它依赖于 b≤(n−1)a 的前提，因此不是一般 LRC 的完整解。但就该引理自身的命题与证明而言，已 100% 完成且封闭）。
