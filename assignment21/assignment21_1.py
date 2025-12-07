import numpy as np
import matplotlib.pyplot as plt




A = np.array([[3.00,-0.10,-0.20],
              [0.10, 7.00,-0.30],
              [0.30,-0.20, 10.0]])

b = np.array([ 7.85,-19.3, 71.4])
x_gt = np.array([ 3.00,-2.50, 7.00])


def Gauss_Seidal(A, b, x_0, num_iter=5):
    D = np.diag(A)
    B = D[:, None] - A
    # print(A)
    # print(D)
    # print(B)
    x_prev = x_0
    print(f"initial\t x = {x_0}")
    for _ in range(num_iter):
        x_appx = Gauss_Seidal_1_iter(A, b, x_prev)
        x_prev = x_appx
        print(f"iter {_+1}\t x = {x_appx}")
    return x_appx
    
def Gauss_Seidal_1_iter(A, b, x_prev):
    x_appx = x_prev.copy()
    for i in range(len(A[0])):
        A_i = A[i,:]
        D = A_i[i]
        B = -A_i.copy()
        B[i] = 0
        
        # print(i, A_i, D, B, b)
        # print((B@x_appx + b[i])/D)
        x_appx[i] = (B@x_appx + b[i])/D
        # print(x_appx)
        # print("=====================")        
    # print(x_appx)
    return x_appx


x_appx = Gauss_Seidal(A, b, np.array([0,0,0], dtype=np.float64))
print(x_appx)