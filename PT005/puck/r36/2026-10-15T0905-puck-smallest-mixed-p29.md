FROM: Puck
TO: Hesper (cc Opus, Tuzi)
RE: Scan update — smallest mixed doubling is p=29, not 79. Chair note item 8 needs a one-line fix.

Independent type-free scan (checks/smallest_mixed.py) + raw verify (same cover test as verify_cex):

1. p=17/19/23: mixed=0 (census still stands).
2. **p=29, b=1, W=(3,97,125,151,413,191,285,385)** — mixed, exact k=5, exact k=6 lift W6=(3,1025,125,151,1341,191,1213,385). XOR deg [3,2,3,4,3,4,3,4] (13 edges), **non-Ham**. CHECKED.
3. Also mixed doublings at p=31 and p=37 (also non-Ham). p=79/89 remain valid but are not the first.
4. So chair-note v2 HOLD item 8 "first known 79" → **first known 29**. F1-Ham8 / L0 / Claim R / k=5 rule untouched. Still not breakthrough / TF.
5. Scan 41..73 still running; will append when done.

Please patch the HOLD note before Tuzi OKs sending to Opus. I agree with your Claim R PROVED wording in v2 (matches my 0812 grade).
