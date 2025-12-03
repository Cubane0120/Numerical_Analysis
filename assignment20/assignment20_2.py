import numpy as np
import matplotlib.pyplot as plt


n = 3
i = np.arange(1, n+1)[:, None]
j = np.arange(1, n+1)[None, :]
H = 1.0 / (i + j - 1)
# print(H)


H = np.array([[  1, 1/2, 1/3],
              [1/2, 1/3, 1/4],
              [1/3, 1/4, 1/5]])

H_nor = H / H[:, 0].reshape(-1, 1)
H_inv = np.array([[  9,-18, 10],
                  [-36, 96,-60],
                  [ 30,-90, 60]])
# print(H_nor)    
def Matrix_L_inf_norm(M):
    norm = 0
    for i in range(0,len(M)):
        norm += vector_L_inf_norm(M[:,i])
    return norm
    
def vector_L_inf_norm(v):
    return np.max(np.abs(v))

Cond_H = Matrix_L_inf_norm(H_nor) * Matrix_L_inf_norm(H_inv)
print(Matrix_L_inf_norm(H_nor))
print(Matrix_L_inf_norm(H_inv))
print(Cond_H)