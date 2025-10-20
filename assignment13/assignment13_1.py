import numpy as np
import matplotlib.pyplot as plt


def bais_of_polynomial(x):
    return np.column_stack([x**2, x, x**0])


x_vals = np.array([300, 400, 500])
f_vals = np.array([0.616, 0.525, 0.457])
f_vals = f_vals.reshape(len(f_vals),1)


A = bais_of_polynomial(x_vals)
A_inv = np.linalg.inv(A)

print(A_inv @ f_vals)