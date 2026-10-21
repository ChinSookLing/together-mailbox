import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
ch=open('chair/2026-10-21T0951-chair-R032-open-verbatim.txt',encoding='utf8').read()
CH=ch[ch.index('TO：Hesper'):]
OP31=open('/workspace/work/pt008r31/replies/2026-10-21T0918-reply-Opus-R031.txt',encoding='utf8').read()
CERT=open('hesper/fwcert.py',encoding='utf8').read()+'\n# ---- copus.py (bad set B(V) on u in (0,U), exact) ----\n'+open('hesper/copus.py',encoding='utf8').read()
STATUS=('R031 记录（不升级）：主席未发 R031 结案裁决；本轮按 R032 任务包开题。FW₄、一般 F_n 均 UNFINISHED；无确认新覆盖；无确认 FW₄ 反例。'
 'R031 原文 sha：Opus ec869f35（DEC=正时间插入非首窗；FWB、FW-EQ、FW-REG、猜想 C-INIT，均作者 PROOF CANDIDATE，无非作者审阅）；DeepSeek a0b2b070（审 Opus R030：A1 VERIFIED 仅正时间、DEC GAP FOUND、UPD VERIFIED 条件性）；'
 'Qwen 00a3f3dc/6b9e8202/39bd7a02（路线 B 无新原理；贪心 Q-B2 DISPROVED，例 (1,2,3,41/10)）；Kimi 5937c3af（首窗证书与主席有理化 A/B：PROOF VERIFIED，一份非作者审阅）。')
LEMMA='已认证可用引理（主席认证，可直接引用）：T4；FW₃；FW₂；FWS(i)（计重数）；FWS(ii)（FW_k ⇒ F^FW 安全，前提不得移除）；CNT k(σ+1)/2。PS_n、GLC、SPC、FWB、主席首窗证书、主席有理化均未经主席认证，引用须标注。'
FACT=('Hesper 事实（精确分数，CHECKED，不是证明；来源 R031 Hesper 核对，mailbox round-031）：\n'
 '(1) 首窗证书：整数四元组 1≤a<b<c<d≤24 共 10,626 组全有首窗见证；随机有理 2,999 组 0 无见证。\n'
 '(2) S_{1/5}(1,2,3)∩(0,1) 四分量 [1/5,4/15]、{2/5}、{3/5}、[11/15,4/5]；B_{1/5}(1,2,3)（u∈(0,200)）精确为 (0,1/4)，与主席第四节一致；t*=4/5 处三距离 (1/5,2/5,2/5) 一致。\n'
 '(3) C-INIT（B=(0,δ/R_max)）仅在 u≤(k+1)v_max 上检查：k=2 δ=1/4 整数≤30 共 435 组、k=3 δ=1/5 ≤20 共 1,140 组、k=4 δ=1/6 ≤13 共 715 组、随机有理三元组 400 组，均 0 例外。\n'
 '(4) Qwen 贪心最小整数规则在 (1) 的 10,626 组中失败 1,310 组（规则失败，非 FW₄ 反例）。\n'
 '这些只是有限检查，不代替证明。')
TASK={'A':'你的任务（主席第五节·Opus）：以完整安全分量为对象，提出一个明确的相位冲突命题（PCL），并尝试证明；优先：从旧速度直接确定若干分量及其关系，证明它们不能在 u>b 时全部被遮住。可先证有实质结构的一族，但须指出哪些步骤可推广、哪些依赖特殊速度。并明确 C-INIT（B=(0,δ/R_max)）与较弱目标 B∩(b,∞)=∅ 的区别。你的 R031 原文（FWB/C-INIT）你已有，不重附。你的新命题会转给 DeepSeek 与 Kimi 审。',
'D':'你的任务（主席第五节·DeepSeek）：主审 Opus R031 的 FWB／FW-EQ／FW-REG 原文（附于 PART 2，sha ec869f35）。勿把你对 R030 的审阅自动套到新命题。核查：空安全集、正长度假设、有限性、高速界、严格端点、全部量词。Opus 的 R032 新结构命题收到后，Hesper 会作补充件转给你；如来不及，本轮先完成 FWB 审阅即可，不制造已审阅的印象。',
'B':'你的任务（主席第五节·Qwen）：从完整安全集合及精确失败条件出发，攻击：A 固定两分量版本；B 允许多分量的明确版本；C C-INIT（陈述见 PART 2 Opus R031 第 III 部分）。每个反例注明：完整输入、门槛与首窗；新速度是否超过旧最大速度；推翻哪条确切命题；是否仍存在其他安全分量或成功时间。特别关注非整数有理速度及可精确处理的不可公度例子。近似数值不得作端点等号的最终依据。Hesper 精确工具附于 PART 3，可复用。',
'C':'你的任务（主席第五节·Kimi）：独立对抗审阅。先审主席第四节测试基准 V=(1,2,3)（B_{1/5}(1,2,3)=(0,1/4)）。再审一个明确的相位冲突候选或反例：Opus/Qwen 的 R032 回复收到后，Hesper 会作补充件转给你。检查是否遗漏孤立点、安全边界或未选中的分量。若无完整失败证书，不得把候选规则失败登记为 FW₄ 反例。Hesper 精确工具附于 PART 2，可复用。回复宜 ≤1500 字。'}
SEAT={'A':('Opus','1/4','Tuzi 的 claude.ai（Opus）对话'),
'D':('DeepSeek','2/4','DeepSeek 新对话「PT-008 DeepSeek R032」（深度思考开，联网关）'),
'B':('Qwen','3/4','Qwen 新对话「PT-008 Qwen R032」（Play CF 项目，thinking，web 关）'),
'C':('Kimi','4/4','Kimi 新对话「PT-008 Kimi R032」（思考模式开，联网关）')}
OPX='############ PART 2 · Opus R031 原文（sha ec869f35…，逐字）############\n'+OP31
EXTRA={'A':'','D':OPX,'B':OPX+'\n\n############ PART 3 · Hesper 精确工具（Python，Fraction；可复用）############\n'+CERT,
'C':'############ PART 2 · Hesper 精确工具（Python，Fraction；可复用）############\n'+CERT}
FMT='''############ 回复格式 ############
第一行写「R032 {n} {seat}」。先写简短 ANSWER BLOCK：状态；本轮确切新增内容；是否证明非空；是否给出直接见证；适用人数与速度范围；最弱未证步骤。
正文按需使用 IDEA / CHECKED / PROOF CANDIDATE / PROOF VERIFIED / DISPROVED / UNFINISHED，区分作者证明与非作者审阅。必须写出「最不确定的一步」。失败尝试与修正原样保留。
七栏登记（沿用 R031）：1 数学有效性及审阅状态；2 对统一构造的具体推进；3 是否保证非空；4 是否处理任意实数速度；5 是否保证有限提取；6 是否满足直接构造目标；7 是否能随人数推广。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers. 引用 Hesper 既有核对须注明来源。
WEB OFF。作者不能升级自己的结果；只有主席裁决。有限样本成功不是全域证明；数值无解不是反例证书。仅重列坏集公式、扩大随机测试或重述统一目标，不算理论突破。
'''
for key,(seat,n,where) in SEAT.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 032 · 相位冲突：哪些失败方式不能同时发生？
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R032 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 032 · Phase-Conflict Lemma (PCL), for {seat}.
TO: {seat}
ASK: do YOUR task (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: find structural conflicts between the exact failure conditions of old safe components when a faster runner u>b is added (PCL = IDEA only). General F_n still UNFINISHED. Goal: One formula for all, and all in one formula.
''','############ PART 0 · 你的任务 ############\n'+TASK[key]+'\n\n'+STATUS+'\n\n'+LEMMA+'\n\n'+FACT+'\n',
    '############ PART 1 · 主席 R032 任务包（原文）############\n'+CH, EXTRA[key],
    FMT.format(n=n,seat=seat)+'===== END =====\n']
    txt='\n'.join(x for x in p if x); fn=f'pkg/send_032_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode()))
