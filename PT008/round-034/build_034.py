import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
rd=lambda p:open(p,encoding='utf8').read()
R='/workspace/work/pt008r33/'
ch=rd('chair/2026-10-21T1120-chair-R034-open-verbatim.txt'); CH=ch[ch.index('TO：Hesper'):]
OP33=rd(R+'replies/2026-10-21T1039-reply-Opus-R033.txt')
DS1=rd(R+'replies/2026-10-21T1047-reply-DeepSeek-R033-S1.txt')
KS1=rd(R+'replies/2026-10-21T1050-reply-Kimi-R033-S1.txt')
TOOLS=rd('hesper/fwcert.py')+'\n# ---- copus.py ----\n'+rd('hesper/copus.py')+'\n# ---- relay.py ----\n'+rd('hesper/relay.py')
STATUS=('R033 记录（不升级）：主席未发 R033 结案裁决；本轮按 R034 任务包开题。FW₄、一般 F_n、一般 C-INIT 均 UNFINISHED；无确认新覆盖；无确认 FW₄ 反例。'
 'R033 原文 sha：Opus c1b027f6（NO-CERT (1,3,4)、引理 W、2CC-A、选择器、实例 (1,3,4,u)；作者 PROOF CANDIDATE；全文附 PART 2）；DeepSeek faa3e8da（FPLC-2 A＋提取 VERIFIED；其分离缺口为代数写反，Hesper 核对）；Qwen 三段（独立 NO-CERT (1,3,4)，第 3 级）；Kimi e67f02de（A＋提取 VERIFIED，B/C UNFINISHED）。'
 '补充审阅 S1（全文附 PART 3）：DeepSeek 39859ccb 与 Kimi c411ba43 均判 Opus R033 (1a)–(1d)、NO-CERT、引理 W、2CC-A、选择器、实例 PROOF VERIFIED；2CC_k 猜想 UNFINISHED（审阅词为审阅人所用；状态以主席裁决为准）。')
LEMMA='已认证可用引理（主席认证，可直接引用）：T4；FW₃；FW₂；FWS(i)（计重数）；FWS(ii)（FW_k ⇒ F^FW 安全，前提不得移除）；CNT k(σ+1)/2。LOCK、FWB、PCL-T、PCL-2、FPLC-2 条件式正确性、2CC-A、主席首窗证书与有理化：引用须标注其审阅状态（无主席认证裁决）。'
FACT=('Hesper 事实（精确分数，CHECKED，不是证明；工具 relay.py）：\n'
 '(1) 主席第五节端点命题与第四节「同一分量窗口不重叠」的有限检查：k=2 δ=1/4 整数≤20（190 组）、k=3 δ=1/5 ≤15（455 组）、k=4 δ=1/6 ≤11（330 组），S 均非空；(b,U) 内窗口端点共 696 / 12,630 / 15,257 个，N(e)<max{N(e⁻),N(e⁺)} 的端点 0 个；同一分量窗口重叠 0；(b,U) 内 N=0 的开段 0 个（与这些输入无 FW 反例一致）。\n'
 '(2) S_{1/5}(1,3,4)={1/5}∪[2/5,9/20]∪[11/20,3/5]∪{4/5}（含两个孤立分量）；B_{1/5}(1,3,4) 在 (0,400) 内 =(0,1/4)。\n'
 '(3) R033 2CC 最少分量数（Hesper 重算，与 Opus R033 §4 一致）：k=3 δ=1/5 ≤15：419 需 1、36 需 2；k=4 δ=1/6 ≤11：306/24；k=5 δ=1/7 ≤9：114/12；无需 ≥3。\n'
 '(4) PT-005 来信统计均按「来信报告、PT-008 未复核」。\n'
 '这些只是有限检查，不代替证明；有限搜索失败不等于不存在。')
PEND='注：主席要求附「R033 主席全轴坏集证明候选」原文；Hesper 处尚无该原文，Tuzi 贴入后作补充件另发，未收到前不得登记已审。'
TASK={'A':'你的任务（主席第七节·Opus，主攻结构定理）：以三旧速度、δ=1/5 为首要测试场，研究失败窗口端点的算术次序。交付一个明确命题及证明尝试，说明为何来自旧速度的端点结构能阻止全部失败同时发生。若提出条件定理，写清条件能否从任意输入验证、能否保证满足。避免只增加另一组特殊速度盒子。你的 R033 原文附 PART 2，两份审阅附 PART 3。',
'D':'你的任务（主席第七节·DeepSeek，独立审查）：先审主席第五节端点命题，包括重复端点、孤立分量、同一分量窗口不重叠（第四节）及严格边界。随后审一个明确的接力结构命题（Opus R034 收到后 Hesper 作补充件转来）。区分：表示法正确／单个输入的有限证书正确／全部输入的非空性保证成立。候选未收到时报告实际审阅范围，不登记预先通过。',
'B':'你的任务（主席第七节·Qwen，精确反例与选择规则）：复用完整安全分量工具（PART 4），寻找能破坏简单接力猜想的精确输入。优先攻击明确命题：固定分量对、按时间顺序选下一分量、只看最近窗口端点等规则；先写规则，再找反例。若研究两分量是否总足够，必须覆盖该输入全部分量对。反例须注明否定的是选择规则、证书数量主张，还是 FW₄ 本身。',
'C':'你的任务（主席第七节·Kimi，对抗审阅及基准复核）：独立审 R033 主席全轴结论 B_{1/5}(1,3,4)=(0,1/4)，包括完整窗口列表、严格端点及 t=4/5 的补充作用（主席证明候选原文另作补充件）。再审一个本轮具体结构或反例，特别检查是否遗漏孤立点、共端点或未选中的安全分量。工具附 PART 4。回复宜 ≤1500 字。'}
SEAT={'A':('Opus','1/4','Tuzi 的 claude.ai（Opus）对话'),
'D':('DeepSeek','2/4','DeepSeek 新对话「PT-008 DeepSeek R034」（深度思考开，联网关）'),
'B':('Qwen','3/4','Qwen 新对话「PT-008 Qwen R034」（Play CF 项目，thinking，web 关）'),
'C':('Kimi','4/4','Kimi 新对话「PT-008 Kimi R034」（思考模式开，联网关）')}
P2='############ PART 2 · Opus R033 原文（sha c1b027f6…，逐字；含 NO-CERT、引理 W、2CC-A、选择器）############\n'+OP33
P3=('############ PART 3a · DeepSeek R033 S1 审阅原文（sha 39859ccb…，逐字）############\n'+DS1+
 '\n\n############ PART 3b · Kimi R033 S1 审阅原文（sha c411ba43…，逐字）############\n'+KS1)
P4='############ PART 4 · Hesper 精确工具（Python，Fraction；可复用）############\n'+TOOLS
EXTRA={'A':'','D':'','B':P4,'C':P4}
FMT='''############ 回复格式 ############
第一行写「R034 {n} {seat}」。先写简短 ANSWER BLOCK：状态；确切新增命题或反例；是否证明非空；是否给出选择规则；适用范围；最弱未证步骤。
附必要的精确推导或可复核代码；按需使用 IDEA / CHECKED / PROOF CANDIDATE / PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED，作者结果与非作者审阅分别记录。失败尝试与更正原样保留。
七栏登记（沿用）：1 数学有效性及审阅状态；2 对统一构造的具体推进；3 是否保证非空；4 是否处理任意实数速度；5 是否保证有限提取；6 是否满足直接构造目标；7 是否能随人数推广。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers. 引用 Hesper 或 PT-005 数字须注明来源。
WEB OFF。作者不能升级自己的结果；只有主席裁决。数值观察不替代普遍证明；完整枚举与等价改写须如实报告方法局限。
'''
for key,(seat,n,where) in SEAT.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 034 · Phase Relay：失败窗口的次序与安全接棒
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R034 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 034 · Phase Relay, for {seat}.
TO: {seat}
ASK: do YOUR task (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: why the relay of surviving safe components cannot break on (b,U), and how to locate a surviving component directly. FW₄, general F_n, general C-INIT UNFINISHED. Goal: One formula for all, and all in one formula.
''','############ PART 0 · 你的任务 ############\n'+TASK[key]+'\n\n'+STATUS+'\n\n'+LEMMA+'\n\n'+FACT+'\n\n'+PEND+'\n',
    '############ PART 1 · 主席 R034 任务包（原文）############\n'+CH, P2, P3, EXTRA[key],
    FMT.format(n=n,seat=seat)+'===== END =====\n']
    txt='\n'.join(x for x in p if x); fn=f'pkg/send_034_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode())[:8])
