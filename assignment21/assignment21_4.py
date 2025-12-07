import numpy as np
import matplotlib.pyplot as plt


x_0 = np.array([1.5, 3.5])

def f(x):
    x1, x2 = x
    f1 = x1**2 + x1*x2 - 10
    f2 = x2 + 3*x1*(x2**2) - 57

    return np.array([f1, f2])

def J(x):
    x1, x2 = x
    
    f1_x1 = 2*x1 + x2
    f1_x2 = x1
    f2_x1 = 3*x2**2
    f2_x2 = 1 + 6*x1*x2
    
    return np.array([[f1_x1, f1_x2],
                     [f2_x1, f2_x2]])


def Newton_Raphson(x_0, num_iter):
    x_prev = x_0
    print(f"initial\t x : \n{x_0}")
    for _ in range(num_iter):
        J_mat = J(x_prev)
        det_J = np.linalg.det(J_mat)
        f_prev = f(x_prev)
        x_prev_1, x_prev_2 = x_prev
        
        x_appx_1 = x_prev_1 - np.linalg.det(np.column_stack((f_prev, J_mat[:, 1]))) / det_J
        x_appx_2 = x_prev_2 - np.linalg.det(np.column_stack((J_mat[:, 0], f_prev))) / det_J
        
        x_appx = np.array([x_appx_1, x_appx_2])
        x_prev = x_appx
        print(f"iter {_+1}\t x : \n{x_appx}")
    return x_appx
    

x_appx = Newton_Raphson(x_0, 5)
print(x_appx)