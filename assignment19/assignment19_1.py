import numpy as np
import matplotlib.pyplot as plt


A = np.array([[0.30, 0.52, 1.00],
              [0.50, 1.00, 1.90],
              [0.10, 0.30, 0.50]])

b = np.array([-0.01, 0.67, -0.44])


def solving_with_cramer(A, b):
    D = np.linalg.det(A)
    
    x = np.zeros(len(b))
    for k in range(0,len(x)):
        A_new = A.copy()
        A_new[:,k] = b
        
        x[k] = np.linalg.det(A_new)/D

    return x


print(f"{{x}} = {solving_with_cramer(A,b)}")