BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 11:25 +08
RE: 猜公式 Round 9 (packet ec15a2d), send text r9_send_full.txt or r9_send_short.txt
SEAT: glm
MODEL: GLM-5.3 Deep Think Max, new chat, short version (thought ~25 min)
CHAT: https://chat.z.ai/c/bd523a5d-d65b-4db0-b4a4-764654f944f7

--- reply verbatim ---
1. Formula (IDEA; 1 fitted constant).
PROOF: every speed covers exactly H cells (t↦vt bijects; the arc ‖x‖<p/N contains 2H residues; t↔p−t pairing leaves exactly H in 1..n). Model: #covers ≈ C(n,N−2)·e^(−κU), U = n·e^(−(N−2)H/n); P*(N) = largest prime p with ln C(n,N−2) ≥ κU.
FACT: forcing E=1 at each last-found prime gives κ = 1.24 (N16@457, exhaustive), 1.31 (N17@479), 1.31 (N18@523), 1.24 (N20@661). Take κ=1.25. Errors (model vs known): N16: 449 vs 457 (−2%); N17: 499 vs 479 (+4%); N18: 541 vs 523 (+3%); N20: 641 vs 661 (−3%). Testable: model predicts missed covers at N17: 487, 499; N18: 541.

2. Not computed — model only (IDEA, ±15%): P*(8…15) ≈ 115, 165, 200, 235, 280, 315, 380, 420 (survivors are p ≡ 1 mod N primes).

3. P*(22): 727 (=22·33+1, E≈4). Range [700, 765], confidence 70%. Backups 709 (E≈7), 733 (E≈1); 739–761 all E<1.
P*(24): 821 (E≈2; 823 E≈1; backup 797, E≈10). Range [785, 860], confidence 65%. κ-drift alone moves these within [709,751] / [797,853]; E≈1 primes are search coin-flips.

4. Scattered survivors, not a cliff — a sawtooth. FACT: H is constant on blocks p∈[mN+1,(m+1)N); within a block E drops ~e^(−5) (N=20), revives at each p ≡ 1 (mod N) (λ=2(N−2)/N maximal), then block-start primes decay ×4: 601, 641, 661, 701 (E≈0.1, dead). Late survivor = fresh-H residue + Poisson luck; no extra arithmetic visible (641 is also ≡1 mod 20; p−1 smoothness uncorrelated — IDEA). Least-sure: 641's emptiness (model E≈2.3 — probable search miss, rerun) and the unexplained κ drift 1.24→1.31.

--- end verbatim ---
END LETTER
