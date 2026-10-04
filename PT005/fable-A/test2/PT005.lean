/-
PT005 · TESTING TURN 2 · seat: Fable-A
Lean 4.30.0, Mathlib v4.30.0 (commit c5ea00351c28e24afc9f0f84379aa41082b1188f)

Machine-checked pieces of the 16-runner route:
  PART A  exact rational arithmetic (Astra's constants)        A1–A5
  PART B  Kimi's numeric inequalities                            B1–B6
  PART C  real-variable step: H1 t > 900 for all real t in (0,1) (theorem `partC`)
No sorry / admit / native_decide / new axioms.
Command: lake env lean PT005.lean
-/
import Mathlib

namespace PT005

/-! ## PART A — exact rationals -/

/-- `B r = (2r / (16·(16−r)))^2`, as in the packet (used for `0 ≤ r ≤ 14`; `B 0 = 0`). -/
def B (r : ℕ) : ℚ := ((2 * r : ℚ) / (16 * (16 - r)))^2

/-- Original increments `c i = B i − B (i−1)` (with `B 0 = 0`). -/
def c (i : ℕ) : ℚ := B i - B (i - 1)

/-- `B'` equals `B` except `B' 13 = 391/960`. -/
def B' (r : ℕ) : ℚ := if r = 13 then 391/960 else B r

/-- Modified increments `c' i = B' i − B' (i−1)`. -/
def c' (i : ℕ) : ℚ := B' i - B' (i - 1)

/-- The coercions in `B` are on `r` itself: the subtraction `16 − r` is taken in `ℚ`. -/
theorem B_def (r : ℕ) : B r = (2 * (r : ℚ) / (16 * (16 - (r : ℚ)))) ^ 2 := rfl

/-- Sanity: `B 0 = 0`, so `c 1 = B 1`. -/
theorem B_zero : B 0 = 0 := by norm_num [B]

/-- A1. -/
theorem A1 : B 14 - 1/3 = 83/192 := by norm_num [B]

/-- A2, first half. -/
theorem A2_lt : (391/960 : ℚ) < 83/192 := by norm_num

/-- A2, second half. -/
theorem A2_le : B 13 ≤ 391/960 := by norm_num [B]

/-- A3: `c' 13 = 4/15`. -/
theorem A3_c13 : c' 13 = 4/15 := by norm_num [c', B', B]

/-- A3: `c' 14 = 43/120`. -/
theorem A3_c14 : c' 14 = 43/120 := by norm_num [c', B', B]

/-- A3: `c' (i+1) / c' i > 4/3` for every `i = 1..13`. -/
theorem A3_ratio : ∀ i ∈ Finset.Icc 1 13, c' (i + 1) / c' i > 4/3 := by
  intro i hi
  rw [Finset.mem_Icc] at hi
  obtain ⟨h1, h2⟩ := hi
  interval_cases i <;> norm_num [c', B', B]

/-- The product of the original increments is nonzero (so the quotient in A4 is meaningful). -/
theorem prod_c_ne_zero : (∏ i ∈ Finset.Icc 1 14, c i) ≠ 0 := by
  rw [Finset.prod_ne_zero_iff]
  intro i hi
  rw [Finset.mem_Icc] at hi
  obtain ⟨h1, h2⟩ := hi
  interval_cases i <;> norm_num [c, B]

/-- A4: `(∏_{i=1}^{14} c' i) / (∏_{i=1}^{14} c i) = 6192/4675`. -/
theorem A4 : (∏ i ∈ Finset.Icc 1 14, c' i) / (∏ i ∈ Finset.Icc 1 14, c i) = 6192/4675 := by
  have hset : Finset.Icc 1 14 = ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14} : Finset ℕ) := by
    decide
  rw [hset]
  norm_num [Finset.prod_insert, c', c, B', B]

/-- A5 (original constants): every ratio `c (i+1) / c i`, `i = 1..13`, is at least `3751/2349`. -/
theorem A5_lower : ∀ i ∈ Finset.Icc 1 13, (3751/2349 : ℚ) ≤ c (i + 1) / c i := by
  intro i hi
  rw [Finset.mem_Icc] at hi
  obtain ⟨h1, h2⟩ := hi
  interval_cases i <;> norm_num [c, B]

/-- A5: the value `3751/2349` is attained, at `i = 6`. -/
theorem A5_attained : c 7 / c 6 = 3751/2349 := by norm_num [c, B]

/-- A5: the minimum exceeds `4/3`. -/
theorem A5_gt : (3751/2349 : ℚ) > 4/3 := by norm_num

/-- A5 as a single statement about the minimum over `i = 1..13`. -/
theorem A5 :
    (Finset.Icc 1 13).inf' (by decide) (fun i => c (i + 1) / c i) = 3751/2349
      ∧ (3751/2349 : ℚ) > 4/3 := by
  refine ⟨le_antisymm ?_ ?_, A5_gt⟩
  · calc (Finset.Icc 1 13).inf' (by decide) (fun i => c (i + 1) / c i)
        ≤ c (6 + 1) / c 6 := Finset.inf'_le _ (by decide)
      _ = 3751/2349 := A5_attained
  · exact (Finset.le_inf'_iff _ _).2 A5_lower

/-! ## PART B — Kimi's numeric inequalities -/

/-- `q x = 1 + 2x − x²`. -/
def q (x : ℚ) : ℚ := 1 + 2 * x - x ^ 2

/-- `cubic t = 378 t³ + 25 t² + 10 t − 1`. -/
def cubic (t : ℚ) : ℚ := 378 * t ^ 3 + 25 * t ^ 2 + 10 * t - 1

/-- `lo = 7247/100000`. -/
def lo : ℚ := 7247/100000

/-- `hi = 7248/100000`. -/
def hi : ℚ := 7248/100000

/-- B1 (value). -/
theorem B1_eq : (-54 * (3/35)^3 - 22 * (3/35)^2 - 8 * (3/35) + 2 : ℚ) = 47962/42875 := by
  norm_num

/-- B1 (positivity). -/
theorem B1_pos : (0 : ℚ) < -54 * (3/35)^3 - 22 * (3/35)^2 - 8 * (3/35) + 2 := by
  norm_num

/-- B2, lower side. -/
theorem B2_gt : ((107/10 : ℚ))^2 > 113 := by norm_num

/-- B2, upper side. -/
theorem B2_lt : ((1063/100 : ℚ))^2 < 113 := by norm_num

/-- B3. -/
theorem B3 : (q (23/280))^15 > (8/5 : ℚ)^15 * (237/2800)^2 := by
  norm_num [q]

/-- B4. -/
theorem B4 : 4 * (8/5 : ℚ)^13 > 1801 := by norm_num

/-- B5, left side. -/
theorem B5_lo : cubic lo < 0 := by norm_num [cubic, lo]

/-- B5, right side. -/
theorem B5_hi : 0 < cubic hi := by norm_num [cubic, hi]

/-- B6 (big integers, about 2,100 digits). -/
theorem B6 : ((1 + 2 * lo + 27 * lo ^ 2) * (q lo) ^ 13) ^ 15 > 900 ^ 15 * hi ^ 28 := by
  norm_num [q, lo, hi]

/-! ## PART C — the real-variable step behind B5–B6

For every real `t ∈ (0,1)`:  `H1 t = (1 + 2t + 27t²)·q(t)^13 / t^(28/15) > 900`.

Route: with `g = 15·log P + 195·log q − 28·log t` (so `g = log F`, `F = P^15 q^195 / t^28`),
`g' t = 28·(1−t)·cubic t / (t·P t·q t)`.  The cubic is increasing, `cubic lo < 0 < cubic hi` (B5),
so `g` is antitone on `(0, lo]` and monotone on `[hi, 1)`.  On `[lo, hi]` the factors are monotone,
so `F s ≥ P(lo)^15 q(lo)^195 / hi^28 > 900^15` by B6.
-/

section PartC

open Set

/-- Real version of `q`. -/
noncomputable def qR (x : ℝ) : ℝ := 1 + 2 * x - x ^ 2

/-- `P x = 1 + 2x + 27x²`. -/
noncomputable def PR (x : ℝ) : ℝ := 1 + 2 * x + 27 * x ^ 2

/-- Real version of `cubic`. -/
noncomputable def cubicR (t : ℝ) : ℝ := 378 * t ^ 3 + 25 * t ^ 2 + 10 * t - 1

/-- The packet's `H1`, with a genuine real power `t^(28/15)`. -/
noncomputable def H1 (t : ℝ) : ℝ :=
  (1 + 2 * t + 27 * t ^ 2) * (qR t) ^ 13 / t ^ ((28 : ℝ) / 15)

/-- Logarithmic form `15·log P + 195·log q − 28·log t`. -/
noncomputable def g (t : ℝ) : ℝ :=
  15 * Real.log (PR t) + 195 * Real.log (qR t) - 28 * Real.log t

/-- `F t = P(t)^15 · q(t)^195 / t^28`, the 15th power of `H1`. -/
noncomputable def F (t : ℝ) : ℝ := PR t ^ 15 * qR t ^ 195 / t ^ 28

theorem lo_pos : (0 : ℝ) < (lo : ℝ) := by norm_num [lo]
theorem lo_le_hi : ((lo : ℚ) : ℝ) ≤ (hi : ℝ) := by norm_num [lo, hi]
theorem hi_lt_one : ((hi : ℚ) : ℝ) < 1 := by norm_num [hi]
theorem lo_lt_one : ((lo : ℚ) : ℝ) < 1 := lo_le_hi.trans_lt hi_lt_one
theorem hi_pos : (0 : ℝ) < (hi : ℝ) := lo_pos.trans_le lo_le_hi

/-- B5 (left) transported to `ℝ`. -/
theorem B5_lo_real : cubicR (lo : ℝ) < 0 := by
  have h := B5_lo
  unfold cubic at h
  unfold cubicR
  exact_mod_cast h

/-- B5 (right) transported to `ℝ`. -/
theorem B5_hi_real : 0 < cubicR (hi : ℝ) := by
  have h := B5_hi
  unfold cubic at h
  unfold cubicR
  exact_mod_cast h

/-- B6 transported to `ℝ`. -/
theorem B6_real : (900 : ℝ) ^ 15 * (hi : ℝ) ^ 28 < (PR (lo : ℝ) * qR (lo : ℝ) ^ 13) ^ 15 := by
  have h := B6
  unfold q at h
  unfold PR qR
  exact_mod_cast h

theorem PR_pos {t : ℝ} (h0 : 0 ≤ t) : 0 < PR t := by
  unfold PR; nlinarith [sq_nonneg t]

theorem qR_pos {t : ℝ} (h0 : 0 ≤ t) (h1 : t ≤ 1) : 0 < qR t := by
  unfold qR; nlinarith

/-- The cubic is increasing on `[0, ∞)`. -/
theorem cubicR_mono {s t : ℝ} (hs : 0 ≤ s) (hst : s ≤ t) : cubicR s ≤ cubicR t := by
  have h : cubicR t - cubicR s
      = (t - s) * (378 * (t ^ 2 + t * s + s ^ 2) + 25 * (t + s) + 10) := by
    unfold cubicR; ring
  have ht : 0 ≤ t := hs.trans hst
  have h2 : 0 ≤ (t - s) * (378 * (t ^ 2 + t * s + s ^ 2) + 25 * (t + s) + 10) :=
    mul_nonneg (sub_nonneg.2 hst) (by positivity)
  linarith

/-- The derivative of `g` on `(0,1)`, in factored form. -/
theorem hasDerivAt_g {t : ℝ} (h0 : 0 < t) (h1 : t < 1) :
    HasDerivAt g (28 * (1 - t) * cubicR t / (t * PR t * qR t)) t := by
  have hPpos : 0 < PR t := PR_pos h0.le
  have hqpos : 0 < qR t := qR_pos h0.le h1.le
  have hP : HasDerivAt PR (2 + 54 * t) t := by
    have ha := ((hasDerivAt_id' t).const_mul (2 : ℝ)).const_add (1 : ℝ)
    have hb := (hasDerivAt_pow 2 t).const_mul (27 : ℝ)
    have hc := ha.add hb
    convert hc using 1
    norm_num
    ring
  have hq : HasDerivAt qR (2 - 2 * t) t := by
    have ha := ((hasDerivAt_id' t).const_mul (2 : ℝ)).const_add (1 : ℝ)
    have hb := hasDerivAt_pow 2 t
    have hc := ha.sub hb
    convert hc using 1
    norm_num
  have hlP := hP.log hPpos.ne'
  have hlq := hq.log hqpos.ne'
  have hlt := Real.hasDerivAt_log h0.ne'
  have h := ((hlP.const_mul (15 : ℝ)).add (hlq.const_mul (195 : ℝ))).sub (hlt.const_mul (28 : ℝ))
  convert h using 1
  have ht : t ≠ 0 := h0.ne'
  have hP' : PR t ≠ 0 := hPpos.ne'
  have hq' : qR t ≠ 0 := hqpos.ne'
  field_simp
  unfold cubicR PR qR
  ring

/-- `g = log F` on `(0,1)`. -/
theorem g_eq_log_F {t : ℝ} (h0 : 0 < t) (h1 : t < 1) : g t = Real.log (F t) := by
  have hP : 0 < PR t := PR_pos h0.le
  have hq : 0 < qR t := qR_pos h0.le h1.le
  unfold F g
  rw [Real.log_div (mul_pos (pow_pos hP 15) (pow_pos hq 195)).ne' (pow_pos h0 28).ne',
    Real.log_mul (pow_pos hP 15).ne' (pow_pos hq 195).ne',
    Real.log_pow, Real.log_pow, Real.log_pow]
  push_cast
  ring

theorem F_pos {t : ℝ} (h0 : 0 < t) (h1 : t < 1) : 0 < F t :=
  div_pos (mul_pos (pow_pos (PR_pos h0.le) 15) (pow_pos (qR_pos h0.le h1.le) 195)) (pow_pos h0 28)

theorem F_le_of_g_le {a b : ℝ} (ha0 : 0 < a) (ha1 : a < 1) (hb0 : 0 < b) (hb1 : b < 1)
    (h : g a ≤ g b) : F a ≤ F b := by
  rw [g_eq_log_F ha0 ha1, g_eq_log_F hb0 hb1] at h
  exact (Real.log_le_log_iff (F_pos ha0 ha1) (F_pos hb0 hb1)).1 h

/-- `g` is antitone on `(0, lo]`: for `0 < t ≤ lo`, `g lo ≤ g t`. -/
theorem g_lo_le {t : ℝ} (h0 : 0 < t) (ht : t ≤ (lo : ℝ)) : g (lo : ℝ) ≤ g t := by
  have hanti : AntitoneOn g (Icc t (lo : ℝ)) := by
    apply antitoneOn_of_deriv_nonpos (convex_Icc _ _)
    · intro x hx
      exact (hasDerivAt_g (h0.trans_le hx.1) (hx.2.trans_lt lo_lt_one)).continuousAt.continuousWithinAt
    · intro x hx
      rw [interior_Icc] at hx
      exact (hasDerivAt_g (h0.trans hx.1) (hx.2.trans lo_lt_one)).differentiableAt.differentiableWithinAt
    · intro x hx
      rw [interior_Icc] at hx
      have hx0 : 0 < x := h0.trans hx.1
      have hx1 : x < 1 := hx.2.trans lo_lt_one
      rw [(hasDerivAt_g hx0 hx1).deriv]
      have hc : cubicR x ≤ 0 := (cubicR_mono hx0.le hx.2.le).trans B5_lo_real.le
      have hn : 0 ≤ 28 * (1 - x) := by linarith
      exact div_nonpos_of_nonpos_of_nonneg (mul_nonpos_of_nonneg_of_nonpos hn hc)
        (mul_pos (mul_pos hx0 (PR_pos hx0.le)) (qR_pos hx0.le hx1.le)).le
  exact hanti (left_mem_Icc.2 ht) (right_mem_Icc.2 ht) ht

/-- `g` is monotone on `[hi, 1)`: for `hi ≤ t < 1`, `g hi ≤ g t`. -/
theorem g_hi_le {t : ℝ} (ht : (hi : ℝ) ≤ t) (h1 : t < 1) : g (hi : ℝ) ≤ g t := by
  have hmono : MonotoneOn g (Icc (hi : ℝ) t) := by
    apply monotoneOn_of_deriv_nonneg (convex_Icc _ _)
    · intro x hx
      exact (hasDerivAt_g (hi_pos.trans_le hx.1) (hx.2.trans_lt h1)).continuousAt.continuousWithinAt
    · intro x hx
      rw [interior_Icc] at hx
      exact (hasDerivAt_g (hi_pos.trans hx.1) (hx.2.trans h1)).differentiableAt.differentiableWithinAt
    · intro x hx
      rw [interior_Icc] at hx
      have hx0 : 0 < x := hi_pos.trans hx.1
      have hx1 : x < 1 := hx.2.trans h1
      rw [(hasDerivAt_g hx0 hx1).deriv]
      have hc : 0 ≤ cubicR x := B5_hi_real.le.trans (cubicR_mono hi_pos.le hx.1.le)
      have hn : 0 ≤ 28 * (1 - x) := by linarith
      exact div_nonneg (mul_nonneg hn hc)
        (mul_pos (mul_pos hx0 (PR_pos hx0.le)) (qR_pos hx0.le hx1.le)).le
  exact hmono (left_mem_Icc.2 ht) (right_mem_Icc.2 ht) ht

/-- On `[lo, hi]`, monotonicity of the factors and B6 give `F s > 900^15`. -/
theorem F_mid {s : ℝ} (hs1 : (lo : ℝ) ≤ s) (hs2 : s ≤ (hi : ℝ)) : (900 : ℝ) ^ 15 < F s := by
  have hs0 : 0 < s := lo_pos.trans_le hs1
  have hs1' : s < 1 := hs2.trans_lt hi_lt_one
  have hPlo : 0 < PR (lo : ℝ) := PR_pos lo_pos.le
  have hqlo : 0 < qR (lo : ℝ) := qR_pos lo_pos.le lo_lt_one.le
  have hPmono : PR (lo : ℝ) ≤ PR s := by
    unfold PR
    nlinarith [mul_nonneg (sub_nonneg.2 hs1) (add_nonneg hs0.le lo_pos.le)]
  have hqmono : qR (lo : ℝ) ≤ qR s := by
    unfold qR
    nlinarith [mul_nonneg (sub_nonneg.2 hs1) (by linarith [lo_lt_one] : (0 : ℝ) ≤ 2 - s - lo)]
  have hnum : PR (lo : ℝ) ^ 15 * qR (lo : ℝ) ^ 195 ≤ PR s ^ 15 * qR s ^ 195 :=
    mul_le_mul (pow_le_pow_left₀ hPlo.le hPmono 15) (pow_le_pow_left₀ hqlo.le hqmono 195)
      (pow_pos hqlo 195).le (pow_pos (hPlo.trans_le hPmono) 15).le
  have hden : s ^ 28 ≤ (hi : ℝ) ^ 28 := pow_le_pow_left₀ hs0.le hs2 28
  have hB6 : (900 : ℝ) ^ 15 * (hi : ℝ) ^ 28 < PR (lo : ℝ) ^ 15 * qR (lo : ℝ) ^ 195 := by
    calc (900 : ℝ) ^ 15 * (hi : ℝ) ^ 28 < (PR (lo : ℝ) * qR (lo : ℝ) ^ 13) ^ 15 := B6_real
      _ = PR (lo : ℝ) ^ 15 * qR (lo : ℝ) ^ 195 := by ring
  unfold F
  rw [lt_div_iff₀ (pow_pos hs0 28)]
  calc (900 : ℝ) ^ 15 * s ^ 28 ≤ 900 ^ 15 * (hi : ℝ) ^ 28 :=
        mul_le_mul_of_nonneg_left hden (by positivity)
    _ < PR (lo : ℝ) ^ 15 * qR (lo : ℝ) ^ 195 := hB6
    _ ≤ PR s ^ 15 * qR s ^ 195 := hnum

/-- `F t > 900^15` on all of `(0,1)`. -/
theorem F_gt {t : ℝ} (h0 : 0 < t) (h1 : t < 1) : (900 : ℝ) ^ 15 < F t := by
  rcases le_total t (lo : ℝ) with h | h
  · exact (F_mid le_rfl lo_le_hi).trans_le
      (F_le_of_g_le lo_pos lo_lt_one h0 h1 (g_lo_le h0 h))
  · rcases le_total t (hi : ℝ) with h' | h'
    · exact F_mid h h'
    · exact (F_mid lo_le_hi le_rfl).trans_le
        (F_le_of_g_le hi_pos hi_lt_one h0 h1 (g_hi_le h' h1))

/-- PART C: for every real `t ∈ (0,1)`, `H1 t > 900`. -/
theorem partC (t : ℝ) (h0 : 0 < t) (h1 : t < 1) : H1 t > 900 := by
  have hF := F_gt h0 h1
  have hq : 0 < qR t := qR_pos h0.le h1.le
  have hN : 0 < (1 + 2 * t + 27 * t ^ 2) * qR t ^ 13 :=
    mul_pos (by nlinarith [sq_nonneg t]) (pow_pos hq 13)
  have hr : 0 < t ^ ((28 : ℝ) / 15) := Real.rpow_pos_of_pos h0 _
  have hpow : (t ^ ((28 : ℝ) / 15)) ^ 15 = t ^ 28 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul h0.le]
    norm_num
  unfold H1
  rw [gt_iff_lt, lt_div_iff₀ hr]
  by_contra hcon
  rw [not_lt] at hcon
  have h15 : ((1 + 2 * t + 27 * t ^ 2) * qR t ^ 13) ^ 15 ≤ (900 * t ^ ((28 : ℝ) / 15)) ^ 15 :=
    pow_le_pow_left₀ hN.le hcon 15
  have h900 : (900 * t ^ ((28 : ℝ) / 15)) ^ 15 = 900 ^ 15 * t ^ 28 := by
    rw [mul_pow, hpow]
  rw [h900] at h15
  have hle : F t ≤ 900 ^ 15 := by
    unfold F
    rw [div_le_iff₀ (pow_pos h0 28)]
    calc PR t ^ 15 * qR t ^ 195 = ((1 + 2 * t + 27 * t ^ 2) * qR t ^ 13) ^ 15 := by
          unfold PR; ring
      _ ≤ 900 ^ 15 * t ^ 28 := h15
  linarith

end PartC

end PT005

#print axioms PT005.A1
#print axioms PT005.A2_lt
#print axioms PT005.A2_le
#print axioms PT005.A3_c13
#print axioms PT005.A3_c14
#print axioms PT005.A3_ratio
#print axioms PT005.prod_c_ne_zero
#print axioms PT005.A4
#print axioms PT005.A5_lower
#print axioms PT005.A5_attained
#print axioms PT005.A5_gt
#print axioms PT005.A5
#print axioms PT005.B1_eq
#print axioms PT005.B1_pos
#print axioms PT005.B2_gt
#print axioms PT005.B2_lt
#print axioms PT005.B3
#print axioms PT005.B4
#print axioms PT005.B5_lo
#print axioms PT005.B5_hi
#print axioms PT005.B6
#print axioms PT005.B5_lo_real
#print axioms PT005.B5_hi_real
#print axioms PT005.B6_real
#print axioms PT005.cubicR_mono
#print axioms PT005.hasDerivAt_g
#print axioms PT005.F_mid
#print axioms PT005.F_gt
#print axioms PT005.partC
