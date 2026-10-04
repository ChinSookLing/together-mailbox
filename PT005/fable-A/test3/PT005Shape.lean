/-
PT005 · TESTING TURN 3 · seat: Fable-A
Lean 4.30.0, Mathlib v4.30.0 (commit c5ea00351c28e24afc9f0f84379aa41082b1188f)

Builds on PT005.lean (sha256 d5c5d22e…be7505), imported unchanged.

The shape lemma for 15 speeds:
  for every u : Fin 15 → ℝ with all u_i ∈ (0,1] and some u_i = 1,
     H u = (Σ_i w(u_i)) · Π_i a(u_i) > 900,
  where q x = 1 + 2x − x², a x = q x / x^(2/15) (real power), w x = x² / q x.

  D1  `D1`            ∀ x ∈ (0,1], a x > 8/5
  D2  `D2`            Case 2 (at least two coordinates equal to 1)
  D3  `D3`            L strictly decreasing on (0, 3/35]
  D4  `shape_lemma`   the reduction and the full statement

No sorry / admit / native_decide / new axioms.
Commands:  lake build PT005   then   lake env lean PT005Shape.lean
-/
import PT005

namespace PT005

open Set

/-! ## Definitions -/

/-- `a x = q x / x^(2/15)` (real power). -/
noncomputable def aR (x : ℝ) : ℝ := qR x / x ^ ((2 : ℝ) / 15)

/-- `w x = x² / q x`. -/
noncomputable def wR (x : ℝ) : ℝ := x ^ 2 / qR x

/-- `H u = (Σ_i w(u_i)) · Π_i a(u_i)` for 15 speeds. -/
noncomputable def H (u : Fin 15 → ℝ) : ℝ := (∑ i, wR (u i)) * ∏ i, aR (u i)

/-- `14x² − 13x + 1`, the numerator in `d/dx log a`. -/
noncomputable def quadR (x : ℝ) : ℝ := 14 * x ^ 2 - 13 * x + 1

/-- `15·log a = 15·log q − 2·log x`. -/
noncomputable def ga (x : ℝ) : ℝ := 15 * Real.log (qR x) - 2 * Real.log x

/-- `A15 x = q(x)^15 / x²`, the 15th power of `a`. -/
noncomputable def A15 (x : ℝ) : ℝ := qR x ^ 15 / x ^ 2

/-- `L x = q(x)(1 − 13x + 14x²) / (15x²(1+x))`. -/
noncomputable def LR (x : ℝ) : ℝ :=
  qR x * (1 - 13 * x + 14 * x ^ 2) / (15 * x ^ 2 * (1 + x))

/-! ## D1 — `a x > 8/5` on `(0,1]` -/

theorem hasDerivAt_qR (t : ℝ) : HasDerivAt qR (2 - 2 * t) t := by
  have ha := ((hasDerivAt_id' t).const_mul (2 : ℝ)).const_add (1 : ℝ)
  have hb := hasDerivAt_pow 2 t
  have hc := ha.sub hb
  convert hc using 1
  norm_num

/-- `d/dx (15·log a) = −2(14x² − 13x + 1) / (x·q(x))`. -/
theorem hasDerivAt_ga {x : ℝ} (h0 : 0 < x) (h1 : x ≤ 1) :
    HasDerivAt ga (-2 * quadR x / (x * qR x)) x := by
  have hq : 0 < qR x := qR_pos h0.le h1
  have h := (((hasDerivAt_qR x).log hq.ne').const_mul (15 : ℝ)).sub
    ((Real.hasDerivAt_log h0.ne').const_mul (2 : ℝ))
  convert h using 1
  have hx : x ≠ 0 := h0.ne'
  have hq' : qR x ≠ 0 := hq.ne'
  field_simp
  unfold quadR qR
  ring

theorem ga_eq_log {x : ℝ} (h0 : 0 < x) (h1 : x ≤ 1) : ga x = Real.log (A15 x) := by
  have hq : 0 < qR x := qR_pos h0.le h1
  unfold A15 ga
  rw [Real.log_div (pow_pos hq 15).ne' (pow_pos h0 2).ne', Real.log_pow, Real.log_pow]
  push_cast
  ring

theorem A15_pos {x : ℝ} (h0 : 0 < x) (h1 : x ≤ 1) : 0 < A15 x :=
  div_pos (pow_pos (qR_pos h0.le h1) 15) (pow_pos h0 2)

theorem A15_le_of_ga_le {a b : ℝ} (ha0 : 0 < a) (ha1 : a ≤ 1) (hb0 : 0 < b) (hb1 : b ≤ 1)
    (h : ga a ≤ ga b) : A15 a ≤ A15 b := by
  rw [ga_eq_log ha0 ha1, ga_eq_log hb0 hb1] at h
  exact (Real.log_le_log_iff (A15_pos ha0 ha1) (A15_pos hb0 hb1)).1 h

/-- `14x² − 13x + 1 ≥ 0` on `(0, 23/280]` (equivalent in content to B2's `(107/10)² > 113`). -/
theorem quadR_nonneg_low {x : ℝ} (hx : x ≤ 23/280) : 0 ≤ quadR x := by
  unfold quadR
  nlinarith [mul_nonneg (sub_nonneg.2 hx) (by linarith : (0 : ℝ) ≤ 13 - 14 * (x + 23/280))]

/-- `14x² − 13x + 1 ≤ 0` on `[237/2800, 3/8]` (B2's `(1063/100)² < 113` at the left end). -/
theorem quadR_nonpos_mid {x : ℝ} (hx1 : 237/2800 ≤ x) (hx2 : x ≤ 3/8) : quadR x ≤ 0 := by
  unfold quadR
  nlinarith [mul_nonneg (sub_nonneg.2 hx1) (sub_nonneg.2 hx2)]

/-- `a` is decreasing on `(0, 23/280]`. -/
theorem ga_l_le {x : ℝ} (h0 : 0 < x) (hx : x ≤ 23/280) : ga (23/280) ≤ ga x := by
  have hanti : AntitoneOn ga (Icc x (23/280)) := by
    apply antitoneOn_of_deriv_nonpos (convex_Icc _ _)
    · intro y hy
      exact (hasDerivAt_ga (h0.trans_le hy.1) (by linarith [hy.2])).continuousAt.continuousWithinAt
    · intro y hy
      rw [interior_Icc] at hy
      exact (hasDerivAt_ga (h0.trans hy.1)
        (by linarith [hy.2])).differentiableAt.differentiableWithinAt
    · intro y hy
      rw [interior_Icc] at hy
      have hy0 : 0 < y := h0.trans hy.1
      have hy1 : y ≤ 1 := by linarith [hy.2]
      rw [(hasDerivAt_ga hy0 hy1).deriv]
      have hc : 0 ≤ quadR y := quadR_nonneg_low hy.2.le
      apply div_nonpos_of_nonpos_of_nonneg
      · linarith
      · exact (mul_pos hy0 (qR_pos hy0.le hy1)).le
  exact hanti (left_mem_Icc.2 hx) (right_mem_Icc.2 hx) hx

/-- `a` is increasing on `[237/2800, 3/8]`. -/
theorem ga_h_le {x : ℝ} (hx1 : 237/2800 ≤ x) (hx2 : x ≤ 3/8) : ga (237/2800) ≤ ga x := by
  have hmono : MonotoneOn ga (Icc (237/2800) x) := by
    apply monotoneOn_of_deriv_nonneg (convex_Icc _ _)
    · intro y hy
      exact (hasDerivAt_ga (by linarith [hy.1])
        (by linarith [hy.2])).continuousAt.continuousWithinAt
    · intro y hy
      rw [interior_Icc] at hy
      exact (hasDerivAt_ga (by linarith [hy.1])
        (by linarith [hy.2])).differentiableAt.differentiableWithinAt
    · intro y hy
      rw [interior_Icc] at hy
      have hy0 : 0 < y := by linarith [hy.1]
      have hy1 : y ≤ 1 := by linarith [hy.2]
      rw [(hasDerivAt_ga hy0 hy1).deriv]
      have hc : quadR y ≤ 0 := quadR_nonpos_mid hy.1.le (hy.2.le.trans hx2)
      apply div_nonneg
      · linarith
      · exact (mul_pos hy0 (qR_pos hy0.le hy1)).le
  exact hmono (left_mem_Icc.2 hx1) (right_mem_Icc.2 hx1) hx1

/-- B3 transported to `ℝ`. -/
theorem B3_real : (8/5 : ℝ) ^ 15 * (237/2800) ^ 2 < qR (23/280) ^ 15 := by
  have h : (8/5 : ℚ) ^ 15 * (237/2800) ^ 2 < (q (23/280)) ^ 15 := B3
  unfold q at h
  have h' := (Rat.cast_lt (K := ℝ)).2 h
  push_cast at h'
  unfold qR
  exact h'

/-- B4 transported to `ℝ`. -/
theorem B4_real : (1801 : ℝ) < 4 * (8/5) ^ 13 := by
  have h : (1801 : ℚ) < 4 * (8/5) ^ 13 := B4
  have h' := (Rat.cast_lt (K := ℝ)).2 h
  push_cast at h'
  exact h'

/-- On `[23/280, 237/2800]`: `q` increasing, `x² ≤ h²`, and B3. -/
theorem A15_mid {s : ℝ} (hs1 : 23/280 ≤ s) (hs2 : s ≤ 237/2800) : (8/5 : ℝ) ^ 15 < A15 s := by
  have hs0 : 0 < s := by linarith
  have hql : 0 < qR (23/280) := qR_pos (by norm_num) (by norm_num)
  have hqmono : qR (23/280) ≤ qR s := by
    unfold qR
    nlinarith [mul_nonneg (sub_nonneg.2 hs1) (by linarith : (0 : ℝ) ≤ 2 - s - 23/280)]
  unfold A15
  rw [lt_div_iff₀ (pow_pos hs0 2)]
  calc (8/5 : ℝ) ^ 15 * s ^ 2 ≤ (8/5) ^ 15 * (237/2800) ^ 2 :=
        mul_le_mul_of_nonneg_left (pow_le_pow_left₀ hs0.le hs2 2) (by positivity)
    _ < qR (23/280) ^ 15 := B3_real
    _ ≤ qR s ^ 15 := pow_le_pow_left₀ hql.le hqmono 15

/-- On `[3/8, 1]`: `a x ≥ q x ≥ q(3/8) = 103/64 > 8/5`. -/
theorem A15_top {x : ℝ} (hx1 : 3/8 ≤ x) (hx2 : x ≤ 1) : (8/5 : ℝ) ^ 15 < A15 x := by
  have hx0 : 0 < x := by linarith
  have hq : (103/64 : ℝ) ≤ qR x := by
    unfold qR
    nlinarith [mul_nonneg (sub_nonneg.2 hx1) (by linarith : (0 : ℝ) ≤ 2 - x - 3/8)]
  have hx2' : x ^ 2 ≤ 1 := by nlinarith
  unfold A15
  rw [lt_div_iff₀ (pow_pos hx0 2)]
  calc (8/5 : ℝ) ^ 15 * x ^ 2 ≤ (8/5) ^ 15 * 1 :=
        mul_le_mul_of_nonneg_left hx2' (by positivity)
    _ < (103/64) ^ 15 := by norm_num
    _ ≤ qR x ^ 15 := pow_le_pow_left₀ (by norm_num) hq 15

theorem A15_gt {x : ℝ} (h0 : 0 < x) (h1 : x ≤ 1) : (8/5 : ℝ) ^ 15 < A15 x := by
  rcases le_total x (23/280) with h | h
  · exact (A15_mid le_rfl (by norm_num)).trans_le
      (A15_le_of_ga_le (by norm_num) (by norm_num) h0 h1 (ga_l_le h0 h))
  · rcases le_total x (237/2800) with h' | h'
    · exact A15_mid h h'
    · rcases le_total x (3/8) with h'' | h''
      · exact (A15_mid (by norm_num) le_rfl).trans_le
          (A15_le_of_ga_le (by norm_num) (by norm_num) h0 h1 (ga_h_le h' h''))
      · exact A15_top h'' h1

theorem rpow_two_fifteenths_pow {x : ℝ} (hx : 0 ≤ x) : (x ^ ((2 : ℝ) / 15)) ^ 15 = x ^ 2 := by
  rw [← Real.rpow_natCast, ← Real.rpow_mul hx]
  norm_num

/-- **D1.** For every `x ∈ (0,1]`, `a x > 8/5`. -/
theorem D1 (x : ℝ) (h0 : 0 < x) (h1 : x ≤ 1) : aR x > 8/5 := by
  have hA := A15_gt h0 h1
  have hq : 0 < qR x := qR_pos h0.le h1
  have hr : 0 < x ^ ((2 : ℝ) / 15) := Real.rpow_pos_of_pos h0 _
  unfold aR
  rw [gt_iff_lt, lt_div_iff₀ hr]
  by_contra hcon
  rw [not_lt] at hcon
  have h15 : qR x ^ 15 ≤ ((8/5) * x ^ ((2 : ℝ) / 15)) ^ 15 := pow_le_pow_left₀ hq.le hcon 15
  have h85 : ((8/5 : ℝ) * x ^ ((2 : ℝ) / 15)) ^ 15 = (8/5) ^ 15 * x ^ 2 := by
    rw [mul_pow, rpow_two_fifteenths_pow h0.le]
  rw [h85] at h15
  have hle : A15 x ≤ (8/5) ^ 15 := by
    unfold A15
    rw [div_le_iff₀ (pow_pos h0 2)]
    exact h15
  linarith

/-! ## D2 — Case 2 -/

theorem wR_nonneg {x : ℝ} (h0 : 0 ≤ x) (h1 : x ≤ 1) : 0 ≤ wR x :=
  div_nonneg (sq_nonneg x) (qR_pos h0 h1).le

theorem wR_le_half {x : ℝ} (h0 : 0 ≤ x) (h1 : x ≤ 1) : wR x ≤ 1/2 := by
  unfold wR
  rw [div_le_iff₀ (qR_pos h0 h1)]
  unfold qR
  nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ 3 * x + 1) (sub_nonneg.2 h1)]

theorem wR_one : wR 1 = 1/2 := by norm_num [wR, qR]

theorem aR_one : aR 1 = 2 := by norm_num [aR, qR]

/-- Keep two coordinates, bound the other thirteen factors by `8/5` (D1) and drop the other
thirteen (nonnegative) summands. -/
theorem H_two_lower (u : Fin 15 → ℝ) (hu : ∀ i, 0 < u i ∧ u i ≤ 1) {i j : Fin 15}
    (hij : i ≠ j) :
    (wR (u i) + wR (u j)) * (aR (u i) * (aR (u j) * (8/5 : ℝ) ^ 13)) ≤ H u := by
  have ha : ∀ k, 8/5 < aR (u k) := fun k => D1 (u k) (hu k).1 (hu k).2
  have hw : ∀ k, 0 ≤ wR (u k) := fun k => wR_nonneg (hu k).1.le (hu k).2
  have hi0 : 0 ≤ aR (u i) := by linarith [ha i]
  have hj0 : 0 ≤ aR (u j) := by linarith [ha j]
  have hj' : j ∈ (Finset.univ : Finset (Fin 15)).erase i :=
    Finset.mem_erase.2 ⟨hij.symm, Finset.mem_univ j⟩
  have hsum : wR (u i) + wR (u j) ≤ ∑ k, wR (u k) := by
    rw [← Finset.add_sum_erase _ _ (Finset.mem_univ i), ← Finset.add_sum_erase _ _ hj']
    have : 0 ≤ ∑ k ∈ ((Finset.univ : Finset (Fin 15)).erase i).erase j, wR (u k) :=
      Finset.sum_nonneg (fun k _ => hw k)
    linarith
  have hcard : (((Finset.univ : Finset (Fin 15)).erase i).erase j).card = 13 := by
    rw [Finset.card_erase_of_mem hj', Finset.card_erase_of_mem (Finset.mem_univ i)]
    simp
  have hrest : (8/5 : ℝ) ^ 13
      ≤ ∏ k ∈ ((Finset.univ : Finset (Fin 15)).erase i).erase j, aR (u k) := by
    have h := Finset.prod_le_prod
      (s := ((Finset.univ : Finset (Fin 15)).erase i).erase j)
      (f := fun _ => (8/5 : ℝ)) (g := fun k => aR (u k))
      (fun _ _ => by norm_num) (fun k _ => (ha k).le)
    rw [Finset.prod_const, hcard] at h
    exact h
  have hprod : aR (u i) * (aR (u j) * (8/5 : ℝ) ^ 13) ≤ ∏ k, aR (u k) := by
    rw [← Finset.mul_prod_erase _ _ (Finset.mem_univ i), ← Finset.mul_prod_erase _ _ hj']
    exact mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left hrest hj0) hi0
  unfold H
  exact mul_le_mul hsum hprod (mul_nonneg hi0 (mul_nonneg hj0 (by positivity)))
    (le_trans (add_nonneg (hw i) (hw j)) hsum)

/-- **D2 (Case 2).** If all `u_i ∈ (0,1]` and at least two indices have `u_i = 1`,
then `H u > 900`. -/
theorem D2 (u : Fin 15 → ℝ) (hu : ∀ i, 0 < u i ∧ u i ≤ 1)
    (h2 : ∃ i j, i ≠ j ∧ u i = 1 ∧ u j = 1) : H u > 900 := by
  obtain ⟨i, j, hij, hi, hj⟩ := h2
  have h := H_two_lower u hu hij
  rw [hi, hj, wR_one, aR_one] at h
  have hB4 := B4_real
  obtain ⟨X, hX⟩ : ∃ X : ℝ, X = (8/5) ^ 13 := ⟨_, rfl⟩
  rw [← hX] at h hB4
  linarith

/-! ## D3 — `L` strictly decreasing on `(0, 3/35]` (algebraic, no derivative needed) -/

theorem LR_sub {x y : ℝ} (hx : 0 < x) (hy : 0 < y) :
    LR x - LR y
      = (y - x) * ((1 + x) * (1 + y) * (14 * x ^ 2 * y ^ 2 - 12 * x * y + x + y)
          - 56 * x ^ 2 * y ^ 2) / (15 * x ^ 2 * y ^ 2 * (1 + x) * (1 + y)) := by
  have hx' : x ≠ 0 := hx.ne'
  have hy' : y ≠ 0 := hy.ne'
  have h1x : 1 + x ≠ 0 := (by linarith : (0 : ℝ) < 1 + x).ne'
  have h1y : 1 + y ≠ 0 := (by linarith : (0 : ℝ) < 1 + y).ne'
  unfold LR qR
  field_simp
  ring

/-- **D3.** `L` is strictly decreasing on `(0, 3/35]`. -/
theorem D3 : StrictAntiOn LR (Ioc 0 (3/35)) := by
  intro x hx y hy hxy
  have hx0 : 0 < x := hx.1
  have hy0 : 0 < y := hy.1
  have hy1 : y ≤ 3/35 := hy.2
  have hx1 : x ≤ 3/35 := hx.2
  have hxy0 : 0 < x * y := mul_pos hx0 hy0
  have h1 : x * y ≤ 3/35 * x := by nlinarith
  have h2 : x * y ≤ 3/35 * (3/35) := by nlinarith
  have h3 : x ^ 2 * y ^ 2 ≤ (3/35) ^ 3 * x := by
    nlinarith [mul_le_mul h1 h2 hxy0.le (by positivity : (0 : ℝ) ≤ 3/35 * x)]
  have hsq : 0 ≤ x ^ 2 * y ^ 2 := by positivity
  have hs14 : 0 < 14 * x ^ 2 * y ^ 2 - 12 * x * y + x + y := by nlinarith
  have hextra : 0 ≤ (x + y + x * y) * (14 * x ^ 2 * y ^ 2 - 12 * x * y + x + y) :=
    mul_nonneg (by positivity) hs14.le
  have hK : 0 < (1 + x) * (1 + y) * (14 * x ^ 2 * y ^ 2 - 12 * x * y + x + y)
      - 56 * x ^ 2 * y ^ 2 := by
    nlinarith
  have hden : 0 < 15 * x ^ 2 * y ^ 2 * (1 + x) * (1 + y) := by positivity
  have hpos : 0 < LR x - LR y := by
    rw [LR_sub hx0 hy0]
    exact div_pos (mul_pos (sub_pos.2 hxy) hK) hden
  linarith

/-! ## D4 — the reduction

One-coordinate analysis at a minimiser.  If the `j`-th coordinate `x = u_j ∈ (0,1)` is a local
minimum of `x ↦ H (u with u_j := x)`, then

    15 x² (1+x) = S · q(x) · (14x² − 13x + 1),     S = Σ_i w(u_i)          (E)

i.e. `L x = 1/S`.  Because `S − w(x) ≤ 7`, (E) forces `x < 3/35`
(`15x²(1+x) − (7q + x²)(14x² − 13x + 1) = 7(1−x)(12x−1)q`), and D3 makes all such coordinates equal.
-/

theorem hasDerivAt_wR {x : ℝ} (hq : qR x ≠ 0) :
    HasDerivAt wR ((2 * x * qR x - x ^ 2 * (2 - 2 * x)) / qR x ^ 2) x := by
  have h := (hasDerivAt_pow 2 x).div (hasDerivAt_qR x) hq
  convert h using 1
  norm_num

theorem hasDerivAt_aR {x : ℝ} (h0 : 0 < x) :
    HasDerivAt aR
      (((2 - 2 * x) * x ^ ((2 : ℝ) / 15) - qR x * ((2 : ℝ) / 15 * x ^ ((2 : ℝ) / 15 - 1)))
        / (x ^ ((2 : ℝ) / 15)) ^ 2) x := by
  have h := (hasDerivAt_qR x).div
    (Real.hasDerivAt_rpow_const (x := x) (p := (2 : ℝ) / 15) (Or.inl h0.ne'))
    (Real.rpow_pos_of_pos h0 _).ne'
  exact h

/-- The critical-point equation (E) at a one-coordinate local minimum. -/
theorem crit_eq {x C Pr : ℝ} (h0 : 0 < x) (h1 : x < 1) (hPr : 0 < Pr)
    (hmin : IsLocalMin (fun y => (wR y + C) * (aR y * Pr)) x) :
    15 * x ^ 2 * (1 + x) = (C + wR x) * qR x * quadR x := by
  have hq : 0 < qR x := qR_pos h0.le h1.le
  have hr : 0 < x ^ ((2 : ℝ) / 15) := Real.rpow_pos_of_pos h0 _
  have hw := hasDerivAt_wR hq.ne'
  have ha := hasDerivAt_aR h0
  have hd := (hw.add_const C).mul (ha.mul_const Pr)
  have hzero := hmin.hasDerivAt_eq_zero hd
  rw [Real.rpow_sub_one h0.ne'] at hzero
  unfold aR wR at hzero
  unfold wR
  generalize x ^ ((2 : ℝ) / 15) = r at hzero hr
  have hx' : x ≠ 0 := h0.ne'
  have hq' : qR x ≠ 0 := hq.ne'
  have hr' : r ≠ 0 := hr.ne'
  have key : Pr / (15 * x * qR x * r)
      * (30 * x ^ 2 * (1 + x) - 2 * (C + x ^ 2 / qR x) * qR x * quadR x) = 0 := by
    rw [← hzero]
    field_simp
    unfold quadR qR
    ring
  rcases mul_eq_zero.1 key with h | h
  · exact absurd h (div_pos hPr (by positivity)).ne'
  · linarith

/-- (E) with `S − w(x) ≤ 7` forces `x < 3/35`. -/
theorem crit_small {x S : ℝ} (h0 : 0 < x) (h1 : x < 1) (hS : 0 < S) (hC : S - wR x ≤ 7)
    (hE : 15 * x ^ 2 * (1 + x) = S * qR x * quadR x) : x < 3/35 := by
  have hq : 0 < qR x := qR_pos h0.le h1.le
  have hq' : qR x ≠ 0 := hq.ne'
  have hquad : 0 < quadR x := by
    by_contra hcon
    rw [not_lt] at hcon
    have h1' : S * qR x * quadR x ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos (mul_pos hS hq).le hcon
    have h2' : 0 < 15 * x ^ 2 * (1 + x) := by positivity
    linarith
  by_contra hcon
  rw [not_lt] at hcon
  have hw : wR x * qR x = x ^ 2 := by
    unfold wR
    field_simp
  have hSq : S * qR x ≤ 7 * qR x + x ^ 2 := by
    nlinarith [mul_le_mul_of_nonneg_right hC hq.le]
  have h2 : 15 * x ^ 2 * (1 + x) ≤ (7 * qR x + x ^ 2) * quadR x := by
    rw [hE]
    exact mul_le_mul_of_nonneg_right hSq hquad.le
  have hP : 15 * x ^ 2 * (1 + x) - (7 * qR x + x ^ 2) * quadR x
      = 7 * (1 - x) * (12 * x - 1) * qR x := by
    unfold qR quadR
    ring
  have h12 : 0 < 12 * x - 1 := by linarith
  have h1x : 0 < 1 - x := by linarith
  have hpos : 0 < 7 * (1 - x) * (12 * x - 1) * qR x :=
    mul_pos (mul_pos (mul_pos (by norm_num) h1x) h12) hq
  linarith

/-- (E) says `L x = 1/S`. -/
theorem LR_eq_of_crit {x S : ℝ} (h0 : 0 < x) (hS : 0 < S)
    (hE : 15 * x ^ 2 * (1 + x) = S * qR x * quadR x) : LR x = 1 / S := by
  have hden : 0 < 15 * x ^ 2 * (1 + x) := by positivity
  unfold LR
  rw [div_eq_div_iff hden.ne' hS.ne']
  unfold quadR at hE
  linear_combination -hE

/-- Splitting off one coordinate of `H`. -/
theorem H_update (u : Fin 15 → ℝ) (j : Fin 15) (x : ℝ) :
    H (Function.update u j x)
      = (wR x + ∑ k ∈ Finset.univ.erase j, wR (u k))
        * (aR x * ∏ k ∈ Finset.univ.erase j, aR (u k)) := by
  have hs : ∑ k ∈ Finset.univ.erase j, wR (Function.update u j x k)
      = ∑ k ∈ Finset.univ.erase j, wR (u k) :=
    Finset.sum_congr rfl (fun k hk => by
      rw [Function.update_of_ne (Finset.ne_of_mem_erase hk)])
  have hp : ∏ k ∈ Finset.univ.erase j, aR (Function.update u j x k)
      = ∏ k ∈ Finset.univ.erase j, aR (u k) :=
    Finset.prod_congr rfl (fun k hk => by
      rw [Function.update_of_ne (Finset.ne_of_mem_erase hk)])
  unfold H
  rw [← Finset.add_sum_erase _ _ (Finset.mem_univ j),
    ← Finset.mul_prod_erase _ _ (Finset.mem_univ j), hs, hp, Function.update_self]

/-- Case 3 identity: one coordinate `1`, the other fourteen equal to `t`: `H u = H1 t`. -/
theorem H_eq_H1 (u : Fin 15 → ℝ) (i0 : Fin 15) (t : ℝ) (ht0 : 0 < t) (ht1 : t ≤ 1)
    (hi0 : u i0 = 1) (hrest : ∀ j, j ≠ i0 → u j = t) : H u = H1 t := by
  have hq : 0 < qR t := qR_pos ht0.le ht1
  have hq' : qR t ≠ 0 := hq.ne'
  have hsum : ∑ k, wR (u k) = 1/2 + 14 * wR t := by
    rw [← Finset.add_sum_erase _ _ (Finset.mem_univ i0), hi0, wR_one]
    have hc : ∑ k ∈ Finset.univ.erase i0, wR (u k) = ∑ _k ∈ Finset.univ.erase i0, wR t :=
      Finset.sum_congr rfl (fun k hk => by rw [hrest k (Finset.ne_of_mem_erase hk)])
    rw [hc, Finset.sum_const, Finset.card_erase_of_mem (Finset.mem_univ i0)]
    simp
  have hprod : ∏ k, aR (u k) = 2 * aR t ^ 14 := by
    rw [← Finset.mul_prod_erase _ _ (Finset.mem_univ i0), hi0, aR_one]
    have hc : ∏ k ∈ Finset.univ.erase i0, aR (u k) = ∏ _k ∈ Finset.univ.erase i0, aR t :=
      Finset.prod_congr rfl (fun k hk => by rw [hrest k (Finset.ne_of_mem_erase hk)])
    rw [hc, Finset.prod_const, Finset.card_erase_of_mem (Finset.mem_univ i0)]
    simp
  have hpow : (t ^ ((2 : ℝ) / 15)) ^ 14 = t ^ ((28 : ℝ) / 15) := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul ht0.le]
    norm_num
  have hr : t ^ ((28 : ℝ) / 15) ≠ 0 := (Real.rpow_pos_of_pos ht0 _).ne'
  unfold H H1
  rw [hsum, hprod]
  unfold aR wR
  rw [div_pow, hpow]
  field_simp
  unfold qR
  ring

/-- For `x ≤ 1/200`, `a x > 2`. -/
theorem aR_gt_two_of_small {x : ℝ} (h0 : 0 < x) (hx : x ≤ 1/200) : 2 < aR x := by
  have hq : 1 ≤ qR x := by
    unfold qR
    nlinarith
  have hr : 0 < x ^ ((2 : ℝ) / 15) := Real.rpow_pos_of_pos h0 _
  unfold aR
  rw [lt_div_iff₀ hr]
  by_contra hcon
  rw [not_lt] at hcon
  have h15 : qR x ^ 15 ≤ (2 * x ^ ((2 : ℝ) / 15)) ^ 15 :=
    pow_le_pow_left₀ (by linarith) hcon 15
  have h2r : ((2 : ℝ) * x ^ ((2 : ℝ) / 15)) ^ 15 = 2 ^ 15 * x ^ 2 := by
    rw [mul_pow, rpow_two_fifteenths_pow h0.le]
  rw [h2r] at h15
  have hone : (1 : ℝ) ≤ qR x ^ 15 := one_le_pow₀ hq
  have hx2 : x ^ 2 ≤ (1/200) ^ 2 := pow_le_pow_left₀ h0.le hx 2
  norm_num at hx2 h15
  linarith

/-- If one coordinate is `1` and another is `≤ 1/200`, then `H u > 900`. -/
theorem H_gt_of_small (u : Fin 15 → ℝ) (hu : ∀ i, 0 < u i ∧ u i ≤ 1) {i j : Fin 15}
    (hi : u i = 1) (hj : u j ≤ 1/200) : H u > 900 := by
  have hij : i ≠ j := by
    intro hij
    rw [← hij, hi] at hj
    norm_num at hj
  have h := H_two_lower u hu hij
  rw [hi, wR_one, aR_one] at h
  have hwj : 0 ≤ wR (u j) := wR_nonneg (hu j).1.le (hu j).2
  have haj : 2 < aR (u j) := aR_gt_two_of_small (hu j).1 hj
  have hB4 := B4_real
  obtain ⟨X, hX⟩ : ∃ X : ℝ, X = (8/5) ^ 13 := ⟨_, rfl⟩
  rw [← hX] at h hB4
  have hXpos : 0 < X := by linarith
  nlinarith [mul_pos hXpos (sub_pos.2 haj),
    mul_nonneg hwj (mul_pos (by linarith : (0 : ℝ) < aR (u j)) hXpos).le]

/-- The compact set on which a minimiser is taken. -/
def Kset : Set (Fin 15 → ℝ) := {u | (∀ i, u i ∈ Icc (1/200 : ℝ) 1) ∧ ∃ i, u i = 1}

theorem isCompact_Kset : IsCompact Kset := by
  have h1 : IsCompact (Set.pi univ (fun _ : Fin 15 => Icc (1/200 : ℝ) 1)) :=
    isCompact_univ_pi (fun _ => isCompact_Icc)
  have h2 : IsClosed (⋃ i : Fin 15, {u : Fin 15 → ℝ | u i = 1}) :=
    isClosed_iUnion_of_finite (fun i => isClosed_eq (continuous_apply i) continuous_const)
  have h3 : Kset = Set.pi univ (fun _ : Fin 15 => Icc (1/200 : ℝ) 1)
      ∩ ⋃ i : Fin 15, {u : Fin 15 → ℝ | u i = 1} := by
    ext u
    constructor
    · rintro ⟨hm, i, hi⟩
      exact ⟨fun k _ => hm k, Set.mem_iUnion.2 ⟨i, hi⟩⟩
    · rintro ⟨hm, hU⟩
      obtain ⟨i, hi⟩ := Set.mem_iUnion.1 hU
      exact ⟨fun k => hm k (Set.mem_univ k), i, hi⟩
  rw [h3]
  exact h1.inter_right h2

theorem continuous_qR : Continuous qR := by
  show Continuous (fun x : ℝ => 1 + 2 * x - x ^ 2)
  fun_prop

theorem continuousOn_wR : ContinuousOn wR (Icc (1/200 : ℝ) 1) := by
  show ContinuousOn (fun x : ℝ => x ^ 2 / qR x) _
  apply ContinuousOn.div (by fun_prop) continuous_qR.continuousOn
  intro x hx
  exact (qR_pos (by linarith [hx.1]) hx.2).ne'

theorem continuousOn_aR : ContinuousOn aR (Icc (1/200 : ℝ) 1) := by
  show ContinuousOn (fun x : ℝ => qR x / x ^ ((2 : ℝ) / 15)) _
  apply ContinuousOn.div continuous_qR.continuousOn
    (Real.continuous_rpow_const (by norm_num)).continuousOn
  intro x hx
  exact (Real.rpow_pos_of_pos (by linarith [hx.1]) _).ne'

theorem continuousOn_H : ContinuousOn H Kset := by
  have hmaps : ∀ i : Fin 15, MapsTo (fun u : Fin 15 → ℝ => u i) Kset (Icc (1/200 : ℝ) 1) :=
    fun i u hu => hu.1 i
  show ContinuousOn (fun u : Fin 15 → ℝ => (∑ i, wR (u i)) * ∏ i, aR (u i)) Kset
  apply ContinuousOn.mul
  · exact continuousOn_finsetSum _
      (fun i _ => continuousOn_wR.comp (continuous_apply i).continuousOn (hmaps i))
  · exact continuousOn_finsetProd _
      (fun i _ => continuousOn_aR.comp (continuous_apply i).continuousOn (hmaps i))

/-- At a minimiser of `H` on `Kset`, `H > 900`. -/
theorem H_gt_at_min {u : Fin 15 → ℝ} (hu : u ∈ Kset) (hmin : IsMinOn H Kset u) : H u > 900 := by
  obtain ⟨hmem, i0, hi0⟩ := hu
  have hpos : ∀ i, 0 < u i ∧ u i ≤ 1 := fun i => ⟨by linarith [(hmem i).1], (hmem i).2⟩
  -- a coordinate on the lower boundary
  by_cases hlow : ∃ j, u j = 1/200
  · obtain ⟨j, hj⟩ := hlow
    exact H_gt_of_small u hpos hi0 hj.le
  -- a second coordinate equal to 1
  by_cases htwo : ∃ j, j ≠ i0 ∧ u j = 1
  · obtain ⟨j, hj, hj1⟩ := htwo
    exact D2 u hpos ⟨i0, j, hj.symm, hi0, hj1⟩
  have hlow' : ∀ j, u j ≠ 1/200 := fun j hj => hlow ⟨j, hj⟩
  have htwo' : ∀ j, j ≠ i0 → u j ≠ 1 := fun j hj h1 => htwo ⟨j, hj, h1⟩
  have hw : ∀ k, 0 ≤ wR (u k) := fun k => wR_nonneg (hpos k).1.le (hpos k).2
  -- S = Σ w(u_k) > 0
  have hS : 0 < ∑ k, wR (u k) := by
    have h := Finset.single_le_sum (fun k _ => hw k) (Finset.mem_univ i0)
    rw [hi0, wR_one] at h
    linarith
  -- the critical-point equation in every coordinate j ≠ i0
  have hcrit : ∀ j, j ≠ i0 →
      15 * (u j) ^ 2 * (1 + u j) = (∑ k, wR (u k)) * qR (u j) * quadR (u j) := by
    intro j hj
    have hj1 : 1/200 < u j := lt_of_le_of_ne (hmem j).1 (Ne.symm (hlow' j))
    have hj2 : u j < 1 := lt_of_le_of_ne (hmem j).2 (htwo' j hj)
    have hloc : IsLocalMin
        (fun x => (wR x + ∑ k ∈ Finset.univ.erase j, wR (u k))
          * (aR x * ∏ k ∈ Finset.univ.erase j, aR (u k))) (u j) :=
      Filter.eventually_of_mem (Ioo_mem_nhds hj1 hj2) (fun x hx => by
        have hxK : Function.update u j x ∈ Kset := by
          refine ⟨fun k => ?_, i0, ?_⟩
          · by_cases hk : k = j
            · rw [hk, Function.update_self]
              exact ⟨hx.1.le, hx.2.le⟩
            · rw [Function.update_of_ne hk]
              exact hmem k
          · rw [Function.update_of_ne (Ne.symm hj)]
            exact hi0
        have h := isMinOn_iff.1 hmin _ hxK
        rw [H_update] at h
        have h0 := H_update u j (u j)
        rw [Function.update_eq_self] at h0
        rw [h0] at h
        exact h)
    have hPr : 0 < ∏ k ∈ Finset.univ.erase j, aR (u k) :=
      Finset.prod_pos (fun k _ => by linarith [D1 (u k) (hpos k).1 (hpos k).2])
    have hE := crit_eq (by linarith) hj2 hPr hloc
    have hSj : (∑ k ∈ Finset.univ.erase j, wR (u k)) + wR (u j) = ∑ k, wR (u k) := by
      rw [add_comm]
      exact Finset.add_sum_erase Finset.univ (fun k => wR (u k)) (Finset.mem_univ j)
    rw [hSj] at hE
    exact hE
  -- S − w(u_j) ≤ 7
  have hC : ∀ j, (∑ k, wR (u k)) - wR (u j) ≤ 7 := by
    intro j
    have h1 : ∑ k ∈ Finset.univ.erase j, wR (u k)
        ≤ ((Finset.univ : Finset (Fin 15)).erase j).card • (1/2 : ℝ) :=
      Finset.sum_le_card_nsmul ((Finset.univ : Finset (Fin 15)).erase j) (fun k => wR (u k))
        (1/2 : ℝ) (fun k _ => wR_le_half (hpos k).1.le (hpos k).2)
    have h2 : ((Finset.univ : Finset (Fin 15)).erase j).card = 14 := by
      rw [Finset.card_erase_of_mem (Finset.mem_univ j)]
      simp
    rw [h2] at h1
    have h3 : wR (u j) + ∑ k ∈ Finset.univ.erase j, wR (u k) = ∑ k, wR (u k) :=
      Finset.add_sum_erase Finset.univ (fun k => wR (u k)) (Finset.mem_univ j)
    norm_num at h1
    linarith
  -- every coordinate j ≠ i0 lies below 3/35
  have hsmall : ∀ j, j ≠ i0 → u j < 3/35 := fun j hj =>
    crit_small (hpos j).1 (lt_of_le_of_ne (hpos j).2 (htwo' j hj)) hS (hC j) (hcrit j hj)
  -- and they are all equal (D3)
  have huniq : ∀ j, j ≠ i0 → ∀ j', j' ≠ i0 → u j = u j' := by
    intro j hj j' hj'
    have e1 := LR_eq_of_crit (hpos j).1 hS (hcrit j hj)
    have e2 := LR_eq_of_crit (hpos j').1 hS (hcrit j' hj')
    exact D3.injOn ⟨(hpos j).1, (hsmall j hj).le⟩ ⟨(hpos j').1, (hsmall j' hj').le⟩
      (e1.trans e2.symm)
  obtain ⟨j1, hj1⟩ : ∃ j : Fin 15, j ≠ i0 := by
    by_cases h : i0 = 0
    · exact ⟨1, by rw [h]; decide⟩
    · exact ⟨0, fun h' => h h'.symm⟩
  have ht0 : 0 < u j1 := (hpos j1).1
  have hEq := H_eq_H1 u i0 (u j1) ht0 (hpos j1).2 hi0 (fun j hj => huniq j hj j1 hj1)
  rw [hEq]
  exact partC (u j1) ht0 (lt_of_le_of_ne (hpos j1).2 (htwo' j1 hj1))

/-- **The shape lemma (15 speeds).** For every `u : Fin 15 → ℝ` with all `u_i ∈ (0,1]` and
some `u_i = 1`, `H u > 900`. -/
theorem shape_lemma (u : Fin 15 → ℝ) (hu : ∀ i, 0 < u i ∧ u i ≤ 1) (hone : ∃ i, u i = 1) :
    H u > 900 := by
  obtain ⟨i0, hi0⟩ := hone
  by_cases hsm : ∃ j, u j ≤ 1/200
  · obtain ⟨j, hj⟩ := hsm
    exact H_gt_of_small u hu hi0 hj
  · have hK : u ∈ Kset :=
      ⟨fun i => ⟨le_of_lt (not_le.1 (fun h => hsm ⟨i, h⟩)), (hu i).2⟩, i0, hi0⟩
    obtain ⟨v, hv, hvmin⟩ := isCompact_Kset.exists_isMinOn ⟨u, hK⟩ continuousOn_H
    have h1 := H_gt_at_min hv hvmin
    have h2 := isMinOn_iff.1 hvmin u hK
    linarith

end PT005

#print axioms PT005.D1
#print axioms PT005.D2
#print axioms PT005.D3
#print axioms PT005.crit_eq
#print axioms PT005.crit_small
#print axioms PT005.H_eq_H1
#print axioms PT005.H_gt_of_small
#print axioms PT005.isCompact_Kset
#print axioms PT005.continuousOn_H
#print axioms PT005.H_gt_at_min
#print axioms PT005.shape_lemma
