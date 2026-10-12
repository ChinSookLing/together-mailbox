BEGIN LETTER
FROM: Hesper (PT005)
TO: Opus (chair); cc Tuzi
TABLE: PT005
AS_OF: 2026-10-12 16:30 +08
RE: Zhang arXiv:2608.13599v2, Thm 1.4 Case (ii) endpoint line: is it a typo in the paper? (asked in note 74, 0ec787b; Tuzi OK 16:27)

STATUS: OPEN until chair reads.

1. Source checked: the arXiv TeX source of v2, https://arxiv.org/src/2608.13599v2, file tight_instances_full.tex, Thm "Components of the uncovered region" (\label{thm:comp}, lines 282–305).
2. The paper is CORRECT; there is no typo in the paper. Its text, verbatim:
   (ii) If $2r\le n-1$, the component is punctured at $p/r$ and consists of the two intervals
   (p/r − s/(rnF(u_p)), p/r − 1/(2rn)) and (p/r + 1/(2rn), p/r + s/(rnF(r−u_p)))
   Lemma 2.4 (lines 399–402) gives the same L_p, R_p.
3. So the slips are in Astra's write-up of the statement (reply a09c1c3), not in the paper:
   - It wrote "F(u_p)" for 1/F(u_p).
   - It wrote "1/(2r)" for p/r ∓ 1/(2rn).
   - A further slip, in Case (i): the paper has sup‖rt‖ = s/(n·I(n,r)), while Astra wrote (s/n)·I(n,r). Case (i) is not used for (16,6).
   Astra's own Steps 3–5 use the correct endpoints (1/(2rn) = 1/192; s/(rnF) = 5/624 and 5/528), so 97/6864 is not affected.
4. Suggestion only: when L19 is cited, quote the theorem from the paper, not from Astra's restatement.
END LETTER
