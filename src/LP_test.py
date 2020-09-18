import numpy as np
import cvxpy as cp


A = np.array([[3,2], [2, 6]])
b = np.array([5,8])
c = np.array([2,3])

x = cp.Variable(2)
#決定変数の次元
obj = cp.Minimize(c.T@x)
#目的関数
cons = [A@x >= b, x >= 0]
#制約条件
prob = cp.Problem(obj, cons)
prob.solve()


print("最適値:", prob.value)
print("最適解:")
print(x.value)
print("双対問題の最適解")
print(prob.constraints[0].dual_value)
