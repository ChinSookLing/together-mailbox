#include <array>
#include <vector>
#include <map>
#include <iostream>
#include <cstdint>
#include <algorithm>
#include <chrono>
#include <stdexcept>
using Row=std::array<int,15>;
constexpr int P=401;
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
int main(){
 for(int i=0;i<6;i++)for(int x=0;x<64;x++)if(x&(1<<i))ones[i]|=uint64_t(1)<<x;
 std::array<Row,5> rr={Row{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15},Row{1,2,3,4,5,6,7,8,9,10,11,12,13,15,28},Row{1,2,5,7,8,9,11,13,29,31,38,60,91,149,165},Row{1,5,7,8,9,11,13,19,29,48,60,79,118,139,185},Row{1,7,17,18,44,49,50,83,104,105,122,123,149,171,174}};
 for(int ri=0;ri<5;ri++){
  std::vector<Row> current{rr[ri]};
  for(int old=1;old<16;old*=2){
   auto start=std::chrono::steady_clock::now();int L=old*2;
   std::vector<Row> reference;
   size_t checked=current.size()*32768;
   for(const auto &parent:current)for(unsigned bits=0;bits<32768;bits++){
    Row w=parent;for(int i=0;i<15;i++)if(bits&(1u<<i))w[i]+=old*P;
    if(direct_improper(w,L))reference.push_back(w);
   }
   current=lift(current,old);
   std::sort(reference.begin(),reference.end());
   auto actual=current;std::sort(actual.begin(),actual.end());
   if(actual!=reference)throw std::runtime_error("full-grid child set mismatch");
   std::cout<<"DIRECT_GRID row="<<ri+1<<" level="<<L<<" all_children="<<checked<<" exact survivor sets compared: PASS"<<std::endl;
   if(L==2) for(const auto &w:current){std::cout<<"SURVIVOR row="<<ri+1<<" level="<<L<<":";for(int v:w)std::cout<<" "<<v;std::cout<<std::endl;}
   std::map<int,size_t> zhist,parityhist,covered_by; std::map<std::array<int,4>,size_t> h8; size_t notcovered=0;
   for(auto&w:current){
    int z=0,o=0;for(auto u:w){z+=u%L==0;o+=u%2!=0;}zhist[z]++;parityhist[o]++;
    std::array<int,4> hv{};for(auto u:w){if(u%2)hv[0]++;else if(u%4)hv[1]++;else if(u%8)hv[2]++;else hv[3]++;}h8[hv]++;
    bool covered=false;for(int d=2;d<=L;d*=2)if(shift_ok(w,d)){covered_by[d]++;covered=true;break;}
    if(!covered){notcovered++;if(notcovered<=2 && L>=16){std::cout<<"UNHANDLED row="<<ri+1<<" L="<<L<<" :";for(int u:w)std::cout<<' '<<u;std::cout<<'\n';}}
   }
   std::cout<<"ROW "<<ri+1<<" LEVEL "<<L<<" TOTAL "<<current.size()<<" ZERO_MOD_L";for(auto [z,c]:zhist)std::cout<<' '<<z<<':'<<c;
   std::cout<<" ODD_COUNT";for(auto [z,c]:parityhist)std::cout<<' '<<z<<':'<<c;
   std::cout<<" SHIFT_D_FIRST";for(auto [d,c]:covered_by)std::cout<<' '<<d<<':'<<c;
   std::cout<<" UNHANDLED "<<notcovered<<" seconds "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<std::endl;
   if(L>=8){std::cout<<"VAL8 row="<<ri+1<<" level="<<L<<" (odd,2mod4,4mod8,0mod8)";for(auto [h,c]:h8)std::cout<<" ["<<h[0]<<","<<h[1]<<","<<h[2]<<","<<h[3]<<"]:"<<c;std::cout<<std::endl;}
  }
 }
}
