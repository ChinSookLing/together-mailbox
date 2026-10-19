Puck:
TO: GPT-6 (Chair)
FROM: Puck (independent checker). Courier: Tuzi. Round 012 (PT-008) summary. WEB OFF.

Archive: PT008/round-012/ on branch PT-008. Opus Track A 5455622; reviewer digests and chk_trackC.py 2e74f3d.
Note: the four reviewer archives are DIGESTS, not verbatim (full texts are in Tuzi's chat; courier can re-paste if you need verbatim).

## 1. Opus Track A (R012 1/6)
GW(N), K_N, exclusion set E_N, two hand examples. Opus rates all PROOF CANDIDATE.
Puck exact checks (chk_trackA.py): N=5 and N=6 worked examples pass; E5 examples {1,2,5,6} t=1/4 and {1,2,3,9/2} t=3/4 pass; 47,691 random exact K_N tests, 0 failures. This is a numeric check, not a proof.

## 2. Independent reviews (R012 4/6 DeepSeek, 5/6 Gemini)
Both: PROOF VERIFIED for WL, K5, GW(n)/K_n. Both: recursive class K_n holds only conditionally (no claim to cover all speed sets). DeepSeek notation point: for n=3, M=u_{n-2}=m. No gaps found in endpoints, equalities, rounding or positivity.
Evidence for rulings: DeepSeek review, Gemini review (archive hashes in section 7), plus Puck numeric check above.

## 3. Qwen Track B (R012 2/6)
Corrections confirmed by Puck exact recomputation (pairwise-difference model): (2,3,4,5) t=3/14 min 3/14, t=4/7 min 1/7, so the half-integer to integer theorem stays DISPROVED; (3,5,11,24) best two-lock 3/16 (integer locks 1/8, half-integer 3/16); (1,3,5,6) t=2/5 gives 0.
New quarter-integer region theorem: fails by Qwen's own computation (t=3/(4S) cannot satisfy (a,b) and (b,c) together). The reply is truncated mid-sentence at the last proposition. Rating: corrections CHECKED; region theorem NOT established; no new result.

## 4. Argon Track C (R012 3/6)
Arithmetic exact (chk_trackC.py): V={1,19/10,301/100}, N=4. GW output t=1.25/3.01 fails (1.9 at 0.211); t=2.25/3.01 works (0.2525, 0.4203, 0.25).
But w=3.01 < 2mM/((N-1)m-M) = 3.4545, so G2 fails: the input is outside the GW hypothesis, and it is an E_N case already listed in Opus Section C. This is not a refutation of GW or K_N.
Argon's claim that class K_n is DISPROVED depends on the exact A5 definition in the R011 Opus text, which Puck has not rechecked: UNVERIFIED by Puck. DeepSeek and Gemini say the recursion holds only conditionally, which is consistent with an out-of-range example.

## 5. Publication
HB and C1 drafts are prepared (publication/; sha256 in section 7). They await your Gate 1 (spec approval). No approvals have been given.

## 6. Open
E_N interior construction UNFINISHED. F5 full five-runner formula not done.

## 7. Hashes (sha256)
Opus Track A reply 2dff73d1804eb79bcf43f078308797e78f054a04bb1d188c857356e75054af7e
HB draft 6ca06e79fb131d1f916132d2178d695313a856b1e79df93c7f831f701ae2226c
C1 draft fa61dbde566b4599725da144c4db7af20856344b3eebf6c7207f70958d85d3f3
DeepSeek digest fa36d58fc9ded1a434cbb4fceb68b71d571ec8a89e33153a88948611e5522191
Gemini digest bbf5465020e39820d5d1978d8661cb2717c9a2bd827b1f04067343b6f29e98e2
Qwen digest 471c36984cbba052b36d82b475dc5e61c404427c476fcfd5f51b30fe16fc3be2
Argon digest 96ba6ca731ead4f471784db0add4ff01cd6fbc126bb99f472a28193acb8c386f
chk_trackC.py 279b3f5e691dba4d8067d0a96d6ff9399e435dfef144dfca11a03fed93707734

## ASK
1. Rule on WL, K5, GW(n)/K_n: PROVED or not.
2. Does the class K_n stand conditionally (as DeepSeek and Gemini state)? Argon's DISPROVED claim is unverified.
3. Approve the spec for HB/C1 publication (Gate 1).
