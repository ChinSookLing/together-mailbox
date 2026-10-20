import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
rul=open('chair/2026-10-20T1003-chair-ruling-R021-and-R022-text-via-Tuzi.txt',encoding='utf8').read()
r21=rul[rul.index('PT-008 · Round 022 · The Exceptional Set\n\nFROM'):rul.index('ROUND 022 OPEN')+len('ROUND 022 OPEN')]
ruling=rul[:rul.index('四、Round 022')]
note=rul[rul.index('五、给 Hesper 的归档裁决'):rul.index('Tuzi，这一轮')]
common=r21[:r21.index('Track A —')]+r21[r21.index('Mandatory Question'):]
def tr(name):
    a=r21.index(name); nxt=[r21.find(x,a+5) for x in ('Track A —','Track B —','Track C —','Track D —','Mandatory Question')]
    return r21[a:min(x for x in nxt if x>a)]
D='/workspace/work/pt008r21/replies/'
rd=lambda p:open(p,encoding='utf8').read()
opus=rd(D+'2026-10-20T0939-reply-Opus-R021.txt'); qwen=rd(D+'2026-10-20T0947-reply-Qwen-R021.txt')
argon=rd(D+'2026-10-20T0951-reply-Argon-R021.txt'); ds=rd(D+'2026-10-20T0953-reply-DeepSeek-R021.txt')
HN={'A':'Hesper 注：Priority 1 由你负责——请给出 PS_n、PS*、LS-1、LS-R、APS、H、FO、TL、OB 九项的完整定理陈述，每项按主席五点分开写。主席对命题 H 的意见：「成功时间点 ⇏ 严格正余量」，请写明用哪个门槛（1/n 或 1/(n+1)）与哪种窗口。Hesper 事实：(1,10,21,30) 换局外人 b 得 t=F4(1,21,30)=13/51 成立；另一成功时间 t=7/31（四距离 7/31, 8/31, 8/31, 7/31）。Qwen、Argon、DeepSeek 的 R022 原文附后。',
'B':'Hesper 注：主席已认证 Q-GATE 仅限三跑者簇安全（b,c,d），不含 a；「Q-GATE + 周期平移装入 a」为 GAP FOUND。Argon 族 (1,N,2N+1,3N)：L=s，frac(L/s)=0，固定局外人 a 时相位锁死（Hesper 复算 N=2,5,10,20）。Argon 答案块里的 (1,12,24,32) 反例不成立（L=9，frac(L/s)=1/4），不得采用。另：你 R022 写的递推 F_n(V)=F_{n-1}(V∖u)+n·P_u，PS 实为 +j·P_u，请更正。Opus、Argon、DeepSeek 的 R022 原文附后。',
'C':'Hesper 注（只做一项，回复宜短 ≤1500 字）：选 PS*、TL 或「换局外人」规则中的一条精确陈述，用一个有理反例去推翻；每个允许的局外人都要算，不只第一个。注意：你 R022 答案块里的 (1,12,24,32) 反例经主席裁定不成立（L=9，frac(L/s)=1/4≠0），不得沿用；族 (1,N,2N+1,3N) 只推翻固定局外人 a 的规则——(1,10,21,30) 换局外人 b 有 t=13/51。Opus R022 原文（含 PS_n、PS*、TL、OB 陈述）附后。',
'D':'Hesper 注：主席要求你的条件归纳引理补上时间域条件——σ=−1（向左移）时必须保证 t=t0−Δ>0（例如假设 t0−h>0，或说明实际位移仍为正）。你的引理与 Opus 命题 H(3)、定理 FO 内容重叠，请写清区别。请独立审阅 Opus 的 H、FO、TL、OB（Opus R022 原文附后，PART 2）。'}
TRACK={'A':('Opus','1/4','Track A — Opus: Exceptional Set Structure','Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取'),
'B':('Qwen','2/4','Track B — Qwen: Corrected Cluster Transfer','Qwen 新对话「PT-008 Qwen R022」（Play CF 项目，3.8-Max thinking，web 关）'),
'C':('Argon','3/4','Track C — Argon: One Narrow Falsification Task','Gemini 新对话「PT-008 Argon R022」（3.1 Pro，High，Personal Intelligence 关）'),
'D':('DeepSeek','4/4','Track D — DeepSeek: Minimal Induction Invariant','DeepSeek 新对话「PT-008 DeepSeek R022」（深度思考开，联网关）')}
ATT={'A':[('你自己的 R021 原文（原样）',opus),('Qwen R021 原文（原样）',qwen),('Argon R021 原文（原样）',argon),('DeepSeek R021 原文（含 Q-GATE、Q-ERC1 审阅与条件归纳引理，原样）',ds)],
'B':[('你自己的 R021 原文（原样）',qwen),('Opus R021 原文（原样）',opus),('Argon R021 原文（原样）',argon),('DeepSeek R021 原文（原样）',ds)],
'C':[('Opus R021 原文（PS_n / PS* / TL / OB，原样）',opus)],
'D':[('Opus R021 原文（H / FO / TL / OB，原样）',opus),('你自己的 R021 原文（原样）',ds)]}
FMT='''############ 回复格式 ############
第一行写「R022 {n} {seat}」。先写 ANSWER BLOCK（≤300 中文字）。四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / IDEA / UNFINISHED / PARTIAL。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED。
最后必须回答主席必答题：Does the proposed result provide a guaranteed mechanism for the induction step, or does it only describe a sufficient subset of inputs? 写 YES / CONDITIONAL / NO；若 CONDITIONAL，写出缺少的假设，并说明它是否自动保持。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。无界搜索不得当作封闭构造。随机测试不能推出证明。不做大规模穷举。
'''
for key,(seat,n,tname,where) in TRACK.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 022 · The Exceptional Set · {tname}
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R022 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 022 · The Exceptional Set, for {seat}.
TO: {seat}
ASK: do YOUR track (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: is the exceptional set E*_n a real obstruction or an artifact of current selection rules; what minimal invariant must pass from F_n to F_(n+1). Unrestricted F5 and general F_n still UNFINISHED.
''','############ PART 0 · 你的任务（主席原文）############\n'+tr(tname)+'\n'+HN[key]+'\n',
    '############ PART 1 · 主席 R022 共同要求（原文）############\n'+common,
    '############ R021 主席裁决（原文，节选至 R022 开题前）############\n'+ruling+'\n'+note]
    for i,(h,t) in enumerate(ATT[key],2): p.append(f'############ PART {i} · {h} ############\n'+t)
    p.append(FMT.format(n=n,seat=seat)+'===== END =====\n')
    txt='\n'.join(p); fn=f'pkg/send_022_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode())[:16])
