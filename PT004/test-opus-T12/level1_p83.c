/* TEST (Opus) · PT004 L3-C · stage (2): level one at p = 83, k = 13.
   New code from arXiv:2609.02604v2 §4, eq. (7): speed class v covers folded time class a when (k+1) d_p(a v) < p.
   I(13,83,1) = 13-multisets of folded speed classes whose covered sets cover all 41 folded time classes.
   Work in discrete logs of G = Z_83^* / {±1} (cyclic of order 41): speed v covers {log a} = D - log v (a translate).
   Enumerate every covering SUPPORT T (as a set of speed classes, |T| <= 13); a support of size s carries C(12, s-1)
   13-multisets. Units act by translation; 41 is prime, so every orbit has exactly 41 members.
   Output: counts by support size, total multisets, number of unit orbits, and sha256-able list of canonical supports. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#define P 83
#define K 13
#define N 41
static int logt[P];            /* log of folded class */
static int expt[N];            /* class of a log */
static uint64_t covmask[N];    /* by speed-log s: mask of covered time-logs */
static int deadline[N];        /* time-log x: largest speed-log index that can cover it */
static uint64_t FULL;
static long long cnt_by_size[K+1];
static long long nodes = 0;
static FILE *out;
static int chosen[K+1];
static long long comb(int n,int r){ long long c=1; for(int i=1;i<=r;i++) c=c*(n-r+i)/i; return c; }
static int fold(int x){ x%=P; if(x<0)x+=P; return x<=P-x? x : P-x; }
static uint64_t need_by[N];    /* times whose deadline is j */
static int canon_cmp(const int *a,const int *b,int s){ for(int i=0;i<s;i++){ if(a[i]!=b[i]) return a[i]-b[i]; } return 0; }
static int cmpint(const void*a,const void*b){ return *(int*)a-*(int*)b; }
static void emit(int s){
  /* canonical representative of the translation orbit of the support: lexicographically least sorted translate */
  int best[K], cur[K];
  for(int i=0;i<s;i++) best[i]=chosen[i];
  for(int sh=1; sh<N; sh++){
    for(int i=0;i<s;i++) cur[i]=(chosen[i]+sh)%N;
    qsort(cur,s,sizeof(int),cmpint);
    if(canon_cmp(cur,best,s)<0) for(int i=0;i<s;i++) best[i]=cur[i];
  }
  /* only print the orbit once: when this support IS its canonical form */
  int same=1; for(int i=0;i<s;i++) if(best[i]!=chosen[i]){same=0;break;}
  if(same){ fprintf(out,"%d:",s); for(int i=0;i<s;i++){ fprintf(out,"%s%d", i?",":"", expt[best[i]]); } fprintf(out,"\n"); }
}
static void dfs(int j,int size,uint64_t cov){
  nodes++;
  if(j==N){ if(cov==FULL){ cnt_by_size[size]++; emit(size);} return; }
  uint64_t unc = FULL & ~cov;
  if(__builtin_popcountll(unc) > 5*(K-size)) return;
  /* include j */
  if(size<K){
    uint64_t c2 = cov | covmask[j];
    if((need_by[j] & ~c2)==0){ chosen[size]=j; dfs(j+1,size+1,c2); }
  }
  /* exclude j */
  if((need_by[j] & ~cov)==0) dfs(j+1,size,cov);
}
int main(void){
  int g=2, x=1;
  for(int e=0;e<N;e++){ int f=fold(x); logt[f]=e; expt[e]=f; x=(x*g)%P; }
  for(int e=0;e<N;e++){ if(expt[e]<1||expt[e]>N){fprintf(stderr,"bad gen\n");return 1;} }
  FULL = (N==64)?~0ULL:((1ULL<<N)-1);
  /* covmask by speed-log: speed class v=expt[s] covers time class a iff 14*d(a v) < 83 */
  for(int s=0;s<N;s++){ uint64_t m=0; int v=expt[s];
    for(int a=1;a<=N;a++){ int r=(a*v)%P; int d = r<=P-r? r:P-r; if((K+1)*d < P) m |= 1ULL<<logt[a]; }
    covmask[s]=m; }
  /* sanity: every speed covers exactly floor((p-1)/(k+1)) = 5 times */
  for(int s=0;s<N;s++) if(__builtin_popcountll(covmask[s])!=5){fprintf(stderr,"cover size != 5\n");return 1;}
  for(int t=0;t<N;t++){ int dl=-1; for(int s=0;s<N;s++) if(covmask[s]>>t&1) if(s>dl) dl=s; deadline[t]=dl; need_by[dl] |= 1ULL<<t; }
  out=fopen("level1_p83_orbits.txt","w");
  dfs(0,0,0);
  fclose(out);
  long long total=0;
  printf("p=%d k=%d folded classes=%d each speed covers 5 times\n",P,K,N);
  for(int s=1;s<=K;s++) if(cnt_by_size[s]){ long long w=comb(K-1,s-1); printf("covering supports of size %2d: %lld  (x C(12,%d)=%lld multisets each)\n",s,cnt_by_size[s],s-1,w); total += cnt_by_size[s]*w; }
  long long sup=0; for(int s=1;s<=K;s++) sup+=cnt_by_size[s];
  printf("covering supports total: %lld; support orbits: %lld (remainder %lld)\n", sup, sup/N, sup%N);
  printf("improper level-1 13-multisets |I(13,83,1)|: %lld; unit orbits: %lld (remainder %lld)\n", total, total/N, total%N);
  int tau=0; for(int s=1;s<=K;s++) if(cnt_by_size[s]){tau=s;break;}
  printf("tau_13(83) (smallest cover): %d\n", tau);
  fprintf(stderr,"dfs nodes %lld\n",nodes);
  return 0;
}
