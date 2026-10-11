BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 15:24 +08
RE: 猜公式 Round 12 (packet c9a646a), send text r12_send_full.txt or r12_send_short.txt
SEAT: kimi
MODEL: Kimi K3 Thinking High
CHAT: https://www.kimi.ai/chat/1a129bc7-1772-844b-8000-09ce45eb4d1a

--- reply verbatim ---
Kimi K3 High, chat https://www.kimi.ai/chat/1a129bc7-1772-844b-8000-09ce45eb4d1a (renamed 'PT005 · Big Picture R12'). Assembled by Hesper from three browser captures (original ANSWER BLOCK, best-set rows captured during streaming, compact ANSWER BLOCK after queued nudge). Full code not captured.

VERBATIM ORIGINAL R12 ANSWER BLOCK (the long reply that opened with an ANSWER BLOCK), chat 1a129bc7-1772-844b-8000-09ce45eb4d1a, K3 High.

Final. ANSWER BLOCK — conclusions (≤300 words)
FACT/computed here. I used ‖x‖ = min(x mod p, p − x mod p). The known Round‑3 near‑misses reproduce U=1 at 383 and 397, so the encoder is consistent. My search gives upper bounds B(p) ≥ D(p); where census already says D≥1, a found B=1 is exact, and 457 is exact D=0. Best found B: 431:2, 433:1, 439:2, 443:2, 449:1, 457:0, 461:3, 463:2, 467:1, 479:2, 487:2, 491:2, 499:2. Sample 601–1009: 601:4, 613:2, 617:4, 631:4, 643:3, 653:4, 683:5, 719:5, 769:5, 829:6, 883:5, 937:7, 997:6, 1009:6.

IDEA/fit. On these upper bounds, B ≈ 0.009295·p − 2.4496 (RMSE 0.756); log/sqrt fits are only marginally better, so over this range it looks roughly linear with a negative intercept, much flatter than M≈0.077p. Slack s=n−8H shows no clear monotone effect (corr(B,s)=0.039).

IDEA/model. Poisson extreme value: choose least d with log(C(n,14)/n)+log P[Poi(M)≤d] ≥ 0. It predicts 0 too often near 431–601, but rises to about 6–7 by 937–1009, qualitatively matching the search.

PROOF status. No theorem is proved. A plausible empirical boundary would be “no covers for all primes ≥461” (last known cover 457), i.e. P0=457; rigorous P0 is UNFINISHED. 120^14 = 128391846454886400000000000000 is vastly larger.

Prediction, judgment not computed: 503: 2–3, medium-high; 547: 2–3, medium; 577: 2–3, medium; 599: 2–3, medium-low (≥4 close second).

[The ANSWER BLOCK is immediately followed by "WORK 1) Measuring U(S) — FACT / PROOF for re-check, IDEA for search quality" and the rest of the long reply (code, best-sets table, shape/model/theorem/prediction sections).]

Best sets found (B=U(S)) table — rows captured during streaming poll (Turn 94 element list). From K3's Round 12 final reply, chat 1a129bc7-1772-844b-8000-09ce45eb4d1a.

p=457, B=0, [4,25,33,41,50,58,83,108,112,128,129,133,158,183]
p=467, B=1, [11,18,29,61,97,108,133,140,158,176,194,205,209,212]
p=479, B=2, [28,51,79,93,116,130,144,165,172,177,208,223,228,235]
p=487, B=2, [14,24,36,86,100,122,129,143,165,171,186,215,222,236]
p=491, B=2, [5,36,41,97,102,133,138,164,166,174,183,184,220,235]
p=499, B=2, [18,22,40,49,58,67,76,128,138,156,178,188,196,245]
p=601, B=4, [5,22,27,71,91,118,125,135,148,189,216,243,281,297]
p=613, B=2, [8,49,65,90,123,146,147,188,229,237,278,286,290,302]
p=617, B=4, [21,63,80,84,134,210,218,231,239,250,260,273,281,294]
p=631, B=4, [25,46,48,117,119,159,163,188,209,232,259,276,280,305]
p=643, B=3, [8,27,35,86,105,113,121,156,183,191,218,222,293,296]
p=653, B=4, [34,52,69,86,137,175,225,240,241,257,275,309,310,326]
p=683, B=5, [16,21,37,84,126,205,226,242,247,268,289,310,315,331]
p=719, B=5, [22,44,66,91,113,135,157,179,201,226,248,270,292,336]
p=769, B=5, [15,51,56,66,107,163,168,209,219,224,270,275,285,382]
p=829, B=6, [45,61,90,106,135,151,196,241,257,286,302,331,376,392]
p=883, B=5, [7,37,61,108,148,202,209,235,310,317,357,364,371,425]
p=937, B=7, [7,59,66,111,125,170,177,184,208,236,244,347,361,420]
p=997, B=6, [50,54,77,127,204,231,281,308,331,358,385,408,435,485]
p=1009, B=6, [18,61,79,97,140,158,176,219,237,298,316,377,395,456]

Note: earlier rows 431 (B=2), 433 (B=1), 439 (B=2), 443 (B=2), 449 (B=1) were visible during Turn 92 but not all captured verbatim yet.

VERBATIM COMPACT ANSWER BLOCK (nudge-induced "ANSWER BLOCK — final."), chat 1a129bc7-1772-844b-8000-09ce45eb4d1a, K3 High, Turn ~105.

ANSWER BLOCK — final.
Encoder validated: known 383/397 near-misses give U=1. I report best found B(p); D(p)≤B(p). Exact where census D≥1 meets B=1, and 457 D=0.
431–499 B: 431=2, 433=1 exact, 439=2, 443=2, 449=1 exact, 457=0 exact, 461=3, 463=2, 467=1 exact, 479=2, 487=2, 491=2, 499=2. 601–1009 sample B: 601=4, 613=2, 617=4, 631=4, 643=3, 653=4, 683=5, 719=5, 769=5, 829=6, 883=5, 937=7, 997=6, 1009=6. Sets are re-checkable from prior reply; exact D for B≥2 rows: UNFINISHED.
Shape: B≈0.009295p−2.4496, RMSE 0.756; log-fit RMSE 0.710, sqrt-fit 0.726, so roughly linear/flat, far below M≈0.077p. corr(B,p)=0.911, corr(B,M)=0.923, corr(B,s)=0.039; no clear p mod 16/slack law beyond M. Poisson-EV: least d with log(C(n,14)/n)+log P[Poi(M)≤d]≥0 gives 0 too often near 431–601, rising to about 6–7 by 937–1009; qualitatively useful, not exact.
Theorem: no lower bound D≥αp−β proved; no uniform o(p) Fourier error proved; rigorous P0 UNFINISHED. Empirical smallest plausible target is "all primes ≥461" after last cover 457. Computed 120^14=128391846454886400000000000000, vastly larger.
No-code predictions, judgment only: 503: 2–3 medium-high; 547: 2–3 medium; 577: 2–3 medium; 599: 2–3 medium-low, ≥4 close second.
--- end verbatim ---
END LETTER
