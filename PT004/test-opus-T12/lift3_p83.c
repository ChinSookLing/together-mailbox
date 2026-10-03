/* TEST (Opus) · PT004 L3-C · stage (3): binary lifting at p = 83, k = 13, levels 2,4,8,16,32. Bitset version.
   Same definitions as lift_p83.c (Definition 2.1; F_{2l} from binary lifts of F_l), faster witness test:
   for level L (M = L*83) and residue x mod M, good[x] = set of times b in 1..M/2 with (k+1) d_M(b x) >= M.
   (b and M-b give the same distances, and b = 0 is never a witness.)  A lift has a witness iff the AND of its
   coordinates' sets is non-empty. gcd alternative at L = 2^j: some i with gcd(L, w_j : j != i) > 1, i.e. all
   coordinates except at most one are even. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define P 83
#define K 13
#define MAXW 21
#define MAXF 4000000
static int Ls[6]={1,2,4,8,16,32};
static uint64_t *good[6]; static int W[6];
static int gcd(int a,int b){ while(b){int t=a%b;a=b;b=t;} return a<0?-a:a; }
static void build(int li){
  int L=Ls[li], M=L*P, H=M/2; W[li]=(H+64)/64;
  good[li]=calloc((size_t)M*W[li],8);
  for(int x=0;x<M;x++) for(int b=1;b<=H;b++){ long r=((long)b*x)%M; long d=r<=M-r?r:M-r; if((K+1)*d>=M) good[li][(size_t)x*W[li]+b/64] |= 1ULL<<(b%64); }
}
static int gcd_proper(const int *w,int L){
  for(int i=0;i<K;i++){ int g=L; for(int j=0;j<K;j++) if(j!=i) g=gcd(g,w[j]); if(g>1) return 1; }
  return 0;
}
static int has_witness(const int *w,int li){
  int M=Ls[li]*P, Wd=W[li]; uint64_t acc[MAXW];
  for(int q=0;q<Wd;q++) acc[q]=~0ULL;
  for(int i=0;i<K;i++){ const uint64_t *g=good[li]+(size_t)(w[i]%M)*Wd; uint64_t any=0; for(int q=0;q<Wd;q++){acc[q]&=g[q]; any|=acc[q];} if(!any) return 0; }
  return 1;
}
/* enumerate binary lifts of base with DFS on the running AND */
static int (*out)[K]; static long nout;
static int Lprev_g, li_g;
static void dfs(const int *base,int i,int *w,const uint64_t *acc){
  int Wd=W[li_g], M=Ls[li_g]*P;
  if(i==K){
    int any=0; for(int q=0;q<Wd;q++) if(acc[q]){any=1;break;}
    if(any) return;                       /* witness exists: proper */
    if(gcd_proper(w,Ls[li_g])) return;    /* gcd alternative: proper */
    if(nout>=MAXF){fprintf(stderr,"MAXF\n");exit(2);} memcpy(out[nout++],w,sizeof(int)*K); return;
  }
  for(int a=0;a<2;a++){
    w[i]=base[i]+a*Lprev_g*P;
    const uint64_t *g=good[li_g]+(size_t)(w[i]%M)*Wd; uint64_t nacc[MAXW];
    for(int q=0;q<Wd;q++) nacc[q]=acc[q]&g[q];
    dfs(base,i+1,w,nacc);
  }
}
static int bufA[MAXF][K], bufB[MAXF][K];
int main(void){
  for(int li=0;li<6;li++) build(li);
  FILE *f=fopen("level1_p83_orbits.txt","r"); if(!f){perror("in");return 1;}
  FILE *sv=fopen("lift_p83_survivors_b.txt","w"); FILE *per=fopen("lift_p83_per_orbit.txt","w");
  char line[512]; long orbits=0, survive=0, tot[6]={0}; long done_lines=0;
  while(fgets(line,sizeof line,f)){
    int s=atoi(line); char *q=strchr(line,':'); int sup[K],n=0; char *tok=strtok(q+1,",\n"); while(tok){sup[n++]=atoi(tok); tok=strtok(NULL,",\n");}
    if(n!=s){fprintf(stderr,"parse\n");return 1;}
    int nvar=(s==13)?1:12;
    for(int var=0;var<nvar;var++){
      int r[K]; for(int i=0;i<s;i++) r[i]=sup[i]; if(s==12) r[12]=sup[var];
      orbits++;
      if(has_witness(r,0)){ fprintf(stderr,"level-1 rep has a witness?!\n"); return 1; }
      int (*cur)[K]=bufA, (*nxt)[K]=bufB; long nc=1; memcpy(cur[0],r,sizeof r); tot[0]++;
      int Lprev=1; long fl[6]={1,0,0,0,0,0};
      for(int li=1; li<6 && nc>0; li++){
        out=nxt; nout=0; Lprev_g=Lprev; li_g=li;
        uint64_t acc[MAXW]; for(int q=0;q<W[li];q++) acc[q]=~0ULL;
        int w[K];
        for(long c=0;c<nc;c++) dfs(cur[c],0,w,acc);
        tot[li]+=nout; fl[li]=nout; int (*t)[K]=cur; cur=nxt; nxt=t; nc=nout; Lprev=Ls[li];
      }
      if(fl[1]>0){ for(int i=0;i<K;i++) fprintf(per,"%d%c",r[i],i<K-1?' ':'|'); fprintf(per,"%ld %ld %ld %ld %ld\n",fl[1],fl[2],fl[3],fl[4],fl[5]); }
      if(nc>0){ survive++; fprintf(sv,"level-1 rep:"); for(int i=0;i<K;i++) fprintf(sv," %d",r[i]); fprintf(sv,"  |F_32| = %ld\n",nc); fflush(sv); }
    }
    if(++done_lines%5000==0){ fprintf(stderr,"%ld support orbits done, %ld multiset orbits, survivors so far %ld\n",done_lines,orbits,survive); }
  }
  fclose(sv); fclose(per);
  printf("level-1 unit orbits processed: %ld\n",orbits);
  printf("sum over orbits of |F_l(r)|: l=1 %ld | l=2 %ld | l=4 %ld | l=8 %ld | l=16 %ld | l=32 %ld\n",tot[0],tot[1],tot[2],tot[3],tot[4],tot[5]);
  printf("orbits with non-empty F_32: %ld (see lift_p83_survivors.txt)\n",survive);
  return 0;
}
