#!/usr/bin/env python3
"""Puck four-eyes for PT-005 chair note 133 (written from scratch, 2026-11-09).
Approach (deliberately different from the chair's): read Allikvere's evidence15_<p>_s0.tgz
directly as tar streams in memory (no extraction), parse each member with my own regexes,
verify his MANIFEST_SHA256.json against the archive bytes, and compare per (r,s) with our
ir.jsonl files (strict json per line; duplicates of (r,s) are reported, never merged).
Usage: puck_allik4eyes.py <archdir> <inputs.tsv> <out.json>
inputs.tsv: p<TAB>side<TAB>path   (side in k11, off, k11km1)
"""
import sys, re, json, tarfile, hashlib, collections

LOG_RE = re.compile(r'^root=(\d+) sub=(\d+) raw_irred15=(\d+) rawscan=\d+ nodes=(\d+) ')
STAT_RE = re.compile(r'^TOTAL rows=(\d+) survivors=(\d+)\s*$', re.M)
FILE_RE = re.compile(r'(?:^|/)out15_(\d+)/(rows_ir|filt|rows_km1)/ir_(\d+)_(\d+)\.(txt\.log|txt|stats)$')
KM1_RE = re.compile(r'(?:^|/)out15_(\d+)/rows_km1/([^/]+)$')

def his_side(path, p):
    logs, txt_lines, stats, km1_files = {}, {}, {}, set()
    manifest = summary = None
    member_sha = {}
    with tarfile.open(path, 'r:gz') as tf:
        for m in tf:
            if not m.isfile():
                continue
            data = tf.extractfile(m).read()
            name = m.name
            mm = re.search(r'out15_%d/(.*)$' % p, name)
            if mm:
                member_sha[mm.group(1)] = hashlib.sha256(data).hexdigest()
            if name.endswith('out15_%d/MANIFEST_SHA256.json' % p):
                manifest = json.loads(data)
            elif name.endswith('out15_%d/SUMMARY.json' % p):
                summary = json.loads(data)
            k = KM1_RE.search(name)
            if k:
                km1_files.add(k.group(2))
            f = FILE_RE.search(name)
            if not f or int(f.group(1)) != p:
                continue
            kind, r, s, ext = f.group(2), int(f.group(3)), int(f.group(4)), f.group(5)
            if kind == 'rows_km1':
                continue
            key = (r, s)
            text = data.decode()
            if kind == 'rows_ir' and ext == 'txt.log':
                lines = [l for l in text.splitlines() if l.strip()]
                assert len(lines) == 1, (name, lines)
                g = LOG_RE.match(lines[0]); assert g, lines[0]
                assert (int(g.group(1)), int(g.group(2))) == key, name
                logs[key] = (int(g.group(3)), int(g.group(4)))
            elif kind == 'rows_ir' and ext == 'txt':
                txt_lines[key] = sum(1 for l in text.split('\n') if l.strip())
            elif kind == 'filt' and ext == 'stats':
                g = STAT_RE.findall(text); assert len(g) == 1, name
                stats[key] = (int(g[0][0]), int(g[0][1]))
    keys = set(logs)
    inner = []
    if set(txt_lines) != keys or set(stats) != keys:
        inner.append('job sets differ among log/txt/stats')
    for k in sorted(keys):
        lr = logs[k][0]
        if txt_lines.get(k) != lr or (stats.get(k) or (None,))[0] != lr:
            inner.append(('rows', k, lr, txt_lines.get(k), stats.get(k)))
    man_bad = [f for f, h in manifest.items() if member_sha.get(f) != h]
    bf = summary['base_family']
    jobs = {k: {'rows': logs[k][0], 'nodes': logs[k][1], 'surv': stats[k][1]} for k in keys}
    tot = lambda f: sum(v[f] for v in jobs.values())
    checks = {
        'bf_jobs_eq': bf['irredundant_jobs'] == len(jobs),
        'bf_rows_eq': bf['irredundant_rows'] == tot('rows'),
        'bf_nodes_eq': bf['irredundant_nodes'] == tot('nodes'),
        'l2surv_eq': bf['level2_survivor_rows_ir'] == tot('surv'),
        'cascade_surv_eq': summary['cascade']['survivor_rows'] == tot('surv') + bf.get('level2_survivor_rows_ext', 0),
    }
    return jobs, {
        'status': summary.get('status'), 'summary_base_family': bf,
        'manifest_entries': len(manifest), 'manifest_mismatch': man_bad,
        'km1_files_in_rows_km1': len(km1_files),
        'inner_mismatch': inner, 'summary_checks': checks,
    }

def our_side(path):
    jobs, dups, bad = {}, [], 0
    raw = open(path, 'rb').read()
    for i, line in enumerate(raw.decode().split('\n')):
        if not line.strip():
            continue
        o = json.loads(line)
        k = (int(o['r']), int(o['s']))
        v = {'rows': int(o['rows']), 'nodes': int(o['nodes']), 'surv': int(o['casc_survivors'])}
        if k in jobs:
            dups.append([k, jobs[k] == v])
        jobs[k] = v
    return jobs, dups, hashlib.sha256(raw).hexdigest()

def cmp(ours, his):
    d = []
    for k in sorted(set(ours) | set(his)):
        a, b = ours.get(k), his.get(k)
        if a != b:
            d.append({'job': list(k), 'ours': a, 'his': b})
    return d

def main():
    archdir, tsv, out = sys.argv[1:4]
    inp = collections.defaultdict(dict)
    for line in open(tsv):
        if line.strip() and not line.startswith('#'):
            p, side, path = line.rstrip('\n').split('\t')
            inp[int(p)][side] = path
    res = []
    for p in sorted(inp):
        his, meta = his_side('%s/evidence15_%d_s0.tgz' % (archdir, p), p)
        e = {'p': p, 'his_jobs': len(his),
             'his_sum_rows': sum(v['rows'] for v in his.values()),
             'his_sum_nodes': sum(v['nodes'] for v in his.values()),
             'his_sum_surv': sum(v['surv'] for v in his.values()), 'his_meta': meta}
        for side in ('k11', 'off'):
            if side in inp[p]:
                o, dups, h = our_side(inp[p][side])
                d = cmp(o, his)
                e[side] = {'file': inp[p][side], 'sha256': h, 'jobs': len(o), 'dup_lines': dups,
                           'sum_rows': sum(v['rows'] for v in o.values()),
                           'sum_nodes': sum(v['nodes'] for v in o.values()),
                           'sum_surv': sum(v['surv'] for v in o.values()),
                           'ndiff': len(d), 'diffs_first20': d[:20]}
        if 'k11km1' in inp[p]:
            km = json.load(open(inp[p]['k11km1']))
            bf = meta['summary_base_family']
            e['km1'] = {'ours_roots': km['roots'], 'ours_covers': km['covers'],
                        'his_km1_jobs': bf['km1_jobs'], 'his_rooted_covers': bf['km1_rooted_covers'],
                        'agree': km['roots'] == bf['km1_jobs'] and km['covers'] == bf['km1_rooted_covers']}
        if 'joblist' in inp[p]:
            jl = set()
            for l in open(inp[p]['joblist']):
                nums = re.findall(r'\d+', l)
                if len(nums) >= 2:
                    jl.add((int(nums[0]), int(nums[1])))
            o, _, _ = our_side(inp[p]['k11'])
            e['joblist'] = {'file': inp[p]['joblist'], 'distinct': len(jl),
                            'eq_k11': jl == set(o), 'eq_his': jl == set(his)}
        res.append(e)
        print(p, e['his_jobs'], e['his_sum_rows'], e['his_sum_nodes'], e['his_sum_surv'],
              'k11', e.get('k11', {}).get('ndiff'), 'off', e.get('off', {}).get('ndiff'),
              'inner', len(meta['inner_mismatch']), 'man', len(meta['manifest_mismatch']),
              all(meta['summary_checks'].values()), e.get('km1', {}).get('agree'),
              e.get('joblist'), flush=True)
    json.dump(res, open(out, 'w'), indent=1, sort_keys=True)

if __name__ == '__main__':
    main()
