/-
TOGETHER · PROOF TABLE 003 · LEAN CHECK of the relay's W1 and W2 (ledger v2, 14:43 +08)

Definition used: `Nat.Powerful`, exactly as carried in Optio's `Erdos364/Defs.lean`
(from google-deepmind/formal-conjectures):

    def Full (k : ℕ) (n : ℕ) : Prop := ∀ p ∈ n.primeFactors, p^k ∣ n
    abbrev Powerful : ℕ → Prop := (2).Full

Under it `0` and `1` are powerful (see `powerful_zero`, `powerful_one` below).

Compile inside a checkout of github.com/ibrahimmian36/Optio (commit 3319f637):
    lake exe cache get && lake build Erdos364.Defs && lake env lean PT003.lean
No `sorry`, no `admit`, no `axiom`, no `native_decide`.
-/
import Erdos364.Defs
import Mathlib

namespace PT003

/-! ## 0. The definition, and basic lemmas -/

/-- The prime-by-prime content of `Nat.Powerful` (also true for `m = 0`). -/
theorem dvd_sq_of_powerful {m p : ℕ} (hp : p.Prime) (hm : m.Powerful) (hd : p ∣ m) :
    p ^ 2 ∣ m := by
  by_cases h0 : m = 0
  · subst h0; exact dvd_zero _
  · exact hm p (Nat.mem_primeFactors.mpr ⟨hp, hd, h0⟩)

/-- `Nat.Powerful` says: every prime dividing `n` has its square dividing `n`. -/
theorem powerful_iff (n : ℕ) :
    n.Powerful ↔ ∀ p : ℕ, p.Prime → p ∣ n → p ^ 2 ∣ n := by
  constructor
  · intro h p hp hd
    exact dvd_sq_of_powerful hp h hd
  · intro h p hp
    exact h p (Nat.prime_of_mem_primeFactors hp) (Nat.dvd_of_mem_primeFactors hp)

/-- In exponent language (the language of the relay's W2 proof). -/
theorem powerful_iff_exponents {n : ℕ} (hn : n ≠ 0) :
    n.Powerful ↔ ∀ p : ℕ, p.Prime → p ∣ n → 2 ≤ n.factorization p := by
  constructor
  · intro h p hp hd
    exact (hp.pow_dvd_iff_le_factorization hn).mp (dvd_sq_of_powerful hp h hd)
  · intro h p hpm
    have hp := Nat.prime_of_mem_primeFactors hpm
    exact (hp.pow_dvd_iff_le_factorization hn).mpr (h p hp (Nat.dvd_of_mem_primeFactors hpm))

theorem powerful_zero : Nat.Powerful 0 := by
  intro p hp
  simp at hp

theorem powerful_one : Nat.Powerful 1 := by
  intro p hp
  simp at hp

theorem not_powerful_two : ¬ Nat.Powerful 2 := by
  intro h
  have := dvd_sq_of_powerful Nat.prime_two h (dvd_refl 2)
  norm_num at this

/-- Squares are powerful. -/
theorem powerful_sq (a : ℕ) : (a ^ 2).Powerful := by
  intro p hp
  have hpp : p.Prime := Nat.prime_of_mem_primeFactors hp
  have hd : p ∣ a ^ 2 := Nat.dvd_of_mem_primeFactors hp
  exact pow_dvd_pow_of_dvd (hpp.dvd_of_dvd_pow hd) 2

/-! ## W1 · the 39 residues mod 900 -/

/-- The relay's list (T3 Kimi and T4 GPT on the wall; identical to the list in the request). -/
def R : List ℕ :=
  [7, 27, 71, 99, 107, 151, 171, 187, 207, 223, 251, 287, 323, 331, 351, 367, 387, 423,
   431, 467, 475, 511, 531, 547, 567, 575, 611, 647, 675, 691, 711, 727, 747, 791, 799,
   827, 871, 891, 899]

theorem R_length : R.length = 39 := by decide
theorem R_nodup : R.Nodup := by decide
theorem R_lt : ∀ r ∈ R, r < 900 := by decide

/-- "Not ruled out by 2, 3, 5": for each of `n, n+1, n+2` and each `p ∈ {2,3,5}`,
`p ∣ n+i → p² ∣ n+i`.  (Computational form with `%`; the `∣` form is `W1_exact`.) -/
def LocalOK (n : ℕ) : Prop :=
  ∀ i ∈ [0, 1, 2], ∀ p ∈ [2, 3, 5], (n + i) % p = 0 → (n + i) % (p * p) = 0

instance : DecidablePred LocalOK := fun n => by unfold LocalOK; infer_instance

-- Finite core: all 900 residues, evaluated by the kernel (`decide +kernel`, not `native_decide`).
set_option maxRecDepth 100000 in
theorem finite_core : ∀ r, r < 900 → (LocalOK r ↔ r ∈ R) := by decide +kernel

/-- `LocalOK` only depends on `n mod 900`. -/
theorem localOK_mod (n : ℕ) : LocalOK (n % 900) ↔ LocalOK n := by
  constructor
  · intro h i hi p hp
    have := h i hi p hp
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hi hp
    rcases hi with rfl | rfl | rfl <;> rcases hp with rfl | rfl | rfl <;> omega
  · intro h i hi p hp
    have := h i hi p hp
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hi hp
    rcases hi with rfl | rfl | rfl <;> rcases hp with rfl | rfl | rfl <;> omega

theorem localOK_iff_dvd (n : ℕ) :
    LocalOK n ↔ ∀ i ∈ [0, 1, 2], ∀ p ∈ [2, 3, 5], p ∣ n + i → p ^ 2 ∣ n + i := by
  constructor
  · intro h i hi p hp hd
    have := h i hi p hp (Nat.mod_eq_zero_of_dvd hd)
    rw [pow_two]; exact Nat.dvd_of_mod_eq_zero this
  · intro h i hi p hp hm
    have := h i hi p hp (Nat.dvd_of_mod_eq_zero hm)
    rw [pow_two] at this; exact Nat.mod_eq_zero_of_dvd this

/-- **W1 (optional part): the set is exactly the residues not ruled out by 2, 3, 5.** -/
theorem W1_exact (n : ℕ) :
    (∀ i ∈ [0, 1, 2], ∀ p ∈ [2, 3, 5], p ∣ n + i → p ^ 2 ∣ n + i) ↔ n % 900 ∈ R :=
  (localOK_iff_dvd n).symm.trans
    ((localOK_mod n).symm.trans (finite_core (n % 900) (Nat.mod_lt _ (by norm_num))))

/-- **W1 (requested statement).** If `n, n+1, n+2` are all powerful, then `n % 900 ∈ R`. -/
theorem W1 {n : ℕ} (h0 : n.Powerful) (h1 : (n + 1).Powerful) (h2 : (n + 2).Powerful) :
    n % 900 ∈ R := by
  apply (W1_exact n).mp
  intro i hi p hp hd
  simp only [List.mem_cons, List.not_mem_nil, or_false] at hi hp
  have hpp : p.Prime := by
    rcases hp with rfl | rfl | rfl
    · exact Nat.prime_two
    · exact Nat.prime_three
    · exact Nat.prime_five
  rcases hi with rfl | rfl | rfl
  · exact dvd_sq_of_powerful hpp h0 hd
  · exact dvd_sq_of_powerful hpp h1 hd
  · exact dvd_sq_of_powerful hpp h2 hd

/-! ### The relay's stated reason, as an exact characterisation

"n+1 ≡ 0 mod 4; whichever of the three is divisible by 3 is divisible by 9;
any one divisible by 5 is divisible by 25." -/

def ReasonOK (n : ℕ) : Prop :=
  (n + 1) % 4 = 0 ∧ (∀ i ∈ [0, 1, 2], 3 ∣ n + i → 9 ∣ n + i) ∧
    (∀ i ∈ [0, 1, 2], 5 ∣ n + i → 25 ∣ n + i)

instance : DecidablePred ReasonOK := fun n => by unfold ReasonOK; infer_instance

set_option maxRecDepth 100000 in
theorem reason_core : ∀ r, r < 900 → (ReasonOK r ↔ r ∈ R) := by decide +kernel

theorem reasonOK_mod (n : ℕ) : ReasonOK (n % 900) ↔ ReasonOK n := by
  have e4 : (n % 900 + 1) % 4 = 0 ↔ (n + 1) % 4 = 0 := by omega
  have a3 (i : ℕ) : 3 ∣ n % 900 + i ↔ 3 ∣ n + i := by omega
  have a9 (i : ℕ) : 9 ∣ n % 900 + i ↔ 9 ∣ n + i := by omega
  have a5 (i : ℕ) : 5 ∣ n % 900 + i ↔ 5 ∣ n + i := by omega
  have a25 (i : ℕ) : 25 ∣ n % 900 + i ↔ 25 ∣ n + i := by omega
  unfold ReasonOK
  constructor
  · rintro ⟨h4, h3, h5⟩
    exact ⟨e4.mp h4, fun i hi hd => (a9 i).mp (h3 i hi ((a3 i).mpr hd)),
      fun i hi hd => (a25 i).mp (h5 i hi ((a5 i).mpr hd))⟩
  · rintro ⟨h4, h3, h5⟩
    exact ⟨e4.mpr h4, fun i hi hd => (a9 i).mpr (h3 i hi ((a3 i).mp hd)),
      fun i hi hd => (a25 i).mpr (h5 i hi ((a5 i).mp hd))⟩

/-- The relay's three conditions hold for `n` iff `n % 900` is in the list. -/
theorem W1_reason_exact (n : ℕ) :
    ((n + 1) % 4 = 0 ∧ (∀ i ∈ [0, 1, 2], 3 ∣ n + i → 9 ∣ n + i) ∧
      (∀ i ∈ [0, 1, 2], 5 ∣ n + i → 25 ∣ n + i)) ↔ n % 900 ∈ R :=
  (reasonOK_mod n).symm.trans (reason_core (n % 900) (Nat.mod_lt _ (by norm_num)))

/-- The relay's three conditions do follow from a powerful triple. -/
theorem W1_reason {n : ℕ} (h0 : n.Powerful) (h1 : (n + 1).Powerful) (h2 : (n + 2).Powerful) :
    (n + 1) % 4 = 0 ∧ (∀ i ∈ [0, 1, 2], 3 ∣ n + i → 9 ∣ n + i) ∧
      (∀ i ∈ [0, 1, 2], 5 ∣ n + i → 25 ∣ n + i) :=
  (W1_reason_exact n).mpr (W1 h0 h1 h2)

/-! ### Ledger entry "REFUTED: T2's W1 list (7 extra, 7 missing)" -/

/-- T2's final list, copied from the wall (table.txt line 425). -/
def T2 : List ℕ :=
  [7, 27, 71, 99, 107, 117, 151, 187, 207, 223, 225, 251, 287, 297, 323, 331, 367, 387,
   431, 467, 475, 477, 511, 547, 567, 575, 611, 647, 657, 691, 727, 747, 765, 791, 799,
   827, 837, 871, 899]

theorem T2_extra : T2.filter (fun r => decide (r ∉ R)) = [117, 225, 297, 477, 657, 765, 837] := by
  decide

theorem T2_missing : R.filter (fun r => decide (r ∉ T2)) = [171, 351, 423, 531, 675, 711, 891] := by
  decide

/-! ## W2 · infinitely many pairs of consecutive powerful numbers (the relay's proof, T7) -/

/-- The relay's sequence.  Index `k` here is the relay's `k + 1` (so `xy 0 = (x₁, y₁) = (3, 1)`). -/
def xy : ℕ → ℕ × ℕ
  | 0 => (3, 1)
  | k + 1 => (3 * (xy k).1 + 8 * (xy k).2, (xy k).1 + 3 * (xy k).2)

def x (k : ℕ) : ℕ := (xy k).1
def y (k : ℕ) : ℕ := (xy k).2

theorem x_zero : x 0 = 3 := rfl
theorem y_zero : y 0 = 1 := rfl
theorem x_succ (k : ℕ) : x (k + 1) = 3 * x k + 8 * y k := rfl
theorem y_succ (k : ℕ) : y (k + 1) = x k + 3 * y k := rfl

/-- The first eight terms (the ones checked by T8 and by the chair). -/
theorem first_eight :
    (List.range 8).map (fun k => (x k, y k)) =
      [(3, 1), (17, 6), (99, 35), (577, 204), (3363, 1189), (19601, 6930),
       (114243, 40391), (665857, 235416)] := by
  decide

/-- Step ①, the identity on the wall: `(3x+8y)² − 8(x+3y)² = x² − 8y²` for all integers. -/
theorem identity (a b : ℤ) : (3 * a + 8 * b) ^ 2 - 8 * (a + 3 * b) ^ 2 = a ^ 2 - 8 * b ^ 2 := by
  ring

/-- Step ①, the invariant: `x_k² = 8·y_k² + 1`. -/
theorem pell (k : ℕ) : x k ^ 2 = 8 * y k ^ 2 + 1 := by
  induction k with
  | zero => norm_num [x_zero, y_zero]
  | succ k ih =>
    rw [x_succ, y_succ]
    nlinarith [ih]

/-- The same invariant in the wall's form `x_k² − 8·y_k² = 1`, over the integers. -/
theorem pell_int (k : ℕ) : (x k : ℤ) ^ 2 - 8 * (y k : ℤ) ^ 2 = 1 := by
  have h : ((x k : ℕ) : ℤ) ^ 2 = 8 * ((y k : ℕ) : ℤ) ^ 2 + 1 := by exact_mod_cast pell k
  linarith

theorem x_pos (k : ℕ) : 0 < x k := by
  induction k with
  | zero => norm_num [x_zero]
  | succ k ih => rw [x_succ]; omega

theorem y_pos (k : ℕ) : 0 < y k := by
  induction k with
  | zero => norm_num [y_zero]
  | succ k ih => rw [y_succ]; omega

/-- Step ③: `y_{k+1} − y_k = x_k + 2·y_k > 0`. -/
theorem y_lt_succ (k : ℕ) : y k < y (k + 1) := by
  rw [y_succ]
  have := x_pos k
  have := y_pos k
  omega

theorem y_strictMono : StrictMono y := strictMono_nat_of_lt_succ y_lt_succ

/-- Step ②, first exponent claim: in `8m²` the exponent of 2 is `3 + 2·v₂(m)`. -/
theorem exponent_two {m : ℕ} (hm : m ≠ 0) :
    (8 * m ^ 2).factorization 2 = 3 + 2 * m.factorization 2 := by
  have h8 : (8 : ℕ) = 2 ^ 3 := by norm_num
  rw [Nat.factorization_mul (by norm_num) (pow_ne_zero 2 hm), h8, Nat.factorization_pow,
    Nat.factorization_pow, Nat.Prime.factorization Nat.prime_two]
  simp

/-- Step ②, second exponent claim: for a prime `p ≠ 2` the exponent in `8m²` is `2·v_p(m)`. -/
theorem exponent_odd {m p : ℕ} (hm : m ≠ 0) (hp2 : p ≠ 2) :
    (8 * m ^ 2).factorization p = 2 * m.factorization p := by
  have h8 : (8 : ℕ) = 2 ^ 3 := by norm_num
  rw [Nat.factorization_mul (by norm_num) (pow_ne_zero 2 hm), h8, Nat.factorization_pow,
    Nat.factorization_pow, Nat.Prime.factorization Nat.prime_two]
  simp [Ne.symm hp2]

/-- Step ②, as argued on the wall: `8m²` is powerful, through the exponents. -/
theorem powerful_eight_mul_sq {m : ℕ} (hm : m ≠ 0) : (8 * m ^ 2).Powerful := by
  have hne : 8 * m ^ 2 ≠ 0 := by positivity
  rw [powerful_iff_exponents hne]
  intro p hp hd
  by_cases h2 : p = 2
  · subst h2
    rw [exponent_two hm]
    omega
  · rw [exponent_odd hm h2]
    have hpm : p ∣ m := by
      rcases (Nat.Prime.dvd_mul hp).mp hd with h | h
      · exfalso
        have h8 : (8 : ℕ) = 2 ^ 3 := by norm_num
        rw [h8] at h
        exact h2 ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp (hp.dvd_of_dvd_pow h))
      · exact hp.dvd_of_dvd_pow h
    have := hp.factorization_pos_of_dvd hm hpm
    omega

/-- Steps ① and ② together: `(8·y_k², x_k²)` are consecutive and both powerful. -/
theorem pair (k : ℕ) : (8 * y k ^ 2).Powerful ∧ (8 * y k ^ 2 + 1).Powerful := by
  refine ⟨powerful_eight_mul_sq (y_pos k).ne', ?_⟩
  rw [← pell k]
  exact powerful_sq _

/-- Step ③: the pairs are all different. -/
theorem pairs_strictMono : StrictMono (fun k => 8 * y k ^ 2) := by
  intro a b hab
  have h1 : y a < y b := y_strictMono hab
  have h2 : y a ^ 2 < y b ^ 2 := Nat.pow_lt_pow_left h1 (by norm_num)
  show 8 * y a ^ 2 < 8 * y b ^ 2
  linarith

/-- **W2 (requested statement).** -/
theorem W2 : Set.Infinite {n : ℕ | Nat.Powerful n ∧ Nat.Powerful (n + 1)} :=
  Set.infinite_of_injective_forall_mem pairs_strictMono.injective pair

/-- W2 restricted to positive `n` (so the Lean convention "0 is powerful" plays no role). -/
theorem W2_pos : Set.Infinite {n : ℕ | 0 < n ∧ Nat.Powerful n ∧ Nat.Powerful (n + 1)} :=
  Set.infinite_of_injective_forall_mem pairs_strictMono.injective
    (fun k => ⟨by have := y_pos k; positivity, pair k⟩)

end PT003

#print axioms PT003.W1
#print axioms PT003.W1_exact
#print axioms PT003.W1_reason_exact
#print axioms PT003.W1_reason
#print axioms PT003.R_length
#print axioms PT003.R_nodup
#print axioms PT003.T2_extra
#print axioms PT003.T2_missing
#print axioms PT003.W2
#print axioms PT003.W2_pos
#print axioms PT003.pell
#print axioms PT003.pair
#print axioms PT003.powerful_eight_mul_sq
#print axioms PT003.exponent_two
#print axioms PT003.exponent_odd
#print axioms PT003.first_eight
#print axioms PT003.powerful_iff
#print axioms PT003.powerful_zero
#print axioms PT003.powerful_one
