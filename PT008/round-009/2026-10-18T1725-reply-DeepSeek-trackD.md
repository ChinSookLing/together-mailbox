# PT-008 Round 009 · Track D independent review · DeepSeek
FROM: Hesper (carrier) · TO: Puck → GPT-6 (chair)
SEAT: DeepSeek · MODEL: DeepSeek DeepThink ON, Search OFF · WEB: OFF · NEW CHAT
CHAT: https://chat.deepseek.com/a/chat/s/400ea696-65ae-4491-a29e-f764698cd5e9
COPIED: 2026-10-18 17:25 +08
SEND TEXT: PT008/round-009/send_009_hesper_trackD_review.txt (commit 6eead36). Pasted text = header + statement + chair R008 proof excerpt; the full chair brief appendix in the committed file was NOT pasted.
VERDICT (seat's own): PROOF VERIFIED — reviewer verdict only; seats do not grant PROVED.
REPLY SHA256 (body below, UTF-8): e45bfabca38f0f083a15323f00d7c75efe1d69bb89082f92b1fca25ad8cf7d4b

--- REPLY VERBATIM ---

ANSWER BLOCK（≤300 中文字，第一行写结论）
PROOF VERIFIED（按原文，n为总人数，非参考数n−1；n≥2）。一般 v∈[a,b] 得 vt∈[a/(a+b),b/(a+b)]；条件 b≤(n−1)a 恰给下界≥1/n、上界≤1−1/n，故圆周距离≥1/n。等号、实数、重复速度均无碍；参考平移后取绝对值正确，a>0排除零速度。证明完整，无实质缺口。

SECTION A — 逐项核对
1. 等号：b=(n−1)a 时，最小 x=a/(a+b)=1/n，最大 x=b/(a+b)=1−1/n，二者到最近整数距离均=1/n；内部 v 的 x 在区间内，距离≥1/n。重复速度不改变逐项估计；a=b 时 x=1/2，n=2等号，n>2时1/2≥1/n。
2. 实数：证明只用 v∈[a,b] 与不等式，不假设整数/有理数。
3. 参考变换：以参考速度 V0，非参考相对速度 r_i=V_i−V0；距离 ‖(V_i−V0)t‖=‖|V_i−V0|t‖，平移不变成对距离，负号无问题。若 r_i=0 则距离0，但命题 a>0 已排除。
4. 人数：按原文五跑者，n=总人数，非参考数 n−1；n=2,3,4,5及一般 n≥2 均成立，目标1/n与总人数一致。
5. 步骤：v_i∈[a,b] ⇒ x_i=v_i/(a+b)∈[a/(a+b),b/(a+b)]；b≤(n−1)a ⇔ a/(a+b)≥1/n；同条件 ⇔ b/(a+b)≤(n−1)/n=1−1/n；故 x_i∈[1/n,1−1/n]，圆周距离≥1/n。完整。

SECTION B — 缺口或反例
无实质缺口。仅措辞建议：原文“全部跑者的孤独距离要求”应明确为“参考者与每位非参考者距离≥1/n”；参考者自身距离0不参与该要求。

SECTION C — 自己做的计算
n=5,a=1,b=4,t=1/5：速度1,2,3,4 得距离1/5,2/5,3/5,4/5，min=1/5。
n=3,a=1,b=2,t=1/3：速度1,2 得距离1/3,2/3，min=1/3。
n=2,a=b=1,t=1/2：距离1/2。
重复例 n=5,a=b=1,t=1/2：x=1/2，距离1/2≥1/5。
参考变换例 V0=10,V1=11,V2=12,V3=13,V4=14，相对绝对值1,2,3,4，同上；V0=10,V1=9 得|−1|=1，距离同。

SECTION D — 未完成部分
无。仅建议定稿明确 n 的定义与“全部跑者”的措辞。
