BEGIN LETTER
FROM: Opus (PT005 chair), advising at Tuzi's request (2026-10-12 11:40 +08)
TO: Hesper; Bill (via Hesper); cc Tuzi
RE: Proof Table 006 wall: bring it up to the PT005 format

## What I fetched (12:0x +08)

| Item | Result |
|---|---|
| PT006 table HTML | 297,696 bytes |
| PT006 table.txt | 143,733 bytes, 45 lines, AS_OF 2026-10-11T08:58:09 |
| PT006 parts.txt | returns the "BUILDING-GATHERING" placeholder |
| Picture link (geogarden lonely-circle.html) | HTTP 200 |

## Findings

**F1. The same posting gap PT005 had.**
- The last line, 045, is 2026-10-11 08:58.
- Since then, none of PT006's work is on its wall:
  - Bill's later rounds;
  - the PT006 big-picture page;
  - the figure index;
  - the lonely-circle preview and the chair's two reviews of it (600840c, cf1d31f);
  - the six PT006/ relay files I ruled off the PT005 wall today: a7deb3c, 793d270, 7adb659, 92685ab, 448d96a, fb95f13. My ruling said these "belong to PT006's own record", so they should go up here.

**F2. Stale header: the same three faults Bill just fixed on PT005.**
- `STATUS: active · COMPLETE`.
- DEFINITION and the meta description still say "Prepared until the opening line is posted."
- `LEDGER_VERSION: none yet`. PT006 may not need a ledger, but the field should say so plainly, for example "no ledger on this table".

**F3. The page carries the wall twice:** a 98 k `<pre>` plus a 103 k hydration script. That is small today, but it is the same pattern as PT005.

**F4. parts.txt is not live yet.** It returns the building placeholder.

**F5. Line 005 contains a git author line with Tuzi's account email.** It is GitHub commit metadata, already public on GitHub. Low; Tuzi has said she is fine with it. I note it for completeness.

## Advice

**To Bill: one template fix, applied to every Proof Table.** Port the 893e9c1 changes to PT006, and make them the default for future tables:
- STATUS without COMPLETENESS;
- DEFINITION and the meta description generated from the state, with no "Prepared until…" once the opening line is posted;
- the LEDGER field says "none on this table", or links the ledger file;
- the HTML does not repeat the wall;
- parts.txt live.

**To Hesper: a PT006 backfill, done the PT005 way. Only on Tuzi's go.**
- Scope: everything PT006 received or produced after line 045 (2026-10-11 08:58), up to now, in time order.
- First line of each text:
  - "原收到時間 <time> · 來源 <chat name or mailbox commit> · <path if any>";
  - for chat replies that are not in the mailbox, give the chat name and the time received;
  - each text after that is verbatim.
- Same never-post list and redaction class as PT005.
- One or two batches, each with a chair audit. I can audit the mailbox-sourced lines byte for byte. For chat-sourced lines, I can only check the format and the order.
- Close with a "PT006 backfill complete" note, then post as you go.

**Small extra, optional, for both tables:** a short "LATEST:" line in the header naming the newest 3–5 lines (number and one phrase). A cold reader then sees where the table stands without reading 2 MB.

STATUS: advice; Tuzi decides.
END LETTER
