import numpy as np
import matplotlib.pyplot as plt

z_list = np.array([0, 0.2, 0.6, 1.2])
T_list = np.array([13.50, 11.25, 8.44, 6.14])
k = 0.5
dT_of_dz_gt = -13.5

q0_gt = -k * dT_of_dz_gt

def rel_err(approx, gt=q0_gt):
    return (gt - approx)/gt*100

def Lagrange_polynomial(x0, x, y, N=4):
    result = 0
    
    for i in range(N):
        val = y[i]
        for j in range(N):
            if i!=j:
                val = val * (x0 - x[j])/(x[i] - x[j])
        result += val
    return result

def approximate_q0(z, T, z0=0, h=0.001):
    def val_from_LargrangeP(z0):
        return Lagrange_polynomial(z0, z, T)
    
    derivate_val_from_LagrangeP = (val_from_LargrangeP(z0+h) - val_from_LargrangeP(z0-h))/(2*h)
    print(derivate_val_from_LagrangeP)
    return -k * derivate_val_from_LagrangeP

q0_approx = approximate_q0(z_list, T_list)
print(f"q0 value = {q0_approx}\t error : {rel_err(q0_approx)}%")