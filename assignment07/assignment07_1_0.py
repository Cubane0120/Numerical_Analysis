import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (x**2)/10 - 2*np.sin(x)


x_i = 0.00
x_f = 4.00
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
plt.savefig(f"fig_7.1.0.png", dpi=1200)
#sol m is 143