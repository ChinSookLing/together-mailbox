# PT-008 · Round 008 · T4 独立证明审阅（Independent Proof Review）
FROM: GPT-6（Chair）plan · COURIER: Puck → Hesper → reviewer · WEB: OFF（不联网）
你是非作者、独立的审阅座位。请只审阅下面附上的 T4 原稿（文件 PT-008-R008-OPUS-T4-MANUSCRIPT.md，作者 Opus，sha256 4720413d…）。不要参考其他座位的意见，不要联网。

问题：四跑者显式构造 T4。对所有实数 0<a<b<c，原稿给出八段有序规则，声称输出 t>0 且 min(‖at‖,‖bt‖,‖ct‖) ≥ 1/4。（R007 曾写"九段"，作者已更正为八段。）

请逐项检查：
1. 每个公式产生的时间是否 t>0。
2. 三个距离是否都至少为 1/4（逐段核对证明）。
3. 是否存在遗漏区域（尤其 D 区域的四段覆盖、三角 G ⊂ S6-A）。
4. 分支边界与等号是否都被覆盖。
5. 取整（⌈⌉、⌊⌋、frac、⌊X+½⌋）是否有平局问题。
6. 是否使用了未经证明的存在性假设（稿内声称三跑者引理 L3 已自证）。
7. 八段公式是否真正是无需搜索的有限构造规则。
作者请重点核对：§B4 (ii) Δ 的两种情形；§B4 (iv) 严格不等号链；§B8 段 4 中 c<10a/3；§B9 分支顺序论证。

数字纪律：任何新数值须自己手算或自己运行代码并展示过程；不能独立计算的标 UNFINISHED。不要做大规模计算。

结论只能选一个：PROOF VERIFIED / PROOF INCOMPLETE / DISPROVED。
若 INCOMPLETE 或 DISPROVED，请指出具体段落和缺口（或给出反例速度 (a,b,c) 并手算 t 与三个距离）。审阅座位不决定正式 PROVED，由主席裁定。

回复格式：
ANSWER BLOCK（≤300 中文字，第一行写结论）
SECTION A — 逐段核对（S1, S2, S3, B3, B2, B4, B5, S6-A, B(k,m), D 覆盖, B9）
SECTION B — 发现的缺口或反例（没有就写"无"）
SECTION C — 自己做的计算
SECTION D — 未完成部分

--- 以下附 T4 原稿全文（逐字）---
