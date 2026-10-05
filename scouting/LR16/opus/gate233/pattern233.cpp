#include <array>
#include <vector>
#include <map>
#include <iostream>
#include <cstdint>
#include <algorithm>
#include <chrono>
#include <stdexcept>
using Row=std::array<int,15>;
constexpr int P=233;
std::array<uint64_t,6> ones;
std::vector<Row> lift(const std::vector<Row>& parents,int oldlevel){
 int oldmod=oldlevel*P,M=2*oldmod;
 std::vector<Row> out;
 for(const auto&w:parents){
  std::array<uint64_t,512> live;live.fill(~uint64_t(0)); int remain=32768;
  if(oldlevel==1){
   unsigned parity=0; for(int i=0;i<15;i++) if(w[i]&1) parity|=1u<<i;
   for(unsigned b=0;b<32768;b++)if(__builtin_popcount(b^parity)<2){live[b>>6]&=~(uint64_t(1)<<(b&63));--remain;}
  }
  // Even grid numerators reduce to the parent's already rejected grid.
  // Odd numerator T and M-T have identical nearest-integer distances.
  for(int T=1;T<=oldmod && remain;T+=2){
   unsigned mask=0,value=0; bool impossible=false;
   for(int i=0;i<15;i++){
    int a=(int)((int64_t)T*w[i]%M); int b=(a+oldmod)%M;
    bool g0=16LL*std::min(a,M-a)>=M;
    bool g1=16LL*std::min(b,M-b)>=M;
    if(!g0&&!g1){impossible=true;break;}
    if(g0!=g1){mask|=1u<<i;if(g1)value|=1u<<i;}
   }
   if(impossible)continue;
   uint64_t low=~uint64_t(0);
   for(int i=0;i<6;i++)if(mask&(1u<<i))low&=(value&(1u<<i))?ones[i]:~ones[i];
   unsigned hm=mask>>6,hv=value>>6,free=(~hm)&511;
   unsigned s=free;
   do{
    unsigned j=hv|s;
    auto killed=live[j]&low;
    remain-=__builtin_popcountll(killed);live[j]^=killed;
    if(s==0)break;s=(s-1)&free;
   }while(true);
  }
  for(unsigned j=0;j<512;j++)while(live[j]){
   int bit=__builtin_ctzll(live[j]);unsigned bits=(j<<6)|bit;live[j]&=live[j]-1;
   Row r=w;for(int i=0;i<15;i++)if(bits&(1u<<i))r[i]+=oldmod;
   out.push_back(r);
  }
 }
 return out;
}
bool shift_ok(const Row&w,int d){
 // exact grid-count inequality: 8 * blocked < 8*d, without floats
 int forbidden=0;
 for(int u:w)if(u%d){int g=std::__gcd(u,d),q=d/g;forbidden+=g*((q+7)/8);}
 return forbidden<d;
}
bool direct_improper(const Row&w,int L){
 int odd=0;for(int u:w)odd+=u%2!=0;
 if(odd<2)return false;
 const int M=L*P;
 for(int T=0;T<M;T++){
  bool good=true;
  for(int u:w){int a=(int)((int64_t)T*u%M);if(16LL*std::min(a,M-a)<M){good=false;break;}}
  if(good)return false;
 }
 return true;
}

#include <sstream>
#include <string>
#include <map>
std::map<int,size_t> pat;
int main(){
 for(int i=0;i<6;i++)for(int x=0;x<64;x++)if(x&(1<<i))ones[i]|=uint64_t(1)<<x;
 std::string line; int rowno=0; size_t tot16=0, unh16=0; int rows_unhandled=0;
 while(std::getline(std::cin,line)){
  if(line.rfind("SURVIVOR base:",0)!=0) continue;
  std::istringstream is(line.substr(14)); Row r{}; for(int i=0;i<15;i++) is>>r[i];
  rowno++;
  std::vector<Row> current{r};
  for(int old=1;old<16;old*=2) current=lift(current,old);
  for(auto&w:current){int z=0,o=0;for(int u:w){z+=u%16==0;o+=u%2;} pat[z*16+o]++;}
  size_t unh=0; for(auto&w:current){bool ok=false;for(int d=2;d<=16;d*=2) if(shift_ok(w,d)){ok=true;break;} if(!ok){unh++; if(unh<=1){std::cout<<"UNHANDLED row "<<rowno<<":";for(int u:w)std::cout<<' '<<u;std::cout<<"\n";}}}
  tot16+=current.size(); unh16+=unh; if(unh) rows_unhandled++;
  std::cout<<"ROW "<<rowno<<" L16 "<<current.size()<<" unhandled "<<unh<<"\n";
 }
 for(auto&kv:pat)std::cout<<"PATTERN z16="<<kv.first/16<<" odd="<<kv.first%16<<" lifts "<<kv.second<<"\n";
 std::cout<<"TOTAL rows "<<rowno<<" level16_lifts "<<tot16<<" unhandled_lifts "<<unh16<<" rows_with_unhandled "<<rows_unhandled<<"\n";
}
