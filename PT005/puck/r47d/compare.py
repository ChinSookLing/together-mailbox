# Puck: compare Check A node set with chair's mislabel_open_children.jsonl and Puck's earlier mislabel_list.tsv; Check B table with chair full.out
import json,collections,re
mine={json.loads(l)['row']:json.loads(l) for l in open('checkA_nodes.jsonl')}
opus={json.loads(l)['row']:json.loads(l) for l in open('/workspace/mbx_pt5/PT005/opus/r47b_grade/mislabel_open_children.jsonl') if l.startswith('{')}
old=set(int(l.split('\t')[0]) for l in open('/workspace/mbx_pt5/PT005/puck/r47B/check/mislabel_list.tsv') if not l.startswith('row'))
print('A: mine',len(mine),'chair',len(opus),'puck r47B',len(old),'mine==chair',set(mine)==set(opus),'mine==puckr47B',set(mine)==old)
print('A: chair n_open nonzero',sum(o['n_open']!=0 for o in opus.values()),'chair p/M mismatches',sum((opus[r]['p'],opus[r]['M'])!=(mine[r]['p'],mine[r]['M']) for r in opus if r in mine))
print('A: min odd coords over all covering children',min(d['min_nodd'] for d in mine.values()))
print('A: L7 witness D/N (first even D|N closing each child, per node union):',collections.Counter(tuple(D*1.0/(2*d['M']) for D in d['l7_D']) for d in mine.values()).most_common(8))
print('A: covering choices per node: min',min(d['n_cover_choices'] for d in mine.values()),'max',max(d['n_cover_choices'] for d in mine.values()))
# B
ch={}
for l in open('/workspace/mbx_pt5/PT005/opus/r47d/full.out'):
    m=re.match(r'\((\d), (\d)\) odd\|U\|: (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)',l)
    if m: g=list(map(int,m.groups())); ch[(g[0],g[1])]=(g[2],g[3],g[4],g[5],g[6],g[7])
mm=0;n=0
for l in open('tableB.out'):
    f=l.split()
    if f and f[0] in('live','dead'):
        key=(int(f[0]=='dead'),int(f[1])); mine_=tuple(map(int,f[2:7])); c=ch[key]
        cc=(c[1],c[2],c[3],c[4],c[5]); n+=1
        if mine_!=cc or c[0]!=0: mm+=1; print('B MISMATCH',key,mine_,c)
print('B: cells compared',n,'rows',len(ch),'mismatching rows',mm)
