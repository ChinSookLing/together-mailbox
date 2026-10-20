import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
ch=open('chair/2026-10-20T1729-chair-GPT6-R029-open-FW4-via-Tuzi.txt',encoding='utf8').read()
CH=ch[ch.index('TO：Hesper'):]
r28=open('/workspace/work/pt008r28/chair/2026-10-20T1618-chair-GPT6-R028-final-ruling-CLOSED.txt',encoding='utf8').read()
pub=open('/workspace/work/pt008r28/up7/round-028/publish/R028-PUBLICATION.md',encoding='utf8').read()
t4=open('/workspace/work/pt008r20/hesper/base.py').read(); t4=t4[t4.index('def F3'):t4.index('A=lambda')]
T4='已认证 T4（PT-008 内部 PROVED，2026-10-18，八段，Opus 作者；手稿 sha256 4720413d）的分支，以 Hesper 存档的精确代码形式抄录（q=1/4，nd=到最近整数距离，fr=小数部分；分支按顺序先命中先用）：\n'+t4
FACT=('Hesper 事实（精确分数，CHECKED，不是证明）：(1) 主席第二节算例全部复核一致：T4(1,2,3)=1/4；ρ=1/60；J=[7/30,4/15]；4J=[14/15,16/15]，端点处 ‖4t‖=1/15；t=1/5 时四个距离为 1/5、2/5、2/5、1/5。'
 '(2) 剩余区域 d>4a、c<d<4c 内全部整数四元组 1≤a<b<c<d≤24（5,890 组）：以边界点 t=(j±1/5)/v 为候选，每组都在首窗 0<t<1/a 内找到 min‖vt‖≥1/5 的时间，无一例外。这只是有限整数范围，不代替实数证明，也不是反例搜索的结论。')
LEMMA='已认证可用引理（主席认证，可直接引用）：T4（四跑者显式构造，安全度 1/4）；FW₃（T4 输出满足 a·t<11/12）；FW₂；FWS(i)（计重数）；FWS(ii)（FW_k ⇒ F^FW 安全，前提不得移除）；CNT k(σ+1)/2。FW-FO 只有一份非作者核验，未认证。'
TASK={'A':'你的任务（主席第三节）：攻击剩余区域 d>4a、c<d<4c 的手证；明确指出使用了哪些已认证引理。',
'B':'你的任务（主席第三节）：独立寻找构造，优先检验不同三速度子集能否互补。',
'C':'你的任务（主席第三节）：审阅主席第一、二节两项推导（d≤4a 取 1/(5a)；d≥4c 由 T4+FW₃+Lipschitz；单个标准小窗口失败的例子），并检查构造中的等号、孤立安全点与首窗边界。若 Opus/Qwen 的构造送到，Hesper 会作补充件转给你。回复宜 ≤1500 字。',
'D':'你的任务（主席第三节）：寻找可随 k 延伸的结构；若只能覆盖附加条件，明确写出条件。',
'E':'你的任务（主席第三节）：在剩余区域 d>4a、c<d<4c 寻找精确反例。反例必须证明整个首窗 (0,1/a) 内无 min‖vt‖≥1/5 的时间，不能只证明某个选择器失败。上面的 Hesper 整数扫描（≤24）未找到反例，请勿重复同一范围。'}
SEAT={'A':('Opus','1/5','Tuzi 的 claude.ai（Opus）对话'),
'B':('Qwen','2/5','Qwen 新对话「PT-008 Qwen R029」（Play CF 项目，thinking，web 关）'),
'C':('Kimi','3/5','Kimi 新对话「PT-008 Kimi R029」（思考模式开，联网关）'),
'D':('DeepSeek','4/5','DeepSeek 新对话「PT-008 DeepSeek R029」（深度思考开，联网关）'),
'E':('Argon','5/5','Argon 新对话「PT-008 Argon R029」（web 关）')}
FMT='''############ 回复格式 ############
第一行写「R029 {n} {seat}」。先写 ANSWER BLOCK（≤300 中文字）：FW₄ 的状态（PROVED 候选 / DISPROVED 候选 / UNFINISHED）以及你严格缩小的剩余区域（若有）。正文分三类标注：FACT / PROOF / IDEA。必须写出「最不确定的一步」。四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / UNFINISHED；审阅结论每项单独给 PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED，并写逐项论证。失败尝试与反例也要报告。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。数值扫描只记 CHECKED。不要假设无理速度有有限共同周期。单个选择器或单个小窗口失败不是 FW₄ 的反例。不做大规模穷举。
'''
for key,(seat,n,where) in SEAT.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 029 · FW₄：攻剩余区域
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R029 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 029 · FW₄, for {seat}.
TO: {seat}
ASK: do YOUR task (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: FW₄ — for every real 0<a<b<c<d, a time 0<t<1/a with min‖vt‖≥1/5 — the next level of the first-window chain toward one deterministic F_n for n=2..47. A bounded search is not the direct formula; general F_n still UNFINISHED.
''','############ PART 0 · 你的任务 ############\n'+TASK[key]+'\n\n'+LEMMA+'\n\n'+FACT+'\n',
    '############ PART 1 · 主席 R029 任务书（原文）############\n'+CH,
    '############ PART 2 · R028 主席最终裁决（原文）############\n'+r28,
    '############ PART 3 · R028 公开记录（墙上原文，sha256 28a70c3c）############\n'+pub,
    '############ PART 4 · T4 原式（已认证）############\n'+T4,
    FMT.format(n=n,seat=seat)+'===== END =====\n']
    txt='\n'.join(p); fn=f'pkg/send_029_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode()))
