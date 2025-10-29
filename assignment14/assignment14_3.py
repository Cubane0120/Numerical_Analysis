import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / ( 1 + 25 * x**2)

def Make_P(DP, x_nodes, y_nodes):
    for i in range(0,N):
        DP[0][i] = y_nodes[i]
        for j in range(1, i+1):
            DP[j][i-j] = (DP[j-1][i-j+1] - DP[j-1][i-j]) / (x_nodes[i] - x_nodes[i-j])
            
def f_app(x, DP, x_nodes):
    result = 0
    term = 1
    for i in range(0,N):
        result += term * DP[i][0]
        term = term * (x-x_nodes[i])
    return result


num_step = 500
N_list = [4, 8, 16]
for i, N in enumerate(N_list):
    x_nodes = np.array([(-1 + 2*i/(N+1)) for i in range(1,N+1)])
    y_nodes = f(x_nodes)
    DP = [[0 for _ in range(N)] for _ in range(N)]
    Make_P(DP, x_nodes, y_nodes)
    
    
    x_axis = np.array([(-1 + 2*i/num_step) for i in range(num_step+1)])
    y_gts = f(x_axis)
    y_pred = [f_app(x,DP,x_nodes) for x in x_axis]

    plt.figure()
    plt.plot(x_axis, y_gts, color="blue", label=None)
    plt.plot(x_axis, y_pred, color="red", label=None)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"approximate results with equally-spaced nodes(N={N})")
    plt.grid(True)
    #plt.legend()
    plt.ylim(-0.1, 1.1)
    plt.savefig(f"fig_14.3_1_{i+1}.png", dpi=1200)


for i, N in enumerate(N_list):
    x_nodes = np.cos((2 * np.arange(1, N+1) - 1) * np.pi / (2 * N))
    y_nodes = f(x_nodes)
    DP = [[0 for _ in range(N)] for _ in range(N)]
    Make_P(DP, x_nodes, y_nodes)
    
    
    x_axis = np.array([(-1 + 2*i/num_step) for i in range(num_step+1)])
    y_gts = f(x_axis)
    y_pred = [f_app(x,DP,x_nodes) for x in x_axis]

    plt.figure()
    plt.plot(x_axis, y_gts, color="blue", label=None)
    plt.plot(x_axis, y_pred, color="red", label=None)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"approximate results with chebyshev nodes(N={N})")
    plt.grid(True)
    #plt.legend()
    plt.ylim(-0.1, 1.1)
    plt.savefig(f"fig_14.3_2_{i+1}.png", dpi=1200)
