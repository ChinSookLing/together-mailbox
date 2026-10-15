#include <stdio.h>
int T[128][2],U[128][4],cnt[32],ch[8],nc[32],cb[32][128];long tot=0,mixc=0;FILE*fo;

int kk(int c,int v,int s){int e[4]={1,-1,3,-3};for(int j=0;j<4;j++){int x=c+e[j]*v;if(((x%32)+32)%32==s){int d=s-x;return (d>=0? d/32 : -((-d+31)/32));}}return 0;}
int dbl(){int ea[32],eb[32],la[32],lb[32],ne[32];for(int o=0;o<32;o++)ne[o]=0;
 for(int i=0;i<8;i++){int c=T[ch[i]][0],v=T[ch[i]][1];for(int j=0;j<4;j++){int o=U[ch[i]][j];int k=kk(c,v,o);if(ne[o]==0){ea[o]=i;la[o]=k;}else{eb[o]=i;lb[o]=k;}ne[o]++;}}
 int pot[8];for(int i=0;i<8;i++)pot[i]=-1;
 for(int r=0;r<8;r++){if(pot[r]>=0)continue;pot[r]=0;int ch2=1;while(ch2){ch2=0;
  for(int o=1;o<32;o+=2){int a=ea[o],b=eb[o],l=((1+la[o]+lb[o])%2+2)%2;
   if(pot[a]>=0&&pot[b]<0){pot[b]=pot[a]^l;ch2=1;}else if(pot[b]>=0&&pot[a]<0){pot[a]=pot[b]^l;ch2=1;}
   else if(pot[a]>=0&&pot[b]>=0&&(pot[a]^pot[b])!=l)return 0;}}}
 return 1;}
void rec(int n,int lo,int li){
  if(n==8){for(int o=1;o<32;o+=2)if(cnt[o]!=2)return;
    tot++;{int a=0,b=0;for(int i=0;i<8;i++){int m=T[ch[i]][1]%8;if(m==1||m==7)a++;else b++;} if(a==8||b==8)return;} if(!dbl())return; mixc++;for(int i=0;i<8;i++)fprintf(fo,"%d %d ",T[ch[i]][0],T[ch[i]][1]);fprintf(fo,"\n");return;}
  int o=-1;for(int x=1;x<32;x+=2)if(cnt[x]<2){o=x;break;} if(o<0)return;
  for(int i=(lo==o?li:0);i<nc[o];i++){int t=cb[o][i],ok=1;
    for(int j=0;j<4;j++)if(cnt[U[t][j]]>=2)ok=0; if(!ok)continue;
    for(int j=0;j<4;j++)cnt[U[t][j]]++; ch[n]=t; rec(n+1,o,i); for(int j=0;j<4;j++)cnt[U[t][j]]--;}
}
int main(){int k=0;for(int c=0;c<32;c+=2)for(int v=1;v<16;v+=2){T[k][0]=c;T[k][1]=v;int e[4]={1,-1,3,-3};
  for(int j=0;j<4;j++)U[k][j]=((c+e[j]*v)%32+32)%32; k++;}
 for(int t=0;t<128;t++)for(int j=0;j<4;j++){int o=U[t][j];cb[o][nc[o]++]=t;}
 fo=fopen("covers.txt","w");rec(0,-1,0);fclose(fo);printf("total %ld mixed %ld\n",tot,mixc);}
