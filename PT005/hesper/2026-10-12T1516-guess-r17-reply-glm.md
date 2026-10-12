BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:16 +08
RE: 猜公式 Round 17 literature walk (packet ad54489), send text r17_send_full.txt or r17_send_short.txt
SEAT: glm
MODEL: GLM-5.3 Deep Think Max (web on)
CHAT: https://chat.z.ai/c/ab2e3ca7-e3ae-48be-8f78-d78158df6f5d

--- reply verbatim ---

Conclusions first

Dish D (random model): Czerwiński (2011) proves that for random speed sets, the Lonely Runner bound jumps from 1/k to 1/2−ε with probability tending to 1. This strongly supports PT005's heuristic that random 14-sets are far from extremal, and the empty-coset fraction (7/8)^14 is plausibly the correct order for the probability that a fixed coset is empty. The result uses Fourier analysis, not a Poisson model, but it is the closest theorem I found.

Dish B (threshold / effective reduction): Tao's 2015 blog post gives an effective reduction of the LRC to integer speeds bounded by an explicit C(k). However, the proof only shows C(k) exists and is finite; the actual bound is astronomically large (grows faster than exponentially in k). It does not help lower P0 from 10^487 to 10^4. To get there, one would need a much sharper effective Kronecker/Dirichlet or Bohr-set size bound, which is still open.

Ingredient #1
Reference: Sebastian Czerwiński, "Random runners are very lonely", arXiv:1102.4464 (2011).
Status: ABSTRACT (I read the arXiv abstract page).
Statement: For random sets of k speeds, with probability tending to one, every runner is lonely with separation at least 1/2 − ε (instead of the conjectured 1/k). The proof uses Fourier analytic methods.
Serves dish: D.
How it plugs in: PT005's random model (U ≈ n·e^{−14H/n} and the empty-coset fraction (7/8)^14) is a deterministic, finite-field analogue. Czerwiński's theorem is the continuum, probabilistic version. It suggests that for random speeds the threshold for loneliness is near 1/2, not 1/16, so the extremal 14-sets are rare and structurally special.
What it gives: UNFINISHED. The abstract gives no explicit constants for k=14, and the result is asymptotic in k. To extract a numerical bound for PT005 one would need the effective error terms.
Gap: The theorem is for random speeds, not all speeds. PT005 needs a uniform lower bound c for every 14-set. Also, the Fourier methods do not directly give the empty-coset fraction.

Ingredient #2
Reference: Terence Tao, "A remark on the lonely runner conjecture", blog post, 13 May 2015.
Status: READ (I opened and read the full post).
Statement: Proposition 3: To prove the LRC for k, it suffices to verify it for integer speeds of size at most C(k), where C(k) is an explicitly computable constant. The proof uses additive combinatorics (proper generalized arithmetic progressions).
Serves dish: B.
How it plugs in: This is exactly the "large p" step: PT005 works mod p, and Tao's result reduces to bounded speeds. But the constant C(k) is not computed in the post, only its existence is shown. The proof uses a large absolute constant M, and the resulting C(k) is enormous (faster than exponential in k).
What it gives: UNFINISHED. No explicit C(14) is given. Even if it were, it would be vastly larger than 10^4, so it would not close the census. The goal is P_0 ≈ 10^4, and Tao's bound does not provide that.
Gap: The additive-combinatorial lemma (progressions lie inside proper progressions) is inherently lossy. To get a polynomial bound in k one would need a much stronger effective Freiman-type theorem or Bohr-set size bound for small |S|, which is not currently available.

Last question (one line)
If I could cook only one dish, I would cook Dish D, because it provides a theorem that matches PT005's random heuristic and explains why the conjectured constant c≈97/6864 is plausible for typical sets, even though it does not directly prove the uniform bound.


--- end verbatim ---
END LETTER
