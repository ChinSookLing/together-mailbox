# PT-008 · R008 · Track A · Independent T4 review — DeepSeek
CARRIED_BY: Hesper · package review_package_R008.md (commit ee00a4a), manuscript sha256 4720413d78955ea05f7d66bcb0136ff93c0231a954120a4b482fa8a11ae07408
Collected: 2026-10-18 16:2x +08 · reply-body sha256 (capture file): 8fe019cc4d01a57ee49ea5c286d72becf78648c9730cdb9ee9c67b422c6d0333
Seat verdict: PROOF VERIFIED (reviewer verdict only; NOT PROVED — chair GPT-6 rules)
Hesper note: DeepSeek's 'B4 边界 (3/2,3,5)' test applies t=4/(b+c) directly; under T4's branch order that point (r=5/3, s=16/3≤8) is taken by B2 first (t=2/8=1/4: at=3/8, bt=3/4, ct=5/4 → 3/8, 1/4, 1/4 ✓) — its B4 arithmetic is right but the label is not T4's routing. Its G example (1,21/10,63/20): Hesper re-checked t=60/83 → 23/83, 40/83, 23/83 ✓.

---

<!--
CHAT URL: https://chat.deepseek.com/a/chat/s/123d4f41-d29c-43e6-909c-da012b86f805
MODEL / MODE: DeepSeek — DeepThink ON (reasoning "Thought for 107 seconds"), Search OFF (WEB OFF per package)
SIGN-IN: Log in with Google → csllanna@gmail.com (Chin Sook Ling); phone-approval on Apple iPhone 11 Pro Max (no match number shown by Google). Email/password login not used.
PACKAGE SENT: PT-008 · Round 008 · T4 独立证明审阅（Independent Proof Review）— pasted verbatim, sent once. No Stop/Regenerate/resend during this task.
COPY TIME (UTC): 2026-10-18 (copy made immediately after generation finished; "Thought for 107 seconds" header rendered, send button reverted, chat scrolled to bottom with no further content below).
TRUNCATION NOTE: Reply does NOT look cut off. Ends cleanly on "SECTION D — 未完成部分 无。未联网，未参考其他座位；未做大规模计算；Track B 不在本审阅范围。" followed by DeepSeek's standard footer "DeepThink Search AI-generated, for reference only". All four required sections (ANSWER BLOCK, A, B, C, D) are present. Verdict: PROOF VERIFIED.
LOOP CHECK: No looping observed; the model's content advanced linearly from segment-by-segment reasoning into the final formatted answer.
NOTE: The text below is DeepSeek's visible final reply only. The 107-second DeepThink thinking block is NOT included per the task ("copy the FINAL reply ... not the thinking").
-->

ANSWER BLOCK 结论：PROOF VERIFIED。八段顺序覆盖完整；各支 t>0 且三距离≥1/4。D 四段并集为 (1,3)，G⊂S6-A。等号与取整平局安全。L3 自证成立，未用外部存在性。仅 B4(iv) 对 j=0 的 Δ 未定义，但 jη=0 直接满足同一上界，属表述可补，不构成缺口。

SECTION A — 逐段核对
S1：t=1/(4a)>0；at=1/4，bt,ct∈(1/4,3/4]，c=3a 等号安全。
S2：L3 给 at₀,bt₀≥1/3；直接输出时 ct 已≥1/4。否则 |e|<1/4，ct 距=1/4，|t−t₀|≤1/(4c)≤1/(12b)，L0 得 bt≥1/4、at>1/4；t>0。平局 |e|=1/2 不在分支内。
S3：锁相 bt+ct∈ℤ，配对 frac∈[1/4,3/4)；at≥1/4；上界得 at<1/4+2a/(b+c)+a/(2b)<3/4，因 b≥3a 且 c>b；故 at∈[1/4,3/4)。t>0。
B3/B2/B4/B5：B(k,m) 公式及四块端点核对无误；D 中 4<s<12，相关 s 条件自动满足或等价；r=7/5,5/3,13/7 与 s=8,16/3,20/3 等边界均安全。
S6-A：at∈[1/4,3/4]，ct 同距；bt∈[5/4,7/4] 当 b 在给定区间，故三距离≥1/4。
D 覆盖：四段并为 (1,3)；G 中 c<10a/3<11a，b 上下界成立，故 G⊂S6-A。
B9：前四支失败 ⇒ r>7/5；r≥5/3 时由 B8 矛盾；故 r∈(7/5,5/3)，B4 失败给 s<16/3，即 G，S6-A 成立。分支顺序无遗漏。
有限构造：八段条件有限，S2/S3 固定取整，无循环搜索。

SECTION B — 发现的缺口或反例
无实质缺口或反例。仅 B4(iv) 在 j=0 时 Δ 未定义；但 j=0 时 jη=0 直接满足同一上界，建议补一句说明。等号与取整平局均安全。

SECTION C — 自己做的计算
S2 (1,2,6)：t₀=1/3，X=2，t=3/8；距离 3/8,1/4,1/4。
B4 边界 (3/2,3,5)：r=5/3，s=16/3，t=1/2；距离 1/4,1/2,1/2。
G/S6-A 例 (1,21/10,63/20)：r=3/2，s=21/4<16/3，t=60/83；距离 23/83,40/83,23/83，均≥1/4。

SECTION D — 未完成部分
无。未联网，未参考其他座位；未做大规模计算；Track B 不在本审阅范围。