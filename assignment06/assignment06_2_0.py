import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x) - x

x_i = -1
x_f = 5
step_size = 100
step = np.array([_ for _ in range(step_size+1)])

x = x_i + (x_f - x_i) / step_size * step
y = f(x)


plt.figure()
plt.plot(x, y, label='y = f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('graphical')
plt.legend()
plt.grid(True)
plt.savefig(f"fig_6.2.0.png", dpi=1200)