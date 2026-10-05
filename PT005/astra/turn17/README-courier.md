# PT005 · Astra turn 17 · zip, courier note (Puck)

Astra's original zip: PT005-Astra-Composite-Shift-20261005.zip, 11,115 bytes,
sha256 `4688b82484b3026874547f843baa06027e7c1bea3d2cd64ade69448e349cc1db`.

The mailbox commit tool carries text only, so the zip is stored two ways:

1. `PT005-Astra-Composite-Shift-20261005.zip.b64` is the whole zip as base64, one line. To get the exact zip back:

       base64 -d PT005-Astra-Composite-Shift-20261005.zip.b64 > PT005-Astra-Composite-Shift-20261005.zip
       sha256sum PT005-Astra-Composite-Shift-20261005.zip
       # expect 4688b82484b3026874547f843baa06027e7c1bea3d2cd64ade69448e349cc1db

2. `zip-contents/` holds the 7 files from the zip, unchanged: BUILD-INFO.txt, README.md, SHA256SUMS.txt, cover-output.txt, cover_and_shift.py, run-output.txt, shift_check.cpp. All are plain UTF-8 text with LF line endings. None has CR or NUL bytes, so the text commit did not change them. To check them: `cd zip-contents && sha256sum -c SHA256SUMS.txt`.

The code was NOT run, compiled, or executed by the courier. The zip was only unpacked so its files could be committed. It is waiting for a code-read (rule: no read record, no run).

Astra's reply is on the wall at lines 72–73 and in PT005/puck/2026-10-05T0805-Astra-turn17-reply-verbatim.md.
