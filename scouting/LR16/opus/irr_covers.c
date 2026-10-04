/* irr_covers.c — count irredundant covers at level one, for scouting k = 13, 14, 15.
 * Folded classes 1..n, n=(p-1)/2.  Speed v covers time a iff (k+1)*d_p(a*v) < p  (eq. (7)).
 * An irredundant cover: a set S of distinct speed classes covering all n times, in which
 * every class covers at least one time no other class in S covers.
 * Units mod p act simply transitively on folded classes, so we count covers that contain
 * class 1 (c1[s]) and recover all covers N_s = n*c1[s]/s.
 * Include/exclude DFS over classes 2..n with prunes:
 *   (a) uncovered times must lie in the union of the remaining classes;
 *   (b) |uncovered| <= (slots left) * (max cover of one class);
 *   (c) a chosen class whose private set is empty can never regain one -> prune.
 * Usage: ./irr_covers k p smax
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#define W 6               /* up to 384 folded times, p <= 769 */
typedef struct { uint64_t w[W]; } B;
static int n, k, p, smax, m;
static B cov[400], suf[402];
static long long cnt[40]; static long long nodes;
static inline int pc(const B *a){int c=0;for(int i=0;i<W;i++)c+=__builtin_popcountll(a->w[i]);return c;}
static inline int sub(const B *a,const B *b){for(int i=0;i<W;i++)if(a->w[i]&~b->w[i])return 0;return 1;}
static int dp(long x){long r=x%p;return r<p-r?r:p-r;}
static int chosen[40]; static int ns;
static B full;
/* private check: for each chosen class, does it own a time no other chosen covers */
static int all_private(void){
  for(int i=0;i<ns;i++){
    B o; memset(&o,0,sizeof o);
    for(int j=0;j<ns;j++) if(j!=i) for(int t=0;t<W;t++) o.w[t]|=cov[chosen[j]].w[t];
    int ok=0; for(int t=0;t<W;t++) if(cov[chosen[i]].w[t]&~o.w[t]){ok=1;break;}
    if(!ok) return 0;
  }
  return 1;
}
static void dfs(int v, B *covd){
  nodes++;
  if(!all_private()) return;                       /* (c) */
  B un; for(int t=0;t<W;t++) un.w[t]=full.w[t]&~covd->w[t];
  int u=pc(&un);
  if(u==0){ cnt[ns]++; return; }                   /* irredundant cover; supersets are redundant */
  if(ns>=smax) return;
  if(v>n) return;
  if(!sub(&un,&suf[v])) return;                    /* (a) */
  if(u > (smax-ns)*m) return;                      /* (b) */
  /* include v */
  B c2; for(int t=0;t<W;t++) c2.w[t]=covd->w[t]|cov[v].w[t];
  chosen[ns++]=v; dfs(v+1,&c2); ns--;
  /* exclude v */
  dfs(v+1,covd);
}
int main(int argc,char**argv){
  k=atoi(argv[1]); p=atoi(argv[2]); smax=atoi(argv[3]); n=(p-1)/2;
  if(n>64*W){fprintf(stderr,"p too large\n");return 1;}
  memset(cov,0,sizeof cov); memset(&full,0,sizeof full);
  for(int a=1;a<=n;a++) full.w[(a-1)/64]|=1ULL<<((a-1)%64);
  m=0;
  for(int v=1;v<=n;v++){int c=0;for(int a=1;a<=n;a++) if((long)(k+1)*dp((long)a*v)<p){cov[v].w[(a-1)/64]|=1ULL<<((a-1)%64);c++;} if(c>m)m=c;}
  memset(&suf[n+1],0,sizeof(B));
  for(int v=n;v>=1;v--) for(int t=0;t<W;t++) suf[v].w[t]=suf[v+1].w[t]|cov[v].w[t];
  clock_t c0=clock();
  chosen[0]=1; ns=1; B c=cov[1]; dfs(2,&c);
  double sec=(double)(clock()-c0)/CLOCKS_PER_SEC;
  printf("k=%d p=%d n=%d per-class=%d smax=%d nodes=%lld time=%.2fs\n",k,p,n,m,smax,nodes,sec);
  for(int s=1;s<=smax;s++) if(cnt[s]) printf("  size %d: covers containing 1 = %lld, all irredundant covers = %lld\n",s,cnt[s],cnt[s]*n/s);
  return 0;
}
