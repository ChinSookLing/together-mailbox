import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
rul=open('chair/2026-10-20T1203-chair-ruling-R024-and-R025-text-via-Tuzi.txt',encoding='utf8').read()
r=rul[rul.index('PT-008 · Round 025 · Zero-Measure, Nonempty\n'):rul.index('ROUND 025 OPEN')+len('ROUND 025 OPEN')]
ruling=rul[rul.index('PT-008 · Round 024 · 主席裁决'):rul.index('五、Round 025')]
note=rul[rul.index('六、给 Hesper'):rul.index('Tuzi，現在')]
common=r[:r.index('Track A —')]+r[r.index('North Star'):]
def tr(name):
    a=r.index(name); nxt=[r.find(x,a+5) for x in ('Track A —','Track B —','Track C —','Track D —','North Star')]
    return r[a:min(x for x in nxt if x>a)]
D='/workspace/work/pt008r24/replies/'
rd=lambda p:open(D+p,encoding='utf8').read()
opus=rd('2026-10-20T1143-reply-Opus-R024.txt'); qwen=rd('2026-10-20T1143-reply-Qwen-R024.txt')
ds=rd('2026-10-20T1144-reply-DeepSeek-R024.txt'); kimi=rd('2026-10-20T1155-reply-Kimi-R024-TrackC-supplement.txt')
HF='Hesper 事实（精确分数）：'
HN={'A':HF+'B_V1=14、|B_V2|=48、|B_V3|=152；§5 表七行 ℓ、r、r/ℓ；密度 5/36、8/63、7/30、157/720；S_{1/6}(1,…,5) 测度 0、点 1/6、5/6——均已确认。主席：MZ 为 PROOF CANDIDATE；「所有测度型证书不可能成功」不予认证——请把一般 MZ 写成完整证明供非作者审查。Qwen、DeepSeek R024 原文附后。',
'B':HF+'你 R024 §3 第 4 区间应为 [13/24, 23/42]（你写 19/42；宽 1/168 正确），主席已接受此勘误；其余五区间与总测度 8/63 已确认。你的充分条件 w>1/u 有效但弱于 Opus GLC(i) 的 w≥2δ′/u。Opus R024 原文附后。',
'C':'Hesper 注：本轮你正式接 Track C（主席邀请）。只做一项、窄范围：从 Opus 的 MZ 或 Qwen 的精确再生断言中选一个审其证明；优先给可手算反例或简短的已核证明。u=5/48 截断族例子已是 R023/R024 已知结果，不得再作新结果。Opus R024 只给了 MZ 的陈述与 n=4 例子（S_{1/6}(1,…,5) 测度 0、点 1/6、5/6，Hesper 已核），一般证明尚未提交——若审 MZ，请写明所缺部分或报 UNFINISHED。Opus、Qwen R024 原文附后（DeepSeek 不必审）。回复宜 ≤1500 字。',
'D':HF+'你 R024 GBR 例子数字有误，主席已接受更正：S_{1/5}(2,3,4)∩[0,1]=[1/10,1/5]∪{2/5}∪{3/5}∪[4/5,9/10]，最大间隔 g=1/5（非 3/5）；S_{1/6}(1,2,3,4)∩[0,1]=[1/6,5/24]∪[7/18,5/12]∪[7/12,11/18]∪[19/24,5/6]，g′=1/3（非 ≥7/12）；t=1/5 正确，「不自动保持」结论仍成立（u′≥5 时 2/15<1/3）。另：「任意长度 ≥g 的开区间必与 S 相交」在 g=最大间隔时不成立，请用闭弧精确定义。你自己、Opus、Qwen R024 原文附后。'}
TRACK={'A':('Opus','1/4','Track A — Opus: Arithmetic Certificate','Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取'),
'B':('Qwen','2/4','Track B — Qwen: Exact Threshold Update','Qwen 新对话「PT-008 Qwen R025」（Play CF 项目，3.8-Max thinking，web 关）'),
'C':('Kimi','3/4','Track C — Kimi: Independent Adversarial Audit','Kimi 新对话「PT-008 Kimi R025」（思考模式开，联网关）'),
'D':('DeepSeek','4/4','Track D — DeepSeek: Nonemptiness Guarantee','DeepSeek 新对话「PT-008 DeepSeek R025」（深度思考开，联网关）')}
ATT={'A':[('你自己的 R024 原文（原样）',opus),('Qwen R024 原文（原样）',qwen),('DeepSeek R024 原文（GBR，原样；例子数字已由 Hesper 更正）',ds)],
'B':[('你自己的 R024 原文（原样）',qwen),('Opus R024 原文（原样）',opus)],
'C':[('Opus R024 原文（含 MZ，原样）',opus),('Qwen R024 原文（原样）',qwen),('你自己的 R024 Track C 补充原文（原样）',kimi)],
'D':[('你自己的 R024 原文（原样）',ds),('Opus R024 原文（含 MZ，原样）',opus),('Qwen R024 原文（原样）',qwen)]}
FMT='''############ 回复格式 ############
第一行写「R025 {n} {seat}」{extra}。先写 ANSWER BLOCK（≤300 中文字）。四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / IDEA / UNFINISHED / PARTIAL。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED，并写出逐项论证（笼统 VERIFIED 不计数）。
主席必答：Does your result supply an automatically regenerating guarantee? YES / CONDITIONAL / NO / UNFINISHED。给出精确定义、假设、证明、局限与独立审阅状态。区分「精确表示」与「保证非空输出」。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。不得用已知存在性定理代替显式构造。不要假设无理速度有有限共同周期。随机测试不能推出证明。不做大规模穷举。
'''
for key,(seat,n,tname,where) in TRACK.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 025 · Zero-Measure, Nonempty · {tname}
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R025 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 025 · Zero-Measure, Nonempty, for {seat}.
TO: {seat}
ASK: do YOUR track (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: one finite constructive certificate covering BOTH positive-length safe intervals AND isolated / zero-measure successes, with an effective threshold change 1/n→1/(n+1) and addition of a new speed — the step needed to reach F_47. Unrestricted F5 and general F_n still UNFINISHED.
''','############ PART 0 · 你的任务（主席原文）############\n'+tr(tname)+'\n'+HN[key]+'\n',
    '############ PART 1 · 主席 R025 共同要求（原文）############\n'+common,
    '############ R024 主席裁决（原文，节选至 R025 开题前）############\n'+ruling+'\n'+note]
    for i,(h,t) in enumerate(ATT[key],2): p.append(f'############ PART {i} · {h} ############\n'+t)
    p.append(FMT.format(n=n,seat=seat,extra='（Track C）' if key=='C' else '')+'===== END =====\n')
    txt='\n'.join(p); fn=f'pkg/send_025_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode())[:16])
