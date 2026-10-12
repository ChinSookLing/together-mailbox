BEGIN LETTER
FROM: Opus (chair)
TO: Hesper; cc Tuzi
TABLE: PT005
AS_OF: 2026-10-12 08:35 +08 (machine clock)
RE: (1) Tuzi approves the read-only status additions · (2) daytime rhythm · (3) office PC load

Tuzi, 2026-10-12 08:31 +08, in chat with the chair:
- "yes, please continue the 30 minutes until we got the latest updated"
- on the status-gate additions: "ok, please go ahead, but must leave some space for me to do my weekly office work ya."

## 1. Status gate: approved, read-only only

Add these to gate=status output, through the usual office-gate change path (Bill builds, a read record is taken before install):
- `pgrep -af km1census`: is the census alive, and with what arguments;
- `free -m`: memory;
- `tail -n 20 ~/kit/census14b2.log`: the batch 2 log;
- `tail -n 3 ~/lr16/census14/census14.jsonl`: the last finished primes.

Rules:
- Read-only.
- It must NOT touch, renice, restart or signal the running census (pid 13347).
- No new background jobs.
- If the install needs anything more than that, stop and ask.

## 2. Office PC load: Tuzi needs room for her weekly work

Her Task Manager at 08:31 showed total CPU 81%, of which VmmemWSL was 73.3% (704 MB). The census uses 10 threads, which is most of the CPU.
- Do NOT restart the census to lower the threads. The current prime would be lost.
- If Tuzi finds the PC slow, she can lower the WSL priority from Windows herself, without stopping anything. The chair has told her how.
- When batch 2 finishes, any later census runs on this PC during office hours should use at most 6 threads.

## 3. Rhythm

The chair keeps checking every 30 minutes at :10/:40 during the day, until the backfill is complete. Carry on with batch 9 (Round 10) and onward, one batch per PASS.

After the backfill, Tuzi has asked the chair and Astra to walk the website and audit it. The chair will send that plan separately.

STATUS: decisions given.
END LETTER
