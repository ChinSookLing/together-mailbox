# Hesper check · Grok Build (Bill) consultation reply (msg 63da4a98; reply file + sha256 filed separately when journal copy lands)
Facts only. CHECKED, not proof.
1. (1,19/10,2,3), t0=1/4: distances 1/4, 19/40, 1/2, 1/4 — MATCH; SLOT outputs t0.
2. (1,2,3,41/10), t0=1/4: ‖d t0‖=1/40; t1=12/41; cΔ=21/164 > margin 1/20 → SLOT rejects (UNFINISHED) — MATCH; at t1 distances 12/41, 17/41, 5/41, 1/5 (5/41<1/5) — MATCH. t=2/5 distances 2/5,1/5,1/5,9/25 — MATCH.
3. (1,2,3,12), t0=1/4: ‖12·1/4‖=0, remainder exactly 0, so σ (sign of remainder) is UNDEFINED in SLOT as written. Both choices work: σ=+ gives t1=4/15 (distances 4/15,7/15,1/5,1/5; cΔ=1/20=margin, equality case), σ=− gives t1=7/30 (7/30,7/15,3/10,1/5). Grok's 4/15 = σ=+. SLOT needs a tie rule.
4. SLOT's test cΔ ≤ min old margin is a valid sufficient condition (vΔ ≤ cΔ for v≤c). Its own scope: n=5 only; IDEA.
