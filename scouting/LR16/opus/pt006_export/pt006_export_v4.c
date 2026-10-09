// PT006 test-run export (chair, PT005), p=223, K=13 cover search. See header line of output for the contract.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define P 223
#define N ((P-1)/2)
#define H ((P-1)/16)
#define K 13
#ifndef LIMIT
#define LIMIT 4000000000LL
#endif
typedef struct { uint64_t w[2]; } bs;
static bs cov[N+1]; static int cl[N+1][H], ncl[N+1];
static inline void bset(bs*b,int i){b->w[i>>6]|=1ULL<<(i&63);}
static inline int bt(const bs*b,int i){return (b->w[i>>6]>>(i&63))&1;}
static inline int pc(bs a){return __builtin_popcountll(a.w[0])+__builtin_popcountll(a.w[1]);}
static inline bs AND(bs a,bs b){a.w[0]&=b.w[0];a.w[1]&=b.w[1];return a;}
static inline bs OR(bs a,bs b){a.w[0]|=b.w[0];a.w[1]|=b.w[1];return a;}
static inline bs NOT(bs a){a.w[0]=~a.w[0];a.w[1]=~a.w[1];return a;}
static inline int Z(bs a){return !(a.w[0]|a.w[1]);}
static bs ALL; static int chosen[K], nch; static int path_t[K], path_v[K], path_i[K]; static long long nodes, s2; static int npr, nun;
static void pl(FILE*f,int*a,int m){fprintf(f,"[");for(int i=0;i<m;i++)fprintf(f,"%s%d",i?",":"",a[i]);fprintf(f,"]");}
static int npr_any,nun_any; static int s2_any_done(void){return npr_any>=8&&nun_any>=8;}
static void judge(bs X,bs U){
  int cand[N],nc=0; for(int v=1;v<=N;v++) if(!bt(&X,v) && !Z(AND(cov[v],U))) cand[nc++]=v;
  s2++; int small=(nc<=12); if(!small && s2_any_done()) return;
  int wit[2],nw=-1;
  if(Z(U)) nw=0;
  for(int i=0;i<nc&&nw<0;i++) if(Z(AND(U,NOT(cov[cand[i]])))){wit[0]=cand[i];nw=1;}
  for(int i=0;i<nc&&nw<0;i++) for(int j=i+1;j<nc&&nw<0;j++) if(Z(AND(U,NOT(OR(cov[cand[i]],cov[cand[j]]))))){wit[0]=cand[i];wit[1]=cand[j];nw=2;}
  int pruned=(nw<0); int want_small= small && (pruned? npr<8 : nun<8); int want_any= pruned? npr_any<8 : nun_any<8; if(!want_small && !want_any) return;
  bs un={{0,0}}; for(int i=0;i<nc;i++) un=OR(un,cov[cand[i]]);
  int mx=0; for(int i=0;i<nc;i++){int c=pc(AND(cov[cand[i]],U)); if(c>mx)mx=c;}
  int ucells[N],nu=0; for(int t=1;t<=N;t++) if(bt(&U,t)) ucells[nu++]=t;
  char reason[160];
  if(!pruned) strcpy(reason,"NOT_PRUNED");
  else { int orph=0; for(int t=1;t<=N;t++) if(bt(&U,t)&&!bt(&un,t)){orph=t;break;}
    if(orph) sprintf(reason,"ORPHAN: cell %d has no candidate",orph);
    else if(nu>2*mx) sprintf(reason,"COUNT: |U|=%d > slots*max_new=%d",nu,2*mx);
    else strcpy(reason,"EXHAUST: all 1 + n + n(n-1)/2 candidate sets checked"); }
  int nx=0; for(int v=1;v<=N;v++) if(bt(&X,v)) nx++;
  printf("{\"set\":\"%s\",\"slots2_node_index\":%lld,\"chosen\":", want_small?(want_any?"both":"small"):"any", s2); int cs[K]; memcpy(cs,chosen,sizeof cs);
  for(int i=0;i<nch;i++)for(int j=i+1;j<nch;j++)if(cs[j]<cs[i]){int t=cs[i];cs[i]=cs[j];cs[j]=t;}
  pl(stdout,cs,nch); printf(",\"slots\":2,\"excluded_or_used_count\":%d,\"uncovered\":",nx); pl(stdout,ucells,nu);
  { int ex[N],ne=0; bs ch={{0,0}}; for(int i=0;i<nch;i++) bset(&ch,chosen[i]); for(int v=1;v<=N;v++) if(bt(&X,v)&&!bt(&ch,v)) ex[ne++]=v; printf(",\"excluded\":"); pl(stdout,ex,ne); }
  printf(",\"path\":["); for(int i=0;i<nch;i++) printf("%s{\"cell\":%d,\"speed\":%d,\"index_in_cell_list\":%d}",i?",":"",path_t[i],path_v[i],path_i[i]); printf("]");
  printf(",\"candidates\":"); pl(stdout,cand,nc); printf(",\"pruned\":%s,\"reason\":\"%s\",\"witness\":",pruned?"true":"false",reason);
  if(pruned) printf("null"); else pl(stdout,wit,nw); printf("}\n"); fflush(stdout);
  if(want_small){ if(pruned) npr++; else nun++; } if(want_any){ if(pruned) npr_any++; else nun_any++; }
}
// X = speeds that may not be added any more (already chosen, or excluded by earlier branches)
/* v4: the three cut rules as functions; dfs and the regression harness call these same functions. */
static int rule_countH(bs U,int s){ return pc(U)>s*H; }                       /* |U| > slots*H  (strict) */
static int rule_maxnew(bs X,bs U,int s){ int mx=0; for(int v=1;v<=N;v++) if(!bt(&X,v)){int c=pc(AND(cov[v],U)); if(c>mx)mx=c;} return pc(U)>s*mx; } /* strict */
static int rule_orphan(bs X,bs U){ bs av={{0,0}}; for(int v=1;v<=N;v++) if(!bt(&X,v)) av=OR(av,cov[v]); return !Z(AND(U,NOT(av))); }
static int dfs(bs X,bs C){
  nodes++; if(npr>=8&&nun>=8) return 1; if((nodes&((1LL<<26)-1))==0) fprintf(stderr,"progress nodes=%lld s2=%lld small:%d/%d any:%d/%d\n",nodes,s2,npr,nun,npr_any,nun_any); if(nodes>LIMIT) return 1;
  bs U=AND(ALL,NOT(C)); int s=K-nch;
  if(Z(U)||s==0) return 0;
  if(rule_countH(U,s)) return 0;
  if(s==2){ judge(X,U); return 0; }
#ifdef MAXNEW
  if(rule_maxnew(X,U,s)) return 0;
#endif
  if(rule_orphan(X,U)) return 0;
  int t=1; while(!bt(&U,t)) t++;
  bs X2=X;
  for(int j=0;j<ncl[t];j++){ int v=cl[t][j]; if(bt(&X2,v)) continue;
    bset(&X2,v); path_t[nch]=t; path_v[nch]=v; path_i[nch]=j; chosen[nch++]=v;
    if(dfs(X2,OR(C,cov[v]))) return 1;
    nch--; }
  return 0;
}
static void init(void){
  memset(&ALL,0,sizeof ALL); for(int t=1;t<=N;t++) bset(&ALL,t);
  for(int v=1;v<=N;v++) for(int t=1;t<=N;t++){ int r=(v*t)%P; int d=r<P-r?r:P-r; if(16*d<P){ bset(&cov[v],t); cl[t][ncl[t]++]=v; } }
  }
#ifndef HARNESS
int main(){ init();
  bs X={{0,0}},C={{0,0}}; dfs(X,C);
  fprintf(stderr,"done(limit %lld) nodes",(long long)LIMIT); fprintf(stderr," nodes=%lld slots2_nodes=%lld pruned_out=%d unpruned_out=%d\n",nodes,s2,npr,nun);
}
#else

/* Regression harness: each stdin line is "ID slots | chosen ... | excluded ...". Prints the three cut rules exactly as
   dfs evaluates them, then a brute-force check over completions of size <= slots from the legal speeds. */
int main(){ init(); char line[8192];
  printf("id slots |U| countH maxnew orphan completions_le_slots pruned_truth\n");
  while(fgets(line,sizeof line,stdin)){
    char id[64]; int s; char*p=line; int k; if(sscanf(p,"%63s %d%n",id,&s,&k)!=2) continue; p+=k;
    bs C={{0,0}},X={{0,0}}; int part=0; int cs[N+1],nc=0;
    while(*p){ if(*p=='|'){part++;p++;continue;} if(*p>='0'&&*p<='9'){int v=strtol(p,&p,10); if(part==1){bset(&X,v);cs[nc++]=v;} else if(part==2) bset(&X,v);} else p++; }
    for(int i=0;i<nc;i++) C=OR(C,cov[cs[i]]);
    bs U=AND(ALL,NOT(C));
    int cand[N],m=0; for(int v=1;v<=N;v++) if(!bt(&X,v)&&!Z(AND(cov[v],U))) cand[m++]=v;
    long comp=0; if(Z(U)) comp=1;
    if(s>=1) for(int a=0;a<m;a++) if(Z(AND(U,NOT(cov[cand[a]])))) comp++;
    if(s>=2) for(int a=0;a<m;a++) for(int b=a+1;b<m;b++) if(Z(AND(U,NOT(OR(cov[cand[a]],cov[cand[b]]))))) comp++;
    printf("%s %d %d %d %d %d %ld %d\n",id,s,pc(U),rule_countH(U,s),rule_maxnew(X,U,s),rule_orphan(X,U),comp,comp==0);
  }
}
#endif
