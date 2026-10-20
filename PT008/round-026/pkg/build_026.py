import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
rul=open('chair/2026-10-20T1240-chair-ruling-R025-and-R026-text-via-Tuzi.txt',encoding='utf8').read()
r=rul[rul.index('PT-008 · Round 026 · The Arithmetic Skeleton\n\nFROM'):rul.index('ROUND 026 OPEN')+len('ROUND 026 OPEN')]
ruling=rul[rul.index('PT-008 · Round 025 · 主席正式裁决'):rul.index('五、Round 026')]
note=rul[rul.index('六、Hesper 的正式归档指令'):rul.index('Tuzi，我觉得')]
common=r[:r.index('Track A —')]+r[r.index('Mandatory Distinctions'):]
def tr(name):
    a=r.index(name); nxt=[r.find(x,a+5) for x in ('Track A —','Track B —','Track C —','Track D —','Mandatory Distinctions')]
    return r[a:min(x for x in nxt if x>a)]
D='/workspace/work/pt008r25/replies/'
rd=lambda p:open(D+p,encoding='utf8').read()
opus=rd('2026-10-20T1217-reply-Opus-R025.txt'); qwen=rd('2026-10-20T1224-reply-Qwen-R025-full.txt')
kimi=rd('2026-10-20T1225-reply-Kimi-R025.txt'); ds=rd('2026-10-20T1226-reply-DeepSeek-R025.txt')
HF='Hesper 事实（精确分数，仅核对，非证明）：'
HN={'A':HF+'你 R025 的 MZ (2,3)@t=1/5 测度 1/9、EQ′ t=19/42 与密度 5/36、8/63、连续块测度 3/25、23/150、ACC 候选数 20/77/321 对上界 30/84/342、ACC 输出=SPC、LM 抽查 V1/V2/V3/(1..5) 局部极大点 6/18/60/5 个全在 C(V)——均已确认。你自报的 4,667 点、123 组比对未经核对。主席已亲证 MZ-ZERO（PROVED）；LM/HS/ACC 仍为 PROOF CANDIDATE。Kimi 本轮将只审你的 HS，DeepSeek 审 LM 与 ACC——请把三条定理写成可独立审阅的完整版本（HS 的完整陈述会转给 Kimi）。Qwen、Kimi、DeepSeek R025 原文附后。',
'B':HF+'你 R025 六区间、总测度 8/63、TR 下界 1/105 已确认。主席已接受两处勘误：t=13/24 时 ‖t‖=11/24；t=23/42 时 ‖t‖=19/42。另：u-安全弧数应为 uP′（你写 uP′+1）。主席裁决：单门槛区间表不足以精确降门槛（EQ′ 反例），更新算法必须写明额外输入（原始速度或完整断点/相位资料 B_V）。Opus R025 原文（含 LM/HS/ACC）附后。',
'C':'Hesper 注：本轮 Track C 仍由你担任（主席建议续任一轮），只审一条定理：Opus 的 HS（hitting skeleton）。HS 完整陈述在附后的 Opus R025 原文 Part II；若 Opus R026 给出更新版本，以主席后续转交为准，本包以 R025 原文为审阅对象，请注明所审版本。给完整证明或具体反例；不得由条件性的命中性质推出无条件存在。你 R025 的 MZ 审阅已被主席计为一份非作者 PROOF VERIFIED。回复宜 ≤1500 字。',
'D':HF+'你 R025 的更正数字（g=1/5、g′=1/3、间隔 13/72、1/6、13/72、绕回 1/3）已确认。注意：g(S) 第一条公式误把分量长度放入 max，下一句的纯间隔定义才正确。主席：GBR 修正版 PROOF CANDIDATE，作者自审不计独立审阅。本轮主任务：独立审 Opus 的 LM 与 ACC（Opus R025 原文附后）；GBR 只在有余力时处理。你自己的 R025 原文附后。'}
TRACK={'A':('Opus','1/4','Track A — Opus: LM, HS and ACC','Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取'),
'B':('Qwen','2/4','Track B — Qwen: Exact Certificate Update','Qwen 新对话「PT-008 Qwen R026」（Play CF 项目，3.8-Max thinking，web 关）'),
'C':('Kimi','3/4','Track C — Kimi: Independent HS Audit','Kimi 新对话「PT-008 Kimi R026」（思考模式开，联网关）'),
'D':('DeepSeek','4/4','Track D — DeepSeek: Independent LM and ACC Audit','DeepSeek 新对话「PT-008 DeepSeek R026」（深度思考开，联网关）')}
ATT={'A':[('你自己的 R025 原文（原样）',opus),('Qwen R025 原文（三段合并，原样）',qwen),('Kimi R025 Track C 原文（MZ 审阅，原样）',kimi),('DeepSeek R025 原文（原样）',ds)],
'B':[('你自己的 R025 原文（三段合并，原样）',qwen),('Opus R025 原文（含 LM/HS/ACC，原样）',opus)],
'C':[('Opus R025 原文（含 HS 完整陈述，原样）',opus),('你自己的 R025 原文（原样）',kimi)],
'D':[('Opus R025 原文（含 LM/ACC，原样）',opus),('你自己的 R025 原文（原样）',ds)]}
FMT='''############ 回复格式 ############
第一行写「R026 {n} {seat}」{extra}。先写 ANSWER BLOCK（≤300 中文字）。四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / UNFINISHED。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED，并写出逐项论证（笼统 VERIFIED 不计数）。
主席强制区分，分别报告：(A) 候选骨架存在；(B) 骨架覆盖每个已存在的安全分量；(C) 对任意输入骨架含成功候选；(D) 成功候选可由保证有限的操作选出。(B) 不推出 (C)；(C) 不推出直接公式，除非 (D) 也成立。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。不得用已知存在性定理代替显式构造。不要假设无理速度有有限共同周期。随机测试不能推出证明。不做大规模穷举。
'''
for key,(seat,n,tname,where) in TRACK.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 026 · The Arithmetic Skeleton · {tname}
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R026 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 026 · The Arithmetic Skeleton, for {seat}.
TO: {seat}
ASK: do YOUR track (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: decide whether the candidate skeleton (LM/HS/ACC) is reliable — covers every safe component, intervals and isolated points alike — and whether it admits a genuine n→(n+1) update and a guaranteed finite selection of a successful candidate, the step needed to reach F_47. Unrestricted F5 and general F_n still UNFINISHED.
''','############ PART 0 · 你的任务（主席原文）############\n'+tr(tname)+'\n'+HN[key]+'\n',
    '############ PART 1 · 主席 R026 共同要求（原文）############\n'+common,
    '############ R025 主席裁决（原文，节选至 R026 开题前）############\n'+ruling+'\n'+note]
    for i,(h,t) in enumerate(ATT[key],2): p.append(f'############ PART {i} · {h} ############\n'+t)
    p.append(FMT.format(n=n,seat=seat,extra='（Track C）' if key=='C' else '')+'===== END =====\n')
    txt='\n'.join(p); fn=f'pkg/send_026_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode())[:16])
