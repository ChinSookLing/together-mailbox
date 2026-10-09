BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 12:11 +08
RE: 猜公式 Round 3 ADD-ON (chair note 46, 34bd541; C16), one narrow task, send text r3b_send_grok.txt
SEAT: grok
MODEL: Grok Expert (Grok 4.6; web search cannot be disabled, prompt said no search)
CHAT: https://grok.com/c/aed6bc08-86f7-40e9-8077-f145aa58f07a

--- reply verbatim ---
ANSWER BLOCK

No 13-set with \(c(S) < 1/16\) was found. C16 is unbroken on this pass. UNFINISHED as a disproof (large \(M\) not exhausted).

FACT. Code (exact `Fraction` merge of the forbidden intervals \(|t - k/v| < 1/(16v)\), circle-split) recovers the chair’s examples: \(S=\{1,2,3,4,5,7,8,9,10,11,12,13,14\}\) has longest piece \(1/224\), so \(c=1/16\); \(\{1..13\}\) has \(c=1/8\). Scaling preserves this: \(2S\) and \(3S\) also give \(c=1/16\) (PROOF of the stated invariance on these instances: same endpoints, scaled by the common factor, cancelled by \(M\)).

FACT. Structured search, all by code, none by hand:
- replace-one in the tight set by \(N\le 300\);
- two-AP unions, divisor-heavy sets, round/floor deformations \(k(v+\varepsilon)\) of \(\{1..5,7..14\}\);
- greedy fill and hill-climb at \(M\in\{30..256\}\) (small speeds biased in).
Minimum stays \(c=1/16\), only on scalings of the tight set. Best non-scaling large set: \(S=\{2,6,16,19,22,23,25,26,27,28,29,30,31\}\), \(M=31\), longest piece \(13/4864\), \(c=403/4864\approx 0.08285>1/16\) (exact). A one-step deform \(\{2,4,6,8,10,14,16,18,20,22,24,26,29\}\) jumps to \(29/208\approx 0.139\). Primes, power-of-two mixes, and AP unions were worse (\(c\ge 0.26\)).

IDEA. The tight piece is pinched by the \(v=1\) wall at \(1/16\) and a \(v=14\) wall at \(15/224\). Replacing 14 by a larger \(N\) moves that wall farther than \(1/(16N)\), so \(c\) rises. Sets that drop 1 leave a coarser gap near 0.

Least-sure step: the hill-climb/AP sample at \(M\ge 30\) is not exhaustive, so a non-scaling counterexample could still exist outside the families above. Nothing sampled landed in \((0.0625, 0.08)\).

--- end verbatim ---
END LETTER
