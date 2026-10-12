BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:20 +08
RE: 猜公式 Round 17 literature walk (packet ad54489), send text r17_send_full.txt or r17_send_short.txt
SEAT: deepseek
MODEL: DeepSeek DeepThink + Search
CHAT: https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202

--- reply verbatim ---

ANSWER BLOCK
Ingredient #1
Reference: Terence Tao, "Some remarks on the lonely runner conjecture," Contributions to Discrete Mathematics 13(2), 1–31 (2018); arXiv:1701.02048.
Status: READ (opened arXiv PDF, lines 8–15)
Statement: Tao proves (i) the gap improves to 1/(2n) + c·log n / (n^2 (log log n)^2); (ii) to verify LRC up to n+1 runners it suffices to check integer speeds of size n·O(n^2).
Serves dish: B
How it plugs in: Replaces L16's crude Dirichlet scaling. PT005's L16 uses p^(1/14) scaling giving P_0 ≈ 10^487; Tao's reduction means one only needs to check speeds up to n·O(n^2), but for n=14 this is still enormous.
What it gives: UNFINISHED (the exponent is not explicit enough for P_0 ≈ 10^4).
Gap: Tao's bound is asymptotic; an explicit constant is needed.

Ingredient #2
Reference: R. D. Malikiosis, F. Santos, M. Schymura, "Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants," arXiv:2411.06903 (2024).
Status: READ (opened ar5iv HTML, lines 8–18)
Statement: Using zonotopal reinterpretation, they improve Tao's finite-checking bound to velocities up to (n+1)^(2n)·n^(n-1) ≤ 2^n·n^(2n).
Serves dish: B
How it plugs in: For n=14, 14^28 ≈ 10^32, still far above 10^4. But the method (zonotope covering radius) may yield a sharper explicit threshold than Dirichlet scaling.
What it gives: UNFINISHED (I did not compute the explicit constant).
Gap: Need to extract an effective P_0 from their zonotope bound for n=14.

Ingredient #3
Reference: Sebastian Czerwiński, "Random runners are very lonely," Journal of Combinatorial Theory Series A 119(6), 1194–1199 (2012); arXiv:1102.4464.
Status: READ (opened ar5iv HTML, lines 4–12)
Statement: For random speed sets, with probability tending to one, the loneliness bound improves from 1/k to 1/2−ε. Proof uses Fourier analytic methods.
Serves dish: D
How it plugs in: PT005's Poisson formula U ≈ n·e^(−14H/n) and empty-coset fraction (7/8)^14 are heuristic. Czerwiński's theorem is the rigorous random-model counterpart: it confirms that random sets are very lonely, far from the extremal near-misses at 383/397.
What it gives: UNFINISHED (his 1/2−ε bound is much stronger than PT005's 1/16 threshold).
Gap: His model uses random speeds from a large range; PT005's speeds are bounded by n=(p−1)/2.

Ingredient #4
Reference: S. Czerwiński, J. Grytczuk, "Invisible runners in finite fields," Information Processing Letters 108(2), 64–67 (2008).
Status: ABSTRACT (ACM abstract, lines 10–17)
Statement: The LRC holds if one chosen runner is eliminated; proof uses double-counting over finite fields. The problem reduces to a statement in Z_n where n is the sum of two speeds.
Serves dish: E
How it plugs in: PT005 works mod p. Their reduction to Z_n suggests that the relevant modulus is not p but a combination of speeds. This could explain why PT005's mod-16 cutoff is empirical rather than structural.
What it gives: UNFINISHED (no explicit threshold).
Gap: Need to translate their finite-field double-counting to the prime p setting.

Ingredient #5
Reference: Noah Kravitz, "Barely lonely runners and very lonely runners: a refined approach to the Lonely Runner Problem," Combinatorial Theory 1, Paper No. 17 (2021); arXiv:1912.06034.
Status: READ (opened arXiv abstract, lines 8–26)
Statement: Kravitz conjectures a gap: either ML(v) = s/(ns+1) for some s∈N, or ML(v) ≥ 1/n. He confirms this for n≤3 and for n=4, 6 when one speed is much faster.
Serves dish: A / C
How it plugs in: The extremal set K* = {1..15} ∖ {6} has ML just above 1/16. Kravitz's conjecture would imply that if a 14-set is not exactly tight, its loneliness is bounded away from 1/16 by a uniform gap. This directly supports C-floor: near-extremal sets are rigid.
What it gives: UNFINISHED (his conjecture is open for n=14).
Gap: Need the n=14 case of his conjecture.

Last question:
I would cook Dish B. Tao's reduction and Malikiosis–Santos–Schymura's improvement are the only published results that directly attack the effective threshold. Even though their current bounds are far from 10^4, the zonotope method is the most promising route to replace L16's crude Dirichlet scaling.

125 web pages
DeepThink · Search
AI-generated, for reference only


--- end verbatim ---
END LETTER
