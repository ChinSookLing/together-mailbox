import hashlib
R17='/workspace/work/mb008/PT008/round-017/'
def sha(b): return hashlib.sha256(b).hexdigest()
ruling=open('chair/ruling017.txt','rb').read()
s17=open(R17+'send_017_B_Qwen.txt',encoding='utf8').read().split('\n')
inv='\n'.join(s17[418:712])   # Part 2..2D
rd=lambda n: open(R17+'replies/'+n,'rb').read()
opus=rd('2026-10-19T1716-reply-Opus-R017.txt'); argon=rd('2026-10-19T1719-reply-Argon-R017.txt')
ds=rd('2026-10-19T1720-reply-DeepSeek-R017.txt'); qwen=rd('2026-10-19T1722-reply-Qwen-R017.txt')
qwen1=rd('2026-10-19T1724-reply-Qwen-R017-FIRST-VERSION-supplement.txt')
qnote=open(R17+'hesper/2026-10-19T1740-Hesper-note-Qwen-R017-first-version.md','rb').read()
WARN='''############ ⚠ 先读 · CLR 原版已被否定（主席 R017 反例；Hesper 精确分数复核 CHECKED）############
Opus R017 的 CLR（Cluster Ladder）原文周期条件只有 Qθ0/m∈ℤ、Qw0/m∈ℤ；缺少 c 的相位周期 Q(1−θ0)/m∈ℤ，等价于补上 Q/m∈ℤ。不得再引用原版周期条件。
反例：m=2，Q=7，θ0=2/7，w0=6/7，R={4}。原两项周期条件成立（Qθ0/m=1，Qw0/m=3），但 Q/m=7/2∉ℤ。参考 k=4（τ=2）三位簇距离 (3/7,3/7,2/7)，余量为正。
速度 (a,b,c,d)=(7/20,2,5,6)：s=20，θ=2/7，w=6/7；G=7，s≥5G/(3m)=35/6 成立。原规则 k0=⌈ms/5⌉=8，k=11，τ=11/2，t=11/14。
距离：a 11/40，b 3/7，c ‖55/14‖=1/14<1/5 ✗，d 2/7。原 CLR 结论失败。
V4（m=1,Q=9）与 V5（m=4,Q=12）满足 Q/m∈ℤ，两个实例仍有效。裁决：CLR 原版 DISPROVED；补上 Q/m∈ℤ 的 CLR v2 = PROOF CANDIDATE，待独立审阅。
（Hesper 另测：300 个随机有理参考形状满足三项周期条件，R 取全部严格安全余数、余量取 R 上最小值，17,971 点 0 失败——仅查错，不是证明。）
'''
P2E='''############ PART 2E · R017 账本（主席 R017 裁决，2026-10-19）############
新认证 PROVED（PT-008 内部认证，严格限于原始假设）：
- Qwen Q-B2：3/2≤c/b≤9，(b+c)/a≤10，3/5≤d/(b+c)≤9/10 ⇒ t=2/(b+c)。仅限原充分条件。
- Opus TE-AL / TE-AU（一个条目）：对所有 u∈{b,c,d}，u/a∈∪_{m≥0}[5m+1,5m+4] ⇒ t=1/(5a)；对所有 u，u/a∈∪_{m≥0}[(5m+1)/4,(5m+4)/4] ⇒ t=4/(5a)。
- Opus a-never-active obstruction：若某 u∈{b,c,d} 有 u/a∈5ℤ，则 a 的全部边沿时间 (j+1/5)/a、(j+4/5)/a 均失败（不否定存在性）。
- Opus LE（结构定理）：S={t>0: min‖vt‖≥δ} 非空时，每个分量为紧区间 [α,β]，α>0；α=(j+δ)/v（某 v 下沿活跃），β=(j′+1−δ)/u（某 u 上沿活跃）。
- Opus LE-1：孤立成功点 t* 必为 k/(u+v)，u≠v，v 下沿、u 上沿活跃。仅为必要刻画；不得改写为「任意一对相反边缘相交即得成功时间」。
DISPROVED：Opus CLR 原版（见最前「先读」）；Qwen R017 第一版的 q 步 k 选择规则（Hesper：V4 形状 S=20..399 共 44 个失败，全为 k0≡8 mod 9；例 (1,130/3,260/3,1040/9) 有解 t=29/130，但窗口 k=26,27,28 无解）。
PROOF CANDIDATE：CLR v2（补 Q/m∈ℤ）；Opus 「换锚=换相位格」；Argon C4（仅限明确定义的菜单类；快锚上界论证待补，例如单跑者快锚上界须用 (Kmax+4/5)/b 一类界，不能直接套双跑者的 M/(…)；不得推出「所有有限公式不可能」）；DeepSeek CL(n) 簇锁充分条件（非递推）。
充分性主席直接核对通过（覆盖新颖性未确立）：Opus B4⁺ ——31/4≤b/a≤31，61/31≤c/b≤64/31，81/31≤d/b≤84/31 ⇒ t=31/(5b)。「整个 B4⁺ 相对已认证规则均为新覆盖」：仅作者逐规则证明，待非作者审阅。
正确代数刻画：Qwen Q-FSR —— 固定正整数 k，t=k/(b+c) 成功 ⟺ ‖kθ‖≥1/5、‖kw‖≥1/5、‖k/s‖≥1/5；第三项 ⟺ ∃整数 j≥0：5k/(5j+4)≤s≤5k/(5j+1)。未给出对所有实数速度有效的确定性 k 选择。
其他 R017 记录：DeepSeek R20 证明（Hesper 20,000 点 0 失败；R20⊂NF-20）；DeepSeek 单侧窗口分类（下-下：右窗口；上-上：左窗口；下-上：无单侧窗口）与 LE/LE-1 一致；Argon NF-20 证明重述，覆盖差集 UNFINISHED。
任意五跑者 F5：UNFINISHED。不批准上墙。
'''
P3C='''############ PART 3C · 见证点当前状态（Hesper 精确分数复核）############
V1=(1,11/10,3,41/10)：SLN1 内部 PROVED；ETS 两步 t=2/5。
V2=(1,2,3,9/2)：Q-B2 / TE-AU（均已 PROVED）；t=2/5 距离 2/5,1/5,1/5,1/5。
V3=(1,3,4,7)：TE-AL（PROVED），t=1/5（距离 1/5,2/5,1/5,2/5）。
V4=(1,30,60,80)：B4⁺ t=31/150；NF-20/R20 t=2/9；CLR(V4 形状 m=1,Q=9,R={4,5}) τ=22，t=11/45（距离 11/45,1/3,1/3,4/9）。
V5=(1,5/2,5,15/2)：b+c=d；CLR(m=4,Q=12,R={3,9}) τ=9/4，t=3/10（距离 3/10,1/4,1/2,1/4）。
CLR 反例 (7/20,2,5,6)：原 CLR 给 t=11/14，‖ct‖=1/14 失败。
'''
FMT='''############ PART 4 · 回复格式 ############
先写 ANSWER BLOCK（≤300 中文字）。然后：精确定理陈述（严格/非严格）、证明或反例、适用边界、剩余缺口。
四个账本栏分开写：PROOF VALIDITY / INDEPENDENT REVIEW / NEW COVERAGE / COMPUTATIONAL CHECK。状态词只用：PROVED / PROOF CANDIDATE / CHECKED / DISPROVED / IDEA / UNFINISHED。审阅结论每项单独给：PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED。
Any number you report must come from your own calculation in this reply (code or hand work shown). If you did not compute it, write UNFINISHED — do not estimate or invent numbers.
WEB OFF。先手证；代码只可核对，不可替代论证。作者不能审自己的结果。新覆盖若无法穷尽符号比较，写 NEW COVERAGE UNFINISHED。没有证明出一般机制就写 UNFINISHED。
'''
RQ='研究问题（全体）：决定性的不是再找一个成功例子，而是一个依赖速度、确定性的选择机制——选相位或锚点并保证成功。检验「相位格」视角能否连接不同簇形状而不需要无界试探。证不出就写 UNFINISHED。'
seats={
'A_Opus':dict(seat='Opus',where='Tuzi 的 claude.ai（Opus）对话；或经 mailbox 由 Opus 自取',track='Priority 1 · CLR Repair',
 tasks=['写出 CLR v2：完整周期假设（Qθ0/m、Qw0/m、Q/m 均为整数，或等价陈述）。从第一原理证明余数表定理。逐项检查：单余数情形（|R|=1，G=Q）、端点、有限间隔界 G、三个簇坐标 b、c、d 各自的相位与余量。',
        '说明参考周期性能否换成只对「所选余数」的较弱条件而不破坏证明；能则精确陈述并证明，不能则给出反例或说明原因。',
        '提交修正后的定理，不是为原陈述整体辩护。'],
 rev=[('你自己的 Opus R017 回复全文（CLR 原版、B4⁺）',opus)]),
'B_Qwen':dict(seat='Qwen',where='Qwen 新对话「PT-008 Qwen R018」（Play CF 项目内，Qwen3.8-Max，Thinking 开，联网关）',track='Priority 3 · Selecting the Phase',
 tasks=['以 Q-FSR 作为固定 k 的精确条件（已被主席接受）。寻找超越特殊有理簇形状的确定性相位选择规则。',
        '处理你第一版 q 步规则的失败（Hesper 反例见 Part 2E 与 Part 3）：θ、w 都是有理数时，任何周期论证必须同时照顾两者。',
        '研究相位规则能否用代数式表达，而不只是递增扫描整数。',
        '无理形状：给出严格的存在性或障碍分析；不得假设「某一维相位稠密」就推出所有坐标同时安全。'],
 rev=[('你自己的 Qwen R017 正式回复全文（Q-FSR）',qwen),('你自己的 Qwen R017 第一版（被撤回的 q 步规则）',qwen1),('Hesper 对第一版的核对信（反例）',qnote),('Opus R017 回复全文（CLR 原版，供参考；周期条件已被否定，见最前）',opus)]),
'C_Argon':dict(seat='Argon',where='Gemini 新对话「PT-008 Argon R018」（3.1 Pro，High，Personal Intelligence 关）',track='Priority 4 · Restricted Menu Obstruction',
 tasks=['为明确定义的菜单类完成 C4 的修正证明。逐个锚类型分别检查（a 的单跑者边沿锚；b、c、d 的单跑者边沿锚；每一对双跑者锁相锚），写出涉及 M 与 Kmax 的精确界。主席指出：单跑者快锚的上界不能直接用双跑者的界。',
        '寻找 CLR v2（补上 Q/m∈ℤ）的反例，或证明先前缺陷已修复。',
        '不得把受限有限菜单障碍推广为「所有有限公式都不可能」。'],
 rev=[('你自己的 Argon R017 回复全文（C4、NF-20）',argon),('Opus R017 回复全文（CLR 原版；周期条件缺陷见最前）',opus)]),
'D_DeepSeek':dict(seat='DeepSeek',where='DeepSeek 新对话「PT-008 DeepSeek R018」（DeepThink 开，联网关）',track='Priority 2 · Independent Adversarial Review',
 tasks=['独立核验主席的 CLR 反例（最前「先读」）。',
        '审阅修正后的 CLR v2（补 Q/m∈ℤ）：间隔界 G、稳定半径 μ/τ、三个簇坐标。（Opus 的 CLR v2 文本本轮同时写作；你先按「原版 + 补 Q/m∈ℤ」审，Opus 的 v2 收到后另行转交。）',
        '审阅 B4⁺ 的充分性，以及作者「与全部已认证区域完全不重叠」的主张（逐条核对 Part 2–2E 的已认证构造）。',
        '数学有效性与覆盖新颖性分开写。'],
 rev=[('Opus R017 回复全文（CLR 原版、B4⁺ 及其覆盖排除证明）',opus)]),
}
for k,s in seats.items():
  parts=[f'【{i+1}】{t}' for i,t in enumerate(s['tasks'])]+[f'【{len(s["tasks"])+1}】{RQ}']
  out=f'''WHO（给谁）：{s['seat']} —— PT-008 Round 018 · Repair the Ladder · {s['track']}
WHERE（贴到哪）：{s['where']}
REPLY（回复贴回哪）：Hesper 的对话（整段原样贴回，开头写「R018 {s['seat']}」）。
下面从「===== BEGIN」下一行复制到「===== END」上一行。
===== BEGIN =====
Hesper: PT-008 Round 018 · Repair the Ladder · {s['track']}, for {s['seat']}.
TO: {s['seat']}
ASK: read the ⚠ block first, then do the items in Part 0 in order. Reply in this chat; the reply is archived verbatim. WEB OFF（不联网）。Courier: Hesper (acting courier for PT-008 until 2026-10-23); the courier promotes nothing.
THIS ROUND SERVES PROOF STEP: make every rung of the cluster ladder sound (CLR v2), then find a speed-dependent deterministic phase/anchor selection mechanism (unrestricted F5 still UNFINISHED).

{WARN}
############ PART 0 · 你的任务（{s['track']}）############
''' + '\n'.join(parts) + f'''

############ PART 1 · 主席 R017 裁决与 R018 原文（逐字，Tuzi 2026-10-19 18:23 转贴，sha256 {sha(ruling)}；注：转贴时中文段部分行内公式丢失，英文段 R018 原文完整）############
{ruling.decode()}

{inv}

{P2E}
'''
  for title,b in s['rev']:
    out+=f'''############ PART 3 · 原文：{title}（字节级原文，sha256 {sha(b)}）############
{b.decode()}

'''
  out+=P3C+'\n'+FMT+'===== END =====\n'
  open(f'pkg/send_018_{k}.txt','w',encoding='utf8').write(out); print(k,len(out.encode()),sha(out.encode()))
open('R017-INTERNAL-PROOF-LEDGER.md','w',encoding='utf8').write(f'''# PT-008 R017 Internal Proof Ledger (recorded by Hesper from chair ruling, sha256 {sha(ruling)})
Round status: R017 CLOSED — PARTIAL · FIVE PRIOR CANDIDATES CERTIFIED · B4⁺ SUFFICIENCY CHECKED · CLR CORRECTION REQUIRED. F5 UNFINISHED. No wall publication.

| Item | Author | Proof validity | Independent review | New coverage | Computation |
|---|---|---|---|---|---|
| Q-B2 | Qwen | PROVED (orig. sufficient condition only) | Opus + DeepSeek VERIFIED | — | CHECKED |
| TE-AL / TE-AU | Opus | PROVED | Qwen + Argon VERIFIED | — | — |
| a-never-active obstruction | Opus | PROVED | Argon + Qwen VERIFIED | n/a | CHECKED (V4) |
| LE | Opus | PROVED (structure theorem) | DeepSeek + Qwen VERIFIED | n/a | — |
| LE-1 | Opus | PROVED — necessary characterisation only | DeepSeek + Qwen VERIFIED | n/a | — |
| CLR (original) | Opus | DISPROVED (missing Q/m∈ℤ; chair cex (7/20,2,5,6), t=11/14, ‖ct‖=1/14) | chair | — | cex CHECKED (Hesper) |
| CLR v2 (+Q/m∈ℤ) | Opus | PROOF CANDIDATE | pending | UNFINISHED | random 17,971 pts 0 fail (Hesper, debug only) |
| Anchor = phase lattice | Opus | PROOF CANDIDATE | — | n/a | V5 CHECKED |
| B4⁺ t=31/(5b) | Opus | sufficiency CHECKED by chair | non-author review of novelty pending | author proof only | 20k pts 0 fail |
| Q-FSR (fixed k exact) | Qwen | correct algebraic characterisation | chair | — | CHECKED |
| Qwen v1 q-step k rule | Qwen | DISPROVED (44 fails, k0≡8 mod 9) | — | — | CHECKED (Hesper) |
| C4 restricted menu | Argon | PROOF CANDIDATE, stated menu class only; fast-anchor bound to be completed | — | n/a | 3 menus CHECKED |
| CL(n) cluster lock | DeepSeek | PROOF CANDIDATE (sufficient, not recursive) | — | — | — |
| R20 | DeepSeek | ⊂ NF-20 | — | UNFINISHED | 20k pts 0 fail |
| Unrestricted F5 | — | UNFINISHED | — | — | — |

R018 "Repair the Ladder" OPEN: Opus CLR v2; DeepSeek adversarial review (chair cex, CLR v2, B4⁺ + novelty); Qwen phase selection; Argon C4 + attack CLR v2. Replies "R018 n/4".
''')
