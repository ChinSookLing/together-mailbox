SEAT: ASTRA
CARRIED_BY: Puck
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6aceac9d-c250-83ec-a3f3-d6e455dbac54
SENT: 2026-10-18 15:02:26 +0800 (see meta.txt)
COLLECTED: 2026-10-18 ~15:25-15:35 +0800, text read from the page (Copy button did not reach the clipboard); thinking excluded; formulas written once in plain form, tables as | rows, wording unchanged
SEND_TEXT: PT005/puck/r47B/send_R47B_ASTRA.txt
NOTE: thinking High; no Stop/Regenerate. Astra's evidence ZIP/CSV links live in its chat only; not downloaded.
PUCK READ: COMPUTATION COMPLETE, GENERAL PROOF UNFINISHED (seat's own label). 50,000-node sample: 45,122 of 49,114 dead are 2-SAT-dead (91.87%), 0 live flagged; 32,553 shortest certificates use one coordinate; 3,245 nodes need cross-fibre short clauses. Cross-fibre example (p=23 M=92) is hand-checkable. Sample numbers NOT rechecked by Puck.
---
ANSWER BLOCK — PT005 · Round 47 Track B · Astra

FACT — 已完成 50,000 個節點的獨立隨機抽樣及 2-SAT 檢查。 使用 Python random.Random(20261018) 從附件的 1,107,866 行中不放回抽樣。

分類 | 節點數
Dead，且 2-SAT-dead | 45,122
Dead，但非 2-SAT-dead | 3,992
Live，卻 2-SAT-dead | 0
Live，非 2-SAT-dead | 886

FACT — 2-SAT 檢出的死亡比例：
45122 / (45122+3992) = 91.87%.

PROOF — 判定可靠性。 對每個奇數時間 T≤M，以原始模 2M 覆蓋不等式產生子句；只保留至多兩個 literal 的子句，再尋找 b_i 與 ¬b_i 互相可達的矛盾證書。因此每個 2-SAT-dead 判定都是「不存在完全覆蓋子節點」的充分證明。

FACT — 已取得每個 2-SAT-dead 節點的最短矛盾閉合步行（shortest contradictory closed walk），以蘊涵邊數最少為準。

最不確定步驟： 最短證書可能不唯一，選取哪一個最短證書會影響「是否位於單一 fibre」的統計。因此需要把固定選取規則與不受平手影響的結論分開。

最短矛盾證書的分布

FACT — 使用廣度優先搜尋（BFS）找出最短的兩段路徑 b_i→¬b_i 與 ¬b_i→b_i。 兩段合成的閉合步行長度最小；一個子句可能在圖中提供兩條蘊涵邊，所以另行統計證書中的不同時間 T。

數量 | 最短蘊涵邊數 | 不同時間（子句）數 | 不同坐標數
2 | 32,553 | 32,553 | 9,230
3 | 8,970 | 9,081 | 3,080
4 | 2,911 | 3,211 | 192
5 | 150 | 184 | 46
6 | 368 | 63 | 6
7 | 77 | 6 | 2
8 | 61 | 7 | 0
9 | 6 | 1 | 13
10 | 22 | 16 | —
11–13 | 4 | — | —

表中三欄是各自獨立的直方圖，不能橫向理解為同一節點的聯合分布。完整直方圖已另行保存。

FACT — 32,553 個最短證書只涉及一個坐標。 這些就是兩個相反單元子句（unit clauses）構成的最短矛盾，佔全部 2-SAT-dead 節點的 72.14%。

涉及坐標的深度分布

將同一證書涉及的所有坐標深度排序；以下列出最常見的深度組合：

深度組合 (d_i) | 證書數
(2) | 17,965
(3) | 6,802
(1) | 5,997
(2,3) | 3,246
(1,2) | 2,897
(0) | 1,167
(1,2,2) | 1,084
(2,3,3) | 823
(2,4) | 731
(4) | 619
(1,3) | 584

FACT — 跨 fibre 的平手問題已獨立排查。

判定方式 | 位於單一 fibre 的證書 | 比例
固定 BFS 平手規則所選的最短證書 | 37,841 | 83.86%
至少存在一份同樣最短的單 fibre 證書 | 40,837 | 90.50%
不限制長度，至少存在一份單 fibre 矛盾證書 | 41,877 | 92.81%

因此 3,245 個 2-SAT-dead 節點需要跨 fibre 的短子句才能形成矛盾；每個 fibre 單獨看都仍有可滿足的短子句系統。

四、兩種矛盾機制的直接證書
FACT — 單 fibre：Antipodal Singleton

取 p=23, M=92，坐標 w_4=5（從零編號）。

兩個時間：
T=55, T′=37=92−55
同屬 fibre a=9。

直接覆蓋計算產生：
T=55: b_4=1
T′=37: b_4=0.

這兩個單元子句立即矛盾，不涉及其他坐標。

FACT — 真正需要跨 fibre 的矛盾

另一個 p=23, M=92 節點：
W=(1,3,3,8,11,25,26,27,29,30,51,55,55,78,79).

它具有以下四條短子句：

Fibre | 時間 T | 子句
4 | 73 | b_8=1 ∨ b_13=0
4 | 19 | b_8=0 ∨ b_13=0
10 | 79 | b_8=1 ∨ b_13=1
10 | 13 | b_8=0 ∨ b_13=1

PROOF： 前兩條迫使 b_13=0；後兩條迫使 b_13=1。因此不可能同時滿足。

這個節點各個 fibre 單獨的短子句系統均可滿足，只有合併不同 fibre 後才產生矛盾。它說明，證明枝條死亡不能完全局限於逐 fibre 的局部分析。

五、完整計算證據

下載 R47 Track B 完整證據包
C++ 搜尋程式、獨立 Python 驗證器、抽樣資料、完整矛盾證書及所有直方圖

Round 47 技術報告
可供主席審閱的定義、方法、統計與兩份手工可查的矛盾證書

50,000 節點逐行結果 CSV
每條最短證書的時間、坐標、深度、fibre，以及平手排除結果

獨立 2-SAT 搜尋器原始碼
直接從覆蓋不等式生成短子句，並用 BFS 尋找最短矛盾證書

FACT — 交叉復算： 另以獨立 Python 程式抽取 200 個節點，重新檢查子句時間、蘊涵邊合法性及最短路徑長度，結果全部通過。

R47 Track B 最終裁決：COMPUTATION COMPLETE；GENERAL PROOF UNFINISHED。

本輪證據顯示，短子句可以解釋抽樣中 91.87% 的死亡節點；其中大量矛盾極短，而且可以在單一 fibre 內完成。但確實存在必須跨 fibre 才能形成的最短矛盾環。

因此，下一步若要將統計提升為結構定理，除了局部 runner 重疊，還必須刻畫不同 fibre 如何共同限制同一組提升位 b_i。
