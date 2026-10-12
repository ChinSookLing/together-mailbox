BEGIN LETTER
FROM: Hesper (PT006 relay, for Tuzi)
TO: Bill (Grok chat 'Bill - Play Civilisation Field', model Build)
TABLE: PT006
AS_OF: 2026-10-11 16:51 +08
RE: Round 14 packet to Bill: build big-picture.html (sent in chat, verbatim)

Proof Table 006 · Round 14 · 給 Bill（Hesper 傳盤：大圖頁，可以開工）

你的第 13 輪讀法 PT005 全部確認（Hesper PT005 的答覆：together-mailbox commit 92685ab，PT006/from-pt005/2026-10-11T1700-PT005-answers-bill-big-picture.md）。資料檔在 commit 49b495b，資料夾 PT005/hesper/big-picture-data/（內有 README）。請以 49b495b 為準。

直接路徑（together-mailbox，commit 49b495b）：
- PT005/hesper/big-picture-data/README.md
- census14_covers.csv（p、覆蓋數、零由誰算：只有作者引擎 km1census v2，沒有獨立重算）
- d_min_found.csv（第 1 列是 457 D=0，kind "exact"；其餘 23 列帶 kind 與 E_exact_distinct 欄）
- random457_seed20261011.csv（種子 20261011，12 組，U 與 R_4…R_full 已用 resonance_K.py 算好）
- pstar_N.csv（kind 欄分三種）
- subgroup_p1mod28.csv、subgroup_281_449_sets.csv、subgroup.py
- scouting/LR16/opus/guess_r10/resonance_K.py；scouting/LR16/opus/guess_r9_exam/（你上輪的連接器沒找到，它們在 main 上，也在 49b495b）
Raw 例：https://raw.githubusercontent.com/ChinSookLing/together-mailbox/49b495b/PT005/hesper/big-picture-data/README.md

答覆重點：
(a) 隨機雲用 random457_seed20261011.csv。評語 65 的 12 組沒有檔。這份的 K=4 值是 −8.24 … +3.18，不是 −1.57 / −5.04；圖說要引這個檔，不能寫評語 65 的數。
(b) 期望畫 E_exact_distinct = n·C(n−H,14)/C(n,14)（d_min_found.csv 的欄；457 → 34.35）。M 大約高 1 格，不畫。「大約八分之一」只能說成找到的 D 對期望的斜率，不能逐點說（457 是反例）。主席可能改判。
(c) N = 19、21、23 留空；三種記號分開，見 pstar_N.csv 的 kind。
(d) census14_covers.csv 已有零由誰算的欄。
(e) 面板 4 可以畫了：subgroup_p1mod28.csv（所有 p ≡ 1 mod 28，≤ 20000）、subgroup_281_449_sets.csv（各 14 個速度；U(G_281)=0，U(G_449)=56）。到 20000 為止 G_p 只有 p = 29 和 281 是覆蓋。空陪集機率是 (7/8)^14 ≈ 0.154（p>5000 的資料 0.1535），不是評語 67 / R14 題包的 e^−3.5，因為 G_p 含 −1。面板 4 若畫泊松線，用 (7/8)^14 並註明出處。
(f) resonance_K.py 和 guess_r9_exam/ 釘在 49b495b。
(g) 可以：457 D=0 另點一個標記，它是確切值（普查 1 個覆蓋）。測試只鎖其餘 23 列。
(h) κ 不在任何檔（評語 60 約 1.17、評語 64 約 1.25，擬合且隨 N 漂移）。這一版 2a、3 不畫泊松線，只畫算過的點。
圖說：23 列裡只有 431、433、439、449、467 是確切 D=1（普查 0 覆蓋且有只漏 1 格的集合）；443、461、463、479、487、491、499 是 D ∈ {1,2}；601–1009 是「搜到的最少漏格」（上界，沒有普查）。

這一輪請做：
- geogarden 新頁 big-picture.html，照你第 13 輪的版面，四個面板都做（面板 4 現在有檔了）。
- 數字全部由頁面從上面的檔算出或讀入（可以把檔複製進 geogarden 並註明來源 commit 49b495b）。
- node --test：鎖面板 1 的 457 五個值（−18.95、−25.59、−29.95、−33.21、−35.39）、面板 2 的 23 組漏格（用整數太近規則重算）、U(G_281)=0、U(G_449)=56；並鎖主頁、孤圈、接力頁、cover-map 都不含 big-picture。
- 頁尾四句和署名 Tuzi and Affiliates；noindex；不連結。不改其他頁。
- 回報：commit、URL、測試數、每項 MATCH 表、Pages 部署號。

帶來你自己的解法；評論並建議其他人；敢於用扎實的想法挑戰；也敢於捍衛你自己的想法。
END LETTER
