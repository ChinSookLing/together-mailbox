BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:52 +08
RE: 猜公式 Round 17 ADDENDUM reply (Opus 9c7d507 seed addendum, sent as follow-up in same chat), send text r17_addendum_send.txt
SEAT: lumo
MODEL: Lumo 2.0 Lite (web on)
CHAT: https://lumo.proton.me/u/29/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
New Ingredient: F5 (Allikvere)
[warning callout] Verified existence of 'Fourteen and fifteen lonely runners' (arXiv:2609.02604). Confirms the 'single implementation' warning: the proof relies on one massive search routine. If that code has a bug, the constant c=240^-14 collapses.

Ingredient 3: Dish A (Constant)
Reference:
Allikvere, T. (2026). "Fourteen and fifteen lonely runners."
arXiv:2609.02604.
Status:
ABSTRACT (Verified listing; full text unread).
Statement:
Establishes m(K) ≥ 240^−14 for 14-sets via an automated exhaustive search of a specific reduced domain.
Serves dish: A
How it plugs in:
Provides the current baseline c = 240^−14 for L17. The "single implementation" note implies the proof is fragile; a formal independent verification of the search logic is required to trust this constant.
What it gives:
UNFINISHED (Cannot verify the constant's robustness without reading the code/logic).
Gap:
Need to confirm if the search space reduction is mathematically sound or just heuristic.

Ingredient 4: Dish E (Finite Fields)
Reference:
Sungkawichai, P., & Trakulthongchai, S. (2026). "Eleven, twelve, and thirteen lonely runners."
arXiv:2604.23906.
Status:
ABSTRACT (Verified listing).
Statement:
Includes a partial result for the Lonely Runner Conjecture over Z_p for n ≤ 13, showing that for large p, the discrete gap matches the continuous gap within O(1/p).
Serves dish: E
How it plugs in:
Directly supports the "Discrete-to-Continuous" bridge needed for Dish B. If the O(1/p) bound holds for n = 14, it validates using m(K) to predict D(p) for p > 10^4.
What it gives:
UNFINISHED (Need the exact error term coefficient for n = 14).
Gap:
Extension to n = 14 is not claimed in the title; must check if the method generalizes.

One line answer:
My one-dish pick remains Dish B, but the Allikvere paper (Dish A) adds a critical vulnerability: if the "single implementation" is flawed, the entire threshold calculation collapses, making the verification of that code the new priority.

[1 file attached by Lumo]

OBSERVATIONS:
- Lumo gave 2 new ingredient cards (Ingredient 3: Allikvere for Dish A; Ingredient 4: Sungkawichai & Trakulthongchai for Dish E), both Status ABSTRACT, both UNFINISHED. This is within the "at most 2 more ingredient cards" limit.
- A leading "New Ingredient: F5 (Allikvere)" warning callout appears before the cards.
- Of the 5 seeds, only 2 were turned into cards (Allikvere 2609.02604 and Sungkawichai & Trakulthongchai 2604.23906). The other 3 seeds (2609.06259 "Lonely Runner Relations", 2605.27941 "Mixed thresholds", 2609.23952 Poliakova shifted) are not present in the reply — Lumo did not add cards for them and did not explicitly say "none usable" for them.
- One-dish pick: unchanged — remains Dish B, with a caveat about Allikvere's single-implementation risk.
- Reply did not use an explicit "ADDENDUM REPLY" header label, but it is the reply to the addendum.
- Word count of reply body exceeds the ≤300 word constraint in the message; flagging only.
- Note on formatting: Lumo's reply text shows the exponents as separate tokens (e.g., "240 − 14", "10 4", "1 / p") when rendered linearly; these represent 240^−14, 10^4, and O(1/p) respectively.

--- end verbatim ---
END LETTER
