import numpy as np
import matplotlib.pyplot as plt




A = np.array([[3.00,-0.10,-0.20],      
              [0.10, 7.00,-0.30],          
              [0.30,-0.20, 10.0]])


def MatrixInverse(A):
    n = len(A[0])
    LU, P = LU_Decomposition(A.copy())
    
    x = np.eye(n)
    x = Substitution_for_matrix_inverse(LU, P, x)

    return x
    
def LU_Decomposition(A):
    n = len(A[0])
    P = np.identity(len(A[0]))
    for k in range(0,n-1):
        Pivioting(A, P, k)

        for i in range(k+1,n):
            # print(piviot * M[i,k] / piviot[0] )
            A[i, k+1:] = A[i, k+1:] - A[k, k+1:] * A[i, k] / A[k, k] 
            A[i, k] = A[i, k] / A[k, k]            
            
    return A, P

def Pivioting(M, P, k):
    reference_val = np.abs(M[k:, 0])
    row_index = np.argmax(reference_val)

    if row_index != 0:
        M[[k, row_index], :] = M[[row_index, k], :]
        P[[k, row_index], :] = P[[row_index, k], :]
        

def Substitution_for_matrix_inverse(LU, P, x):
    n = len(LU[0])
    # print(x)
    U = np.triu(LU)
    L = np.tril(LU, k=-1) + np.eye(n)
    
    for i in range(0, n):
        b = x[:,i]
        d = Forward_Substitution(np.hstack([L, P @ b.reshape(-1, 1)]))
        # print(d)
        x[:,i] = Backward_Substitution(np.hstack([U, d.reshape(-1, 1)]))
        # print(x[:,i])
    
    return x

def Forward_Substitution(M):
    n = M.shape[0]
    x = np.zeros(n)
    for k in range(n):
        b_val = M[k, -1] - np.sum(M[k, :k] * x[:k])
        # print(x, M[k, k:n] * x[k:], x[k:])
        x[k] = b_val / M[k, k]
        # print(x)
    return x

def Backward_Substitution(M):
    n = M.shape[0]
    x = np.zeros(n)
    for k in range(n-1, -1, -1):
        b_val = M[k, -1] - np.sum(M[k, k:n] * x[k:])
        # print(x, M[k, k:n] * x[k:], x[k:])
        x[k] = b_val / M[k, k]
        # print(x)
    return x


A_inv = MatrixInverse(A)
pseudo_I = A @ A_inv
print(A_inv)
print(pseudo_I)