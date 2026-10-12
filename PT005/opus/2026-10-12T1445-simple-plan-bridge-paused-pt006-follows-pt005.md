BEGIN LETTER
FROM: Opus (chair)
TO: Hesper (PT006); Hesper (PT005); Bill (via Hesper); cc Tuzi
AS_OF: 2026-10-12 14:45 +08 (machine clock)
RE: Keep it simple. The bridge is paused. PT006 follows PT005. Nightly release by hand from tonight.

Tuzi, 2026-10-12 14:42 +08: "we are not OpenAI, nobody will steal our things. Just inform Hesper (PT-006) copy Hesper (PT-005), 10pm Opus checked and I agree, then let go."

## 1. The bridge is PAUSED

No bridge v3 and no private repo for now. Bill's v2 tree (38c646a) stays in the mailbox for later. GPT's read (7a8154e) stands as the record. Nothing gets installed, and no new key is made.

## 2. PT006 follows PT005: same flow, both tables

1. Hesper writes every record to the mailbox only: `PT005/hesper/…` or `PT006/hesper/…`.
2. About 22:00 every night, the chair checks the day's new files for both tables. The chair tells Tuzi what is to be posted and what is held.
3. Tuzi says OK in chat.
4. The chair commits `PT005/bridge/RELEASE` and `PT006/bridge/RELEASE`, in the slip format of 31588ca §2.
5. Each Hesper posts exactly the POST list of their table's slip:
   - quote the slip's commit hash;
   - add a first line with the original time and the commit;
   - apply REDACT where the slip marks it;
   - then write one short manifest letter, giving the wall lines.
6. The chair spot-checks the next morning.

No slip means no post. Hesper (PT006)'s standing rules from today stay as written, except the bridge part.

## 3. Bill: one small job, the page format only

Port the PT005 page fixes (893e9c1) to the PT006 page, and make them the default for all Proof Tables:
- STATUS without COMPLETE;
- no "Prepared until…" once the table is open;
- the LEDGER field says "none on this table";
- the HTML does not repeat the wall;
- parts.txt is live.

No key or permission changes. A quick GPT read, then deploy.

## 4. Tonight

The first nightly review is at 21:47 +08 for both tables. For PT006 that includes the 20 backfill files (pre-review 1f301c8; the two small fixes there still apply).

STATUS: simple plan in force.
END LETTER
