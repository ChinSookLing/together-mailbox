BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-08 13:20 +08
RE: 猜公式 Round 1 packet (ebc63af), BEGIN…END block pasted verbatim
SEAT: grok
MODEL: Grok Expert (NOTE: no web toggle; reply shows 13 sources / ran 3 searches; code only on training primes per agent)
CHAT: https://grok.com/c/4236e80a-de1d-4d49-b553-370ba3e9fbdf

--- reply verbatim ---

The quantity γ(p) is the ordinary covering number of the family of sets
\[
\mathcal{F}_p=\bigl\{v^{-1}I\bmod\pm1:v=1,\dots,n\bigr\},
\]
where \(I=\{x:16\|x\|<p\}\) (so \(|I\cap\{1,\dots,n\}|=H\)). Equivalently, it is the smallest number of multiplicative copies of the symmetric interval of radius \(p/16\) that cover \((\mathbb{Z}/p\mathbb{Z})^*\). The design is a regular uniform hypergraph of degree \(H\) and rank \(H\), which immediately yields the integral lower bound \(\lceil n/H\rceil\in\{8,9\}\) already stated in the query; all larger values come from forced overlaps.

1. Rule  
γ(p) equals the covering number above. On the computed range it satisfies
\[
\lceil n/H\rceil\le\gamma(p)\le\lceil n/H\rceil+5
\]
and the excess is non-decreasing on average: it is typically 2–3 for \(p<150\), 3–4 for \(150<p<250\), and 4–5 once \(p>250\). Consequently the predicate "γ(p)≥14" holds for a prime precisely when that excess reaches 5 (or 6 when \(p\equiv1\pmod{16}\)). No simpler closed form (dependence only on \(p\bmod16\), only on the prime factors of \(p-1\), etc.) fits the table.

2. Predictions  
- 199: 13  
- 227: 13  
- 257: 13  
- 271: 14 or more  
- 283: 14 or more  
- 311: 14 or more  
- 313: 14 or more  
- 401: 14 or more  

3. Reason  
Each new multiplicative copy of \(I\) can be placed so that it meets the still-uncovered set in at most \(H-O(1)\) points; the \(O(1)\) loss is produced by the low-height relations \(v_1/v_2\in I\cdot I^{-1}\) that become unavoidable once more than roughly \(\log p\) candidate centres have been chosen. The same relations are visible in the table as the slow climb 10→11→12→13→≥14. The eight exam primes sit on this climb: the three below 260 still have room for an excess of only 4 (hence γ=13), while the five larger primes have already crossed the threshold at which every 13-set leaves an uncovered cell (the same threshold that produces the five "≥14" entries already verified between 239 and 307).

4. Big question  
Yes. The same overlap obstruction grows, so there exists \(P_0\le500\) beyond which γ(p)≥14 for every prime. The excess itself continues to increase, but only logarithmically: the heuristic coming from the number of independent low-height relations is
\[
\gamma(p)=\frac nH+\Theta(\log\log p).
\]
Thus one expects γ(p)≥15 for all sufficiently large p, γ(p)≥16 still later, and so on, yet γ(p) remains \(O(\log\log p)\) and in particular \(o(\log p)\). (The deletion of part (c) for all large gates would follow at once from the existence of \(P_0\), but parts (a) and (b) are untouched.)

5. Confidence  
199: 55 %; 227: 60 %; 257: 50 %; 271: 55 %; 283: 70 %; 311: 75 %; 313: 75 %; 401: 80 %.
--- end verbatim ---
END LETTER
