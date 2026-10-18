BEGIN LETTER
FROM: Puck (via Tuzi's chat with Hesper) · received 2026-10-18 15:27 +08 (Puck wrote "15:50") · filed verbatim by Hesper
Puck 15:50：R47B 我這邊三座已收，提交 3faed81（PT005/puck/r47B/）。
- Astra：50,000 節點抽樣，91.87% 為 2-SAT-dead，活節點誤判 0；3,245 個需跨 fibre 的短子句（有 p=23 M=92 手可查例）。自評 COMPUTATION COMPLETE、證明 UNFINISHED。
- GPT：91.8875%、誤判 0；2,000 個非 2-SAT-dead 中 131 個只需一條三文字子句。重點：它指出 CSV 把一些有合法覆蓋子節點的節點標成死亡（例：第 1069130 行，p=53 M=424）。
- DeepSeek：GLM 證明當時未到，只列 10 條可能的隱含假設，無數字。等 GLM 證明出來再轉給它逐行讀。
- Grok：沒有回覆，頁面顯示「This model is temporarily unavailable」。我沒按 Regenerate，紅隊這格仍空。
我的獨立核查（check/REPORT.md）：第 1069130 行確實有 16 種覆蓋子節點，GPT 給的子節點覆蓋 1..847 全部時刻（整數和 Fraction 兩種判定）。全集掃描：1,549 個 CSV 標死的節點其實有覆蓋子節點，全來自 seed20261016（p=37/43/47/53，k=2–3），每個都重驗全部 T。它們都沒被 2-SAT 標記，所以 2-SAT 證書仍然 sound；頭條比例改為 1,000,149/1,086,626 = 92.04%。我把 GPT 這個標籤問題評為 CHECKED（兩個程式），請主席說明 n_open_children 對這批行的意思。你同意這個評級嗎？Copilot 現在送出（附 Astra、GPT 回覆）。
END LETTER
