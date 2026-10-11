BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 09:02 +08
RE: 猜公式 Round 7 (packet 1006d95), send text r7_send_full.txt or r7_send_short.txt
SEAT: grok
MODEL: Grok Expert
CHAT: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7

--- reply verbatim ---
Source: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7
Model: Expert
Worked for 23s

Worked for 23s
ANSWER BLOCK
Q1: C-core4 holds on all 321 enumerated covers (min M₁₅=4). Partial: after scaling 1∈S the H cells t∈[H+1,2H] each require a speed near p/t∈[8,16]; their limited overlap forces ≥4 distinct small speeds. No counter-example found.
Q2: Floor 4 is tied to the 16-runner window of width H≈p/16; for 1/N with N−2 speeds the analogous floor is conjectured ⌈(N−2)/4⌉.
Q3: Checking 1 365 cores of size 4 plus 10 fillers is far cheaper than the full census once p>400; window containment prunes composites heavily. The floor itself does not explain the die-out after 431.
Q4: For 337, number of covers with M₁₅=4 lies in 80–250; largest M₁₅ in 8–11. Confidence 60 %.
Reasoning
FACT: In the chair’s complete enumerations (347 through 457) and the 274-cover sample at 307, together 321 covers, M₁₅ never drops below 4. The exceptional 389 cover reaches exactly 4.
PROOF: Window containment implies that a composite v contributes new cells only on residue classes coprime to v. Consequently the H cells t=H+1..2H (where p/t∈[8,16]) can be covered only by speeds whose scaled images lie in that narrow band; each such speed covers at most a short arithmetic progression of those cells.
IDEA: Covering H≈p/16 such cells with speeds drawn from a set of size ≤15 therefore requires at least four distinct members, establishing the floor once 1 is scaled into the cover.
FACT: Average core size is 210/n < 2 for every p≥307, so the maximum must be attained by a thin set of favourable scalings.
IDEA: The same window argument scales with the runner count: replacing 16 by N replaces the band [8,16] by [N/2,N] and the forced core size by roughly (N−2)/4.
FACT: There are C(15,4)=1 365 candidate cores. Extending each by 10 fillers and testing the n cells is O(1 365·n·10) arithmetic operations—orders of magnitude below the exhaustive search that produced the original census for p>400. Window containment further discards any core containing a multiple that cannot cover a coprime residue.
IDEA: The observed extinction of covers after 431 is driven by the growing residual after any fixed core of size 4, not by the floor itself.
Least-sure step: the precise constant 4 rather than 3; the window-overlap estimate has not been made fully rigorous for every residue pattern. UNFINISHED: a complete proof of C-core4 for all p.

--- end verbatim ---
END LETTER
