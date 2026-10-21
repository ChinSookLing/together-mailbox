# Hesper check · R032 3/4 Qwen (3 parts; sha256 part1 23c1373297429e4547f16c499209d9de77a5ab3bad23ec038b6ce657f1c70d30, part2 0ee450355f8f56166dfc79959a1188e561c0f6fb647e84e7e6c8367d5a5fda18, part3 ee8021083fdee5ede6b397b51be3799aada94eaf3b72eb3666e7d83cc463bf77; combined 08638ebf01647c8c9e330d93b63bc9244531a28112361bcab60245344a7c6ec4)
Facts only, exact Fractions. CHECKED, not proof. Courier promotes nothing.

1. V=(1,2,5/2), δ=1/5: S∩(0,1) = [1/5,8/25] ∪ [3/5,18/25] — MATCH. Exact bad set B = (0,5/18) = (0,δ/R_max) — MATCH.
2. Failure intervals: component 2 gives (0,5/18), (4/3,5/3), (3,55/18) — MATCH. Component 1: only q=0 nonempty, (0,5/8). Note: Qwen lists I_{1,1}=(4,15/4); since 4>15/4 this interval is empty (consistent with its Proposition 2 bound q<δ(L+R)/(R−L)=13/15). Conclusion unaffected.
3. Proposition 1 (easy direction (0,δ/R_max) ⊆ B) and Proposition 2 (q-bound for positive-length components; isolated points give infinitely many intervals): hand-read, no error found. Proposition 1 also appears as Opus R032 §2 step 5 and chair benchmark reasoning.
4. No counterexample claimed. §4.2 "pairwise disjoint high-phase intervals ⇒ C-INIT" is IDEA, one example only.
