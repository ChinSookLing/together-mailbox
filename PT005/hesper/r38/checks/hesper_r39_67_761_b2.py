# Hesper: own solver (hesper_r39_P769b.realized, tests all 7,168 mixed doublable abstract configs) at b=2 for every prime 67..761.
import importlib.util,sys,json,os
sys.argv=['x']; here=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location('h',os.path.join(here,'hesper_r39_P769b.py')); h=importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
S=set(tuple(tuple(x) for x in k) for k in json.load(open(os.path.join(here,'hesper_U_769.json'))))
ps=[p for p in range(67,768) if all(p%q for q in range(2,int(p**.5)+1))]
bad=[p for p in ps if h.realized(p,2)!=S]
print("primes",len(ps),ps[0],"..",ps[-1],"b=2 realized set == 640-set at all:",not bad,"exceptions:",bad)
