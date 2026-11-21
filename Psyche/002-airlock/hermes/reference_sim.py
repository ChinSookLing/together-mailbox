"""Reference simulator for airlock-v0.1 (Hermes). Bill: behaviour to match; not production code."""
import json,random,sys
T=json.load(open("airlock-v0.1-events.json"))
M=T["state"]["meters"]
def mulberry32(a):
    a&=0xffffffff
    def r():
        nonlocal a
        a=(a+0x6D2B79F5)&0xffffffff; t=a
        t=((t^(t>>15))*(t|1))&0xffffffff
        t^=(t+(((t^(t>>7))*(t|61))&0xffffffff))&0xffffffff
        return ((t^(t>>14))&0xffffffff)/4294967296
    return r
def tier(m,v,lang=0):
    for lo,hi,en,zh in M[m]["tiers"]:
        if lo<=v<=hi: return en if lang==0 else zh
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
def packet(seed,s,step,hours,lines,so_far,scene,opts,moves):
    o="".join(f'{x["key"]} {x["en"]}\n' for x in opts)
    return T["packet_template"].format(seed=seed,sol=min(step,7),step=step,water=tier("water",s["water"]),power=tier("power",s["power"]),dust=tier("dust",s["dust"]),seal=tier("seal",s["seal"]),hours=hours,lines=lines,so_far=so_far or "none",scene=scene,options=o,moves=moves)
def play(seed,chooser,show=False):
    r=mulberry32(seed); nights=[]
    for _ in range(6): w=1 if r()<0.4 else 0; p=1 if r()<0.4 else 0; nights.append((w,p))
    s=dict(T["state"]["start"]); flags=[]; moves=""; extra=""; maxlen=0; echo=None
    for n in range(1,8):
        d,v=sol_def(s,n)
        if v: echo=v["id"]; flags.append(v["flag"])
        lines=extra
        if "start_effects" in d: apply(s,d["start_effects"])
        if "start_line" in d: lines+=d["start_line"]["en"]+"\n"
        if s["water"]<=3 or s["power"]<=3 or s["dust"]>=6: lines+=T["state"]["shelter_line"]["en"]+"\n"
        opts=d["options"]
        p=packet(seed,s,n,4,lines,", ".join(T["state"]["so_far_labels"][x] for x in flags),d["scene"]["en"],opts,moves); maxlen=max(maxlen,len(p))
        if show and n in(1,5): print(p,"\n")
        c=chooser(opts)
        if c=="P": eff=T["sols"][0]["options"][1]["effects"]
        else: o=[x for x in opts if x["key"]==c][0]; eff=o["effects"]; f=o.get("flag"); f and flags.append(f)
        apply(s,eff); left=4+eff.get("time",0); moves+=c
        extra=""
        if left>=3: s["dust"]-=1; clamp(s); extra=T["state"]["vacuum_line"]["en"]+"\n"
        if n<7:
            w,p_=nights[n-1]; s["water"]-=w; s["power"]-=p_
            if s["dust"]>=4: s["water"]-=1
            clamp(s)
    return s,flags,echo,moves,maxlen
if __name__=="__main__":
    if len(sys.argv)>1: play(1,lambda o:o[0]["key"],show=True); sys.exit()
    import collections
    E=collections.Counter(); ML=0; shelter=0; tiers=collections.Counter()
    for seed in range(1,201):
        rnd=random.Random(seed)
        s,f,e,m,ml=play(seed,lambda o:rnd.choice([x["key"] for x in o]+(["P"] if rnd.random()<0.05 else [])))
        E[e]+=1; ML=max(ML,ml); tiers[(tier("water",s["water"]),tier("dust",s["dust"]))]+=1
    print("echo variants:",dict(E)); print("max packet chars:",ML); print("final water/dust:",tiers.most_common(8))
