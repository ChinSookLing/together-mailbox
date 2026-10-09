BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 16:44 +08
RE: 猜公式 Round 4 part (a) (packet 61862ac), send text r4_send_kimi.txt
SEAT: kimi
MODEL: Kimi K3, Thinking effort Max, web off
CHAT: https://www.kimi.ai/chat/1a11fce9-0272-807b-8000-09ce456c3773

--- reply verbatim ---
[Courier note: assembled from the browser's verbatim read of the final answer (fields in page order). Kimi used 3 Python tools on training primes only.]

ANSWER BLOCK Q3 predictions (rows / surv. L2 / gate closes = alive L16 = 0?):
p = 307 (H=19, n=153, p≡3 mod 16): rows ≈ 10^6.9 ≈ 8×10⁶, range 3×10⁶–2×10⁷ (conf. ~65%). Surv. L2 ≈ 4×10³, range 10³–3×10⁴ (~60%). Gate closes: yes (~90%).
p = 337 (H=21, n=168, p≡1): rows ≈ 10^6.5 ≈ 3×10⁶, range 10⁶–10⁷ (~65%; two independent extrapolations agree at 10^6.5). Surv. L2 ≈ 7×10², range 50–5×10³ (~60%). Gate closes: yes (~92%).
p = 383 (H=23, n=191, p≡15): rows ≈ 10^4.9 ≈ 8×10⁴, range 2×10⁴–5×10⁵ (~55%). Surv. L2 ≈ 3, range 0–60 (~55%). Gate closes: yes (~95%); pure-(a) gate consistent with this.
Q1: rows(p) ≈ C(n,15)·e^{−n(1−H/n)^15}/(p−1)·e^{0.16−0.24H}: binomial growth loses to exponential covering decay, peaking near H≈15–17; r=(p−1) mod 16 sets coverage density H/n (r=0 densest, hence 241 ≫ 239).
Q2: The 409 survivor is (a scaling of) the tight row {1,…,15} — the only cover whose torus-good point sits at the dyadic boundary 1/16, hence hardest to kill on 2^k·p grids.
Q4: Conjecture: for large p every irredundant row is a reduction of a bounded-height integer tuple whose uncovered torus set has only 2-power denominators — finitely many "ancestors," and rows(p) stabilizes at their count. Cheap test: compute min-over-scalings height of all 401/409 rows; it should stay bounded and the counts should converge.
Q5: Enumerate bounded-height integer ancestors directly, not rows mod p — that turns the 10¹²-node search into a finite ledger, exactly as L15/L16 did for (b)/(c).

Reasoning (FACT/PROOF/IDEA).
IDEA: model a random 15-class set as covering with Poisson rate n(1−H/n)^15; rows ≈ C(n,15)·e^{−n(1−H/n)^15}/(p−1) times an irredundancy factor.
FACT: fitting the 17 training rows, the residual to this model drifts as 0.16−0.24·H (RMS scatter ≈0.5 dex); 337's prediction is corroborated by pure r=0 interpolation 241→401 (10^6.50).
IDEA: the drift means irredundancy bites harder as H grows — large-H covers must be near-equidistributed, forcing bounded integer height (supports Q4).
FACT: log(surv/rows) fits 2.99−0.068·n across 13 points (residual ≤1.3 dex).
FACT: alive L16 = 0 at all 15 completed primes, including 1.1×10⁶ L2-survivors at 241 — hence the high gate-closure confidence.
PROOF: at x=1/16, min distance of i·x (i=1..15) is exactly 1/16, failing strict "<1/16", and 1/16 first appears on the 16p grid — matching the FACT that {1..15} dies only at level 16 at p=401.
IDEA: 383's r=14 sparsity (H/n=0.120 vs 0.125) plus H=23 drift shrinks rows fastest of the three.
Least-sure step: the −0.24·H residual slope is anchored mainly by the two H=25 points; if it flattens or steepens beyond H=15, the 383 row count moves most (my stated ranges absorb ~±0.7 dex of this).
UNFINISHED: no independent orbit-count audit of the engine's canonical row counts.

--- end verbatim ---
END LETTER
