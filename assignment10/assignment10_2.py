import numpy as np
import matplotlib.pyplot as plt


m = 2 # num of order = 2
x0_ = np.array([1 for _ in range(0, 6)])
x1_ = np.array([0, 2, 2.5, 1, 4, 7])
x2_ = np.array([0, 1, 2, 3, 6, 2])
y_ = np.array([5, 10, 9, 0, 3, 27])

n = len(x1_)

x0 = x0_.reshape(n,1)
x1 = x1_.reshape(n,1)
x2 = x2_.reshape(n,1)
y = y_.reshape(n,1)

x_l = [x0, x1, x2]

def A_elem(i, j):
    if i==0 and j==0:
        return n
    else:
        return np.sum(x_l[int(i)] * x_l[int(j)])

def B_elem(i, j):
    if j != 0:
        raise ValueError()
    
    return np.sum(y * x_l[int(i)])

A = np.fromfunction(np.vectorize(A_elem, otypes=[float]), (m+1, m+1))
B = np.fromfunction(np.vectorize(B_elem, otypes=[float]), (m+1, 1))

a = np.linalg.inv(A) @ B

def y_pred(x1_val, x2_val, a):    
    return a[0, 0] + a[1, 0]*x1_val + a[2, 0]*x2_val

for i in range(0,n):
    print(y_pred(x1_[i], x2_[i], a))

print(a)