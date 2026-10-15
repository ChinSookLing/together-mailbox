# Hesper sanity run behind hesper_P769_rerun_out.txt: all b for p=29,47,61; b in {2,3} for P=769,773.
# Uses realized() from hesper_r39_P769b.py (same folder). Note: the CLI of that script loops b in {2,3} only.
import importlib.util,sys,os
sys.argv=['x']
spec=importlib.util.spec_from_file_location('h',os.path.join(os.path.dirname(__file__),'hesper_r39_P769b.py'))
h=importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
U61=None
for p in (29,47,61):
    U=set()
    for b in range(1,(p+1)//2): U|=h.realized(p,b)
    print(p,"all b",len(U),flush=True)
    if p==61: U61=U
for P in (769,773):
    U=set()
    for b in (2,3): r=h.realized(P,b); U|=r; print(P,b,len(r),flush=True)
    print(P,"UNION",len(U),"equal to p61 set:",U==U61,flush=True)
