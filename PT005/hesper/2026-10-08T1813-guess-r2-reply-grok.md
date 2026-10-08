BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-08 18:14 +08
RE: 猜公式 Round 2 packet (aaa37b9), BEGIN…END block pasted verbatim
SEAT: grok
MODEL: Grok Expert (web search used)
CHAT: https://grok.com/c/4236e80a-de1d-4d49-b553-370ba3e9fbdf

--- reply verbatim ---
[Courier note: web search was used by Grok (2 searches, 5 sources; Grok has no off switch). Grok's Copy truncated; part 1 = Copy output (LaTeX), part 2 = page-text tail from the splice join, math glyphs as the page rendered them.]

=== PART 1: Copy output ===
COPY-PASTED TEXT from Grok Expert's Copy response button (final answer text only; excludes the opening thinking sentence "The draft is logically sound; the gap is the approximation exponent, not a false step. I am checking the LRC statement and the margin arithmetic before tightening the threshold." which was the streaming preamble shown before the final structured answer).

VERBATIM FROM CLIPBOARD (Grok's own copy output, clean LaTeX). Note: Grok's copy UI truncated mid-sentence at the end: it ends with "A factor-of-ten improvement inside the present Dirichlet proof i…(truncated)". The missing tail was read verbatim from the page text in a prior turn and is appended in grok_round2_reply_page_tail.md so the full answer can be reconstituted.

--- COPY START ---
The draft is correct. The 20-order gap is the Dirichlet exponent, not a false line.

**1. Referee T1.**

Lemma A: **YES.** Lemma B: **YES.** Final step: **YES.**

- LRC(14) is applied to exactly 13 speeds, which is what the packet's statement of F5 gives. The stationary runner is not one of the \(w_i\).
- Signs. After F2, \(qS\) is a cover. Dirichlet returns \(qs_i\equiv\varepsilon_i\pmod p\) with \(|\varepsilon_i|\le p/N\). The positive representatives \(c_i=|\varepsilon_i|\) are the speeds of \(qS\). They are nonzero because \(q\not\equiv0\) and \(s_i\not\equiv0\). They are distinct up to sign because \(q\) is a unit and the \(s_i\) are already distinct up to sign: \(qs_1\equiv\pm qs_2\) would force \(s_1\equiv\pm s_2\). For \(N\ge56\), \(c_i\le p/56<(p-1)/2\), so each \(c_i\) is already the canonical speed in \(1..n\).
- Strictness. Too-near demands \(\|vt/p\|<1/16\). The chain gives
  \[
  \|w_it/p\|\ge\frac1{14}-\frac{w_i}{2p}\ge\frac1{14}-\frac1{112}=\frac1{16},
  \]
  so equality is still not too-near. F3's parity obstruction is not needed here. The torus estimate \(\|w_i(t/p-x)\|\le w_i/(2p)\) is valid because \(w_i/(2p)\le1/2\).
- The only bookkeeping fix, not a gap: take \(M=\lfloor p/N\rfloor\). Then \(c_i\le M\) and \(M/(2p)\le1/112\) still holds as soon as \(N\ge56\), i.e. \(p-1\ge56^{13}\).

Weakest step: Lemma B. It is true, but plain Dirichlet is what inflates the threshold from the data's \(\sim280\) to \(10^{22}\).

**2. Shrink the threshold.**

(a) *Better margin — does not improve the constant.* **PROOF.** Around an LRC witness \(x\) the set where every \(\|w_ix\|\ge1/16\) contains an interval of length \(1/(56M)\), because the slack \(1/14-1/16=1/112\) can be spent at rate at most \(M\). Guaranteeing a grid point \(t/p\) in that interval again forces length \(>1/p\), hence \(p\ge56M\). Same constant. It is sharp for this method: speeds \(\{1,\ldots,13\}\) attain loneliness exactly \(1/14\), so no uniform \(\delta>0\) exists.

(b) *Pinning one speed does not cut the exponent.* **PROOF.** F2 can put \(1\in S\), but the image of that speed is the Dirichlet \(q\) itself. Forcing \(q\) small as well is a 13th simultaneous condition, so the exponent stays 13. Dropping it leaves a scaled speed as large as \(N^{12}\), and Lemma A no longer applies.

(c) *Different route.* **IDEA.** Inclusion-exclusion cannot close the gap by itself: \(13H/n\approx1.625\), and a cover is allowed to make some pairwise intersections as small as the multiplicative geometry permits, so the worst case for an upper bound on the union is exactly the case with the least forced overlap. A character-sum expansion of \(\prod_{v\in S}(1-1_{\|vt\|<p/16})\) has main term \((7/8)^{13}n>0\), but the error is a sum of \(2^{13}\) incomplete geometric sums and does not go negative for any reasonable explicit \(p\) without a structure hypothesis.

(d) *Hybrid, the real shrinkage.* **IDEA, using the architecture of F5.** Allikvere's proof of LRC(14) does not treat all 13-tuples equally: a primitive counterexample to loneliness \(1/14\) has speed product below an explicit logarithmic bound (about \(e^{409}\) in the fourteen-runner argument). So the only 13-sets that could possibly survive Lemma A's discretisation are those for which **every** unit multiple has a signed representative of small product. That is a thin set. Certify as follows:
- Analytic range: any 13-set whose reduction (Lemma B) has product \(>e^{409}\) is not a cover, as soon as the discretisation margin fits, which is a bound polynomial in that product rather than \(56^{13}\).
- Finite range: the surviving small-product orbits are the same orbits the LRC certificates already enumerated modulo the archived primes. Re-checking those orbits for the strict \(1/16\)-cover property, instead of re-running the gate engine on all \(\binom{n}{13}\) tuples, is the cheap computation between 300 and that polynomial bound.

A factor-of-ten improvement inside the present Dirichlet proof i…(truncated)
--- COPY END ---

The "(truncated)" occurs immediately after the fragment "A factor-of-ten improvement inside the present Dirichlet proof i". The remainder of the answer (continuing from that sentence through sections 3 and 4) was read verbatim from the page and is saved in grok_round2_reply_page_tail.md.
=== PART 2: page-read tail ===
PAGE-READ TAIL — splices into grok_round2_reply_copy.md at the truncation point.

The Copy response button truncated mid-sentence at:
"...A factor-of-ten improvement inside the present Dirichlet proof i…(truncated)"

The page text at that point (captured verbatim from the conversation's text layer at 2m 29s) completes the sentence and continues through to the final "4. One sentence for Tuzi." The remainder of section 2(d)'s closing and sections 3 and 4 are below.

Math formatting note for this tail: the page's text layer breaks MathML variables into separate glyphs (e.g. "𝑒 409" instead of e^409, "56 13" instead of 56^13, "10 22" instead of 10^22, "𝑝 − 1 ≥ 56 13" instead of p−1 ≥ 56^13, "𝑁 12" instead of N^12). I keep these as the page rendered them, because the copy portion already uses LaTeX and I am not normalizing across the splice. Where I could unambiguously read the intended value from the copy's own parallel passage, the exponents are: e^409, 56^13, 10^22, 120^14, N^12. The splice join is marked.

=== SPLICE JOIN (completes the truncated copy sentence and continues) ===

A factor-of-ten improvement inside the present Dirichlet proof is not available; the interval form of (a) saturates at the same 56.

3. The 14 question. No infinite family of 14-covers. PROOF, conditional on F5. T2 is the same argument with LRC(15), 14 speeds, margin 1/15 − 1/16 = 1/240, and threshold p ≥ 120M. Dirichlet in dimension 14 then kills every 14-set once p > 120^14. Combined with F3, γ(p) = 15 for all such p. The data (last 13-cover at 277, then ≥ 14) is the beginning of that climb, not evidence of a persistent 14-family. Weakest point is again the exponent, not the conclusion.

4. One sentence for Tuzi. The lever is Allikvere's speed-product bound, not a sharper Dirichlet box: it reduces "no 13-cover" to a finite list of small-product orbits that the LRC certificates already classified, which is the only way to bring the threshold from 10^22 down to a range a machine can finish.

=== END OF RESPONSE ===

Confirmation that the answer had finished at the moment of capture: the "Working for Ns" indicator was gone from the page, and the post-reply UI was in place — a "5 sources" chip and follow-up suggestion buttons ("Give the proof for (c)", "Explore the LRC(14) speed-product bound", "Rewrite problem 3 in English") with the model label "Expert" beside them. The Copy response button was enabled and returned the text above.

Observations about web search: during generation the response showed "Ran 2 searches"; the finished answer shows a "5 sources" chip. Conclusion: the reply used web search.
--- end verbatim ---
END LETTER
