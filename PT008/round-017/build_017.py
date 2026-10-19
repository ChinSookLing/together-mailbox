import hashlib
R15='/workspace/work/mb008/PT008/round-015/'; R16='/workspace/work/mb008/PT008/round-016/'
def sha(b): return hashlib.sha256(b).hexdigest()
ruling=open('chair/ruling016.txt','rb').read()
s16=open(R16+'send_016_B_Qwen.txt',encoding='utf8').read().split('\n')
inv='\n'.join(s16[299:583])   # Part 2 + 2B + 2C (lines 300..583)
opus15=open(R15+'2026-10-19T1243-reply-Opus-R015-1of4.txt','rb').read()
qwen15=open(R15+'2026-10-19T1244-reply-Qwen-R015-2of4-pasted-twice.txt','rb').read()
qb2='\n'.join(qwen15.decode().split('\n')[117:257]).encode()
opus16=open(R16+'replies/2026-10-19T1647-reply-Opus-R016-PT-008-R016-OPUS.txt','rb').read()
ds16=open(R16+'replies/2026-10-19T1503-reply-DeepSeek-R016-4of4.txt','rb').read()
ar16=open(R16+'replies/2026-10-19T1645-reply-Argon-R016.txt','rb').read()
P2D='''############ PART 2D · R016 账本（主席 R016 裁决，2026-10-19）############
一份非作者审阅 VERIFIED，第二审待完成（不因审阅数量自动升格）：Qwen Q-B2（首审 Opus）；Opus TE-AL/TE-AU（首审 Qwen）；Opus a-never-active obstruction（首审 Argon）；Opus LE/LE-1（首审 DeepSeek）。
PROOF CANDIDATE：Opus ETS（条件性：终止需假设成功时间存在，且无只依赖比例的步数上界——不是无条件构造公式）；Opus V4-B4；DeepSeek V4-R20；Argon V4-NF-20。
主席亲自手算：NF-20 充分性成立——25≤s≤100、31/100≤θ≤34/100、86/100≤w≤89/100（s=(b+c)/a，θ=b/(b+c)，w=d/(b+c)）⇒ t=20/(b+c) 成功；R20 参数盒包含于 NF-20。新颖性/覆盖差集：未确立（Argon「零重叠」被主席撤回；Hesper：盒内 2,316/20,000 点满足 NW-(i)，其余 NW 条件未查）。
DISPROVED：Qwen 的 k0,k0+1,k0+2 三步选择规则（(1,30,60,d) 网格 270/1799 点无解，首个 d=311/5）。
Argon 异常预报告（主席另行裁决）：V5=(1,5/2,5,15/2) 有效测试点；所有整数/半整数 (b+c) 锁相失败——CHECKED；t=3/(b+d)=3/10 成功，距离 3/10,1/4,1/2,1/4——CHECKED；同一时间 = (9/4)/(b+c)，故「必须切换锚点」DISPROVED；「V5 不属于任何既有规则」UNVERIFIED。
Argon C4（有限菜单不完备）自称 PROVED：主席暂不认可（文中四元组缺失，一般 τ 情形中断）。
任意五跑者 F5：UNFINISHED。
'''
P3C='''############ PART 3C · 见证点当前状态（Hesper 精确分数复核）############
V1=(1,11/10,3,41/10)：SLN1 内部 PROVED；ETS 两步 t=2/5。
V2=(1,2,3,9/2)：TE-AU、Q-B2 候选；ETS 一步 t=4/15（距离 4/15,7/15,1/5,1/5）。
V3=(1,3,4,7)：TE-AL 候选，t=1/5（距离 1/5,2/5,1/5,2/5）。
V4=(1,30,60,80)：三个候选开盒——B4 t=31/150（距离 31/150,1/5,2/5,7/15）；R20 与 NF-20 t=2/9（距离 2/9,1/3,1/3,2/9）；均 PROOF CANDIDATE（NF-20 充分性主席手算通过）。
V5=(1,5/2,5,15/2)：t=3/10 成功（距离 3/10,1/4,1/2,1/4）；b+c=d，整数/半整数 (b+c) 锁全失败。
'''
FMT='''############ PART 4 · 回复格式 ############
先写 ANSWER BLOCK（≤300 中文字）。然后：精确定理陈述（严格/非严格）、证明或反例、适用边界、与已认证规则的覆盖关系、剩余缺口。
数学有效性、新覆盖、计算核对分开写。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / IDEA / UNFINISHED。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；不做大规模暴力搜索。作者不能审自己的结果。新覆盖若无法穷尽符号比较，写 NEW COVERAGE UNFINISHED。
'''
seats={
'A_Opus':dict(seat='Opus',where='Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取',track='Track A · Cluster Extension',
 review=None,
 p2='写出 V4-B4（t=31/(5b)）的完整证明：精确假设、端点、非空性、与 R20/NF-20 区域的包含关系（精确证明哪块包含哪块，或证明互不包含）、与全部已认证区域的覆盖差集（做不完写 NEW COVERAGE UNFINISHED）。',
 rev=[('DeepSeek R016 回复全文（R20 原文）',ds16,ds16),('Argon R016 回复全文（NF-20 原文）',ar16,ar16)],
 task='把 NF-20 的固定相位 20 换成符号相位 τ：t=τ/(b+c)。求 a、b、c、d 各自的精确充分区间；寻找覆盖多个速度比区域的确定性 τ 选择机制，不得是无界试整数清单。ETS 只可作发现工具/条件性算法；若声称 ETS 给出无条件 F5，必须证明保证终止并给出不依赖已知五跑者存在性定理的显式选择规则。注：主席发现 V5 的成功时间 3/(b+d) 同时等于 (9/4)/(b+c)——τ 不必是整数或半整数。'),
'B_Qwen':dict(seat='Qwen',where='Qwen 新对话「PT-008 Qwen R017」（Play CF 项目内，Qwen3.8-Max，Thinking 开，联网关）',track='Track B · Fitting the Slow Runner',
 review='第二份独立审阅（作者均为 Opus，原文见 Part 3·REVIEW，Opus R015 全文）：(1) a-never-active obstruction（首审 Argon）：若某 u∈{b,c,d} 有 u/a∈5ℤ，则 a 的全部边沿时间 (j±1/5)/a 失败；审精确假设、证明、作用范围。(2) LE 与 LE-1（首审 DeepSeek）：LE 与 LE-1 分开给结论；LE-1 必须区分「孤立成功点的必要刻画」与「构造成功时间的充分条件」。',
 p2=None,
 rev=[('Opus R015 1/4 全文（a-never-active、LE/LE-1 原文）',opus15,opus15)],
 task='把 b,c,d 当作一个簇：找出让它们位置安全的代数选择规则，再判定 a 是否也安全；研究能否用显式区间或相位不等式把最慢速度纳入。无证明不作全局覆盖声明。宣称新区域前核对与 Part 2/2B/2C 全部已认证构造的重叠。'),
'C_Argon':dict(seat='Argon',where='Gemini 新对话「PT-008 Argon R017」（3.1 Pro，High，Personal Intelligence 关）',track='Track C · Adversarial Cluster Test',
 review='第二份独立审阅：Opus TE-AL / TE-AU（作者 Opus，首审 Qwen；原文见 Part 3·REVIEW，Opus R015 全文）。逐条：精确实数假设、t=1/(5a) 与 t=4/(5a)、乘积域（每个 u/a mod 5 的安全弧）、证明、端点、反例检查。TE-AL 与 TE-AU 分开给结论。',
 p2='写出你的 V4-NF-20 完整证明（主席已手算其充分性）：边界端点、非空性、R20⊂NF-20 的精确证明、与全部已认证区域的覆盖差集（做不完写 NEW COVERAGE UNFINISHED；你 R016 的「零重叠」已被撤回）。另：把 C4 重写成完整陈述——补上缺失的速度四元组，并精确限定菜单类型；做不到就降为 PROOF CANDIDATE 或 UNFINISHED。',
 rev=[('Opus R015 1/4 全文（TE-AL/TE-AU 原文）',opus15,opus15),('你自己的 Argon R016 回复全文（NF-20、C4 原文）',ar16,ar16)],
 task='挑战本轮提出的 τ 选择规则：无理速度比、端点相等、相位碰撞、虚假新颖性、有界相位菜单失败。区分「某固定菜单失败」与「所有构造公式不可能」。'),
'D_DeepSeek':dict(seat='DeepSeek',where='DeepSeek 新对话「PT-008 DeepSeek R017」（DeepThink 开，联网关）',track='Track D · Structural Generalization',
 review='第二份独立审阅：Qwen Q-B2（作者 Qwen，首审 Opus；原文见 Part 3·REVIEW）。逐条：精确实数假设 3/2≤c/b≤9、(b+c)/a≤10、3/5≤d/(b+c)≤9/10、t=2/(b+c)、四个距离证明、每个端点、反例检查，并核对与已认证规则的重叠。',
 p2='写出你的 V4-R20（t=20/(b+c)）完整证明：端点、非空性、R20⊂NF-20 的精确证明、与全部已认证区域的覆盖差集（做不完写 NEW COVERAGE UNFINISHED）。',
 rev=[('Qwen R015 2/4 Part 3（Q-B2 原文，双贴的第一份，第 118–257 行）',qb2,qwen15),('你自己的 DeepSeek R016 回复全文（R20、单侧窗口原文）',ds16,ds16)],
 task='研究「先簇后最慢」构造能否推广到更多跑者：求 n 跑者的符号充分条件，不只是 n=6 或 12 的数值例子。另：分别检验下包络交点处的成功时间是否有单侧安全区间（主席已认可你 R016 单侧窗口判据的局部思路，安排正式复核）。'),
}
for k,s in seats.items():
  parts=[]
  n=1
  if s['review']: parts.append(f'【{n}】（Priority 1）{s["review"]}'); n+=1
  if s['p2']: parts.append(f'【{n}】（Priority 2）{s["p2"]}'); n+=1
  parts.append(f'【{n}】{s["track"]}：{s["task"]}')
  out=f'''WHO（给谁）：{s['seat']} —— PT-008 Round 017 · {s['track']}
WHERE（贴到哪）：{s['where']}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R017 {s['seat']}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 017 · Cluster First, Slowest Last · {s['track']}, for {s['seat']}.
TO: {s['seat']}
ASK: do the items in Part 0 in order. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing. Review assignments are the courier's (author never reviews own work).
THIS ROUND SERVES PROOF STEP: control the faster cluster's phases first, then bring the slowest runner into the safe arc — a deterministic selection mechanism (unrestricted F5 still UNFINISHED).

############ PART 0 · 你的任务 ############
''' + '\n'.join(parts) + f'''

############ PART 1 · 主席 R016 裁决、R017 原文、Argon 异常回复裁决（逐字，Tuzi 2026-10-19 17:04 转贴，sha256 {sha(ruling)}）############
{ruling.decode()}

{inv}

{P2D}
'''
  for title,b,full in s['rev']:
    out+=f'''############ PART 3 · 原文：{title}（字节级原文；完整回复 sha256 {sha(full)}）############
{b.decode()}

'''
  out+=P3C+'\n'+FMT+'===== END =====\n'
  open(f'pkg/send_017_{k}.txt','w',encoding='utf8').write(out); print(k,len(out),sha(out.encode()))
