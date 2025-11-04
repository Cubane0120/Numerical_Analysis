import numpy as np
import matplotlib.pyplot as plt


x_list = np.array([3.0, 4.5, 7.0, 9.0])
y_list = np.array([2.5, 1.0, 2.5, 0.5])


x_target = 5
n = len(x_list)
h_list = x_list[1:] - x_list[:-1]


def f(i, j):
    i, j = int(i), int(j)
    if i==0 or i==n-1:
        if i==j:
            return 1
        else:
            return 0
    else:
        if i==j+1:
            return h_list[i-1]
        if i==j:
            return 2*(h_list[i-1] + h_list[i])
        if i==j-1:
            return h_list[i]
        else:
            return 0

M = np.fromfunction(np.vectorize(f, otypes=[float]), (n, n))
A = y_list.reshape(-1,1)
# print(A)
df = (y_list[1:] - y_list[:-1]) / h_list
ddf = (df[1:] - df[:-1])*3
ddf_ = np.hstack(([0], ddf, [0]))
N = ddf_.reshape(-1, 1)

C = np.linalg.inv(M) @ N
B = df.reshape(-1,1) - h_list.reshape(-1,1)/3 * (2*C[:-1]+C[1:])
D = (C[1:] - C[:-1]) / 3 / h_list.reshape(-1,1) 
# print(D)
# print(C)

def find_adjacent(x0, x_list=x_list):
    min_i, max_i = 0, len(x_list)-1
    if x0 < x_list[min_i] or x0 > x_list[max_i]:
        raise "extrapolation"
    
    while (max_i - min_i) > 0:
        i = (min_i+max_i)//2
        if x0 < x_list[i]:
            max_i = i
        elif x0 > x_list[i+1]:
            min_i = i
        else:
            return i, x_list[i]
        
def calculate_y(x0):
    i, xi = find_adjacent(x0)
    
    return A[i] + B[i]*(x0-xi) + C[i]*(x0-xi)**2 + D[i]*(x0-xi)**3

print(calculate_y(x_target))

num_step = 60
x_axis = [np.min(x_list) + (np.max(x_list) - np.min(x_list)) * i / num_step for i in range(num_step+1)]
y_spline = [calculate_y(x_val) for x_val in x_axis]


plt.figure()
plt.plot(x_axis, y_spline, label="cubic splines")
plt.scatter(x_list, y_list, color="blue", label="given data")
plt.scatter(x_target, calculate_y(x_target), color="red", label="x=5")

plt.xlabel("x")
plt.ylabel("f")
plt.title("cubic splines")
plt.grid(True)
plt.legend()

plt.savefig(f"fig_15.3.png", dpi=1200)