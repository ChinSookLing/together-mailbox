// Kimi-style (MMCS-like) harness, ported to multiword bitsets, started from an exact gate-job prefix
// dumped from the author's engine (sel, remaining candidate classes, class-1 quota). Counts raw rows
// (15 classes, cover, every class private) to compare with the author's rawscan.
#include <bits/stdc++.h>
using namespace std; typedef unsigned long long u64;
const int W=4, K=15;
struct B{u64 w[W]={};};
static inline bool anyb(const B&a){for(int i=0;i<W;i++)if(a.w[i])return 1;return 0;}
static inline int cnt(const B&a){int s=0;for(int i=0;i<W;i++)s+=__builtin_popcountll(a.w[i]);return s;}
int p,n,m,mode,quota; vector<B> S; vector<int> chosen; vector<u64> qm; B C1;
long long nodes=0,rows=0;
void dfs(B allowed,B covered){
  nodes++;
  B U; for(int i=0;i<W;i++) U.w[i]=~covered.w[i]&((i<W)?~0ULL:0);
  // mask to n bits
  for(int t=n;t<64*W;t++) U.w[t>>6]&=~(1ULL<<(t&63));
  int rem=K-(int)chosen.size();
  // private sets
  vector<B> priv;
  for(size_t a=0;a<chosen.size();a++){ B o; for(size_t b=0;b<chosen.size();b++) if(a!=b) for(int i=0;i<W;i++) o.w[i]|=S[chosen[b]].w[i];
    B pa; for(int i=0;i<W;i++) pa.w[i]=S[chosen[a]].w[i]&~o.w[i]; if(!anyb(pa)) return; priv.push_back(pa); }
  if(!anyb(U)){ if(rem==0) rows++; return; }
  if(!rem) return;
  // quota on class 1 (chosen[0]==0): popcount(OR qm[v], v!=class1) <= quota
  { u64 q=0; for(size_t a=1;a<chosen.size();a++) q|=qm[chosen[a]]; if(__builtin_popcountll(q)>quota) return; }
  if(mode){ B keep; for(int i=0;i<W;i++){u64 A=allowed.w[i]; while(A){int b=__builtin_ctzll(A);A&=A-1;int v=64*i+b; bool bad=0;
      for(auto&pa:priv){bool sub=1; for(int j=0;j<W;j++) if(pa.w[j]&~S[v].w[j]){sub=0;break;} if(sub){bad=1;break;}}
      if(!bad) keep.w[i]|=1ULL<<b; }} allowed=keep; }
  vector<int> g; for(int i=0;i<W;i++){u64 A=allowed.w[i]; while(A){int b=__builtin_ctzll(A);A&=A-1;int v=64*i+b; int x=0; for(int j=0;j<W;j++) x+=__builtin_popcountll(S[v].w[j]&U.w[j]); if(x) g.push_back(x);}}
  if((int)g.size()<rem) { /* may still finish with fewer gains? need exactly rem classes each adding coverage */ }
  sort(g.rbegin(),g.rend()); long long cap=0; for(int i=0;i<rem&&i<(int)g.size();i++) cap+=g[i]; if(cap<cnt(U)) return;
  int bt=-1,bc=INT_MAX;
  for(int i=0;i<W;i++){u64 X=U.w[i]; while(X){int b=__builtin_ctzll(X);X&=X-1;int t=64*i+b; int c=0;
      for(int j=0;j<W;j++){u64 A=allowed.w[j]; while(A){int bb=__builtin_ctzll(A);A&=A-1; if(S[64*j+bb].w[t>>6]>>(t&63)&1) c++;}}
      if(c<bc){bc=c;bt=t;}}}
  if(!bc) return;
  for(int j=0;j<W;j++){u64 A=allowed.w[j]; while(A){int bb=__builtin_ctzll(A);A&=A-1;int v=64*j+bb;
      if(!(S[v].w[bt>>6]>>(bt&63)&1)) continue;
      allowed.w[v>>6]&=~(1ULL<<(v&63)); chosen.push_back(v); B c2; for(int i=0;i<W;i++) c2.w[i]=covered.w[i]|S[v].w[i]; dfs(allowed,c2); chosen.pop_back(); }}
}
int main(int argc,char**argv){
  FILE*f=fopen(argv[1],"r"); mode=atoi(argv[2]); int ns; fscanf(f,"%d %d",&p,&ns);
  n=(p-1)/2; m=(p-1)/16; S.assign(n,B());
  for(int v=0;v<n;v++) for(int t=1;t<=n;t++){ long long r=(long long)(v+1)*t%p; r=min(r,(long long)p-r); if(16*r<p) S[v].w[(t-1)>>6]|=1ULL<<((t-1)&63); }
  // qm: bit i = i-th point of class 1
  vector<int> c1pts; for(int t=0;t<n;t++) if(S[0].w[t>>6]>>(t&63)&1) c1pts.push_back(t);
  qm.assign(n,0); for(int v=0;v<n;v++) for(size_t i=0;i<c1pts.size();i++){int t=c1pts[i]; if(S[v].w[t>>6]>>(t&63)&1) qm[v]|=1ULL<<i;}
  B covered; for(int i=0;i<ns;i++){int x; fscanf(f,"%d",&x); chosen.push_back(x-1); for(int j=0;j<W;j++) covered.w[j]|=S[x-1].w[j];}
  B allowed; int x; char line[1<<16]; fgets(line,sizeof line,f); fgets(line,sizeof line,f);
  { char*q=line; int off; while(sscanf(q,"%d%n",&x,&off)==1){ allowed.w[(x-1)>>6]|=1ULL<<((x-1)&63); q+=off; } }
  fscanf(f,"%d",&quota);
  auto t0=chrono::steady_clock::now(); dfs(allowed,covered);
  double secs=chrono::duration<double>(chrono::steady_clock::now()-t0).count();
  printf("p=%d mode=%d nodes=%lld raw_rows=%lld secs=%.1f\n",p,mode,nodes,rows,secs);
}
