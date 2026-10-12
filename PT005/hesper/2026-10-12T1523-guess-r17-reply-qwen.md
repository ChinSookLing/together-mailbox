BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:23 +08
RE: 猜公式 Round 17 literature walk (packet ad54489), send text r17_send_full.txt or r17_send_short.txt
SEAT: qwen
MODEL: Qwen3.8-Max Thinking (web toggle on, seat says no web tool)
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---

Conclusions first

Honesty preamble (important):
I have no web-search / browsing tool available in this session, so I cannot READ or ABSTRACT-check any paper right now. Every reference below is therefore MEMORY and unverified. The chair's seed list already warns these may be misremembered; I treat mine the same way. Where I am not confident even that a paper exists as stated, I say so explicitly rather than risk a fabricated citation. No new literature constant is reported as fact; literature-derived numbers are UNFINISHED. The only numbers I report are my own hand computations.

What I can give this round:
(1) a memory-based map of which papers likely serve which dish; (2) my own computed comparison of the target constant 97/6864 against L17's 240⁻¹⁴; (3) my own computed (7/8)^14 for Dish D. Everything that requires opening a paper is UNFINISHED.

My own computations (the only numbers I'm allowed to report)

FACT (hand computation).
The empty-coset / random-safe benchmark for Dish D:
(7/8)^14 = 7^14 / 8^14 = 678,223,072,849 / 4,398,046,511,104 ≈ 0.15421007.
I computed 7^14 = 678,223,072,849 (via 7^8=5,764,801, 7^12=13,841,287,201, ×49) and 8^14=2^42=4,398,046,511,104.

FACT (hand computation).
Target floor constant:
m* = 97/6864 ≈ 0.0141317.
(6864×0.014=96.096; remainder 0.904; 0.904/6864=0.0001317.)

FACT (hand computation).
The deficit ratio used in Rounds 12–14:
δ = m* / (7/8)^14 = 0.0141317 / 0.15421007 ≈ 0.09164.

FACT (hand computation).
The gap Dish A must close. With log10(240)=2.380211, we get 14·log10(240)=33.322954, so 240⁻¹⁴ ≈ 10^{-33.323}. Also log10(m*)=log10(0.0141317)=−1.8498. Hence m* is larger than L17's 240⁻¹⁴ by a factor of about 10^{33.323 − 1.850} = 10^{31.47}.
So Dish A needs to gain roughly 31.5 decimal orders of magnitude over the current proved constant.

Ingredient cards

Global caveat: all five are MEMORY (no browsing available). Verify author/title/year/venue/statement before any use.

Ingredient #1
Reference: Terence Tao, remarks on the lonely runner conjecture (exact title/venue NOT confirmed)
Status: MEMORY (cannot verify in this session)
Statement: I believe Tao discussed reducing the lonely runner conjecture to bounded speeds and discussed gap/measure improvements. I CANNOT reliably state the exact theorem, bound, or year from memory.
Serves dish: B (bounded-speeds reduction), partly A (gap/measure)
How it plugs in: Directly relevant to L16's "make all speeds small" step (Lemma B) and to Round 16 Line B's goal of replacing the Dirichlet step.
What it gives: UNFINISHED — I cannot quote the actual bound without the paper.
Gap: Must locate the paper and extract the exact bounded-speeds reduction and any explicit gap constant.

Ingredient #2
Reference: Goddyn & Wong, "tight instances" of the lonely runner conjecture (year/venue NOT confirmed; seed says 2006)
Status: MEMORY
Statement: I recall this concerns extremal/tight speed sets for which the lonely time is exactly 1/(n+1). I CANNOT confirm the exact classification or statements from memory.
Serves dish: C (why the extremal set is {1..15}∖{6})
How it plugs in: If tight instances have a known structure, it could explain why omitting 6 is forced and guide C-floor.
What it gives: UNFINISHED — no constant extractable from memory.
Gap: Need the actual tight-instance characterization; unknown whether it addresses threshold 1/16 with 14 speeds specifically.

Ingredient #3
Reference: Czerwiński, "Random runners are very lonely" (year NOT confirmed; seed says ~2012)
Status: MEMORY
Statement: I recall a result that for random speed sets the lonely time is close to 1/2 (much larger than 1/(n+1)) with high probability. Exact theorem NOT confirmed from memory.
Serves dish: D (random model)
How it plugs in: Would justify treating a random 14-set as having U≈E(p) with small deviation, i.e. that the resonance R(S) is typically tiny — the backbone of our count formula.
What it gives: My own computed benchmark (7/8)^14 ≈ 0.15421007 (above). Literature threshold: UNFINISHED.
Gap: Need the exact concentration statement and whether it covers our fixed-density (H≈p/16) regime.

Ingredient #4
Reference: Czerwiński & Grytczuk, "Invisible runners in finite fields" (year/venue NOT confirmed; seed says ~2008)
Status: MEMORY
Statement: I recall a finite-field / modular formulation of the view-obstruction problem. Exact theorem NOT confirmed from memory.
Serves dish: E (mod-p / finite field)
How it plugs in: PT005 is entirely mod p; a finite-field view-obstruction result could directly frame D(p) and the subgroup cover G_281.
What it gives: UNFINISHED — no number extractable from memory.
Gap: Must confirm the finite-field model matches our "too near iff ‖vt‖≤H" definition.

Ingredient #5
Reference: Barajas & Serra, the seven-runner case (year NOT confirmed; seed says 2008)
Status: MEMORY
Statement: I believe the lonely runner conjecture has been proved for 7 runners (and small n), but I CANNOT confirm the exact runner count settled or the method from memory.
Serves dish: C / verification baseline
How it plugs in: Establishes how far rigorous small-n verification has reached; our N=16 problem is far beyond, so this is context, not a direct tool.
What it gives: UNFINISHED.
Gap: Confirm exact n settled and whether the method is analytic (could extend) or case-specific.

What I could NOT confirm (flagging to avoid fabrication)

Malikiosis–Santos–Schymura ("linearly-exponential checking…") and Henze & Malikiosis (lattice zonotopes / covering radius): I have weak or no reliable memory of exact title/authors/year. Treat as unverified; I did not make an ingredient card for them. This is the lane the chair assigned to Dish B, so a seat with web access should prioritize confirming these.

Beck, Hoşten, Schymura "lonely runner polyhedra": not confident enough to state. Unverified.

Kravitz "barely lonely / very lonely runners": seed-listed; I cannot confirm specifics. Unverified.

A 2025 computer-assisted proof for 8+ runners: I cannot confirm this exists. Do not treat as real until a seat with browsing verifies it.

Bohr-set sharpening for small |S| (beyond |B(S,ρ)|≥ρ^{|S|}N): I recall the standard Tao–Vu bound only as MEMORY; I do not know a sharper small-|S| result. UNFINISHED.

Last question (one line)

I would cook Dish B (the threshold) — the gap between the true transition (~460) and the proved bound (~10⁴⁸⁷) is the single largest obstacle, and any effective bounded-speeds/equidistribution result would let the census close everything below it.


--- end verbatim ---
END LETTER
