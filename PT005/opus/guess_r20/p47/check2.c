#include <stdio.h>
int P=47,K=15;
int improper(long*c,long N2){ // child at level N2: all odd T<=N2/2 covered
  long N=N2/2; for(long T=1;T<=N;T+=2){int cov=0; for(int i=0;i<K;i++){long y=(T*c[i])%N2; long d=y<N2-y?y:N2-y; if(16*d<N2){cov=1;break;}} if(!cov) return 0;} return 1;}
int main(){
  long W[15]={142,96,144,5,147,8,56,104,152,576,436,296,344,584,632};
  long par[15]; for(int i=0;i<K;i++) par[i]=W[i]%376;
  // W must be the child of par with bits b_i = (W_i>=376)
  printf("W improper at 16p (odd-T check): %d\n", improper(W,752));
  long n=0; long c[15];
  for(int b=0;b<(1<<K);b++){ for(int i=0;i<K;i++) c[i]=par[i]+(((b>>i)&1)?376:0); n+=improper(c,752);} 
  printf("improper children of W's parent at 16p: %ld\n",n);
  long m=0; for(int b=0;b<(1<<K);b++){ for(int i=0;i<K;i++) c[i]=W[i]+(((b>>i)&1)?752:0); m+=improper(c,1504);} 
  printf("improper children of W at 32p: %ld\n",m);
}
