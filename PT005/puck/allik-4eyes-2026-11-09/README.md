Puck four-eyes of chair note 133 (2026-11-09 09:39 +08).
- puck_allik4eyes.py: written from scratch; did not read or run the chair's cmp_allik.py. It reads the 16 evidence15_<p>_s0.tgz archives as tar streams (no extraction), parses rows_ir/*.txt.log, rows_ir/*.txt and filt/*.stats with its own regexes, checks his MANIFEST_SHA256.json against the archive bytes, checks the SUMMARY totals, and compares each (r,s) with our ir.jsonl (strict JSON; duplicate (r,s) lines would be reported, none found).
- Run: python3 puck_allik4eyes.py <dir with evidence15_*.tgz> inputs.tsv result.json
- K11 inputs for 383/397/431/443/491/499/503/509 come from the k11-gate branch `results` at commit 2890912 ("k11 checkpoint 42541770750"); those files are not in the mailbox. The paths in inputs.tsv for these are local copies made with `git show`.
- I downloaded the archives from Zenodo record 23304361 myself. They are not committed; their hashes are in evidence_archives_sha256_puck.txt.
