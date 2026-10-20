import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
rul=open('chair/2026-10-20T1048-chair-ruling-R022-and-R023-text-via-Tuzi.txt',encoding='utf8').read()
r21=rul[rul.index('PT-008 · Round 023 · The Regenerative Invariant\n\nFROM'):rul.index('ROUND 023 OPEN')+len('ROUND 023 OPEN')]
ruling=rul[:rul.index('四、Round 023')]
note=rul[rul.index('五、给 Hesper 的归档指令'):rul.index('Tuzi，我们已经')]
common=r21[:r21.index('Track A —')]+r21[r21.index('Common Test Cases'):]
def tr(name):
    a=r21.index(name); nxt=[r21.find(x,a+5) for x in ('Track A —','Track B —','Track C —','Track D —','Common Test Cases')]
    return r21[a:min(x for x in nxt if x>a)]
D='/workspace/work/pt008r22/replies/'
rd=lambda p:open(p,encoding='utf8').read()
opus=rd(D+'2026-10-20T1016-reply-Opus-R022.txt')
qwen=rd(D+'2026-10-20T1020-reply-Qwen-R022-part1of3.txt')+'\n\n[Hesper: 第 2 段接续]\n\n'+rd(D+'2026-10-20T1020-reply-Qwen-R022-part2of3.txt')+'\n\n[Hesper: 第 3 段接续]\n\n'+rd(D+'2026-10-20T1020-reply-Qwen-R022-part3of3.txt')
argon=rd(D+'2026-10-20T1026-reply-Argon-R022.txt'); ds=rd(D+'2026-10-20T1028-reply-DeepSeek-R022.txt')
HN={'A':'Hesper 注：主席要求重写 N、TF、CORE 的正式陈述，特别写清 CORE 的量词（对所有选择规则 F？所有局外人？所有相位格？还是固定有限规则族？），只证实际支持的最强版本。主席提醒：结构核 C_n 是相对于所定义传递规则的障碍，不是「无安全时间」；1,689/11/1,678 分类目前只是你的报告，Hesper 未独立重算。Hesper 事实：V₂=(1,2,9,30) 不在 C_4（t=1/4 距离 1/4,1/2,1/4,1/2，且任一局外人去掉后其余三者 ≥1/4）。Qwen、Argon、DeepSeek 的 R022 原文附后。',
'B':'Hesper 注：主席要求从 Q-GATE 与 Q-FSR 出发，测试「保留多个安全时间」能否装入局外人；家族须可在无界搜索之外生成，并在 V₁=(1,3,4,7)、V₂=(1,2,9,30) 上测试。不要假设无理速度的安全集是周期的。Hesper 事实：(1,3,4,7) 在 1/5 下安全集只有孤立点 {1/5,2/5,3/5,4/5}；(1,2,9,30) 的 T4 四个局外人相位为 2/11、49/60、3/40、5/6，但 t=1/4 成功。你 R022 的「E*_n 全是假象」用的是「无安全时间才算结构障碍」的定义；主席已裁：结构核是相对传递规则的障碍。Opus、Argon 的 R022 原文附后。',
'C':'Hesper 注（只做一项，回复宜短 ≤1500 字）：选一个已完整陈述的不变量或再生规则（例如 Opus 的 I_old / I_new / 双门槛不变量，或 DeepSeek 的受控间隔族），对其全称断言给一个可手算的反例；结论只能落在主席列的前三类之一（某个选择器失败／某有限类全部失败／某数学不变量失败），不得推到「不存在显式公式」。注意：你 R022 ANSWER BLOCK 中的数字（1/8, 2/33, 1/35, 6/11；R={4,5,6,7}, G=8, 40/3）与你的正文不符，主席裁定以正文为准（2/11, 49/60, 3/40, 5/6；R={2,9}, G=7, 35/3），请勿沿用错误数字。Opus、DeepSeek 的 R022 原文附后。',
'D':'Hesper 注：主席要求独立复审 Opus R022 新版 H1–H3（你 R022 审的是 R021 旧版 H）以及 CORE 的量词；左移时保留严格正时间条件。你的条件再生引理须按主席七项（输入证书、门槛、选时规则、存在性证明、间隔或复杂度界、再生条件、是否自动保持）逐项写出。Opus R022 原文（含 H1–H3、N、TF、CORE）附后（PART 2）。'}
TRACK={'A':('Opus','1/4','Track A — Opus: Define the Invariant','Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取'),
'B':('Qwen','2/4','Track B — Qwen: Alternative Safe-Time Families','Qwen 新对话「PT-008 Qwen R023」（Play CF 项目，3.8-Max thinking，web 关）'),
'C':('Argon','3/4','Track C — Argon: One Rigorous Obstruction','Gemini 新对话「PT-008 Argon R023」（3.1 Pro，High，Personal Intelligence 关）'),
'D':('DeepSeek','4/4','Track D — DeepSeek: Conditional Regeneration Lemma','DeepSeek 新对话「PT-008 DeepSeek R023」（深度思考开，联网关）')}
ATT={'A':[('你自己的 R022 原文（原样）',opus),('Qwen R022 原文（三段，原样）',qwen),('Argon R022 原文（原样）',argon),('DeepSeek R022 原文（含 H/FO/TL/OB 审阅，原样）',ds)],
'B':[('你自己的 R022 原文（三段，原样）',qwen),('Opus R022 原文（原样）',opus),('Argon R022 原文（原样）',argon)],
'C':[('Opus R022 原文（I_old / I_new / 双门槛不变量 §5，原样）',opus),('DeepSeek R022 原文（受控间隔族，原样）',ds)],
'D':[('Opus R022 原文（H1–H3 / N / TF / CORE，原样）',opus),('你自己的 R022 原文（原样）',ds)]}
FMT='''############ 回复格式 ############
第一行写「R023 {n} {seat}」。先写 ANSWER BLOCK（≤300 中文字）。每项结果标 PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / UNFINISHED。四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / IDEA / UNFINISHED / PARTIAL。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED。
对你提出的不变量（或审阅对象）必须逐项回答主席五问：Is it explicitly finite? / Does it produce a safe time? / Is regeneration proved? / Does it apply to arbitrary real speeds? / Does it advance a uniform F_n? 无依据的写 UNFINISHED，不得估计。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。无界搜索不得当作封闭构造。随机测试不能推出证明。不做大规模穷举。
'''
for key,(seat,n,tname,where) in TRACK.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 023 · The Regenerative Invariant · {tname}
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R023 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 023 · The Regenerative Invariant, for {seat}.
TO: {seat}
ASK: do YOUR track (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: finite constructive data I_n(V) that yields a safe time and regenerates to I_(n+1) at threshold 1/(n+2) — the mechanism needed to reach F_47. Unrestricted F5 and general F_n still UNFINISHED.
''','############ PART 0 · 你的任务（主席原文）############\n'+tr(tname)+'\n'+HN[key]+'\n',
    '############ PART 1 · 主席 R023 共同要求（原文）############\n'+common,
    '############ R022 主席裁决（原文，节选至 R023 开题前）############\n'+ruling+'\n'+note]
    for i,(h,t) in enumerate(ATT[key],2): p.append(f'############ PART {i} · {h} ############\n'+t)
    p.append(FMT.format(n=n,seat=seat)+'===== END =====\n')
    txt='\n'.join(p); fn=f'pkg/send_023_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode())[:16])
