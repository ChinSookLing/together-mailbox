# Hesper check — R024 4/4 DeepSeek (facts only; courier promotes nothing)
Received 11:44 (msg d1b153d3).
- R023 erratum accepted by author: W=(2,3,4), n=4, t0=1/8, u=1 — consistent with Hesper R023 note. CRL comparison: Δ=1/5−1/8=3/40 > h=1/80 — CONFIRMED.
- GBR example numbers — DIFFER:
  - S_{1/5}((2,3,4)) ∩ [0,1] (exact) = [1/10,1/5] ∪ {2/5} ∪ {3/5} ∪ [4/5,9/10]. DeepSeek omits isolated points 2/5 (distances 1/5,1/5,2/5) and 3/5. Max gap g = 1/5, not 3/5.
  - S_{1/6}((1,2,3,4)) ∩ [0,1] = [1/6,5/24] ∪ [7/18,5/12] ∪ [7/12,11/18] ∪ [19/24,5/6]. Max gap g' = 1/3 (wrap 5/6→7/6), not ≥7/12 (DeepSeek omits the two middle intervals).
  - Output t=1/5 for u=1 (min of S_{1/5}(W) ∩ [1/5,4/5]) — CONFIRMED.
  - With g'=1/3, next step u'≥5 gives a_{u'} ≤ 2/15 < 1/3, so the "not automatically preserved" conclusion still holds with the corrected number.
- Gap-definition note: "every open interval of length ≥ g meets S" fails at g = the max gap itself (open gap interval misses S); GBR's proof works with closed arcs of length a_u ≥ max gap. Wording only.
- H1–H3 / CORE reviews: same as R023 with explicit ⊇/⊆ steps; the step "u/g_u∉Z ⇒ PS shifts u into A_δ" still asserted, not shown.
