BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-10 10:56 +08
RE: 猜公式 Round 5 (packet 4640c52), send text r5_send_kimi.txt
SEAT: kimi
MODEL: Kimi K3 High
CHAT: https://www.kimi.ai/chat/1a1231e4-7012-87e0-8000-09ce1972343a

--- reply verbatim ---
[Hesper note: assembled from the browser's verbatim capture, taken in four segments and joined at their overlaps; the reply's thinking and 38 Python tool calls are excluded.]

ANSWER BLOCK
Q3 predictions (rule: class-5/9 primes keep covers; other classes are dead above their Data-1 threshold): 503: 0 (80%) · 509: 0 (85%) · 521: >0 (60%) · 523: 0 (80%) · 541: 0 (85%) · 547: 0 (80%) · 557: 0 (85%) · 563: 0 (80%) · 569: >0 (55%) · 571: 0 (80%) · 577: 0 (80%) · 587: 0 (80%) · 593: 0 (80%) · 599: 0 (80%)
Q1. Rule: covers = 0 iff p mod 16 ∈ {1,3,7,11,13,15} AND p exceeds a class threshold T_c (fitted between each class's last >0 and first 0: T₁∈(401,433), T₃∈(419,467), T₇∈(359,439), T₁₁∈(379,443), T₁₃∈(349,397), T₁₅∈(367,383)); covers > 0 whenever p mod 16 ∈ {5,9} (⟺ n mod 8 ∈ {2,4}) or p < T_c. Score: 33/33 on Data 1 (8 fitted thresholds — overfit risk flagged).
Q2. Exact reformulation: speed v covers cells = folded times-table {canon(j·v⁻¹): j ≤ H}, so a cover = 14 moduli whose H-truncated tables cover [1..n]. 457 works because 457 = 4·114+1: modulus 4 has canon(4·114) = 1, so its folded table wraps into short residues; its cover contains modulus 4, and the speed-run 111..117 near −1/4 is the inverse image of that. Family: p = km+1 ⇒ modulus k's table covers extras |kj′−i|.
Q4. FACT: every Data-2 cover scales to max speed ≤ 6.3H ≈ 0.39p (457: 3.1H). Cover structure beats Dirichlet's p^13/14 by a huge margin — the wall may be an artifact of unstructured sets.
Reasoning
FACT (verified 3×, with negative controls): my bit-verifier reproduces all 19 Data-2 covers, L15 at 499, and Data 3's boundary (no 13-cover at 239; 13-covers at 233/241/251/263). Definitions match the table's.
FACT (class-monotonicity): inside every mod-16 class of Data 1, covers > 0 up to a threshold, then all 0 — no interleaving. Classes 5 and 9 (n mod 8 = 2 or 4) show no zero through 499; class 9 survives to 457.
PROOF (reformulation): v too near at t ⟺ vt ≡ ±j (j ≤ H) ⟺ t ≡ ±j·v⁻¹. So cover(S) ⟺ ∪_{w∈S⁻¹} {canon(jw): j≤H} = [1..n]. Scaling v→uv permutes moduli by u⁻¹ — the criterion is automatically scale-invariant, and WLOG modulus 1 ∈ W (matches all Data-2 covers containing 1 after scaling).
IDEA (mechanism): p = km+1 makes canon(mk) = 1, so modulus k's folded table hits both multiples of k and short wrap residues |kj′−i|. Small-k decompositions (457 = 4·114+1) buy coverage that generic primes lack. Class 5/9 resistance may come from n = 8H+2, 8H+4 forcing favorable factorizations of cells near n and p−t — UNFINISHED.
FACT (by-product): each zero prime has an explicit irredundant 15-cover of form {1..15}∖{k}∪{2k}, e.g. 383: {1..13,15,28} (verified cell by cell). Useful witnesses for γ = 15 in the ledger.
IDEA (Q4 bridge): covers scale to O(H) because moduli can be chosen ≤ ~6H — their tables are short intervals, so a unit exists making everything small simultaneously. Lemma B's p^13/14 assumes no structure; a cover IS structure. If provable, γ(p) ≤ 14 candidates always admit polynomial-size witnesses, and the Dirichlet wall concerns only non-cover sets.
Least-sure step: the two >0 calls (521, 569). Class 9 has no observed zero, but its threshold is only bounded below by 457; one data point (457) carries the whole prediction. If the office PC shows 0 at 521, the rule collapses to 'everything ≥ 503 is 0' and the criterion question reopens.

--- end verbatim ---
END LETTER
