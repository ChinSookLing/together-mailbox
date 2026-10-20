import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
rul=open('chair/2026-10-20T1120-chair-ruling-R023-and-R024-text-via-Tuzi.txt',encoding='utf8').read()
r=rul[rul.index('PT-008 · Round 024 · The Guarantee Gap\n\nFROM'):rul.index('ROUND 024 OPEN')+len('ROUND 024 OPEN')]
ruling=rul[rul.index('PT-008 · Round 023 · 主席裁决'):rul.index('五、Round 024')]
note=rul[rul.index('六、Hesper 归档指令'):rul.index('Tuzi，這輪')]
common=r[:r.index('Track A —')]+r[r.index('Additional Question'):]
def tr(name):
    a=r.index(name); nxt=[r.find(x,a+5) for x in ('Track A —','Track B —','Track C —','Track D —','Additional Question')]
    return r[a:min(x for x in nxt if x>a)]
D='/workspace/work/pt008r23/replies/'
rd=lambda p:open(D+p,encoding='utf8').read()
opus=rd('2026-10-20T1100-reply-Opus-R023.txt')
qwen=rd('2026-10-20T1100-reply-Qwen-R023-part1of3.txt')+'\n\n[Hesper: 第 2 段接续]\n\n'+rd('2026-10-20T1100-reply-Qwen-R023-part2of3.txt')+'\n\n[Hesper: 第 3 段 = 主席采用的替代修正版]\n\n'+rd('2026-10-20T1108-reply-Qwen-R023-part3of3-ALT.txt')
argon=rd('2026-10-20T1109-reply-Argon-R023.txt'); ds=rd('2026-10-20T1109-reply-DeepSeek-R023.txt')
HN={'A':'Hesper 注：主席裁定 SPC 与 Qwen 区间证书是「同一类有理速度安全集表示」，但未证明等价；须写明共同周期要求、断点数、更新复杂度，并区分 (A) 表示 /(B) 更新 /(C) 保证。Hesper 事实：κ(V1)=1/5 @1/5，κ(V2)=9/31 @9/31，κ(V3)=1/3 @31/90 已确认；|B| 计数 14/48/152 未核。Qwen（三段，第 3 段为主席采用版）、Argon、DeepSeek 的 R023 原文附后。',
'B':'Hesper 注：用你的替代第 3 段（主席已采用）。主席要求正式记录两处勘误：δ=1/6 时 V2 在 t=1/4 附近的安全区间不对称（左端 1/4−1/108 由速度 9 卡住，右端 1/4+1/90 由速度 30 卡住）；K≤2Σv_i 只在共同周期 P=1 时成立，一般为 2P·Σv_i。原版「u=5/48 击穿全族」已 DISPROVED（t=9/5、t=8/5 存活）。Opus R023 原文（SPC）附后。',
'C':'Hesper 注（只做一项，回复宜短 ≤1500 字）：从 Track A 或 B 选一个精确的「非空保证」断言，给一个可手算反例；断言若对所有局外人量化，须逐一检查全部局外人。提交前核对 ANSWER BLOCK 与正文一致。主席 R023 裁定：你 R023 的反例只成立于固定局外人 a；V2 选 u=9 时交集 [16/45, 9/25] 非空（t=16/45 距离 16/45,13/45,1/5,1/3），「全部局外人失败」不成立；你笼统的 PROOF VERIFIED 不计为审阅。Opus、Qwen（三段，第 3 段为主席采用版）R023 原文附后。',
'D':'Hesper 注：从 CRL 出发。主席要求四项分开写：引理有效性 / 假设是否可得 / 有效可计算性 / 是否推进普遍 n→n+1。Hesper 事实：你 R023 例子「(1,2,3,4)，t0=1/8」中 t0 不是 (1,2,3,4) 的成功点（速度 1 在 1/8）；若指 W=(2,3,4)、n=4 则一致——请更正。主席：你的 H1–H3 审阅计一份非作者 VERIFIED；CORE 只在已核对量词范围内计。你自己、Opus、Qwen（第 3 段为主席采用版）的 R023 原文附后。'}
TRACK={'A':('Opus','1/4','Track A — Opus: A Guaranteed Certificate?','Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取'),
'B':('Qwen','2/4','Track B — Qwen: Interval Regeneration','Qwen 新对话「PT-008 Qwen R024」（Play CF 项目，3.8-Max thinking，web 关）'),
'C':('Argon','3/4','Track C — Argon: One Adversarial Obstruction','Gemini 新对话「PT-008 Argon R024」（3.1 Pro，High，Personal Intelligence 关）'),
'D':('DeepSeek','4/4','Track D — DeepSeek: Regenerative Guarantee Lemma','DeepSeek 新对话「PT-008 DeepSeek R024」（深度思考开，联网关）')}
ATT={'A':[('你自己的 R023 原文（原样）',opus),('Qwen R023 原文（三段，第 3 段为替代修正版，原样）',qwen),('Argon R023 原文（原样；主席裁定其结论只限固定局外人 a）',argon),('DeepSeek R023 原文（CRL，原样）',ds)],
'B':[('你自己的 R023 原文（第 1、2 段 + 替代第 3 段，原样）',qwen),('Opus R023 原文（SPC，原样）',opus)],
'C':[('Opus R023 原文（SPC，原样）',opus),('Qwen R023 原文（区间证书，第 3 段为替代修正版，原样）',qwen)],
'D':[('你自己的 R023 原文（CRL，原样）',ds),('Opus R023 原文（SPC，原样）',opus),('Qwen R023 原文（第 3 段为替代修正版，原样）',qwen)]}
FMT='''############ 回复格式 ############
第一行写「R024 {n} {seat}」。先写 ANSWER BLOCK（≤300 中文字）。四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / IDEA / UNFINISHED / PARTIAL。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED，并写出逐项论证（笼统 VERIFIED 不计数）。
对你提出的每个证书逐项回答主席六问（YES / CONDITIONAL / NO / UNFINISHED）：1 Finite representation? 2 Effective update? 3 Guaranteed nonempty output? 4 Deterministic safe-time selection? 5 Applicable to arbitrary real speeds? 6 Automatically preserved under induction?
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。不得由 (A) 表示或 (B) 更新推出 (C) 保证。不要假设无理速度有有限共同周期。随机测试不能推出证明。不做大规模穷举。
'''
for key,(seat,n,tname,where) in TRACK.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 024 · The Guarantee Gap · {tname}
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R024 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 024 · The Guarantee Gap, for {seat}.
TO: {seat}
ASK: do YOUR track (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: (C) GUARANTEE — after adding a speed and lowering the threshold to 1/(n+1), the updated safety set is provably nonempty and a safe time is selected by a proven finite operation; this is the step needed to reach F_47. Unrestricted F5 and general F_n still UNFINISHED.
''','############ PART 0 · 你的任务（主席原文）############\n'+tr(tname)+'\n'+HN[key]+'\n',
    '############ PART 1 · 主席 R024 共同要求（原文）############\n'+common,
    '############ R023 主席裁决（原文，节选至 R024 开题前）############\n'+ruling+'\n'+note]
    for i,(h,t) in enumerate(ATT[key],2): p.append(f'############ PART {i} · {h} ############\n'+t)
    p.append(FMT.format(n=n,seat=seat)+'===== END =====\n')
    txt='\n'.join(p); fn=f'pkg/send_024_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode())[:16])
