import numpy as np
import matplotlib.pyplot as plt


x_1 = 0
x_2 = 1
x_3 = 4

num_iter = 10

def f(x):
    return (x**2)/10 - 2*np.sin(x)

def g(x1, x2, x3):
    p = (x2 - x1)
    q = (x2 - x3)
    F_l = (f(x2) - f(x3))
    F_r = (f(x2) - f(x1))
    
    return x2 - (1/2) * (p**2 * F_l - q**2 * F_r) / (p * F_l - q*F_r)


x_list = []
y_list = []

for _ in range(num_iter):
    x_4 = g(x_1, x_2, x_3)
    
    x_list.append(x_4)
    y_list.append(f(x_4))
    
    x_1, x_2, x_3 = x_2, x_3, x_4
    

x_axis = [_+1 for _ in range(len(x_list))]

# print(x_axis)
# print(x_list)
# print(y_list)

plt.figure()
plt.plot(x_axis, x_list, label='iteration_step vs x-value of minimum')
plt.xlabel('step')
plt.ylabel('x value')
plt.title('iteration_step vs x-value graph')
plt.legend()
plt.grid(True)
plt.savefig("fig_7.2_x.png", dpi=1200)
plt.figure()


plt.figure()
plt.plot(x_axis, y_list, label='iteration_step vs minimum value')
plt.xlabel('step')
plt.ylabel('f(x) value')
plt.title('iteration_step vs minimum value')
plt.legend()
plt.grid(True)
plt.savefig(f"fig_7.2_y.png", dpi=1200)
plt.figure()