import numpy as np
import matplotlib.pyplot as plt

tot_A = 64

def c(a, b):
    if a==0 or b==0:
        return 0
    
    c_ = (tot_A//2 - a*b)/(a + b)
    
    if c_<0:
        return 0
    return c_
    
def V(a, b, c):
    if a<0 or b<0 or c<0:
        return 0
    
    return a*b*c

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = V(X[i, j], Y[i, j], c(X[i, j], Y[i, j]))

idx = np.unravel_index(np.argmax(Z), Z.shape)
print(f"Max Volume : {Z[idx]}, at a = {X[idx]}, b = {Y[idx]}, c = {c(X[idx], Y[idx])}")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

fig.savefig(f"fig_8.1.png", dpi=1200)