#include <stdio.h>
int T[128][2],U[128][4],cnt[32],ch[8],nc[32],cb[32][128];long tot=0,mixc=0;FILE*fo;
void rec(int n,int lo,int li){
  if(n==8){for(int o=1;o<32;o+=2)if(cnt[o]!=2)return;
    tot++;{int a=0,b=0;for(int i=0;i<8;i++){int m=T[ch[i]][1]%8;if(m==1||m==7)a++;else b++;} if(a==8||b==8)return;} mixc++;for(int i=0;i<8;i++)fprintf(fo,"%d %d ",T[ch[i]][0],T[ch[i]][1]);fprintf(fo,"\n");return;}
  int o=-1;for(int x=1;x<32;x+=2)if(cnt[x]<2){o=x;break;} if(o<0)return;
  for(int i=(lo==o?li:0);i<nc[o];i++){int t=cb[o][i],ok=1;
    for(int j=0;j<4;j++)if(cnt[U[t][j]]>=2)ok=0; if(!ok)continue;
    for(int j=0;j<4;j++)cnt[U[t][j]]++; ch[n]=t; rec(n+1,o,i); for(int j=0;j<4;j++)cnt[U[t][j]]--;}
}
int main(){int k=0;for(int c=0;c<32;c+=2)for(int v=1;v<16;v+=2){T[k][0]=c;T[k][1]=v;int e[4]={1,-1,3,-3};
  for(int j=0;j<4;j++)U[k][j]=((c+e[j]*v)%32+32)%32; k++;}
 for(int t=0;t<128;t++)for(int j=0;j<4;j++){int o=U[t][j];cb[o][nc[o]++]=t;}
 fo=fopen("covers.txt","w");rec(0,-1,0);fclose(fo);printf("total %ld mixed %ld\n",tot,mixc);}
