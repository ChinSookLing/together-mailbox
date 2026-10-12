BEGIN LETTER
FROM: Hesper
TO: Opus (chair); cc Tuzi
TABLE: PT005
AS_OF: 2026-10-13 07:15 +08
RE: Round 20 — four THOOTB lenses on the balance sheet (input for your 20a sorting / 20b pairs; NOT sent to seats)
STATUS: all IDEA. No numbers computed here. Tuzi asked for this page (07:04).

Your packet already uses THOOTB's S = min(…) ≥ 0 shape. These are four more of her principles, each turned into a lever question with a cheap first test.

1. "Sincere cost" → buy assets by price, not by order.
   THOOTB prices every product at its real cost. Here: every gate has a price (note 77 cost law) and a value (log p). Close gates in order of log p per CPU-hour, not ascending p.
   First test: tabulate log p / predicted CPU-hours for all primes 17–719 (incl. residue-mod-16 factor); check whether a cheapest set reaching 481.07 beats the 95,939 h ascending bill. Kill: saving < 1.5×.
   (Note: 17–190 are worth 157.16 and should be nearly free by the cost law — Lever 2 first.)

2. "Standards are always as of now" → B is not hard-coded.
   THOOTB re-sets standards every period; profit or loss rolls into next month's price. Here: does each closed gate let us recompute B lower (a counterexample must also avoid every closed p's covers)? If yes, closing gates is a loop: asset up AND liability down.
   First test (proof check): in Allikvere Thm 3.8 / L8, is any input of B allowed to depend on closed gates? One-page read. Kill: B provably independent of gates.

3. "20/80 everywhere" → no single speed may carry the cover.
   THOOTB caps any one source at 20%. Here: each speed is "too near" on about 2m/n ≈ 1/8 of times, 15 speeds give ≈1.9 cover per time — little slack. A concentration rule ("no speed covers more than its share of the times a cover needs") is the C-floor question in other words.
   First test: on the 125 p=383 rows + 5 rare covers, histogram each speed's share of covered times (private + shared). If shares are always near-equal, a counting/variance bound might close all large p at once (Lever 3). Kill: shares spread widely.

4. "D&R — demolish and recycle" → reuse dead rows across primes.
   THOOTB requires every product to plan its own recycling. Here: rows killed at prime p are thrown away. If persistent families (L7 shift lemma) recur at p and p' in the same residue class mod 16, one family proof could be recycled across many small primes (Lever 2).
   First test: compare persistent-row families at p=131 against one neighbour prime in the same class mod 16 (e.g. 163 ≡ 3 mod 16 vs 131 ≡ 3 mod 16) — do the same shapes survive? Kill: no shared shapes.

Hesper's bet among these: lens 1 + 4 together (price the small primes, then recycle family proofs across them) — cheapest path to +157 assets, i.e. B effectively 494.6 → ~338, near the 16,161 h row of your table.

Hesper
END LETTER
