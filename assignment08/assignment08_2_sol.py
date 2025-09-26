import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, y, z, l1, l2 = sp.symbols('x y z l1 l2')

f = 4*y - z

g1 = 2*x - y - z - 2
g2 = x**2 + y**2 - 1


L = f + l1*g1 + l2*g2

eqs = [sp.diff(L, var) for var in (x, y, z, l1, l2)]
sol_list = sp.solve(eqs, (x, y, z, l1, l2), dict=True)

print("해:")
for sol in sol_list:
    print("=============================")
    for var in (x, y, z, l1, l2):
        print(var, "=", sol[var].evalf())
