import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
ch=open('chair/2026-10-20T2156-chair-R030-draft-verbatim.txt',encoding='utf8').read()
CH=ch[ch.index('TO：Hesper'):]
r29=open('/workspace/work/pt008r29/chair/2026-10-20T1729-chair-GPT6-R029-open-FW4-via-Tuzi.txt',encoding='utf8').read()
R29=r29[r29.index('TO：Hesper'):]
t4=open('/workspace/work/pt008r20/hesper/base.py').read(); t4=t4[t4.index('def F3'):t4.index('A=lambda')]
T4='已认证 T4（PT-008 内部 PROVED，2026-10-18，八段，Opus 作者；手稿 sha256 4720413d）的分支，以 Hesper 存档的精确代码形式抄录（q=1/4，nd=到最近整数距离，fr=小数部分；分支按顺序先命中先用）：\n'+t4
STATUS=('R029 记录（不升级）：FW₄ 仍 UNFINISHED；五席均未找到反例或全域证明。Opus 的 FW-SO（b≤5a/4）、R2（c≥6b）、R2′（c≥15b/4 且 d≥4c/3）有 Kimi 非作者审阅 PROOF VERIFIED，但主席尚未裁决。'
 'Qwen 归约 x=at 的正确范围是 x∈[1/5,4/5]（Kimi 指出原文误把 ‖x‖ 当 x）。主席未发 R029 结案裁决；本轮按主席转向信开题。')
LEMMA='已认证可用引理（主席认证，可直接引用）：T4（四跑者显式构造，安全度 1/4）；FW₃（T4 输出满足 a·t<11/12）；FW₂；FWS(i)（计重数）；FWS(ii)（FW_k ⇒ F^FW 安全，前提不得移除）；CNT k(σ+1)/2。'
FACT=('Hesper 事实（精确分数，CHECKED，不是证明）：(1) 主席路线 A 的区间公式 t_*=max{L,(m_*+δ)/u}：20,000 组随机有理 (δ,u,L,R) 中判据成立的 19,826 组，t_* 全部落在 [L,R] 且 ‖u t_*‖≥δ，0 失败。'
 '(2) 主席路线 B 的等价式：2,992 组随机有理速度（n=3..7，δ=1/n）先找到一个安全 t，取 q_i=⌊v_i t⌋，全部满足两两不等式，且 t=max_i (q_i+δ)/v_i 也安全，0 失败。'
 '(3) R029：剩余区域 d>4a、c<d<4c 内整数四元组 1≤a<b<c<d≤24 共 5,890 组都有首窗安全时间。这些只是有限检查，不代替证明。')
TASK={'A':'你的任务（主席分工表）：路线 A——全安全集合的结构。交付：一个明确的一般 k 不变量（必须能从旧速度验证，并证明更新后保持；不能只是“新安全集合非空”的改写）、更新法，以及最弱未证步骤。',
'D':'你的任务（主席分工表）：路线 A 的独立攻击。检查路线 A 的保证是否循环论证、是否遗漏短分量及孤立安全点；给出证明或反例。你不会先看到 Opus 本轮的回复；请独立攻击主席文中的路线 A 表述，若 Opus 的不变量送到，Hesper 会作补充件转给你。',
'B':'你的任务（主席分工表）：路线 B——全局整数构造。利用主席给出的两两耦合不等式 v_j q_i − v_i q_j ≤ (1−δ)v_i − δ v_j，提出直接构造整数向量 q 的原理（取整原理、格点构造或其他有保证的选择机制）。明确禁止用无界枚举充当答案。区间内取时间的整数选择已有主席直接公式，不要再把主要精力花在那里。',
'C':'你的任务（主席分工表）：对抗审阅（adversarial review）。攻击两条路线的确切命题：主席路线 A 区间公式 t_* 的证明、路线 A 失败条件的表述、路线 B 的等价推导（两个方向）。逐项区分：表示失败、选择器失败、原命题失败。若 Opus/Qwen/DeepSeek 的回复送到，Hesper 会作补充件转给你。回复宜 ≤1500 字。'}
SEAT={'A':('Opus','1/4','Tuzi 的 claude.ai（Opus）对话'),
'D':('DeepSeek','2/4','DeepSeek 新对话「PT-008 DeepSeek R030」（深度思考开，联网关）'),
'B':('Qwen','3/4','Qwen 新对话「PT-008 Qwen R030」（Play CF 项目，thinking，web 关）'),
'C':('Kimi','4/4','Kimi 新对话「PT-008 Kimi R030」（思考模式开，联网关）')}
FMT='''############ 回复格式 ############
第一行写「R030 {n} {seat}」。先写 ANSWER BLOCK（≤300 中文字）：你负责的路线交付了什么（一般定理候选 / 反例 / 比现有障碍更具体的未证引理 / UNFINISHED）。正文分三类标注：FACT / PROOF / IDEA。必须写出「最不确定的一步」。四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / UNFINISHED；审阅结论每项单独给 PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED，并写逐项论证。失败尝试与反例也要报告。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。数值扫描只记 CHECKED。仅增加区域覆盖不算本轮交付。不要假设无理速度有有限共同周期。单个选择器失败不是原命题的反例。不做大规模穷举。
'''
for key,(seat,n,where) in SEAT.items():
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 030 · 双路线：安全集合结构（A）/ 全局整数构造（B）
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R030 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 030 · two routes, for {seat}.
TO: {seat}
ASK: do YOUR task (Part 0) only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: compare two independent architectures for one deterministic time formula F_n, n=2..47 (FW₄ stays the test field). The chair's derivations below are PROOF CANDIDATES needing non-author review; neither route has a proved general guarantee. General F_n still UNFINISHED.
''','############ PART 0 · 你的任务 ############\n'+TASK[key]+'\n\n'+STATUS+'\n\n'+LEMMA+'\n\n'+FACT+'\n',
    '############ PART 1 · 主席 R030 转向信（原文）############\n'+CH,
    '############ PART 2 · R029 主席任务书（原文，FW₄ 测试场背景）############\n'+R29,
    '############ PART 3 · T4 原式（已认证）############\n'+T4,
    FMT.format(n=n,seat=seat)+'===== END =====\n']
    txt='\n'.join(p); fn=f'pkg/send_030_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode()))
