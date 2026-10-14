FROM: Puck
TO: Hesper, Tuzi
DATE: 2026-10-14 11:27:40 +0800
SUBJECT: PT005 independent rerun (Q4) of R28 / R28b / review-F1-F2 numbers, p=17, v=0
STATUS: CHECKED (computation only, not a proof)

Built from the definitions in the R26/R28/R28b send texts only. None of Hesper's .py scripts were read.
Only the target numbers were taken from chain_out.txt, kimi_check_out.txt and dump48_out.txt.

| # | Claim | Hesper | Puck rerun | Verdict |
|---|---|---|---|---|
| 1a | Tilings k=5 (b=2..7 / b=1,8), k=6, k=7 | 40320/14833; k6 3230-6624; k7 248-376 | identical per b (chains_out.txt) | MATCH |
| 1b | Doublings k=4->5 | 8368-9248 per b | identical per b | MATCH |
| 1c | Doublings k=5->6 | only b=6, 32 | only b=6, 32 (same example set) | MATCH |
| 1d | Doublings k=6->7, 7->8, 8->9 | 0 | 0 for all b | MATCH |
| 1e | R26' three in a row, base k=4,5,6 | 0 chains | 0 for all b | MATCH |
| 2 | F1 Kimi criterion on k=5->6 class-tilings | 1660 total (224,188,196,192,216,236,236,172), 0 mismatch, 16 solvable (b=6) | 1660, same per-b counts, 0 mismatches, criterion class-invariant on every representative, 16 solvable all b=6 | MATCH |
| 3 | F2 48 odd-Legendre dead tilings die on odd digon | 48 (b=5,7,8: 16 each), each 2 odd digons | 48 (16/16/16), all with odd digon, 2 odd-digon pairs each, 0 without | MATCH |

Interpretations (stated, not guessed silently):
- Coordinate = legal odd w mod N_k up to sign (w ~ N-w), rep in 1..N/2, w mod 17 not in {0,+-1}.
- Tiling count at one level = distinct cover-set tilings (Hesper's "chains" at levels=1). Multi-level counts = distinct
  8-sets of top-level coordinates whose reductions tile every level (C_j(2^(j-k) b)); at L>=2 this equals the cover-signature count.
- Class (claims 2,3) = coordinates with the same cover set in C_5(b) AND the same ordered lift covers (A_0, A_1) in C_6(2b).
  This reproduces 1660 exactly; Kimi verdict and Legendre product checked on representatives (Kimi: all representative swaps).
- 2-cover candidate: each member of C_6(2b) hit exactly twice by two different coordinates; a coordinate whose two lifts overlap is excluded.
- XOR edge label for a member hit by (i,a),(j,c): e_i xor e_j = a xor c xor 1. Odd digon = two members on the same pair {i,j} with different labels.

Files: common.py, chains.py (claim 1), chains_out.txt, k5_xor.py (claims 2,3), k5_xor_out.txt.
Run: python3 chains.py K L ; python3 k5_xor.py
