from math import floor,ceil
def A(q): return [k for k in range(q) if 5*k>=q and 5*k<=4*q]
print("A7",A(7),len(A(7)),"3q/5",21/5); print("A6",A(6))
for r in (1,5): print("r",r,sorted({(r*j)%6 for j in A(6)}) )
print("A2",A(2))
