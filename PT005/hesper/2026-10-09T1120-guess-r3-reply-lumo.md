BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 11:21 +08
RE: 猜公式 Round 3 packet (1aeab1c), rules header + own §A line + BEGIN…END block pasted verbatim (send text r3_send_lumo.txt)
SEAT: lumo
MODEL: Lumo 2.0 Max
CHAT: https://lumo.proton.me/u/8/c/e4221dde-840c-4244-bbc6-49dcbeec78de

--- reply verbatim ---
Worked through your question

§A: UNSURE. Chair's LP refutation checks: n/H = ((p−1)/2)/⌊(p−1)/16⌋ ≈ 8. FACT: fractional cover ≈ 8, not 14. IDEA: strengthened LPs (pair constraints, Gomory cuts) might narrow but bridging 8→14 requires eliminating exponentially many fractional solutions; integrality gap appears structural, not just weak relaxation.

§B: Route 1 (Discrepancy). DATA shows L ≈ 0.114 consistently. IDEA: uniform lower bound L₀ > 0 plausible; count of pieces may be improvable beyond Σ v ≤ 13p/N. PROOF-needed: worst-case L over all 13-sets.

§C: Jirí Matoušek. His book Lectures on Discrete Geometry + discrepancy expertise directly matches the safe-set/grid-point intersection analysis.

Least sure step: Whether a uniform L₀ > 0 bound truly holds for all 13-speed sets at threshold 1/16—the data suggests yes but exhaustive search over the combinatorial space is infeasible.

# GLM's fact 2 verification on p=311 (my choice)
def safe_set(p, speeds, thresh=1/16):
    """Compute safe set pieces as (start, end) intervals"""
    intervals = [(0,1)]  # start with full circle
    for v in speeds:
        new_int = []
        for s,e in intervals:
            # Forbidden region for speed v: ||vx|| < thresh
            # This creates gaps at multiples of 1/(2v) ± thresh/v
            gaps = []
            k_min = int(-v*s - 0.5)
            k_max = int(v*(1-e) + 0.5)
            for k in range(k_min, k_max+1):
                gap_start = max(s, (k - thresh)/v)
                gap_end = min(e, (k + thresh)/v)
                if gap_start < gap_end:
                    gaps.append((gap_start, gap_end))
            # Subtract gaps from current interval
            curr = s
            for g_s, g_e in sorted(gaps):
                if curr < g_s:
                    new_int.append((curr, g_s))
                curr = max(curr, g_e)
            if curr < e:
                new_int.append((curr, e))
        intervals = new_int
    return intervals

p = 311
speeds = list(range(1,15))  # test 14 speeds
pieces = safe_set(p, speeds)
total_len = sum(e-s for s,e in pieces)
print(f"p={p}, 14 speeds, total safe length: {total_len:.4f}, pieces: {len(pieces)}")
# Expected: near 0.11 with ~100+ pieces for valid covers

UNFINISHED

[Courier note: text reconstructed from the rendered page (Proton blocks clipboard read). Lumo's own code is float-based and was not run by Hesper.]
--- end verbatim ---
END LETTER
