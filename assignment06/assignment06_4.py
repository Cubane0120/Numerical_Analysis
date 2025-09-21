import numpy as np
import matplotlib.pyplot as plt

g_ = 9.81 #kg*m/s^2
c_d = 0.25 #kg/m
gt = 36.0 #velocity, m/s
ddx = 1e-6

x_0 = 50
x_1 = x_0

err_thd = 0.01 # %

def err(x_1, x_0):
    return np.abs((x_1-x_0) / x_1) * 100

def f(m): #v_at_t4(m):
    return np.sqrt(g_*m/c_d) * np.tanh(np.sqrt(g_*c_d/m) * 4) - gt

def df_of_dx(x):
    return (f(x+ddx*x) - f(x)) / (ddx * x)

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
    # print(err_val, x_1, f(x_1))
    
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
plt.savefig("fig_6.4_err.png", dpi=1200)
plt.figure()

plt.figure()
plt.plot(x_axis, y_list, label='iteration_step vs f(x)')
plt.xlabel('step')
plt.ylabel('f(x) when x=pseudo_root')
plt.title('iteration_step vs f(x) graph')
plt.legend()
plt.grid(True)
plt.savefig(f"fig_6.4_f(x).png", dpi=1200)
plt.figure()