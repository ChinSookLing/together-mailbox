BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 16:37 +08
RE: 猜公式 Round 4 part (a) (packet 61862ac), send text r4_send_grok.txt
SEAT: grok
MODEL: Grok Expert (web search cannot be disabled; prompt said no search)
CHAT: https://grok.com/c/762d4637-053d-4337-9070-11e87be90327

--- reply verbatim ---
# Grok Expert — PT005 Round 4 Part (a) — Verbatim Reply (Final)
Chat: https://grok.com/c/762d4637-053d-4337-9070-11e87be90327
Mode shown: Expert (selector label; no underlying model name like "grok-3" was displayed)
Status bar on completion: "Worked for 2m 14s"

VERBATIM REPLY (everything Grok returned as the answer; the three lines at the very end are Grok's own follow-up prompts, NOT part of the answer):

---
ANSWER BLOCK

Q3. 307 (≡3, H=19): rows 4×10⁶–4×10⁷, point 1.3×10⁷; surv. L2 200–1.5×10⁴, point 3×10³; alive L16 = 0, gate closes. Confidence low on the counts, high on the close. 337 (≡1, H=21): rows 1.5×10⁶–6×10⁶, point 3.2×10⁶; surv. L2 100–4×10³, point 700, with {1..15} inside; alive L16 = 0, gate closes. Confidence medium / medium-low / high. 383 (≡15, H=23, γ=15, so (a) only): rows 10⁴–3×10⁵, point 8×10⁴; surv. L2 1–40, point 4, again including {1..15}; alive L16 = 0, gate closes. Confidence low / low / high.

Q1. IDEA: for H≥15, rows(p) ≈ A(p mod 16)·2^{15−H} with A(1)≈2.05×10⁸; FACT: 241/401 = 1030.4 against 2^{10}=1024 (per step 2.001). p≡1 is the rich class, p≡15 the poor one (241/239≈21).

Q2. IDEA: surv. L2 ≈ B(p mod 16)·3.42^{15−H}, B(1)≈1.10×10⁶; FACT: 241/401 = 220900, per step 3.423. The single 409 survivor is the canonical tight row {1..15}.

Q4. IDEA: for large p every irredundant 15-cover is a unit scaling of a 15-subset of {1..15+k}, k=o(H), and past H≈25 the only L2 survivor is {1..15}. Cheap test: rerun the engine on classes ≤30 at 241 or 401 and compare with the full row count.

Q5. Tuzi, the lever on (a) is a tight-cluster lemma, not a faster search: L2 already keeps only scalings of {1..15}, so the 10¹² nodes are the cost of enumerating a set the first lift has shown is empty.

Least-sure step: the residue multiplier for 307 and 383 inside the unmeasured gap H=16–24. UNFINISHED: no training prime with 16≤H≤24, so the decay law is a two-point fit.

Reasoning. FACT: H=⌊(p−1)/16⌋, and each class covers a 1/8-arc, so n/H≈8 is the width budget. FACT: alive L16=0 on every computed gate, including 401 where {1..15} dies only at 16p and the other four L2 survivors die at level 4. That is why all three gates are called closed.

PROOF (arithmetic only): the ≡1 row ratio is 2.001 per H from 241 to 401, not a rounded 2. The survivor ratio is 3.423 per H over the same pair, and 3.423^{10} recovers 5. Both extrapolations above are that pair pushed to H=19, 21, 23. IDEA, not proof: each extra unit of H adds one independent interval-fitting constraint, killing about half the rows and about 3.4 of the L2 survivors.

IDEA: the pre-241 rise (H=6→15, and the ≡1 spikes at 113 and 241) is the loose-window regime, where many 15-subsets of a short initial segment are irredundant covers. The post-241 collapse is that window freezing onto {1..15}. FACT: 401 still has 198,769 rows but only 5 L2 survivors, so the row count lags the survivor count; 409 having 1 survivor is the lag closing. IDEA: that unique row is {1..15}, because the four non-tight 401 survivors are exactly the ones a shifted threshold (409≡9) kills before level 2. The 307 and 383 points are the same law times a residue factor. FACT: at matched H the factor is already 1.6–21 (131/137, 241/239, 401/409). IDEA: ≡3 stays near the ≡1 curve, ≡15 sits 10–20× below. That factor, not the 2-per-H step, is the soft part.

[Grok's own follow-up prompts, not part of the answer:]
Translate to Chinese
What is the 15-cover in the 409 case?
Do the same for Part (b)
---

CAPTURE METHOD NOTE:
- The reply was captured verbatim by reading the completed page.
- While streaming, extract_content(full) truncated the tail because the conversation was too long. The tail was recovered by find_text("401 still has") with context, which returned one continuous span ending at "soft part."
- Completion was verified by find_text("Working for") returning no matches (the live timer vanished) and by the post-completion status "Worked for 2m 14s" in the viewport read.
- The model invoked a code tool once ("Ran command / Compute exact training ratios and extrapolations") to check training-prime ratios before committing the predictions; this is allowed by the packet (code permitted on training primes only). The code panel was collapsed in the UI; its output was not separately requested, and the resulting numbers appear in the answer itself.
- I did not send any message. Grok did not stall, loop, or request anything.
--- end verbatim ---
END LETTER
