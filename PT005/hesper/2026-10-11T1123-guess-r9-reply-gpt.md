BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 11:24 +08
RE: 猜公式 Round 9 (packet ec15a2d), send text r9_send_full.txt or r9_send_short.txt
SEAT: gpt
MODEL: GPT-6.1 Sol Max, web off, worked 13m 20s (see courier note re split first send)
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ac9c0b6-9ffc-83ec-a1ee-b11795796df5

--- reply verbatim ---
[Courier note (Hesper): The first paste split into several bubbles; GPT saw only a truncated Q2/Q3 fragment and replied (27 s) with Q3 = 701 (620–850, 60%) / 787 (680–1000, 55%), then acknowledged the scoring fragments. The full packet was then sent as one message; the reply below (worked 13m 20s) is to the full packet and explicitly revises 701/787 → 757/877. N=22/24 were not computed in either. Text below was assembled by the browser from the page in order (ANSWER BLOCK, then reasoning paragraphs); interim progress notes streamed between tool calls are omitted. Witness sets re-checked by Hesper: all 8 PASS.]

答案區塊（ANSWER BLOCK）

[IDEA／FACT] Q1：二常數模型 P̂(N) = 8.371864(N − 2)^1.503189。對16、17、18、20的現有末次找到值，誤差依次為 −14.75、+11.58、+17.56、−15.74；均方根誤差（RMSE）15.06。

[FACT] Q2：N = 8 … 15 的已證下界依次為 113、127、131、157、229、251、281、281。8在199以內、9在251以內已窮舉；其餘只報搜尋下界，均未證全域 P*。

[IDEA] Q3：按評分的觀測死亡線（observed death line）：22→757，範圍620–850，信心60%；24→877，範圍680–1000，信心55%。

[PROOF／IDEA] Q4：存在散落倖存者的過渡區。641與661皆為 1 mod 20，故此餘數條件不足；661的具體速度機制仍 UNFINISHED。

[FACT] 擬合使用457、479、523、661作代理值（proxy），最小化對數平方誤差。它們是現有最大找到值，尚非已證的全域 P*；上述誤差只對這四個代理值而言。 [IDEA] 計數模型給出隱式候選方程 log(nC(N−2)) − log n − κ·n·e^(−(N−2)H/n) ≈ 0。固定 κ 的理想化漸近反而接近線性增長；我不能從它推出 3/2 次冪。這條幂律是經驗擬合，沒有證明地位。

[FACT] 以下速度組全部依原始整數不等式逐格驗證，直接證明相應下界。N / 質數下界 / 覆蓋速度組：8 / 113 / {1,3,4,5,50,53}；9 / 127 / {1,8,32,39,40,48,56}；10 / 131 / {1,8,11,15,28,38,39,54}；11 / 157 / {1,28,29,42,59,70,75,76,77}；12 / 229 / {1,7,8,9,10,11,19,68,90,106}；13 / 251 / {1,4,9,55,62,111,114,119,120,122,123}；14 / 281 / {1,30,51,71,72,73,86,91,103,106,107,123}；15 / 281 / {1,9,10,11,12,13,14,17,23,35,99,104,106}。

[PROOF／FACT] 完整回溯先縮放使 1 屬於 S，再對未覆蓋格的所有可覆蓋速度分支；剪枝使用剩餘覆蓋量的上界。無逾時地判定全部相關質數，得到 max{p≤199：8跑者有覆蓋} = 113，max{p≤251：9跑者有覆蓋} = 127。其餘搜尋的逾時結果均保留為 UNFINISHED。

[FACT] 非單調性已有完整判定的例子：N = 8 在47無覆蓋，53卻有。至於641、653，資料包只說限時未找到，不能稱為已證無覆蓋。

[FACT] 晚存活可以來自精確的視窗互補。113的核心 {1,3,4,5} 剩下 R = {15,16,17,18,19,32,49,50,51,52}。速度50覆蓋其中 {16,18,50,52}，53覆蓋其餘六格，正好補完。

[IDEA] 這種短整數比與模算術視窗對齊，是平滑容量模型漏掉的結構；但不能據此斷言661也靠同一構造。

[IDEA] 最不確定的一步：將現有找到值與150秒搜尋的可見性，外推到22、24的觀測死亡線。

--- end verbatim ---
END LETTER
