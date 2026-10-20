import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
rul=open('chair/2026-10-20T1529-chair-GPT6-R027-final-ruling-R028-open-via-Tuzi.txt',encoding='utf8').read()
L=rul[rul.index('PT-008 · R027 FINAL CHAIR LETTER'):rul.index('R028 OPEN.')+len('R028 OPEN.\n\n— GPT-6\nChair · PT-008 Time Forge')]
ruling=L[:L.index('2. ROUND 028')]
r2=L[L.index('2. ROUND 028'):]
common=r2[:r2.index('Track A —')]+r2[r2.index('3. UNIVERSAL FORMULA TEST'):]
def tr(name):
    a=r2.index(name); nxt=[r2.find(x,a+5) for x in ('Track A —','Track B —','Track C —','Track D —','3. UNIVERSAL FORMULA TEST')]
    return r2[a:min(x for x in nxt if x>a)]
D='/workspace/work/pt008r27/replies/'
rd=lambda p:open(D+p,encoding='utf8').read()
opus=rd('2026-10-20T1500-reply-Opus-R027.txt'); qwen=rd('2026-10-20T1510-reply-Qwen-R027-full-complete.txt')
kimi=rd('2026-10-20T1452-reply-Kimi-R027.txt'); kimis=rd('2026-10-20T1521-reply-Kimi-R027-supplement-FWS.txt'); ds=rd('2026-10-20T1505-reply-DeepSeek-R027.txt')
t4=open('/workspace/work/pt008r20/hesper/base.py').read(); t4=t4[t4.index('def F3'):t4.index('A=lambda')]
T4='已认证 T4（PT-008 内部 PROVED，2026-10-18，八段，Opus 作者）的分支，以 Hesper 存档的精确代码形式抄录（q=1/4，nd=到最近整数距离，fr=小数部分；分支按顺序先命中先用）：\n'+t4
FACT='Hesper 事实（精确分数，CHECKED，不是证明）：用附后「T4 原式」代码对全部整数三元组 1≤a<b<c≤40（9,880 组）逐一计算：T4 输出全部安全（min≥1/4），且全部满足 0<t<1/a；各分支组数 B1 c≤3a 4472、B2 c≥3b 1014、B3 b≥3a 2955、B4 3/(b+c) 235、B5 2/(b+c) 848、B6 4/(b+c) 231、B7 5/(b+c) 86、B8 3/(a+c) 39，t≥1/a 均为 0。这只是有限整数范围，不代替逐分支证明，也不覆盖实数速度。'
HN={'A':FACT+' 主席另要 FWS(i)/(ii) 完整文本供 DeepSeek 第二次审阅。你的 R027 原文、Kimi 补充审阅原文附后。',
'B':FACT+' 主席 R027 裁决：你 §5.2「任意实数无普适有限界」为 UNSUPPORTED，保持 UNFINISHED，不作已证不可能。你的 R027 原文、Opus R027 原文附后。',
'C':FACT+' 请独立手证或反证 FW₃；数值扫描不能作证明。Opus R028 的 FW₃ 论证若送到，Hesper 会作补充件转给你。Opus R027 原文、你的 R027 补充审阅原文附后。回复宜 ≤1500 字。',
'D':'Hesper 注：你的主任务是 FWS(i)/(ii) 的第二份非作者审阅（Kimi 已交第一份，原文附后，请独立论证、勿照抄），然后研究 FWₖ ⇒ FWₖ₊₁。Opus R027 §4.2–§4.4 原文（FW/FWS）在附后的 Opus R027 原文中；Opus R028 若交更完整的 FWS 文本，以后续补充件为准。'+FACT+' 你的 R027 原文附后。'}
TRACK={'A':('Opus','1/4','Track A — Opus','Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取'),
'B':('Qwen','2/4','Track B — Qwen','Qwen 新对话「PT-008 Qwen R028」（Play CF 项目，3.8-Max thinking，web 关）'),
'C':('Kimi','3/4','Track C — Kimi','Kimi 新对话「PT-008 Kimi R028」（思考模式开，联网关）'),
'D':('DeepSeek','4/4','Track D — DeepSeek','DeepSeek 新对话「PT-008 DeepSeek R028」（深度思考开，联网关）')}
ATT={'A':[('你自己的 R027 原文（原样）',opus),('Kimi R027 补充审阅原文（审你的 FW_2/FWS，原样）',kimis)],
'B':[('你自己的 R027 原文（三段合并，原样）',qwen),('Opus R027 原文（原样）',opus)],
'C':[('Opus R027 原文（含 FW/FWS，原样）',opus),('你自己的 R027 补充审阅原文（原样）',kimis)],
'D':[('Opus R027 原文（含 FW/FWS，原样）',opus),('Kimi R027 补充审阅原文（FWS 第一份审阅，原样）',kimis),('你自己的 R027 原文（原样）',ds)]}
FMT='''############ 回复格式 ############
第一行写「R028 {n} {seat}」。先写 ANSWER BLOCK（≤300 中文字）。然后回答主席 UNIVERSAL FORMULA TEST：YES / CONDITIONAL / NO / UNFINISHED 选一，并逐条说明是否提供：1. Existence within a bounded horizon；2. A finite candidate family；3. A guaranteed finite selector；4. A direct formula without trial enumeration；5. An induction rule that automatically preserves its hypotheses。五项不得视为等价。四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / UNFINISHED。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED，并写出逐项论证（笼统 VERIFIED 不计数）。失败尝试与反例也要报告。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。不得从「某处存在成功时间」推出 FW₃。不要假设无理速度有有限共同周期。随机测试不能推出证明。不做大规模穷举。
'''
for key,(seat,n,tname,where) in TRACK.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 028 · The First Window Test · {tname}
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R028 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 028 · The First Window Test, for {seat}.
TO: {seat}
ASK: do YOUR track (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: prove or disprove FW₃ (a safe four-runner time inside the first window 0<t<1/v_min), and test whether First Window gives a finite horizon that propagates level to level toward F_47. A bounded search is not the direct formula; general F_n still UNFINISHED.
''','############ PART 0 · 你的任务（主席原文）############\n'+tr(tname)+'\n'+HN[key]+'\n',
    '############ PART 1 · 主席 R028 共同要求（原文）############\n'+common,
    '############ R027 主席最终裁决（原文）############\n'+ruling,
    '############ T4 原式（已认证）############\n'+T4]
    for i,(h,t) in enumerate(ATT[key],2): p.append(f'############ PART {i} · {h} ############\n'+t)
    p.append(FMT.format(n=n,seat=seat)+'===== END =====\n')
    txt='\n'.join(p); fn=f'pkg/send_028_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode())[:16])
