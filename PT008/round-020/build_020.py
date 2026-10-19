import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
R='/workspace/work/mb008/PT008/'
rul=open('chair/2026-10-20T0609-chair-ruling-R019-and-R020-text-via-Tuzi.txt',encoding='utf8').read()
def cut(a,b): i=rul.index(a); return rul[i:rul.index(b,i+len(a))]
r20=rul[rul.index('PT-008 · Round 020 · The Selection Gate'):rul.index('ROUND 020 OPEN.')+len('ROUND 020 OPEN.')]
ruling=rul[:rul.index('四、Round 020')]
rd=lambda p:open(R+p,encoding='utf8').read()
opus19=rd('round-019/replies/2026-10-19T1919-reply-Opus-R019.txt')
qwen19=rd('round-019/replies/2026-10-19T1929-reply-Qwen-R019.txt')
opus18=rd('round-018/replies/2026-10-19T1832-reply-Opus-R018.txt')
pri=r20[r20.index('Priority 1 — Independent Reviews'):r20.index('Track A —')]
req=r20[r20.index('Required Mathematical Output'):]
def tr(name):
    a=r20.index(name); nxt=[r20.find(x,a+5) for x in ('Track A —','Track B —','Track C —','Track D —','Required Mathematical Output')]
    return r20[a:min(x for x in nxt if x>a)]
REV={'Opus':'Q-ERC1（第一审）、Q-ERC2（第二审）——原文见 PART 3（Qwen R019）。',
 'Qwen':'Opus LS（第一审）、Opus PS 与 APS（第二审）——原文见 PART 2（Opus R019）。',
 'DeepSeek':'Opus PS 与 APS（第一审）、Opus LS（第二审）、Q-ERC2（第一审）、Q-ERC1（第二审）——原文见 PART 2、PART 3。',
 'Argon':None}
NOTE_Q='Hesper 注：Qwen R019 的存档原文在「分母上界」讨论中途截断（贴回时即如此，SHA 5b69ec44…）。PART 3 是存档的全部内容；凡定义或证明不在其中的部分，审阅请写 UNFINISHED，不要替作者补全。'
TRACK={'A':('Opus','1/4','Track A — Opus: Selection Gate','Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取'),
'B':('Qwen','2/4','Track B — Qwen: Empty Sets and Phase Switching','Qwen 新对话「PT-008 Qwen R020」（Play CF 项目，3.8-Max thinking，web 关）'),
'C':('Argon','3/4','Track C — Argon: Focused Adversarial Review','Gemini 新对话「PT-008 Argon R020」（3.1 Pro，High，Personal Intelligence 关）'),
'D':('DeepSeek','4/4','Track D — DeepSeek: Effective Constructivity','DeepSeek 新对话「PT-008 DeepSeek R020」（深度思考开，联网关）')}
FMT='''############ 回复格式 ############
第一行写「R020 {n} {seat}」。先写 ANSWER BLOCK（≤300 中文字）。然后按主席「Required Mathematical Output」六项写：假设、所选相位格与时间、选择器有定义且终止的证明、每位跑者安全的证明、反例搜索或符号障碍、与已认证构造的差别。
{rev}四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / IDEA / UNFINISHED。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能升级自己的结果；只有主席裁决。无界搜索不得当作封闭选择规则。随机测试不能推出证明。
提前告知（主席北极星，2026-10-19）：从 R021 起，每条研究路线都必须说明如何通向一般 n（一个确定性 F_n，n=2…47）。R020 可选写一行。
'''
for key,(seat,n,tname,where) in TRACK.items():
    rev=REV[seat]
    p=[f'''WHO（给谁）：{seat} —— PT-008 Round 020 · The Selection Gate · {tname}
WHERE（贴到哪）：{where}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R020 {n} {seat}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 020 · The Selection Gate, for {seat}.
TO: {seat}
ASK: do YOUR track (Part 0){' and YOUR independent reviews' if rev else ''} only. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: how to decide, from the speed data alone, a phase lattice that is guaranteed to succeed (a selector, not a search). Unrestricted F5 still UNFINISHED.
''','############ PART 0 · 你的任务（主席原文）############\n'+tr(tname)]
    if rev: p.append('你的独立审阅任务（主席分配）：'+rev+'\n审阅须回答：结论究竟是什么？证明有没有依赖未声明的存在性假设？它是否真的比既有 CLR v2 多解决了一种情况？并明确区分：已证充分条件 / 条件性选择器 / 需非空安全集的选择器 / 真正普适的选择规则。Hesper 已完成大量精确分数测试，不必重复同规模扫描；优先符号审查。\n\n'+pri)
    else: p.append('Hesper 注（按主席指示）：只做一项。从 PART 2（Opus PS/LS/APS）与 PART 3（Qwen Q-ERC1/2）中选你认为最强的一个具体选择断言，检查其假设、周期、间隔界与全部四个坐标的安全条件。不要重复已被判 DISPROVED 的 C-Lat 断言；不做大规模计算。回复宜短（≤1500 字）。若上下文混乱，直接写 UNFINISHED。')
    p.append('############ PART 1 · 主席 R020 共同要求（原文）############\n'+req)
    p.append('############ R019 主席裁决（原文，节选至 R020 开题前）############\n'+ruling)
    if key in 'BCD': p.append('############ PART 2 · Opus R019 原文（PS / LS / APS，原样）############\n'+opus19)
    if key in 'ACD': p.append('############ PART 3 · Qwen R019 原文（Q-ERC1 / Q-ERC2，原样）############\n'+NOTE_Q+'\n\n'+qwen19)
    if key=='B': p.append('############ PART 3 · 你自己的 R019 原文（Q-ERC1 / Q-ERC2，原样；存档在中途截断）############\n'+qwen19)
    if key in 'D': p.append('############ PART 4 · Opus R018 原文（已认证 CLR v2 完整证明，原样）############\n'+opus18)
    p.append(FMT.format(n=n,seat=seat,rev='审阅部分每项单独成节。\n' if rev else '')+'===== END =====\n')
    txt='\n'.join(p); fn=f'pkg/send_020_{key}_{seat}.txt'; open(fn,'w',encoding='utf8').write(txt)
    print(fn,len(txt.encode()),sha(txt.encode()))
