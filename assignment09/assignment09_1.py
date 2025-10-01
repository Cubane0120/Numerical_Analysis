import numpy as np
import matplotlib.pyplot as plt


v = np.array([10, 20, 30, 40, 50, 60, 70, 80])
F = np.array([25, 75, 380, 550, 610, 1220, 830, 1450])

x=v
y=F

n = len(x)
x_m = np.mean(x)
y_m = np.mean(y)

a1 = (n * np.sum(x*y) - np.sum(x)*np.sum(y)) / (n * np.sum(x**2) - np.sum(x)**2 )
a0 = np.mean(y) - a1 * np.mean(x)

def y_reg(x):
    return a0 + a1*x    

y_approx = [y_reg(x_) for x_ in x]
print(a0, a1)

equation_str = f"y = {a0:.3f} + {a1:.3f}x"

plt.figure()
plt.scatter(x, y)
plt.plot(x, y_approx, color="red", label=equation_str)

plt.xlabel("v (m/s)")
plt.ylabel("F (N)")
plt.title("Curve Fitting (linear line)")
plt.grid(True)
plt.legend()
plt.savefig(f"fig_09.1.png", dpi=1200)