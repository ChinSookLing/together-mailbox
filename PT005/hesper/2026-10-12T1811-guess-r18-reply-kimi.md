BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 18:12 +08
RE: 猜公式 Round 18 make the gate cheap (packet ab3ea04), send text r18_send_kimi.txt
SEAT: kimi
MODEL: Kimi K3 Thinking High (Tuzi relay of finished reply)
CHAT: https://www.kimi.ai/chat/1a1155fd-dfb2-86ed-8000-09ce73efa9f3

--- reply verbatim ---
[Relay note: Kimi K3 High finished its Round 18 reply in chat www.kimi.ai/chat/1a1155fd-dfb2-86ed-8000-09ce73efa9f3 (sent ≈17:14 +08). Tuzi copied it from her side and pasted it into Hesper's chat at 2026-10-12 18:11 +08. Text below is exactly as Tuzi pasted it. Supersedes the partial record 3e7cc49.]

## ANSWER BLOCK

**FACT:** I propose making **W4 proactive**: before computing gains or branching, delete every candidate class that would exhaust the remaining private-time pool of an already selected class.

**PROOF:** For selected class \(a\), let \(P_a=S_a\setminus\bigcup_{b\ne a}S_b\) over currently selected \(b\). Future choices can only add coverage, so a time outside \(P_a\) can never become private to \(a\). If a candidate covers all of \(P_a\), selecting it leaves \(a\) without any possible private time; therefore no irredundant completion is lost by deleting that candidate.

**FACT:** In my own bitset reproduction, normalizing every row to contain class 1, W4 reduced nodes from 8,563,521 to 4,353,814 at p=83, from 79,380,440 to 38,290,525 at p=101, and from 97,867,203 to 49,320,090 at p=103. The respective row counts—595,035, 12,056,514, and 18,073,015—and sorted row-hash multisets were unchanged.

**FACT:** Adding the pairwise excess-conflict cut below reduced the p=101 and p=103 node counts further, to 37,223,266 and 46,912,915, again with identical row-hash multisets.

**IDEA:** Expected speed-up on the author’s production engine at the real gate primes: **UNFINISHED**, because I did not run that engine.

---

## Q1 · Proactive W4 cut

### Rule

**FACT:** At a partial node with selected classes \(C\), define for each \(a\in C\)

\[
P_a=S_a\setminus\bigcup_{b\in C\setminus\{a\}}S_b.
\]

For every unselected candidate \(x\):

\[
\boxed{\text{If }P_a\subseteq S_x\text{ for any }a\in C,\text{ reject }x.}
\]

Do this **before** the rarest-time branch, not only after tentatively selecting \(x\).

### Soundness

**PROOF:**  
1. \(P_a\) is exactly the set of times currently private to \(a\) among selected classes.  
2. A time not in \(P_a\) either is not covered by \(a\) or is already covered by another selected class.  
3. Later selections never remove coverage, so no time outside \(P_a\) can later become private to \(a\).  
4. If \(x\) covers every point of \(P_a\), then after selecting \(x\), every time covered by \(a\) is covered by at least one other selected class.  
5. Hence \(a\) can never have a private time, and no completion containing \(x\) is irredundant.  
6. Therefore deleting \(x\) cannot delete an irredundant cover.

---

## Optional second cut: pairwise excess conflicts

**FACT:** Let \(U\) be the uncovered times, \(r\) the remaining slots, and \(G_i=S_i\cap U\), \(g_i=|G_i|\). For candidates \(i,j\), let \(T_{ij}\) be the sum of the largest \(r-2\) gains among the other candidates.

Reject the pair \(\{i,j\}\) as incompatible when

\[
\boxed{g_i+g_j+T_{ij}-|G_i\cap G_j|<|U|.}
\]

**PROOF:** For any \(r\)-class completion containing \(i,j\),

\[
\begin{aligned}
\left|\bigcup_{q\in R}G_q\right|
&\le |G_i\cup G_j|+\sum_{q\in R\setminus\{i,j\}}|G_q|\\
&=g_i+g_j-|G_i\cap G_j|
  +\sum_{q\in R\setminus\{i,j\}}g_q\\
&\le g_i+g_j+T_{ij}-|G_i\cap G_j|.
\end{aligned}
\]

If the right side is below \(|U|\), no such completion can cover \(U\). Thus, after branching on \(i\), every \(j\) conflicting with \(i\) may be removed from that branch.

**IDEA:** I used this only for \(2\le r\le4\), where the dead-branch profile says the search is close enough to the leaves to make pair tests cheap.

---

## Own calculation: test harness

**FACT:** This is the stripped harness used for the W4 measurements. It fixes class 1 by unit dilation; both modes use the same normalization, so the comparison tests the cut, not symmetry removal.

```cpp
#include <bits/stdc++.h>
using namespace std;
using u64=unsigned long long;
int p,n,m,mode; const int K=15;
vector<u64> S; vector<int> chosen;
long long nodes=0, complete=0, rowCount=0, filtered=0;
FILE *out;

u64 rowHash() {
    vector<int> a=chosen; sort(a.begin(),a.end());
    u64 h=1469598103934665603ULL;
    for(int x:a) for(int y=x+1;y;y/=251) {
        h ^= (unsigned)(y%251);
        h *= 1099511628211ULL;
    }
    return h;
}

void dfs(u64 allowed,u64 covered) {
    nodes++;
    u64 FULL=(1ULL<<n)-1, U=~covered&FULL;
    int rem=K-(int)chosen.size();

    if(!U) {
        complete++;
        if(chosen.size()==K) {
            bool ok=1;
            for(int a:chosen) {
                u64 o=0;
                for(int b:chosen) if(a!=b) o|=S[b];
                if(!(S[a]&~o)) {ok=0;break;}
            }
            if(ok) {
                rowCount++;
                fprintf(out,"%016llx\n",(unsigned long long)rowHash());
            }
        }
        return;
    }
    if(!rem) return;

    vector<u64> priv;
    for(int a:chosen) {
        u64 o=0;
        for(int b:chosen) if(a!=b) o|=S[b];
        u64 pa=S[a]&~o;
        if(!pa) return;
        priv.push_back(pa);
    }

    if(mode) {                 // proactive W4
        u64 keep=0;
        for(u64 A=allowed;A;) {
            int v=__builtin_ctzll(A); A&=A-1;
            bool bad=0;
            for(u64 pa:priv)
                if((pa&~S[v])==0) {bad=1;break;}
            if(bad) filtered++;
            else keep|=1ULL<<v;
        }
        allowed=keep;
    }

    vector<int> gains;
    for(u64 A=allowed;A;) {
        int v=__builtin_ctzll(A); A&=A-1;
        int g=__builtin_popcountll(S[v]&U);
        if(g) gains.push_back(g);
    }
    sort(gains.rbegin(),gains.rend());
    long long cap=0;
    for(int i=0;i<rem&&i<(int)gains.size();i++) cap+=gains[i];
    if(cap<__builtin_popcountll(U)) return;

    int bt=-1,bc=INT_MAX;
    for(u64 X=U;X;) {
        int t=__builtin_ctzll(X); X&=X-1;
        int c=0;
        for(u64 A=allowed;A;) {
            int v=__builtin_ctzll(A); A&=A-1;
            if(S[v]>>t&1) c++;
        }
        if(c<bc) {bc=c;bt=t;}
    }
    if(!bc) return;

    for(u64 A=allowed;A;) {
        int v=__builtin_ctzll(A); A&=A-1;
        if(!(S[v]>>bt&1)) continue;
        allowed&=~(1ULL<<v);
        chosen.push_back(v);
        dfs(allowed,covered|S[v]);
        chosen.pop_back();
    }
}

int main(int argc,char**argv) {
    p=atoi(argv[1]); mode=atoi(argv[2]); out=fopen(argv[3],"w");
    n=(p-1)/2; m=(p-1)/16; S.assign(n,0);
    for(int v=0;v<n;v++) for(int t=1;t<=n;t++) {
        int r=(int)((long long)(v+1)*t%p);
        r=min(r,p-r);
        if(16*r<p) S[v]|=1ULL<<(t-1);
    }
    for(int v=0;v<n;v++) assert(__builtin_popcountll(S[v])==m);

    chosen.push_back(0);
    dfs(((1ULL<<n)-1)&~1ULL,S[0]);
    fclose(out);
    fprintf(stderr,
      "p=%d mode=%d nodes=%lld complete=%lld rows=%lld filtered=%lld\n",
      p,mode,nodes,complete,rowCount,filtered);
}
```

**FACT:** Commands used:

```bash
g++ -O3 -std=c++17 repro_w4.cpp -o repro_w4

./repro_w4 83 0 h83.base
./repro_w4 83 1 h83.w4
./repro_w4 101 0 h101.base
./repro_w4 101 1 h101.w4
./repro_w4 103 0 h103.base
./repro_w4 103 1 h103.w4

sort h83.base > h83.base.s
sort h83.w4   > h83.w4.s
sha256sum h83.base.s h83.w4.s
# similarly for 101 and 103
```

### Results

**FACT:** W4 measurements:

| p | baseline nodes | W4 nodes | nodes cut | node ratio | rows | row-hash multiset |
|---:|---:|---:|---:|---:|---:|---|
| 83 | 8,563,521 | 4,353,814 | 4,209,707 | 1.966901× | 595,035 | identical |
| 101 | 79,380,440 | 38,290,525 | 41,089,915 | 2.073109× | 12,056,514 | identical |
| 103 | 97,867,203 | 49,320,090 | 48,547,113 | 1.984327× | 18,073,015 | identical |

**FACT:** Sorted 64-bit row-hash multisets, followed by SHA-256:

```text
p=83:
d2d37789e8de0aa37827039dd9516e9a83dafe77e5355352e02633822a5de0eb
d2d37789e8de0aa37827039dd9516e9a83dafe77e5355352e02633822a5de0eb

p=101:
3a3205559c8285d8fc6fbb1d5f9ec6e07100077421651ce57eab7ea2931e4317
3a3205559c8285d8fc6fbb1d5f9ec6e07100077421651ce57eab7ea2931e4317

p=103:
a729c450b18fb33a0b6c1d8ef5e4fb3d806666202d4e76b18b6644a678f24c26
a729c450b18fb33a0b6c1d8ef5e4fb3d806666202d4e76b18b6644a678f24c26
```

**FACT:** The ratios were calculated from the displayed integers with:

```python
for B,N in [(8563521,4353814),
            (79380440,38290525),
            (97867203,49320090)]:
    print((B-N)/B*100, B/N)
```

Output:

```text
49.15859959939375 1.9669009746397068
51.76327442881396 2.0731092091320242
49.605088846771274 1.9843273400352677
```

---

## Pair-conflict implementation and result

**FACT:** I inserted this after W4 filtering and before rarest-time branching. The important implementation detail is that conflict removal is branch-local: it must not mutate the parent’s candidate set for later siblings.

```cpp
vector<int> cand;
vector<u64> G;
for(u64 A=allowed;A;) {
    int v=__builtin_ctzll(A); A&=A-1;
    u64 gi=S[v]&U;
    if(gi) {cand.push_back(v); G.push_back(gi);}
}
int c=cand.size(), unc=__builtin_popcountll(U);

vector<u64> conflict(c,0);
if(2<=rem && rem<=4) {
    vector<int> g(c), ord(c);
    for(int i=0;i<c;i++) g[i]=__builtin_popcountll(G[i]);
    iota(ord.begin(),ord.end(),0);
    sort(ord.begin(),ord.end(),
         [&](int a,int b){return g[a]>g[b];});

    for(int aa=0;aa<c;aa++) for(int bb=aa+1;bb<c;bb++) {
        int i=ord[aa], j=ord[bb], need=rem-2;
        long long others=0;
        for(int q=0;q<c&&need>0;q++) {
            int z=ord[q];
            if(z==i||z==j) continue;
            others += g[z]; need--;
        }
        int inter=__builtin_popcountll(G[i]&G[j]);
        if((long long)g[i]+g[j]+others-inter < unc) {
            conflict[i] |= 1ULL<<cand[j];
            conflict[j] |= 1ULL<<cand[i];
        }
    }
}

// When branching on vv:
u64 branchAllowed = allowed & ~(1ULL<<vv);
int local = index_of_vv_in_cand;
if(local>=0) branchAllowed &= ~conflict[local];
dfs(branchAllowed, covered|S[vv]);
```

**FACT:** W4 plus pair conflicts gave:

| p | baseline nodes | W4+pair nodes | node ratio | row hashes |
|---:|---:|---:|---:|---|
| 101 | 79,380,440 | 37,223,266 | 2.132549× | identical |
| 103 | 97,867,203 | 46,912,915 | 2.086147× | identical |

**FACT:** Ratio calculation:

```python
for B,N in [(79380440,37223266),
            (97867203,46912915)]:
    print((B-N)/B*100, B/N)
```

Output:

```text
53.107760551591795 2.1325490353264542
52.064722846937805 2.0861462776295183
```

---

## Recommendation

**IDEA:** Build proactive W4 first: it is local, exact, cheap in bitsets, and already shows about a two-fold node reduction in my p=83/101/103 reproduction. Then add pair conflicts only for \(2\le r\le4\), where they gave a further reduction from 38,290,525 to 37,223,266 nodes at p=101 and from 49,320,090 to 46,912,915 at p=103.

**FACT:** No papers or web references were opened for this reply; there are no READ/ABSTRACT/MEMORY citations to report.

**Last question — IDEA:** Build **proactive W4 private-pool filtering** this week; production speed-up at p≥383 is **UNFINISHED** because only my stripped p=83/101/103 harness was measured.

--- end verbatim ---
END LETTER
