import numpy as np
import matplotlib.pyplot as plt




A = np.array([[ 40.0,-20.0, 0.00],
              [-20.0, 40.0,-20.0],
              [ 0.00,-20.0, 40.0]])



def PowerMethod(A, x_0, num_iter=10):
    print(f"initial\t x = {x_0}")
    x_prev, lam_prev = eigenVecVal(x_0)
    
    for _ in range(num_iter):
        x_appx, lam_appx = eigenVecVal(A @ x_prev)
        print(f"iter {_+1}\t x = {x_appx}")
        print(f"\t lambda = {lam_appx}")
        err = err_approx(lam_appx, lam_prev)
        print(f"\t e = {err}")
        
        x_prev, lam_prev = x_appx, lam_appx 
    return x_appx, lam_appx, err

def eigenVecVal(x):
    lam = x[np.argmax(np.abs(x))]
    x_norm = x/lam
    
    return x_norm, lam

def err_approx(curr, prev):
    return np.abs((curr - prev)/curr*100)



x_appx = PowerMethod(A, np.array([1,1,1], dtype=np.float64))
print(x_appx)