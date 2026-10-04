# Chair (non-author) check of Kimi's shape-lemma proof for n=15 (PT005 line 31): derive the polynomials independently.
import sympy as sp
u, t, A = sp.symbols('u t A', positive=True)
n = 15
q = 1 + 2*u - u**2
L = q*(1 - (n-2)*u + (n-1)*u**2) / (n*u**2*(1+u))          # left side of (eq:crit)
num = sp.factor(sp.numer(sp.together(sp.diff(L, u))))
print("dL/du numerator (factored):", num)
P_kimi = 14*u**5 + 28*u**4 - 54*u**3 - 22*u**2 - 8*u + 2
print("dL/du numerator == -c*P_kimi for a positive constant c?", sp.simplify(sp.expand(num) / sp.expand(-P_kimi)))
a = q / u**sp.Rational(2, n)
print("critical points of a: roots of", sp.factor(sp.numer(sp.together(sp.diff(sp.log(a), u)))))
u1 = (13 - sp.sqrt(113)) / 28
print("u1 bounds 23/280 < u1 < 237/2800:", sp.Rational(23,280) < u1, u1 < sp.Rational(237,2800), "(via sqrt(113) < 10.7:", sp.Rational(107,10)**2 > 113, ", sqrt(113) > 10.63:", sp.Rational(1063,100)**2 < 113, ")")
qlo = 1 + 2*sp.Rational(23,280) - sp.Rational(23,280)**2
print("exact: a(u1) > 8/5  <=  q(23/280)^15 > (8/5)^15 * (237/2800)^2 :", qlo**15 > sp.Rational(8,5)**15 * sp.Rational(237,2800)**2)
H = (1 + 2*t + 27*t**2) * (1 + 2*t - t**2)**13 / t**sp.Rational(28, 15)
d = sp.factor(sp.together(sp.diff(sp.log(H), t)))
print("dlogH/dt =", d)
print("sign check: dlogH/dt has the SAME sign as the cubic on (0,1) (denominator 15t(t^2-2t-1)(...) < 0 and (t-1) < 0)")
