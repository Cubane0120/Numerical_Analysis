import numpy as np
import matplotlib.pyplot as plt

def f(x, y, z):
    return 4*y - 2*z

def g1(x, y, z):
    return 2*x - y - z - 2

def g2(x, y, z):
    return x**2 + y**2 - 1


grid = np.linspace(-10, 10, 500)
X, Y, Z = np.meshgrid(grid, grid, grid)


f_list = f(X, Y, Z)
g1_list = g1(X, Y, Z)
g2_list = g2(X, Y, Z)

tol = 0.005
mask = (np.abs(g1_list) < tol) & (np.abs(g2_list) < tol)

x_sel = X[mask]
y_sel = Y[mask]
z_sel = Z[mask]
f_sel = f_list[mask]

idx = np.unravel_index(np.argmax(f_sel), f_sel.shape)
print(f"Max f value : {f_sel[idx]}, at x = {x_sel[idx]}, y = {y_sel[idx]}, z = {z_sel[idx]}")
idx = np.unravel_index(np.argmin(f_sel), f_sel.shape)
print(f"Min f value : {f_sel[idx]}, at x = {x_sel[idx]}, y = {y_sel[idx]}, z = {z_sel[idx]}")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
p = ax.scatter(x_sel, y_sel, z_sel, c=f_sel, cmap='viridis', s=5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

fig.savefig(f"fig_8.2.png", dpi=1200)