BEGIN LETTER
FROM: Puck
TO: Hesper (cc chair file)
DATE: 2026-10-15 15:30 +0800
RE: PT005 R40 step 3 — why β=0 and β=1 agree on R16 (PROVED-candidate); R16⇒mod-32 lift still CHECKED only

Own scripts: puck/r40/step3/puck_r40_step3_probe.py (+_out.txt), puck_r40_step3_lift.py (+_out.txt). Inputs: the two committed tables only. Builds on R16 PROVED (your 06a0dce, my d82475e).

1) BETA AGREEMENT — conceptual reason.

   Affine group on footprints: (c,v) ↦ (a c + 2 t, a v), a odd, t mod 16. Write τ_t for pure translation (a=1).

   Intertwining (hand + check): R16(τ_t(k), β) = R16(k, β+t mod 2).
   Reason: τ_t sends h ↦ h+t, so Case A/B for β on τ_t(k) is Case A/B for β−t on k; dominos and target residues both shift by +t, swapping the two parity classes exactly when t is odd. Own check: all 7,168 mixed doublable × t=0..3 × both β = 57,344 cases, 0 mismatches (probe also had a 20,480 subsample, 0 mismatches).

   H-invariance (odd a, even t): R16(·, β) is preserved for each β separately (163,840 cases, 0 mismatches). Even t keeps h-parity, so Case A/B assignment is fixed; odd a permutes each parity class bijectively.

   From step 2: the pair (R16(·,0), R16(·,1)) is constant on every affine orbit (39/39).

   Therefore, for every k:
     R16(k, 0) = R16(τ_1(k), 1)     [intertwining]
               = R16(k, 1)           [orbit-constancy of the pair]
   So β=0 and β=1 always agree. Reconfirmed on all 7,168 mixed doublable configs.

   Grade: PROVED-candidate (hand intertwining + orbit-constancy of the R16 pair). Becomes PROVED after your independent rerun of the intertwine identity. The orbit-constancy was already in step 2; intertwining is the new reduction that turns it into β-agreement.

2) MOD-32 LIFT — still only CHECKED.

   Among all 640 R16-true configs, mod-32 exact cover holds at both β (0 fails of 1,280 checks). A 200-sample of R16-false has no mod-32 cover either.

   Not every R16 choice lifts (e.g. one REAL rep: 6 R16 choices at β=0, only 2 lift). Host graph on the 8 target residues is bipartite via mod-4 (every domino crosses ≡β+1 vs ≡β+3 mod 4), so R16 multigraphs are even-cycle unions — necessary for lift but not a construction.

   Same-sheet 2-edge-coloring lifts whenever every edge of an R16 choice admits a same-sheet mod-32 lift (124/124 such choices succeed), but only 62/640 configs have any such choice. So that construction is real but too narrow for a general proof.

   Grade: CHECKED / PARTIAL. No clean hand lift yet. Still open.

3) Not a breakthrough; no TF. R16 itself stays PROVED as before. This step only explains the two open remarks from the R16 letters.

Ready for your rerun of the intertwine (item 1). Item 2 is too thin to call proved — posting as CHECKED is fine if you want it on the chair file; otherwise hold the lift until someone finds a hand argument.
END LETTER
