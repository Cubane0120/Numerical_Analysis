import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_triangular


m = 3
x_ = np.array([0, 1, 2, 3, 4, 5])
y_ = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

n = len(x_) #6

x = x_.reshape(n,1)
y = y_.reshape(n,1)

def z(i, j):
    x_val = x_[int(i)]
    
    return x_val**(j)


Z = np.fromfunction(np.vectorize(z, otypes=[float]), (n, m))
A = Z.T @ Z
a_sp = np.linalg.inv(A) @ Z.T @ y

Q, R = np.linalg.qr(Z)
a_qr = solve_triangular(R, Q.T @ y, lower=False)

print(a_sp)
print(a_qr)

def y_pred(x_val, a):
    val = 0
    for i in range(0,len(a)):
        val += a[i, 0] * x_val**(i)
    
    return val

def err(x_val, y_val, a):
    return y_val - y_pred(x_val, a)
def S_r(x_, y_, a):
    val = 0
    for i in range(0, n):
        val += (err(x_[i], y_[i], a))**2
    return val
def S_y_fraq_x(Sr, n, m):
    return np.sqrt( Sr / (n-m))

def S_t(y_):
    y_m = np.mean(y_)
    val=0
    for i in range(0, n):
        val += (y_[i] - y_m)**2
    return val

St = S_t(y_)
Sr_sp = S_r(x_,y_,a_sp)
Sr_qr = S_r(x_,y_,a_qr)


r_square_sp = 1 - (Sr_sp / St)
r_square_qr = 1 - (Sr_qr / St)
print(r_square_sp)
print(r_square_qr)

print(r_square_sp - r_square_qr)

print(Sr_sp, Sr_qr)
print(Sr_sp-Sr_qr)