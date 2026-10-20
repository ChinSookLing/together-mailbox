import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
ch=open('chair/2026-10-21T0745-chair-R031-followup-verbatim.txt',encoding='utf8').read()
CH=ch[ch.index('TO：Hesper'):]
op21=open('/workspace/work/pt008r21/replies/2026-10-20T0939-reply-Opus-R021.txt',encoding='utf8').read().split('\n')
PS='\n'.join(op21[27:61])
op25=open('/workspace/work/pt008r25/replies/2026-10-20T1217-reply-Opus-R025.txt',encoding='utf8').read()
SPC=op25[op25.index('## I-1 SPC'):op25.index('## I-2 EQ')]
GLC=op25[op25.index('## I-4 GLC'):op25.index('**局限**：在 R024')]
OP30=open('/workspace/work/pt008r30/replies/2026-10-21T0708-reply-Opus-R030.txt',encoding='utf8').read()
CERT=open('hesper/fwcert.py',encoding='utf8').read()
DEP=('A1/DEC/UPD 所依赖命题的准确版本与审阅状态（Hesper 从已归档原文逐字抄录）：\n'
 '• PS_n：Opus R021 §1（原文 sha 见 mailbox round-021）。状态：R021 主席裁决「多方 PROOF VERIFIED；待主席核对完整陈述后正式认证」；R022 裁决「已收到完整原文的报告；主席审阅待办」。未见主席正式认证。注意 PS_n 原假设 (H4) t₀=F_n(W)，W 的安全度 1/n > δ；A1 改用 t₀∈S_δ(V)（同一门槛 δ），证明第 1 步只需 ‖wt₀‖≥δ。\n'
 '• GLC：Opus R025 I-4。状态：R025 主席裁决「应在完整证明审阅后再决定认证范围」。\n'
 '• SPC（含 O3 THRESHOLD）：Opus R025 I-1。状态：R025 主席裁决「Opus · SPC 表示及更新：PROOF CANDIDATE；部分获独立审阅」。\n'
 '• 主席区间公式 t_*：R030 主席转向信；R030 Kimi 非作者审阅 PROOF VERIFIED（主席未裁决）。\n\n'
 '----- PS_n 原文（Opus R021 §1）-----\n'+PS+'\n\n----- GLC 原文（Opus R025 I-4）-----\n'+GLC+'\n----- SPC 原文（Opus R025 I-1）-----\n'+SPC)
STATUS=('R030 记录（不升级）：FW₄、一般 F_n 均 UNFINISHED；无确认新全域覆盖；无确认 FW₄ 反例。R030 原文 sha：Opus c6a3d758；DeepSeek 第一版 f229982a、第二版 a68eb16e；Qwen 三段 43862566/e862f8b8/f3478459；Kimi 65ff7cd8。主席未发 R030 结案裁决；本轮按主席后续任务信开题，登记为 R031。')
LEMMA='已认证可用引理（主席认证，可直接引用）：T4；FW₃；FW₂；FWS(i)（计重数）；FWS(ii)（FW_k ⇒ F^FW 安全，前提不得移除）；CNT k(σ+1)/2。'
FACT=('Hesper 事实（精确分数，CHECKED，不是证明）：\n'
 '(1) 主席第四节首窗证书，Hesper 精确实现（代码附于 Kimi 包）：全部整数四元组 1≤a<b<c<d≤24 共 10,626 组，每组都得到首窗见证（0<t<1/a，四距离 ≥1/5），0 组无见证；2,999 组随机有理四元组，0 组无见证。\n'
 '(2) 周期问题：Opus DEC 对 V=(1,2,3)、t₀=1/5、δ=1/5，路径 (a) 19,649 个随机非整数有理 u 中，7,831 个需要 j≥1，输出 t=1/5+j≥6/5，超出首窗 (0,1)。即 DEC 的 (a) 路径给出的是正时间见证，不一定是首窗见证。\n'
 '(3) R030：DEC 对 (1,2,3) 按文字实现，20,000 个随机 u 零失败（只验安全，不验首窗）。\n'
 '这些只是有限检查，不代替证明。')
LEDGER='每项成果分别登记七栏：1 数学有效性及审阅状态；2 对统一构造的具体推进；3 是否保证非空；4 是否处理任意实数速度；5 是否保证有限提取；6 是否满足直接构造目标；7 是否能随人数推广。'
TASK={'A':'你的任务（主席第二节）：路线 A 主攻。交付重点：有限例外见证的一般定理，或明确的再生条件及其证明。必须分别回答主席第二节五问（正时间见证？首窗见证？有限共振例外是否全有见证？证书能否下一层再生？可公度/不可公度各处理到哪里？），并核明周期问题（P≥1/a，t₀+P 越出首窗）下 DEC 的实际结论。DeepSeek 本轮会逐步审你的 A1/DEC/UPD。',
'D':'你的任务（主席第二节）：逐步审阅 Opus R030 的 A1／DEC／UPD（原文附于 PART 2）。标明循环、缺失假设、边界或有效结论；不要独立另写一套讨论。必须分别回答主席第二节五问，并核明周期问题。主席说明：使用新门槛安全集合本身不构成循环；把「插入后非空」当作未证前提才构成循环。',
'B':'你的任务（主席第三节）：路线 B——提出明确的取整、代数或几何选择规则，并尝试证明或否证。规则必须给出：如何从输入直接产生输出；为何有限完成；全部适用假设；最弱未证步骤；什么反例能推翻它。不得用先知道安全时间的取整、无界枚举或未证优化器充当答案。若无新构造原理或结构性推进，请如实报告（主席：将暂停该整数架构，不宣布统一公式不可能）。主席另自交路线 B 推导，不在本包。',
'C':'你的任务（主席第四、五节）：优先独立审阅 (i) 第四节精确首窗证书（J=[1/(5a),4/(5a)]、分量判据、见证提取；含孤立点、端点等号、有理/实数计算模型的区分）；(ii) 第五节主席证明候选「FW₄ 反例有理化」（Lipschitz 界、ε<5γ/4、有序性保持、结论 A/B）。逐项给 PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED。之后可用证书攻击具体主张。Hesper 的精确实现附于 PART 2，可复用，不必重写。回复宜 ≤1500 字。'}
SEAT={'A':('Opus','1/4','Tuzi 的 claude.ai（Opus）对话'),
'D':('DeepSeek','2/4','DeepSeek 新对话「PT-008 DeepSeek R031」（深度思考开，联网关）'),
'B':('Qwen','3/4','Qwen 新对话「PT-008 Qwen R031」（Play CF 项目，thinking，web 关）'),
'C':('Kimi','4/4','Kimi 新对话「PT-008 Kimi R031」（思考模式开，联网关）')}
EXTRA={'A':'############ PART 2 · 所依赖命题原文与状态 ############\n'+DEP,
'D':'############ PART 2 · Opus R030 原文（sha c6a3d758…，逐字）############\n'+OP30+'\n\n############ PART 3 · 所依赖命题原文与状态 ############\n'+DEP,
'B':'',
'C':'############ PART 2 · Hesper 首窗证书精确实现（Python，Fraction；可复用）############\n'+CERT}
FMT='''############ 回复格式 ############
第一行写「R031 {n} {seat}」。先走短提案初筛（确切命题、新步骤、最弱假设、可否证方式），通过后再写完整证明。先写 ANSWER BLOCK（≤300 中文字）。正文分三类标注：FACT / PROOF / IDEA。必须写出「最不确定的一步」。'''+LEDGER+'''
状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / UNFINISHED；审阅结论每项单独给 PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED，并写逐项论证。失败尝试、更正与反例也要报告。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。数值扫描只记 CHECKED。截短候选列表失败、随机搜索失败都不是反例。不要假设无理速度有有限共同周期。不要重启「十个短想法」流程。
'''
out=[]
for key,(seat,n,where) in SEAT.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 031 · R030 后续：双路线推进与精确首窗证书
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R031 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 031 · follow-up to R030, for {seat}.
TO: {seat}
ASK: do YOUR task (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: method check after R030 — route A (full safe set, finite certificate, regeneration) and route B (direct global construction); the exact first-window certificate is a shared test tool. General F_n still UNFINISHED. Goal: One formula for all, and all in one formula.
''','############ PART 0 · 你的任务 ############\n'+TASK[key]+'\n\n'+STATUS+'\n\n'+LEMMA+'\n\n'+FACT+'\n',
    '############ PART 1 · 主席 R031 任务信（原文）############\n'+CH, EXTRA[key],
    FMT.format(n=n,seat=seat)+'===== END =====\n']
    txt='\n'.join(x for x in p if x); fn=f'pkg/send_031_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode()))
