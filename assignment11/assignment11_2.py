import numpy as np
import matplotlib.pyplot as plt


def y_gt(t):
    return 1.7 + np.cos( 4.189*t + 1.0472)

w0 = 4.189 
dt = 0.15
N = 10

t = np.array([i*dt for i in range(N)])
y = np.array([y_gt(t) for t in t])

A0 = np.sum(y) / N
A1 = np.sum(y * np.cos(w0*t)) * 2 / N
B1 = np.sum(y * np.sin(w0*t)) * 2 / N

def y_pred(t):
    return A0 + A1*np.cos(w0*t) + B1*np.sin(w0*t)

def err(x_val, y_val):
    return y_val - y_pred(x_val)
def S_r(x_, y_):
    val = 0
    for i in range(0, N):
        val += (err(t[i], y[i]))**2
    return val

def S_t(y_):
    y_m = np.mean(y_)
    val=0
    for i in range(0, N):
        val += (y_[i] - y_m)**2
    return val

St = S_t(y)
Sr = S_r(t,y)

print(Sr)
print(St)
r_square = 1 - (Sr / St)
print(r_square)


num_step = 50
x_axis = [np.min(t) + (np.max(t) - np.min(t)) * i / num_step for i in range(num_step+1)]
y_gt_list = [y_gt(x_val) for x_val in x_axis]
y_pred_list = [y_pred(x_val) for x_val in x_axis]

equation_str_gt = f"y = 1.7 + cos(4.189 t + 1.0472)"
equation_str_pred = f"y = {A0:.3f} + {A1:.3f}cos(4.189*t) + {B1:.3f}sin(4.189*t)"

plt.figure()
plt.plot(x_axis, y_gt_list, color="red", label=equation_str_gt)
plt.plot(x_axis, y_pred_list, color="blue", label=equation_str_pred)

plt.xlabel("t")
plt.ylabel("y")
plt.title("Least-square fit of a Sinusoidal")
plt.grid(True)
plt.legend()

plt.savefig(f"fig_11.2_1.png", dpi=1200)


num_step = 200
x_axis = [0.50 + (0.02) * i / num_step for i in range(num_step+1)]
y_gt_list = [y_gt(x_val) for x_val in x_axis]
y_pred_list = [y_pred(x_val) for x_val in x_axis]

equation_str_gt = f"y = 1.7 + cos(4.189 t + 1.0472)"
equation_str_pred = f"y = {A0:.3f} + {A1:.3f}cos(4.189*t) + {B1:.3f}sin(4.189*t)"

plt.figure()
plt.plot(x_axis, y_gt_list, color="red", label=equation_str_gt)
plt.plot(x_axis, y_pred_list, color="blue", label=equation_str_pred)

plt.xlabel("t")
plt.ylabel("y")
plt.title("Least-square fit of a Sinusoidal")
plt.grid(True)
plt.legend()

plt.savefig(f"fig_11.2_2.png", dpi=1200)