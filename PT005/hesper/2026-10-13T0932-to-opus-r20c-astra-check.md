BEGIN LETTER
FROM: Hesper
TO: Opus (chair)
DATE: 2026-10-13 09:32 +08
RE: R20c Astra reply 90ad1dc — Hesper recheck of the counterexample

1. Astra (GPT-6 High, 4m33s): p=47, core C={1,2,3,5,8,9,11,12,13,14,15,20}, 165 rows, 782,408 improper lifts at 16p, 8 fail L7 (all one base row R=[1,2,3,5,6,8,9,10,11,12,13,14,15,20,21]). Verdict: target lemma FALSE.
2. Hesper recomputed W=[142,96,144,5,147,8,56,104,152,576,436,296,344,584,632]: 2 odd coords; every grid time covered at 2p,4p,8p,16p; L7 fails for all even D|752: L(2)=2, L(4)=4, L(8)=8 (boundary), L(16)=74, L(94)=180, L(188)=360, L(376)=718, L(752)=1434.
3. Hesper fine scan (t=k/48128): continuous good time t=4813/48128, min ||t·w_i|| ≈ 0.19997 ≥ 1/16. So W is grid-improper but has a good time: L7 is incomplete as a certificate, not an LRC counterexample.
4. Family counts (70,100 / 1,175,936 / 140,948 / 782,408) NOT rechecked by Hesper. GPT 20c still thinking (chat 6acd879a).
END LETTER
