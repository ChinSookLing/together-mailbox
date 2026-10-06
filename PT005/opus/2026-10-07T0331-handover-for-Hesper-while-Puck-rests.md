# Handover · PT005 work for Hesper while Puck rests (until Sunday 2026-10-11)

From: Opus (chair) · 2026-10-07 03:31 +08 (machine clock) · Asked for by Tuzi (03:31)
Welcome, Hesper. Please first add your self-introduction in `PT005/hesper/` (who you are, where you run, what you can do: mailbox read/write, office-PC commands, wall posting, sending packets to other seats, and whether it costs Tuzi money).

## Rules of this table (short)

- **Times and hashes are copied from the machine, never typed from memory** (`date '+%F %T %Z'`, `sha256sum`).
- **No read record, no run.** Any code that is new or changed is read by someone who is not its author before it runs on the office PC. Every file named below already has a read record unless marked otherwise.
- **No keys or passwords** in chats, the mailbox or the wall. Use your own access. Never Puck's key.
- **Ledger status changes only with Tuzi's explicit approval.** Hesper and Opus propose; Tuzi decides.
- **No paid compute or paid top-ups.** If something needs money, stop and tell Tuzi.
- **Commit footers:** use your own name. Copy texts from other seats verbatim, under a short courier header (seat, chat link if any, time, model).

## Tasks, in this order

### 1. Bring back the p = 233 results (the run finished on the office PC on Tue 2026-10-06)
Totals seen by Tuzi in the terminal already match the chair. What is still missing is the files themselves and the compare.
- Files to commit under `PT005/hesper/officepc-p233/`:
  - from `~/core233/`: `cores.jsonl`, `run.log`, `run.time`, `km1low.log`, `kit.sha256`;
  - from `~/lr16/out233/`: `ir.jsonl`;
  - from `~/kit/`: `run233.log`, `run233.time`;
  - from `~/lr16/out233/km1.json`: only its sha256 plus the lines that are not `l4=0` (the file is large).
- Then run the two compares. Both scripts are already read; they are in the mailbox.
  - `python3 compare_cores.py ~/core233/cores.jsonl chair_cores233.jsonl`
    - script: `scouting/LR16/opus/core223/compare_cores.py`
    - reference: `scouting/LR16/opus/gate233/chair_cores233.jsonl`
  - `python3 compare_239.py ~/lr16/out233 ir_K15_p233.jsonl km1_K15_p233.json`
    - script: `scouting/LR16/opus/officepc/compare_239.py`
    - references: in `gate233/`
- Commit both outputs. The chair will check them and ask Tuzi about ledger entry L12.

### 2. Run p = 191 (all three parts)
- Follow `scouting/LR16/opus/gate191/RUN-SHEET-p191.md`. It needs **no new code**. ESTIMATE about 40 minutes.

### 3. DeepSeek read for p = 241 (c), before running 241 (c)
- Send DeepSeek chair note 36 (`PT005/opus/2026-10-06T1516-chair-note-36-early-L7-p241-closed.md`) and `scouting/LR16/opus/gate241/shift_rows_early.cpp` (sha256 `7487a9c5…`).
- Ask two things:
  1. Is the difference from `gate233/shift_rows.cpp` exactly those 5 lines?
  2. Is using L7 already at levels 4 and 8 (D = 4 or 8) justified by the same reasons as the USE line of ledger L7?
- Commit the reply verbatim.

### 4. Run p = 241
- **(a)+(b)** need no new code, so they may start right after 191, before DeepSeek's read. Use `kcascade_run.py` per `gate241/RUN-SHEET-p241.md`. ESTIMATE: several hours. One part runs on a single core.
- **(c)** only after DeepSeek's read record exists. With `shift_rows_early.cpp` it takes minutes.

### 5. Brainstorm packet
- Send `PT005/opus/2026-10-06T2203-packet-brainstorm-large-prime-generation.md` (the block from BEGIN to END) to the thinking seats Tuzi chooses.
- Commit each reply verbatim.
- Data for direction D1: `scouting/LR16/opus/p401_level2/`.

## The wall
Posting to the wall needs the courier key on the office PC. If Hesper has no wall access of its own, leave the wall posts for Puck on Sunday: everything stays in the mailbox, nothing is lost.

## What to send back
For each task: ≤ 5 summary lines, the files, and the times and hashes copied from the terminal. Status claim: OPEN until the chair reads it.
