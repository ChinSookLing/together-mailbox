BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 09:11 +08
RE: 猜公式 Round 7 (packet 1006d95), send text r7_send_full.txt or r7_send_short.txt
SEAT: gpt
MODEL: GPT-6.1 Sol Extra High
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ac9c0b6-9ffc-83ec-a1ee-b11795796df5

--- reply verbatim ---
FINAL STATUS
- Chat: PT005. Big Picture (Sol 6.1) — https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ac9c0b6-9ffc-83ec-a1ee-b11795796df5
- Sent: ~9:03 AM (packet pasted via paste_text, auto-sent)
- Model/effort label rendered by the reply: **GPT-6.1 Sol / Extra High** (user-confirmed override; user explicitly said to keep this setting and record it exactly as shown, overriding the original GPT-5.6 Sol / High requirement)
- Web search: no toggle present in composer → OFF (per prior verification)
- "Worked for" duration: **6m 2s**
- Status indicator: "Response complete"
- The model produced a complete reply in Chinese; no error, no Google sign-in.
- Note on reply behavior: it first streamed a tentative ANSWER BLOCK, ran tool commands (p=281 search + more), then REPLACED the answer block with a revised one reflecting the p=281 counterexample. The text below is the final rendered reply (the second/definitive version).

FULL FINAL REPLY (verbatim, Traditional Chinese as rendered):

答案區塊（ANSWER BLOCK）

[PROOF] Q1：C-core4 不成立。 p=281 有14-cover，且 M15=3；完整速度組與證明如下。這不反駁限定 p≥307 的版本。

**[IDEA] Q2：**4 不是16跑者的普遍底線。暫猜其他閾值的全域底線：N=8 為4，N=10,12,16 為3；信心低。

**[PROOF／IDEA] Q3：**1,365核心的全域歸約失效。條件成立時，直接擴充需 1365·C(n−4,10) 個分支；縮放去重後未必省工。431也不是終止點：457仍有覆蓋。

**[IDEA] Q4：**337的 M15=4 數量預測 100–400，中心220，信心70%；最大 M15 預測 8–10，中心9，信心75%。維持先前鎖定的預測。

[FACT] 反例為 p=281, n=140, H=17：
S={1,10,28,32,34,36,39,53,59,79,100,109,116,124}.
依定義檢查140個時間格，全部被覆蓋；140個縮放的小速數量分布為 1:84, 2:42, 3:14。

[PROOF] 可用乘法子群（multiplicative subgroup）給出短證明。令
C={±v:v∈S}, χ(x)=x^28 (mod 281).
逐項驗算，C 的28個元素皆滿足 x^28=1；因多項式只有至多28個根，C 正是 χ 的核（kernel）。

[FACT] 以下是 1≤r≤17 的完整分組：
χ(r) → r
1 → 1, 10
49 → 11
86 → 7, 8, 9
90 → 2
128 → 3
153 → 5, 14, 16, 17
191 → 12, 13
195 → 15
232 → 4
280 → 6

[PROOF] 任意非零 t 都有 χ(t)^10=1。表中10個不同值已用盡這個方程的全部根，所以總能選到 r≤17，使 χ(r)=χ(t)。於是 r/t∈C，即某個 v∈S 滿足 vt≡±r，證明覆蓋。

[PROOF] 對任意縮放 u，小速 r≤15 出現在 uS 中，恰當且僅當 χ(r)=χ(u)。表中忽略16、17後，每組最多3個；u=7 得到小速 {7,8,9}。因此 M15=3。

[PROOF] 平均公式仍給出有效部分下界：
M15 ≥ ⌈420/(p−1)⌉.
故 p≤139 時至少4，p≤199 時至少3，p≤419 時至少2。

[FACT／IDEA] 對一般 N，取
S_{N,p} = {v ≤ (p−1)/2 : v^{2(N−2)} ≡ 1 (mod p)}.
程式核驗得到覆蓋及核心容量 (N,p,M) = (8,37,4), (10,113,3), (12,101,3)。這支持考察乘法陪集（multiplicative cosets）的占位分布；尚不能推出全域底線。

[PROOF] 四核心直接擴充，在307約需 1.49×10^18 分支，在499約需 2.43×10^20 分支。相對全部14子集，分別少約16.1倍、114.4倍；但這兩個質數的縮放軌道大小都是 n，相對「每軌道一次」的候選數，反而多9.53倍、2.18倍。這些是候選數比較，不能當成引擎耗時預測。

[PROOF／IDEA] 視窗包含不能直接刪除含合數的核心。可令 R 為核心未覆蓋格，計算每個候選速度新增覆蓋量；若最大的10項之和仍小於 |R|，即可剪枝。此方法尚未解釋大質數的覆蓋消失。

**[IDEA] 最不確定的一步：**Q2把少量例子的核心容量外推成其他閾值的全域底線。

---
Hesper check (09:12 +08, python, p=281 only): S has 14 distinct speeds, H=17, uncovered cells = [] (full cover), small-speed counts over 140 scalings {1:84, 2:42, 3:14}, max = 3. Counterexample CONFIRMED for p=281 (below the 307 range; p>=307 version untouched).

--- end verbatim ---
END LETTER
