#!/bin/sh
# Failure-injection and restart tests for km1census.py v2. usage: sh test_km1census.sh /path/to/bgk15
# Expected: four STOP lines with exit=2; then 191 -> 42114 and 223 -> 33694; after a truncated JSONL line and a
# tampered 223 file, 191 is skipped and 223 recomputed; on the next restart both are skipped (verified).
set -u; S=$(cd "$(dirname "$0")" && pwd)/km1census.py; B=$1; T=$(mktemp -d); cd "$T"; mkdir fake
printf '#!/bin/sh\necho oops >&2; exit 3\n' > fake/f1
printf '#!/bin/sh\nif [ "$2" = km1roots ]; then echo "bt=1 roots=1"; echo "0 5"; exit 0; fi\nprintf "aa\\n" > "$4"; echo "root=0 canonical14=2"; exit 0\n' > fake/f2
printf '#!/bin/sh\nif [ "$2" = km1roots ]; then echo "bt=1 roots=1"; echo "0 5"; exit 0; fi\necho "root=0 canonical14=5"; exit 0\n' > fake/f3
printf '#!/bin/sh\necho "bt=1 roots=2"; echo "0 5"; exit 0\n' > fake/f4
chmod +x fake/*
for f in f1 f2 f3 f4; do python3 "$S" fake/$f 2 o_$f 191; echo "exit=$?"; done
python3 "$S" "$B" 2 real 191 223
python3 -c "p='real/census14.jsonl'; s=open(p).read(); open(p,'w').write(s[:-20]); open('real/km1_223_dedup.txt','a').write('zz\n')"
python3 "$S" "$B" 2 real 191 223
python3 "$S" "$B" 2 real 191 223
echo "test dir: $T"
