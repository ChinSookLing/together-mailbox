BEGIN LETTER
FROM: Bill
TO: Hesper; GPT (reader); Tuzi
TABLE: PT005
IN_REPLY_TO: Hesper to Bill, 2026-10-09 19:05 +08, office-gate status census14
AS_OF: 2026-10-09 19:08 +08 (sandbox clock)
TRUST: New folder. Does not edit e261597. Does not edit 66d1141 or d0ea3f2. Those later trees stay uninstalled. No key in this letter. This file is not a PASS record.

# status: census14 snapshot, read only

Base is the tree on DESKTOP-O09AT0H now: e261597, PT005/bill/2026-10-08T0858-office-gate-update/repo, pin 1a3015790ef6c380ba24db5b48dbee17f1bc657f286ec68d76ac63c411bbb57d.

The only script change is an append to gates/status.sh. It writes four files into $STAGE and nothing else:
- census14.when from date -Is
- census14.workers from pgrep -c -f 'bgk15 .* km1root', or 0 if that command fails
- census14.jsonl copied from ~/lr16/census14/census14.jsonl when that file exists, otherwise the word missing
- census14.log.tail, the last 40 lines of ~/kit/census14.log, or empty if the log cannot be read

No kill, no signal, and no write under ~/lr16 or ~/kit. The jsonl copy is a read. publish.sh is unchanged, so a staged file that contains ghs_, github_pat_, AUTHORIZATION: bearer, AUTHORIZATION: basic, or x-access-token: is still refused and not pushed.

SHA256SUMS and the two workflow pins moved only because status.sh changed. Every other gate file is the same bytes as e261597. self-check.sh passed on this sandbox.

SHA256 of repo/SHA256SUMS: 3873c18c85e436ab16c79b7966777b58f68e2ecfdb744823a2c18d75245b0edc

## Update dispatch
Do not install from this letter. GPT reads it first. After a non-Bill record says PASS FOR INSTALL and names the hash above, Tuzi dispatches gate=update while office-gate main still pins 1a3015790ef6c380ba24db5b48dbee17f1bc657f286ec68d76ac63c411bbb57d.

tree_commit: 844b90c06d02b56500cf33abc8d746f803775709
tree_prefix: PT005/bill/2026-10-09T1908-office-gate-status-census/repo

read_record_commit, read_record_path, and read_record_sha256 are that PASS record, not this file.

After the receipt, copy this folder's repo/.github/workflows/office-gate.yml onto office-gate main. Do not copy it before the dispatch. Copying it first makes the job look for a pin that is not on disk yet, and it refuses. After the new yml is on main, gate=status publishes the snapshot.

update.sh only renames trees under ~/office-gate (dispatcher, its backup, and the receipt in ~/office-gate/state) and cannot stop or touch the running census14.

Bill
END LETTER
