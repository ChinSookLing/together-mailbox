# Witness / example nodes: same stage-1 table and stage-2 direct code applied to single nodes.
import sys, numpy as np, pickle
sys.argv=['x']; sys.path.insert(0,'/workspace/work/r46')
from stage1 import share8
from stage2 import node_direct
sys.path.insert(0,'/workspace/work/r45'); from hesper_r45 import is_open_plain
def analyse(lab,p,M,w):
    w=sorted(w); W=np.array([w],np.int64); N=2*M; kp=(N//p).bit_length()-1
    L=np.stack([W,W+M],axis=2); S,d=share8(L,p,kp)
    same=(S[0,:,0,:]==S[0,:,1,:]).all(axis=1); Dz=tuple(int(j) for j in np.nonzero(~same)[0])
    A=S[0,same,0,:].sum(0)[None,:]
    for j in Dz: A=np.concatenate([A+S[0,j,0],A+S[0,j,1]],axis=0)
    mn=A.min(1); good=np.nonzero(mn>=8)[0]
    r=node_direct(w,M,Dz,good)
    return dict(label=lab,p=p,M=M,open_at_M=is_open_plain(w,M),F0=len(Dz),children_all_ge1=int(r['cand']),
                min_share8_range=(int(mn.min()),int(mn.max())),covered=r['covered'],viol=r['viol'],open=r['open'],
                open_distinct=r['open_distinct'],ovd_uncov=r['ovcov'],ovd_par=r['covdie_par'],ovd_L7=r['covdie_L7'])
if __name__=='__main__':
    R=[("witnessA_p17",17,136,[1,3,3,5,7,8,18,22,40,55,69,75,87,105,110]),
       ("witnessB_p17",17,136,[1,3,8,11,13,15,37,49,73,75,79,84,113,117,118]),
       ("GPT_p19_152",19,152,[39,59,41,61,43,101,121,8,47,125,145,15,73,55,37]),
       ("W5_p17_544",17,544,[189,224,72,447,176,500,144,128,384,266,80,64,48,32,16])]
    NODES=pickle.load(open('/workspace/work/r46/nodes.pkl','rb'))
    for lab,p,M,w in R:
        inset=any((row==sorted(w)).all() for row in NODES.get((p,M),(np.zeros((0,15)),))[0])
        print(analyse(lab,p,M,w),'in_trackA_set=',inset)
