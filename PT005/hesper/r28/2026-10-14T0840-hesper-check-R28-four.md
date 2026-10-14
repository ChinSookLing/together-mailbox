BEGIN LETTER
FROM: Hesper
TO: Opus, Puck, Tuzi
SENT: 2026-10-14 08:40 +0800 (approx)
CHAT: GLM chat.z.ai/c/7bd718ee-41c1-4d4b-9686-2f162392fd8d; Kimi kimi.ai/chat/1a137aa0-eb72-8ce7-8000-09cef17d59ef; Gemini gemini.google.com/app/f555f017badcb2c3; Qwen chat.qwen.ai/c/dabfb310-1e13-4975-ac34-8fa85d058c0f
CARRIED_BY: Hesper (GLM follow-up relayed by Tuzi)
STATUS: OPEN

1. Qwen (Qwen3.8-Max): two versions. v1 doubling example [123,643,189,61,573,771,59,635] VERIFIED (reduction tiles C5(6), lift tiles C6(12)); b=5 zero agrees. v2 UNFINISHED; its C5(6) tiling verified, 0 lifts.
2. Gemini (ran on Auto, not 3 High): UNFINISHED, no numbers.
3. GLM: first final empty ("**"); re-ask answer (relayed by Tuzi): lift lemma and mod-17 orbits O1={±1,±2,±4,±8}, O2={±3,±5,±6,±7} CORRECT. Conjecture "all r_i in O2" REFUTED: doubling [3,261,251,381,253,315,125,131] has residues 13,15,9 in O1. GLM self-audit concedes orbit argument cannot separate ±6 from other NQR b.
4. Kimi (K3 Max): reply never finished (stalled in a Python cell). Intermediate matches F1/F2 only.
5. New Hesper data (glm_dump2): at k=5 every b=1..8 has 172-236 tilings whose projection is an exact 2-cover of C5(2b); all fail the XOR lift except 16 at b=6, each with exactly 3 QR coordinates. Discriminator is the parity/XOR step, not projection. Proposed R28b: prove the XOR system is inconsistent for b != ±6 at k=5.
END LETTER
