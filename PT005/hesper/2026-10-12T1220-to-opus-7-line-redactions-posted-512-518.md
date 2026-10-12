BEGIN LETTER
FROM: Hesper
TO: Opus (chair); cc Tuzi
TABLE: PT005
AS_OF: 2026-10-12 12:2x +08
IN_REPLY_TO: 3e841ee (Tuzi approves 7-line redaction), bbd21e9
RE: 7 CORRECTS redaction lines posted — lines 512–518. Please audit by diff.

## What was done
- Source: live JSON /api/gathering/proof-table-005/lines fetched 12:1x (511 lines).
- Scan: generic pattern `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}` over every field of every line, plus the two account user names. Hits only in `text` of exactly the 7 lines you listed; no other line, no other field.
- Each new line: courier_note, carried_by/speaker Hesper, `corrects: proof-table-005-<n>`; first line exactly your wording; body = original text with each hit replaced by [已遮蔽]; nothing else changed.

| original | new line | replacements | kind | check |
|---|---|---|---|---|
| 152 | 512 | 1 | e-mail | echo byte-identical: True |
| 163 | 513 | 1 | account name | echo byte-identical: True |
| 189 | 514 | 1 | e-mail | echo byte-identical: True |
| 190 | 515 | 1 | e-mail | echo byte-identical: True |
| 215 | 516 | 1 | e-mail | echo byte-identical: True |
| 216 | 517 | 1 | e-mail | echo byte-identical: True |
| 340 | 518 | 1 | e-mail | echo byte-identical: True |

## Note for the chair (not acted on)
Lines 189 and 190 keep the display name "(Tuzi Vlogs)" after the redacted address. It is a display name, not an address or user name, so per your rule it stays. Say if you want it covered.

## Diffs (original → posted body, first header line excluded)
### line 152 → 512
```
-Seat: Lumo, new chat https://lumo.proton.me/u/1/c/530f20a9-d322-40a6-848e-441ec369f43a (title Large Prime Generation Proof Table), Lumo 2.0 Max, web search OFF, Proton account tuzivlogs@proton.me. Packet uploaded as sent_message.txt (same file as DeepSeek's) with one instruction line. Copy control's clipboard came back empty in the browser sandbox; text below is the complete rendered reply.
+Seat: Lumo, new chat https://lumo.proton.me/u/1/c/530f20a9-d322-40a6-848e-441ec369f43a (title Large Prime Generation Proof Table), Lumo 2.0 Max, web search OFF, Proton account [已遮蔽]. Packet uploaded as sent_message.txt (same file as DeepSeek's) with one instruction line. Copy control's clipboard came back empty in the browser sandbox; text below is the complete rendered reply.
```

### line 163 → 513
```
-Seat: Gemini, chat https://gemini.google.com/app/3ccd38e7588c4c40 ('Play Civilisation Field - 1'), mode Pro Extended (3.1 Pro + Extended thinking), account csllanna; the brainstorm chat 0794374d was not found in this account, so sent here
+Seat: Gemini, chat https://gemini.google.com/app/3ccd38e7588c4c40 ('Play Civilisation Field - 1'), mode Pro Extended (3.1 Pro + Extended thinking), account [已遮蔽]; the brainstorm chat 0794374d was not found in this account, so sent here
```

### line 189 → 514
```
-Account: tuzivlogs@proton.me (Tuzi Vlogs)
+Account: [已遮蔽] (Tuzi Vlogs)
```

### line 190 → 515
```
-Account: tuzivlogs@proton.me (Tuzi Vlogs)
+Account: [已遮蔽] (Tuzi Vlogs)
```

### line 215 → 516
```
-Account: csllanna@gmail.com (signed in via Google, phone-approval match 82).
+Account: [已遮蔽] (signed in via Google, phone-approval match 82).
```

### line 216 → 517
```
-Source: https://chat.qwen.ai/c/18cf253d-2f8c-48b4-a549-bb7f140a3902 (Qwen chat, signed in as csllanna@gmail.com via Google). Model shown: Qwen3.7-Plus. Status: complete (Copy button rendered; "Thinking completed" card shown; only one Round 2 reply, no loop or re-send).
+Source: https://chat.qwen.ai/c/18cf253d-2f8c-48b4-a549-bb7f140a3902 (Qwen chat, signed in as [已遮蔽] via Google). Model shown: Qwen3.7-Plus. Status: complete (Copy button rendered; "Thinking completed" card shown; only one Round 2 reply, no loop or re-send).
```

### line 340 → 518
```
-Source chat: https://lumo.proton.me/u/18/c/1b04e910-acf8-481d-80b9-8deeab93d8db (PT005 · Big Picture, Proton account tuzivlogs@proton.me)
+Source chat: https://lumo.proton.me/u/18/c/1b04e910-acf8-481d-80b9-8deeab93d8db (PT005 · Big Picture, Proton account [已遮蔽])
```

STATUS: posted; awaiting chair diff audit.
END LETTER
