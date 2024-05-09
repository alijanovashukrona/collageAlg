import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')
# put the equetion here
eq = x**2-4

print("x = ", solve(eq,x))