import hashlib,os
R18='/workspace/work/mb008/PT008/round-018/'
sha=lambda b:hashlib.sha256(b).hexdigest()
rul=open('chair/2026-10-19T1907-chair-ruling-R018-and-R019-text-via-Tuzi.txt',encoding='utf8').read()
# R019 section only (from "PT-008 · Round 019 · Phase Lattice Switching" to "ROUND 019 OPEN\n\n— GPT-6\nChair · PT-008 Time Forge")
i=rul.index('PT-008 · Round 019 · Phase Lattice Switching'); jx=rul.index('Chair · PT-008 Time Forge',i)+len('Chair · PT-008 Time Forge')
r19=rul[i:jx]
rd=lambda n:open(R18+'replies/'+n,encoding='utf8').read()
opus=rd('2026-10-19T1832-reply-Opus-R018.txt'); qwen=rd('2026-10-19T1846-reply-Qwen-R018.txt')
ds=rd('2026-10-19T1848-reply-DeepSeek-R018.txt'); arg=rd('2026-10-19T1856-reply-Argon-R018-resend.txt')
LEDGER='''############ R018 账本（主席 R018 正式裁决，2026-10-19）############
R018 CLOSED — PARTIAL · CLR v2 REPAIRED AND CERTIFIED · B4⁺ NOVELTY CORRECTED · R019 OPEN。
- Opus CLR v2：PROVED（PT-008 内部认证），限于完整假设：Q/m、Qθ0/m、Qw0/m ∈ ℤ；非空安全余数集 R⊂{0..Q−1}、最大循环间隔 G；μ_b、μ_c、μ_d 取 R 上最小值且严格为正；s ≥ 5G/(3m)；τ|θ−θ0| ≤ min(μ_b,μ_c)，τ|w−w0| ≤ μ_d。规则 k0=⌈ms/5⌉，k=k0+min_{ρ∈R}((ρ−k0) mod Q)，τ=k/m，t=τ/(b+c)。
  主席反例修复：(7/20,2,5,6)，Q=14，R={4,10}，G=8 → t=5/7，距离 (1/4,3/7,3/7,2/7)。
- Opus B4⁺ 充分性：PROVED（31/4≤b/a≤31，61/31≤c/b≤64/31，81/31≤d/b≤84/31 ⇒ t=31/(5b)）。
- 「B4⁺ 整块为新覆盖」：DISPROVED —— 角点 (1,31,61,81) 同属 TE-AL 与 TE-AU（t=1/5 与 t=4/5 四距离均为 1/5）。覆盖差集另作研究。
- Argon C4：PROVED，仅限其定义的受限有限静态菜单 M(Kmax,M)；反例族 V_N=(1,5N,10N,15N)，N=max(Kmax+1,⌊M⌋+1)。V_N 有成功时间 t_N=(4N+1)/(20N)，距离 (1/5+1/(20N),1/4,1/2,1/4)。不得推广到所有有限/自适应公式。
- Argon「有限 CLR 家族在大 s 下形状覆盖面积 → 0」：PROOF CANDIDATE，待条件审阅。
- Qwen Q-PSR：有条件的正确构造，属 CLR v2 在 m=1、零形状偏差下的特例；不得计为第二条一般机制。有理形状的联合整数相位安全集可能为空。
- 先前已认证（R017）：Q-B2；TE-AL/TE-AU；a-never-active obstruction；LE；LE-1（仅必要刻画）。Q-FSR 为固定整数 k 的正确充要刻画。
- 一般确定性相位选择：UNFINISHED。无限制 F5：UNFINISHED。不批准上墙。

############ Hesper 精确分数核对（仅事实，不作裁决）############
V5=(1,5/2,5,15/2)：θ=1/3，w=1（b+c=d）。取 Q=3m（满足三项周期条件），全部严格安全余数集：
m=1：空（kw=k∈ℤ，‖kw‖=0）；m=2：空；m=3：R={2,7}，距离 (2/9,4/9,1/3)；m=4：R={3,9}，距离 (1/4,1/2,1/4)；m=5：R={3,4,6,9,11,12}（含距离恰为 1/5 者）；m=6：R={4,14}；m=7：R={5,16}；m=8：R={5,6,18,19}。
即 V5 形状下，最小可用分母为 m=3（不只 m=4）。
其他见证点：V1=(1,11/10,3,41/10) SLN1；V2=(1,2,3,9/2) Q-B2/TE-AU t=2/5；V3=(1,3,4,7) TE-AL t=1/5；V4=(1,30,60,80) CLR(m=1,Q=9,R={4,5}) t=11/45；V5 CLR(m=4,Q=12,R={3,9}) t=3/10。
'''
TRACK={
'A':('Opus','1/4','Track A — Opus: Switching Between Lattices','Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取'),
'B':('Qwen','2/4','Track B — Qwen: Empty-Residue Classification','Qwen 新对话「PT-008 Qwen R019」（Play CF 项目，3.8-Max thinking，web 关）'),
'C':('Argon','3/4','Track C — Argon: Adversarial Resource-Light Review','Gemini 新对话「PT-008 Argon R019」（3.1 Pro，High，Personal Intelligence 关）'),
'D':('DeepSeek','4/4','Track D — DeepSeek: Effective Phase Selection','DeepSeek 新对话「PT-008 DeepSeek R019」（深度思考开，联网关）'),
}
FMT='''############ 回复格式 ############
第一行写「R019 {n} {seat}」。先写 ANSWER BLOCK（≤300 中文字）。然后：精确定理陈述（严格/非严格）、证明或反例、适用边界、剩余缺口。
四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / IDEA / UNFINISHED。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。无界搜索不得当作封闭选择规则。
'''
def tr(name):
    a=r19.index(name); 
    nxt=[r19.find(x,a+5) for x in ('Track A —','Track B —','Track C —','Track D —','Common Mathematical Requirement')]
    nxt=[x for x in nxt if x>a]; return r19[a:min(nxt)]
common=r19[r19.index('Central Research Question'):r19.index('Track A —')]+r19[r19.index('Common Mathematical Requirement'):r19.index("Chair’s Goal")]
out={}
for key,(seat,n,tname,where) in TRACK.items():
    parts=[f'''WHO（给谁）：{seat} —— PT-008 Round 019 · Phase Lattice Switching · {tname}
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R019 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 019 · Phase Lattice Switching, for {seat}.
TO: {seat}
ASK: do YOUR track (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: a deterministic, speed-dependent rule that chooses the phase lattice (τ=k/m) and the phase, with proof, instead of a longer list of successful examples. Unrestricted F5 still UNFINISHED.
''',
    '############ PART 0 · 你的任务（主席原文）############\n'+tr(tname)]
    if key=='C':
        parts.append('''Hesper 注（按主席指示）：只做一项针对性审阅/反例，不做大规模扫描。Opus/Qwen 的 R019 方案尚未产生；请审阅下面的现成具体方案「V5 分数格切换」：
方案（取自 R018 已认证 CLR v2）：对 b+c=d（w=1）、θ=1/3 的形状族，整数格 m=1 安全集为空；改用 m=4，Q=12，R={3,9}，k0=⌈4s/5⌉，k=k0+min((ρ−k0) mod 12)，τ=k/4，t=τ/(b+c)。尝试打破：周期条件、选择规则、边界情形（s 小、取等）、以及「m=4 对所有 w=1 形状都够」这类分母声明（例如 θ≠1/3 时）。给出一个具体反例或 PROOF VERIFIED / UNFINISHED。回复宜短（≤1500 字）。若你的上下文出现混乱，直接写 UNFINISHED。''')
    parts.append('############ PART 1 · 主席 R019 中心问题与共同要求（原文）############\n'+common)
    parts.append(LEDGER)
    if key in 'ABD':
        parts.append('############ PART 2 · Opus R018 原文（CLR v2 完整证明，原样）############\n'+opus)
    if key in 'BD':
        parts.append('############ PART 3 · Qwen R018 原文（Q-PSR；主席裁定为 CLR v2 m=1 特例，原样）############\n'+qwen)
    if key=='A':
        parts.append('############ PART 3 · DeepSeek R018 审阅原文（原样）############\n'+ds)
    parts.append(FMT.format(n=n,seat=seat)+'===== END =====\n')
    txt='\n'.join(parts)
    fn=f'pkg/send_019_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode()))
