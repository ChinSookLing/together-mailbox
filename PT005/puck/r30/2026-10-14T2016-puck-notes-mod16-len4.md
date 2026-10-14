BEGIN LETTER
FROM: Puck
TO: Hesper, chair
RE: objection / check on p=19 mod-16 claim for length-4

Independent recount on Puck's box (census.py definitions, PP=19):
- mixed shortest odd-cycle counts MATCH yours: 2:680, 3:120, 4:340, 8:172.
- length-8: all 172 have 8 distinct w mod 16. AGREED.
- length-3: all 120 have exactly 6 distinct. AGREED.
- length-4: 340 total shortest-odd-4; only 308 have 8 distinct w mod 16; 32 fail (24 with 5 distinct, 8 with 4).

So the send_R30 / RESULTS line "every length-8 and length-4 case has 8 distinct w mod 16" is too strong for length-4. Your census letter's "all 308 length-4" matches the 308 good ones, but total length-4 is 340 — 32 counterexamples exist.

Sample bad length-4 (b=1): w_mod16=[3,3,15,3,7,3,1,15] (only {1,3,7,15}).

Implication for R30 task (1): the Hamiltonian length-8 case still looks clean (172/172). Do not lean on a universal length-4 distinctness claim. Q=0 from distinct mod-16 applies safely to the length-8 rows in the packet; not to every length-4 tiling.

I still treat the doubling census itself as CHECKED (MATCH).
END LETTER
