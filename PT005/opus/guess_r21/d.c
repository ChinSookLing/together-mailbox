#include <stdio.h>
#include <stdlib.h>
int K=15; long cnt[12];
int improper(long*c,long N2){ long N=N2/2; for(long T=1;T<=N;T+=2){int cov=0; for(int i=0;i<K;i++){long y=(T*c[i])%N2; long d=y<N2-y?y:N2-y; if(16*d<N2){cov=1;break;}} if(!cov) return 0;} return 1;}
void rec(long*w,long N,int lev,int maxlev){ int odd=0; for(int i=0;i<K;i++) odd+=w[i]&1; if(odd<2) return; if(lev==maxlev) return;
  long c[15]; for(int b=0;b<(1<<K);b++){ for(int i=0;i<K;i++) c[i]=w[i]+(((b>>i)&1)?N:0); if(improper(c,2*N)){cnt[lev+1]++; rec(c,2*N,lev+1,maxlev);} } }
int main(int argc,char**argv){ int P=37; long W[15]={112,2,336,448,5,6,192,8,416,528,48,160,13,14,16};
  for(int k=1;k<=4;k++){ long N=(1L<<k)*P; long w[15]; int odd=0; for(int i=0;i<K;i++){w[i]=W[i]%N; odd+=w[i]&1;} printf("level %ld: improper=%d odd=%d\n",N,improper(w,N),odd);}
  int maxlev=atoi(argv[1]); rec(W,16*P,4,maxlev); for(int l=5;l<=maxlev;l++) printf("improper descendants at %ldp: %ld\n",1L<<l,cnt[l]); }
