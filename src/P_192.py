import numpy as np
import cvxpy as cp

x1, x2 = cp.Variable(), cp.Variable()
obj = cp.Maximize(2*x1 + x2)
cons = [
    2*x1 + x2 <= 2,
    x1 + 2*x2 >= 6,
    x1 + x2 <= 4,
    x1 >= 0,
    x2 >= 0
]

P = cp.Problem(obj, cons)
P.solve(verbose=True)
print("最適値")
print(P.value)
print("最適解")
print(x1.value, x2.value)