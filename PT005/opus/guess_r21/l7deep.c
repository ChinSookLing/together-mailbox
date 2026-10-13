#include <stdio.h>
int K=15,P=37;
long g(long a,long b){while(b){long t=a%b;a=b;b=t;}return a;}
int improper(long*c,long N2){ long N=N2/2; for(long T=1;T<=N;T+=2){int cov=0; for(int i=0;i<K;i++){long y=(T*c[i])%N2; long d=y<N2-y?y:N2-y; if(16*d<N2){cov=1;break;}} if(!cov) return 0;} return 1;}
int l7(long*u,long M){ for(long D=2;D<=M;D+=2){ if(M%D) continue; int e=0; long s=0; for(int i=0;i<K;i++){ if(u[i]%D==0) continue; e++; long gi=g(D,u[i]); long Di=D/gi; s+=gi*((Di+7)/8);} if(e>=2 && s<D) return (int)D; } return 0; }
long nfail[10], ntot[10];
void rec(long*w,long N,int lev,int maxlev){ int odd=0; for(int i=0;i<K;i++) odd+=w[i]&1; if(odd<2) return;
  ntot[lev]++; if(!l7(w,N)) { nfail[lev]++; } else return; /* handled lifts need no further lifting */
  if(lev==maxlev) return; long c[15];
  for(int b=0;b<(1<<K);b++){ for(int i=0;i<K;i++) c[i]=w[i]+(((b>>i)&1)?N:0); if(improper(c,2*N)) rec(c,2*N,lev+1,maxlev);} }
int main(){ long W[15]={112,2,336,448,5,6,192,8,416,528,48,160,13,14,16};
  rec(W,16*P,4,7); for(int l=4;l<=7;l++) printf("level %dp: improper lifts reached %ld, failing L7 (D|%dp) %ld\n",1<<l,ntot[l],1<<l,nfail[l]); }
