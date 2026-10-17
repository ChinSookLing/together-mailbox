# Second, separate verification of the two kill witnesses using the functions of Puck's earlier R43 checker
# (PT005/puck/r43/check/puck_r43_check.py, pure Python, literal COMMON definitions), not the numpy engine.
src=open("/workspace/mbx_pt5/PT005/puck/r43/check/puck_r43_check.py").read().split("# Grok p=17")[0]
exec(src)
def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c
def F(w,M,p,t):
    k=(M//p).bit_length()-1; return sum(1 for x in w if k-v2(x)>=t)
paths={
 "Astra p17":(17,[[1,1,1,2,3,3,3,4,5,5,6,7,7,8,8],[1,1,3,3,3,5,6,7,7,8,8,18,19,21,22],[1,1,3,3,5,7,7,8,18,19,22,37,40,42,55],
              [1,3,3,5,7,8,18,22,40,55,69,75,87,105,110],[1,3,5,7,8,69,75,87,139,154,158,176,191,241,246]]),
 "Grok p17":(17,[[8,11,11,15,3,5,15,11,7,16,1,15,16,3,13],[1,3,3,5,7,8,11,11,11,13,15,15,15,16,16],[1,3,5,7,8,11,11,13,15,16,37,45,49,49,50],
              [1,3,8,11,13,15,37,49,73,75,79,84,113,117,118],[1,13,15,79,84,118,139,144,147,173,185,209,211,249,253]]),
}
for name,(p,vs) in paths.items():
    print("==",name); M=p
    for i,w in enumerate(vs):
        lk = True if i==0 else lift_ok(sorted(vs[i-1]),w,M//2)
        print(f" level {M//p}p M={M} E={frozen(w,M,p)} F3={F(w,M,p,3)} F4={F(w,M,p,4)} odd={odd(w)} allT_covered={covered_all(w,M)} open={isopen(w,M)} lift_of_prev={lk}")
        if i>=3:
            for D,e,s,c in l7(w,M): print(f"    D={D} |E|={e} S={s} closed={c}")
        M*=2
