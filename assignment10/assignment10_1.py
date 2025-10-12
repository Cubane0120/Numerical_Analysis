import numpy as np
import matplotlib.pyplot as plt


m = 2 # num of order = 2
x_ = np.array([0, 1, 2, 3, 4, 5])
y_ = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

n = len(x_)

x = x_.reshape(n,1)
y = y_.reshape(n,1)

def A_elem(i, j):
    if (i+j) == 0:
        return n
    else:
        return np.sum(x**(i+j))

def B_elem(i, j):
    if j != 0:
        raise ValueError()
    
    return np.sum(y * x**i)

A = np.fromfunction(np.vectorize(A_elem, otypes=[float]), (m+1, m+1))
B = np.fromfunction(np.vectorize(B_elem, otypes=[float]), (m+1, 1))

a = np.linalg.inv(A) @ B

def y_pred(x_val, a):
    val = 0
    for i in range(0,len(a)):
        val += a[i, 0] * x_val**(i)
    
    return val

for x_val in x:
    print(y_pred(x_val, a))

num_step = 50
x_axis = [np.min(x) + (np.max(x) - np.min(x)) * i / num_step for i in range(num_step+1)]
y_approx = [y_pred(x_val, a) for x_val in x_axis]


def err(x_val, y_val):
    return y_val - y_pred(x_val, a)
def S_r(x_, y_):
    val = 0
    for i in range(0, n):
        val += (err(x_[i], y_[i]))**2
    return val
def S_y_fraq_x(Sr, n, m):
    return np.sqrt( Sr / (n-(m+1)))
def S_t(y_):
    y_m = np.mean(y_)
    val=0
    for i in range(0, n):
        val += (y_[i] - y_m)**2
    return val


St = S_t(y_)
Sr = S_r(x_,y_)
print(Sr)
print(S_y_fraq_x(Sr, n, m))
r_square = 1 - (Sr / St)
print(r_square)

equation_str = f"y = {a[0,0]:.3f} + {a[1,0]:.3f}x + {a[2,0]:.3f}x^2"

plt.figure()
plt.scatter(x_, y_)
plt.plot(x_axis, y_approx, color="red", label=equation_str)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial regression")
plt.grid(True)
plt.legend()

plt.savefig(f"fig_10.1.png", dpi=1200)