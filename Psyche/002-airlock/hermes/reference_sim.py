"""Reference simulator for airlock-v0.1 (Hermes), aligned 2026-11-21 with Bill's live engine.
Rules: PASS = that sol's B effects (B's flag is NOT set); an unoffered letter = NO MOVE (not applied, ask again);
step 8 = handover note (A honest, B 'All normal.', PASS blank); no shelter mode.
Usage: python3 reference_sim.py                -> 200 random weeks
       python3 reference_sim.py S1 AAB-CBD-AA [zh] -> replay one code, print ending (and last packet)"""
import json,random,sys,os
T=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"airlock-v0.1-events.json")))
M=T["state"]["meters"]; L={"en":0,"zh":1}
def mulberry32(a):
    a&=0xffffffff
    def r():
        nonlocal a
        a=(a+0x6D2B79F5)&0xffffffff; t=a
        t=((t^(t>>15))*(t|1))&0xffffffff
        t^=(t+(((t^(t>>7))*(t|61))&0xffffffff))&0xffffffff
        return ((t^(t>>14))&0xffffffff)/4294967296
    return r
def tier(m,v,lang="en"):
    for lo,hi,en,zh in M[m]["tiers"]:
        if lo<=v<=hi: return en if lang=="en" else zh
def clamp(s):
    for m in M: s[m]=max(M[m]["min"],min(M[m]["max"],s[m]))
def apply(s,eff):
    for k,v in eff.items():
        if k!="time": s[k]+=v
    clamp(s)
def sol_def(s,n):
    d=T["sols"][n-1]
    if d["id"]!="echo": return d,None
    for v in d["variants"]:
        c=v["condition"]
        if c.startswith("dust") and s["dust"]>=3: return v,v
        if c.startswith("seal") and s["seal"]>=2: return v,v
        if c=="otherwise": return v,v
class Game:
    def __init__(s,seed):
        s.seed=seed; r=mulberry32(int(str(seed).lstrip("S")))
        s.nights=[]
        for _ in range(6): w=1 if r()<0.4 else 0; p=1 if r()<0.4 else 0; s.nights.append((w,p))
        s.st=dict(T["state"]["start"]); s.flags=[]; s.moves=""; s.step=1; s.extra=[]; s.note=None; s.cur=None
        s._enter()
    def _enter(s):
        if s.step>7: s.cur=None; return
        d,v=sol_def(s.st,s.step)
        if v: s.flags.append(v["flag"])
        s.lines=list(s.extra)
        if "start_effects" in d: apply(s.st,d["start_effects"])
        if "start_line" in d: s.lines.append(d["start_line"])
        s.cur=d
    def offered(s):
        return [o["key"] for o in (s.cur["options"] if s.cur else T["step8"]["options"])]
    def move(s,c):
        if c=="PASS": c="P"
        if c!="P" and c not in s.offered(): return "NO MOVE"
        if s.step==8:
            s.note={"A":"honest","B":"normal","P":None}[c]; s.moves+=c; s.step=9; return "ok"
        opts=s.cur["options"]
        if c=="P": eff=[o for o in opts if o["key"]=="B"][0]["effects"]
        else:
            o=[o for o in opts if o["key"]==c][0]; eff=o["effects"]
            if o.get("flag"): s.flags.append(o["flag"])
        apply(s.st,eff); left=4+eff.get("time",0); s.moves+=c; s.extra=[]
        if left>=3: s.st["dust"]-=1; clamp(s.st); s.extra=[T["state"]["vacuum_line"]]
        if s.step<7:
            w,p=s.nights[s.step-1]; s.st["water"]-=w; s.st["power"]-=p
            if s.st["dust"]>=4: s.st["water"]-=1
            clamp(s.st)
        s.step+=1; s._enter(); return "ok"
    def replay(s):
        m=s.moves; return f"{s.seed}/airlock-v0.1/"+"-".join([m[0:3],m[3:6],m[6:8]][:1+(len(m)>3)+(len(m)>6)])
    def so_far(s,lang="en"):
        lab=T["state"]["so_far_labels" if lang=="en" else "so_far_labels_zh"]
        parts=[f"sol {i+1} {c}" if lang=="en" else f"第{i+1}天 {c}" for i,c in enumerate(s.moves[:7])]
        parts+= [lab[f] for f in s.flags]
        return "; ".join(parts) if parts else ("none" if lang=="en" else "無")
    def ending(s,lang="en"):
        E=T["ending"]; t=lambda m: tier(m,s.st[m],lang)
        out=[E["opening"][lang].format(water_tier=t("water"),power_tier=t("power"),dust_tier=t("dust"),seal_tier=t("seal"))]
        out+=[E["flag_lines"][f][lang] for f in s.flags if f in E["flag_lines"]]
        wp=s.st["water"]+s.st["power"]; d=s.st["dust"]
        k="kept_resources" if wp>=14 and d>=4 else "kept_clean" if d<=1 and wp<14 else "balance" if d<=3 and wp>=14 else "stretched"
        out.append(E["protected_let_go"]["lines"][k][lang])
        if s.note is None: out.append(E["note_line"]["blank"][lang])
        else:
            tpl=T["step8"]["options"][0 if s.note=="honest" else 1]["note_template"][lang]
            note=tpl.format(dust_tier=t("dust"),seal_tier=t("seal"),water_tier=t("water"),power_tier=t("power"),lesson="",lesson_zh="").strip()
            out.append(E["note_line"][lang].format(note=note))
        out.append(E["closing"][lang].format(replay=s.replay()))
        return ("" if lang=="zh" else " ").join(out)
def run(seed,code):
    g=Game(seed)
    for c in code.replace("-",""): 
        if g.move(c)!="ok": raise SystemExit(f"NO MOVE at step {g.step}: {c}")
    return g
if __name__=="__main__":
    if len(sys.argv)>=3:
        g=run(sys.argv[1],sys.argv[2]); lang=sys.argv[3] if len(sys.argv)>3 else "en"
        print(g.ending(lang)); sys.exit()
    import collections
    E=collections.Counter(); K=collections.Counter()
    for seed in range(1,201):
        rnd=random.Random(seed); g=Game(seed)
        while g.step<=8:
            g.move("P" if rnd.random()<0.05 else rnd.choice(g.offered()))
        E[[f for f in g.flags if f in("ade_cough","seal_hissed","five_sols_clean")][0]]+=1
        K[(tier("water",g.st["water"]),tier("dust",g.st["dust"]))]+=1
    print("echo:",dict(E)); print("final water/dust:",K.most_common(6))
