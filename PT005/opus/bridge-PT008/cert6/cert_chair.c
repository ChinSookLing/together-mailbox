// Chair's own test program for PT-008 Cert(p), written from the definition in the handoff (not from WB code).
// M=6p; A={1..3p}\{p,2p,3p}; all nondecreasing 5-tuples from A; filter: for each i, gcd(the other four, M)=1;
// need some j in [0,M) with p <= j*rho_i mod M <= 5p for all i (endpoints safe).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static int g(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){
  int p=atoi(argv[1]); int M=6*p; int A[512],n=0;
  for(int x=1;x<=3*p;x++) if(x%p) A[n++]=x;
  // precompute safe[x][j] as bitset over j for residue x
  int W=(M+63)/64; uint64_t *S=calloc((size_t)(3*p+1)*W,8);
  for(int x=1;x<=3*p;x++) for(int j=0;j<M;j++){int r=(int)((long)j*x%M); if(r>=p&&r<=5*p) S[(size_t)x*W+j/64]|=1ULL<<(j%64);}
  long long tot=0,filt=0,fail=0; uint64_t t1[8],t2[8],t3[8],t4[8];
  for(int a=0;a<n;a++){int x1=A[a]; for(int w=0;w<W;w++)t1[w]=S[(size_t)x1*W+w];
   for(int b=a;b<n;b++){int x2=A[b]; int g12=g(g(x1,x2),M); for(int w=0;w<W;w++)t2[w]=t1[w]&S[(size_t)x2*W+w];
    for(int c=b;c<n;c++){int x3=A[c]; int g123=g(g12,x3); for(int w=0;w<W;w++)t3[w]=t2[w]&S[(size_t)x3*W+w];
     for(int d=c;d<n;d++){int x4=A[d]; int g1234=g(g123,x4); for(int w=0;w<W;w++)t4[w]=t3[w]&S[(size_t)x4*W+w];
      for(int e=d;e<n;e++){int x5=A[e]; tot++;
        int v[5]={x1,x2,x3,x4,x5}; int ok=1;
        for(int i=0;i<5&&ok;i++){int gg=M; for(int k=0;k<5;k++) if(k!=i) gg=g(gg,v[k]); if(gg!=1) ok=0;}
        if(!ok) continue; filt++;
        int any=0; for(int w=0;w<W;w++) if(t4[w]&S[(size_t)x5*W+w]){any=1;break;}
        if(!any){fail++; if(getenv("ALL")||fail<=5) printf("FAIL %d %d %d %d %d\n",x1,x2,x3,x4,x5);}
      }}}}}
  printf("p=%d M=%d |A|=%d tuples=%lld filtered=%lld fail=%lld\n",p,M,n,tot,filt,fail); return 0;}
