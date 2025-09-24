import numpy as np
import matplotlib.pyplot as plt


x_l = 0
x_u = 4

num_iter = 10


g_rate = (1 + np.sqrt(5)) / 2
print(g_rate)

def f(x):
    return (x**2)/10 - 2*np.sin(x)


x_list = []
y_list = []

for _ in range(num_iter):
    if x_l > x_u:
        raise ValueError
    d = (g_rate - 1) * (x_u - x_l)
    x_1 = x_l + d
    x_2 = x_u - d
    #print(x_l, x_u)
    #print(f(x_1), f(x_2), f(x_l), f(x_u))
    
    if f(x_1) < f(x_2):
        x_list.append(x_1)
        y_list.append(f(x_1))       
        x_l = x_2
    else:
        x_list.append(x_2)
        y_list.append(f(x_2))
        x_u = x_1
    
x_axis = [_+1 for _ in range(len(x_list))]

print(x_axis)
print(x_list)
print(y_list)

plt.figure()
plt.plot(x_axis, x_list, label='iteration_step vs x-value of minimum')
plt.xlabel('step')
plt.ylabel('x value')
plt.title('iteration_step vs x-value graph')
plt.legend()
plt.grid(True)
plt.savefig("fig_7.1.1_x.png", dpi=1200)
plt.figure()


plt.figure()
plt.plot(x_axis, y_list, label='iteration_step vs minimum value')
plt.xlabel('step')
plt.ylabel('f(x) value')
plt.title('iteration_step vs minimum value')
plt.legend()
plt.grid(True)
plt.savefig(f"fig_7.1.1_y.png", dpi=1200)
plt.figure()