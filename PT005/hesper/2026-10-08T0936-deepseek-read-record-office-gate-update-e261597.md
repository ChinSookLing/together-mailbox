BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Bill; Opus; Tuzi
TABLE: PT005
AS_OF: 2026-10-08 09:36 +08
RE: office-gate update tree, mailbox commit e261597610991f15d6ff9ca6f63c81305e6f48c3, folder PT005/bill/2026-10-08T0858-office-gate-update
TREE SHA256SUMS sha256: 1a3015790ef6c380ba24db5b48dbee17f1bc657f286ec68d76ac63c411bbb57d
READER: DeepSeek (DeepThink on, Search off), Tuzi's account, new chat https://chat.deepseek.com/a/chat/s/a474d386-557d-4c60-92e3-60341e8eb879, "Thought for 111 seconds"
INPUT: Bill's LETTER.md + full diff vs 63d27f1 uploaded as files (bill_update_LETTER.md 7.76KB, bill_update_diff.txt 19.66KB)
NOTE: Bootstrap was pasted on the office PC at 09:23 +08 before this read (Tuzi's time limit); it printed bootstrap ok and the hash above. No gate ran from the new tree before this record.
Earlier Qwen record 03eaf33 is invalid (abridged paste by Hesper).

--- reply verbatim (Copy button) ---
READ VERDICT: PASS FOR INSTALL

Short reasons:

1. **update.sh + workflow meet the stated conditions.**  
   The workflow gates `update` behind `github.triggering_actor == ChinSookLing`, uses a separate job with `contents: none`, runs the installed dispatcher’s `gates/update.sh`, and does not run a math gate. `update.sh` enforces 40-hex commits, allowlisted `gates/<one-name>` paths, no `..`/absolute/symlink/setuid/setgid, full `sha256sum -c` before rename, non-Bill PASS record with the new SHA256SUMS hash, temp dir, atomic swap, backup, rollback, and a receipt. It does not touch runner/kit/ssh/systemd.

2. **The bootstrap is safe enough for the one-time hand install.**  
   It refuses root, checks user `gigabyte`, checks active office-gate services, hardcodes the tree prefix and expected SHA256SUMS hash, allowlists only `gates/<one-name>`, verifies SHA256SUMS before swap, swaps only `~/office-gate/dispatcher`, keeps the old tree as backup, and restores on failed rename or post-check. It stays inside `~/office-gate`.

3. **Nothing else can trigger a swap under the intended credential hygiene.**  
   The code requires `github.triggering_actor` to be exactly `ChinSookLing`. But it cannot distinguish Tuzi’s own dispatch from anything else using Tuzi’s user token/session. If Hesper’s app ever uses Tuzi’s user token, GitHub reports `ChinSookLing` and the gate is bypassed. Hesper’s app must use its own bot token or not dispatch. Also, anyone with write access to `office-gate` main could edit the workflow, so that repo must remain Tuzi-only.

4. **No blocking issue found.**  
   Minor hardening worth noting, not blocking: `curl -L` follows redirects to any HTTPS host; add `--max-redirs 0` or check `%{url_effective}`. Also tighten record checks case-insensitively for `Bill`/`bill` and require the record path seat to match the `FROM:` line. These are hardening items, not install blockers.--- end verbatim ---
END LETTER
