#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Count improper descendants of Astra's p=47 lift W through levels 32p, 64p (exact per 79fb6c5 definition).
int P=47,K=15;
long cnt[10];
void rec(long *w,long N,int lev,int maxlev){
  int odd=0; for(int i=0;i<K;i++) odd+=w[i]&1; if(odd<2) return; // q2 screen on parent
  if(lev==maxlev) return;
  long N2=2*N; long c[15];
  for(int b=0;b<(1<<K);b++){
    for(int i=0;i<K;i++) c[i]=w[i]+(((b>>i)&1)?N:0);
    int ok=1;
    for(long T=1;T<=N && ok;T+=2){ int cov=0; for(int i=0;i<K;i++){ long y=(T*c[i])%N2; long d=y<N2-y?y:N2-y; if(16*d<N2){cov=1;break;} } if(!cov) ok=0; }
    if(ok){ cnt[lev+1]++; rec(c,N2,lev+1,maxlev); }
  }
}
int main(int argc,char**argv){
  long W[15]={142,96,144,5,147,8,56,104,152,576,436,296,344,584,632};
  int maxlev=atoi(argv[1]); // level index: 4 = 16p (W), 5 = 32p, 6 = 64p
  rec(W,16*P,4,maxlev);
  for(int l=5;l<=maxlev;l++) printf("improper descendants at level %dp: %ld\n",1<<l,cnt[l]);
}
