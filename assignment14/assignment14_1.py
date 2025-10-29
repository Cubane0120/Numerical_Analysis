import numpy as np
import matplotlib.pyplot as plt


x_list = [0, 20, 40]
y_list = [3.85, 0.800, 0.212]


def Lagrange_polynomial(x0, N=3, x = x_list, y = y_list):
    result = 0
    
    for i in range(N):
        val = y[i]
        for j in range(N):
            if i!=j:
                val = val * (x0 - x[j])/(x[i] - x[j])
        result += val
    return result

x_approx = 15

print(Lagrange_polynomial(15))