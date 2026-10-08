BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-08 20:53 +08
RE: 猜公式 Round 2 packet (aaa37b9), BEGIN…END block pasted verbatim
SEAT: deepseek
MODEL: DeepSeek (Tuzi's phone; relayed in chat 20:53 +08; NOTE: reply is in Round 1 format (8 EXAM predictions), not an answer to the Round 2 lemmas)
CHAT: Tuzi's own DeepSeek app (no URL)

--- reply verbatim ---
1. Rule.
   Use the following empirical threshold rule for “γ(p) ≥ 14?”:

· If H \le 12: predict 12 or less.
· If 13 \le H \le 16: usually 13, unless the residue class has an early flip.
· Flip to “14 or more” by residue p \bmod 16:
  · mod 1: H \ge 17
  · mod 3: H \ge 19
  · mod 5: H \ge 18
  · mod 7: H \ge 19
  · mod 9: H \ge 17
  · mod 11: H \ge 17
  · mod 13: H \ge 16
  · mod 15: H \ge 14

This rule fits all training rows, including the observed “≥14” entries.

2. Predictions.
   For the 8 EXAM primes:

p H p mod 16 Prediction
199 12 7 12 or less
227 14 3 13
257 16 1 13
271 16 15 14 or more
283 17 11 14 or more
311 19 7 14 or more
313 19 9 14 or more
401 25 1 14 or more

3. Reason.
   The data show a clear threshold phenomenon: γ grows with H, but the residue p \bmod 16 shifts the threshold. Bad residues such as 15,13,9,3 flip earlier; good residues such as 1,7,11,5 survive a little longer at 13. The table’s “≥14” entries are exactly where H has crossed the residue-dependent threshold. So I am using interpolation from the training rows rather than a proven closed formula.
4. Big question.
   I think yes: eventually \gamma(p) \ge 14 for every prime beyond some P_0. From the data, P_0 is probably around 300, though there may be isolated later exceptions. I do not think γ stays bounded at 13 forever; the covering problem becomes harder as H grows, and γ should keep creeping upward, likely logarithmically slowly rather than linearly. So \gamma(p) should eventually reach 15, 16, etc., but very slowly.
5. Confidence.

p Prediction Confidence
199 12 or less 80%
227 13 60%
257 13 55%
271 14 or more 90%
283 14 or more 65%
311 14 or more 80%
313 14 or more 85%
401 14 or more 95%

--- end verbatim ---
END LETTER
