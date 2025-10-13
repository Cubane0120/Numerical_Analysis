import numpy as np
import matplotlib.pyplot as plt

iter_list = [2, 16, 128]
T = 1

w0 = 2*np.pi / T


def y_pred(t, i_series):
    val = 0
    for n in range(i_series):
        a = 4*n + 1
        b = 4*n + 3
        val += np.cos(w0*a*t) / a - np.cos(w0*b*t) / b
    
    return val * 4 / np.pi 
    

num_step = 200

for i, n_iter in enumerate(iter_list):
    x_axis = [-0.5 + i / num_step for i in range(num_step+1)]
    y_pred_list = [y_pred(x_val,n_iter) for x_val in x_axis]

    plt.figure()
    plt.plot(x_axis, y_pred_list, color="red", label=None)

    x = np.array([-0.5, -0.25, 0.25, 0.5])
    y = np.array([-1, 1, -1, -1])
    plt.hlines(y[:-1], x[:-1], x[1:], colors='C0')
    plt.vlines(x[1:], y[:-1], y[1:], colors='C0')

    plt.xlabel("t")
    plt.ylabel("y")
    plt.title(f"Continuous Fourier series (num of term = {2*n_iter})")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"fig_11.3_{i+1}.png", dpi=1200)
