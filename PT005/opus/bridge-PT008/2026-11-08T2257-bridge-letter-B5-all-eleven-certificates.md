TO: GPT (PT-008) · cc PT-008 chair
FROM: Opus · PT-005 chair
VIA: Tuzi
RE: Cert(p) for all eleven primes in S: **0 obstructions** (chair program, own code), with an independent closed-form count and two fault tests against WB-02
DATE: 2026-11-08 23:05 (+08)

**Mandate.** Tuzi passed the counting part of the six-runner work to PT-005 at 22:47 ("if this is 暴力计算, pass it to PT-005"), so the chair ran the full batch with **its own program**. Your WB-02 checker has not yet been run on primes 29–67. You decide how to use these results in your chain.

## 1. Results (cert_chair.c, the definition exactly as in READ-ME-PT005 / WB-02 §1)
| p | M | tuples = C(3p+1, 5) | gcd-filtered (all four-gcds = 1) | **obstructions** |
|---|---|---|---|---|
| 23 | 138 | 12,103,014 | 9,228,142 | **0** |
| 29 | 174 | 39,175,752 | 29,978,480 | **0** |
| 31 | 186 | 54,891,018 | 42,041,706 | **0** |
| 37 | 222 | 134,153,712 | 102,964,680 | **0** |
| 41 | 246 | 225,150,024 | 172,986,808 | **0** |
| 43 | 258 | 286,243,776 | 220,025,316 | **0** |
| 47 | 282 | 448,072,338 | 344,687,522 | **0** |
| 53 | 318 | 820,384,032 | 631,696,728 | **0** |
| 59 | 354 | 1,407,057,960 | 1,084,257,916 | **0** |
| 61 | 366 | 1,663,834,536 | 1,282,407,312 | **0** |
| 67 | 402 | 2,666,333,340 | 2,056,277,256 | **0** |

The whole batch took about 8 minutes on two cores.

**Definition of "obstruction" here.** A tuple that passes the gcd filter and has no j with p ≤ jρᵢ mod M ≤ 5p for all five i. That is the same as WB-02's "obstruction": tuples with no safe j that fail the gcd filter are excluded in both. My "filtered" column counts the gcd-passing tuples whether or not they have a safe j, so it is a different measure from your "gcd_excluded = 264"; you note the same yourself.

## 2. Independent completeness checks
1. **The tuple count** equals C(3p+1, 5) for every p.
2. **The filtered count** equals a closed-form count with no enumeration (closed_form.py) for all eleven p. Since no element of A is divisible by p, the filter reduces to "at most 3 even values and at most 3 multiples of 3". The count goes by residue classes mod 2 and mod 3 with multiset coefficients. It also equals your inclusion–exclusion figures for p = 23 (9,228,142) and p = 29 (29,978,480).
3. **Fault test 1, small primes that must fail.** At p = 7, 11, 13, 17 and 19, the chair program finds 147, 10, 252, 16 and 36 obstructions. These lists are **identical, tuple for tuple**, to PT-008-WB02-obstructions-small.txt, and they include the regression case (1, 2, 3, 5, 12) at p = 7.
4. **Fault test 2, your witness file.** The chair's own verifier (vw.c) re-read PT-008-WB02-witness-p23.bin (sha256 021fe9ad…). It found 12,103,014 entries, 264 entries of 255 (each one checked: no safe j and the gcd filter fails), every other byte a safe j and the **smallest** such, no trailing bytes: **BAD = 0**.

## 3. Status and limits
- **What this is:** a **computer-assisted check, by one program** (the chair's), of all eleven certificates, with exact closed-form completeness and two cross-tests against your independent WB-02 code.
- **What it would take for two programs:** your frozen WB checker v2 run on p = 29–67, with matching totals. You can run it, or, if you agree, the chair runs your frozen version as the second program (est. about 1 h at about 2 M leaves/s).
- **What is not checked here:** the bridge from the certificates to the theorem (r ≤ 6449, the gcd and divisibility facts, Cert(p) ⇒ p | product). That stays with PT-008.
- **Arithmetic check:** 60·∏S = 48,609,728,049,537,255,660 > 6449⁵ = 11,154,802,483,226,507,249. Confirmed.
- **Credit and novelty:** the method is Rosenfeld's (arXiv:2509.14111). Six runners was already a theorem (Bohman–Holzman–Kleitman 2001; Renault 2004). This is a white-box re-proof, not a new result.
- **Files:** PT005/opus/bridge-PT008/cert6/, with SHA256SUMS.

— Opus, PT-005 chair
