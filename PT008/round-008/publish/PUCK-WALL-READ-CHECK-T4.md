# PT-008 · T4 wall read-check (Puck)

- Checked: 2026-10-18 ~19:08 +08 (Asia/Singapore), after Bill's report (Grok chat 680d7713, reply ~18:42-19:00 +08).
- Authorized text: PT008/round-008/publish/T4-PUBLICATION.md on branch PT-008, sha256 3bae49ad8bc9c49f8850e1c19567a581d8a97f146dfbc8118070a70c37256485.
- Gates: chair 7aa8daa (re-confirmed c976dc2) · Puck PASS FOR INSTALL 65e0264 · Hesper MATCH 4e64201.

## Plain text (curl https://play.civilisationfield.com/gathering/proof-table-008/table.txt)
- Downloaded file sha256 4128b75cbd41ec859832b80a546d04cd03220b4e2574765450b1bf7eb1fe99e4 (24184 bytes).
- Header: STATE_VERSION 6b9888a5 · AS_OF 2026-10-18T18:42:11+08:00 · STATUS open.
- Block between the lines "BEGIN T4" and "END T4" (lines 140-418) extracted byte-for-byte: 12198 characters, sha256 3bae49ad8bc9c49f8850e1c19567a581d8a97f146dfbc8118070a70c37256485 = authorized file. **EXACT MATCH** (unified diff: 0 lines).

## HTML (curl https://play.civilisationfield.com/gathering/proof-table-008/table)
- Downloaded file sha256 58e45b3e7b8fafd22d966fcbe09eb0b2b976c09abc1ae4a98353e138a7ecb019 (30512 bytes).
- The <pre> block containing T4, tags stripped and HTML entities unescaped: identical to the authorized file (string equality true, diff 0 lines).

## Other content
- Page status stays OPEN; AIM unchanged; ROUNDS "none posted"; LEDGER "none on this table". No round 009/010 records and no unreviewed proof candidate are on the page. Only T4 was added, as the chair cleared.
- The "STATUS: PROVED" line inside T4 is T4's own certification text (chair 7aa8daa), not a page status.

## Verdict
T4 publication on the PT-008 wall: **DONE, verified exact** (HTML and table.txt). No fix request to Bill needed.
