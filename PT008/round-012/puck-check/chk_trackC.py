from fractions import Fraction as F
import math
def d(x):
    f=x-math.floor(x); return min(f,1-f)
N=4; dl=F(1,N)
U=[F(1),F(19,10),F(301,100)]
m,M,w=U[0],U[1],U[2]
print('K_N cond M<=(N-1)^2 m/(N+1):',M<=F((N-1)**2,N+1)*m, ' (N-1)m=',(N-1)*m,' w<=(N-1)m?',w<=(N-1)*m)
print('G1 M<(N-1)m:',M<(N-1)*m)
den=(N-1)*m-M
print('G2 threshold 2mM/((N-1)m-M)=',float(2*m*M/den),' w>=thr?',w>=2*m*M/den)
tl=dl/m; X=w*tl
print('X=',float(X),'||X||=',float(d(X)),'<delta?',d(X)<dl)
k=math.floor(X+F(1,2)); t=(k+dl)/w
print('k',k,'t',float(t),[ (str(u),float(d(u*t))) for u in U],'ok',all(d(u*t)>=dl for u in U))
t2=F(9,4)/w
print('t=2.25/3.01',float(t2),[ (str(u),float(d(u*t2))) for u in U],'ok',all(d(u*t2)>=dl for u in U))
