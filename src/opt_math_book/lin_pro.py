import cvxpy as cp
import numpy as np

x1, x2 = cp.Variable(), cp.Variable()
obj = cp.Maximize(29*x1 + 45*x2)
cons = [
    2*x1 + 8*x2 <= 60,
    4*x1 + 4*x2 <= 60,
    x1 >=0,
    x2 >=0
]
#制約の記述

P = cp.Problem(obj, cons)
P.solve(verbose=True)
print(x1.value, x2.value)