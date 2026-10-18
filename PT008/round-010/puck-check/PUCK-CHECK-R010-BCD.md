# PT-008 R010 · Puck exact checks of Tracks B, C, D (Hesper-filed replies)

Script: puck_check_R010_BCD.py (exact Fractions, no floats in the tests). Output: puck_check_R010_BCD_output.txt. 19 checks, 0 failures, plus one search (INFO).
Sources: Qwen B 5322664, Argon C 361a2b4, DeepSeek D 221bca6, Gemini D 0dd9138 (all PT008/round-010/).

## Track C (Argon) — all numeric claims CONFIRMED
- (1,2,3,10) is in the corridor 4a<d<4c. Lock t=k/(b+c)=k/5 gives ||dt||=0 for every k. Lock t=k/(a+d)=k/11 has no working k (exhaustive over the period). k=2 sits with b and c both exactly on 1/5, so every nudge of either sign fails. k=1 nudge window for delta is exactly [1/50, 1/15]; t=23/100 and t=1/4 both work.
- Puck note: these disprove single fixed locks, not general existence (consistent with Argon's own labels).

## Track B (Qwen)
- Sec.1 DISPROVED family a=eps, b=1, c=1+eps, d=2+eps=b+c: CONFIRMED in corridor and ||dt||=0 for all k (eps=1/10, 1/3, 1/2, 13/20).
- Sec.4 ||k/201||>=1/5 iff k mod 201 in 41..160: CONFIRMED.
- Sec.3 PROOF CANDIDATE ("q=b+c>=15, d not 0 mod q gives a working k"): the counting bound q-3*ceil(2q/5) is negative for every q (Hesper flag 2 CONFIRMED), so the argument proves nothing. Further, the proposition itself is FALSE: Puck search found integer counterexamples with gcd 1 and d not 0 mod q, e.g. (3,5,11,24) with q=16 and (1,7,9,24) with q=16; for these no k makes the lock t=k/(b+c) work. (3,5,11,24) also lies in the corridor (12<24<44). Suggested label for Sec.3: DISPROVED as stated.
- Sec.2 Hesper flag 3 stands: "k must grow unboundedly" is not by itself an impossibility proof for floor/ceil formulas.

## Track D (LN reviews, DeepSeek + fresh Gemini) — both return PROOF VERIFIED
- Key boundary d=4c: nudge |t-t0|<=1/(5d) costs at most c/(5d)=1/20, leaving 1/4-1/20=1/5. CONFIRMED exactly. Matches Puck's earlier 28,558-check run (c976dc2).
- Gemini's extra remark: since ||ct0||>=1/4 forces t0>=1/(4c), d>=4c gives dt0>=1, so the k=0 branch of LN is never reached (harmless redundancy). Puck agrees with the arithmetic.
