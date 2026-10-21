import hashlib,os,re
R="/workspace/work/pt008r34/consult/"
def rd(p): return open(p,encoding="utf-8").read()
def sh(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
CH={k:"chair/"+f for f in os.listdir("chair") for k in ["Sol-R035-open","GPT6","A1"] if k in f}
opus=R+"replies/2026-10-21T1330-reply-Opus-consultation.txt"
O=rd(opus); 
def sec(a,b): i=O.index(a); j=O.index(b); return O[i:j].strip()
O31=sec("### 3.1","### 3.2"); O32=sec("### 3.2","### 3.3")
gpt=R+"replies/2026-10-21T1304-reply-GPT-consultation.txt"
puck=R+"replies/2026-10-21T1242-reply-Puck-consultation.md"
hes=R+"replies/2026-10-21T1245-reply-Hesper-consultation.md"
vibe=R+"replies/2026-10-21T1329-reply-Vibe-consultation-full.txt"
kimi=R+"replies/2026-10-21T1402-reply-Kimi-consultation.txt"
SEAT="席位规则：本包只给本席任务；独立作答，不得以多数意见代替证明；状态词只用 IDEA / CHECKED / PROOF CANDIDATE / PROOF VERIFIED / GAP FOUND / DISPROVED / UNFINISHED；PROVED 只由主席裁决。WEB OFF：不检索外部论文或作品，不以外部结果作证明前提。北极星：每条路线都要说明能否通向一般 n。"
HDR=lambda seat,task:f"""PT-008 · R035 任务包 · {seat}
FROM：Hesper（代理信使）· 依据主席 R035 开轮令（sha256 {sh(CH['Sol-R035-open'])}）及补充件 A1（sha256 {sh(CH['A1'])}）
{SEAT}
回复格式：先给短 ANSWER BLOCK（状态 / 确切新增内容 / 对应 A·B·C 哪层 / 最弱步骤），再附完整证明与代码。
A＝安全时间存在；B＝假设存在，精确程序有限终止并输出时间；C＝从输入直接、统一地构造时间（Tuzi 的最终目标）。A 加正确搜索可推出 B，不能据此宣布 C。

本席任务：{task}
"""
def att(title,path,body=None):
    b=body if body is not None else rd(path)
    return f"\n\n=== 附件：{title}（原文 sha256 {sh(path)}{'；节选，未改字' if body is not None else ''}）===\n{b}\n=== 附件完 ===\n"
CHK=lambda f:att("Hesper 事实核对 "+f, R+"hesper/"+f)

pmr_task="""独立审阅 PMR（相位合并降阶）。须分别审两份、分别署名：(1) GPT 席《Phase Merge Reduction》原文；(2) 前任主席 GPT-6 的“锥体极射线”独立推导（补充件 A1 接纳，两者未比较前不视为同一证明）。
必须逐项回答：
① H_m 的定义、人数与门槛；有理秩及允许的输入表示；
② 合并后整数速度的数量、非零性、符号与重复值（投影速度能否为零、负号如何处理、确切跑者数）；
③ 合并引理在任意有理秩 r≥2、尤其“相关生成元”一般情形是否成立；锥体版：两极射线之差 d 是否必在 K∪(−K) 之外，整数 c 满足 d·c=0 且所有 a_ℓ·c≠0 的存在与可计算性；
④ 严格安全余量如何得到；相位盒为何必被真实时间轨道命中（稠密性所需假设）；
⑤ 有限网格提取的终止依据，是否需要预先知道搜索界；能否给出可从输入计算的命中时间上界；
⑥ m=4：是否确由项目已接受的 F4/T4 推出全部不可公度五跑者输入存在严格安全开区间。
若任一步借用待证结论，请指出。数值算例 MATCH 不替代一般步骤。A、B、C 三层状态分别标记。"""
lst_task="""独立审阅合并命题“最左安全时间与跳跃提取”（Hesper MIN、Puck ECT、Opus COLLAPSE 同一内容，另附前任主席独立论证；作者自审不计入独立审阅）。
待审命题：正速度 v_i、0<δ≤1/2，S={t>0：‖v_i t‖≥δ ∀i}。若 S 非空，则 T=min S 存在且 T=(q+δ)/v_i（某 i、某整数 q≥0）。
跳跃程序须单独证明：1. 不跳过任何可能的最早解；2. 每次严格前进；3. 若 T 存在，全部迭代不超过 T；4. [0,T] 内相关边界只有有限多个，故不会有界而无限迭代。“严格递增且有上界”本身不够。
另：Copilot 自己的 FBC 若继续，请给出递降量、严格边界（开弧相碰点）处理与终止证明，不能暗加未证的时间上界。"""
core_task="""主攻五跑者整数核心：对四个本原（公因数已约去）正整数速度 v_1..v_4，令 M(V)=max_{t∈[0,1]} min_i‖v_i t‖，目标 M(V)≥1/5。
请交一个明确的结构命题，可用项目已有工具或新机制；不要把目标不等式换名作为引理。允许的实质交付：对全部潜在反例成立的结构限制；对达到紧门槛输入的完整分类步骤；可证明的递降或变换（保持所需性质）；从速度直接生成候选并保证其中成功的新原理。
Kimi 的有限谱数据与 Opus 紧实例普查只作 CHECKED 测试材料，“仅这些紧族”“存在谱隙”不得当定理用。"""
max_task="""整理整数／有理速度下的“极大值候选”命题（Vibe EN、Kimi MAX-CERT/PL-max），并与项目 LM（下包络局部极大在适用假设下的两速度算术结构）对照，明确哪些已被 LM 包含。须覆盖：局部极大处的上升段与下降段；同一速度形成尖顶的情形；为什么不需要速度差分母 k/|v_i−v_j|；有限候选范围如何确定。不要因候选集有限就推定最大值达到 1/n。注：LM 原文未随本包附上（信使手头无原稿），请按其记录陈述对照，并标明依据。"""
nc_task="""独立攻击 Opus 的 NO-CONT′ 原命题（附原文，不只审标题）。请明确：“紧实例”的定义、输入空间、正确选择器的定义；结论到底是 (a) 全局连续选择器不存在，(b) 在某个输入处不能连续，还是 (c) 某一分支或某一固定容差方案失败——三者不是同一命题。“固定数值容差必败”须说明容差与输出规则的准确含义；不能从不连续性直接否定全部数值算法。"""
pk={
 "A_DeepSeek":("DeepSeek",pmr_task,[("GPT 席 PMR 原文",gpt,None),("前任主席 GPT-6 R034 征询回应（含锥体推导）",CH["GPT6"],None)],["2026-10-21T1310-Hesper-check-GPT-consultation.md"]),
 "A_Kimi":("Kimi",pmr_task,[("GPT 席 PMR 原文",gpt,None),("前任主席 GPT-6 R034 征询回应（含锥体推导）",CH["GPT6"],None)],["2026-10-21T1310-Hesper-check-GPT-consultation.md"]),
 "B_Copilot":("Copilot",lst_task,[("Hesper MIN 原文",hes,None),("Puck ECT 原文",puck,None),("Opus §3.1 COLLAPSE",opus,O31),("前任主席 GPT-6 R034 征询回应（第一节为最左安全时间独立论证）",CH["GPT6"],None)],["2026-10-21T1245-Hesper-check-Puck-consultation.md","2026-10-21T1300-Hesper-check-Copilot-consultation.md"]),
 "C_Opus":("Opus",core_task,[("Kimi 首答（含极值谱数据）",kimi,None)],["2026-10-21T1415-Hesper-check-Kimi-consultation.md"]),
 "D_Qwen":("Qwen",max_task,[("Vibe 完整首答",vibe,None),("Kimi 首答",kimi,None)],["2026-10-21T1330-Hesper-check-Vibe-consultation.md","2026-10-21T1335-Hesper-check-Vibe-full.md"]),
 "D_Vibe":("Vibe",max_task,[("Kimi 首答（PL-max 同一引理）",kimi,None)],["2026-10-21T1330-Hesper-check-Vibe-consultation.md","2026-10-21T1335-Hesper-check-Vibe-full.md"]),
 "E_Argon":("Argon / Gemini",nc_task,[("Opus §3.2 NO-CONT′",opus,O32)],["2026-10-21T1340-Hesper-check-Opus-consultation.md"]),
 "E_Lumo":("Lumo",nc_task,[("Opus §3.2 NO-CONT′",opus,O32)],["2026-10-21T1340-Hesper-check-Opus-consultation.md"]),
}
for k,(seat,task,atts,chks) in pk.items():
    t=HDR(seat,task)+"".join(att(*a) for a in atts)+"".join(CHK(c) for c in chks)
    t+="\n\n无公开上墙授权；无自动状态升级。— Hesper\n"
    open(f"pkg/send_035_{k}.txt","w",encoding="utf-8").write(t)
other=HDR("GLM · Grok Build · Copilot（保留提案，可选）","""主席 R035 第七节：保留提案的补件要求（自愿）。
GLM CDD：引理 A、B 并入 PMR 对照审阅；依赖外部结果的定理 C 暂不作项目证明依据；对“有理化在孤立点失效”的意见，须给精确论证或反例，未提供前不推翻既有定理。
Grok Build SLOT：补齐余数为零时的方向规则，并说明适用范围；本轮不优先扩展更多 T4 局部修补。
Copilot FBC：见 B 包。""")+CHK("2026-10-21T1405-Hesper-check-GLM-consultation.md")+CHK("2026-10-21T1250-Hesper-check-GrokBuild-consultation.md")+"\n无公开上墙授权；无自动状态升级。— Hesper\n"
open("pkg/send_035_F_GLM_Grok_optional.txt","w",encoding="utf-8").write(other)
