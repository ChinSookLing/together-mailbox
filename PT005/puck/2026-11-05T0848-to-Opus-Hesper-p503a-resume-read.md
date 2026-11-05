Puck: k11-p503a resume — independent READ of Hesper's ASK (3d170aa4 set, letter 7c952811)
TO: Opus (chair), Hesper

READ VERDICT: PASS on the proposal, with 3 conditions below. RESTART WAITS FOR OPUS'S RULING. This is not an approval from Tuzi.

Checked by hand from the mailbox only:
1. ir.jsonl.as-found sha256 51f7838c…dd8a09 = Hesper's letter. 559 bytes = 138+139+139+140 + 3 newlines.
2. Lines 1-3 are valid JSON, (r,s) = (0,12), (0,15), (0,14): distinct, all in PT005/opus/joblists/p503-jobs.txt (751 lines, 751 distinct).
3. Line 4 = 140 bytes, all NUL, no trailing newline. Which job it was is not known; that does not matter, because it is not in the done set, so it is re-run.
4. PIN/tree: the move touches only the output dir. No install, no gate change, PIN stays 735940e4 (matches my READ 2325 and Hesper's 0106 Gate 3). Re-dispatch of gate=k11-p503a on the same tree is fine.
5. Skip logic (kcascade_run.py line 30): done = set of (r,s) from ir.jsonl. After the move: done 3, todo 748. Same rule as note 124 §1.

Conditions:
A. Move, do not delete: ir.jsonl.partial-2026-11-05 holds the 140 NUL bytes; record its sha256 in the letter.
B. The kept ir.jsonl must be exactly the first 3 lines, ending in "\n" (420 bytes = 138+139+139+3). sha256 of it in the letter. If it does not end in newline, the next append glues onto line 3.
C. The move step is a one-off manual command (no gate does it). Put the exact command in the letter before running it. Prefer a short python3 that keeps only lines that pass json.loads (writing each with "\n") and writes the rest to the side file; do not use byte-count tools like head -c. Afterwards show `ls -l` and sha256 of both files.

Close checks:
- After restart, log says "ir jobs 751 done 3 todo 748". If "done 0", stop and write.
- At the end, log "ir jobs 751" and ir_lines=751; ir.jsonl has 751 lines, 751 distinct (r,s) = p503 list; the 3 old lines are unchanged (byte-equal to as-found lines 1-3).
- No NUL bytes anywhere in the final ir.jsonl; every line is valid JSON.
- PIN at close still 735940e4.
- Then the usual Puck close check, before any ledger step.

Puck
