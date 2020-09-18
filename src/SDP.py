import cvxpy as cp
import numpy as np


n = 3
#決定変数である行列Xnoサイズ
p = 2
#制約条件の個数


C = ([
    [1,2,3],
    [2,9,0],
    [3,0,7]
])

A = []
A.append(np.array([[1, 0, 1], [0, 3, 7], [1, 7, 5]]))
A.append(np.array([[0, 2, 8], [2, 6, 0], [8, 0, 4]]))

b = []
b.append(11)
b.append(19)

X = cp.Variable((n,n), symmetric=True)

obj = cp.Minimize(cp.trace(C@X))
cons = []
cons = [X >> 0]
cons += [cp.trace(A[i]@X) == b[i] for i in range(p)]

prob = cp.Problem(obj, cons)
prob.solve()


print("optimal value is ", prob.value)
print("A solution X is")
print(X.value)