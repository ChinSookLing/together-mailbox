// p=223 gate part (b): extend each irredundant 14-cover (km1root, deduped) by one class v=1..111 (as filterext does),
// drop rows that contain a covering 13-subset (certified family-by-family in chair note 29), write the rest as 15-class rows.
#include <cstdio>
#include <cstring>
#include <vector>
#include <bitset>
#include <algorithm>
const int P=241, NC=120;
std::bitset<NC+1> cov[NC+1];
int hexv(char c){return c<='9'?c-'0':(c|32)-'a'+10;}
int main(int argc,char**argv){
  for(int v=1;v<=NC;v++)for(int t=1;t<=NC;t++){int r=v*t%P; if(16*std::min(r,P-r)<P) cov[v][t]=1;}
  FILE*in=fopen(argv[1],"r"); FILE*out=fopen(argv[2],"w"); char line[128];
  long long rows=0,kept=0,dropped=0,covers=0,badcover=0;
  std::bitset<NC+1> all; for(int t=1;t<=NC;t++) all[t]=1;
  while(fgets(line,sizeof line,in)){
    int len=strcspn(line,"\r\n"); if(len!=28) continue; covers++;
    int b[15]; for(int i=0;i<14;i++) b[i]=hexv(line[2*i])*16+hexv(line[2*i+1]);
    {std::bitset<NC+1> u; for(int i=0;i<14;i++) u|=cov[b[i]]; if(u!=all) badcover++;}
    for(int v=1;v<=NC;v++){
      b[14]=v; rows++;
      int m[NC+1]={0}; for(int i=0;i<15;i++) for(int t=1;t<=NC;t++) m[t]+=cov[b[i]][t];
      bool has13=false;
      for(int i=0;i<15&&!has13;i++)for(int j=i+1;j<15&&!has13;j++){
        bool ok=true; for(int t=1;t<=NC;t++) if(m[t]-cov[b[i]][t]-cov[b[j]][t]<=0){ok=false;break;}
        if(ok) has13=true;
      }
      if(has13){dropped++;continue;}
      int s[15]; memcpy(s,b,sizeof s); std::sort(s,s+15);
      for(int i=0;i<15;i++) fprintf(out,"%02x",s[i]); fputc('\n',out); kept++;
    }
  }
  fclose(out);
  printf("covers %lld (not covering: %lld) rows %lld dropped_with_13cover %lld kept %lld\n",covers,badcover,rows,dropped,kept);
}
