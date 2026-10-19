import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
rul=open('chair/2026-10-20T0656-chair-ruling-R020-and-R021-text-via-Tuzi.txt',encoding='utf8').read()
r21=rul[rul.index('PT-008 · Round 021 · The Induction Bridge\n\nFROM'):rul.index('ROUND 021 OPEN')+len('ROUND 021 OPEN')]
ruling=rul[:rul.index('四、Round 021')]
note=rul[rul.index('给 Hesper 的决定'):rul.index('Tuzi，我记得')]
common=r21[:r21.index('Track A —')]+r21[r21.index('Mandatory Final Question'):]
def tr(name):
    a=r21.index(name); nxt=[r21.find(x,a+5) for x in ('Track A —','Track B —','Track C —','Track D —','Mandatory Final Question')]
    return r21[a:min(x for x in nxt if x>a)]
D='/workspace/work/pt008r20/replies/'
rd=lambda p:open(p,encoding='utf8').read()
opus19=rd('/workspace/work/mb008/PT008/round-019/replies/2026-10-19T1919-reply-Opus-R019.txt')
opus20=rd(D+'2026-10-20T0619-reply-Opus-R020.txt')
qwen20=rd(D+'2026-10-20T0640-reply-Qwen-R020-part1of6.txt')+'\n\n[Hesper: 第二段接续]\n\n'+rd(D+'2026-10-20T0640-reply-Qwen-R020-part2.txt')
argon20=rd(D+'2026-10-20T0648-reply-Argon-R020.txt')
ds20=rd(D+'2026-10-20T0649-reply-DeepSeek-R020.txt')
HN={'A':'Hesper 注：主席要求你先提交 PS / LS / APS（及 PS*）的完整定理陈述与证明原文，供主席认证；请勿只写缩写。三位审阅人的 R020 原文附后（PART 3–5），供你回应其中的条件与限定。',
'B':'Hesper 注：主席要求先交 Q-GATE 连分数选择器的完整证明（分母上界的推导、对 b,c,d 三个旧约束的影响、a 是否安全）。若只得到三速安全簇、无法装入 a，明写 PARTIAL。另交 Q-ERC1 修订证明，并逐项回应 Opus（PART 3）与 Argon（PART 4）指出的具体缺口。注：Argon 提出的反例 (θ,w)=(1/3,4/3) 经 Hesper 精确复算是错的（k=1 时两距离都是 1/3，R1={1,2}），但它指出的鸽笼不等式 2+1≤3 问题仍需回应。',
'C':'Hesper 注（按主席指示，只做一项、回复宜短 ≤1500 字）：从 PART 2 选一条已提出的 F4→F5 转移规则（Qwen Q-GATE，或 Opus PS*），按其原文陈述测试。优先 a 远小于 b,c,d、有理相位共振、无理比值三类情形。不要把一个受限反例扩大成"所有构造都不可能"。上轮你的 Q-ERC1 反例 (1/3,4/3) 经精确复算不成立（R1={1,2}），请勿沿用。',
'D':'Hesper 注：PART 2 为 Qwen R020 原文（含 Q-GATE 与重写的 Q-ERC1，作为独立审阅对象）；PART 3 为 Opus R020 原文（含 PS*，供归纳不变量参考）。你上轮判 Q-ERC1 为 PROOF VERIFIED，而 Opus、Argon 判 GAP FOUND——本轮请审 Qwen 的新证明，并具体回答 Opus 指出的缺口（集合投影、|A_q|≥3q/5 在 q=7 时不成立、小 g 鸽笼）是否已补上。'}
TRACK={'A':('Opus','1/4','Track A — Opus: Induction Transfer','Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取'),
'B':('Qwen','2/4','Track B — Qwen: F4-to-F5 Gate','Qwen 新对话「PT-008 Qwen R021」（Play CF 项目，3.8-Max thinking，web 关）'),
'C':('Argon','3/4','Track C — Argon: One Counterexample Mission','Gemini 新对话「PT-008 Argon R021」（3.1 Pro，High，Personal Intelligence 关）'),
'D':('DeepSeek','4/4','Track D — DeepSeek: Missing Induction Invariant','DeepSeek 新对话「PT-008 DeepSeek R021」（深度思考开，联网关）')}
ATT={'A':[('Opus R019 原文（PS / LS / APS 初版，原样）',opus19),('Qwen R020 原文（审阅 LS/PS/APS 部分在内，原样）',qwen20),('Argon R020 原文（对 PS/LS 的对抗审阅，原样）',argon20),('DeepSeek R020 原文（审阅 PS/APS/LS，原样）',ds20)],
'B':[('你自己的 R020 原文（Q-GATE / Q-ERC1，原样）',qwen20),('Opus R020 原文（含对 Q-ERC1/2 的审阅，原样）',opus20),('Argon R020 原文（含对 Q-ERC1 的附注，原样）',argon20),('DeepSeek R020 原文（含对 Q-ERC1/2 的审阅，原样）',ds20)],
'C':[('Qwen R020 原文（Q-GATE，原样）',qwen20),('Opus R020 原文（PS*，原样）',opus20)],
'D':[('Qwen R020 原文（Q-GATE / 重写的 Q-ERC1，原样）',qwen20),('Opus R020 原文（PS* 与对 Q-ERC1 的审阅，原样）',opus20)]}
FMT='''############ 回复格式 ############
第一行写「R021 {n} {seat}」。先写 ANSWER BLOCK（≤300 中文字）。四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / IDEA / UNFINISHED / PARTIAL。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED。
最后必须回答主席必答题：Does your result directly advance a uniform, guaranteed construction from 2 to 47 runners? 写 YES / CONDITIONAL / NO，并说明理由。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。无界搜索不得当作封闭构造。随机测试不能推出证明。本轮不需扩大随机测试规模。
'''
for key,(seat,n,tname,where) in TRACK.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 021 · The Induction Bridge · {tname}
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R021 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 021 · The Induction Bridge, for {seat}.
TO: {seat}
ASK: do YOUR track (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: what information must pass from F_n to F_(n+1) so one mechanism reaches F_47. Unrestricted F5 and general F_n still UNFINISHED.
''','############ PART 0 · 你的任务（主席原文）############\n'+tr(tname)+'\n'+HN[key]+'\n',
    '############ PART 1 · 主席 R021 共同要求（原文）############\n'+common,
    '############ R020 主席裁决（原文，节选至 R021 开题前）############\n'+ruling+'\n'+note]
    for i,(h,t) in enumerate(ATT[key],2): p.append(f'############ PART {i} · {h} ############\n'+t)
    p.append(FMT.format(n=n,seat=seat)+'===== END =====\n')
    txt='\n'.join(p); fn=f'pkg/send_021_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode())[:16])
