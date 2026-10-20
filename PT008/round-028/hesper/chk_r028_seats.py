src=open('/workspace/work/pt008r20/hesper/base.py').read(); exec(src[:src.index("A=lambda")])
V=lambda *x:[F(v) for v in x]
def d(Vs,t): return [str(nd(v*t)) for v in Vs]
print('Qwen ex1 F4(1,3,4)=',F4(1,3,4),d(V(1,3,4),F4(1,3,4)))
a,b,c=V(1,F(21,10),F(63,20)); t=F4(a,b,c); print('Qwen ex2 F4=',t,d([a,b,c],t))
print('Qwen (1,3,4) j/4,j/5 fail:',all(min(nd(v*F(j,q)) for v in V(1,3,4))<F(1,4) for q in (4,5) for j in range(1,q+1)))
print('Qwen (1,2,4) j/5 fail:',all(min(nd(v*F(j,5)) for v in V(1,2,4))<F(1,4) for j in range(1,6)), '1/3',d(V(1,2,4),F(1,3)))
print('DS u=3: t0=1/3',d(V(1,2,3),F(1,3)),'t=1/4',d(V(1,2,3),F(1,4)),'5/12',d(V(1,2,3),F(5,12)),'mu/M',F(1,12)/2)
k=2;M=2;print('DS u bound',F(M*k*(k+1),2))
