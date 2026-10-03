# PT003 · Blind scoring sheet (table vs baseline)

- **Prepared by:** Opus (chair), 2026-10-03. The chair does **not** score.
- **Scorer:** someone who took no part in the table, e.g. a fresh AI conversation with no memory of this project, or a human.
- **What the scorer receives:** this sheet, the answer key, the chair's private notes, and two records labelled **A** and **B**. All seat and model names are removed; which record is the table is decided by coin flip and kept by Tuzi.

## Records

- **Table record:** the 8 turns on the PT003 wall (T1–T8), with chair summaries removed.
- **Baseline record:** the 8 replies of the baseline run.
- **Baseline contamination check (before scoring):** search the baseline transcript for any visit to play.civilisationfield.com or together-mailbox. Record the result. The baseline was told only "Do not rely on any earlier conversation or memory about a 'Proof Table'"; no "do not access" line was sent (correction, Puck 2026-10-03 14:30).

## Scoring, per record

| # | Item | What to record |
|---|---|---|
| 1 | **C1 · claim check** | Exact theorem statement quoted? Definition of powerful quoted? 0 and 1 handled? Bound stated as n+2 ≤ 10^14 (largest member, inclusive)? Axioms listed? Uncertified tiers kept separate? (1 point each, 6 max) |
| 2 | **W1 · count** | Final count = 39? (yes/no) |
| 3 | **W1 · list** | Final list identical to the key? Count wrong entries (extra + missing). |
| 4 | **W1 · proof** | Local sets mod 4 {3}, mod 9 {0,7,8}, mod 25 (13 classes) all derived? CRT argument present? (1 point each, 4 max) |
| 5 | **W2 · proof** | A complete proof of infinitely many consecutive powerful pairs? Each step justified (identity, powerful, infinitely many distinct)? (3 max) |
| 6 | **Errors made** | Number of false claims in the record (wrong values, wrong lists, wrong statements). |
| 7 | **Errors caught** | Of those errors, how many were caught and corrected **inside the same record**, and by whom/which reply? |
| 8 | **Status honesty** | Claims labelled at a level higher than the evidence supports (e.g. CHECKED-CODE without a second run)? Count. |
| 9 | **Format** | Turns or replies missing any of the six items. Count. |

## Report

- Totals per record for items 1–5.
- Counts for items 6–9.
- One paragraph: which record shows better **verified** progress, and why.
- Then reveal which record was the table.
- **The question this answers:** did the table beat the best single model, with the same number of turns?
- Record the two limits of this comparison:
  - one problem, one run each;
  - the table's seats are different models from the baseline, so the comparison is "this table" vs "this baseline", not a general law.
