# Chair check of Kimi's (PT005 line 10) shape-lemma formulas for n = 15. Not a proof.
import sympy as sp
t,u = sp.symbols('t u', positive=True)
n = 15
q = 1 + 2*t - t**2
H = (sp.Rational(1,2) + (n-1)*t**2/q) * 2 * q**(n-1) / t**sp.Rational(2*(n-1), n)
H_kimi = q**13 * (1 + 2*t + 27*t**2) / t**sp.Rational(28, 15)
print("H formula equal:", sp.simplify(H - H_kimi) == 0)
num = sp.factor(sp.together(sp.diff(sp.log(H_kimi), t)))
N = sp.numer(num); D = sp.denom(num)
print("log-derivative =", num)
kimi = -14 + 154*t + 210*t**2 + 4537*t**3 - 5292*t**4
print("Kimi numerator proportional:", sp.simplify(sp.expand(N) / kimi))
roots = [r for r in sp.Poly(kimi, t).nroots(n=30) if r.is_real and 0 < r < 1]
print("real roots in (0,1):", roots)
t0 = roots[0]
print("H(t0) =", sp.N(H_kimi.subs(t, t0), 15), " R15 =", sp.N(15/sp.sqrt(H_kimi.subs(t, t0)), 12))
alpha = (13 - sp.sqrt(113))/28
print("alpha_15 =", sp.N(alpha, 12), " t0 < alpha:", t0 < sp.N(alpha))
a = (1 + 2*u - u**2) / u**sp.Rational(2, 15)
crit = sp.solve(sp.diff(sp.log(a), u), u)
print("critical points of a(u):", [sp.N(c, 10) for c in crit], " a there:", [sp.N(a.subs(u, c), 10) for c in crit], " a(1) =", a.subs(u, 1))
print("4*(8/5)^13 =", sp.N(4*sp.Rational(8,5)**13, 10))
print("---- correction pass ----")
cub = 378*t**3 + 25*t**2 + 10*t - 1
print("expand (t-1)*cubic =", sp.expand((t-1)*cub), "; times -14 =", sp.expand(-14*(t-1)*cub))
r = [x for x in sp.Poly(cub, t).nroots(n=30) if x.is_real][0]
print("root of correct cubic t0 =", r, " H(t0) =", sp.N(H_kimi.subs(t, r), 15), " R15 =", sp.N(15/sp.sqrt(H_kimi.subs(t, r)), 12))
print("cubic increasing on (0,1): derivative 1134t^2+50t+10 > 0 always")
# rational bracket like the paper: increasing factors at lower end, decreasing t^(-28/15) at upper end
lo, hi = sp.Rational(724,10000), sp.Rational(725,10000)
print("cubic(lo) < 0 < cubic(hi):", cub.subs(t, lo) < 0 < cub.subs(t, hi))
qq = lambda x: 1 + 2*x - x**2
lb = qq(lo)**13 * (1 + 2*lo + 27*lo**2) / hi**sp.Rational(28,15)
print("rational-bracket lower bound for H(t0):", sp.N(lb, 12), " > 900:", lb > 900)
