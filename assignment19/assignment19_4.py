import numpy as np
import matplotlib.pyplot as plt


A = np.array([[ 2.04,-1.00, 0.00, 0.00],
              [-1.00, 2.04,-1.00, 0.00],
              [ 0.00,-1.00, 2.04,-1.00],
              [ 0.00, 0.00,-1.00, 2.04]])

b = np.array([40.8, 0.80, 0.80,200.8])

def solving_with_Naive_Gauss_elimination(A, b, use_Pivioting=False):
    M = Forward_Elimination(A, b, use_Pivioting)
    x = Backward_Substitution(M)
    return x
    
def Forward_Elimination(A,b, use_Pivioting):
    M = np.hstack([A, b.reshape(-1, 1)])
    n = len(b)
    for k in range(0,n-1):
        piviot = Pivioting(M[k:,k:], use_Pivioting)
        for i in range(k+1,n):
            # print(piviot * M[i,k] / piviot[0] )
            M[i,k+1:] = M[i,k+1:] - piviot[1:] * M[i,k] / piviot[0] 
            M[i,k] = 0
        # print(M)                
    return M

def Pivioting(M, flag):
    if not flag:
        return M[0,:]

    reference_val = np.abs(M[:, 0])
    row_index = np.argmax(reference_val)

    if row_index != 0:
        M[[0, row_index], :] = M[[row_index, 0], :]
    return M[0, :]

def Backward_Substitution(M):
    n = M.shape[0]
    x = np.zeros(n)
    for k in range(n-1, -1, -1):
        b_val = M[k, -1] - np.sum(M[k, k:n] * x[k:])
        # print(x, M[k, k:n] * x[k:], x[k:])
        x[k] = b_val / M[k, k]
        # print(x)
    return x
    
print(f"{{x}} = {solving_with_Naive_Gauss_elimination(A,b, use_Pivioting=True)}")