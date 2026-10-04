/-
TOGETHER · PROOF TABLE 004 · Round 4 · Turn 15 · item L4-L
Seat: Fable-A (testing seat) · carried by hand by Tuzi
Versions: Lean 4.30.0 · Mathlib v4.30.0 (commit c5ea00351c28e24afc9f0f84379aa41082b1188f)
Run with:  lake env lean PT004_L4L_FableA.lean

The weak bound 1/(2n): for every n ≥ 1 and all non-zero integer speeds v 0, …, v (n-1)
there is a time t in [0, 1] at which every v i * t is at distance at least 1/(2n) from
the integers.  The statement `weak_bound` at the end is the one given in the seat block.

The proof follows the four steps of the hand proof (Astra, T9), carried out on the
circle ℝ/ℤ (`UnitAddCircle`) instead of the interval [0, 1):
  (1) one speed: the points x of the circle with ‖a • x‖ < δ form a set of measure ≤ 2δ,
      because x ↦ a • x preserves the measure of the circle when a ≠ 0, and a ball of
      radius δ has measure ≤ 2δ;                                 (`measure_bad_le`)
  (2) union bound: if 2nδ < 1 the n bad sets cannot cover the circle, which has
      measure 1;                                                 (`exists_point_of_lt`)
  (3) x ↦ min_i ‖v i • x‖ is continuous;                          (`continuous_minDist`)
  (4) it attains its maximum on the compact circle, and by (2) the maximum is at least
      1/(2n);                                                    (`exists_point`)
  last, a point of the circle is the class of a real number, which can be taken in
      [0, 1), and ‖(y : ℝ/ℤ)‖ = |y - round y| = distInt y.        (`weak_bound`)

Nothing is copied from the prior-work file (Zenodo 21975059).
The file contains only definitions, theorems with complete proofs, and `#print` commands.
-/
import Mathlib

open MeasureTheory

/-- Distance from the real number `x` to the nearest integer (as in PT004_L1L_FableA.lean). -/
noncomputable def distInt (x : ℝ) : ℝ := |x - round x|

namespace PT004L4

/-! ### `distInt` means what it says (not used in the proof) -/

/-- No integer is closer to `x` than `distInt x`. -/
theorem distInt_le_abs_sub_int (x : ℝ) (m : ℤ) : distInt x ≤ |x - m| :=
  round_le x m

/-- Some integer is at distance exactly `distInt x` from `x`. -/
theorem exists_int_distInt_eq (x : ℝ) : ∃ m : ℤ, distInt x = |x - m| :=
  ⟨round x, rfl⟩

/-! ### Steps (1) and (2): measure on the circle -/

/-- Step (1).  For a non-zero integer `a`, the set of points `x` of the circle with
`‖a • x‖ < δ` has measure at most `2 δ`. -/
theorem measure_bad_le (a : ℤ) (ha : a ≠ 0) (δ : ℝ) :
    volume ((fun x : UnitAddCircle => a • x) ⁻¹' Metric.ball 0 δ) ≤ ENNReal.ofReal (2 * δ) := by
  have hmp : MeasurePreserving (fun x : UnitAddCircle => a • x) volume volume :=
    MeasureTheory.Measure.measurePreserving_zsmul volume ha
  rw [hmp.measure_preimage Metric.isOpen_ball.measurableSet.nullMeasurableSet]
  calc volume (Metric.ball (0 : UnitAddCircle) δ)
      ≤ volume (Metric.closedBall (0 : UnitAddCircle) δ) := measure_mono Metric.ball_subset_closedBall
    _ = ENNReal.ofReal (min 1 (2 * δ)) := AddCircle.volume_closedBall 1 δ
    _ ≤ ENNReal.ofReal (2 * δ) := ENNReal.ofReal_le_ofReal (min_le_right _ _)

/-- Step (2).  If `2 n δ < 1`, some point of the circle has `‖v i • x‖ ≥ δ` for every `i`. -/
theorem exists_point_of_lt {n : ℕ} (v : Fin n → ℤ) (hv : ∀ i, v i ≠ 0) {δ : ℝ}
    (hδ : 2 * (n : ℝ) * δ < 1) : ∃ x : UnitAddCircle, ∀ i, δ ≤ ‖v i • x‖ := by
  by_contra h
  push Not at h
  -- otherwise the `n` bad sets cover the whole circle
  have hcover : (Set.univ : Set UnitAddCircle)
      ⊆ ⋃ i, (fun x : UnitAddCircle => v i • x) ⁻¹' Metric.ball 0 δ := by
    intro x _
    obtain ⟨i, hi⟩ := h x
    exact Set.mem_iUnion.mpr ⟨i, mem_ball_zero_iff.mpr hi⟩
  have h1 : (1 : ENNReal) ≤ ENNReal.ofReal (2 * (n : ℝ) * δ) := by
    calc (1 : ENNReal) = volume (Set.univ : Set UnitAddCircle) := UnitAddCircle.measure_univ.symm
      _ ≤ volume (⋃ i, (fun x : UnitAddCircle => v i • x) ⁻¹' Metric.ball 0 δ) :=
          measure_mono hcover
      _ ≤ ∑ i, volume ((fun x : UnitAddCircle => v i • x) ⁻¹' Metric.ball 0 δ) :=
          measure_iUnion_fintype_le _ _
      _ ≤ ∑ _i : Fin n, ENNReal.ofReal (2 * δ) :=
          Finset.sum_le_sum fun i _ => measure_bad_le (v i) (hv i) δ
      _ = ENNReal.ofReal (2 * (n : ℝ) * δ) := by
          rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, ← ENNReal.ofReal_nsmul,
            nsmul_eq_mul]
          congr 1
          ring
  have h2 : ENNReal.ofReal (2 * (n : ℝ) * δ) < 1 := by
    rw [← ENNReal.ofReal_one]
    exact (ENNReal.ofReal_lt_ofReal_iff one_pos).mpr hδ
  exact absurd h1 (not_le.mpr h2)

/-! ### Steps (3) and (4): continuity and the maximum on the compact circle -/

/-- `min_i ‖v i • x‖`, a function of the point `x` of the circle. -/
noncomputable def minDist {n : ℕ} [Nonempty (Fin n)] (v : Fin n → ℤ) (x : UnitAddCircle) : ℝ :=
  Finset.univ.inf' Finset.univ_nonempty fun i => ‖v i • x‖

theorem minDist_le {n : ℕ} [Nonempty (Fin n)] (v : Fin n → ℤ) (x : UnitAddCircle) (i : Fin n) :
    minDist v x ≤ ‖v i • x‖ :=
  Finset.inf'_le _ (Finset.mem_univ i)

theorem le_minDist {n : ℕ} [Nonempty (Fin n)] (v : Fin n → ℤ) (x : UnitAddCircle) {c : ℝ}
    (h : ∀ i, c ≤ ‖v i • x‖) : c ≤ minDist v x :=
  Finset.le_inf' _ _ fun i _ => h i

/-- Step (3). -/
theorem continuous_minDist {n : ℕ} [Nonempty (Fin n)] (v : Fin n → ℤ) :
    Continuous (minDist v) :=
  Continuous.finset_inf'_apply Finset.univ_nonempty fun i _ => (continuous_zsmul (v i)).norm

/-- Step (4).  Some point of the circle has `‖v i • x‖ ≥ 1/(2n)` for every `i`. -/
theorem exists_point {n : ℕ} (hn : 1 ≤ n) (v : Fin n → ℤ) (hv : ∀ i, v i ≠ 0) :
    ∃ x : UnitAddCircle, ∀ i, 1 / (2 * (n : ℝ)) ≤ ‖v i • x‖ := by
  haveI : Nonempty (Fin n) := ⟨⟨0, hn⟩⟩
  have hnR : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn
  -- a point where `minDist v` is largest
  obtain ⟨x, -, hx⟩ := isCompact_univ.exists_isMaxOn Set.univ_nonempty
    (continuous_minDist v).continuousOn
  refine ⟨x, fun i => ?_⟩
  by_contra hlt
  rw [not_le] at hlt
  -- then the maximum `M = minDist v x` is below `1/(2n)`; take `δ` strictly between
  have hM : minDist v x < 1 / (2 * (n : ℝ)) := lt_of_le_of_lt (minDist_le v x i) hlt
  obtain ⟨δ, hδ1, hδ2⟩ := exists_between hM
  have hδ : 2 * (n : ℝ) * δ < 1 := by
    have h := mul_lt_mul_of_pos_left hδ2 (by positivity : (0 : ℝ) < 2 * (n : ℝ))
    rwa [mul_one_div_cancel (by positivity : (2 * (n : ℝ)) ≠ 0)] at h
  -- step (2) gives a point that does better than the maximum
  obtain ⟨y, hy⟩ := exists_point_of_lt v hv hδ
  have h3 : δ ≤ minDist v y := le_minDist v y hy
  have h4 : minDist v y ≤ minDist v x := isMaxOn_iff.mp hx y (Set.mem_univ y)
  linarith

end PT004L4

/-- **The weak bound `1/(2n)`.**  For `n ≥ 1` non-zero integer speeds there is a time
`t ∈ [0, 1]` at which every `v i * t` is at distance at least `1/(2n)` from the integers. -/
theorem weak_bound (n : ℕ) (hn : 1 ≤ n) (v : Fin n → ℤ) (hv : ∀ i, v i ≠ 0) :
    ∃ t : ℝ, t ∈ Set.Icc (0:ℝ) 1 ∧ ∀ i, distInt ((v i : ℝ) * t) ≥ 1 / (2 * (n : ℝ)) := by
  obtain ⟨x, hx⟩ := PT004L4.exists_point hn v hv
  -- the point `x` of the circle is the class of a real number `s`; use `t = fract s`
  obtain ⟨s, rfl⟩ := QuotientAddGroup.mk_surjective x
  refine ⟨Int.fract s, ⟨Int.fract_nonneg s, (Int.fract_lt_one s).le⟩, fun i => ?_⟩
  have h := hx i
  rw [← AddCircle.coe_zsmul, zsmul_eq_mul, UnitAddCircle.norm_eq] at h
  -- `v i * fract s` and `v i * s` differ by the integer `v i * ⌊s⌋`
  have e : distInt ((v i : ℝ) * Int.fract s) = |(v i : ℝ) * s - round ((v i : ℝ) * s)| := by
    have e1 : (v i : ℝ) * Int.fract s = (v i : ℝ) * s - ((v i * ⌊s⌋ : ℤ) : ℝ) := by
      rw [Int.cast_mul, ← Int.self_sub_floor]
      ring
    unfold distInt
    rw [e1, round_sub_intCast, Int.cast_sub, sub_sub_sub_cancel_right]
  rw [ge_iff_le, e]
  exact h

#print axioms weak_bound
