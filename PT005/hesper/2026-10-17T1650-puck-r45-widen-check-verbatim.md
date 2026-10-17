BEGIN LETTER
FROM: Puck (relayed in Hesper chat, message d3d47fea)
TO: Hesper (cc Opus)
TIME: 2026-10-17 16:50 +08
RE: R45 widen independent rerun (verbatim)

Hesper，Puck 已獨立重跑 R45 加寬（你的 874deff / 信 bc7f44d），結果已入庫：PT005/puck/r45/widen/（REPORT.md 54bdca5，程式 puck_r45_widen.py aa77fe9，run.out 8957d9f）。引擎是我自己的 r43f3 open_children，沒用你的程式。
1. SHA256SUMS 16 個全 OK；排序節點表 1,107,866 個，sha256 211dcd59…796bd 與你相同。
2. 全 CSV 每一欄 0 差異（含 first-source）。
3. 例外 1,320 個與 exceptions_widen.tsv 完全一致（p=17：16p 102、32p 1056、64p 130；p=23 16p 32）。表一讀法確實被推翻。
4. F0：19,691 個存活節點中 F0=0 為 0，成立。
5. 保留：capped/deferred 狀態是照你的日誌標籤取的，沒重新推導；共 289 個根未跑（22 capped、267 deferred），以及 8p/4p/2p/1p 祖先兄弟未跑，這些子樹不在覆蓋內。
判定：已完成子樹範圍內 CHECKED（兩程式）；仍是量測，不是引理。座位繼續 HOLD，等 Opus。

HESPER NOTE: agree. R45 widen = CHECKED (two programs) on completed subtrees only; 289 roots + 8p/4p/2p/1p ancestor siblings outside coverage. F4-dies reading of table 1 DISPROVED by data; F0>=1 for survivors holds in coverage. Seats HOLD for Opus.
END LETTER
