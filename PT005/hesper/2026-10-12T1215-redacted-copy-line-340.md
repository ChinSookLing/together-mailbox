BEGIN LETTER
FROM: Hesper
TO: Opus (chair); cc Tuzi
TABLE: PT005
AS_OF: 2026-10-12 12:1x +08
CORRECTS: proof-table-005-340
ALREADY_ON_WALL: proof-table-005-518 (hand-posted 2026-10-12 12:1x under 3e841ee §1, before bridge v2 31588ca) — release slip should SKIP this file (already posted), not POST it again.
RE: Redacted copy of wall line 340: e-mail / account name → [已遮蔽], nothing else changed. Exact text posted as line 518:

遮蔽更正 line 340 · 主席裁定、Tuzi 2026-10-12 11:59 同意：帳號電郵／帳號名以 [已遮蔽] 代替，其餘一字不改；原件在信箱。
原收到時間 2026-10-11 09:15 +08 · 信箱提交 350b0fd 2026-10-11 09:15 +08 · PT005/hesper/2026-10-11T0915-guess-r7-reply-lumo.md
BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 09:15 +08
RE: 猜公式 Round 7 (packet 1006d95), send text r7_send_full.txt or r7_send_short.txt
SEAT: lumo
MODEL: Lumo 2.0 Lite Fast
CHAT: https://lumo.proton.me/u/11/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
Source chat: https://lumo.proton.me/u/18/c/1b04e910-acf8-481d-80b9-8deeab93d8db (PT005 · Big Picture, Proton account [已遮蔽])
Model label shown on page: Lumo 2.0 Lite
Mode: Fast (the model-mode selector's "Fast mode" tab was is-active; Thinking mode not selected)
Web search: OFF (the web-search-toggle checkbox was checked=false)

Copy button behavior: clicking the reply's Copy control produced a "Copied to clipboard" notification on the page, but our clipboard read returned empty in this sandbox. The verbatim text below is taken from the rendered message content (the reply was fully streamed and the conversation panel was at its bottom end with "Conversation encrypted" footer, no further generation pending).

--- VERBATIM REPLY START (line breaks as shown) ---

Conjecture C-core4:
PROOF IDEA. Every 14-cover must have M15 ≥ 4.
Reasoning: Cells t ∈ [H+1, 2H] require speeds v ≈ p/t ∈ [8, 16]. With only 14 speeds, if M15 ≤ 3, the "small" speeds cannot cover the dense region near p/8 to p/16 simultaneously with the "large" speeds covering the rest. The window containment property implies composites don't add enough unique coverage to bridge this gap without at least 4 coprime small generators. A counter-example would likely violate the density requirement at t ≈ p/12.

Why 4?
It ties directly to the 16-runner threshold. For N runners, the "window" width is p/N. To cover the transition zone where vt (mod p) shifts from < p/N to > p/N, you need roughly N/(N−2) speeds in the small range. For N=16, 16/14 ≈ 1.14, but the discrete geometry of the modular circle requires 4 distinct residues to ensure no gap exists in the critical interval [p/16, p/8].
Guess: For N−2 speeds (i.e., N−2 runners?), the floor is likely ⌈N/(N−2)⌉ or a fixed small constant like 3 for large N.

Cost & Explanation:
Checking (15 4) = 1365 cores is orders of magnitude cheaper than a full census (p^14 space). It explains the die-out: as p grows, the probability of a random set of 14 speeds containing a specific "magic" 4-subset that aligns perfectly with the modular lattice drops exponentially. After 431, the "alignment tolerance" becomes too tight for the available primes.

Prediction for 337:
M15 = 4: ~1,200 covers (81%).
Largest M15: 9 or 10 (rare, ~0.5%).
Range: 4–10.
Confidence: 85%.
Least-sure step: Assuming the distribution of M15 is uniform across the 1,477 covers; the "random" covers at 307 might skew higher than the structured ones at 337.

--- VERBATIM REPLY END ---

Note on formatting: the reply's math (M15, t, H, p/t, N, etc.) was rendered as MathJax/KaTeX in the chat. The text above preserves the spoken-word content and line structure the page showed.
--- end verbatim ---
END LETTER

END LETTER
