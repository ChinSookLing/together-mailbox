---
ROUND: PT005 R20b
SEAT: DeepSeek
CARRIED_BY: Puck
SEND_TEXT: PT005/hesper/r20b-send-texts/send_DeepSeek.txt (last changed 52dabab, 3301 B, sha256 cb6e850d...)
CHAT: PT005 · Big Picture https://chat.deepseek.com/a/chat/s/e008b16c-7253-44d7-ab76-60faf3f73202
MODE: DeepThink ON, Search OFF (no model name shown in UI)
SENT: 2026-10-13 08:26:54 +08
RECEIVED: 2026-10-13 08:27:59 +08
NOTE: final answer only, thinking trace not included; no data file attached (lens 2 needs none)
---

**ANSWER BLOCK**

**Assignment:** Can closed gates enter the bound \(B\) (Allikvere Thm 3.8 / L8)?

**Verdict:** Clear **no**, under the standard reading that \(B\) is a uniform analytic threshold.  
**PROOF (under stated assumption):** Allikvere Thm 3.8 gives a single number \(B\) such that for every prime \(p>B\), no 14-cover exists. The proof of such a bound uses only universal inequalities—Dirichlet approximation, geometry of numbers, zonotope covering—not finite computations for specific primes. Closed gates are computational facts of the form “for this \(p\), gate (a)/(b)/(c) is empty.” They are not universal statements and cannot be hypotheses in a uniform analytic proof.  
**What closed gates can do:** They can shrink the finite check set: if \(B\) is already small enough, or if the theorem is conditional on checking \(p\le B\), then closed gates remove those \(p\) from the check. But they do not lower \(B\) itself.  
**What would be needed to enter \(B\):** A new analytic lemma showing that a closed gate at some prime \(p_0\) forces a stronger inequality for all \(p>p_0\). No such lemma exists in the ledger.  
**Caveat:** If the actual Thm 3.8 explicitly allows computational input into the bound, this verdict changes. We do not have its text in this chat. **UNFINISHED** on that specific point.

**Least-sure step:** Whether Thm 3.8 is purely analytic or already conditional on a finite check.

**Reasoning**

FACT: L7 is a sufficient condition for a rational \(t\) to avoid all speeds in a set \(E\). FACT: L8 is presumably the ledger entry for Allikvere Thm 3.8, which gives a bound \(B\) on primes that need checking. IDEA: Closed gates are results like “\(p=383\) has no 14-cover,” proved by census. PROOF: A uniform bound \(B\) cannot depend on a finite list of exceptions. If it did, it would not be a bound; it would be a case distinction. Therefore closed gates cannot be substituted into the derivation of \(B\).

IDEA: One might try to use closed gates to prove a stronger version of L7. For example, if for all \(p\le 190\) every improper lift satisfies L7, then perhaps for \(p>190\) the same holds by a monotonicity argument. But that is exactly the target lemma, not a consequence of closed gates. The target lemma is still open. FACT: The data at \(p=131\) show 2,467,648 improper level-16 lifts all handled by L7. IDEA: That supports the target lemma but does not prove it. It also does not enter \(B\).

PROOF: The bound \(B\) in Allikvere Thm 3.8 is a threshold in a theorem of the form \(\forall p>B\). If we replace \(B\) by a function that depends on closed gates, the statement becomes “for all \(p>B\) except those in a finite set,” which is not a single bound. The only way closed gates enter is if the theorem is stated as “check \(p\le B\) by computer; for \(p>B\) use analysis.” Then closed gates reduce the computer check, not \(B\).

UNFINISHED: Without the exact text of Allikvere Thm 3.8, we cannot rule out that its proof uses a finite check as an intermediate step. If so, closed gates could reduce that intermediate check, but the final bound \(B\) would still be the same. The question asks “enter the bound \(B\),” not “enter the proof.” So the answer remains no.

**Shortest path to a proof of the target lemma:** Show that any improper lift of a core-containing row either satisfies L7 directly or maps to a smaller case. The \(p=131\) data suggest a \(4\times\) growth per level, which is a structural recurrence. Proving that recurrence is the engine. But that is separate from Dish B / bound \(B\).