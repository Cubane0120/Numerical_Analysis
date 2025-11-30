import numpy as np
import matplotlib.pyplot as plt


A = np.array([[3.00,-0.10,-0.20],
              [0.10, 7.00,-0.30],
              [0.30,-0.20, 10.0]])

b = np.array([7.85,-19.3, 71.4])

def solving_with_Naive_Gauss_elimination(A, b):
    M = Forward_Elimination(A, b)
    x = Backward_Substitution(M)
    return x
    
def Forward_Elimination(A,b):
    M = np.hstack([A, b.reshape(-1, 1)])
    n = len(b)
    for k in range(0,n-1):
        piviot = M[k,k:]
        for i in range(k+1,n):
            # print(piviot * M[i,k] / piviot[0] )
            M[i,k+1:] = M[i,k+1:] - piviot[1:] * M[i,k] / piviot[0] 
            M[i,k] = 0
        # print(M)                
    return M

def Backward_Substitution(M):
    n = M.shape[0]
    x = np.zeros(n)
    for k in range(n-1, -1, -1):
        b_val = M[k, -1] - np.sum(M[k, k:n] * x[k:])
        # print(x, M[k, k:n] * x[k:], x[k:])
        x[k] = b_val / M[k, k]
        # print(x)
    return x
    
print(f"{{x}} = {solving_with_Naive_Gauss_elimination(A,b)}")