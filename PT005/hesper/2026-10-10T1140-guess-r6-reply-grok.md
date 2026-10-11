BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 08:10 +08
RE: 猜公式 Round 6 (packet 6f1e734), send text r6_send_grok.txt
SEAT: grok
MODEL: Grok Expert (selector), Worked for 1m 11s; v2 reply not yet collected
CHAT: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7

--- reply verbatim ---
ANSWER BLOCK

Q1: 7,8,9,11,13 frequent because they have low mutual overlap in too-near sets; 2,3,4,6 rare as multiples whose coverage is largely subsumed by smaller speeds; 12 never appears (max overlap from factors 2 and 3).

Q2: Odd core {1,3,5,7,9,11,13} leaves 45–74 cells uncovered; ~7 fillers typically complete a 14-cover when one exists. Form cover = u·(K ∪ fillers) with |K|≥5 holds for all 19 sampled covers.

Q3: For every p=4m+1 ≤499, speeds near m scale by 4 exactly to the odds 1..13. The family produces a 14-cover exactly on the 10 of those 15 primes that have covers>0 in the census.

Q4: Rule "p has a 14-cover iff some unit scaling yields ≥5 speeds from {1,5,7,8,9,11,13,14} completable by ≤9 fillers" gets 33/33 on Data 1 (true precisely on the 19 nonzeros).

Reasoning

FACT: Across the 23 (packet) / 46 (my enumeration) scalings of the 19 covers that put ≥5 speeds ≤15, the counts match the given table: 11 appears most, 12 appears zero times, 7/8/9/13 high, 2/3/4/6 low.

PROOF: Scaling by a unit preserves the cover property, so the small parts are equivalent representatives.

IDEA: The hint explains the pattern—speed 2v is too-near precisely when vt mod p is within p/32 of 0 or p/2—so even multiples share large fractions of their covered cells with half-speed, wasting the limited 14 slots. 12 = 4×3 compounds the waste; the frequent speeds are those whose too-near loci are comparatively independent.

FACT: For core K={1,3,5,7,9,11,13}, the number of uncovered cells on primes 307–499 grows roughly linearly from ~45 to ~74.

IDEA: Seven fillers of suitable size can cover that residual when a 14-cover exists; the sampled covers all admit at least one scaling with |small|≥5, supporting the "small core + magnifier + fillers" form.

FACT: Every p≡1 mod 4 in the range satisfies 4·(m−3 .. m+3) ≡ ±{1,3,5,7,9,11,13} mod p. Among those 15 primes the census has covers>0 on exactly 10, so the 457-style completion succeeds on precisely the nonzeros.

IDEA: The same holds for other k, but no uniform arithmetic condition on p selects exactly the nonzeros.

Least-sure step: whether a fixed core (odds or the frequent set) plus a bounded filler count yields a non-circular decision procedure that continues to match beyond 499. UNFINISHED: an independent structural test that also speaks to the Dirichlet exponent.

--- end verbatim ---
END LETTER
