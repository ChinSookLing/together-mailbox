/* TEST (Opus) · PT004 L3-C · stage (3b): level 14 for the two persistent orbits at p = 83, k = 13 (paper §4.3).
   For each improper level-2 member w of the orbit's fiber F_2(r), its 7^13 lifts to level 14 are w + a*(2p),
   a in {0..6}^13. A lift is witness-free iff no b in 1..M/2 (M = 14p) has (k+1) d_M(b w_i) >= M for all i.
   Branch and bound over digits (our own form of the paper's bound): keep the set A of times that are still
   witnesses for all assigned coordinates; for each unassigned coordinate i let b_i = max over its 7 choices of
   |A \ good(choice)| (times it can kill). If |A| > sum b_i, every completion keeps a witness: prune.
   Leaves with A empty are witness-free; each is tested for the gcd alternative gcd(14, w_j : j != i) > 1. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define P 83
#define K 13
#define WD 10
static int M14=14*P, H14, M2=2*P, H2;
static uint64_t *good14, *good2;
static long leaves=0, wf=0, wf_gcd_proper=0, wf_all7=0, nodes=0;
static int gcd(int a,int b){ while(b){int t=a%b;a=b;b=t;} return a<0?-a:a; }
static void build(uint64_t **g,int M,int H,int words){ *g=calloc((size_t)M*words,8); for(int x=0;x<M;x++) for(int b=1;b<=H;b++){ long r=((long)b*x)%M; long d=r<=M-r?r:M-r; if((K+1)*d>=M) (*g)[(size_t)x*words+b/64]|=1ULL<<(b%64);} }
static int pc(const uint64_t *a){ int c=0; for(int q=0;q<WD;q++) c+=__builtin_popcountll(a[q]); return c; }
static int base[K], w[K];
static FILE *leaf_out;
static void dfs(int i,const uint64_t *A){
  nodes++;
  int nA=pc(A);
  if(i==K){ leaves++; if(nA==0){ wf++;
      int prop=0; for(int x=0;x<K&&!prop;x++){ int g=14; for(int j=0;j<K;j++) if(j!=x) g=gcd(g,w[j]); if(g>1) prop=1; }
      if(prop) wf_gcd_proper++;
      int all7=1; for(int j=0;j<K;j++) if(w[j]%7){all7=0;break;} if(all7) wf_all7++;
      if(!prop){ fprintf(leaf_out,"IMPROPER LEAF:"); for(int j=0;j<K;j++) fprintf(leaf_out," %d",w[j]); fprintf(leaf_out,"\n"); }
    } return; }
  if(nA==0){ /* every completion is witness-free: enumerate them all (gcd test needs each) */ }
  else {
    int sumb=0; uint64_t tmp[WD];
    for(int j=i;j<K;j++){ int best=0; for(int a=0;a<7;a++){ const uint64_t *g=good14+(size_t)((base[j]+a*M2)%M14)*WD; int kill=0; for(int q=0;q<WD;q++) kill+=__builtin_popcountll(A[q]&~g[q]); if(kill>best) best=kill; } sumb+=best; if(sumb>=nA) break; }
    if(nA>sumb) return;
    (void)tmp;
  }
  for(int a=0;a<7;a++){ w[i]=base[i]+a*M2; const uint64_t *g=good14+(size_t)(w[i]%M14)*WD; uint64_t B[WD]; for(int q=0;q<WD;q++) B[q]=A[q]&g[q]; dfs(i+1,B); }
}
static int improper2(const int *v){
  int W2=(H2+64)/64; uint64_t acc[2]={~0ULL,~0ULL};
  for(int i=0;i<K;i++){ const uint64_t *g=good2+(size_t)(v[i]%M2)*W2; for(int q=0;q<W2;q++) acc[q]&=g[q]; }
  int any=0; for(int q=0;q<W2;q++) if(acc[q]) any=1; if(any) return 0;
  for(int x=0;x<K;x++){ int g=2; for(int j=0;j<K;j++) if(j!=x) g=gcd(g,v[j]); if(g>1) return 0; }
  return 1;
}
int main(void){
  H14=M14/2; H2=M2/2; if((H14+64)/64>WD){fprintf(stderr,"WD\n");return 1;}
  build(&good14,M14,H14,WD); build(&good2,M2,H2,(H2+64)/64);
  leaf_out=fopen("level14_p83_improper_leaves.txt","w");
  int reps[2][K]={{1,2,3,4,5,6,7,8,9,10,11,12,13},{1,2,3,4,5,6,7,8,9,10,11,13,24}};
  const char *name[2]={"a13 = (1,...,13)","b13 = (1,...,11,13,24)"};
  for(int o=0;o<2;o++){
    long f2=0, l0=leaves, w0=wf, g0=wf_gcd_proper, s0=wf_all7, n0=nodes;
    for(int a=0;a<(1<<K);a++){ int v[K]; for(int i=0;i<K;i++) v[i]=reps[o][i]+((a>>i)&1)*P; if(!improper2(v)) continue; f2++;
      memcpy(base,v,sizeof v); uint64_t A[WD]; for(int q=0;q<WD;q++) A[q]=~0ULL;
      /* clear bits above H14 and bit 0 */
      for(int q=0;q<WD;q++) A[q]=0; for(int b=1;b<=H14;b++) A[b/64]|=1ULL<<(b%64);
      dfs(0,A);
      fprintf(stderr,"  %s: level-2 member %ld done, nodes so far %ld\n",name[o],f2,nodes); }
    printf("%s: |F_2| = %ld; level-14 search nodes %ld; witness-free leaves %ld; of these proper by gcd %ld; all 13 coords divisible by 7: %ld\n",
      name[o], f2, nodes-n0, wf-w0, wf_gcd_proper-g0, wf_all7-s0);
  }
  fclose(leaf_out);
  printf("TOTAL witness-free leaves %ld, gcd-proper %ld, improper (neither) %ld\n", wf, wf_gcd_proper, wf-wf_gcd_proper);
  return 0;
}
