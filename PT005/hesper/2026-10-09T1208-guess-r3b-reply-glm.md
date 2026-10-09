BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 12:11 +08
RE: 猜公式 Round 3 ADD-ON (chair note 46, 34bd541; C16), one narrow task, send text r3b_send_glm.txt
SEAT: glm
MODEL: GLM-5.3 Deep Think Max, web off
CHAT: https://chat.z.ai/c/d0b0f356-5af2-41b0-9d15-df47f920759b

--- reply verbatim ---
**ANSWER BLOCK**

**FACT (result).** For S = {1,2,3,4,5,7,8,9,10,11,12,13,14}, the longest 1/16-safe piece in [0, 1/2] is **[1/16, 15/224]**, of length 15/224 − 14/224 = **1/224 exactly — CONFIRMED**. Its left end is made by **speed v = 1**, its right end by **speed v = 14**. Hence c(S) = 14·(1/224) = 1/16 (equality in C16), matching the chair's data.

**PROOF (ends).** t < 1/16 ⇒ ‖t‖ < 1/16, so v = 1 forces the left end (‖t‖ = 1/16 at t = 1/16). Right end: 14·(15/224) = 15/16, so ‖14t‖ = 1/16 at t = 15/224 = 1/14 − 1/224, the left edge of v = 14's exclusion zone about 1/14; for t ∈ (15/224, 17/224), 14t ∈ (15/16, 17/16) ⇒ ‖14t‖ < 1/16.

**PROOF (safe throughout).** For t ∈ [1/16, 15/224]: if v ≤ 7, vt ∈ [v/16, 15v/224] ⊂ (0, 1/2), so ‖vt‖ = vt ≥ v/16 ≥ 1/16. If v ≥ 8, vt ∈ [v/16, 15v/224] ⊆ [1/2, 15/16] ⊂ [1/2, 1), so ‖vt‖ = 1 − vt ≥ 1 − 15v/224 ≥ 1 − 210/224 = 1/16. Equality occurs only at the two ends (v = 1 left, v = 14 right), so the piece is maximal.

**PROOF (it is the longest).** Merging all exclusion zones in [0, 1/2] (enumeration below) leaves six interval-gaps; the runner-up, [11/64, 31/176] between speeds 12 and 11, has length 3/704 < 1/224 (704 > 672). Mirroring t → 1 − t gives 12 intervals + 6 isolated points = **18 pieces**, matching the chair's count.

**Least-sure step:** the by-hand merge of 33 zone centers — one arithmetic slip would misrank a minor gap (not the winner, which is cross-checked three ways: length 1/224, 18 pieces, c = 1/16).

**Supporting enumeration.** Speed v excludes open zones (k/v ± 1/(16v)); a reduced p/q is a center only for speeds divisible by q, with effective radius 1/(16·v_min(q)), v_min(q) = least element of S divisible by q (since 6 ∉ S, the zone at 1/6 has radius only 1/192, from v = 12). Centers in [0,1/2] = the 33 Farey-14 fractions. Merged gaps:
- [1/16, 15/224], 1/224, speeds 1 & 14 ← longest
- [17/128, 15/112], 1/896, speeds 8 & 7
- [33/208, 31/192], 7/2496, speeds 13 & 12
- [11/64, 31/176], 3/704, speeds 12 & 11 (near-tie, ~4.5% shorter)
- [17/64, 47/176], 1/704, speeds 4 & 11
- [97/208, 15/32], 1/416, speeds 13 & 2
plus isolated points 3/16, 5/16, 7/16 (doubly bound: v = 5 & 11, 3 & 13, 7 & 9).

**IDEA (aside):** chair's "loneliness ≈ 0.086957" equals 2/23 exactly; provenance not verified here.

--- end verbatim ---
END LETTER
