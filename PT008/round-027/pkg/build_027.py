import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
rul=open('chair/2026-10-20T1407-chair-GPT6-R026-ruling-R027-open-via-PT006.txt',encoding='utf8').read()
r=rul[rul.index('PT-008 · Round 027 · From Skeleton to Selector\n\nFROM'):rul.index('ROUND 027 OPEN')+len('ROUND 027 OPEN')]
ruling=rul[rul.index('PT-008 · Round 026 · 主席正式裁決'):rul.index('四、Round 027')]
note=rul[rul.index('五、給 Hesper 的歸檔決定'):rul.index('Tuzi，今天')]
common=r[:r.index('Track A —')]+r[r.index('Required Reply'):]
def tr(name):
    a=r.index(name); nxt=[r.find(x,a+5) for x in ('Track A —','Track B —','Track C —','Track D —','Required Reply')]
    return r[a:min(x for x in nxt if x>a)]
D='/workspace/work/pt008r26/replies/'
rd=lambda p:open(D+p,encoding='utf8').read()
opus=rd('2026-10-20T1250-reply-Opus-R026.txt'); qwen=rd('2026-10-20T1258-reply-Qwen-R026-full.txt')
kimi=rd('2026-10-20T1256-reply-Kimi-R026-v2-on-Opus-R026-HS.txt'); ds=rd('2026-10-20T1259-reply-DeepSeek-R026.txt')
HF='Hesper 事实（精确分数，仅核对，非证明）：'
HN={'A':HF+'你 R026 计重数 30/83/341、去重 20/77/321、k(σ+1)/2=32/86/344、V={1} 反例、κ=1/5、9/31、1/3 均已确认（有限实例，不代替一般计数证明）。主席：LM、HS 内部 PROVED（限 R026 精确陈述）；ACC 旧上界 kσ/2 DISPROVED；k(σ+1)/2 待逐式复核；UP/PR PROOF CANDIDATE，无非作者审阅——请写成可独立审阅的完整版（DeepSeek 将审 UP/PR）。Qwen、Kimi、DeepSeek R026 原文附后。',
'B':HF+'主席已裁：(i) 你 §2.1「区间中点与 ACC/SPC 输出同一时间」不接受——只有 ACC=SPC 选同一时间；(ii) §4.1「B_V ⊂ C(V)」不成立：V1=(1,3,4,7) 的 m_V 在 (0,1/2) 有 12 个断点，t=1/3（‖3t‖=0，局部最小）不在 C(V)；可用的是 argmax ∈ B_V∩C(V)，依赖它的复杂度比较须撤回。(iii) ACC 上界应为 k(σ+1)/2（kσ/2 已 DISPROVED，反例 V={1}），ACC 规模 O(kσ)。(iv) 区分项用状态词，不用 YES。你的实例数字（V1 孤立点 k/5、V2 的 9/31、t=1/4 距离 1/4,1/2,1/4,1/2）已确认。Opus R026 原文附后。',
'C':'Hesper 注：本轮 Track C 仍由你担任。主席要求你从 Opus 或 Qwen 的「新选择断言」中选一条审实际定理（不审转述）；若无完整选择器，则审 Opus 修正后的 ACC 计数上界 |C_P(V)| ≤ k(σ+1)/2（见附后 Opus R026 §3.1 (iii)：逐项 ⌊(N_v+N_v′)/2⌋ 与 ⌊(N_v+1)/2⌋ 求和）。Opus/Qwen 的 R027 回复送到后，Hesper 会把其中的选择断言作补充件转给你；补充件未到时，请先审该上界。注意：你 R026 两份 HS 审阅被主席计为一位审阅者。Opus、Qwen R026 原文附后。回复宜 ≤1500 字。',
'D':HF+'主席：你 R026 的 LM、HS 非作者 VERIFIED 已计入（LM、HS 内部 PROVED）；ACC-com 核心构造保留你的 VERIFIED，但你标 VERIFIED 的计数上界 kσ/2 错（V={1} 有 1 个候选 1/2 > 1/2；第二类精确数为 ⌊(N_v+1)/2⌋，V1 为 9 而非 7.5）——修正上界 k(σ+1)/2 另行审阅。GBR 仍属作者自审，不计。本轮主任务：独立审 Opus 的 UP 与 PR（Opus R026 §4，原文附后；Opus R027 若交完整版，以主席后续转交为准）。你自己的 R026 原文附后。'}
TRACK={'A':('Opus','1/4','Track A — Opus: Skeleton Selection','Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取'),
'B':('Qwen','2/4','Track B — Qwen: Direct Selector','Qwen 新对话「PT-008 Qwen R027」（Play CF 项目，3.8-Max thinking，web 关）'),
'C':('Kimi','3/4','Track C — Kimi: Independent Selector Audit','Kimi 新对话「PT-008 Kimi R027」（思考模式开，联网关）'),
'D':('DeepSeek','4/4','Track D — DeepSeek: Guarantee Versus Enumeration','DeepSeek 新对话「PT-008 DeepSeek R027」（深度思考开，联网关）')}
ATT={'A':[('你自己的 R026 原文（原样）',opus),('Qwen R026 原文（三段合并，原样）',qwen),('Kimi R026 Track C 原文（审 Opus R026 版 HS，原样）',kimi),('DeepSeek R026 原文（原样）',ds)],
'B':[('你自己的 R026 原文（三段合并，原样）',qwen),('Opus R026 原文（原样）',opus)],
'C':[('Opus R026 原文（含 ACC 修正上界，原样）',opus),('Qwen R026 原文（三段合并，原样）',qwen)],
'D':[('Opus R026 原文（含 UP/PR，原样）',opus),('你自己的 R026 原文（原样）',ds)]}
FMT='''############ 回复格式 ############
第一行写「R027 {n} {seat}」{extra}。先写 ANSWER BLOCK（≤300 中文字）。然后分别回答主席五问，每问只用 PROVED / CONDITIONAL / UNFINISHED：1. Candidate generation；2. Candidate success；3. Finite selection；4. Arbitrary real speeds；5. Uniform F_n induction。四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / UNFINISHED。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED，并写出逐项论证（笼统 VERIFIED 不计数）。
区分：A 生成候选；B 证明成功候选存在；C 以有显式界的有限构造步骤选出。可计算搜索界即使成立，也不自动是 Tuzi 要的直接公式。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。不得用已知存在性定理代替显式构造。不要假设无理速度有有限共同周期。随机测试不能推出证明。不做大规模穷举。
'''
for key,(seat,n,tname,where) in TRACK.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 027 · From Skeleton to Selector · {tname}
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R027 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 027 · From Skeleton to Selector, for {seat}.
TO: {seat}
ASK: do YOUR track (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: turn the proved skeleton (LM/HS) into a guaranteed finite selector with an explicit bound — not a list of candidates but the rule that picks the safe time — the step needed to reach F_47. Unrestricted F5 and general F_n still UNFINISHED.
''','############ PART 0 · 你的任务（主席原文）############\n'+tr(tname)+'\n'+HN[key]+'\n',
    '############ PART 1 · 主席 R027 共同要求（原文）############\n'+common,
    '############ R026 主席裁决（原文，节选至 R027 开题前）############\n'+ruling+'\n'+note]
    for i,(h,t) in enumerate(ATT[key],2): p.append(f'############ PART {i} · {h} ############\n'+t)
    p.append(FMT.format(n=n,seat=seat,extra='（Track C）' if key=='C' else '')+'===== END =====\n')
    txt='\n'.join(p); fn=f'pkg/send_027_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode())[:16])
