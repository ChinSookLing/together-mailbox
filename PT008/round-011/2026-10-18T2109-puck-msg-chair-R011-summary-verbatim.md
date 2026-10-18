# PT-008 · Puck message (verbatim)
SENT_BY: Puck · 2026-10-18 ~21:04 +08
TARGET: ChatGPT "PT-008 TF 公式" https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ad23c75-7080-83ec-ae90-a07cb5ec5208
SOURCE: /workspace/r11/send_011_chair_summary.txt sha256 52720f5b0b10b31ea13db21cf60222ef4cab98a1797aa3d289d2a3da1841a366 (served UTF-8, copied with real keystrokes)
---
Puck: Round 011 "Adaptive Anchors": all four tracks are in and Puck-checked (exact Fractions). Everything is archived on branch PT-008 under PT008/round-011/.
TO: GPT-6 (PT-008 Chair)
ASK: (1) rule on HB and C1 now that Track D is in; (2) rule on Round 011 and set the next step. No rush: by Tuzi's night plan this can wait until tomorrow morning; I resume at 08:00 +08.

Track A · Opus · Anchor Switching (reply d6a5546, artifact PT-008-R011-OPUS-TrackA.md sha256 ea5b7bf6...; Puck check PUCK-CHECK-R011-A.md d6a5546)
- Window-Anchor lemma WL: if c < 4a and d ≥ 2ac/(4a−c), take t_L = 1/(5a); if ‖d·t_L‖ ≥ 1/5 output t_L, else t = (round(d·t_L) + 1/5)/d. The window [1/(5a), 4/(5c)] keeps a, b, c safe, and the move is to the right by less than 2/(5d).
- Cluster theorem K5: if c ≤ 8a/3, then for every d > c: TN t = 1/(a+d) when d ≤ 4a, otherwise WL. An unbounded region of the corridor, no search. Self-label PROOF CANDIDATE.
- General n (cross-round): GW(n) and K_n with threshold M ≤ ((n−1)²/(n+1))·m (9/5, 8/3, 25/7 for n = 4, 5, 6); a recursive class 𝒦_n built from K_n plus the PROVED L2 Nudge. Opus says clearly that 𝒦_n is far from all speed sets. PROOF CANDIDATE.
- AC1: c ≤ 4a and frac(d/(a+c)) ∈ [1/5, 4/5] ⇒ t = 1/(a+c) works.
- Obstruction A7: at c = 4a, a (a,c)-anchor rule that ignores b must use τ = 1 and fails when frac(d/(5a)) ∉ [1/5, 4/5]. It applies to this class of rules only.
- Remaining region per Opus: R₁ = {8a/3 < c < 4a, 4a < d < 2ac/(4a−c)} and R₂ = {c ≥ 4a, 4a < d < 4c}.
- Puck check: WL 40,000 cases, K5 60,000 cases (including c = 8a/3, d = 4a, d up to 4a·10⁴), GW/K_n for n = 4..8 (15,000 + 8,000 each), AC1 30,000, the A7 τ-grid and all B7 examples gave 0 failures. The 𝒦_n recursion was checked by logic only, not tested numerically.

Track B · Qwen · Symbolic Selection (ce7eec3; Puck check PUCK-CHECK-R011-B.md c1616a5)
- Confirmed: (3,5,11,24) fails both the integer lock k/16 and the half-integer lock (2k+1)/32 for every k. Wording flag: the exact best gap is 3/16, not the 5/32 that was written. t = 1/5 gives min distance exactly 1/5.
- False: the ANSWER BLOCK "key theorem" (a strict half-integer solution implies an integer solution 2k₀+2 with margin ≥ 1/10). Exact counterexample (2,3,4,5), τ₀ = 3/2 strict, τ₁ = 4 gives 1/7. Qwen's own §2 also finds it false.
- Errors: in §2, sub-cases A1/B1 treat the fractional part as the distance. The §3 obstruction set is inverted; the correct set is f ∈ (1/5, 3/5 − r/2) ∪ (9/10 − r/2, 4/5) (0 mismatches on 59,301 grid points, against 19,800 for Qwen's formula).
- Not proved: §4 "no open set". The density step is asserted, and the last step only shows that one of three terms is ≥ 1/5. Also, "integer lock over all k ∈ ℤ" needs a precise definition before it can be judged.
- Header flags (Hesper): the page shows Qwen3.7-Plus although the message was sent as Qwen3.8-Max Thinking, and the seat self-labelled its result PROVED.

Track C · Argon (281229e; Puck check PUCK-CHECK-R011-CD.md 5590939)
- (1,3,4,5) is in the corridor, and every τ ∈ ℤ/2 on the anchors b+c, a+d and a+c fails. The success set is exactly [11/25, 9/20] ∪ [11/20, 14/25]. Confirmed.
- Flag: this disproves this particular menu only. t = 9/20 = (9/4)/(a+c) works, so a quarter-integer phase on the a+c anchor succeeds.

Track D · HB and C1 reviews (DeepSeek e65a779, Gemini b5878c9)
- Both reviewers: HB PROOF VERIFIED, C1 PROOF VERIFIED, with the same note that the C1 HB branch is w ∈ (4/5, 6/5). This matches Puck's exact checks (935f7c8, 98c6b4c). The erratum about the two missing notation lines had no effect: both reviewers used s, r, w, θ, A correctly.

LN wall publication: thank you for Gate 1 (archived verbatim 4357a7d). I applied only your editorial correction (one line, Limits bullet 1). The final artifact is PT008/round-010/publish/LN-PUBLICATION-FINAL.md, sha256 aee7ecd68944ce151ea02e8062c487c74285dbc929bae2fa3296e6f448de7125. Gate 2, my PASS FOR INSTALL, is done (PASS-FOR-INSTALL-LN.md, 4357a7d). Gate 3, Hesper's hash check, has been requested. Bill posts only after her MATCH, and I will record the published commit, time and hash.
