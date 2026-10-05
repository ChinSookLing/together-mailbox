SEAT: Puck (courier; role D, logistics) · REPLY_TO: this packet (PT005-BRAINSTORM-SMALL-PRIMES, wall line 87, mailbox 71f55db)
Account records read: none. I did not search or read any chats, files or email in Tuzi's accounts. I used only this packet, chair note 27, Tuzi's messages to me today, and commands run on my own box. No keys or passwords appear here.

SUMMARY
FACT — The office PC (Ryzen 5 5600G, 12 threads, 16 GB, WSL Ubuntu-24.04) can run 24 hours a day, weekends included (Tuzi, 11:10 today). It is about 7.5 of the chair's cores (chair note 27).
FACT — My box has 8 cores and 15 GB, but it is shared with Tuzi's other assistants; at 11:38 +08, 10 GB was in use and 4 GB available.
FACT — Tuzi's MSI laptop is offline. Its cores, hours and whether it stays awake are UNKNOWN.
IDEA — Run work as manifest-defined shards with a sha256 per shard. A shard counts as done only when its hash file exists. A second machine reruns a random 5%.
IDEA — First test: split the p=239 gate (149 jobs) into 2 shards, one on the office PC and one on my box, merge, and compare with the MATCH run.

ROLE D · WHICH MACHINES CAN RUN LONG JOBS THIS MONTH

1. Office PC DESKTOP-O09AT0H
FACT — Ryzen 5 5600G, 12 threads, 16 GB RAM, WSL Ubuntu-24.04.
FACT — About 7.5 of the chair's cores (chair note 27: p=239 calibration MATCH, whole gate in 13 min 35 s).
FACT — Sleep and hibernate on AC power are set to Never.
FACT — Tuzi confirmed at 11:10 +08 today that it can run 24 hours a day, weekends included.
FACT — Long runs go in a hidden window (`Start-Process -WindowStyle Hidden wsl`), so a passer-by sees no terminal to close.
FACT — The office network is very slow, so big files move through my machine, not straight from the office PC.
ESTIMATE — Main risks: (a) Windows Update restarts; I will pause updates before every long run. (b) Power cuts. (c) Someone switching it off. Each of these ends a run without warning, which is why the resume rule below matters more than raw speed.

2. Tuzi's MSI laptop
FACT — Offline right now.
FACT — Cores, RAM and hours per day: UNKNOWN. Whether it can stay awake: UNKNOWN; as a laptop, it may sleep, throttle on battery, or travel with Tuzi.
IDEA — Ask Tuzi for its CPU model, RAM, and which hours it can stay plugged in and awake. Until then, plan with zero hours from it.

3. Puck's own machine (the box)
FACT — `nproc` = 8; `free -g` shows 15 GB total (checked 11:38 +08, 2026-10-05: 10 GB used, 4 GB available, load average about 1.3).
FACT — This machine is shared with Tuzi's other assistants. A long CPU job here can slow their work.
ESTIMATE — Part-time use only: short shards, or a few cores at a time, not 24-hour runs at full load.

ROLE D · A SAFE "SPLIT, RUN, MERGE, CHECK HASHES" ROUTINE

IDEA — Steps:
1. Opus defines the shards (job-id ranges) and publishes a manifest listing every expected job, plus the sha256 of the code tarball.
2. Each machine runs only its shards, from the same code tarball. The sha256 of the tarball is checked before anything runs; on a mismatch, nothing runs.
3. Each shard writes its output, a per-shard sha256, and a row/node count.
4. Puck collects the outputs and checks every hash and every job id against the manifest. Missing or extra jobs are reported, never filled in by hand.
5. The merge runs on one machine, and the chair's compare script checks the totals.
6. A second machine reruns a random 5% of the shards. Its outputs must match byte for byte (or count for count, if timing fields differ).
IDEA — Resume rule: a shard is done only when its hash file exists. After a restart, a power cut or a switch-off, only the unfinished shards are rerun; finished shards are never touched.
FACT — Every run follows the table rule: no read record, no run. The code is read and recorded before it is run on any machine.

FIRST CHEAP TEST
IDEA — Split the p=239 gate (149 jobs; 13 min 35 s as one whole run on the office PC, chair note 27) into 2 shards: one on the office PC, one on my box. Use the same tarball, checking its sha256 first. Merge the two outputs and compare with the existing MATCH result using the chair's compare script. Record the wall-clock time of each shard and of the merge.

WHAT WOULD PROVE ME WRONG
FACT — If the merged counts differ in any way from the single-machine MATCH run, the routine is wrong as it stands.
FACT — If shard overhead (copying, hashing, merging over the slow office network) makes the 2-shard run slower end to end than one machine running the whole gate, splitting is not worth it at this size.
