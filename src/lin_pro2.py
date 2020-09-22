import cvxpy as cp
import numpy as np

x1, x2 = cp.Variable(), cp.Variable()
obj = cp.Maximize(150*x1 + 300*x2)
cons = [
    2*x1 + x2 <= 16,
    x1 + x2 <= 8,
    x2 <= 3.5
]

P = cp.Problem(obj, cons)
P.solve(verbose=True)
print("最適値")
print(P.value)
print("最適解")
print(x1.value, x2.value)