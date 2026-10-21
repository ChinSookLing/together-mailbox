import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
rd=lambda p:open(p,encoding='utf8').read()
ch=rd('chair/2026-10-21T1030-chair-R033-open-verbatim.txt'); CH=ch[ch.index('TO：Hesper'):]
a1=rd('chair/2026-10-21T1031-chair-R033-A1-verbatim.txt'); A1=a1[a1.index('TO：Hesper'):]
OPL=rd('chair/2026-10-21T1033-Opus-PT005-letter-B2-verbatim.txt')
OP32=rd('/workspace/work/pt008r32/replies/2026-10-21T0958-reply-Opus-R032.txt')
CERT=rd('hesper/fwcert.py')+'\n# ---- copus.py (bad set B(V) on u in (0,U), exact) ----\n'+rd('hesper/copus.py')
STATUS=('R032 记录（不升级）：主席未发 R032 结案裁决；本轮按 R033 任务包开题。FW₄、一般 F_n、一般 C-INIT 均 UNFINISHED；无确认新覆盖；无确认 FW₄ 反例。'
 'R032 原文 sha：Opus 2330ee7d（LOCK、PCL-T、PCL-2，作者 PROOF CANDIDATE；附于下文）；DeepSeek f6d419d6（审 Opus R031 FWB/FW-EQ/FW-REG：PROOF VERIFIED）；Qwen 23c13732/0ee45035/ee802108（C-INIT 易向命题 1、分量 q 有限命题 2，PROOF CANDIDATE 待审）；Kimi b666a5db（主席基准 B_{1/5}(1,2,3)=(0,1/4) VERIFIED）。'
 '补充审阅 S1：DeepSeek fc43ab8a 与 Kimi 709b4687 均判 Opus LOCK、PCL-T、PCL-2（充分条件）PROOF VERIFIED（审阅词为审阅人所用；状态以主席裁决为准）。')
LEMMA='已认证可用引理（主席认证，可直接引用）：T4；FW₃；FW₂；FWS(i)（计重数）；FWS(ii)（FW_k ⇒ F^FW 安全，前提不得移除）；CNT k(σ+1)/2。主席任务信称 LOCK 为「已接受」；FWB、PCL-T、PCL-2、主席首窗证书与有理化尚无主席认证裁决，引用须标注。'
FACT=('Hesper 事实（精确分数，CHECKED，不是证明）：\n'
 '(1) PCL-T 的锁与区间代入 FPLC-2（τ₁=1/(k+1), m₁=k；τ₂=1/(k+2), m₂=k+1；r/s=(k+1)/(k+2)；I=[τ₁−h, τ₁+h], h=1/(k(k+1)(k+2))）：k=2..8 全部满足 (m_i+1)δ≤1、分离 η₁+η₂≤1/(rτ₁)（左端 17/24, 31/60, 49/120, 71/210, 97/336, 127/504, 161/720，右端 1）、η=1/(k+1)≤b、C−η≥U（C=(k+1)(k+2), U=k(k+1)）。\n'
 '(2) 第五节提取规则在同一证书上（k=2..6）：14,965 个随机有理 u>b 中，四锁点全失败的 356 个，区间分支输出 t∈I 且 ‖ut‖≥δ，0 失败。\n'
 '(3) Opus R032 报告 k=3、δ=1/5、速度≤15 的 455 组中 30 组未被骨架两锁封死（原文列出 6 例：(1,3,4)、(1,4,5)、(1,8,9)、(1,9,10)、(1,13,14)、(2,5,7)）；Hesper R032 核对：其中所测 6 例 B∩(b,∞) 均为空——即非 FW₄ 反例。Hesper 未重算 30/455 计数。\n'
 '(4) PT-005 来信中的统计（308,449；417,077；1,088,175；86,477；522；1,549 等）均按「来信报告、PT-008 未复核」登记。\n'
 '这些只是有限检查，不代替证明。')
TASK={'A':'你的任务（主席第六节·Opus，主攻证书存在性）：先提取 FPLC-2 限制了哪些算术结构，再研究一般旧速度能否提供它们。优先 k=3、δ=1/5 的一般输入，尤其 R032 未封死样本。交付之一：有实质推广能力的证书存在性定理；或无法拥有 FPLC-2 证书的精确速度构型及证明；或明确指出哪项条件过强并提出可独立审阅的替代条件。不以另一个特选整数行族作为主要验收结果。按补充 A1：PT-005 离散证据只作 IDEA；τ 与 1−τ 称反射时间对，与对跖结构、LOCK 倍数结构的联系须分别证明。你的 R032 原文附于 PART 3 供引用。',
'D':'你的任务（主席第六节·DeepSeek，主审正确性）：独立审主席任务包第四、五节（FPLC-2 给定证书后的保证与提取规则）。给出 PROOF VERIFIED、GAP FOUND 或 DISPROVED，并写出准确修正；特别核查等号、整数中心、首窗条件，以及提取规则只假定「四锁点失败」而不再假定全部 S 失败。不要把证书存在性当作已实现的前提。同时检查 R032 PCL-T 所用锁与区间能否满足本证书条件，作为一致性基准（Opus R032 原文附于 PART 3）。按补充 A1：不因离散类比而跳过证明。',
'B':'你的任务（主席第六节·Qwen，精确构造与障碍）：选择一个 R032 未封死样本（见 PART 3 Opus R032 §3），提供完整旧安全集合；尝试构造 FPLC-2，或分析其不可能性。若搜索未找到，必须报告搜索边界：时间表示、比例分子分母、倍数及区间选择范围；有限搜索失败不得提升为证书不存在。如提出新选择规则，说明为何能从速度直接产生锁与区间、为何保证有限完成。按补充 A1 第四节区分：两锁条件过强／需更多锁或更高阶关系／需相位外额外约束／原首窗命题失败。Hesper 精确工具附于 PART 4，可复用。',
'C':'你的任务（主席第六节·Kimi，对抗审阅）：独立攻击 FPLC-2 证书的正确性、边界及存在性主张。严格区分四项：1 这组锁不合格；2 一个有限搜索范围内没有证书；3 该输入不存在任何 FPLC-2 证书；4 该输入没有首窗安全时间。四项强度不同，不得互相替代。并按补充 A1 第四节区分失败原因。Opus 或 Qwen 的 R033 新命题收到后，Hesper 会作补充件转给你；未收到原文不得登记已审。Opus R032 原文附于 PART 3；Hesper 精确工具附于 PART 4。回复宜 ≤1500 字。'}
SEAT={'A':('Opus','1/4','Tuzi 的 claude.ai（Opus）对话'),
'D':('DeepSeek','2/4','DeepSeek 新对话「PT-008 DeepSeek R033」（深度思考开，联网关）'),
'B':('Qwen','3/4','Qwen 新对话「PT-008 Qwen R033」（Play CF 项目，thinking，web 关）'),
'C':('Kimi','4/4','Kimi 新对话「PT-008 Kimi R033」（思考模式开，联网关）')}
P2=('############ PART 2 · 主席补充 A1（原文）############\n'+A1+
 '\n\n############ PART 2b · Opus（PT-005 主席）来信，含警告与归功（原文，按 A1 完整附上；离散模型，仅 IDEA；统计为来信报告、PT-008 未复核）############\n'+OPL)
P3='############ PART 3 · Opus R032 原文（sha 2330ee7d…，逐字；含 LOCK、PCL-T、PCL-2 与未封死样本）############\n'+OP32
P4='############ PART 4 · Hesper 精确工具（Python，Fraction；可复用）############\n'+CERT
EXTRA={'A':P3,'D':P3,'B':P3+'\n\n'+P4,'C':P3+'\n\n'+P4}
FMT='''############ 回复格式 ############
第一行写「R033 {n} {seat}」。先写简短 ANSWER BLOCK：状态；本轮确切新增命题或反例；回答 A、B、C 中哪项；适用速度与人数；最弱未证步骤。
正文附必要证明、精确计算或可复核代码；按需使用 IDEA / CHECKED / PROOF CANDIDATE / PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED，作者结果与非作者审阅分别记录。必须写出「最不确定的一步」。失败尝试与更正原样保留。
七栏登记（沿用）：1 数学有效性及审阅状态；2 对统一构造的具体推进；3 是否保证非空；4 是否处理任意实数速度；5 是否保证有限提取；6 是否满足直接构造目标；7 是否能随人数推广。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers. 引用 Hesper 或 PT-005 数字须注明来源。
WEB OFF。作者不能升级自己的结果；只有主席裁决。仅验证更多样本、重述非空性、或列出未证明普遍可满足的条件，不登记为统一突破。
'''
for key,(seat,n,where) in SEAT.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 033 · 有限相位锁证书：正确性、存在性与直接生成
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R033 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 033 · Finite Phase-Lock Certificate (FPLC-2), for {seat}.
TO: {seat}
ASK: do YOUR task (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: (A) correctness of FPLC-2 given a certificate, (B) existence for every input, (C) direct generation. Proving A does not prove B or C. FW₄, general F_n, general C-INIT UNFINISHED. Goal: One formula for all, and all in one formula.
''','############ PART 0 · 你的任务 ############\n'+TASK[key]+'\n\n'+STATUS+'\n\n'+LEMMA+'\n\n'+FACT+'\n',
    '############ PART 1 · 主席 R033 任务包（原文）############\n'+CH, P2, EXTRA[key],
    FMT.format(n=n,seat=seat)+'===== END =====\n']
    txt='\n'.join(x for x in p if x); fn=f'pkg/send_033_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode()))
