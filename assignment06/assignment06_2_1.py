import numpy as np
import matplotlib.pyplot as plt


x_0 = 0
x_1 = x_0

err_thd = 0.01 # %

def err(x_1, x_0):
    return np.abs((x_1-x_0) / x_1) * 100

def f(x):
    return np.exp(-x) - x

def df_of_dx(x):
    return -np.exp(-x) - 1

def g(x):
    return x - f(x)/df_of_dx(x)

err_val = 1
err_list = []
y_list = []
while err_val > err_thd:
    x_0 = x_1
    x_1 = g(x_0)
    err_val = err(x_1, x_0)
    err_list.append(err_val)
    y_list.append(f(x_1))
    #print(err_val, x_1, f(x_1))
    
x_axis = [_+1 for _ in range(len(err_list))]

print("sol(root) : ", x_1)
print("f(x_roots) : ", f(x_1))

plt.figure()
plt.plot(x_axis, err_list, label='iteration_step vs error')
plt.xlabel('step')
plt.ylabel('error [%]')
plt.title('iteration_step vs error graph')
plt.legend()
plt.grid(True)
plt.savefig("fig_6.2.1_err.png", dpi=1200)
plt.figure()

plt.figure()
plt.plot(x_axis, y_list, label='iteration_step vs f(x)')
plt.xlabel('step')
plt.ylabel('f(x) when x=pseudo_root')
plt.title('iteration_step vs f(x) graph')
plt.legend()
plt.grid(True)
plt.savefig(f"fig_6.2.1_f(x).png", dpi=1200)
plt.figure()