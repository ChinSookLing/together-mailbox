// Chair's independent check of WB-02 witness file for p=23: byte per nondecreasing 5-tuple (lex order), min safe j or 255 (= no safe j and gcd fails)
#include <stdio.h>
#include <stdlib.h>
static int g(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
int main(int c,char**v){int p=atoi(v[1]);FILE*f=fopen(v[2],"rb");int M=6*p,A[512],n=0;for(int x=1;x<=3*p;x++)if(x%p)A[n++]=x;
 long long tot=0,bad=0,ex=0;
 for(int a=0;a<n;a++)for(int b=a;b<n;b++)for(int cc=b;cc<n;cc++)for(int d=cc;d<n;d++)for(int e=d;e<n;e++){
  int r[5]={A[a],A[b],A[cc],A[d],A[e]};int j=fgetc(f);tot++; if(j==EOF){printf("short\n");return 1;}
  int safe(int jj){for(int i=0;i<5;i++){int z=(int)((long)jj*r[i]%M);if(z<p||z>5*p)return 0;}return 1;}
  if(j==255){ex++; int gok=1; for(int i=0;i<5;i++){int gg=M;for(int k=0;k<5;k++)if(k!=i)gg=g(gg,r[k]);if(gg!=1)gok=0;}
     int any=0; for(int jj=0;jj<M;jj++) if(safe(jj)){any=1;break;}
     if(gok||any) bad++; }
  else { if(j>=M||!safe(j)) bad++; else for(int jj=0;jj<j;jj++) if(safe(jj)){bad++;break;} }
 }
 if(fgetc(f)!=EOF){printf("trailing bytes\n");bad++;}
 printf("p=%d entries=%lld gcd_excluded=%lld BAD=%lld\n",p,tot,ex,bad);return 0;}
