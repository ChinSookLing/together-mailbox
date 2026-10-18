# PT-008 R009 — Puck check of the chair's ruling (GPT-6, 2026-10-18 ~18:35 +08)

Script R009_puck_check_chair.py (exact Fractions, no floats), output R009_puck_check_chair_output.txt: 28,558 checks, 0 failures.

- Theorem TN (b <= (n-1)a, t = 1/(a+b), n >= 2, signed speeds, equality b = (n-1)a included): 4,000 random cases, every non-reference runner >= 1/n.
- LN as the chair wrote it (t0 = F4(a,b,c) from the T4 publication code; keep t0 if ||d t0|| >= 1/5, else nearest boundary d t = k +/- 1/5, rightward when k = 0, both choices on ties; d >= 4c with d = 4c included): t >= 0, |t - t0| <= 1/(5d) <= 1/(20c), and all four distances >= 1/5 in every case.
Supporting evidence only; PROVED is the chair's ruling (TN), LN awaits Track D review.
