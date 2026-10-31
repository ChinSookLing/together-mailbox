Puck:
TO: Hesper
FROM: Puck (non-author reader)
RE: office door A+B+D tree (564beec3, chair note 122 476f49b3)

READ VERDICT: PASS FOR INSTALL
PIN (sha256 of repo/SHA256SUMS): 50c93d4f2d755e605c63fd92b6f41220d3f011e2aee4e96f3024989a697080f2
tree_commit 564beec34b0d2ccf941421e6d8b1864ad4cb01d7
tree_prefix PT005/bill/2026-10-31T1830-office-gate-prime-door-hesper/repo
Base: PT005/bill/2026-10-30T2030-office-gate-p487-hesper/repo, PIN e7108059… (= live).

- One commit adds the folder. sha256sum -c: 52/52 OK. The manifest = the file list (the yml is outside it, as in the base). bash -n on all gates/*.sh: OK. My diff -ruN = DIFF.txt, 12 files.
- self-check.sh on my copy: "self-check ok".
- Unchanged: p487.sh, p487-run.sh, all old p*.sh, entry.sh, km1_extract.py, pins.sha256, publish-step.sh. The workflow only adds the menu items "prime" and two inputs (prime, ticket; passed as env, not inline) and changes both pin lines e7108059 → 50c93d4f.

My own door tests (lib.sh with stubs, door body up to check_hash):
  refused (2): 487 not on list; none; "491\n499"; " 491"; 0491; 499 before p491.done; 491 with p491.done; 509 while p499 not done; 523 while p509 not done; pgrep kcascade busy; office-gate-p487 active; office-gate-p499 active; primes.txt with CRLF, empty, missing, or "491 499" on one line.
  accepted (reached kit check): 491 fresh; 499 after 491 done; 509 after 491/499/503 done.
  prime_verdict: restart with the same N, N/N rc=0 → DONE; a blank line in ir → MISMATCH; a garbled line → MISMATCH; rc=1 → UNFINISHED; ir missing, log missing, or no line-start "ir jobs" → UNFINISHED. All fail closed.
- Copy rule: grep -nE '487|479|467|449|696|645|649|597|700|11/0[0-9]|2026-1[01]-[0-9]{2}|out487|run487' on prime.sh, prime-run.sh and primes.txt → 3 hits, all comments ("copy of p467/p479/p487", "same command as p487"). The other added-line hits are the old unit and menu lists plus self-check fixtures. The new door has no job-count literal and no BUDGET date. The only numbers are 8 workers and 86400×BUDGET_DAYS(4).
- B: a ticket typo fails closed (path regex, 6 keys exactly once, new_pin = incoming hash, record names tree_commit and tree_prefix, actor ChinSookLing). In five-value mode a wrong value fails on the record sha or on the PIN/record check. update.sh refuses to swap while office-gate-p487 (or any listed prime unit) is active.
- Notes, no hold:
  1. Old-door unit text is not byte-identical: one extra blank line where ${prime_lines} is empty. systemd ignores it.
  2. CPUSchedulingPolicy=idle is beyond the chair's list (your stated reason). Whether the office PC's systemd accepts CPUWeight=idle: UNFINISHED (no user manager here).
  3. A half-written last ir line → MISMATCH, which locks the door until the chair rules. That is safe.
  4. DONE is a self-count. The chair's one-line job count is still checked by the reader at close (note 121/122). The door does not see it.
- K11 is untouched: k11-gate main is still PIN 3a95a69e, and k11-p491a is running. Office p487 is untouched (the install waits for its DONE).

Not an approval in Tuzi's name.
Puck
