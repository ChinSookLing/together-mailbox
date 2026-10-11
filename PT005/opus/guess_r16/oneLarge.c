// Chair's independent engine (Opus, 2026-10-11) for the R16 claim (Kimi):
// every 14-set with at most one speed > 24 has m >= 97/6864.
// Covers: (i) all 14-subsets of {1..24}; (ii) every 13-subset K' of {1..24} plus any v >= 25.
// Exact integer arithmetic. Unit = 1/L, L = 16*lcm(1..24).
// Tail: proven per-interval bound loss <= min(len, len/8 + 7/(64v)) (GPT/Astra R16 Q1), monotone in v.
// usage: oneLarge FIRST_MIN FIRST_MAX   (partition by the smallest element of the 13-set)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll; typedef __int128 i128;
#define MAXI 4096
#ifndef MAXS
#define MAXS 24
#endif
#if MAXS==24
static const ll A = 5354228880LL;
#elif MAXS==30
static const ll A = 2329089562800LL;
#endif
static const ll L = 16LL*A;
typedef struct { ll a,b; } iv;
static iv buf[15][MAXI]; static int cnt[15];
static ll nexact=0, nsets=0, nfail=0, n14=0;
static i128 best_num=-1; static ll best_den=1; static int best_set[14]; static int best_v;
static i128 best14_num=-1; static ll best14_den=1; static int best14_set[14];
static int cur[14];
static void pr128(i128 x);

static int intersect(const iv *in, int n, int k, iv *out){
  ll Ak = L/(16*k), P = 16*Ak; int m=0;
  for(int i=0;i<n;i++){
    ll a=in[i].a,b=in[i].b;
    for(ll j=a/P; j*P < b; j++){
      ll lo=j*P+Ak, hi=j*P+15*Ak;
      if(lo<a) lo=a; if(hi>b) hi=b;
      if(lo<hi){ if(m && out[m-1].b==lo) out[m-1].b=hi; else { out[m].a=lo; out[m].b=hi; m++; } }
    }
  }
  if(m>=MAXI){fprintf(stderr,"overflow\n");exit(1);}
  return m;
}
// exact loss of intervals under unsafe arcs of v, in units 1/(L v)
static i128 exact_loss(const iv *I, int n, ll v){
  i128 loss=0;
  for(int i=0;i<n;i++){
    i128 a=(i128)I[i].a*v, b=(i128)I[i].b*v;    // scaled
    // arcs [(16j-1)A,(16j+1)A], j integer (j=0 arc wraps: [-A,A] and [16v A - A, 16vA+A])
    ll j0 = (ll)((a + A) / (16*(i128)A)); if (j0>0) j0--;
    for(ll j=j0; (i128)(16*j-1)*A < b; j++){
      i128 lo=(i128)(16*j-1)*A, hi=(i128)(16*j+1)*A;
      if(lo<a) lo=a; if(hi>b) hi=b;
      if(lo<hi) loss+=hi-lo;
    }
  }
  return loss;
}
static int bound_ok(const iv *I, int n, ll msum, ll v){
  // need msum - sum min(len, len/8 + 7L/(64v)) >= 97L/6864 ; work in units 1/(64*v*6864*... ) using long double safely? use exact i128:
  // loss_i*64v <= min(64v len, 8v len + 7L)
  i128 tot=0;
  for(int i=0;i<n;i++){ i128 len=I[i].b-I[i].a; i128 x=64*(i128)v*len, y=8*(i128)v*len+7*(i128)L; tot += x<y?x:y; }
  // (msum*64v - tot)*6864 >= 97 L *64 v
  return ((i128)msum*64*v - tot)*6864 >= (i128)97*L*64*v;
}
static void rec_best(i128 num, ll den, int v, int *setbest, int which){
  // compare num/den with best
  if(which==0){ if(best_num<0 || num*best_den < best_num*den){ best_num=num; best_den=den; memcpy(best_set,cur,13*sizeof(int)); best_v=v; } }
  else { if(best14_num<0 || num*best14_den < best14_num*den){ best14_num=num; best14_den=den; memcpy(best14_set,cur,13*sizeof(int)); best14_set[13]=v; } }
}
static void handle13(){
  iv *I=buf[13]; int n=cnt[13]; ll msum=0; for(int i=0;i<n;i++) msum+=I[i].b-I[i].a;
  nsets++;
  // (i) 14-sets inside {1..24}: largest element v in (max K', 24]
  for(int v=cur[12]+1; v<=MAXS; v++){
    ll Ak=L/(16*v); (void)Ak;
    iv tmp[MAXI]; int m=intersect(I,n,v,tmp); ll s=0; for(int i=0;i<m;i++) s+=tmp[i].b-tmp[i].a;
    n14++;
    if((i128)s*6864 < (i128)97*L){ nfail++; printf("FAIL14 "); for(int t=0;t<13;t++)printf("%d,",cur[t]); printf("%d\n",v);}
    rec_best(s, L, v, NULL, 1);
  }
  // (ii) v >= 25
  if(((i128)msum - L/8)*6864 >= (i128)97*L) return;   // cap: loss <= 1/8 always
  for(ll v=MAXS+1;;v++){
    if(bound_ok(I,n,msum,v)) break;
    i128 loss=exact_loss(I,n,v); nexact++;
    i128 num=(i128)msum*v - loss; ll den=L*v;      // m = num/den
    if(num*6864 < (i128)97*den){ nfail++; printf("FAIL "); for(int t=0;t<13;t++)printf("%d,",cur[t]); printf(" v=%lld\n",v);}
    rec_best(num, den, (int)v, NULL, 0);
  }
}
static void dfs(int depth, int start){
  if(depth==13){ handle13(); return; }
  for(int k=start; k<=MAXS-(12-depth); k++){
    cur[depth]=k; cnt[depth+1]=intersect(buf[depth],cnt[depth],k,buf[depth+1]);
    dfs(depth+1,k+1);
  }
}
static void pr128_(i128);
static void pr128(i128 x){ char s[64]; int n=0; if(x==0){printf("0");return;} while(x>0){s[n++]='0'+(int)(x%10); x/=10;} while(n) putchar(s[--n]); }
int main(int argc,char**argv){
  if(argc>1 && !strcmp(argv[1],"test")){ int k[13]; ll v;
    while(scanf("%d %d %d %d %d %d %d %d %d %d %d %d %d %lld",&k[0],&k[1],&k[2],&k[3],&k[4],&k[5],&k[6],&k[7],&k[8],&k[9],&k[10],&k[11],&k[12],&v)==14){
      buf[0][0].a=0; buf[0][0].b=L; cnt[0]=1;
      for(int d=0;d<13;d++) cnt[d+1]=intersect(buf[d],cnt[d],k[d],buf[d+1]);
      ll ms=0; for(int i=0;i<cnt[13];i++) ms+=buf[13][i].b-buf[13][i].a;
      i128 num=(i128)ms*v-exact_loss(buf[13],cnt[13],v); pr128(num); printf(" "); pr128((i128)L*v); printf("\n"); }
    return 0; }
  int f0=atoi(argv[1]), f1=atoi(argv[2]);
  buf[0][0].a=0; buf[0][0].b=L; cnt[0]=1;
  for(int k=f0;k<=f1 && k<=MAXS-12;k++){ cur[0]=k; cnt[1]=intersect(buf[0],1,k,buf[1]); dfs(1,k+1); }
  printf("first in [%d,%d]: sets13=%lld exact_checks=%lld sets14=%lld fails=%lld\n",f0,f1,nsets,nexact,n14,nfail);
  if(best_num>=0){ printf("min (13-set + v>=25) = "); pr128(best_num); printf("/"); pr128((i128)best_den); printf(" at {"); for(int t=0;t<13;t++)printf("%d,",best_set[t]); printf("} + v=%d\n",best_v);}
  if(best14_num>=0){ printf("min 14-set <=24 = "); pr128(best14_num); printf("/"); pr128((i128)best14_den); printf(" at {"); for(int t=0;t<14;t++)printf("%d%s",best14_set[t],t<13?",":""); printf("}\n");}
  return 0;
}
