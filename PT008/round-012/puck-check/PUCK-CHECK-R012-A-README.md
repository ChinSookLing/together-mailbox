# PT-008 R012 · Puck exact check of Opus Track A (GW(N), K_N) — see opus-reply/PT-008-R012-OPUS-TrackA.md
Script: chk_trackA.py (exact Fractions, round(X)=floor(X+1/2)). Output: chk_trackA_output.txt.
- Worked example N=5, U={1,3/2,5/2,23/5}: t=6/23 (shift branch), all distances >= 1/5. PASS.
- Worked example N=6, U={1,2,3,7/2,31/4}: t=1/6 (t_L branch), all >= 1/6. PASS.
- E5 examples (outside the construction): {1,2,5,6} at t=1/4 and {1,2,3,9/2} at t=3/4, distances 1/4,1/2,1/4,1/2 and 1/4,1/2,1/4,3/8. PASS.
- 47,691 random exact K_N cases (N=3..9, M<=(N-1)^2 m/(N+1), w>M arbitrary): 0 failures.
Status: check of the author examples and K_N statement. Not a grade; GW(N)/K_N stay PROOF CANDIDATE.
