import numpy as np
import matplotlib.pyplot as plt


x_list = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990]
y_list = [106.46, 123.08, 132.12, 152.27, 180.67, 205.05, 227.23, 249.46]

x_appx = 2000
y_gt = 281.42

def Lagrange_polynomial(x0, N=8, x = x_list, y = y_list):
    result = 0
    
    for i in range(N):
        val = y[i]
        for j in range(N):
            if i!=j:
                val = val * (x0 - x[j])/(x[i] - x[j])
        result += val
    return result

y_appx = Lagrange_polynomial(x_appx)
err = abs(y_gt - y_appx) / y_gt
print(y_appx, err*100)
