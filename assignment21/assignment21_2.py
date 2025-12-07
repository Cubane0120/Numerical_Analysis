import numpy as np
import matplotlib.pyplot as plt




A = np.array([[-3.00, 12.0],
              [ 10.0,-2.00]])

b = np.array([ 9.00, 8.00])

relaxation_factor = 1.2
stop_crietrion = 0.10

P = np.array([[0, 1],
              [1, 0]], dtype=int)

def JacobiMethod(A, b, x_0, e_stop, w=0):
    D = np.diag(A)
    B = D[:, None] - A

    x_prev = x_0
    print(f"initial\t x = {x_0}")
    err = 1.0

    i = 0
    while not np.all(err < e_stop):
        # x_appx = (1-w)*x_prev + w*Jacobi_1_iter(A, b, x_prev)
        x_appx, err = Jacobi_1_iter(A, b, x_prev, w)
        x_prev = x_appx
        print(f"iter {i}\t x = {x_appx}")
        print(f"\t e = {err}")
        i+= 1
    return x_appx
    
def Jacobi_1_iter(A, b, x_prev, w):
    x_appx = x_prev.copy()
    x_relx = x_prev.copy()
    err = x_prev.copy()
    for i in range(len(A[0])):
        A_i = A[i,:]
        D = A_i[i]
        B = -A_i.copy()
        B[i] = 0
        x_appx[i] = (B@x_relx + b[i])/D
        x_relx[i] = (1-w)*x_prev[i] + w*x_appx[i]
        # print(x_appx)
        # print(x_relx)
        # print("===============")
        
    err = np.abs((x_relx-x_prev)/x_relx)
    return x_relx, err


x_appx = JacobiMethod(P@A, P@b, np.array([0,0], dtype=np.float64), stop_crietrion, w = relaxation_factor)
print(x_appx)